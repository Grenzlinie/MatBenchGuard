TECHNICAL PAPER

# A size-dependent model to study nonlinear static behavior of piezoelectric cantilever microbeams with damage

Yufang Zheng¹ · Tao Chen¹ · Changping Chen²

Received: 23 September 2016 / Accepted: 19 December 2016
© Springer-Verlag Berlin Heidelberg 2017

**Abstract** Based on the modified couple stress theory and von Kármán nonlinear theory, a size-dependent nonlinear mathematical model for an electrostatically actuated micro- beam with a piezoelectric layer bonded to the top surface is formulated by the Hamilton's principle. In the developed model, the static behavior of the microbeam is discussed by using numerical methods. The results show that the size effect is significant when the microbeam thickness is com- parable to the material length scale parameter. The effect of geometric nonlinearity on the pull-in voltage mainly depends on the initial gap. By applying a small negative voltage to the piezoelectric layer, the pull-in voltage may effectively reduce. To attain accurate analysis for the static behaviors of microscale beam devices, the damage has to be considered.

## 1 Introduction

Microbeams have become prevalent in the fields of MEMS such as microsensors (Shah-Mohammadi-Azar et al. 2015) and microactuators (Sathiya et al. 2016). Researches on the behaviors of microbeams are essential for the design of MEMS. Typical electrostatically actuated MEMS are comprised of a deformable electrode suspended above a fixed electrode (Fig. 1). A direct current voltage is applied between the two electrodes. The behavior of the microbeam is affected by the coupling of the mechanical resistance and the electric field force. As the voltage exceeds the critical voltage, the "pull-in" phenomena will occur. The critical voltage and the critical displacement are called pull-in volt- age and pull-in displacement respectively. Accurate calcu- lation of them is one of the major issues in the static analy- sis for electrostatically actuated microbeams.

Using the shooting method, Choi and Lovell (1997) investigated the stretching effect in axially constrained clamped-clamped microbeams for mechanical and electro- static loads. Batra et al. (2006) studied the collapse insta- bility of a cantilever beam and a fixed-fixed beam by the meshless method. The approximate analytical solution of the pull-in voltage of a cantilever beam is obtained by applying the energy method (Hu 2006). The results are in good agreement with the previous numerical results and experimental results. Rezazadeh (2007) analyzed the vari- ation regularity of the pull-in voltage of a laminated micro- beam with the Newton iterative method. Piezoelectric materials are paid increasingly attention for light weight, rapid response and low power consumption. The piezo- electric voltage is useful to control the performance of microbeams. The effect of the piezoelectric voltage on the static and dynamic stabilities of microbeams has been stud- ied (Rezazadeh et al. 2009). However, the aforementioned works were performed within the context of the classical continuum mechanics theory. As the MEMS structures are on the order of microns or sub-microns, the mechanical and physical properties of the microstructure are very different from the macroscale which is called size effect. To explain and predict the size-dependent phenomena, there are three available theories: the modified couple stress theory, the strain gradient elasticity theory and the nonlocal theory. All of them describe size effect by introducing material length scale parameters.

Correspondence: Changping Chen
cpchen@126.com

¹ College of Civil Engineering, Fuzhou University,
Fuzhou 350116, China
² Department of Civil Engineering and Architecture,
Xiamen University of Technology, Xiamen 361024, China

Fig. 1 Model of piezoelectric
cantilever microbeam

![](./images/811090618825572354_1.jpg)

Based on the theory of strain gradient elasticity, Kong
et al. (2009) conducted researches on the static and
dynamic characteristics of a microbeam. With the modified
couple stress theory, the influence of size effect on the pull-
in voltage of an electrostatically actuated microbeam was
discussed (Yin et al. 2011). Xiao et al. (2015) established
a versatile size-dependent model for piezoelectro-mechan-
ical coupling problem to analyze the size-dependent pull-
in instability under mechanical and electrostatic forces.
Using Eringen's nonlocal elasticity theory, Tavakolian et al.
(2015) investigated the small-scale effects on the pull-in
instability of micro-switches.

Microstructures can be damaged in the process of pro-
duction, packaging and use (Davison et al. 1977; Kausch
and Béguelin 2001). As damage is harmful to the operation
and life of the devices, it is significant to take damage into
account for the design of MEMS. In the recent work, the
nonlinear model analysis of microbeams is mostly based on
clamped-clamped microbeams without damage. The paper
aims to study the static behavior of a piezoelectric cantile-
ver microbeam with damage by establishing a size-depend-
ent nonlinear model.

