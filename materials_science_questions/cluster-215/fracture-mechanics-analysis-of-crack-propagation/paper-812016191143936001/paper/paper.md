# A Nonlinear Energy Analysis for Cracked Lamina of Fibre-Reinforced Composite Material

## WEI SHEN AND YAO-PU YONG
Huazhong University of Science and Technology
Wuhan, China

(Received March 5, 1983)

## ABSTRACT
The general G-K relation has been obtained and the nonlinear energy method generalized to analyzing the mixed mode fracture problem by W. Shen and James D. Lee. For the special case in which the line crack is perpendicular to one of the major loading axes, it has been found that the linear energy release rate is independent of the biaxial load factor while the nonlinear energy rate depends on it. In this paper, based on the nonlinear energy method for mixed mode fracture, the calculations for the process of the nonlinear rate of off-axis cracked lamina of composite material subjected to biaxial loading have been performed. In addition, several examples have been given to explain the influence of fiber-orientation, biaxial loading factor and how the nonlinear correction factors vary with changes of the applied load.

## INTRODUCTION
TN THE EARLY 1920'S, IN ACCORDANCE WITH THE PRINCIPLE OF MINIMUM
potential energy, A.A. Griffith [1] suggested that the unstable fracture of a center cracked plate subjected to tensile load under fixed grip is due to the decrease in total potential energy, that is, the strain energy released from the elastic cracked plate and used for inducing a new crack surface. Starting from this point, Griffith unprecedentedly set up the quantitative relation between the failure stress, the critical crack size and the material when brittle fracture begins to appear, thus laying a good foundation for the formation of the linear elastic fracture mechanics. Griffith's concept of the elastic release rate, together with that of stress intensity factor and its corresponding fracture criterion advanced by Irwin [2,3], forms the basic content of the overall system of the linear elastic fracture mechanics. In the early 70's, H. Liebowitz et al. put forward the concept of nonlinear energy rate $\tilde{G}$ [4-9] based on the first law of thermodynamics, and provided a general definition of fracture toughness applicable to semi-brittle fracture. Further, the toughness parameter $\tilde{G}_{C}$ can be determined by a single experimental load-displacement curve through the expression
196
Journal of REINFORCED PLASTICS AND COMPOSITES, Vol. 2-July 1983
0731-6844/83/03/0196-13 $04.50/0
©1983 Technomic Publishing Co., Inc.

$$
\tilde{G}=\tilde{C}G \tag{1}
$$

where $G$ is the corresponding linear elastic energy release rate which follows Irwin's G-K relation and $\tilde{C}$ is the measure of the curvature of the load-displacement curve. In fact, with a two-dimensional problem, $\tilde{G}$ has the same expression as Rice's famous J-integral [10,11]:

$$
\tilde{G}=J=-\frac{\partial \pi}{\partial A} \tag{2}
$$

where $\pi$ is the total potential energy of the cracked system, and $A$ is the crack area. It should be pointed out, however, that $\tilde{G}$ is applicable to both plane stress and plane strain conditions and can be applied to any geometry for which the stress intensity factor can be obtained. No doubt, like the J-integral, there are similar constraints for the application of $\tilde{G}$.

Shortly before, Shen and Lee further developed the nonlinear energy method [12] for mixed mode fracture subjected to a biaxial load and the results of the research are very satisfactory. Apparently, the research mentioned above was supposed to be concerned with the homogeneous and isotropic materials. The present paper is intended to propose the application of the nonlinear energy method to analyzing the mixed mode fracture of the cracked lamina of fibre-reinforced composite material. Some achievements have already been made in this respect.

## BASIC ANALYTIC METHOD

In the case of fixed grip, the general expression (2) can be written as:

$$
\tilde{G}=-\left.\frac{\partial U}{\partial A}\right|_{u} \tag{3}
$$

In the case of the fixed load,

$$
\tilde{G}=\left.\frac{\partial \Gamma}{\partial A}\right|_{F} \tag{4}
$$

