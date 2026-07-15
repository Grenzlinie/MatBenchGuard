# First-principles calculation of microstructural processes in alloys

Tetsuo Mohri

Research Center for Integrative Mathematics and Division of Materials Science and Engineering, Graduate School of Engineering, Hokkaido University, Sapporo 060-8628, Japan

---

## A R T I C L E  I N F O

**Article history:**
Received 15 October 2009
Received in revised form 30 January 2010
Accepted 1 February 2010
Available online 19 February 2010

**Keywords:**
Phase Field Method
Cluster Variation Method
First-principles calculation
Continuous Displacement Cluster Variation Methods
Fe-Pd system
$L1_0$ ordered phase
Coarse graining

---

## A B S T R A C T

By combining Cluster Variation Method with FLAPW electronic structure total energy calculations and Phase Field Method, time evolution of Anti Phase Boundary associated with $L1_0$ ordering process in Fe-Pd was calculated from the first-principles. The theoretical framework of these calculations is reviewed, and it is pointed out that the introduction of the local lattice relaxation effects is indispensable to achieve higher accuracy. Preliminary calculations based on Continuous Displacement Cluster Variation Method are attempted on two-dimensional square lattice to examine the significance of the local lattice relaxation effects.

© 2010 Published by Elsevier B.V.

---

## 1. Introduction

Cluster Variation Method (hereafter CVM) [1] has been recognized as one of the most reliable theoretical tools to calculate configurational entropy and free energy of an alloy system. The level of the CVM approximation is specified by a largest cluster explicitly considered in the free energy formula, termed *basic cluster*, and it has been amply demonstrated [2,3] that the calculated transition temperatures approaches a correct value obtained by other methods such as Monte Carlo simulation or high temperature expansion by increasing the size of the basic cluster. Although the employment of a bigger basic cluster demands heavy computational burden, recent development of high performance computer resolves such a difficulty.

The power of the CVM is not limited to the accuracy of the calculated results, but also the expandability and connectivity with other theoretical means to perform first-principles calculation of phase equilibria and phase transition dynamics are unique advantageous feature. In fact, the author have been attempting the first-principles calculations of phase diagrams [4-9] by combining CVM with the electronic structure total energy calculations such as FLAPW method and reproduced the experimental phase diagram with high accuracy. The key to such an expandability of the CVM is ascribed to the *correlation functions* [2,3,10] which describe the atomic configurations of an alloy, and correlation functions are common variables shared by various theoretical methods in other realm of alloy theories including energetics and dynamics as will be discussed in this article.

Recently, Phase Field Method (hereafter PFM) [11] has been attracting broad attention as a powerful theoretical tool to predict and analyze microstructure evolution process of alloys. The key to the PFM is to define appropriate *order parameters* of which spatial distribution represents microstructure of interests, and the evolution process is described by Time Dependent Ginzburg Landau equation [12] and/or Cahn Hilliard equation [13]. The applicability of the PFM is surprisingly versatile, which can be ascribed to the phenomenological nature of the PFM in which the free energy is efficiently parametrized. It is, however, noted that the microstructure in the PFM is defined in a continuum medium, indicating that the order parameter is a continuous quantity of which atomistic origin is obscured. Hence, the length scale is not uniquely assigned based on the discrete nature of a lattice. This is regarded as a drawback of PFM to extend it to more quantitative and atomistic calculations.

The author's group attempted [14-20] to combine PFM with the CVM by assigning correlation functions appearing in the CVM as order parameters in the PFM. Since the correlation functions are defined on a discrete lattice, it is necessary to perform the coarse graining operation in order to incorporate correlation functions in a coherent manner in the PFM which is defined in the continuum medium. Ohno [18] developed a unique procedure of the coarse graining operation by extending the traditional work by Kikuchi and Cahn [21], and performed multi-scale calculation for the growth process of Anti Phase Boundary (hereafter APB) associated with ordering reactions. Later, Mohri et al. further

---

E-mail address: tmohri@eng.hokudai.ac.jp

0927-0256/$ - see front matter © 2010 Published by Elsevier B.V.
doi:10.1016/j.commatsci.2010.02.001

included the electronic structure total energy calculations and performed the first-principles microstructure evolution calculations for $Fe-Pd$ [20] and $Fe-Pt$ systems. The first half of the present paper is attributed to the introduction of the theoretical framework of these calculations.

