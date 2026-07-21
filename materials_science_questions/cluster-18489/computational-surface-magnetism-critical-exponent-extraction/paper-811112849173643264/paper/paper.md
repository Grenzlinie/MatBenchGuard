# Mean-field theory of magnetic transitions in semi-infinite Ising models
F. Aguilera-Granja
Departamento de Física, Centro de Investigación y de Estudios Avanzados del Instituto Politécnico Nacional,
Apartado Postal 14-740 07000 México Distrito Federal, México

J. L. Morán-López*
Laboratoire de Magnétisme et de Structure Electronique des Solides, Université Louis Pasteur,
4 rue Blaise Pascal, 67070 Strasbourg Cedex, France

(Received 13 November 1984)

The semi-infinite Ising model, for $S=\frac{1}{2}$ and with an arbitrary number of surface magnetic couplings $J_{mn}$ different from the bulk $J$, is solved in the mean-field approximation. Exact expressions for the critical couplings $J_{mn,C}$ leading to a surface Curie temperature $T_{CS}$ higher than the bulk $T_C$ are obtained. The value for $T_{CS}$ in the semi-infinite crystal is obtained by means of a continued-fraction method. The model is applied to explain recent experimental results on the (0001) surface of gadolinium.

## I. INTRODUCTION
It is well established $^{1-7}$ that surface magnetic properties may differ from those in the bulk. This is naturally expected since the surface atoms are embedded in a lower symmetry environment and consequently the exchange constants between atoms in the surface region may differ from the bulk value. However, for simplicity, and in the absence of experimental data, most of the theoretical analysis have been performed under the assumption that only the exchange constant of atoms at the surface plane $J_{00}$ differs for the bulk $J$, and for the (100) surface of a simple cubic lattice.

Depending on the value of $J_{00}$, two different behaviors at the surface can be obtained: (i) If $J_{00}$ is smaller than a critical value $J_{00,C}$, the surface will order at the temperature where the bulk does (ordinary transition); and (ii) If $J_{00}>J_{00,C}$, the surface will disorder at a temperature $T_{CS}$ (surface transition) larger than the bulk transition temperature $T_C$ (extraordinary transition). In the last case, for $T_C<T<T_{CS}$, the magnetization decays exponentially into the bulk with a characteristic length.

The experimental study of magnetic surfaces is very difficult and only few experimental results are available. Nickel and iron seem to correspond to the first kind of systems $^{8,9}$ discussed above and gadolinium is the only system reported $^{10,11}$ with a surface Curie temperature larger than the bulk $T_C$. To explain the experimental findings in Gd, it has been proposed $^{11}$ that not only the surface coupling constant $J_{00}$ differs from the bulk $J$ but also the coupling constant between atoms in the first and second plane $J_{01}$.

Here, within the mean-field approximation, we present a new method for obtaining exact expressions for the critical coupling constants in the surface region. Formalism is valid for any number of $J_{ij}$ differing from $J$. We present results for various cases. In Sec. II we outline the theory. The results, the discussion, and the application of the method to Gd are contained in Sec. III.

## II. THEORY
The magnetic properties of the semi-infinite system are described by the Ising model with spin $\frac{1}{2}$. The crystal is subdivided into planes parallel to the surface. The coordination number of the planes parallel to the surface and between planes are denoted by $Z_0$ and $Z_1$, respectively, and $N_{\|}$ represents the total number of atoms per plane.

The magnetic couplings are assumed to be location dependent and we denote by $J_{mn}$ the coupling between spins in the $m$ and $n$ layers. In the single-site approximation, there are two different probabilities per plane and they are denoted by $P_{i,\sigma}$, where $i=0,1,2,\dots$ and $\sigma=\uparrow,\downarrow$. The magnetic long-range order parameter at the $i$th plane is defined by
$$
\eta_{i} \equiv P_{i, \uparrow}-P_{i, \downarrow}. \tag{2.1}
$$