## 2 Modeling

As illustrated in Fig. 1, the studied model is an isotropic
microbeam of length $L$, width $b$, thickness $h_b$, density
$\rho_b$ and Young's modulus $E_b$, with a piezoelectric layer
bonded on the top surface. The piezoelectric layer has
thickness $h_p$, density $\rho_p$, Young's modulus $E_p$, and equiva-
lent piezoelectric coefficient $e_{31}$. The total height of the
microbeam is $h = h_b + h_p$. The gap distance between the
electrodes is denoted by $d$. The vacuum gap has the per-
mittivity of the vacuum $\varepsilon_v$. A voltage $V$ is applied between
the movable beam and the fixed electrode, and $V_p$ is
applied between the top and bottom surfaces of the piezo-
electric layer.

According to the isotropic damage theory and equiv-
alent-strain principle, the one-dimensional damage
constitutive equation can be written as (Kachanov and Kra-
jcinovic 1986)

$$
\varepsilon_{e}=\frac{\sigma}{E(1-D)} \tag{1}
$$

where $E$, $D$, $\sigma$ are undamaged Young's modulus, damage
variable and Cauchy stress, respectively.

From Eq. (1), The equivalent elastic modulus of the
damaged material can be expressed as

$$
\tilde{E}=E(1-D) \tag{2}
$$

In the paper, only the beam's damage is considered,
described by $D$. Establishing the coordinate system as
shown in Fig. 1. The $z$-axis and $\tilde{z}$-axis are attached to the
middle and top of the left end of the microbeam, respec-
tively. Setting the $x$-axis as the neutral axis, the distance
between the neutral axis and the top of the piezoelectric
layer, $z_c$, can be determined as follows (Asghari et al. 2010)

$$
z_{c}=\frac{\int_{A} E(\tilde{z}) \tilde{z} d A}{\int_{A} E(\tilde{z}) d A} \tag{3}
$$

where $E(\tilde{z})$ is the equivalent elastic modulus which varies
along the $\tilde{z}$-axis and can be written as

$$
E(\tilde{z})= \begin{cases}E_{p}, & 0 \leq \tilde{z}<h_{p} \\ (1-D) E_{b}, & h_{p}<\tilde{z} \leq h_{p}+h_{b}\end{cases} \tag{4}
$$

By substituting Eq. (4) into Eq. (3), it follows that

$$
z_{c}=\frac{(1-D) E_{b} h_{p} h_{b}+\frac{1}{2} E_{p} h_{p}^{2}+\frac{1}{2}(1-D) E_{b} h_{b}^{2}}{E_{p} h_{p}+(1-D) E_{b} h_{b}} \tag{5}
$$

In the $x o z$ coordinate system, the equivalent elastic mod-
ulus can be expressed as

$$
E(z)= \begin{cases}E_{p},-z_{c} \leq z<h_{p}-z_{c} \\ (1-D) E_{b}, & h_{p}-z_{c}<z \leq h_{p}+h_{b}-z_{c}\end{cases} \tag{6}
$$

Based on the modified couple stress theory (Yang et al.
2002), the strain energy function of an isotropic linear elas-
tic material occupying region $\Omega$ is given by

$$
U=\frac{1}{2} \int_{\Omega}\left(\sigma_{i j} \varepsilon_{i j}+m_{i j} \chi_{i j}\right) d \Omega \quad(i, j=1,2,3)
\tag{7}
$$

where the stress tensor $\sigma_{i j}$, strain tensor $\varepsilon_{i j}$, deviatoric part of the couple stress tensor $m_{i j}$, and symmetric curvature tensor $\chi_{i j}$, are, respectively, defined by

$$
\sigma_{i j}=\lambda \operatorname{tr}\left(\varepsilon_{i j}\right) I+2 \mu \varepsilon_{i j}
\tag{8}
$$

$$
\varepsilon_{i j}=\frac{1}{2}\left(\partial_{i} u_{j}+\partial_{j} u_{i}\right)
\tag{9}
$$

$$
m_{i j}=2 l^{2} \mu \chi_{i j}
\tag{10}
$$

$$
\chi_{i j}=\frac{1}{2}\left(\partial_{i} \theta_{j}+\partial_{j} \theta_{i}\right)
\tag{11}
$$

which $\lambda$ and $\mu$ are Lamé's constants, $l$ is a material length scale parameter, $u_{i}$ is the displacement vector and $\theta_{i}$ is the rotation vector, and

