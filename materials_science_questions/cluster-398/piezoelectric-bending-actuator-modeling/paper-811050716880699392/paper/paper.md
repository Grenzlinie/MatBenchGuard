TECHNICAL PAPER

# Deflection of circular diaphragm-type piezoactuators coupling with gas compression in micropumps

Yuanlin Hu¹ · Xin Liang¹ · Wen Wang¹

Received: 30 November 2016 / Accepted: 6 March 2017
© Springer-Verlag Berlin Heidelberg 2017

## Abstract
An analytical solution is formulated to predict the deflection of circular piezoactuators for the sake of gas compression in micropumps. The solution is derived from the energy minimization method and Rayleigh–Ritz method based on the Kirchhoff thin plate theory. Energy associated with the micropump includes elastic potential energy of the deflecting actuator, electric potential energy in the piezodiscs and compression work to gas. The proposed analytical solution is validated via the finite element simulations and experimental data. Furthermore, the effects of dimensions and material properties of the piezoactuator on the static pressure rise are discussed; there exist optimal radius ratio of the PZT layer to passive layer, optimal thickness ratio of the PZT layer to passive layer, and optimal ratio of the passive layer thickness to its radius, however, these optimal values are related to pressure load as well. Finally, the static pressure rise and the deflection profile of the piezoactuator have been discussed under the optimal dimensions.

## 1 Introduction
Micro electro mechanical systems (MEMS) have been widely applied in electric, chemical and biological devices, such as micropumps (Amirouche et al. 2009). Based on actuation mechanisms, micropumps are categorized as piezoelectric, electrostatic, pneumatic, electromagnetic, thermopneumatic, shape memory alloy and ultrasonic micropumps (Iverson and Garimella 2008), in which piezoelectric micropumps have demonstrated attractive performance due to advantages of high stroke force, fast reaction and low power consumption. According to the pumping fluid, the micropumps are classified to liquid micropumps and gas micropumps. Generally, the gas micropumps with check valves provide higher pressure rise and more linearly controllable flow rates (Li et al. 2005). The maximum pressure rise and deformation of the piezoactuator are necessary for designing a micropump. However, development of gas micropumps has lagged behind the liquid micropumps for the past decades, even though they are intensely required in the micro refrigeration and fuel cell systems (Laser and Santiago 2004; Nisar et al. 2008).

Normally, a piezoelectrically actuated gas micropump consists of a compression chamber, inlet and outlet check valves and an elastic diaphragm with a piezodisc, shown in Fig. 1. The piezodisc is bonded to the elastic diaphragm through a thin layer of epoxy resin, namely bonding layer. When a voltage is imposed on the piezodisc, its contraction or expansion in the radial and lateral directions induces a bending moment to the actuator, and results in a deformation. Such piezoelectric actuators can be termed as unimorph or bimorph one. The unimorph is that one side of the elastic diaphragm is bonded with a piece of piezodisc, while the bimorph is that both sides of the elastic diaphragm are bonded symmetrically with a piece of piezodisc. Reciprocal deformation of the actuator can lead to a cyclic compression and suction process. Stroke volume ratio caused by the deformation dominates the pressure rise and flow rate of a gas micropump. In the scope of developing high performance micropumps, a major objective is to design an actuator that is optimally suited for specific operating conditions (Herz et al. 2010). However, there was a

---

✉ Wen Wang
wenwang@sjtu.edu.cn

¹ Institute of Refrigeration and Cryogenics, School of Mechanical Engineering, Shanghai Jiao Tong University, Shanghai 200240, China

Fig. 1 Schematic of the PZT
actuator micropump

![](./images/811050716880699392_1.jpg)

little attention on optimizing the piezoactuator deflection coupling with gas compression through analytical solu- tions. Therefore, accurate analytical models are neces- sary for computing the deformations of such multilayered piezoactuators in the gas micropump in terms of the actua- tor dimensions, material properties, loads and boundary conditions.

Analytical solutions proposed in the literature to calcu- late deflection of the circular unimorph or bimorph type piezoactuators were mostly neglected the resisting gas pressure load during the compression. Dobrucki and Pruch- nicki (1997) investigated the deflection of a bimorph pie- zoactuator in the form of elastic shell of revolution based on the constitutive equations of piezoelectricity and the classic beam equations, which were solved with finite ele- ment method (FEM) and validated through the test of a flat circular plate bimorph. Prasad et al. (2006) constructed an analogical equivalent electrical circuit to predict the elec- tromechanical behavior of a clamped axisymmetric pie- zoelectric transducer (unimorph structure) based on the lumped parameter system; the piezoactuator is concluded as a linear, conservative and reciprocal transducer, moreo- ver, optimum configurations for maximum static displace- ment were presented. The bonding layer is relatively much thinner than other layers of the piezoactuator and often neglected before. Wang and Huo (2010) discussed the effect of the bonding layer on the circular unimorph deflec- tion, and their deflection model became satisfied when tak- ing the bonding layer into account as an individual layer. Optimization of an edge-clamped circular piezoelectric uni- morph was presented by Li and Chen (2003); they obtained analytical solutions based on the moments balancing by assuming a linear strain distribution along thickness of the elastic diaphragm, moreover, the optimal value of the elas- tic diaphragm thickness/diameter ratio was around 0.02. Using the similar method, Wang et al. (2007) developed an analytical solution on analyzing deflections of an annular piezoactuator applied in the droplet ejections; the solution was well validated through experimental data and FEM simulations after incorporating the residual stresses to the diaphragm. A circular piezoactuator applied to the valveless micropumps was analyzed by Cui et al. (2007), the deflec- tion model of the actuator was derived, and the influence of dimensions and material properties of the piezoactuator on the deflection were further investigated through FEM simu- lations, from which the optimal thickness ratio of the PZT layer to passive layer was around 0.8. Dong et al. (2007) studied a circular piezoactuator under a simple supported boundary condition with the elastic diaphragm entirely covered by piezoceramic; the impacts of geometric and material parameters on the static deflection were further discussed and the optimal ratio of thickness to diameter for the elastic layer was around 0.026. Deshpande and Sag- gere (2007) developed more detailed analytical closed form equations for a circular piezoelectric unimorph of partially piezoceramic covered on the elastic diaphragm. The equa- tions were based on the classical laminated plate theory (CLPT), and the results well agreed with the experimental data and FEM results. Incorporating the transverse forces, Herz et al. (2010) derived a solution for the transverse and radial displacement of a circular unimorph actuator under diverse loads with piezoceramic entirely and partially cov- ered on the elastic diaphragm. Based on the CLPT, Papila et al. (2008) studied edge-clamped circular composite uni- morph and bimorph plates with the piezoceramic shape of inner disc and outer ring; the circular bimorph structure had performance advantages in a proper dimension compared with the unimorph structure. The piezoactuators with the annular piezodisc applied for the nebulizers or atomizers were investigated by Samuel and En (2011); the analytical deflections with different packaging boundary constraint were validated through experiment data.