where $U$ and $\Gamma$ are the strain energy and complementary energy of the cracked lamina respectively; $F$ and $u$ are the applied load and load-point displacement; $U$ and $\Gamma$ can be found by the experimental load-displacement curve.

Let's consider a simple lamina of fibre-reinforced composite material with length $2L_y$, width $2L_x$ and thickness B. Suppose there is a center-through crack with length 2a along the direction of fibre in the matrix (Figure 1) and it forms an angle $\beta$ with the axis $y$. The engineering elastic constants of the lamina are $E_1$, $E_2$, $\nu_{12}$, $\nu_{21}$ and $G_{12}$, where the subscripts 1 and 2 represent directions parallel and normal to the fibre direction, respectively. The cracked

![](./images/812016191143936001_1.jpg)

Figure 1. The configuration and load condition of a cracked lamina.

lamina is subjected to the in-plane biaxial loads $F_x$ and $F_y$, far away from the crack. The biaxial loading factor $k$ can be defined as

$$
k \equiv \frac{F_{x}}{F_{y}} \tag{5}
$$

Assuming that the loading is slowly and monotonically increased to the onset of subcritical crack growth, i.e., the quasi-static case, and the biaxial load factor remains constant in this process.

From the two experimental load-displacement curves, $F_x$-$u_x$ curve and $F_y$-$u_y$ curve (Figure 2), we can obtain the strain energy of the cracked lamina:

$$
U=\int_{0}^{u_{x}} F_{x} d u_{x}+\int_{0}^{u_{y}} F_{y} d u_{y} \tag{6}
$$

and the complementary energy of it:

$$
\Gamma=\int_{0}^{F_{x}} u_{x} d F_{x}+\int_{0}^{F_{y}} u_{y} d F_{y} \tag{7}
$$

![](./images/812016191143936001_2.jpg)

Figure 2. The typical experimental load-displacement curves.

Let the load-point displacements $u$ and $v$ be divided into linear and nonlinear parts as follows (Figure 2):

$$
u_{x} \equiv u_{x}^{e}+u_{x}^{n} \tag{8}
$$

$$
u_{y} \equiv u_{y}^{e}+u_{y}^{n} \tag{9}
$$

It is shown by tests that nonlinear displacements $(u_{x}^{n}, u_{y}^{n})$ can be expressed with the function of its linear parts $\varrho_{x}$ and $\varrho_{y}$, i.e.,

$$
u_{x}^{n} \equiv \varrho_{x}\left(u_{x}^{e}\right) \tag{10}
$$

$$
u_{v}^{n} \equiv \varrho_{y}\left(u_{y}^{e}\right) \tag{11}
$$

Substituting Eqns. (10) and (11) into Eqns. (8) and (9), we have

$$
u_{x}=u_{x}^{e}+\varrho_{x}\left(u_{x}^{e}\right) \tag{12}
$$

$$
u_{y}=u_{y}^{e}+\varrho_{y}\left(u_{y}^{e}\right) \tag{13}
$$

According to the strain-stress relation of the anisotropic material [13,14],

$$
\varepsilon_{i j}^{e}=a_{i j k l} \sigma_{k l} \tag{14}
$$

where $a_{i j k l}$ is the compliance tensor. As for the problem to be investigated

$$
\varepsilon_{x}^{e}=a_{x x} \sigma_{x x}+a_{x y} \sigma_{y y} \tag{15}
$$

$$
\varepsilon_{v}^{e}=a_{v v} \sigma_{x x}+a_{v y} \sigma_{v y} \tag{16}
$$

Obviously, the corresponding relation of displacement-load should be

$$
u_{x}^{e}=C_{x} F_{x}+C_{x v} F_{v} \tag{17}
$$

$$
u_{v}^{e}=C_{x v} F_{x}+C_{v} F_{v} \tag{18}
$$

Here $C_{x}, C_{v}$ and $C_{x v}$ can be called the compliance factors. Substituting Eqns. (17) and (18) into Eqns. (12) and (13) we have