The equilibrium values for the order parameters are obtained by minimizing the free energy, which in terms of the order parameters is given by
$$
\begin{aligned}
F=N_{\|}\left\{\sum_{i=0}^{\infty}\right. & \left(-\frac{Z_{0}}{2} J_{i i} \eta_{i}^{2}-Z_{1} J_{i, i+1} \eta_{i} \eta_{i+1}\right. \\
+ & k_{B} T \sum_{i=0}^{\infty}\left[\frac{1+\eta_{i}}{2} \ln \left(\frac{1+\eta_{i}}{2}\right)\right. \\
& \left.\left.+\frac{1-\eta_{i}}{2} \ln \left(\frac{1-\eta_{i}}{2}\right)\right]\right\}. \tag{2.2}
\end{aligned}
$$

Here, $J_{ij}>0$ ($<0$) means ferromagnetic (antiferromagnetic) coupling. The minimization of the free energy
---
©1985 The American Physical Society

$$
\frac{\partial F}{\partial \eta_{i}}=0, \quad i=0,1, \ldots
\tag{2.3}
$$
leads to the coupled set of equations, for $i=1,2, \ldots$,
$$
\begin{aligned}
-2\left(Z_{0} J_{00} \eta_{0}+Z_{1} J_{01} \eta_{1}\right)+k_{B} T \ln \left(\frac{1+\eta_{0}}{1-\eta_{0}}\right) & =0, \\
\ldots & \\
-2\left(Z_{1} J_{i-1} \eta_{i-1}+Z_{0} J_{i i} \eta_{i}\right. & \\
\left.+Z_{1} J_{i+1} \eta_{i+1}\right)+k_{B} T \ln \left(\frac{1+\eta_{i}}{1-\eta_{i}}\right) & =0,
\end{aligned}
\tag{2.4}
$$

Deep inside the bulk, the temperature dependence of the bulk $\eta$ is given by the relation
$$
2 Z J \eta-k_{B} T \ln \left(\frac{1-\eta}{1-\eta}\right)=0
\tag{2.5}
$$
and the Curie temperature is
$$
k_{B} T_{C}=Z J.
\tag{2.6}
$$

Here, $Z=Z_{0}+2 Z_{1}$ is the bulk coordination number.

As was mentioned in the Introduction, depending on the values of the coupling constants near the surface, the
$$
\left(Z_{0}, J_{00, C}-Z J\right)\left[\left(Z_{0} J_{11, C}-Z J\right)\left(Z_{1} J\right)^{n-2} D_{n-2}-\left(Z_{1} J\right)^{n-1} D_{n-3}\right]-\left(Z_{1} J_{01, C}\right)^{2}\left(Z_{1} J\right)^{n-2} D_{n-2}=0,
\tag{2.11}
$$
where
$$
D_{m}=\left|\begin{array}{cccc}
-2 & 1 & 0 & \cdots \\
1 & -2 & 1 & \\
\vdots & & &
\end{array}\right|
\tag{2.12}
$$
is a determinant of order $m$, whose value is
$$
D_{m}=(-1)^{m}(m+1).
\tag{2.13}
$$

Therefore, for $n \geq 2$, the critical coupling constants are given by the relation
$$
\frac{Z J-Z_{0} J_{00, C}}{Z_{1} J}\left(\frac{Z J-Z_{0} J_{11, C}}{Z_{1} J}-\frac{n-2}{n-1}\right)=\left(\frac{J_{01, C}}{J}\right)^{2}.
\tag{2.14}
$$

This result is valid under the assumption that the magnetization in the $n$ planes near the surface differs from the bulk value. For $n \rightarrow \infty,(n-2) /(n-1) \rightarrow 1$.

Equation (2.14) determines the critical surface of the multicritical transitions in the parameter space of $J$. A system with values $(J_{00}, J_{01}, J_{11})$ lying inside the surface will disorder at the same temperature as the bulk does. On the other hand, if the set of $J$ lies outside the surface, it will disorder at $T_{CS}>T_{C}$. In the second case, the surface critical temperature $T_{CS}$ is obtained from surface Curie temperature $T_{CS}$ is equal to or larger than the bulk $T_{C}$. The set of values for the coupling constants separating these two behaviors are denoted by $J_{m n, C}$.

Near the surface Curie temperature, the logarithmic functions in Eq. (2.4) can be written as a series in powers of $\eta_{i}$. Keeping only the linear terms we obtain the homogeneous set of equations
$$
\underline{A} \underline{\eta}=0,
\tag{2.7}
$$
where the infinite matrix $\underline{A}$ is symmetric and tridiagonal with elements
$$
A_{m n}=\left(k_{B} T_{C S}-Z_{0} J_{m m}\right) \delta_{m, m}-Z_{1} J_{m n}\left(\delta_{m+1, n}+\delta_{m, n+1}\right).
\tag{2.8}
$$

The critical values for $J$ leading to the special transition, where $T_{CS}=T_{C}=Z J$, are obtained from the condition
$$
\operatorname{det} \underline{A}=0.
\tag{2.9}
$$

To calculate the determinant of the infinite matrix we first calculate the determinant of a matrix $n \times n$ and then take the limit $n \rightarrow \infty$. In principle one can take any number of $J_{m n}$ different from bulk $J$. Here, we illustrate the method for
$$
J_{m n} \neq J, \quad m, n=0,1.
\tag{2.10}
$$

In this case, we can write Eq. (2.9) in the form
$$
\operatorname{det}\left(\underline{B}-k_{B} T_{C S} \underline{1}\right)=0,
\tag{2.15}
$$
where
$$
B_{m n}=Z_{0} J_{m m} \delta_{m n}+Z_{1} J_{m n}\left(\delta_{m+1, n}+\delta_{m, n+1}\right). \quad(2.16)
$$

By assuming only $J_{00}, J_{01}, J_{11} \neq J$, the determinant (2.15) can be rewritten in the form
$$
\left|\begin{array}{cccccc}
x-a & -c & 0 & 0 & \cdots \\
-c & x-b & -1 & 0 & & \\
0 & -1 & x & -1 & 0 \\
0 & 0 & -1 & x & -1 & 0 \\
\vdots & & & & &
\end{array}\right|=0,
\tag{2.17}
$$
where
$$
\begin{aligned}
& x=\frac{k_{B} T_{C S}-Z_{0} J}{Z_{1} J}, \quad a=\frac{Z_{0}\left(J_{00}-J\right)}{Z_{1} J}, \\
& b=\frac{Z_{0}\left(J_{11}-J\right)}{Z_{1} J}, \quad c=\frac{J_{01}}{J}.
\end{aligned}
\tag{2.18}
$$

Equation (2.17) can be written in the form
$$
(x-a)\left((x-b) \frac{\mathscr{D}_{n-2}}{\mathscr{D}_{n-3}}-1\right)-c^{2} \frac{\mathscr{D}_{n-2}}{\mathscr{D}_{n-3}}=0, \quad(2.19)
$$

where
$$
\mathscr{D}_{m}=\left|\begin{array}{ccccc}
x & -1 & 0 & \cdots & \\
-1 & x & -1 & 0 & \\
0 & -1 & x & -1 & 0 \\
\vdots & & & &
\end{array}\right|
\tag{2.20}
$$
is a determinant of order $m$. Furthermore, the ratio $\mathscr{D}_{m} / \mathscr{D}_{m-1}$ is given in terms of lower dimensionality determinants by the relation
$$
\frac{\mathscr{D}_{m}}{\mathscr{D}_{m-1}}=x-\frac{1}{\mathscr{D}_{m-1} / \mathscr{D}_{m-2}}.
\tag{2.21}
$$
for $m \rightarrow \infty$ the value of the continued fraction (2.21) can be obtained by defining
$$
\gamma=\frac{\mathscr{D}_{m}}{\mathscr{D}_{m-1}},
\tag{2.22}
$$
which, substituted in Eq. (2.21), gives the equation
$$
\gamma^{2}-x \gamma+1=0.
\tag{2.23}
$$

Thus, the surface critical temperature $T_{C S}$ is given by the root of the equation
$$
\begin{aligned}
b x^{3}-\left(1-c^{2}+2 a b+b^{2}\right) x^{2}+ & {\left[2 a\left(a b-c^{2}\right)(a+2 b)\right] x } \\
& -a^{2}-(a b-c)^{2}=0, \quad(2.24)
\end{aligned}
$$
which is obtained by substituting $\gamma$ in Eq. (2.19).

## III. RESULTS AND DISCUSSION
The question of surface critical coupling constants has been addressed by several authors. $^{1-7,12-14}$ However, most of those studies have been done in the (100) surface of a simple-cubic crystal by assuming that only $J_{00} \neq J$ or $J_{00}, J_{01} \neq J$. Under those circumstances our theory reduces to those published in Refs. 1 and 5, respectively.

Here, we treat the most general case with specific results for the situation where $J_{00}, J_{01}$, and $J_{11} \neq J$ [see Fig. 1(a)]. The critical surface of multicritical transitions in the $(J_{00}, J_{01}, J_{11})$ parameter space is given by Eq. (2.14). Assuming that the magnetization of an infinite number of planes differs from the bulk $(n \to \infty)$ and for the particular case of the (111) surface of a fcc crystal [similar effects are expected at the (0001) surface of a hcp crystal], the critical surface is given by
$$
6\left(2-\frac{J_{00, C}}{J}\right)\left(1-\frac{2 J_{11, c}}{3 J}\right)=\left(\frac{J_{01, C}}{J}\right)^{2}.
\tag{3.1}
$$

A section of the critical surface is shown in Fig. 2. It is symmetrical in $J_{01, C}$, i.e., the critical values for $J_{00}$ and $J_{01}$ are the same for ferromagnetic or antiferromagnetic coupling between the substrate $(n=1)$ and the uppermost plane $(n=0)$ [see Fig. 1(b)].

This simple model allows us to treat a variety of special subsystems. The case of $J_{01}=0$ corresponds to an isolated two-dimensional layer with $T_{CS}=Z_{0} J_{00}$ and a fcc crystal in which only the uppermost layer, in this case $n=1$, is considered to have different magnetic couplings. This case is shown in Fig. 1(c). Since $2 Z_{0}=Z=12$, it is necessary that $J_{00}=2 J$ in order to obtain $T_{CS}=T_{C}$. Furthermore, for this situation the critical value for $J_{11}$ is 1.5. Three other special cases can be obtained. They are illustrated in Figs. 1(d) to 1(f). The highest value for the critical coupling constants $(J_{01}=12^{1 / 2} J)$ corresponding to the case 1(f) where the zeroth and first layers interact magnetically only with neighbors in the adjacent layers.

![](./images/811112849173643264_1.jpg)

FIG. 1. Illustration of the various surface systems that can be obtained with particular values of the coupling exchange constants $J_{00}, J_{01}$ , and $J_{11}$.

In Fig. 3, we show the surface critical temperature as a function of $J_{00}$ and $J_{01}$ for the case where $J_{11}=J$. The origin is chosen at $(1,1,1)$. Any system with values $(J_{00}/J,J_{01}/J)$ inside the boundary at $T_{CS}/T_{C}=1$ will show an ordinary transition $(T_{CS}=T_{C})$. The critical boundary depends on the number assumed to have a different magnetization from the bulk. We present in Fig. 4 results for $n=2,4$, and $\infty$. One can see that for small values of $J_{01}$, the critical value $J_{00, C}$ is almost independent of $n$. This is because in this case, the surface layer behaves like a quasi-two-dimensional system. This is not

![](./images/811112849173643264_2.jpg)

FIG. 2. A section of the critical surface in the $(J_{00}/J,J_{01}/J,J_{11}/J)$ parameter space for a (111) surface of a fcc crystal $(Z_{0}=6, Z_{1}=3)$.

![](./images/811112849173643264_3.jpg)

FIG. 3. The surface critical temperature as a function of $J_{00}/J$ and $J_{01}/J$ for a system with $J_{11}=J$, assuming an infinite number of planes different from the bulk.

the case for small $J_{00}$, where the surface layer orders be- cause of the adjacent coupling to the substrate. For the extreme case of $J_{00}=0$

$$
J_{01, C}(n)-J_{01, C}(\infty) \approx J / n. \tag{3.2}
$$

We also analyzed the dependence of $T_{CS}/T_{C}$ on $J_{00}$ and $J_{01}$ along three different trajectories: (a) $J_{01}=J$, i.e., only $J_{00} \neq J$; (b) $J_{00}=\alpha^{2} J$ and $J_{01}=\alpha J$, where $\alpha^{2}=\frac{4}{3}$ is obtained from Eq. (2.14); and (c) $J_{00}=J_{01}$. The results are displayed in Fig. 5, which are particular cases of the general curve⁵

$$
\left(1-c^{2}\right) x^{2}-a\left(2-c^{2}\right) x+\left(a^{2}+c^{4}\right)=0. \tag{3.3}
$$

![](./images/811112849173643264_4.jpg)

FIG. 4. The boundary for $T_{CS}=T_{C}$ (below the curves) and $T_{CS}>T_{C}$ (above the curves) assuming 2,4, and an infinite number of layers differing from the bulk. These results correspond also to the case $J_{11}=J$. The trajectories $a, b$, and $c$ correspond to the three different models discussed in the text.

![](./images/811112849173643264_5.jpg)

FIG. 5. The surface critical temperature as a function of $J_{00}/J$ for (a) $J_{01}=J, J_{11}=J$; (b) $J_{01}=2 J / \sqrt{3}, J_{11}=J$; and (c) $J_{01}=J_{00}, J_{11}=J$.

![](./images/811112849173643264_6.jpg)

FIG. 6. Experimental results (Ref. 11) for the magnetization in the (0001) direction of gadolinium (upper figure). SPLEED denotes spin polarized low-energy electron-diffraction measure- ment. Calculated temperature dependence of the average surface magnetization $\eta^{*}=\eta_{0}+\eta_{1}+\eta_{2}$ (solid line) and $\eta^{*}=\eta_{0}+2 \eta$ (dashed line). The long-dashed line is the absolute value of the magnetization above the bulk $T_{C}$ that would be seen experimen tally. The values taken for the magnetic couplings are $J_{00}=1.645 J$ and $J_{0}=-1.282 J$.

The most simple case, treated by other authors, $^{1,2}$ corresponds to $c=1$. The three trajectories are shown also in Fig. 4.

Recently, it has been observed $^{11}$ in polarized-low-energy-electron-diffraction experiments that the Curie temperature at the (0001) surface of gadolinium is $7.5\%$ higher than the bulk $T_{C}$. Furthermore, it has been observed that the temperature dependence of the surface magnetization shows a kind of compensation point at a temperature $T_{\text{comp}}<T_{C}$ (see Fig. 6). A possible explanation of this behavior, given by the authors, $^{11}$ is that the surface layer couples in an antiferromagnetic way to the rest of the system.

The most appropriate model for describing the magnetization of Gd is the Heisenberg Hamiltonian. However, we expect that the general conclusions obtained by applying this simple Ising theory to Gd hold also for systems with larger spins.

In contrast to other more sophisticated models, like Monte Carlo, $^{12}$ renormalization group, $^{13,14}$ etc., we can estimate in a simple way the values necessary to obtain the observed behavior. In the three models discussed above with $J_{00}$ and $J_{01}$ as parameters, we obtain (a) $J_{00}=1.845$, $J_{01}=-J$; (b) $J_{00}=1.645J$, $J_{01}=-1.282$; and (c) $J_{00}=-J_{01}=1.485$.

To calculate the magnetization at the different surface layers, it is necessary to solve the nonlinear set of equations (2.4). In principle, one should take an infinite number of equations. However, in second-order phase transitions, the magnetizations at plane $n$ and in the bulk differ by a very small amount for $n\sim4,5$. Therefore, we calculate the magnetization for values of the parameters corresponding to case (b) assuming only four layers differing from the bulk. The results for two average magnetizations,
$$\eta^{*}=\eta_{0}+\eta_{1}+\eta_{2} \text{ (solid line)}\tag{3.4}$$
and
$$\eta^{*}=\eta_{0}+2\eta \text{ (dashed line)},\tag{3.5}$$
are shown in the lower part of Fig. 6. The long-dashed line shows how the magnetization would be measured in an experiment. We present in the upper part of the figure the experimental results for comparison. We see that the results are better reproduced by Eq. (3.5). This could be an indication that the antiferromagnetic coupling between the two uppermost layers is very small and therefore the contribution to the average magnetization of the semi-infinite solid up to layer one in the range $T_{C}<T<T_{CS}$ is negligible.

## ACKNOWLEDGMENTS
The authors acknowledge the kind of hospitality and support from the Institut für Festkörperforschung der K.F.A. Jülich, Germany, where this investigation was started. We are grateful to Dr. S. F. Alvarado and Dr. D. Weller for communicating their results prior to publication and to Dr. F. Mejia-Lira for stimulating discussions. This work was partially supported by Consejo Nacional del Sistema de Educación Tecnológica de la Secretaria de Educación Pública and Consejo Nacional de Ciencia y Tecnología (México). The Laboratoire de Magnétisme et de Structure Électronique des Solides (LMSES) is "Laboratoire associé au CNRS," No. 306. One of the authors (J.L.M.-L.) acknowledges support from the John Simon Guggenheim foundation.

*On leave from Departamento de Física, Centro de Investigación y Estudios Avanzados del Instituto Politécnico Nacional, Apartado Postal 14-740, 07000 México, Distrito Federal, México.

$^{1}$D. L. Mills, Phys. Rev. B 3, 3887 (1971).
$^{2}$K. Binder and P. C. Hohenberg, Phys. Rev. B 6, 3461 (1972).
$^{3}$M. N. Barber, Phys. Rev. B 8, 407 (1973).
$^{4}$F. Yndurain, Phys. Lett. 62A, 93 (1977).
$^{5}$T. W. Burkhardt and E. Eisenriegler, Phys. Rev. B 16, 3213 (1977).
$^{6}$K. Binder, in *Phase Transitions and Critical Phenomena*, edited by C. Domb and J. L. Lebowitz (Academic, New York, 1983), Vol. 8.
$^{7}$F. Aguilera-Granja, J. L. Morán-López, and J. Urías, Phys. Rev. B 28, 3909 (1983).
$^{8}$R. J. Celotta, D. T. Pierce, G. C. Wang, S. D. Bader, and G. P. Felcher, Phys. Rev. Lett. 43, 728 (1979).
$^{9}$S. F. Alvarado, M. Campagna, and H. Hopster, Phys. Rev. Lett. 48, 51 (1982).
$^{10}$C. Rau and S. Eichner, *Springer Series in Chemical Physics* (Springer, New York, 1981), Vol. 17, p. 138.
$^{11}$D. Weller, S. F. Alvarado, W. Gudat, K. Schröder, and M. Campagna, Phys. Rev. Lett. 54, 1555 (1985).
$^{12}$K. Binder and D. P. Landau, Phys. Rev. Lett. 52, 318 (1984).
$^{13}$E. F. Sarmento and C. Tsallis, J. Phys. C (to be published).
$^{14}$H. W. Diehl, S. Dietrich, and E. Eisenriegler, Phys. Rev. B 27, 2937 (1982).