As for circular piezoactuated gas micropumps, several experimental and numerical investigations were reported

as well. Yoon et al. (2009) experimentally investigated a piezoactuated gas micropump with check valves through microfabrication techniques on silicon wafers, they observed that voltage had a stronger influence on the performance than frequency, which was different from the liquid micropump (Cheng and Tseng 2013; Singh et al. 2015). Kang and Auner (2011) discussed the relationship between the stroke volume and the backpressure of a square piezo diaphragm micropump with check valves through FEM analysis; they adopted the diaphragm average displacement concept, and observed a reversed deflection of the piezoactuator under certain backpressure.

Most publications above covered modeling efforts on the deformation of piezoelectric actuators either through CLPT analysis or FEM simulation, however, these piezoactuators rarely deflected under resisting gas pressure load during compression or propelling. There are insufficient reported analytical models to calculate the deflection of piezoactuator for the sake of gas compression and predict the static pressure rise of a piezoactuated gas micropump because of the complexity of electro-fluid-structural coupling.

Moreover, the optimization criterion in most publications focused on the center displacement of a diaphragm, which is an important factor for other types of actuators but is not suitable for that in gas micropumps, because the center displacement is a discrete data point and unable to comprehensively present volume stroke of a gas micropump (Kang and Auner 2011).

This paper makes efforts on an analytical solution to predict and optimize the deflection of piezoactuators coupling with the gas compression, the energy minimization method and Rayleigh-Ritz method is employed, which is more convenient to solve the electro-fluid-structural problems. The total energy associated with the solution includes elastic potential energy of the deflecting actuator, electric potential energy in the piezodiscs and compression work on gas. The elastic potential energy in both radial and lateral directions is considered for all layers (i.e. elastic layer, PZT layer and bonding layer) based on the Kirchhoff thin plate theory. The electric potential was assumed to be quadratic function along the PZT thickness to fulfill the Maxwell static electricity equation. The proposed analytical solution is validated both numerically through FEM simulation and experimentally through deflection measurements. Based on the analytical equations, a piezoelectric bimorph is further optimized under a criterion of the pressure rise, which is determined by the volume stroke ratio.

## 2 Analytical modeling

The typical piezoelectric multilayered diaphragm-type actuators are composed of passive layer, bonding layer and PZT layer, shown in Fig. 2. The basic idea is to convert the contraction or expansion in the PZT layer to a large bending displacement of the actuator in the transverse direction. The conversion is fulfilled through the bonding layer, which tightly glues the passive layer and PZT layer together. Both unimorph and bimorph type of piezoactuators are widely employed in the micropumps, shown in Fig. 3. The unimorph type has one PZT layer installed only on one side of the passive layer, while the bimorph type has two PZT layers symmetrically installed on both sides of the passive layer. The imposed electric fields in the two PZT layers of the bimorph are opposite to generate a larger force, resulting in a larger deflection. The piezoelectric actuators for most liquid micropumps are the unimorph type to avoid short circuit, while the gas micropumps are able to employ the bimorph type to generate larger displacement and actuation force. The deflection of the piezoactuator induces a decrease of chamber volume and then an increase of gas pressure. In this paper, analytical solutions are derived to directly predict the pressure rise in the chamber and the deflections for both unimorph and bimorph type actuators.

The radius of the PZT layers and bonding layers are $r_2$, and the radius of the passive layer is $r_1$, the thicknesses of the passive layer, bonding layers and PZT layers are $t_p$, $t_b$, and $t_{pzt}$. The subscript $p$, $b$, and $pzt$ represent the passive layer, the bonding layer, and the PZT layer, respectively. During the piezoactuator deflection, there exists a neutral plane with no transverse strain, and $h$ is the distance from the neutral plane to the bottom of the passive layer. The

![](./images/811050716880699392_2.jpg)

Fig. 2 Schematic of the circular diaphragm-type piezoactuator for gas micropumps

![](./images/811050716880699392_3.jpg)

Fig. 3 Two types circular diaphragm-type piezoactuators. a Non-symmetric unimorph type, b Symmetric bimorph type

actuator is rigidly edge-clamped on the passive layer in the micropump.

The minimization energy and Raleigh-Ritz method are employed to determine transverse displacement of the piezoactuator, and the stroke volume (i.e. gas pressure rise) is then obtained. The analytical equations are based on the following assumptions:

(1) Isotropic multilayer diaphragm and uniformly distributed properties; the PZT layers are polarized along z-direction.

(2) The deflection follows the Kirchhoff thin plate theory: (i) the normal stress and shear stress are neglected, i.e. $\sigma_{zz}=0$; (ii) elements remain perpendicular to the neutral surface after bending, i.e. $e_{rz}=e_{\theta z}=0$.

(3) Impact of the electrodes layer on the deflection is neglected since its thickness is less than $0.5\ \mu\text{m}$ (Arik et al. 2005); the viscoelastic nature of the bonding layers is neglected.

(4) Electric potential is assumed to be quadratic function along the PZT thickness and satisfy the Maxwell static electricity equation, i.e. $dD_{z}/dz=0$, where $D_{z}$ is the electric displacement.

(5) Compressed gas in the chamber is thought as the ideal gas at constant temperature; gas flow in the chamber is disregarded (Zhang and Wang 2011) and the pressure is uniformly distributed because the velocity of the piezoactuator is far less than the sound speed of the compressed gas; gas pressure outside the chamber is assumed to keep $P_{0}$ as constant.