$$
\theta_{i}=\frac{1}{2} e_{i j k} \partial_{j} u_{k}
\tag{12}
$$

According to the Bernoulli-Euler hypothesis, the displacement field of a beam in bending can be written as

$$
\begin{aligned}
& u(x, z, t)=-z \frac{\partial w(x, t)}{\partial x}, v(x, z, t)=0 \\
& w(x, z, t)=w(x, t)
\end{aligned}
\tag{13}
$$

where $u(x, z, t), v(x, z, t), w(x, z, t)$ are the $x, y$ and $z$ directional components of the displacement vector, respectively.

Considering the nonlinear strain-displacement relations, the strain component $\varepsilon_{i j}$ is obtained as

$$
\begin{aligned}
\varepsilon_{x x}(x, z, t) & =\frac{\partial u(x, z, t)}{\partial x}+\frac{1}{2}\left(\frac{\partial w}{\partial x}\right)^{2} \\
& =-z \frac{\partial^{2} w}{\partial x^{2}}+\frac{1}{2}\left(\frac{\partial w}{\partial x}\right)^{2}
\end{aligned}
\tag{14}
$$

$$
\varepsilon_{y y}=\varepsilon_{z z}=\varepsilon_{x y}=\varepsilon_{y z}=\varepsilon_{z x}=0
\tag{15}
$$

Substituting Eqs. (12) and (13) into (11), it follows that

$$
\begin{aligned}
& \chi_{x y}=-\frac{1}{2} \frac{\partial^{2} w}{\partial x^{2}} \\
& \chi_{x x}=\chi_{y y}=\chi_{z z}=\chi_{y z}=\chi_{z x}=0
\end{aligned}
\tag{16}
$$

For a slender beam with a large aspect ratio, the Poisson effect is minor and may be neglected to facilitate the formulation of a simple beam theory (Park and Gao 2006). Substituting Eqs. (14) and (15) into Eq. (8), gives the non-zero stresses $\sigma_{i j}$ of the beam can be obtained as

$$
\sigma_{x x}=(1-D) E_{b} \varepsilon_{x x}=E(z) \varepsilon_{x x}
\tag{17}
$$

and according to the piezoelectric theory, the non-zero stresses $\sigma_{i j}$ of the piezoelectric layer can be expressed as

$$
\sigma_{x x}=E_{p} \varepsilon_{x x}-e_{31} E_{z}=E(z) \varepsilon_{x x}-e_{31} E_{z}
\tag{18}
$$

where $E_{z}$ is the electric field strength of the piezoelectric layer, defined as $E_{z}=V_{p} / h_{p}$.

And from Eqs. (16) and (10), that is

$$
m_{x y}=-\mu(z) l^{2}(z) \frac{\partial^{2} w}{\partial x^{2}}
\tag{19}
$$

where

$$
\mu(z) l^{2}(z)=
\begin{cases}
\frac{E_{p} l_{p}^{2}}{2\left(1+v_{p}\right)}, & -z_{c} \leq z<h_{p}-z_{c} \\
\frac{(1-D) E_{b} l_{b}^{2}}{2\left(1+v_{b}\right)}, & h_{p}-z_{c}<z \leq h_{p}+h_{b}-z_{c}
\end{cases}
$$

where $v_{p}$ and $l_{p}$ are the Poisson's ratio and length scale parameter of the piezoelectric layer, respectively. $v_{b}$ and $l_{b}$ are the Poisson's ratio and length scale parameter of the beam, respectively.

According to the Hamilton's principle, the strain energy $U$, the kinetic energy $T$ and the total work done by external forces $W$ should satisfy the following variational equation.

$$
\int_{t_{1}}^{t_{2}}(\delta T-\delta U+\delta W) d t=0
\tag{20}
$$

From Eq. (7), gives the variation of the strain energy of the microbeam as

$$
\delta U=\int_{\Omega}\left(\sigma_{i j} \delta \varepsilon_{i j}+m_{i j} \delta \chi_{i j}\right) d \Omega
\tag{21}
$$

Substituting Eqs. (14-19) into Eq. (21), it follows that

