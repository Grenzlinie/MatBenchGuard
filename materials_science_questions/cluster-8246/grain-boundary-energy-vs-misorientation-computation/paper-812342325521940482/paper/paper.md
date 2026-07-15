# Planar dislocation interactions in anisotropic media with applications to nodes

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1973 J. Phys. F: Met. Phys. 3 1659

(http://iopscience.iop.org/0305-4608/3/9/007)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

Download details:

IP Address: 130.237.29.138
This content was downloaded on 17/08/2015 at 14:22

Please note that [terms and conditions apply]().

# Planar dislocation interactions in anisotropic media with applications to nodes

R J Asaro and J P Hirth

Metallurgical Engineering, The Ohio State University, Columbus, Ohio 43210, USA

Received 18 April 1973

Abstract. A simple graphical technique for solving planar dislocation interaction problems, based on recent theoretical advances in anisotropic dislocation theory, is presented. The method is quite efficient since it limits numerical computation to the generation of a set of tables of energy factor data. As an example, the method is applied to the problem of disloca- tion nodes and networks in bcc iron. Theoretically predicted node angles are very close to those observed experimentally. The need for including anisotropy, in a precise fashion, in interaction problems is demonstrated.

## 1. Introduction

The problem of dislocation interactions in anisotropic media can in principle be solved by the Lothe-Brown-Indenbom-Orlov approach (Lothe 1967, Brown 1967, Indenbom and Orlov 1967, 1968). In this scheme dislocation arrays composed of straight line segments or curved configurations approximated by straight line segments are treated piecewise to give the elastic field at a point in the medium containing the arrays. The method is applicable to three dimensional arrays (Indenbom and Orlov 1967, 1968) but is particularly tractable in two dimensions (Lothe 1967, Brown 1967, Indenbom and Orlov 1967). In either case the resultant elastic field for a given segment can be expressed in terms of the stress field of an infinite straight dislocation. For the planar case of interest here, the stress field of a segment can be expressed in terms of the so called energy factors of the dislocation (Lothe 1967, Barnett and Asaro 1972).

The fundamental problem in anisotropic dislocation theory is determining the stress field of an infinite straight dislocation. The solutions are not explicit in the sense that the roots and eigenvectors of the general, sextic, secular equation associated with the problem are not known analytically. As a consequence, except for certain high symmetry directions of dislocation lines, dislocation calculations are necessarily performed numerically.

Two different approaches to the solution of the secular equation provide alternatives for the numerical calculations. One of these is the direct solution of the secular equation to give a set of parameters in terms of which the elastic stresses can be evaluated by known expressions (Eshelby et al 1953, Stroh 1962). The other is based on the evaluation of the stress field in terms of Green functions (Lothe 1967, Mura 1963, Willis 1970), with the resulting integrals to be computed using roots of the sextic equation. However, Barnett (1972) showed that the derivatives of the anisotropic elastic Green functions,

necessary for the treatment of planar dislocation problems, could be simply and accurately evaluated using Fourier transforms without the necessity of solving the sextic equation. The latter approach has been applied to dislocation computations (Barnett and Swanger 1971, Barnett *et al* 1972).

For a given problem one is interested in generating the most expedient algorithm for the numerical solution. The work based upon Barnett's method has shown that the necessary numerical calculations are, in general, accomplished quite rapidly and with a high degree of accuracy. Furthermore, the degeneracies associated with the technique, alluded to by others (Lothe 1972) and in particular by Petterson (1971) in his analysis of stacking fault nodes, do not exist in the Barnett technique.

The dislocation problems treated to date by the Barnett technique include the solution for the energy of straight dislocations (Barnett and Swanger 1971) and the evaluation of dislocation line tensions (Barnett *et al* 1972). The problem of a slit like crack has also been examined (Barnett and Asaro 1972). There are, in addition, a number of dislocation interaction problems that involve planar configurations of dislocations, including equilibrium faulted arrays, unextended nodes, and kink and jog configurations. In the following we present the computational formalism for applying Barnett's technique to this class of problem. As a particular example we consider the equilibrium form of three-fold dislocation nodes.

## 2. Method of solution

### 2.1. The coordinate system

Tensor notation is used throughout, with all indices ranging from 1 to 3 and with repeated indices denoting summation from 1 to 3 (unless otherwise stipulated). Furthermore, the coordinates $x_1$, $x_2$ and $x_3$, called crystal axes, are fixed along symmetry directions such that the elastic constants are displayed in their simplest form.

The Lothe-Brown-Indenbom-Orlov analyses require straight dislocation data as a function of angular orientation in a particular glide plane as well as the angular derivatives of this data in that plane. The Burger's vector $\boldsymbol{b}$ and sense vector $\boldsymbol{\xi}$ are chosen with the convention that $\boldsymbol{b}$ and $\boldsymbol{\xi}$ point in the same direction for a righthanded screw dislocation. Unit vectors $\boldsymbol{e}$ and $\boldsymbol{p}$, the latter normal to the glide plane, are defined by $\boldsymbol{e} = \boldsymbol{b}/|\boldsymbol{b}|$, and $\boldsymbol{p} = \boldsymbol{b} \times \boldsymbol{\xi}/|\boldsymbol{b} \times \boldsymbol{\xi}|$. A unit vector $\boldsymbol{A}$ is defined by

$$
\begin{gathered}
\boldsymbol{A} = \boldsymbol{p} \times \boldsymbol{e} \\
A_i = \epsilon_{ijk}p_j e_k
\end{gathered} \tag{1}
$$

where $\epsilon_{ijk}$ is the permutation tensor. The unit vector $\boldsymbol{\xi}$ is related to the orthogonal vector set by

$$
\xi_i = e_i \cos \theta + A_i \sin \theta \tag{2}
$$

where $\theta$ is the angle between $\boldsymbol{\xi}$ and $\boldsymbol{e}$ measured clockwise from $\boldsymbol{e}$ to $\boldsymbol{\xi}$ by an observer looking in the $\boldsymbol{p}$ direction.

Next, we consider another coordinate system rotated in such a way that $x_3^0||\boldsymbol{\xi}, x_2^0||\boldsymbol{p}$ and $x_1^0||\boldsymbol{h} = \boldsymbol{\xi}\boldsymbol{p}$. This transformed coordinate system is related to the crystal axis system by

$$
x_i^0 = a_{ij}x_j \tag{3}
$$

where
$$
a_{i j}=\left(\begin{array}{ccc}
h_{1} & h_{2} & h_{3} \\
p_{1} & p_{2} & p_{3} \\
\xi_{1} & \xi_{2} & \xi_{3}
\end{array}\right). \tag{4}
$$

These coordinates are summarized in figure 1.

![](./images/812342325521940482_1.jpg)

Figure 1. Summary of the coordinates used to describe dislocation positions.

### 2.2. Calculation of the in-plane stress field
The treatment of the in-plane stress field of a dislocation is parallel to that of Barnett and Asaro (1972) for the field of a dislocation lying in the plane of a slit like crack. The energy per unit length of a straight dislocation is given by the well known formula
$$
E=K_{i j} b_{i} b_{j} \ln \left(R / r_{0}\right) \tag{5}
$$
where $K_{i j}=K_{j i}$ and the $b_{i}$ are the components of the Burger's vector. Since this energy is just the reversible work on a hypothetical cut plane in creating the dislocation,
$$
E=\frac{1}{2} \oint_{s} \sigma_{i j} n_{j} b_{i} \mathrm{~d} s=\frac{1}{2} \int_{r_{0}}^{R} \sigma_{i 2}^{0} b_{i}^{0} \mathrm{~d} x_{1}^{0} \tag{6}
$$
where $\boldsymbol{n}$ is an outward pointing unit vector normal to the surface $s$. Here we have made use of the rotated coordinate system and have chosen the cut on the plane $x_{2}^{0}=0$. Thus we also have
$$
\sigma_{i 2}^{0}=a_{i m} \sigma_{m k} n_{k}. \tag{7}
$$

A comparison of equation (6) with equation (5) under the conditions that $b_{1}^{0}=b_{1}^{0}$, $b_{2}^{0}=b_{3}^{0}=0$ indicates that
$$
\int_{r_{0}}^{R} \frac{K_{11}^{0} b_{1}^{0} b_{1}^{0}}{x_{1}^{0}} \mathrm{~d} x_{1}^{0}=\frac{1}{2} \int_{r_{0}}^{R} \sigma_{12}^{0(1)} b_{1}^{0} \mathrm{~d} x_{1}^{0}. \tag{8}
$$

The superscript 1 in equation (8) means that we are considering only the field arising from the Burger's vector component in the $x_{1}^{0}$ direction. Equation (8) shows that
$$
\sigma_{12}^{0(1)}=\frac{2 K_{11}^{0} b_{1}^{0}}{x_{1}^{0}}. \tag{9}
$$

Similarly
$$
\sigma_{22}^{0(2)}=2 K_{22}^{0} b_{2}^{0} / x_{1}^{0} \quad \sigma_{32}^{0(3)}=2 K_{33}^{0} b_{3}^{0} / x_{1}^{0}. \tag{10}
$$

In the case where $b_{1}^{0}=b_{1}^{0}, b_{2}^{0}=b_{2}^{0}$ and $b_{3}^{0}=0$, there is an interaction term between the field caused by $b_{1}^{0}$ and that caused by $b_{2}^{0}$. Betti's reciprocal theorem states that for these two systems of stress

$$
\sigma_{22}^{0(1)} b_{2}^{0}=\sigma_{12}^{0(2)} b_{1}^{0}.
\tag{11}
$$

If we now compare the energy calculated by equations (5) and (6) we find that

$$
\sigma_{22}^{0(1)}=2 K_{21}^{0} b_{1}^{0} / x_{1}^{0} \quad \sigma_{12}^{0(2)}=2 K_{12}^{0} b_{2}^{0} / x_{1}^{0}.
\tag{12}
$$

In general

$$
\sigma_{i 2}^{0(s)}=2 K_{i s}^{0} b_{s} / x_{1}^{0} \quad \text { (no sum on } s \text { ). }
\tag{13}
$$

Finally, the in-plane traction vector. $\boldsymbol{T}$, is

$$
T_{i}^{0}=\sigma_{i 2}^{0(1)}+\sigma_{i 2}^{0(2)}+\sigma_{i 2}^{0(3)}=2 K_{i q}^{0} b_{q}^{0} / x_{1}^{0}.
\tag{14}
$$

In terms of the crystal axis coordinate system these tractions are given by

$$
\sigma_{i j} n_{j}=T_{i}=a_{i k}^{-1} \sigma_{k 2}^{0}
\tag{15}
$$

where $a_{i k}^{-1} a_{k j}=\delta_{i j}$ and $\delta_{i j}$ is the Kronecker delta. Using equations (14) and (15) and letting $x_{1}^{0}=d$ equal the distance from the dislocation in the glide plane we get, in terms of untransformed quantities

$$
T_{i}=\frac{2 a_{i k}^{-1} a_{k r} K_{r n} a_{n q} a_{q m} b_{m}}{d}=\frac{2 K_{i m} b_{m}}{d}.
\tag{16}
$$

Furthermore, the angular derivatives of the surface tractions are given by

$$
\frac{\mathrm{d} T_{i}}{\mathrm{~d} \theta}=\frac{2 K_{i m}^{\prime}(\theta) b_{m}}{d}=T_{i}^{\prime}(\theta)
\tag{17}
$$

since $\boldsymbol{b}$ is a fixed datum. Here $\theta$ is as defined earlier but can clearly be thought of as any angular variable in the plane referred to an arbitrary fixed direction. The above tractions are referred to as straight dislocation data. Expressions for the energy factors $K_{i j}(\theta)$ and the derivatives. $K_{i j}^{\prime}(\theta)$, are given in the appendix.

### 2.3. Theorems for in-plane stress fields

The results of the analyses of Lothe (1967), Brown (1967) and Indenbom and Orlov $(1967,1968)$ show that, if the stress field of an infinitely straight dislocation is $\sigma_{i j}=\Sigma_{i j}(\theta) / d$ as in $\S 2.2$. then the full field at a point Q arising from a planar loop is given by the line integral

$$
\sigma_{i j}=\frac{1}{2} \oint_{\mathrm{L}} \frac{\left\{\Sigma_{i j}(\theta)+\Sigma_{i j}^{\prime \prime}(\theta)\right\}}{|\boldsymbol{r}|^{2}} \sin (\theta-\gamma) \mathrm{d} l.
\tag{18}
$$

The angles $\theta$ and $\gamma$ and the vector $\boldsymbol{r}$ are shown in figure 2. In terms of equations (15) and (16), $n_{j} \Sigma_{i j}(\theta)=2 K_{i j}(\theta) b_{j}$ so that for the in-plane traction, $T_{i}^{*}(\theta)$

$$
T_{i}^{*}(\theta)=\sigma_{i j} n_{j}=\frac{1}{2} \oint_{\mathrm{L}} \frac{\left\{T_{i}(\theta)+T_{i}^{\prime \prime}(\theta)\right\}}{|\boldsymbol{r}|^{2}} \sin (\theta-\gamma) \mathrm{d} l.
\tag{19}
$$

Since it is often convenient and more precise to describe a loop in a piecewise straight fashion we require the field at a point $(r, \theta)$ produced by a segment such as AB (see figure

![](./images/812342325521940482_2.jpg)

Figure 2. Schematic representation of the coordinates used in the line integral in equation (19).

3). Partial integration of equation (19), with attention to the sense of line integral, yields

$$
T_{i}^{*}\left(d, \theta_{1}, \theta_{2}\right)=\frac{1}{d}\left\{-K_{i j}(\theta) b_{j} \cos (\theta-\alpha)+K_{i j}^{\prime}(\theta) b_{j} \sin (\theta-\alpha)\right\}_{\theta_{1}}^{\theta_{2}}. \quad(20)
$$

### 2.4. Resolved interaction force produced by a segment
From the Peach-Koehler equation, the components of the force on a dislocation with Burger's vector $\hat{b}$ and direction $\boldsymbol{\xi}$ are

$$
F_{k}=-\epsilon_{i j k} \sigma_{j l} \hat{b}_{l} \xi_{i}. \quad(21)
$$

We wish to extract the in-plane components of this force. In the direction of the vector $A$ this force is

$$
F_{A}=F_{k} A_{k}=-\epsilon_{i j k} \epsilon_{k m q} \xi_{i} \sigma_{j l} \hat{b}_{l} p_{m} e_{q} \quad(22)
$$

or since

$$
\begin{aligned}
\epsilon_{i j k} \epsilon_{k m q} & =\delta_{i m} \delta_{j q}-\delta_{i q} \delta_{j m} \\
F_{A} & =\sigma_{l j} p_{j} \hat{b}_{l} e_{i} \xi_{i}=T_{l}^{*} \hat{b}_{l} e_{i} \xi_{i}
\end{aligned} \quad(23)
$$

with $T^{*}$ given by equations (19) and (20). The force in the other in-plane direction $e$ is by similar reasoning

$$
F_{e}=T_{l}^{*} \hat{b}_{l} A_{i} \xi_{i}. \quad(24)
$$

Equations (23) and (24) complete the method of solution. We now consider various specific applications.

## 3. Applications
The method of reconstruction of complex ensembles of loops in a piecewise straight fashion using equation (20) suggests a simple graphical technique for obtaining the tractions and thus the in-plane forces acting on other dislocations. All that is required is a table of the energy factors $K_{i j}(\theta)$ and $K_{i j}^{\prime}(\theta)$ as a function of orientation in the given plane.

Precision in the data is required. In order to demonstrate this need for precision, as well as to provide specific application of the formulae, we now consider the problem of three fold nodes in $\alpha$-Fe in the $(\overline{1}10)$ glide plane.

### 3.1. Calculation of the data
The Burgers vector for the dislocation segments generating the traction data is taken as $\frac{1}{2}a[11]$. Furthermore, the tractions are conveniently normalized by $2|a|$, so that $n_{i}\Sigma_{ij}(\theta)=\sum_{j=1}^{3}K_{ij}(\theta)$ and $n_{j}\Sigma_{ij}'(\theta)=\sum_{j=1}^{3}K_{ij}'(\theta)$; $a$ is the lattice parameter. Figure 4

![](./images/812342325521940482_3.jpg)

Figure 3. Segment of a line integral as given by equation (20). Note that the arrow marks the sense of integration and thus defines $\theta_{1}$ and $\theta_{2}$.

shows the results for $T_{i}(\theta)$ calculated to a precision of $0\cdot1\%$ in 5 degree intervals: the original data being accurate to better than $0.01\%$. The elastic constants were taken from Hirth and Lothe (1968). Also shown, by the broken lines, are the isotropic results obtained by computing Voigt average elastic constants from the anisotropic moduli. These curves show that the quantitative errors in using isotropic theory for straight dislocations are appreciable, especially near the common screw and edge orientations. However, since the shapes of these curves do not differ drastically, isotropic calculations should be qualitatively correct and should contain errors probably no greater than $40\%$. This is only true in the case where we are dealing with configurations of infinitely straight dislocations. When the straight segments are finite as in loops, angular dislocations, etc, equation (20) includes contributions from the derivative terms. Figure 5 shows the results for $T_{i}'(\theta)$. The discrepancies between isotropic and anisotropic theory are now much larger. Near both the edge and screw orientations there are errors in absolute magnitude which are now as large as $500\%(\theta=160^{\circ})$. In addition, and even more importantly, there are also errors in sign. Thus conclusions drawn from isotropic calculations could be *qualitatively* in error. Furthermore, the shapes of the curves in figure 4, for example, suggest that curve fitting such as in harmonic analysis would be inappropriate for the generation of the derivative data unless the fitting were extremely accurate. The direct generation of the derivative data, $K_{ij}'(\theta)$, is inherently more accurate for a given degree of computation than the indirect approach of harmonic analysis followed by differentiation.

### 3.2. Threefold nodes in $\alpha$ iron
The most commonly observed node in $\alpha$ iron and the one present in hexagonal networks is displayed in figure 6. The reaction giving rise to the node has been given as

$$
\frac{1}{2}a[111]+\frac{1}{2}a[\overline{1}11]\to a[001].\tag{25}
$$

![](./images/812342325521940482_4.jpg)

Figure 4. Angular part of the normalized tractions $T_{i}$. caused by infinitely straight disloca- tions.

Carrington et al (1960) and Ohr and Beshers (1963) have examined these nodes experi- mentally and have found that the measured angle $2 \alpha$ is $91^{\circ}$. On the other hand, based on anisotropic line energy concepts, Chou (1965) calculated an angle of $85^{\circ}$ (correcting an earlier value of $81^{\circ}$ (Chou 1972)); the isotropic line tension method predicted an angle of $103^{\circ}$. Two possible reasons for these discrepancies are that, (i) line energy methods are inadequate and (ii) the methods of calculation were imprecise. Of course, concerning the isotropic calculation, the need to include anisotropy is evident.

The line energy method (line tension concept) considers two types of forces acting on the rays composing the node; a component tangent to the ray equal to the line energy and a component normal to the ray equal to the angular derivative of the energy (Hirth and Lothe 1968). Hence a line energy balance, at equilibrium, is equivalent to a mini- mization of the sum of the self energies of all the rays. However, in general, there will be a nonzero interaction energy which also depends on the configuration of the node. As already suggested (Lothe 1969), neglect of the interaction energy can lead to errors in predicting equilibrium node angles. Also (Lothe 1969), the line tension method fails to include net torque terms which can act on nodes and which can influence equilibrium. As discussed in the next section there are cases where the line energy method becomes exact, but this is only true if the rays are semi-infinite and when there exists sufficient symmetry.

Making use of equation (20) we include interactions by calculating the net moment exerted on each ray by the other rays or segments composing the node. At equilibrium these moments are individually zero.

### 3.3. Calculation of the moments: semi-infinite case

First we consider isolated threefold nodes comprised of semi-infinite rays. We define a quantity $g^{(i)}$ whose value is $+1(-1)$ if the sense of the $i$ th ray leads away from (into)

![](./images/812342325521940482_5.jpg)

Figure 5. Angular derivatives of the normalized tractions. Note the significant differences between anisotropic and isotropic (broken lines) calculations.

the node point. In this case, if $b_{j}^{(i)}$ is the $j$ th component of the Burger's vector of the $i$ th ray, and $\theta^{i}$ the angle that the $i$ th ray makes with the datum equation (20), or equation (19), yields for the moment $F^{(i)}$

$$
F^{(i)}=-b_{j}^{(i)} \sigma_{j p} n_{p}
$$

or

$$
\begin{aligned}
F^{(i)}=\frac{1}{\lambda} \sum_{\substack{k=1 \\
k \neq i}}^{n} g^{(k)}\left\{\operatorname{cosec}\left(\theta^{i}-\theta^{k}\right) K_{r s}\left(\theta^{k}\right) b_{r}^{(k)} b_{s}^{(i)}+\cot \left(\theta^{i}-\theta^{k}\right) K_{r s}\left(\theta^{i}\right) b_{r}^{(k)} b_{s}^{(i)}-K_{r s}^{\prime}\left(\theta^{i}\right) b_{r}^{(k)} b_{s}^{(i)}\right\}.
\end{aligned}
$$

In equation (26) $\lambda$ is the linear distance along the $i$ th ray measured from the node point (see figure 6). Furthermore, in keeping with the concept of conservation of Burger's vector, changing the sign of $g^{(k)}$ (ie reversing the sense of the line integral in equation (19)) necessitates changing the sign of $\boldsymbol{b}^{(k)}$.

With the insertion of the data shown in figures 4 and 5, equations (26) yielded the stable nodes shown in figure 7. The symmetric network node is included: however, the equilibrium angle is now calculated to be $86 \pm 0.5^{\circ}$. Furthermore one asymmetric node was also found, figure $7(d)$, its occurance probably being caused by the fact that there are eight extrema in the polar plot of energy for the [001] dislocation, figure 8. At or near these extrema, the torque terms vanish or are small, thus enabling equilibrium to ensure. An interesting consequence of having symmetric nodes such as the network node in figure $7(a)$ is that they can be treated exactly with the simpler line energy analysis. That is, the geometrical symmetry as well as the essential equivalence of the $\frac{1}{2} a[111]$ and $\frac{1}{2} a[\overline{1} \overline{1} 1]$ dislocations suggests that the following relations hold:

![](./images/812342325521940482_6.jpg)

Figure 6. Network node in $\alpha$ iron as shown by Ohr and Beshers (1963).

![](./images/812342325521940482_7.jpg)

Figure 7. This figure shows the four types of equilibrium nodes found in this system. Burger's vector designations indicate the importance of experimentally determining the character of each ray in a node.

![](./images/812342325521940482_8.jpg)

Figure 8. Polar plot of the energy of the glide dislocation, $b=\frac{1}{2}a[111]$ in $\alpha$ iron and one half the energy of the $b=a[001]$ dislocation. Note the presence of eight extrema in the energy of the latter. The units of energy are $10^{-5}$ erg cm $^{-1}$.

$$
K_{i j}(\alpha) b_{i}^{(3)} b_{j}^{(2)}=K_{i j}(-\alpha) b_{i}^{(3)} b_{j}^{(2)} \tag{27a}
$$

$$
K_{i j}^{\prime}(\alpha) b_{i}^{(3)} b_{j}^{(2)}=-K_{i j}^{\prime}(-\alpha) b_{i}^{(3)} b_{j}^{(2)} \tag{27b}
$$

$$
K_{i j}(-\alpha) b_{i}^{(3)} b_{j}^{(1)}=K_{i j}(\alpha) b_{i}^{(2)} b_{j}^{(1)} \tag{27c}
$$

$$
K_{i j}^{\prime}(-\alpha) b_{i}^{(3)} b_{j}^{(1)}=-K_{i j}^{\prime}(\alpha) b_{i}^{(2)} b_{j}^{(1)}. \tag{27d}
$$

Because $F_{2}=-F_{3}$ one can examine equilibrium using the condition $F_{3}-F_{2}=0$: it is easily shown that, by symmetry, $F_{1}=0$. Using relations (27a)-(27d), equation (26) and the conservation equation $b_{i}^{(1)}=b_{i}^{(2)}+b_{i}^{(3)}$ we find at equilibrium
$$
2\left\{E_{3}(-\alpha) \cot (\alpha)+E_{3}^{\prime}(-\alpha)\right\}-E_{1}(0) / \sin \alpha=0 \tag{28}
$$
which is equivalent to Chou's (1965) equation (6) based on self energy methods. This equivalence of the line segment method and the line tension method for symmetric nodes might be expected by an extrapolation to the node case of Lothe's theorem for a bend (Lothe 1967), which has been accomplished, in fact, by Lothe (1969).

The discrepancy between the present value of $2 \alpha=86 \pm 0.5^{\circ}$ and the value, $2 \alpha=85^{\circ}$ obtained by Chou (1972) arises from the use of different elastic constants. The use of Chou's elastic constants with the present method gives a value $2 \alpha=85 \pm 0.5^{\circ}$.

### 3.4. Finite segments
When the networks are composed of segments of finite length the results for the equilib- rium shape will differ from the isolated node case because of interactions. Consider, the node of figure 7(a) redrawn in figure 9. Since the length of segment (1) is usually smaller

![](./images/812342325521940482_9.jpg)

Figure 9. Coordinates used to describe and calculate the equilibrium network shape involving nodes of the type found in figure 7(a).

than that of either (2) or (3), we assume, again, that (2), (2)', (3) and (3)' are semi-infinite. Thus the moment on ray (2) will be altered by the stress fields of rays (2)', (3)' and the now finite ray (1). With the use of equation (21), the change in the moment resulting from the presence of rays (2)' and (3)' is calculated to be

$$
\begin{aligned}
\delta F=\frac{1}{R_{2}} & \left\{E^{(2)}(\alpha)-E^{(2)}(\kappa) \cos (-\alpha)-E^{(2) \prime}(\kappa) \sin (\theta-\alpha)\right\}+\frac{1}{R_{3}}\left\{K_{i j}(-\alpha) b_{i}^{(3)} b_{j}^{(2)}\right. \\
& \left.-K_{i j}(\kappa) b_{i}^{(3)} b_{j}^{(2)} \cos (\kappa+\alpha)+K_{i j}^{\prime}(\kappa) b_{i}^{(3)} b_{j}^{(2)} \sin (\kappa+\alpha)\right\}.
\end{aligned}
\tag{29}
$$

The increment of force tends to further open the node since at $\kappa=0$ it is negative, and the contribution from ray (1) is essentially unchanged from its semi-infinite value. Within a distance $\lambda$ along ray (2) equal to about the length of the finite ray (1) this change in force becomes slightly positive: the finiteness of (1) becoming important. Thus, considering finite segments should give even better correspondence with experiment. In fact if we compute the average force along ray (2) from the node $(\lambda=0)$ to $\lambda=d$ and let it act at $\lambda=d / 2$ we find that the equilibrium node angle is $91.6 \pm 0.5^{\circ}$, in even better agreement with the experimental network value of $2 \alpha=91^{\circ}$ than the isolated node case. Of course we should proceed even further and allow rays (2),(2)',(3) and (3)' to be finite, pinned perhaps at their centres. It is clear how this could be done, but for brevity we omit the details here. We do note that the next nearest segment in the actual network case would produce forces opposite in sign but weaker in strength than the segments considered and so on. Hence, one would expect the actual network value to lie between the isolated node value of $86 \pm 0.5^{\circ}$ and the figure 9 value of $91.6 \pm 0.5^{\circ}$, probably lying nearer the latter value. Hence, the agreement with the experimental network node value of $91^{\circ}$ is considered to be good.

### 4. Conclusion

A simple but accurate graphical technique for examining dislocation interactions in a plane has been presented. The analysis of the problems of dislocation nodes and networks in bcc iron has demonstrated that the inclusion of elastic anisotropy in a precise fashion produced results in good agreement with experimental observations.

Applications of the analysis given here should aid in the understanding of other types of interaction phenomena, some of which were mentioned in the text.

## Acknowledgments
The authors are happy to acknowledge the support of this research by the National Science Foundation under grant number GH36125.

## Appendix
Barnett *et al* (1972) have given for the energy, and its angular derivative, the formulae
$$
E(\theta)=\left(G_{s n i r} \cos \theta+H_{s n i r} \sin \theta\right) \int_{0}^{\pi} Z_{s} \frac{\mathrm{d} Z n}{\mathrm{~d} \psi} M_{i r}^{-1} \mathrm{~d} \psi \tag{A.1}
$$
and
$$
\begin{aligned}
\left(\frac{\mathrm{d} E}{\mathrm{~d} \theta}\right)= & \left(-G_{s n i r} \sin \theta+H_{s n i r} \cos \theta\right) \int_{0}^{\pi} Z_{s} \frac{\mathrm{d} Z n}{\mathrm{~d} \psi} M_{i r}^{-1} \mathrm{~d} \psi+\left(G_{s n i r} \cos \theta+H_{s n i r} \sin \theta\right) \\
& \times \int_{0}^{\pi}\left\{\left(\xi_{s} \frac{\mathrm{d} Z n}{\mathrm{~d} \psi} \sin \psi+Z_{s} \xi_{n} \cos \psi\right) M_{i r}^{-1}-Z_{s} \frac{\mathrm{d} Z n}{\mathrm{~d} \psi} F_{i r} \sin \psi\right\} \mathrm{d} \psi.
\end{aligned} \tag{A.2}
$$

In the above,
$$
G_{s n i r}\left(H_{s n i r}\right)=\frac{B_{m} B_{q}}{4 \pi^{2}} \epsilon_{p j w} C_{n g i p} C_{w m r s} e_{j}\left(A_{j}\right) \tag{A.3}
$$

$$
F_{i r}=M_{i x}^{-1} M_{\beta r}^{-1} C_{x \lambda \beta \mu}\left(Z_{\lambda} \xi_{\mu}+Z_{\mu} \xi_{\lambda}\right) \tag{A.4}
$$
and the Christoffel stiffness matrix $M_{ir}$ is given by
$$
M_{i r}=C_{i j r s} Z_{j} Z_{s}. \tag{A.5}
$$

$B_{m}$ is the $m$th component of the Burger's vector and the quantities $\theta$, $e$ and $A$ are those defined in §2.1 of the text. The elastic constants are $C_{i j h l}$ referred to crystal axis coordinates. Finally the unit vector $\boldsymbol{z}(\psi)$ is defined by $\boldsymbol{Z} \cdot \boldsymbol{\xi}=0$ and thus can be written as
$$
Z_{i}(\psi)=p_{j} \cos \psi-\frac{\mathrm{d} \xi_{j}}{\mathrm{~d} \theta} \sin \psi. \tag{A.6}
$$

Hence using equations (A.5) we can extract $K_{m g}$ and $K_{m g}^{\prime}$ by replacing $G_{s n i r}$ and $H_{s n i r}$ in equations (A.1) and (A.2) by quantities defined as follows,
$$
G_{s n i r m g}\left(H_{s n i r m g}\right)=\frac{1}{4 \pi^{2}} \epsilon_{p j w} C_{n g i p} C_{w m r s} e_{j}\left(A_{j}\right). \tag{A.7}
$$

For given crystal symmetry the quantities appearing in equations (A.1) and (A.2) can be simplified as shown by Barnett *et al* (1972).

### References

Barnett D M 1972 *Phys. Stat. Solidi* (b) **49** 741

Barnett D M and Asaro R J 1972 *J. Mech. Phys. Solids* **20** 353

Barnett D M, Asaro R J, Gavazza S D, Bacon D J and Scattergood R O 1972 *J. Phys. F: Metal Phys.* 2 854

Barnett D M and Swanger L A 1971 *Phys. Stat. Solidi* (b) **48** 419

Brown L M 1967 *Phil. Mag.* **15** 363

Carrington W, Hale K F and McLean D 1960 *Proc. R. Soc.* A**259** 203

Chou Y T 1965 *J. appl. Phys.* **36** 1435
—— 1972 *J. Mater. Sci. Engr.* **10** 81

Eshelby J D, Read W T and Shockley W 1953 *Acta Metall.* **1** 251

Hirth J P and Lothe J 1968 *Theory of Dislocations* (New York: McGraw Hill)

Indenbom V L and Dubnova G N 1967 *Sov. Phys.-Solid St.* **9** 915

Indenbom V L and Orlov S S 1967 *Sov. Phys.-JETP Lett.* **6** 274
—— 1968 *Sov. Phys.-Crystallogr.* **12** 849

Lothe J 1967 *Phil. Mag.* **15** 353
—— 1969 *Fundamental Aspects of Dislocation Theory*, NBS Spec. Publ. No 317 p 11
—— 1969 *PhD Thesis* University of Oslo
—— 1972 *Computational Solid State Physics* ed F Herman, N W Dalton and T Koehler (New York: Plenum)
p 425

Malen K and Lothe J 1970 *Phys. Stat. Solidi* (b) **39** 289

Mura T 1963 *Phil. Mag.* 3 625

Ohr S M and Beshers D N 1963 *Phil. Mag.* **8** 1343

Petterson B 1971 *Rep. AE-434 Aktiebolaget Atomenergi, Studsvik, Nykoping, Sweden*

Stroh A N 1958 *Phil. Mag.* 4 625
—— 1962 *J. Math. Phys.* **41** 77

Willis J R 1970 *Phil. Mag.* **21** 931