$$
u_{x}=C_{x} F_{x}+C_{x v} F_{v}+\varrho_{x}\left(C_{x} F_{x}+C_{x v} F_{y}\right) \tag{19}
$$

$$
u_{v}=C_{x v} F_{x}+C_{v} F_{v}+\varrho_{y}\left(C_{x v} F_{x}+C_{v} F_{y}\right) \tag{20}
$$

and substituting the above into Eqn. (7) as well as Eqn. (4), we have

$$
\begin{aligned}
\tilde{G} & =\frac{1}{2 B} \frac{\partial}{\partial a}\left[\int_{0}^{F_{x}} u_{x} d F_{x}+\int_{0}^{F_{y}} u_{y} d F_{y}\right]_{F} \\
& =\frac{1}{4 B} F_{x}^{2} \frac{\partial C_{x}}{\partial a}+\frac{1}{4 B} F_{y}^{2} \frac{\partial C_{y}}{\partial a}+\frac{1}{2 B} F_{x} F_{y} \frac{\partial C_{x y}}{\partial a} \\
& +\frac{1}{2 B} \int_{0}^{F_{x}}\left[\frac{\partial \varrho_{x}}{\partial a}\right]_{F_{x}} d F_{x}+\frac{1}{2 B} \int_{0}^{F_{y}}\left[\frac{\partial \varrho_{y}}{\partial a}\right]_{F_{y}} d F_{y}
\end{aligned}
\tag{21}
$$

where

$$
\begin{aligned}
\int_{0}^{F_{x}}\left[\frac{\partial \varrho_{x}}{\partial a}\right]_{F_{x}} d F_{x}= & {\left[\frac{\varrho_{x}}{u_{x}^{e}} F_{x}^{2}-\frac{F_{x}}{u_{x}^{e}} \int_{0}^{F_{x}} \varrho_{x} d F_{x}\right] \frac{\partial C_{x}}{\partial a} } \\
+ & {\left[\frac{\varrho_{x}}{u_{x}^{e}} F_{x} F_{y}-\frac{F_{y}}{u_{x}^{e}} \int_{0}^{F_{x}} \varrho_{x} d F_{x}\right] \frac{\partial C_{x y}}{\partial a} }
\end{aligned}
\tag{22}
$$

and

$$
\begin{aligned}
\int_{0}^{F_{y}}\left[\frac{\partial \varrho_{y}}{\partial a}\right]_{F_{y}} d F_{y}= & {\left[\frac{\varrho_{y}}{u_{y}^{e}}-\frac{F_{y}}{u_{y}^{e}} \int_{0}^{F_{y}} \varrho_{y} d F_{y}\right] \frac{\partial C_{y}}{\partial a} } \\
+ & {\left[\frac{\varrho_{y}}{u_{y}^{e}} F_{x} F_{y}-\frac{F_{x}}{u_{y}^{e}} \int_{0}^{F_{y}} \varrho_{y} d F_{y}\right] \frac{\varrho C_{x y}}{\varrho a} }
\end{aligned}
\tag{23}
$$

Then, by substituting Eqns. (22) and (23) into Eqn. (21), the expression for the nonlinear energy rate $\tilde{G}$ can be finally obtained:

$$
\tilde{G}=\tilde{C}_{x} G_{x}+\tilde{C}_{y} G_{y}+\tilde{C}_{x y} G_{x y}
\tag{24}
$$

where

$$
\tilde{C}_{x}=1+\frac{1}{u_{x}^{e}}\left[\varrho_{x}-\frac{1}{F_{x}} \int_{0}^{F_{x}} \varrho_{x} d F_{x}\right]
\tag{25}
$$

$$
\tilde{C}_{y}=1+\frac{1}{u_{y}^{e}}\left[\varrho_{y}-\frac{1}{F_{y}} \int_{0}^{F_{y}} \varrho_{y} d F_{y}\right]
\tag{26}
$$

$$
\tilde{C}_{x y}=\frac{1}{2}\left(\tilde{C}_{x}+\tilde{C}_{y}\right)
\tag{27}
$$