$$
\begin{aligned}
\delta U= & \int_{0}^{L}\left[\left((E I)_{e q}+\left(\mu A l^{2}\right)_{e q}\right) w^{\prime \prime \prime \prime}+b e_{31} E_{z} h_{p} w^{\prime \prime}\right. \\
& \left.-\frac{3}{2}(E A)_{e q}\left(w^{\prime}\right)^{2} w^{\prime \prime}\right] \delta w d x \\
& +\left[\left(-\left((E I)_{e q}+\left(\mu A l^{2}\right)_{e q}\right) w^{\prime \prime \prime}-b e_{31} E_{z} h_{p} w^{\prime}\right.\right. \\
& \left.\left.+\frac{1}{2}(E A)_{e q}\left(w^{\prime}\right)^{3}\right) \delta w\right]_{0}^{L} \\
& +\left[\left(\left((E I)_{e q}+\left(\mu A l^{2}\right)_{e q}\right) w^{\prime \prime}\right.\right. \\
& \left.\left.+\frac{1}{2} b e_{31} E_{z}\left(\left(h_{p}-z_{c}\right)^{2}-z_{c}^{2}\right)\right) \delta w^{\prime}\right]_{0}^{L}
\end{aligned}
\tag{22}
$$

![](./images/811090618825572354_2.jpg)

where
$$
\begin{aligned}
(E I)_{e q}= & \int_{A} E(z) z^{2} d A \\
= & \frac{1}{12} E_{p} b h_{p}^{3}+\frac{1}{12}(1-D) E_{b} b h_{b}^{3}+E_{p} b h_{p}\left(z_{c}-\frac{1}{2} h_{p}\right)^{2} \\
& +(1-D) E_{b} b h_{b}\left(h_{p}+\frac{1}{2} h_{b}-z_{c}\right)^{2}
\end{aligned}
$$

$$
(E A)_{e q}=\int_{A} E(z) d A=E_{p} b h_{p}+(1-D) E_{b} b h_{b}
$$

$$
\begin{aligned}
\left(\mu A l^{2}\right)_{e q} & =\int_{A} \mu(z) l^{2}(z) d A \\
& =\frac{E_{p} b h_{p} l_{p}^{2}}{2\left(1+v_{p}\right)}+\frac{(1-D) E_{b} b h_{b} l_{b}^{2}}{2\left(1+v_{b}\right)}
\end{aligned}
$$

$$
w^{\prime \prime \prime \prime}=\frac{\partial^{4} w}{\partial x^{4}} w^{\prime \prime \prime}=\frac{\partial^{3} w}{\partial x^{3}} w^{\prime \prime}=\frac{\partial^{2} w}{\partial x^{2}} w^{\prime}=\frac{\partial w}{\partial x}
$$

The variation of the kinetic energy of the microbeam can be written as
$$
\delta T=\int_{0}^{L} m \frac{\partial w}{\partial t} \delta\left(\frac{\partial w}{\partial t}\right) d x\qquad(23)
$$

where $m$ is the linear density of the piezoelectric microbeam, defined by
$$
m=\rho_{p} b h_{p}+\rho_{b} b h_{b}
$$

For this model, there is only the electric field force and its edge effect is neglected. The electric field force can be expressed as (Younis and Nayfeh 2003)
$$
F(x, t)=\frac{1}{2} \varepsilon_{v} \frac{b V^{2}}{(d-w)^{2}}\qquad(24)
$$

Then, the variation of the work done by external forces is
$$
\delta W=\int_{0}^{L} F(x, t) \delta w d x\qquad(25)
$$

Substituting Eqs. (22), (23) and (25) into Eq. (20), it is obtained that
$$
\begin{aligned}
& \left((E I)_{e q}+\left(\mu A l^{2}\right)_{e q}\right) \frac{\partial^{4} w}{\partial x^{4}} \\
& \quad+b e_{31} V_{p} \frac{\partial^{2} w}{\partial x^{2}}-\frac{3}{2}(E A)_{e q}\left(\frac{\partial w}{\partial x}\right)^{2} \frac{\partial^{2} w}{\partial x^{2}} \\
& \quad+m \frac{\partial^{2} w}{\partial t^{2}}=\frac{1}{2} \varepsilon_{v} \frac{b V^{2}}{(d-w)^{2}}
\end{aligned}\qquad(26)
$$

The corresponding boundary conditions are ($x=0$ and $x=L$)
$$
\begin{gathered}
\left((E I)_{e q}+\left(\mu A l^{2}\right)_{e q}\right) \frac{\partial^{2} w}{\partial x^{2}} \\
+\frac{1}{2} b e_{31} V_{p}\left(h_{p}-2 z_{c}\right)=0 \quad \text { or } \quad \frac{\partial w}{\partial x}=0 \\
\left((E I)_{e q}+\left(\mu A l^{2}\right)_{e q}\right) \frac{\partial^{3} w}{\partial x^{3}}+b e_{31} V_{p} \frac{\partial w}{\partial x} \\
-\frac{1}{2}(E A)_{e q}\left(\frac{\partial w}{\partial x}\right)^{3}=0 \quad \text { or } \quad w=0
\end{gathered}\qquad(27)
$$