However, there still remain room for improvement for these first-principles calculations in view of the recent development of the CVM. In particular, the lattice dealt with by the conventional CVM is allowed to deform only in a uniform manner and local lattice distortion is by no means introduced. This is deemed a serious drawback to achieve high accuracy in calculated results, since the system may still stay in the excited state without considering the local lattice relaxation. However, a fully satisfactory calculation of even static phase equilibria incorporating the local lattice relaxation effects is still pre-matured, and the implementation of such a scheme into PFM is far away. In the later half of the present report, preliminary calculations [22] for phase equilibria with local lattice relaxation effects are introduced and the significance of the effects are pointed out.

Furthermore, a brief discussion on the interface structure by the CVM is offered at the end, since the evolution kinetics of an APB is affected by the detailed atomistic structure and atomistic calculations of the interface should be more seriously explored. In fact, in the multi-scale calculation, interface falls in the medium scale range and it is a difficult task to reflect the atomistic structure of the interface efficiently into the microstructural formation and evolution processes.

The organization of the present report is as follows. In the next section, theoretical frameworks to perform the first-principles microstructure evolution calculation in the previous studies are reviewed and main results are reproduced. Two problems to be settled in the future calculations are pointed out in the third section and preliminary results are demonstrated. Finally the brief summary follows in the last section. Throughout this report, a particular focus is placed on the discussion of how the CVM free energy has been modified towards the first-principles microstructure calculations and how the CVM free energy should be further revised for accurate calculations.

### 2. First-principles calculation of time evolution of Anti Phase Boundary

The common parameters which connect three theoretical tools from FLAPW (electronic structure) to PFM (microstructure) through CVM (atomistic configuration) are the correlation functions as described below. In the electronic structure calculations, the main outcome is the total energy $E^{(m)}$ of a phase specified by $m$, and the heats of formation $\Delta E^{(m)}$ is derived with respect to an appropriate energy reference state. The heats of formation of a selected set of ordered phases including pure constituents are further expanded in the following manner,

$$
\Delta E^{(m)}=\sum_{i} v_{i} \cdot \xi_{i}^{(m)}
\tag{1}
$$

where $i$ indicates a cluster, $\xi_{i}^{(m)}$ the correlation function which describes the atomic configuration on the cluster $i$ involved in the phase $m$, and $v_{i}$ is an effective interaction energy. The expansion given in Eq. (1) has been termed Cluster Expansion Method (hereafter CEM) [23] and the mathematical basis of the CEM is guaranteed by the formation of the orthonormal basis by the set of correlation functions. Since the total energy electronic structure calculations are carried out for various phases including hypothetical phases, the left hand side of Eq. (1) forms a vector. Accordingly the correlation functions are described by the matrix, and effective cluster interaction energies which are elements of a vector are determined by the matrix inversion.

It is noted that in the actual operation of the CEM in alloy systems, the heats of formation is obtained as a function of lattice constant or atomic separation. In this case, the resultant effective cluster interaction energies are also derived as a function of lattice constant. Moreover, the temperature dependence can be incorporated in the effective cluster interaction energies when the vibrational free energy is calculated for each ordered phase. These schemes have been amply demonstrated in author's previous publications [4].

According to the CVM, the entropy formula is formally written as

$$
S=k_{B} \sum_{k}^{K} \alpha_{k} \sum_{J} L\left(X_{k}(J)\right),
\tag{2}
$$

where $k_{B}$ is the Boltzmann constant, $\alpha_{k}$ is a coefficient for a cluster $k$, $L(x)$ is defined as $L(x)=x \cdot \ln x-x$, $X_{k}(J)$ is the cluster probability of finding an atomic arrangement specified by $J$ in the cluster $k$. It is noted that CVM provides the systematic means to determine the coefficient terms $\{\alpha_{k}\}$.

The largest cluster, $K$, considered in the entropy formula is termed *basic cluster* as was introduced in the previous section.

It has been amply demonstrated that the cluster probabilities and correlation functions are mutually related through a linear transformation,

$$
X_{k}(J)=\frac{1}{2^{k}}\left\{1+\sum_{l} V_{k, l}(J) \cdot \xi_{l}\right\},
\tag{3}
$$

where $V_{k,l}(J)$ is termed V-matrix [2,3] which conveys the information of atomic configuration $J$ in the cluster $l$ contained in the cluster $k$. Hence, by substituting Eq. (3) into Eq. (2), the entropy is formally rewritten as $S=S(\{\xi_{i}\})$ in terms of correlation functions.

Together with Eq. (1), the configurational free energy of the system,