$$
G_{x}=\frac{1}{4 B} F_{x}^{2} \frac{\delta C_{x}}{\delta a}
\tag{28}
$$

$$
G_{y}=\frac{1}{4 B} F_{y}^{2} \frac{\delta C_{y}}{\delta a}
\tag{29}
$$

$$
G_{x y}=\frac{1}{2 B} F_{x} F_{y} \frac{\delta C_{x y}}{\delta a}
\tag{30}
$$

Clearly, $G_{x}, G_{y}$ and $G_{x y}$ are three corresponding components of the linear static energy release rate and the three nonlinear correction coefficients $\tilde{C}_{x}, \tilde{C}_{y}$ and $\tilde{C}_{x y}$ can be determined with the two experimental curves, namely, $F_{x}-u_{x}$ curve and $F_{y}-u_{y}$ curve.

## Linear Elastic Case

In this section, the attention is focused on the linear elastic case for the cracked lamina of composite in which the displacement-load relations may be written as

$$
u_{x}=u_{x}^{e}=C_{x} F_{x}+C_{x y} F_{y}
\tag{31}
$$

$$
u_{y}=u_{y}^{e}=C_{x y} F_{x}+C_{y} F_{y}
\tag{32}
$$

Substitution into Eqns. (7) and (4) gives the expression for the linear elastic release rate:

$$
G=G_{x}+G_{y}+G_{x y}
\tag{33}
$$

If one assumes that the initiation of crack propagation happens along the fibre direction, then for the problem to be studied its stress intensity factor may be written as follows [15,16]:

$$
K_{1}=\left(\frac{F_{y}}{2 B L_{x}} \sin ^{2} \beta+\frac{F_{x}}{2 B L_{y}} \cos ^{2} \beta\right) a^{1 / 2}
\tag{34}
$$

$$
K_{2}=\left(\frac{F_{y}}{2 B L_{x}}-\frac{F_{x}}{2 B L_{y}}\right) \sin \beta \cos \beta \cdot a^{1 / 2}
\tag{35}
$$

The corresponding energy release rate components are

$$
G_{I}=\pi K_{1}\left(\frac{a_{11} a_{22}}{2}\right)^{1 / 2}\left[\left(\frac{a_{22}}{a_{11}}\right)^{1 / 2}+\frac{2 a_{12}+a_{66}}{2 a_{11}}\right]^{1 / 2}
\tag{36}
$$

$$
G_{I I}=\pi K_{2}\left(\frac{a_{11}^{2}}{2}\right)^{1 / 2}\left[\left(\frac{a_{22}}{a_{11}}\right)^{1 / 2}+\frac{2 a_{12}+a_{66}}{2 a_{11}}\right]^{1 / 2}
\tag{37}
$$

And the total energy release rate
$$
\begin{aligned}
G & =G_{I}+G_{I I} \\
& =\pi a \psi\left\{\frac{F_{x}^{2}}{4 B^{2} L_{y}^{2}} \cos ^{2} \beta\left[\cos ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \sin ^{2} \beta\right]\right. \\
& +\frac{F_{y}}{4 B^{2} L_{x}^{2}} \sin ^{2} \beta\left[\sin ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \cos ^{2} \beta\right] \\
& \left.+\frac{F_{x} F_{y}}{2 B^{2} L_{x} L_{y}} \sin ^{2} \beta \cos ^{2} \beta\left[1-\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2}\right]\right\}
\end{aligned}
\tag{38}
$$
where
$$
\psi \equiv\left[\left(\frac{a_{22}}{a_{11}}\right)^{1 / 2}+\frac{2 a_{12}+a_{66}}{2 a_{11}}\right]^{1 / 2}\left(\frac{a_{11} a_{22}}{2}\right)^{1 / 2}
\tag{39}
$$

Here, $a_{11}, a_{22}, a_{12}, a_{66}$ are the compliance coefficients of the lamina. If the engineering constants $E_{1}, E_{2}, v_{12}, v_{21}$ and $G_{12}$ are used to indicate the compliance coefficients, for the plane stress case, there are the following relations:
$$
a_{11}=1 / E_{1}
\tag{40}
$$