In the Eqs. (26) and (27), $\left(\mu A l^{2}\right)_{e q}$ describes the size effect of the microbeam. If the material length scale parameters $l_{p}$ and $l_{b}$ are both zero, the model is reduced to the classical model. For convenience, defining the equivalent length scale parameter of the microbeam as $l_{e q}$, expressed as
$$
l_{e q}^{2}=\frac{\int_{A} \mu(z) l^{2}(z) d A}{\int_{A} \mu(z) d A}\qquad(28)
$$

Introducing the following nondimensional parameters:
$W=\frac{w}{d}, \quad \xi=\frac{x}{L}, \quad H=(E I)_{e q}+\left(\mu A l^{2}\right)_{e q}, \quad \bar{e}_{31}=\frac{b e_{31} L^{2} V_{0}}{H}$,
$\bar{V}_{p}=\frac{V_{p}}{V_{0}}, \quad \alpha=\frac{3 d^{2}(E A)_{e q}}{2 H}, \quad T=\sqrt{\frac{m L^{4}}{H}}, \quad \tau=\frac{t}{T}, \quad \bar{V}=\frac{V}{V_{0}}$,
$\beta=\frac{b \varepsilon_{v} L^{4} V_{0}^{2}}{2 d^{3} H}$, where $V_{0}$ is unit voltage. Then, Eq. (26) can be rewritten as
$$
\frac{\partial^{4} W}{\partial \xi^{4}}+\bar{e}_{31} \bar{V}_{p} \frac{\partial^{2} W}{\partial \xi^{2}}-\alpha\left(\frac{\partial W}{\partial \xi}\right)^{2} \frac{\partial^{2} W}{\partial \xi^{2}}+\frac{\partial^{2} W}{\partial \tau^{2}}=\beta \frac{\bar{V}^{2}}{(1-W)^{2}}
$$

The rewritten boundary conditions are ($\xi=0$ and $\xi=1$)
$$
\begin{aligned}
& \frac{\partial^{2} W}{\partial \xi^{2}}+\frac{1}{2} \bar{e}_{31} \bar{V}_{p} \frac{h_{p}-2 z_{c}}{d}=0 \quad \text { or } \quad \frac{\partial W}{\partial \xi}=0 \\
& \frac{\partial^{3} W}{\partial \xi^{3}}+\bar{e}_{31} \bar{V}_{p} \frac{\partial W}{\partial \xi}-\frac{1}{3} \alpha\left(\frac{\partial W}{\partial \xi}\right)^{3}=0 \quad \text { or } \quad W=0
\end{aligned}
$$

For the static analysis, the governing equation can be expressed as
$$
\frac{d^{4} W}{d \xi^{4}}+\bar{e}_{31} \bar{V}_{p} \frac{d^{2} W}{d \xi^{2}}-\alpha\left(\frac{d W}{d \xi}\right)^{2} \frac{d^{2} W}{d \xi^{2}}=\beta \frac{\bar{V}^{2}}{(1-W)^{2}} \quad(31)
$$

The boundary conditions for a cantilever are
$$
\begin{aligned}
\xi=0: W=0, & \frac{d W}{d \xi}=0 \\
\xi=1: \frac{d^{2} W}{d \xi^{2}}+\frac{1}{2} \bar{e}_{31} \bar{V}_{p} \frac{h_{p}-2 z_{c}}{d} & =0 \\
\frac{d^{3} W}{d \xi^{3}}+\bar{e}_{31} \bar{V}_{p} \frac{d W}{d \xi}-\frac{1}{3} \alpha\left(\frac{d W}{d \xi}\right)^{3} & =0
\end{aligned}
$$

![](./images/811090618825572354_3.jpg)

## 3 Numerical results and discussion

The method adopted in this paper for solving the governing differential Eq. (31) is the differential quadrature method (DQM). The DQM was originally introduced by Bellman and Casti (1971) and elaborated upon further by Civan and Sliep- cevich (1984). It is a quite efficient approximate technique for the numerical solution of differential and partial differential equations, especially the boundary value problem.