$$
f=\Delta E(\{\xi_{i}\})-T \cdot S(\{\xi_{i}\})
\tag{4}
$$

is also written in terms of correlation functions, $f(\{\xi_{i}\})$. As pointed out above, the effective cluster interaction energies are often obtained as a function of an atomic distance, $r$. Hence, the free energy is more generally written as $f(r,\{\xi_{i}\})$, and at each temperature, $T$, the equilibrium state is determined by minimizing the free energy with respect to both correlation functions and lattice constant,

$$
\left.\frac{\partial f}{\partial\{\xi_{i}\}}\right|_{T,i\neq j}=0 \quad \text{and} \quad \left.\frac{\partial f}{\partial r}\right|_{T,\{\xi_{i}^{e}\}}=0
\tag{5}
$$

These are the essential ingredients to obtain the most stable state of a given phase, and by employing the same procedure for various phases, one may determine the phase equilibria from the first-principles. The accuracy of the first-principles calculations for phase equilibria is mainly examined by the reproducibility of experimental transition temperatures. Although the model above is rather simple, the outcome is surprisingly good when compared with experimental results for certain $Fe$-based alloy systems such as $Fe-Pd$ and $Fe-Pt$ [6,8,9]. In fact, the discrepancies of $L1_{0}$-disorder transition temperatures in these systems are merely in the range of $\sim 20$ K. It is, however, noted that for most alloy systems the transition temperatures are considerably overestimated, which is mainly attributed to the neglect of *local lattice distortion effects*. This is further discussed in the latter part of this report.

For the description of the microstructure, Ginzburg-Landau type free energy is a starting equation which is written as

$$
F_{\text{chem}}=\int\left[f[\{\eta_{i}\}]+\sum_{i} \kappa_{i}(\nabla \eta_{i})^{2}\right] \cdot dV
\tag{6}
$$

where $f[\{\eta_{i}\}]$ is the bulk chemical free energy density of the homogeneous system, $\eta_{i}$ is an order parameter to characterize a

microstructure, and the second term in the kernel indicates the gradient energy with $\kappa_i$ the gradient energy coefficient. When CVM is incorporated into PFM, the bulk free energy density term in Eq. (6) is replaced by $f(\{\xi_i\})$ by regarding the correlation functions as order parameters. It should be noted that a correlation function in the PFM depends on position and time, $\xi_i(\mathbf{r}, t)$, which is in marked difference with the original correlation function in Eqs. (3)-(5) which is defined in a homogeneous medium.

Within the tetrahedron approximation [24] of the CVM, the number of the correlation functions to describe $L1_0$ ordered phase, which is the main concern of the present report, in the phase equilibria calculation is eight. However, for the description of $\langle 100\rangle$ type Anti Phase Boundary, three different variants should be distinguished. Otherwise, triple point junction of the APB which is one of the most characteristic features of the $L1_0$ ordering is by no means reproduced. Hence, the total number of the correlation functions in the PFM increases up to fifteen [14-20].

As pointed out in the introduction, correlation functions are defined in the discrete lattice while the Ginzburg Landau type free energy expression in Eq. (6) is basically defined in the continuous medium. Hence, in order to achieve the coherency of the length scale, it is indispensable to introduce coarse graining operation. Ohno [18] generalized the coarse graining scheme proposed by Kikuchi and Cahn [21] in the following manner.

First, a crystalline lattice is divided into cells in which numerous atomic planes are contained, and two kinds of coordinate systems are introduced; one is a global coordinate system to describe the location $\mathbf{R}_l$ of a cell, and the other is a local coordinate system to specify the position $\mathbf{r}_m$ of an atomic plane within the cell. Then, the spatial dependence of the correlation functions pointed out above is rewritten as $\xi_i(\mathbf{P}_n)$ where $\mathbf{P}_n$ indicates the $n$-th atomic plane in the lattice and is further written as $\mathbf{P}_n = \mathbf{R}_l + \mathbf{r}_m$, suggesting that the $n$-th atomic plane in the lattice is rephrased as $m$-th atomic plane in the $l$-th cell. It is noted that for a multibody correlation function, the cluster expands over several atomic planes and an additional term to average the positions of these atomic planes is necessary to uniquely specify the location of the correlation function, hence more general expression is given by $\mathbf{P}_n = \mathbf{R}_l + \mathbf{r}_m + \mathbf{h}(a)$ where $\mathbf{h}(a)$ is a vector function of a lattice constant $a$. But, since the rigorous description rather complicates the mathematical notation and hampers to grasp the essential points, we avoid to introduce the dependencies on $\mathbf{h}(a)$.The correlation function $\xi_i(\mathbf{P}_n) = \xi_i(\mathbf{R}_l + \mathbf{r}_m)$ is expanded around the global coordinate system and higher order terms above third order derivatives are truncated to yield