$$
a_{22}=1 / E_{2}
\tag{41}
$$

$$
a_{12}=-v_{12} / E_{1} \text { or }-v_{21} / E_{2}
\tag{42}
$$

$$
a_{66}=1 / G_{12}
\tag{43}
$$

Let's divide Eqn. (38) into three components of linear energy release rate, namely,
$$
G_{x} \equiv \frac{\pi a \psi}{4 B^{2} L_{y}^{2}} F_{x}^{2} \cos ^{2} \beta\left[\cos ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \sin ^{2} \beta\right]
\tag{44}
$$

$$
G_{y} \equiv \frac{\pi a \psi}{4 B^{2} L_{x}^{2}} F_{y}^{2} \sin ^{2} \beta\left[\sin ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \cos ^{2} \beta\right]
\tag{45}
$$

$$
G_{x y} \equiv \frac{\pi a \psi}{2 B^{2} L_{x} L_{y}} F_{x} F_{y} \sin ^{2} \beta \cos ^{2} \beta\left[1-\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2}\right]
\tag{46}
$$

Comparing Eqns. (28), (29), (30) with Eqns. (44), (45), (46) respectively, we can determine the linear elastic compliance factors and load-point displacements of the cracked lamina.

$$
\frac{\partial C_{x}}{\partial a}=\frac{\pi a \psi}{B L_{y}^{2}}\left[\cos ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \sin ^{2} \beta\right] \cos ^{2} \beta \tag{47}
$$

$$
\frac{\partial C_{y}}{\partial a}=\frac{\pi a \psi}{B L_{y}^{2}}\left[\sin ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \cos ^{2} \beta\right] \sin ^{2} \beta \tag{48}
$$

$$
\frac{\partial C_{x y}}{\partial a}=\frac{\pi a \psi}{B L_{x} L_{y}}\left[1-\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2}\right] \sin ^{2} \beta \cos ^{2} \beta \tag{49}
$$

Integrating the above three equations, we have

$$
C_{x}=C_{x}(0)+\frac{\pi a \psi}{2 B L_{y}^{2}}\left[\cos ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \sin ^{2} \beta\right] \cos ^{2} \beta \tag{50}
$$

$$
C_{y}=C_{y}(0)+\frac{\pi a \psi}{2 B L_{x}^{2}}\left[\sin ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \cos ^{2} \beta\right] \sin ^{2} \beta \tag{51}
$$

$$
C_{x y}=C_{x y}(0)+\frac{\pi a \psi}{2 B L_{x} L_{y}}\left[1-\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2}\right] \sin ^{2} \beta \cos ^{2} \beta \tag{52}
$$

where $C_{x}(0), C_{y}(0), C_{x y}(0)$ are the compliance factors for the uncracked lamina with the same sizes and their expressions may be given as follows:

$$
C_{x}(0)=\frac{L_{x}}{B L_{y}}\left[a_{11} \sin ^{4} \beta+\left(2 a_{12}+a_{66}\right) \sin ^{2} \beta \cos ^{2} \beta+a_{22} \cos ^{4} \beta\right], \tag{53}
$$

$$
C_{y}(0)=\frac{L_{y}}{B L_{x}}\left[a_{11} \cos ^{4} \beta+\left(2 a_{12}+a_{66}\right) \sin ^{2} \beta \cos ^{2} \beta+a_{22} \sin ^{4} \beta\right], \tag{54}
$$

$$
C_{x y}(0)=\frac{1}{B}\left[a_{11}\left(\sin ^{4} \beta+\cos ^{4} \beta\right)+\left(a_{11}+a_{12}-a_{66}\right) \sin ^{2} \beta \cos ^{2} \beta\right]. \tag{55}
$$

Now let's substitute Eqns. (50), (51), (52) into Eqns. (31), (32) and the load-point linear elastic displacements can be obtained:

$$
\begin{aligned}
u_{x}^{e}= & \left\{C x(0)+\frac{\pi a^{2} \psi}{2 B L_{v}^{2}}\left[\cos ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \sin ^{2} \beta\right] \cos ^{2} \beta\right\} F_{x} \\
& +\left\{C_{x y}(0)+\frac{\pi a^{2} \psi}{2 B L_{x} L_{y}}\left[1-\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \sin ^{2} \beta \cos ^{2} \beta\right\} F_{y}\right.
\end{aligned} \tag{56}
$$

and
$$
\begin{aligned}
u_{y}^{e}= & \left\{C_{x y}(0)+\frac{\pi a^{2} \psi}{2 B L_{x} L_{y}}\left[1-\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2}\right] \sin ^{2} \beta \cos ^{2} \beta\right\} F_{x} \\
& +\left\{C_{y}(0)+\frac{\pi a^{2} \psi}{2 B L_{x}^{2}}\left[\sin ^{2} \beta+\left(\frac{a_{11}}{a_{22}}\right)^{1 / 2} \cos ^{2} \beta\right] \sin ^{2} \beta\right\} F_{y}
\end{aligned}
\tag{57}
$$

## Determination of the Nonlinear Correction Coefficients
With the expression (4) as its basis, the nonlinear energy rate $\tilde{G}$ may be obtained using its three corresponding linear components ($G_x$, $G_y$ and $G_{xy}$) to multiply the three nonlinear coefficients ($\tilde{C}_x$, $\tilde{C}_y$, $\tilde{C}_{xy}$) respectively and to find their sum. With one of the following three methods, the nonlinear correction coefficients may be determined:

### 1. Suppose
$$
u_{x}^{n}=\varrho_{x}\left(u_{x}^{e}\right)=\sum_{m=2}^{M} \gamma_{m}\left(u_{x}^{e}\right)^{m}
\tag{58}
$$

$$
u_{y}^{n}=\varrho_{y}\left(u_{y}^{e}\right)=\sum_{m=2}^{M} \delta_{m}\left(u_{y}^{e}\right)^{m}
\tag{59}
$$

Substitution into Eqns. (25), (26) and (27) yields
$$
\tilde{C}_{x}=1+\sum_{m=2}^{M} \gamma_{m} \frac{2 m}{1+m}\left(u_{x}^{e}\right)^{m-1}
\tag{60}
$$

$$
\tilde{C}_{y}=1+\sum_{m=2}^{M} \delta_{m} \frac{2 m}{1+m}\left(u_{y}^{e}\right)^{m-1}
\tag{61}
$$

$$
\tilde{C}_{x y}=\frac{1}{2}\left(\tilde{C}_{x}+\tilde{C}_{y}\right)
\tag{62}
$$

where $u_{x}^{e}$ and $u_{y}^{e}$ can be obtained by Eqns. (56) and (57). The coefficients $\gamma_{m}$ and $\delta_{m}$ of the polynomial forms (Eqns. (58), (59)) can be found by the least square method according to the load-displacement curves (or stress-strain curve) of the test.

### 2. Suppose

$$
u_{x}^{n}=\varrho_{x}\left(u_{x}^{e}\right)=\alpha_{1}\left(u_{x}^{e}\right)^{p} \tag{63}
$$

$$
u_{y}^{n}=\varrho_{y}\left(u_{y}^{e}\right)=\alpha_{2}\left(u_{y}^{e}\right)^{q} \tag{64}
$$

Substituting the above into Eqns. (25), (26) and (27), we have

$$
\tilde{C}_{x}=1+\frac{2 \alpha_{1} p}{1+p}\left(u_{x}^{e}\right)^{p-1} \tag{65}
$$

$$
\tilde{C}_{y}=1+\frac{2 \alpha_{2} p}{1+q}\left(u_{y}^{e}\right)^{q-1} \tag{66}
$$

$$
\tilde{C}_{x y}=\frac{1}{2}\left(\tilde{C}_{x}+\tilde{C}_{y}\right) \tag{67}
$$

where $p>1$, $q>1$, $\alpha_{1}>0$, $\alpha_{2}>0$ and are determined by the three-parameter method with the two load-displacement curves.