### 2.1 Energy analysis for the piezoactuators

Elastic potential energy of the piezoactuator is determined from the strains and the stresses of all layers in both radial and lateral directions. Based on the Kirchhoff thin plate theory, radial displacement $(u_{r})$, lateral displacement $(u_{\theta})$, radial strain $(e_{r})$ and lateral strain $(e_{\theta})$ of the piezoactuators are defined:

$$
\left\{
\begin{aligned}
\frac{\partial w(r,\theta)}{\partial r}+\frac{\partial u_{r}}{\partial z}&=0 \\
\frac{\partial w(r,\theta)}{r\partial\theta}+\frac{\partial u_{\theta}}{\partial z}&=0
\end{aligned}
\right. \tag{1}
$$

$$
\left\{
\begin{aligned}
e_{r}=\frac{\partial u_{r}}{\partial r}&=-z\frac{d^{2}w}{dr^{2}} \\
e_{\theta}=\frac{u_{r}}{r}&=-z\frac{dw}{rdr}
\end{aligned}
\right. \tag{2}
$$

where $w(r,\theta)$ represents the transverse displacement.

According to the generalized Hook's Law, stresses in radial $(\sigma_{r,p})$ and lateral $(\sigma_{\theta,p})$ directions of the passive layer are calculated as

$$
\left\{
\begin{aligned}
\sigma_{r,p}&=\frac{E_{p}}{1-v_{p}^{2}}(e_{rr}+v_{p}e_{\theta}) \\
\sigma_{\theta,p}&=\frac{E_{p}}{1-v_{p}^{2}}(e_{\theta\theta}+v_{p}e_{r})
\end{aligned}
\right. \tag{3}
$$

where $E_{p}$ and $v_{p}$ are the Young's modulus and Poisson's ratio of the passive layer.

The thickness of the bonding layer is around $20\ \mu\text{m}$, which is significantly thinner than the passive layer

Microsyst Technol

and PZT layer, thus its viscoelastic nature is negligible.
Therefore, the stresses in radial ($\sigma_{r,b}$) and lateral ($\sigma_{\theta,b}$)
directions of the bonding layer are calculated as

$$
\left\{
\begin{aligned}
\sigma_{r,b} &= \frac{E_b}{1-v_b^2}(e_{rr} + v_b e_{\theta}) \\
\sigma_{\theta,b} &= \frac{E_b}{1-v_b^2}(e_{\theta\theta} + v_b e_r)
\end{aligned}
\right. \tag{4}
$$

According to the linear piezoelectric constitutive equa-
tions, stresses in radial ($\sigma_{r,b}$) and lateral ($\sigma_{\theta,b}$) directions
of the PZT layer are expressed as

$$
\left\{
\begin{aligned}
\sigma_{r,pzt} &= \frac{1}{s_{11}^E(1-v_{pzt}^2)}\left(e_r + v_{pzt} e_{\theta}\right) - \frac{d_{31}}{s_{11}^E(1-v_{pzt})}E_Z \\
\sigma_{\theta,pzt} &= \frac{1}{s_{11}^E(1-v_{pzt}^2)}\left(e_{\theta} + v_{pzt} e_r\right) - \frac{d_{31}}{s_{11}^E(1-v_{pzt})}E_Z
\end{aligned}
\right. \tag{5}
$$

where $v_{pzt} = -s_{12}^E/s_{12}^E s_{11}^E \cdot s_{11}^E$ is the Poisson's ratio of the
PZT material, $s_{12}^E$ and $s_{11}^E$ are the compliance constants of
the PZT material, $d_{31}$ is the piezoelectric constant. $E_z$ is
the electric field in the PZT layer.

During the deflection of the piezoactuators, a neutral
plane is defined where no transverse strain exists. The
location of the neutral plane for the multilayered com-
posite structure is obtained based on the moment balance,
shown as below:

$$
\begin{aligned}
\int_{-h}^{t_p-h} &\frac{E_p}{1 - v_p^2}zdz + \int_{t_p-h}^{t_p-h+t_b} \frac{E_b}{1 - v_b^2}zdz + \int_{t_p-h+t_b}^{t_p-h+t_b+t_{pzt}} \\
&\times \frac{1}{s_{11}^E(1 - v_{pzt}^2)}zdz = 0
\end{aligned} \tag{6}
$$

After expanding and simplifying all terms in the
Eq. (6), the distance from the neutral plane to the bottom
of the passive layer is obtained for the unimorph actua-
tor, expressed as Eq. (7), which is used by Li and Chen
(2003).

$$
h = \frac{1}{2}\frac{E_p t_p^2/\left(1 - v_p^2\right) + E_b\left[\left(t_b + t_p\right)^2 - t_p^2\right]/\left(1 - v_b^2\right) + \left[\left(t_{pzt} + t_b + t_p\right)^2 - \left(t_b + t_p\right)^2\right]/s_{11}^E\left(1 - v_{pzt}^2\right)}{E_p t_p/\left(1 - v_p^2\right) + E_b t_b/\left(1 - v_b^2\right) + t_{pzt}/\left[s_{11}^E\left(1 - v_{pzt}^2\right)\right]} \tag{7}
$$

When it comes to the bimorph, since the symmetric struc-
ture, $h = t_p/t_p 2.2$.

Electric potential ($\varphi$) distribution in the PZT layer is
assumed to be quadratic function expressed as

$$
\phi = a_0 + a_1 z + a_2 z^2 \tag{8}
$$

where $a_0, a_1, a_2$ are constants determined according to the
electric potential boundary condition and the Maxwell
equation.

The electric field strength ($E_z$) and electric displace-
ment ($D_z$) are calculated as

$$
\left\{
\begin{aligned}
E_z &= -\frac{d\varphi}{dz} = -a_1 - 2z a_2 \\
D_z &= d_{31}(\sigma_{r,pzt} + \sigma_{\theta,pzt}) + \varepsilon_{33} E_z
\end{aligned}
\right. \tag{9}
$$

where $\varepsilon_{33}$ is the dielectric constant of PZT material. To
fulfill the Maxwell static electricity equation, $dDz/dz = 0$.
The electric boundary voltage on the upper and the bot-
tom of PZT layer is $V_1$ and $V_2$. By substituting Eq. (5) to
Eq. (9) and combining the boundary conditions, the con-
stants for the electric potential ($\varphi$) are obtained as

$$
\left\{
\begin{aligned}
a_2 &= \frac{d_{31}}{4d_{31}^2 - 2s_{11}^E \varepsilon(1 - v_{pzt})}\left(\frac{d^2w}{dr^2} + \frac{dw}{rdr}\right) \\
a_1 &= \frac{V_1 - V_2}{t_{pzt}} - 2t a_2
\end{aligned}
\right. \tag{10}
$$

where $t = tp/2 + tb + t pzt/2$.

Based on the strains and stresses in radial and lateral
directions of the passive layer and bonding layer, their
elastic potential energy can be calculated through volume
integration of the layers. Elastic potential energy of the
passive layer is calculated as

$$
\begin{aligned}
U_p &= \int_{-h}^{t_p-h} \int_{0}^{r_1} \int_{0}^{2\pi} \frac{1}{2}(\sigma_{r,p} e_{r,p} + \sigma_{\theta,p} e_{\theta,p}) r dr d\theta dz \\
&= \frac{\pi E_p\left[\left(t_p - h\right)^3 + h^3\right]}{3(1 - v_p^2)} \int_{0}^{r_1} \\
&\quad \times \left[ r\left(\frac{d^2w}{dr^2}\right)^2 + 2v_p \frac{dw}{dr} \frac{d^2w}{dr^2} + \frac{1}{r}\left(\frac{dw}{dr}\right)^2 \right] dr \quad (11)
\end{aligned}
$$

Likewise, elastic potential energy of the bonding layer
is

$$
\begin{aligned}
U_b &= \int_{t_p-h}^{t_p+t_b-h} \int_{0}^{r_2} \int_{0}^{2\pi} \frac{1}{2}(\sigma_{r,b} e_{r,b} + \sigma_{\theta,b} e_{\theta,b}) r dr d\theta dz \\
&= \frac{\pi E_p\left[\left(t_p + t_b - h\right)^3 - \left(t_p - h\right)^3\right]}{3(1 - v_b^2)} \int_{0}^{r_2} \\
&\quad \times \left[ r\left(\frac{d^2w}{dr^2}\right)^2 + 2v_b \frac{dw}{dr} \frac{d^2w}{dr^2} + \frac{1}{r}\left(\frac{dw}{dr}\right)^2 \right] dr \quad (12)
\end{aligned}
$$

There is only one bonding layer in the unimorph struc-
ture, while two bonding layers in the bimorph structure,

![](./images/811050716880699392_4.jpg)

thus the elastic potential energy of the bonding layer is doubled for the bimorph type piezoactuator.

The energy in the PZT layer is comprised of two parts, (1) the elastic potential energy because of the deformation; (2) the electric potential energy because of the imposed voltage. The elastic potential energy of the PZT layer is calculated as

$$
\begin{aligned}
U_{p z t}= & \int_{t_{p}+t_{b}-h}^{t_{p}+t_{b}+t_{p z t}-h} \int_{0}^{r_{2}} \int_{0}^{2 \pi} \frac{1}{2}\left(\sigma_{r, p z t} e_{r, b}+\sigma_{\theta, p z t} e_{\theta, b}\right) r d r d \theta d z \\
= & \frac{\pi\left[\left(t_{p}+t_{b}+t_{p z t}-h\right)^{3}-\left(t_{p}+t_{b}-h\right)^{3}\right]}{3 s_{11}^{E}\left(1-v_{p z t}^{2}\right)} \\
& \times \int_{0}^{r_{2}}\left[r\left(\frac{d^{2} w}{d r^{2}}\right)^{2}+2 v_{b} \frac{d w}{d r} \frac{d^{2} w}{d r^{2}}+\frac{1}{r}\left(\frac{d w}{d r}\right)^{2}\right] d r \\
& -\frac{2 \pi d_{31}\left[\left(t_{p}+t_{b}+t_{p z t}-h\right)^{3}-\left(t_{p}+t_{b}-h\right)^{3}\right]}{3 s_{11}^{E}\left(1-v_{p z t}\right)} \\
& \times \int_{0}^{r_{2}}\left(r \frac{d^{2} w}{d r^{2}}+\frac{d w}{d r}\right) a_{2} d r \\
& -\frac{\pi d_{31}\left[\left(t_{p}+t_{b}+t_{p z t}-h\right)^{2}-\left(t_{p}+t_{b}-h\right)^{2}\right]}{2 s_{11}^{E}\left(1-v_{p z t}\right)} \\
& \times \int_{0}^{r_{2}}\left(r \frac{d^{2} w}{d r^{2}}+\frac{d w}{d r}\right) a_{1} d r
\end{aligned}
$$

The electric potential energy of the PZT layer with electric field is

$$
\begin{aligned}
U_{E}= & \int_{t_{p}+t_{b}-h}^{t_{p}+t_{b}-h+t_{p z t}} \int_{0}^{r_{2}} \int_{0}^{2 \pi} \frac{1}{2} E_{z} D_{z} r d r d \theta d z \\
= & \left(\pi \varepsilon_{33}-\frac{2 \pi d_{31}^{2}}{s_{11}^{E}\left(1-v_{p z t}\right)}\right) \int_{t_{p}+t_{b}-h}^{t_{p}+t_{b}-h+t_{p z t}} \\
& \times \int_{0}^{r_{2}}\left(a_{1}^{2}+4 z a_{1} a_{2}+4 z^{2} a_{2}^{2}\right) r d r d z \\
& +\frac{\pi d_{31}^{2}}{s_{11}^{E}\left(1-v_{p z t}\right)} \int_{t_{p}+t_{b}-h}^{t_{p}+t_{b}-h+t_{p z t}} \\
& \times \int_{0}^{r_{2}} z\left(a_{1}+2 z a_{2}\right)\left(\frac{d^{2} w}{d r^{2}}+\frac{1}{r} \frac{d w}{d r}\right) r d r d z
\end{aligned}
$$

Likewise, the $U_{p z t}$ and $U_{E}$ should be doubled for the bimorph structure.

The total energy of the deflected structure reaches the minimum value in the equilibrium state. According to the Rayleigh-Ritz method, the potential function of the piezoactuator deflecting without any pressure load is expressed as

$$
L=U_{p}+U_{b}+U_{p z t}-U_{E}
$$

The piezoactuator is rigidly clamped around its circumference and asymmetric with $\theta$. On the boundary,

$$
\left.w\right|_{r=r_{1}}=0,\left.\quad \frac{d w}{d r}\right|_{r=r_{1}}=0, \frac{\partial w}{\partial \theta}=0
$$

The transverse displacement of the piezoactuator is general expressed in the form of power series,

$$
\left\{\begin{aligned}
w(r) & =\left(1-\frac{r^{2}}{r_{1}^{2}}\right)^{2}\left[\sum_{i=1}^{n} C_{i}\left(1-\frac{r^{2}}{r_{1}^{2}}\right)^{i-1}+R(n)\right] \\
R(n) & =\frac{\left(1-r^{2} / r_{1}^{2}\right)^{n+1}}{(n+1)!} w^{(n+1)}(\xi)
\end{aligned}\right.
$$

where $R(n)$ is the remainder term of the series. Substituting the Eqs. (11)-(14) and (17) into Eq. (15), the factors $C_{i}$ in the power series are determined by the equations: $\partial L / \partial C_{i}=0,(i=1,2,3, \ldots, n)$. Then, the transverse displacement of the edge-clamped piezoactuator is obtained. Moreover, the $w(r)$ is investigated with different degrees $(n)$, and the deflection results are stable when $n \geq 3$; we take $n=4$ in the calculations.

### 2.2 Gas compression process

The clamped piezoactuator and cylinder cavity makes up a sealed compression chamber, depicted in Fig. 4. The initial gas pressure and volume inside the chamber are $P_{0}$ and $V_{0}$. When a voltage is imposed on the piezoactuator, it deforms to decrease the gas volume, and simultaneously the gas pressure increases, $P V=$ constant, where $P$ and $V$ are gas pressure and gas volume. The pressure outside the chamber is supposed as constant $P_{0}$, thus compression work done by the surrounding is $P_{0}\left(V_{0}-V\right)$. Therefore, the gas compression work done by the piezoactuator is expressed as

$$
\begin{aligned}
U_{g a s} & =-W_{g}=-\int_{V_{0}}^{V} P d V-P_{0}\left(V_{0}-V\right) \\
& =P_{0} V_{0} \ln \left(V_{0} / V\right)-P_{0}\left(V_{0}-V\right)
\end{aligned}
$$

When the piezoactuator is subjected to a uniform pressure load, the flow work done by the actuator is

$$
U_{\text {gas }}=\left(P-P_{0}\right)\left(V_{0}-V\right)
$$

Initial volume of the cylinder chamber can be calculated as $V_{0}=H_{c} \pi r_{1}^{2}$, where $H_{c}$ and $r_{1}$ are the depth and inner radius of the cavity. The volume $(V)$ during compression is

$$
V=\int_{0}^{r_{1}} 2 \pi r\left(w-H_{c}\right) d r
$$

The $U_{\text {gas }}$ is a function of the $w$, which can be obtained through the Raleigh-Ritz method. As a functional problem,

![](./images/811050716880699392_5.jpg)

![](./images/811050716880699392_6.jpg)

Fig. 4 Schematic of the gas compression for the gas micropump. a Initial compression state, b Equilibrium compression state

<table>
<thead>
<tr>
<th>Layer</th>
<th>Dimension (radius × thickness)</th>
<th>Material properties</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>PZT-5A</td>
<td>12 mm × 100 μm</td>
<td>Piezoelectricity $e$ (C/m)</td>
<td>$$\begin{bmatrix} 0 & 0 & -5.4 \\ 0 & 0 & -5.4 \\ 0 & 0 & 15.8 \\ 0 & 12.3 & 0 \\ 12.3 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Permittivity (F/m)</td>
<td>$$\begin{bmatrix} 8.107 & 0 & 0 \\ 0 & 8.107 & 0 \\ 0 & 0 & 7.346 \end{bmatrix} \times 10^{-9}$$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Compliance $S$ (m²/N)</td>
<td>$$\begin{bmatrix} 16.4 & -5.75 & -8.45 & 0 & 0 & 0 \\ -5.75 & 16.4 & -8.45 & 0 & 0 & 0 \\ -8.45 & -8.45 & 18.8 & 0 & 0 & 0 \\ 0 & 0 & 0 & 44.3 & 0 & 0 \\ 0 & 0 & 0 & 0 & 47.5 & 0 \\ 0 & 0 & 0 & 0 & 0 & 47.5 \end{bmatrix} \times 10^{-12}$$</td>
</tr>
<tr>
<td>Brass</td>
<td>15 mm × 150 μm</td>
<td>Young's modulus (GPa)</td>
<td>100</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Poisson's ratio</td>
<td>0.27</td>
</tr>
<tr>
<td>Epoxy</td>
<td>12 mm × 20 μm</td>
<td>Young's modulus (GPa)</td>
<td>5.17</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Poisson's ratio</td>
<td>0.3</td>
</tr>
</tbody>
</table>

Table 2 Geometric and
material parameters for various
layers of the unimorph tested in
the experiments

<table>
<thead>
<tr>
<th rowspan="2">Layers</th>
<th rowspan="2">Material</th>
<th rowspan="2">Dimension (radius × thickness)</th>
<th colspan="2">Properties</th>
</tr>
<tr>
<th>Young' modulus (GPa)</th>
<th>Poisson's ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td>PZT layer</td>
<td>PZT-5A</td>
<td>12.5 mm × 180 μm</td>
<td>63</td>
<td>0.3</td>
</tr>
<tr>
<td>Bonding layer</td>
<td>Epoxy</td>
<td>12.5 mm × 20 μm</td>
<td>5.17</td>
<td>0.3</td>
</tr>
<tr>
<td>Passive layer</td>
<td>Brass</td>
<td>17.5 mm × 160 μm</td>
<td>100</td>
<td>0.27</td>
</tr>
</tbody>
</table>

![](./images/811050716880699392_7.jpg)

energy potential function of the piezoactuator considering the gas compression work is expressed as,

$$L = U_p + U_b + U_{pzt} - U_E + U_{gas} \tag{21}$$

Combining Eq. (21) with Eqs. (16) and (17), the coefficients in the Eq. (17) are determined according to the equations: $\partial L/\partial C_i = 0$, $(i=1,2,3,\dots,n)$, then the gas pressure rise in the chamber and deflection of the piezoactuator for sake of the gas compression are obtained.

## 3 Validation of the analytical solution

The solution of the piezoactuator derived above was validated both through FEA simulations and experimental measurements. The FEA simulations were applied to validate the solution for a circular bimorph piezoactuator under the voltage load only. The bimorph consisted of two PZT-5A layers, two epoxy resin layers and one brass layer. Its geometric and material parameters were presented in Table 1. The experimental measurements were conducted to validate the solutions for a circular unimorph with three loading cases: (1) voltage load only, (2) pressure load only, (3) combined voltage and pressure loads. The piezoactuator was commercially available and the main geometric and material parameters of the test unimorph were summarized in Table 2.

### 3.1 Finite element analysis

The finite element simulation to the bimorph was done with ANSYS. The coupled-field element Solid-226 with 20 nodes was chosen to model the PZT layers; and the solid element Solid-186 with 20 nodes was chosen to model the brass layer and the epoxy resin layers. The brass layer was fixed at the edge, and the voltages were imposed on the nodes belong to the upper and lower surfaces of the PZT layers.

According to the grid independence examination, over 46,000 elements (3 division of the minimum length) are required to obtain stable and converged deflections. In our finite element models, there are around 59,700 (4 division of the minimum length) elements for the bimorph piezoactuators. Comparisons between the FEA simulations and the analytical solutions are presented in Figs. 5, 6. The center displacement (maximum displacement) of the bimorph piezoactuator from both FEM simulations and analytical solutions linearly increase with the operating voltage; the value from the analytical calculation is $53.74\ \mu\text{m}$ and the value from FEM is $55.15\ \mu\text{m}$ under the voltage of 100 V, the differences are within 2.6%. Furthermore, the deflection profiles of the bimorph from calculations and FEM simulations are observed, and they agree well with each other, shown in Fig. 6.

![](./images/811050716880699392_8.jpg)

Fig. 5 Center displacement of the bimorph from analytical solutions and FEM simulations

![](./images/811050716880699392_9.jpg)

Fig. 6 Deflection profiles of the bimorph from analytical solutions and FEM simulations

### 3.2 Experiment

Deflection of the circular unimorph piezoactuator was measured under a certain voltage and pressure loads. The schematic and photograph of the experiments setup were showed in Fig. 7, there were a piezoactuator clamper, a signal generator (including its amplifier and an oscilloscope), a laser displacement sensor (LK-G30, resolution of $0.1\ \mu\text{m}$) to measure the deflection, a pressure container to generate the pressure loads and a pressure transducer (XN-801C, ranging 0–30 kPa, accuracy within 0.1%) to measure the pressure loads. The unimorph clamper was

specially designed to provide the edge-clamped boundary condition as well as pressure loads to the unimorph. It was comprised of an upper part with an extended lip and a lower part with a groove to fit the unimorph. The effective clamped radius of the unimorph was 17.5 mm. The laser sensor was mounted on an adjusted support allowed it to measure any point of the piezoactuator.

As for the voltage actuation, the unimorph was driven by a square wave of 2 Hz frequency, which is far less than the first resonant frequency of the unimorph measured around 1.45 kHz, and voltages varied at 20, 30 and 40 V. For the pressure actuation, the pressure load varied at 6, 9.1 and 12.1 kPa, which was controlled by the gas valve and measured by the pressure transducer. For the combined pressure and voltage actuation, the unimorph was driven by a constant pressure load of 1.74 kPa while simultaneously driven by voltages of 10, 20, and 30 V.

The transverse deflections from the experimental measurements and the analytical solutions of the unimorph piezoactuator are compared under loads of voltage only, pressure only and combined voltage and pressure, shown in Figs. 8, 9, 10. The analytical results closely agree with the experimental results in the three loading cases, and their offset is less than 6%, which is

**Fig. 7** Photograph and schematic of the experiments setup.
a Photograph, b Schematic

![](./images/811050716880699392_10.jpg)

![](./images/811050716880699392_11.jpg)

Fig. 8 Deflections of the unimorph under pressure load only

![](./images/811050716880699392_12.jpg)

Fig. 9 Deflections of the unimorph under voltage load only

![](./images/811050716880699392_13.jpg)

Fig. 10 Deflections of the unimorph under combined voltage and pressure loads

a little more than 2.6% the offset between the analytical and FEM result. This may attribute to the non-uniform diaphragm thickness, the imperfect bonded condition between the layers, and the imperfect edge-clamped boundary condition (Gomes 2011).

## 4 Discussion of the bimorph piezoactuator for gas compression

The analytical solutions are highly valuable to the optimal discussion on piezoactuators, such as maximizing the pressure rise in the chamber which is related to the packaging dimensions and material properties of the piezoactuator. In this discussion, the dimensions and material properties of the bimorph type piezoactuator are optimized for a higher gas pressure rise from four aspects: (1) radius ratio of the PZT layer to passive layer $(r_{2}/r_{1})$; (2) thickness ratio of the PZT layer to passive layer $(t_{pzt}/$ $t_{p})$; (3) material properties of the passive layer and bonding layer; (4) ratio of the passive layer thickness to its radius $(t_{p}/r_{1})$. Furthermore, the gas pressure rise and actuator deflection profile are investigated under the optimal dimensions. The depth of the cylinder cavity is $100\ \mu$m, and the initial pressure inside and outside the chamber is 101.3 kPa. The default dimensions and material properties of the bimorph are presented in Table 1.

Deflection of the bimorph piezoactuator is discussed with variation of the $r_{2}/r_{1}$ for two loading cases, shown in Fig. 11, one is the bimorph deflects to compress the gas in the chamber, and the other is the bimorph deflects without any pressure load. The $r_{2}/r_{1}$ ranges from 0.6 to 0.93, and the voltage varies at 40, 60, 80 and 100 V. The optimal $r_{2}/r_{1}$ of the bimorph piezoactuator for gas compression is around 0.85, and the value hardly varies with the excitation voltage. However, the optimal $r_{2}/r_{1}$ of the bimorph deflecting without any pressure load is around 0.76, which is consistent with the conclusion in the reference (Prasad et al. 2006). Therefore, the optimal radius ratio $(r_{2}/r_{1})$ is higher when the bimorph deflects for gas compression.

Deforming profiles of the bimorph piezoactuator for gas compression are further observed to explain the inconsistent optimal $r_{2}/r_{1}$ for the two loading cases. The profiles are observed for different $r_{2}/r_{1}$ under the voltage of 100 V, shown in Fig. 12. When $r_{2}/r_{1}$ is lower than 0.8, the center displacement of the bimorph is larger than the displacement of $r_{2}/r_{1}=0.87$. However, the gas pressure rise is on the contrary according to the Fig. 11, that is the gas pressure is higher when $r_{2}/r_{1}=0.87$. This phenomenon is due to the reversed deflection near the clamped edge according to the deforming profiles, and the reversed deflection significantly decreases the stroke volume ratio of the compression. A similar phenomenon is observed through numerical

![](./images/811050716880699392_14.jpg)

Fig. 11 Deflection of the bimorph for two loading cases: a gas compression (solid lines); b without pressure load (dash lines)

![](./images/811050716880699392_15.jpg)

Fig. 12 Cross section profiles of the bimorph for gas compression with different $r_2/r_1$ under the voltage of 100 V

simulations to a square edge-clamped piezoactuator by Kang and Auner (2011). The reversed deflection occurs because the passive layer deflects reversely around its edge to balance the moment from the gas pressure. Moreover, from the analytical calculations, the critical value of $r_2/r_1$ inducing the reversed deflection decreases with the increase of the passive layer thickness. Therefore, the reversed deflection near the edge results in the different optimal $r_2/r_1$ in the two loading cases.

In Fig. 13, the effect of PZT thickness on the gas pressure rise is investigated as well. The thickness ranges from 0.05 to 0.15 mm, namely the thickness ratio $(t_{pz}/t_p)$ ranges from 0.33 to 1. From the figure, there exists an optimal radius ratio $(r_2/r_1)$ for each thickness, and this optimal ratio decreases with the increase of the thickness. The optimal $r_2/r_1$ is around 0.8 when the PZT layer thickness is 0.05 mm, while it is around 0.88 when the thickness is 0.15 mm. Thus, to acquire the highest pressure rise at the optimal $r_2/r_1$, the thickness of the PZT layer should be around 0.1 mm $(t_{pz}/t_p=0.67)$.

![](./images/811050716880699392_16.jpg)

Fig. 13 Effect of the PZT thickness on the pressure rise under the voltage of 100 V

![](./images/811050716880699392_17.jpg)

Fig. 14 Gas pressure rise vs. the $r_2/r_1$ for four passive layer materials under the voltage of 100 V

Figure 14 depicts the gas pressure rise varies with $r_2/r_1$ for four passive layer materials. The Young's Modulus and Poisson's ratio are 200 GPa and 0.3 for steel, 160 GPa and 0.23 for silicon, 100 GPa and 0.27 for brass, 55 GPa and 0.25 for glass. The optimal $r_2/r_1$ is around 0.8 for steel while nearly 0.87 for glass. Therefore, the optimal $r_2/r_1$ is also determined by the material properties of the passive layer. Among these properties, the Young's Modulus takes the main role because the Poisson's ratio has little impact on the piezoactuator deflection according to our calculations and the discussion in the reference (Cui et al. 2007).

![](./images/811050716880699392_18.jpg)

Figure 15 shows the effect of the bonding layer materials on the pressure rise. The Young's Modulus is 8.1 GPa for polyester, 5.17 GPa for epoxy, 4.0 GPa for phenolic, and 2.14 GPa for PVC. The gas pressure rise varies just within 10 Pa among the four materials, but their Young's Modulus is greatly different. Therefore, the bonding layer materials weakly affect the gas pressure rise and take less significant role than the passive layer in terms of the material Young's Modulus.

The optimal ratio of the passive layer thickness to its radius ($t_p/r_1$) is investigated with the excitation voltage at 40, 60, 80 and 100 V, shown in Fig. 16. The optimal $t_p/r_1$ is around 0.0065, and the value hardly varies with the excitation voltage. However, the optimal $t_p/r_1$ is around 0.04 for the piezoactuator without any pressure load according to our calculation and the reference (Li and Chen 2003). The difference is mainly due to the impacts of the gas pressure load.

Static gas pressure rise in the chamber and the piezoactuator deflection profiles are further observed under the optimal geometric parameters ($r_2/r_1=0.85$, $t_{pzt}/t_p=0.67$ and $t_p/r_1=0.0065$), shown in Figs. 17 and 18. The gas pressure rise linearly increases with the voltage, and reaches 9.87 kPa when the voltage is 120 V. Since the gas pressure rise is dominated by the stroke volume ratio of the piezoactuator, the deflection also linearly increases with the voltage. Compared with Fig. 6, the deflection profiles for gas compression are obviously much flatter than the profiles without any pressure load.

![](./images/811050716880699392_19.jpg)

Fig. 15 Gas pressure rise vs. the $r_2/r_1$ for four bonding layer materials under the voltage of 100 V

![](./images/811050716880699392_20.jpg)

Fig. 16 Gas pressure rise vs. the $t_p/r_1$ with the voltage at 40, 60, 80 and 100 V

![](./images/811050716880699392_21.jpg)

Fig. 17 Gas pressure rise with the voltage under the optimal geometric parameters

![](./images/811050716880699392_22.jpg)

Fig. 18 Cross section profiles for gas compression under the optimal geometric parameters

![](./images/811050716880699392_23.jpg)

## 5 Conclusion

An analytical solution for the circular piezoelectric actuated gas micropump is proposed using the energy minimization method and Rayleigh-Ritz method based on Kirchhoff thin plate theory. The solution is applicable to the multilayered diaphragm-type piezoactuators, and is highly accurate according to the validation through FEM simulations and experimental measurements. The analytical and FEM results agree within 2.6%, while the experimental and analytical results agree within 6% deviation.

The equations are simple to use for piezoactuator analysis where the transverse deflection of the actuator can be calculated as explicit functions of the imposed voltage, pressure load, dimensions and material properties. From discussion to the bimorph piezoactuator for gas compression, effects of the actuator dimensions and material properties on the gas pressure rise are observed. Firstly, there exist optimal radius ratio of the PZT layer to passive layer ($r_2/r_1 = 0.85$), optimal thickness ratio of the PZT layer to passive layer ($t_{pz}/t_p = 0.67$), and optimal ratio of the passive layer radius to its thickness ($t_p/r_1 = 0.0065$). These optimal values are different when the actuator deflects without gas pressure load. Moreover, in terms of the Young's Modulus, the passive layer takes more important role than the bonding layer in piezoactuators. Lastly, under the optimal dimensions, the gas pressure rise linearly increases with the voltage, and the bimorph deflection profiles for gas compression are much flatter than the profiles without pressure load.

Acknowledgements The authors are grateful for the support of the National Science Foundation of China (Grant No. 51576123).

## References

Amirouche F, Zhou Y, Johnson T (2009) Current micropump technologies and their biomedical applications. Microsyst Technol 15:647-666. doi:10.1007/s00542-009-0804-7

Arik M, Zurn SM, Bar-Cohen A, Polla DL (2005) Design, fabrication, and characterization of thin film PZT membranes for high flux electronics cooling applications. Smart Mater Struct 14:1239-1249. doi:10.1088/0964-1726/14/6/017

Cheng C-H, Tseng Y-P (2013) Characteristic studies of the piezoelectrically actuated micropump with check valve. Microsyst Technol 19:1707-1715. doi:10.1007/s00542-013-1857-1

Cui Q, Chengliang L, Zha XF (2007) Modeling and numerical analysis of a circular piezoelectric actuator for valveless micropumps. J Intell Mater Syst Struct 19:1195-1205. doi:10.1177/1045389x07084204

Deshpande M, Saggere L (2007) An analytical model and working equations for static deflections of a circular multi-layered diaphragm-type piezoelectric actuator. Sens Actuators A 136:673-689. doi:10.1016/j.sna.2006.12.022

Dobrucki AB, Pruchnicki P (1997) Theory of piezoelectric axisymmetric bimorph. Sens Actuators A 58:203-212. doi:10.1016/S0924-4247(97)01401-5

Gomes LT (2011) Effect of damping and relaxed clamping on a new vibration theory of piezoelectric diaphragms. Sens Actuators A 169:12-17. doi:10.1016/j.sna.2011.04.005

Herz M, Horsch D, Wachutka G, Lueth TC, Richter M (2010) Design of ideal circular bending actuators for high performance micropumps. Sens Actuators A 163:231-239. doi:10.1016/j.sna.2010.05.018

Iverson BD, Garimella SV (2008) Recent advances in microscale pumping technologies: a review and evaluation. Microfluid Nanofluid 5:145-174. doi:10.1007/s10404-008-0266-8

Kang J, Auner GW (2011) Simulation and verification of a piezoelectrically actuated diaphragm for check valve micropump design. Sens Actuators A 167:512-516. doi:10.1016/j.sna.2011.01.012

Laser DJ, Santiago JG (2004) A review of micropumps. J Micromech Microeng 14:R35-R64. doi:10.1088/0960-1317/14/6/r01

Li S, Chen S (2003) Analytical analysis of a circular PZT actuator for valveless micropumps. Sens Actuators A 104:151-161. doi:10.1016/s0924-4247(03)00006-2

Li B, Chen Q, Lee D-G, Woolman J, Carman GP (2005) Development of large flow rate, robust, passive micro check valves for compact piezoelectrically actuated pumps. Sens Actuators A 117:325-330. doi:10.1016/j.sna.2004.06.029

Nisar A, Afzulpurkar N, Mahaisavariya B, Tuantranont A (2008) MEMS-based micropumps in drug delivery and biomedical applications. Sensors and Actuators B Chemical 130:917-942. doi:10.1016/j.snb.2007.10.064

Papila M, Sheplak M, Cattafesta LN (2008) Optimization of clamped circular piezoelectric composite actuators. Sens Actuators A 147:310-323. doi:10.1016/j.sna.2008.05.018

Prasad SAN, Gallas Q, Horowitz SB, Homeijer BD, Sankar BV, Cattafesta LN, Sheplak M (2006) Analytical electroacoustic model of a piezoelectric composite circular plate. AIAA Journal 44:2311-2318. doi:10.2514/1.19855

Samuel I, En L (2011) Investigation on packaging parameters of a circular multi-layered diaphragm-type piezoelectric actuator. Comput Struct 89:371-379. doi:10.1016/j.compstruc.2010.11.007

Shuxiang Dong KU, Li Longtu, Viehland Dwight (2007) Analytical solutions for the transverse deflection of a piezoelectric circular axisymmetric unimorph actuator. IEEE Trans Ultrason Ferroelectr Freq Control 54:10

Singh S, Kumar N, George D, Sen AK (2015) Analytical modeling, simulations and experimental studies of a PZT actuated planar valveless PDMS micropump. Sens Actuators A 225:81-94. doi:10.1016/j.sna.2015.02.012

Wang DH, Huo J (2010) Modeling and testing of the static deflections of circular piezoelectric unimorph actuators. J Intell Mater Syst Struct 21:1603-1616. doi:10.1177/1045389x10385485

Wang DA, Cheng CH, Hsieh YH, Zhang ZX (2007) Analysis of an annular PZT actuator for a droplet ejector. Sens Actuators A 137:8. doi:10.1016/j.sna.2007.03.020

Yoon JS, Choi JW, Kim MS (2009) Computational and experimental investigation on the performance characteristics of the micro gas compressor. Microelectron Eng 86:1975-1982. doi:10.1016/j.mee.2008.12.048

Zhang Y, Wang W (2011) Analytical model of electrostatic actuators for micro gas pumps. Microsyst Technol 17:1683-1696. doi:10.1007/s00542-011-1354-3

![](./images/811050716880699392_24.jpg)