$$
\xi_i(\mathbf{R}_l + \mathbf{r}_m) = \xi_i(\mathbf{R}_l) + \mathbf{r}_m \cdot \nabla \xi_i(\mathbf{R}_l) + \frac{1}{2}|\mathbf{r}_m|^2 \cdot \nabla^2 \xi_i(\mathbf{R}_l) \tag{7}
$$

Accordingly, the free energy $f$ is dependent on the atomic position and the dependence is mathematically given as $f = f(\{\xi_i(\mathbf{R}_l)\}, \{\nabla \xi_i(\mathbf{R}_l)\}, \{\nabla^2 \xi_i(\mathbf{R}_l)\}, \mathbf{r}_m)$. Then, the free energy of the system $F$ which corresponds to $F_{Chem}$ in Eq.(6) is given as the sum of $f$ from each atomic plane and is written as

$$
F = \sum_{l} \sum_{m} f(\{\xi_i(\mathbf{R}_l)\}, \{\nabla \xi_i(\mathbf{R}_l)\}, \{\nabla^2 \xi_i(\mathbf{R}_l)\}, \mathbf{r}_m) \tag{8}
$$

It is noted that the first and second order derivatives in $f$ represents the inhomogeneity of a system. The free energy above is further expanded around a homogeneous state $f^0 = f(\{\xi_i\}, 0, 0)$ and the resultant expression is given as