3. Some simplifications can be made of Eqn. (25), i.e.,

$$
\begin{aligned}
\tilde{C}_{x} & =1+\frac{2}{u_{x}^{e}}\left(\varrho_{x}^{n}-\frac{1}{F_{x}} \int_{0}^{F_{x}} \varrho_{x} d F_{x}\right) \\
& =\frac{F_{x}^{e}+2\left(F_{x} \varrho_{x}^{n}-\int_{0}^{F_{x}} \varrho_{x} d F_{x}\right)}{F_{x} u_{x}^{e}} \\
& =\frac{1 / 2 F_{x} u_{x}^{e}+F_{x} \varrho_{x}^{n}-\int_{0}^{F_{x}} \varrho_{x} d F_{x}}{1 / 2 F_{x} u_{x}^{e}}=\frac{A_{x}}{A_{x}^{e}}
\end{aligned} \tag{68}
$$

Similarly, Eqn. (26) can be simplified as

$$
\tilde{C}_{y}=\frac{A_{y}}{A_{y}^{e}} \tag{69}
$$

and

$$
C_{x y}=\frac{1}{2}\left(\frac{A_{x}}{A_{x}^{e}}+\frac{A_{y}}{A_{y}^{e}}\right) \tag{70}
$$

where $A_{x}^{e}$, $A_{x}$, $A_{y}^{e}$, $A_{y}$ are, in fact, equal to the pertinent areas indicated in the two load-displacement curves (Fig. 3). $A_{x}$ and $A_{y}$ are the two strain energy components of the cracked lamina while $A_{x}^{e}$ and $A_{y}^{e}$ are the corresponding

![](./images/812016191143936001_3.jpg)

Figure 3. The geometric expression of the nonlinear correction coefficients.

parts of the linear elastic strain energy. Eqns. (69) and (70) indicate that the nonlinear correction coefficients $\tilde{C}_{x}$ and $\tilde{C}_{y}$ are just equal to the ratio of the strain energy of the cracked lamina to its proper linear elastic parts, and that $\tilde{C}_{x y}$ equals half of the sum of the two coefficients mentioned above.

Examples

In order to expound the problem, we take the cracked lamina of the composite material T300/5208 graphite-epoxy as an example. Its engineering elastic constants are: $E_{1}=181$ Gpa, $E_{2}=10.3$ Gpa, $G_{12}=7.17$ Gpa, $\nu_{12}=$ 0.28. The following are the results of the calculation of some special problems:

1. Influence of the fibre orientation
Suppose the width of lamina $2 \mathrm{~L}_{\mathrm{x}}$ is $0.6 \mathrm{~m}$, its length $2 \mathrm{~L}_{\mathrm{y}}$ also $0.6 \mathrm{~m}$, thickness $0.0025 \mathrm{~m}$; crack length $2 \mathrm{a}=0.1 \mathrm{~m}$, applied force $\mathrm{F}_{\mathrm{y}}$ is $0.331 \mathrm{MN}$, biaxial load factor $\mathrm{k}$ is 0.5 . For different fibre orientations $\left(\beta=0^{\circ}-90^{\circ}\right)$, the three components $G_{x}, G_{y}$, and $G_{x y}$ and the total linear elastic energy release rate $\mathrm{G}$ calculated are shown in Figure 4.

Obviously, the fibre orientation exerts an influence on the energy release rate and its three components. $G_{x}$ decreases as $\beta$ increases; $G_{y}$ increases as $\beta$ increases; and $G_{x y}$ takes its maximum at $\beta=45^{\circ}$ while $G_{x y}=0$ at $\beta=0$ or $90^{\circ}$. The total energy release rate $\mathrm{G}$ increases as $\beta$ does.

![](./images/812016191143936001_4.jpg)

Figure 4. Influence of the fibre orientation.

![](./images/812016191143936001_5.jpg)

Figure 5. Influence of the biaxial loading factor.