As an illustration, a silicon beam with PZT-4 piezoelec- tric actuator is considered with the geometric and material constants listed in Table 1 (Rezazadeh et al. 2006).

Rokni et al. (2013) introduced an analytical solution to investigate the size-dependent pull-in voltages of electro- statically actuated cantilever, and found that the material length scale parameter for (poly) silicon is on the order of $10^{-1}$ µm. Figure 2 shows the non-dimensional tip dis placements $W$ for various voltages $\bar{V}$ applied between the electrodes. The curves have been calculated by different non-dimensional voltages $\bar{V}_{p}$, which is applied to the piezoelectric layer for classical model (CM, not incorporating the length scale effect) and present model (PM, $l_{eq}=0.7$ µm). It can be seen from Fig. 2 that the deformation of the microbeam can be greatly affected by the voltage applied to the piezoelectric layer even though the voltage is small. As indicated in the works of Rezazadeh et al. (2006) and Xiao et al. (2015), the positive and negative applied volt- ages to the piezoelectric layer cause to apply a compressive force and a tensile force in the axial direction, respectively. For the microbeam with single piezoelectric layer, how- ever, there is an additional bending moment deriving from the offset compressive force or tensile force which makes a quite difference from the sandwiched microbeam. The neg- ative applied voltage to the piezoelectric layer causes to a bending moment which results in a downward curving ten- dency of the microbeam and vice verse. It can be seen from Fig. 2 that the initial tip displacement is above zero with $\bar{V}_{p}=-1$ and below zero with $\bar{V}_{p}=1$ by setting $\bar{V}=0$.

The effect of the applied voltage to the piezoelectric layer on the pull-in voltage is shown in Fig. 3. By increas- ing the negative applied voltage to the piezoelectric layer, the corresponding pull-in voltage decreases even if the beam stiffens. Conversely, the positive applied voltage to the piezoelectric layers would soften the microbeam and increase the pull-in voltage. The variable tendency of the pull-in voltage is just the opposite of the results of the pre- vious works (Rezazadeh et al. 2006; Xiao et al. 2015). The reason is that the additional moment plays a greater role on the pull-in voltage than the axial force does under small deformation conditions. The pull-in voltage can be dramat- ically reduced by applying a negative voltage on the piezo- electric layer as shown in Fig. 3. For example, by applying negative 1.5 unit voltage to the piezoelectric layer (present model), the pull-in voltage decreases from 49.70 to 39.56 unit voltage.

The size effect is investigated by comparing the present model with the classical model in Figs. 2 and 3. The non- dimensional tip displacement of the present model is a little

<table><caption>Table 1 Geometrical and material properties of the piezoelectric microbeam</caption>
<thead>
<tr>
<th></th>
<th>Beam</th>
<th>Piezoelectric layer</th>
</tr>
</thead>
<tbody>
<tr>
<td>Length</td>
<td>100 µm</td>
<td>100 µm</td>
</tr>
<tr>
<td>Width</td>
<td>15 µm</td>
<td>15 µm</td>
</tr>
<tr>
<td>Height</td>
<td>3 µm</td>
<td>0.5 µm</td>
</tr>
<tr>
<td>Young's modulus</td>
<td>169 GPa</td>
<td>78.6 GPa</td>
</tr>
<tr>
<td>Poisson's ration</td>
<td>0.06</td>
<td>0.3</td>
</tr>
<tr>
<td>Density</td>
<td>2331 kg/m³</td>
<td>7500 kg/m³</td>
</tr>
<tr>
<td>$e_{31}$</td>
<td>–</td>
<td>–9.29</td>
</tr>
<tr>
<td>$\varepsilon _{v}$</td>
<td>$8.854×10^{-12}$ F/m</td>
<td>–</td>
</tr>
<tr>
<td>Initial gap</td>
<td>1 µm</td>
<td>–</td>
</tr>
</tbody>
</table>

![](./images/811090618825572354_4.jpg)

Fig. 2 Variation of the non-dimensional tip displacement with volt- age applied between the electrodes, predicted by the classical and present models

![](./images/811090618825572354_5.jpg)

Fig. 3 Non-dimensional pull-in voltage versus voltage applied to the piezoelectric layer for classical model and present model

![](./images/811090618825572354_6.jpg)

less than that of the classical model in Fig. 2, while the pull-in voltage of the present model is a bit higher than that of the classical model in Fig. 3. According to Eq. (26), the material scale parameter improves the bending rigidity of the microbeam which results in the increase of the pull-in voltage.