$$
\begin{aligned}
F & \cong \sum_{l,m} \bigg\{ f^0[\{\xi_j\}] + \sum_{j} \left. \frac{\partial f}{\partial (\nabla \xi_j)} \right|_0 (\nabla \xi_j) + \sum_{j} \left. \frac{\partial f}{\partial (\nabla^2 \xi_j)} \right|_0 (\nabla^2 \xi_j) \\
& \quad + \frac{1}{2} \sum_{j,j'} \left. \frac{\partial^2 f}{\partial (\nabla \xi_j) \partial (\nabla \xi_{j'})} \right|_0 (\nabla \xi_j)(\nabla \xi_{j'}) \bigg\},
\end{aligned} \tag{9}
$$

where 0 stands for a homogeneous state. By converting the sum into integral followed by the application of Gauss's divergence theorem, one can yield the final form of the free energy functional for an inhomogeneous system,

$$
F = \frac{1}{L} \int \left[ f_{\text{CVM}}^0[\{\xi_j\}] + \sum_{j,j'} \kappa_{jj'} (\nabla \xi_j)(\nabla \xi_{j'}) \right] \cdot dx \tag{10}
$$

where $\kappa_{jj'}$ is a generalized gradient coefficient which is no more constant and depends on temperature, local atomic configuration and lattice constant.

Then, the time evolution of the system is traced by substituting Eq. (10) into the Time Dependent Ginzburg Landau equation given by

$$
\frac{\partial \xi_i}{\partial t} = - \sum_{j} L_{ij} \frac{\delta F_{\text{chem}}}{\delta \xi_j} \tag{11}
$$

where $L_{ij}$ is a relaxation constant. In accordance with the modification of the free energy functional derived in Eq. (10), TDGL equation is also modified, but the derivation of the modified TDGL equation is not a main task of the present report and the reader interested in the derivation should consult the original article [18].

The formalism above is applied to the study of time evolution process of APB associated with $L1_0$ ordering reaction of $Fe-Pd$ system at 820 K, and some of the snapshots of time evolution process are reproduced in Fig. 1 [20]. Note that the gray levels indicate the magnitude of square of the Long Range Order parameter which are calculated based on the point correlation functions in three $\langle 100\rangle$ directions.

### 3. Prospects for future first-principles calculations and local lattice relaxation effects

In order to further improve and generalize the free energy formula for first-principles calculations of phase equilibria and microstructural evolution process, two important modifications and applications are suggested in the present section. The first one is the incorporation of the local lattice relaxation effects. As pointed out in the earlier section, without local lattice relaxation effects, the system is still not fully in the equilibrium state and the introduction of the local lattice relaxation effects is indispensable in order to achieve higher accuracy.

In the present section, the significance of the local relaxation effects is examined by focusing on the order-disorder transition in the two-dimensional square lattice. Within the square approximation of the CVM, the free energy is given by [22].

$$
\begin{aligned}
f & = \omega \sum_{i,j} e_{ij} \cdot y_{ij}^{(\alpha \beta)} - k_B T \\
& \quad \cdot \left[ 2 \sum_{i,j} L(y_{ij}^{(\alpha \beta)}) - \frac{1}{2} \cdot \left( \sum_{i} L(x_i^{(\alpha)}) + \sum_{j} L(x_j^{(\beta)}) \right) - \sum_{i,j,k,l} L(w_{ijkl}) \right]
\end{aligned} \tag{12}
$$

where $\omega$ is one half the coordination number (four for the square lattice), $e_{ij}$ and $y_{ij}^{(\alpha \beta)}$ are the nearest neighbor pair interaction energy and pair probability for $i$-$j$ pair. $\alpha(\beta)$ is the sub-lattice at which $A(B)$ atom is preferentially located, and it is easily understood that for the ordered phase shown in Fig. 2 at 1:1 stoichiometric composition, $\alpha$ and $\beta$ sub-lattices are alternatively located and, therefore, only one type of pair probability function $y_{ij}^{(\alpha \beta)}$ is considered in the free energy. $x_i^{(\alpha)}$ ($x_j^{(\beta)}$) is the point probability to find an atomic species $i$ ($j$) on the sub-lattice $\alpha(\beta)$ and $w_{ijkl}$ is the square cluster probability for the atomic arrangement specified by the subscripts. The free energy is minimized with respect to the square cluster probabilities under the constraint given by $\sum w_{ijkl}=1$. The calculated temperature dependence of Long Range Order parameter

![](./images/811803417642008577_1.jpg)

Fig. 1. Snapshots of time evolution process of APB associated with L10 ordering in Fe-Pd system at 50 at.% at 820 K. The bar indicates 100 nm and the arrows suggest [1 0 0] and [0 1 0] directions [20].

![](./images/811803417642008577_2.jpg)

Fig. 2. Ordered phase in the two-dimensional square lattice considered in the present study.

![](./images/811803417642008577_3.jpg)

Fig. 3. Temperature dependence of the Long Range Order parameter at 1:1 stoichiometric composition. The unity of the Long Range Order parameter corresponds to the fully ordered phase in Fig. 2. The temperature is normalized with respect to nearest neighbor pair interaction energy between A atoms.

(hereafter LRO) at a fixed composition of 50 at.% is shown in Fig. 3.
Note that the temperature axis is normalized with respect to pair
interaction energy between species $A$, $e_{AA}$. One can confirm the typ-
ical 2nd order transition behavior, and the temperature 2.43 is iden-
tified as the transition temperature at which LRO falls null.

In the calculations above, the atoms are located exactly on the
square lattice points and no displacements are allowed. In this
sense, the present square lattice is a rigid lattice. While if the pair
interaction energy depends on the lattice constant (atomic separa-
tion) $r$, the lattice is uniformly deformable and the minimization of
the free energy is carried out with respect to $r$ in addition to square
cluster probabilities $w_{ijkl}$, as was mentioned in Eq. (5) for the first-
principles calculation.

The local relaxation effects are equivalent to the introduction of
additional freedom of atomic displacements around each lattice
point. Hence, the deformation of the lattice is non-uniform which de-
stroys the symmetry of the square lattice and the conventional CVM
free energy formula given in Eq. (12) is no more justified. The mod-
ification of the free energy for the local relaxation effects was per-
formed by Kikuchi within the CVM as the extension of the liquid
free energy formula and the new formalism has been termed Contin-
uous Displacement Cluster Variation Method (CDCVM) [22,25–27].

In the CDCVM, additional lattice points which are termed qua-
si-lattice points are introduced around each Bravais lattice point
and an atom is allowed to displace to one of these additional lattice
points. The key to CDCVM is that atoms displaced to different qua-
si-lattice points are regarded as different atomic species which are
located at the Bravais lattice points, and the additional entropy
arising from the atomic displacements is converted to the configu-
rational entropy of multi component alloys. When the number of
quasi-lattice points is given by $n$, for instance, the system is re-
garded as $n+1$ component system even if the original system is
a pure metal. The internal energy is, on the other hand, evaluated
by explicitly considering the separation between quasi-lattice
points. In this way, the difficulty of the broken symmetry is tacitly
circumvented within the conventional free energy formula.

The CDCVM free energy for a square lattice within the pair
approximation is given as
$$
\begin{aligned}
f= & \omega \cdot \sum_{i} \sum_{j} \int d \mathbf{r}_{i} \cdot \int d \mathbf{r}_{j}^{\prime} \cdot \varphi_{i j}\left(\mathbf{r}_{i}, \mathbf{r}_{j}^{\prime}\right) \cdot g\left(\mathbf{r}_{i}, \mathbf{r}_{j}^{\prime}\right)-k_{B} T \\
& \cdot\left[\frac{2 \omega-1}{2}\left(\sum_{i} \int d \mathbf{r}_{i} \cdot L\left(f_{i}^{\alpha}\left(\mathbf{r}_{i}\right)\right)+\sum_{j} \int d \mathbf{r}_{j}^{\prime} \cdot L\left(f_{j}^{\beta}\left(\mathbf{r}_{j}^{\prime}\right)\right)\right)\right. \\
& \left.-\omega \sum_{i} \sum_{j} \int d \mathbf{r}_{i} \int d \mathbf{r}_{j}^{\prime} \cdot L\left(g\left(\mathbf{r}_{i}, \mathbf{r}_{j}^{\prime}\right)\right)+(\omega-1)\right]
\end{aligned}
$$
(13)
where $f_{i}^{\alpha}(\mathbf{r}_{i})$ and $f_{j}^{\beta}(\mathbf{r}_{j}^{\prime})$ are the (point) distribution functions to de-
scribe the probability of finding atomic species $i$ and $j$ at $\mathbf{r}_{i}$ and $\mathbf{r}_{j}^{\prime}$,
respectively, and pair distribution function $g_{ij}^{\alpha \beta}(\mathbf{r}_{i}, \mathbf{r}_{j}^{\prime})$ is similarly de-
fined. It is noted that these distribution functions are the general-
ization of point and pair probabilities $x_{i}^{\alpha}(x_{j}^{\beta})$ and $y_{ij}^{\alpha \beta}$ in the
conventional CVM free energy formula in the continuous space.
$\varphi_{ij}(\mathbf{r}_{i}, \mathbf{r}_{j}^{\prime})$ is the atomic pair potential and, in the present investiga-
tion, Lennard-Jones pair potential is assigned. It should be pointed
out that in the actual minimization process, one needs to consider
the generalized geometrical relationship which further imposes
symmetry constraint written as
$$
f_{i}^{\alpha}\left(\mathbf{r}_{i}\right)=\sum_{j} \int d \mathbf{r}_{j}^{\prime} \cdot g\left(\mathbf{r}_{i}, \mathbf{r}_{j}^{\prime}\right))=\sum_{j} \int d \mathbf{r}^{\prime} \cdot g\left(\mathbf{R}^{-1} \mathbf{r}_{i}, \mathbf{r}_{j}^{\prime}\right).
$$
(14)
where $\mathbf{R}$ is the symmetry operator for a parent square lattice.

The comparison of the resultant phase diagrams between CVM
and CDCVM is shown in Fig. 4 [22]. One can see that the transition

![](./images/811803417642008577_4.jpg)

Fig. 4. Comparison of the calculated phase boundaries between conventional CVM (open circles) and CDCVM (solid circles). Pair interaction energies are assigned by Lennard-Jones type potential [22].

![](./images/811803417642008577_5.jpg)

Fig. 5. Temperature dependence of point distribution function for A atom on $\alpha$ sublattice at 50 at.% at temperature $T=0.25$. Unit scale in $x$ and $y$ directions corresponds to 7.5% of the lattice constant.

temperature is significantly reduced in the CDCVM. This is because the system is able to find lower energy state by the additional freedom endowed by the local lattice relaxation effects, and the effects are much more dictated in the disordered phase for which the chances of encountering atoms with different sizes are enhanced. Shown in Fig. 5 is $f_{i}^{\alpha}(\mathbf{r}_{i})$ at temperature 0.25 at which ordered phase is stabilized (see Fig. 4). One can see that the atoms are distributed widely around the Bravais lattice point even in the ordered phase, while in the conventional CVM the distribution function is a delta-function sharply peaked at the center.

The introduction of the local relaxation effects in the PFM is necessary particularly for a system in which the sizes of constituent atoms differ significantly. The coherency and consistency of the CDCVM free energy in the homogeneous free energy density term in PFM has not been seriously investigated. The first step is to extend the correlation function in the continuous space, and sub-local coordinate system may be introduced within the local coordinate system for the coarse graining operation covering the quasi-lattice points. The details should be awaited for further investigation.

The second point to be explored is the atomistic description of the interface structure. In fact, an interface plays a key role in the evolution of the microstructure through its mobility, and we focus on APB in the present study. In contrast to other first-principles approaches to structure and properties of interfaces [28-32], our treatment is based on CVM free energy and one is capable of carrying out a consistent study of stability of the interface based on the calculated phase diagram, although the size of the basic cluster adopted in the CVM formalism limits the applicability to low symmetric ordered phases. In the following, a preliminary study on two-dimensional square lattice prior to performing a first-principle study on more realistic three dimensional systems including $L1_{0}$ ordered phase is demonstrated.

![](./images/811803417642008577_6.jpg)

Fig. 6. APB studied in the present investigation (upper figure) and sequence of square lattices in $\langle 10\rangle$ direction and sub-lattices.

![](./images/811803417642008577_7.jpg)

Fig. 7. The variation of the LRO along 60 at.% planes in $\langle 10\rangle$ direction. Three curves correspond to three different temperatures indicated in the right hand side of the figure. The temperatures correspond to the ones in Fig. 3.

In the classical theory, the interface including APB is regarded as sharp without any structure, while within the PFM the APB has a certain width which is determined by two competing mechanisms. One is the reduction of the total free energy by decreasing the disordered area between two ordered domains which is nothing but an APB. The other one is the reduction of the gradient energy which is given by $\kappa \cdot (\nabla \xi)^{2}$ in the Ginzburg Landau type free energy in Eq. (6) by increasing the width (therefore, decreasing the gradient) of the APB. Within the present free energy model described in the previous section for the PFM, the width of the APB is discussed only within the size of the basic cluster which may be too small. One way to circumvent such a drawback is to extend the free energy formula explicitly for the interface. This has been discussed by

Kikuchi et al. [33] and Kitashima et al. [34]. In the present case of a simple square lattice, the free energy is further modified as

$$
\begin{aligned}
f= & \frac{\omega}{4}\left[\sum_{i j} e_{i j} \cdot y_{i j}^{(\alpha \beta), n}+\sum_{j, l} e_{j l} \cdot y_{j l}^{(\beta \delta), n}+\sum_{l k} e_{l k} \cdot y_{l k}^{(\delta \gamma), n+1}+\sum_{i j} e_{k i} \cdot y_{k i}^{(\gamma \alpha), n}\right] \\
& -k_{B} T \cdot\left\{\frac{1}{2}\left\{\sum_{i j} L\left(y_{i j}^{(\alpha \beta), n}\right)+\sum_{j, l} L\left(y_{j l}^{(\beta \delta), n}\right)+\sum_{l k} L\left(y_{l k}^{(\delta \gamma), n+1}\right)+\sum_{k, i} L\left(y_{k i}^{(\gamma \alpha), n}\right)\right\}\right. \\
& \left.-\frac{1}{4}\left\{\sum_{i} L\left(x_{i}^{(\alpha), n}\right)+\sum_{j} L\left(x_{j}^{(\beta), n}\right)+\sum_{l} L\left(x_{l}^{(\delta), n+1}\right)+\sum_{k} L\left(x_{k}^{(\gamma), n+1}\right)\right\}-L\left(w_{i j k l}^{n}\right)\right]
\end{aligned}
$$

where the superscripts in the cluster probabilities indicate the distinction of four sub-lattices and $n$ $(n+1)$ indicates n-th $(n+1st)$ square. Fig. 6 facilitates to understand the meaning of these superscripts. This is a natural extension of the free energy formula given by Eq. (12), but the distinction of the four sub-lattices has to fulfill the constraint given by

$$
y_{i j}^{(\alpha \beta), n}=\sum_{l, k} w_{i j l k}^{n}=\sum_{k, l} w_{k l j i}^{n-1}
$$

The free energy function is minimized with respect to $w_{i j k l}^{n}$.

The variation of the LRO along 60 at. planes in the $\langle 10\rangle$ direction is shown in Fig. 7 for three temperatures. One can clearly see the width of the APB increases towards the transition temperature and at both the ends, $n=1$ and 60 , the equilibrium LRO (see Fig. 3) is attained. One can extend the present calculations towards the first-principles investigation by introducing the pair interaction energies $e_{i j}$ obtained by electronic structure calculations. However, more disturbance of the atomic arrangement is expected in the APB and the introduction of CDCVM is indispensable to achieve the calculation with high accuracy.

## 4. Summary
First-principles calculation of time evolution process of APB is attempted for $Fe-Pd$ $L1_{0}$-disorder transition by combining CVM and FLAPW with PFM through coarse graining operation. The length scale is uniquely fixed in a self-consistent manner in the theoretical framework and the resultant microstructural evolution is quite reasonable. It is pointed out that for further accurate calculations, it is indispensable to introduce local lattice distortion effects. Preliminary calculation on the square lattice indicates significant reduction of the transition temperature due to the introduction of the local lattice distortion effects. Furthermore, the detailed microstructure of the interface is calculated by extending the conventional CVM, yet the introduction of the local relaxation effects is again indispensable to obtain reliable results of the interface structure.

## Acknowledgements
The present work was partly supported by Next Generation Supercomputing Project, Nanoscience Program, MEXT, Japan. The author is grateful to Professor M. Ohno of Hokkaido University and Professor Y. Chen of U. Tokyo for their stimulating discussions and collaborations.

## References
[1] R. Kikuchi, Phys. Rev. 81 (1951) 998.
[2] J.M. Sanchez, D. de Fontaine, Phys. Rev. B17 (1978) 2926.
[3] T. Mohri, J.M. Sanchez, D. de Fontaine, Acta Metal. 33 (1985) 1171.
[4] See for instance, Tetsuo Mohri, Alloy Phys., in: Pfeiler (Ed.), Wiley-VCH, 2007, pp. 525-588, and references therein (Chapter 10).
[5] Y. Chen, T. Atago, T. Mohri, J. Phys. Condens. Matter 14 (2002) 1903.
[6] T. Mohri, Y. Chen, Mater. Trans. 43 (2002) 2104.
[7] Y. Chen, S. Iwata, T. Mohri, Calphad 26 (2002) 583.
[8] T. Mohri, Y. Chen, Mater. Trans. 45 (2004) 1478.
[9] T. Mohri, Y. Chen, J. Alloys Compd. 383 (2004) 23.
[10] J.M. Sanchez, F. Ducastelle, D. Gratias, Physica (Utrecht) 128A (1984) 33.
[11] L.-Q. Chen, Ann. Rev. Mater. Res. 32 (2002) 113. and references therein.
[12] D. Fan, L.-Q. Chen, Acta Mater. 45 (1997) 3297.
[13] J.W. Cahn, J.E. Hilliard, J. Chem. Phys. 28 (1958) 258.
[14] M. Ohno, T. Mohri, Mater. Sci. Eng. A312 (2001) 50.
[15] M. Ohno, T. Mohri, Mater. Trans. 42 (2001) 2033.
[16] M. Ohno, T. Mohri, Mater. Trans. 43 (2002) 2189.
[17] M. Ohno, T. Mohri, Philos. Mag. 83 (2003) 315.
[18] M. Ohno, PhD dissertation, Graduate School of Engineering, Hokkaido University, 2004.
[19] M. Ohno, T. Mohri, Mater. Trans. 47 (2006) 2718.
[20] T. Mohri, M. Ohno, Y. Chen, J. Phase Equilib. Diffus. 27 (2006) 47.
[21] R. Kikuchi, J.W. Cahn, J. Phys. Chem. Solids. 23 (1962) 137.
[22] T. Mohri, Int. J. Mater. Res. 100 (2009) 301.
[23] J.W. Connolly, A.R. Williams, Phys. Rev. B27 (1983) 5169.
[24] R. Kikuchi, J. Chem. Phys. 60 (1974) 1071.
[25] R. Kikuchi, A. Beldjenna, Physica A182 (1992) 617.
[26] R. Kikuchi, J. Phase. Equilib. 19 (1998) 412-421.
[27] R. Kikuchi, K. Masuda-Jindo, Compt. Mater. Sci. 14 (1999) 295.
[28] Y. Koizumi, S. Ogata, Y. Minamino, N. Tsuji, Philos. Mag. 86 (2006) 1243.
[29] C. Colinet, Philos. Mag. B 82 (2002) 1715.
[30] A. Van de Walle, M. Asta, Metall. Mat. Trans. A 33 (2002) 735.
[31] M. Asta, A.A. Quong, Philos. Mag. Lett. 76 (1997) 331.
[32] N.M. Rosengaard, H.L. Skriver, Phys. Rev. B 50 (1994) 4848.
[33] R. Kikuchi, J.W. Cahn, Acta Metal. 27 (1979) 1337.
[34] T. Kitashima, T. Yokokawa, A.C. Yeh, H. Harada, Intermetallics (2008) 779.