### 2. Influence of the biaxial loading factor
Regarding the cracked lamina mentioned above, we suppose that $\beta=45^{\circ}$ and $k=-2-+2$. Through calculations we find that $G_{x}, G_{y}, G_{x y}$ and $G$ vary with the biaxial loading factor k (Figure 5). We can see in Figure 5 that $F_{y}$ is taken as a constant, therefore $G_{y}=$ constant. $G_{x}$ has its minimum at $\mathrm{k}=0$; the increase of k's absolute value increases as $\mathrm{G}_{\mathrm{x}}$ increases. $\mathrm{G}_{\mathrm{xy}}=0$ at $\mathrm{k}=0$ while we have $\mathrm{G}_{\mathrm{xy}}>0$ when $\mathrm{k}>0$ and $\mathrm{G}_{\mathrm{xy}}<0$ when $\mathrm{k}<0$. The total linear elastic energy release rate $\mathrm{G}$ takes its minimum when $\mathrm{k}=0$; $\mathrm{G}$ will increase when the absolute value of $\mathrm{k}$ increases, i.e., $\left|\mathrm{F}_{\mathrm{x}}\right|$ increases.

### 3. Influence of nonlinearity
The size of the cracked lamina is the same as that of the previous one. Suppose $\beta=45^{\circ}, \mathrm{k}=0$. We use the stress-strain relation of the unidirectional composite material provided in the reference [14] to calculate and the nonlinear correction coefficient $\tilde{\mathrm{C}}=\mathrm{f}\left(\mathrm{F}_{\mathrm{y}}\right)$ can be shown in Figure 6. Apparently, the $\tilde{\mathrm{C}}$ here will increase as $\mathrm{F}_{\mathrm{y}}$ does. The $\tilde{\mathrm{C}}$ value in the case of tension is different from the compression case since the extent of nonlinearity of their stress-strain relation is different.

![](./images/812016191143936001_6.jpg)

Figure 6. Influence of nonlinearity.

## REFERENCES

1. Griffith, A.A., "Philosophical Transaction of the Royal Society of London," Series A, Vol. 221, pp. 163-198 (1921).
2. Irwin, G.R., "Transaction of ASME," J. of Applied Mechanics, Vol. 24, pp. 361-364 (1957).
3. Irwin, G.R., "Transaction of ASME," J. of Bas. Eng., pp. 417-425 (1960).
4. Liebowitz, H. and Eftis, J., Eng. Fracture Mech., Vol. 3, p. 267 (1971).
5. Liebowitz, H. and Jones, D.L., 10th Ann. Meet. Soc. Eng. Sci., Raleigh, North Carolina (1973).
6. Jones, D.L., Liebowitz, H. and Eftis, J., Eng. Fracture Mech., Vol. 6 (1974).
7. Eftis, J. and Liebowitz, H. Eng. Fracture Mech., Vol. 7 (1975).
8. Jones, D.L., Poulose, P.K., Eftis J. and Liebowitz, H., Eng. Fracture Mech., Vol. 10 (1978).
9. Jones, D.L., Lee, J.D. and Liebowitz, H., Advances in Fracture Research (5th International Conference on Fracture), Vol. 4, edited by D. Francois, p. 1769 (1981).
10. Rice, J.R., J. of Applied Mech., Trans. of ASME, pp. 379-386 (1968).
11. Rice, J.R., Fracture, Vol. II, H. Liebowitz Ed., pp. 191-311 (1968).
12. Shen, W. and Lee, J.D., Eng. Fracture Mech., Vol. 6 (1982).
13. Tsai, S.W. and Hahn, H.T., Introduction to Composite Materials, Technomic Publishing Co. (1980).
14. Agarwal, B.D. and Broutman, L.J., Analysis and Performance of Fibre Composites, A Wiley-Inter-Science publication (1980).
15. Sih, G.C. and Liebowitz, H., Fracture, Vol. II, H. Liebowitz Ed., (1968).
16. Sih, G.C., Handbook of Stress Intensity Factor, Institute of Fracture and Solid Mechanics, Lehigh Univ. (1975).