The non-dimensional tip displacements with respect to the applied voltages between the electrodes are illustrated in Fig. 4 for the classical mode and different equivalent length scale parameters $l_{eq}$. In Fig. 4 and the following figures, the applied voltage to the piezoelectric layer is chosen to be 1 unit voltage. Figure 4 shows that the pull-in voltage increases with $l_{eq}$. All curves pass through the same point which represents the undeformed state. Figure 5 presents the effect of normalized microbeam thickness $(h/l_{eq})$ on the normalized pull-in voltage $(\bar{V}_{pl}/\bar{V}_{pl0})$ for the present model ($l_{eq}=0.7\ \mu\text{m}$). $\bar{V}_{pl0}$ is the non-dimensional pull-in voltage corresponding to the classical model. The thickness ratio of the beam and piezoelectric layer is kept to be the same by setting $h_b/h_p=6/1$. From this figure it may be concluded that the influence of micro scale on the pull-in voltage becomes significant for small values of $h/l_{eq}$ and negligible for large ones. For instance, the pull-in voltage for the present model with $h/l_{eq}=1$ is 1.41 times of that for the classical model with the same microbeam thickness, while the difference in pull-in voltage can be ignored if $h/l_{eq}$ is greater than 20.

![](./images/811090618825572354_7.jpg)

Fig. 4 Non-dimensional tip displacement versus voltage applied between the electrodes for different non-dimensional equivalent length scale parameters ($l_{eq}$)

![](./images/811090618825572354_8.jpg)

Fig. 5 Effect of non-dimensional microbeam thickness $(h/l_{eq})$ on the pull-in voltage

The effect of damage on the pull-in voltage is depicted in Fig. 6. It is apparent that the damage of the beam softens the microbeam for both the classical model and the present model, which leads to a lower pull-in voltage. Therefore, the damage needs to be taken into account to predict the pull-in voltage.

![](./images/811090618825572354_9.jpg)

Fig. 6 Effect of damage of the beam on the pull-in voltage

Figure 7 is plotted for the relationship of the non-dimensional pull-in voltage versus the initial gap. With an increase of the initial gap, the pull-in voltage increases non-linearly for each curve of a particular model. For instance, by changing the initial gap of the nonlinear present model from $1\ \mu\text{m}$ to $4\ \mu\text{m}$, the pull-in voltage increases from 51.98 to 521.24 unit voltage by 9.0 times. A conclusion can be drawn that the pull-in voltage is extremely sensitive to the initial gap. To get a low pull-in voltage, the initial gap should be as small as possible. This can be helpful to the design of electrostatically actuated microbeams.

In order to discuss the influence of geometric nonlinearity on the pull-in voltage, the relative increment of the

![](./images/811090618825572354_10.jpg)

Fig. 7 Nondimensional pull-in voltage versus initial gap

![](./images/811090618825572354_11.jpg)

![](./images/811090618825572354_12.jpg)

Fig. 8 The relative increment of pull-in voltage for geometric nonlinearity versus initial gap

![](./images/811090618825572354_13.jpg)

Fig. 9 Nondimensional pull-in voltage versus microbeam thickness for geometric nonlinear model and geometric linear model with different microbeam lengths

pull-in voltage, compared with the geometric linear model, is introduced in Fig. 8. The relative increment is tiny at a small initial gap and grows up rapidly with the increase of the initial gap. It comes to a conclusion that the effect of geometric nonlinearity needs to be considered to predict the pull-in voltage as the initial gap is large enough. From Fig. 9, the geometric nonlinear model and geometric linear model are almost the same pull-in voltage no matter what microbeam length and thickness are. This shows that the effects of microbeam length and thickness on geometric nonlinearity characteristic of the piezoelectric cantilever microbeams are very small.

## 4 Conclusions

A size-dependent geometrically nonlinear mathematical model is developed for analyzing the static deflection and the pull-in voltage of an electrostatically actuated microbeam with a piezoelectric layer bonded to the top surface. The effects of the applied voltage to the piezoelectric layer, microbeam thickness, damage, initial gap and geometric nonlinearity on the pull-in voltage are studied.

By applying a small negative voltage to the piezoelectric layer, the pull-in voltage can be significantly reduced and the beam stiffens. The size effect may improve the bending rigidity of microbeams, which results in the decrease of the deflections and the increase of the pull-in voltages. The size effect increases with the decrease of the microbeam thickness, especially when the microbeam thickness is comparable to the material length scale parameter. Reducing the initial gap is conducive to lower the pull-in voltage. When the initial gap is large enough, the geometric nonlinearity of the beam may be taken into account. Besides, the damage of the beam could not be neglected for precisely predicting the pull-in voltage. This study may be helpful to the design and accurate analysis for related MEMS devices.

Acknowledgements This work is supported by the National Natural Science Foundation of China (Grant No. 11272270).

## References

Asghari M, Ahmadian MT, Kahrobaiyan MH, Rahaeifard M (2010) On the size-dependent behavior of functionally graded microbeams. Mater Design 31:2324-2329

Batra RC, Porfiri M, Spinello D (2006) Electromechanical model of electrically actuated narrow microbeams. J Microelectromech Syst 15:1175-1189

Bellman R, Casti J (1971) Differential quadrature and long-term integration. J Math Anal Appl 34:235-238

Choi B, Lovell EG (1997) Improved analysis of microbeams under mechanical and electrostatic loads. J Micromech Microeng 7:24-29

Civan F, Sliepcevich CM (1984) Differential quadrature for multidimensional problems. J Math Anal Appl 101:423-443

Davison L, Stevens AL, Kipp ME (1977) Theory of spall damage accumulation in ductile metals. J Mech Phys Solids 25:11-28

Hu YC (2006) Closed form solutions for the pull-in voltage of microcurled beams subjected to electrostatic loads. J Micromech Microeng 16:648-655

Kachanov LM, Krajcinovic D (1986) Introduction to continuum damage mechanics. M. Nijhoff, The Hague

Kausch HH, Béguelin P (2001) Deformation and fracture mechanisms in filled polymers. Macromol Symp 169:79-87

Kong S, Zhou S, Nie Z, Wang K (2009) Static and dynamic analysis of micro beams based on strain gradient elasticity theory. Int J Eng Sci 47:487-498

Park SK, Gao XL (2006) Bernoulli-Euler beam model based on a modified couple stress theory. J Micromech Microeng 16:2355

Rezazadeh G (2007) A comprehensive model to study nonlinear behavior of multilayered micro beam switches. Microsyst Technol 14:135-141. doi:10.1007/s00542-007-0398-x

Rezazadeh G, Tahmasebi A, Zubstov M (2006) Application of piezoelectric layers in electrostatic MEM actuators: controlling of pull-in voltage. Microsyst Technol 12:1163-1170. doi:10.1007/s00542-006-0245-5

![](./images/811090618825572354_14.jpg)

Rezazadeh G, Fathalilou M, Shabani R (2009) Static and dynamic stabilities of a microbeam actuated by a piezoelec- tric voltage. Microsyst Technol 15:1785–1791. doi:10.1007/ s00542-009-0917-z

Rokni H, Seethaler RJ, Milani AS, Hosseini-Hashemi S, Li X-F (2013) Analytical closed-form solutions for size-dependent static pull-in behavior in electrostatic micro-actuators via Fredholm integral equation. Sens Actuators, A 190:32–43

Sathiya S, Umapathy M, Vasuki B, Uma G (2016) Simple liquid pumping system using piezoelectric actuated cantilever beam. Instrum Exp Tech 59:142–148

Shah-Mohammadi-Azar A, Shabani R, Rezazadeh G (2015) A novel micro-cantilever based angular speed sensor controlled piezo- electrically and tuned by electrostatic actuators. Sens Imaging 16:1–14

Tavakolian F, Farrokhabadi A, Mirzaei M (2015) Pull-in instabil- ity of double clamped microbeams under dispersion forces in the presence of thermal and residual stress effects using nonlo- cal elasticity theory. Microsyst Technol, pp 1–10. doi:10.1007/ s00542-015-2785-z

Xiao Y, Wang B, Zhou S (2015) Pull-in voltage analysis of electrostat- ically actuated MEMS with piezoelectric layers: a size-depend- ent model. Mech Res Commun 66:7–14

Yang F, Chong ACM, Lam DCC, Tong P (2002) Couple stress based strain gradient theory for elasticity. Int J Solids Struct 39:2731–2743

Yin L, Qian Q, Wang L (2011) Size effect on the static behavior of electrostatically actuated microbeams. Acta Mech Sinica 27:445–451

Younis MI, Nayfeh AH (2003) A study of the nonlinear response of a resonant microbeam to an electric actuation. Nonlinear Dyn 31:91–117

![](./images/811090618825572354_15.jpg)