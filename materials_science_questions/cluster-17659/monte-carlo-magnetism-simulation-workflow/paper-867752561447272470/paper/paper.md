# Condensation of Eigen Microstate in Statistical Ensemble and Phase Transition
Gaoke Hu$^{1,3}$, Teng Liu$^3$, Maoxin Liu$^5$, Wei Chen$^4$, and Xiaosong Chen$^{1,2,3*}$

$^{1}$Institute of Theoretical Physics, Key Laboratory of Theoretical Physics, Chinese Academy of Sciences, P.O. Box 2735, Beijing, 100190, China;
$^{2}$School of Systems Science, Beijing Normal University, Beijing 100875, China;
$^{3}$School of Physical Sciences, University of Chinese Academy of Science, No. 19A Yuquan Road, Beijing 100049, China;
$^{4}$State Key Laboratory of Multiphase Complex Systems, Institute of Process Engineering, Chinese Academy of Sciences, Beijing 100190, China;
$^{5}$State Key Laboratory of Information Photonics and Optical Communications & School of Science, Beijing University of Posts and Telecommunications, Beijing 100876, China

Received November 20, 2018; accepted December 6, 2018

In a statistical ensemble with $M$ microstates, we introduce an $M \times M$ correlation matrix with the correlations between microstates as its elements. Using eigenvectors of the correlation matrix, we can define eigen microstates of the ensemble. The normalized eigenvalue by $M$ represents the weight factor in the ensemble of the corresponding eigen microstate. In the limit $M \to \infty$, weight factors go to zero in the ensemble without localization of microstate. The finite limit of weight factor when $M \to \infty$ indicates a condensation of the corresponding eigen microstate. This indicates a phase transition with new phase characterized by the condensed eigen microstate. We propose a finite-size scaling relation of weight factors near critical point, which can be used to identify the phase transition and its universality class of general complex systems. The condensation of eigen microstate and the finite-size scaling relation of weight factors have been confirmed by the Monte Carlo data of one-dimensional and two-dimensional Ising models.

PACS number(s): 05.50.+q, 05.70.Fh

Citation: Hu G K, Liu T, Liu M X, et al, Condensation of Eigen Microstate in Statistical Ensemble and Phase Transition, Sci. China-Phys. Mech. Astron. 62, 000000 (2018), doi: 10.1007/s11432-016-0037-0

## 1 Introduction
In statistical physics, the concept of ensemble in phase space serves as a starting point. An ensemble in phase space is composed of the microstates of system under some thermodynamic conditions. Thermodynamic quantities of system can be obtained by the ensemble-average with the summation over all microstates of the ensemble.

Three important thermodynamic ensembles were defined by J. W. Gibbs [1]. They are the micro-canonical ensemble, the canonical ensemble, and the grand canonical ensemble. The micro-canonical ensemble is under the thermodynamic conditions that the number of particles $N$, the volume $V$, and the total energy $E$ of system are fixed. In the canonical ensemble, the energy of system is not known exactly. In place of the energy, the temperature $T$ is specified. In the grand canonical ensemble, neither the energy nor particle number are fixed. In their place, the temperature $T$ and chemical potential $\mu$ are specified.

In computer simulations or experimental investigations of complex systems under some conditions, snapshots of system can be taken. From these snapshots, we can obtain at first microstates and then a statistical ensemble of the system. In this paper, we study the correlations between microstates in the statistical ensemble. With the correlations between mi-

*Corresponding author (email: chenxs@bnu.edu.cn )

crostates as its elements, we can get a correlation matrix of microstate in the statistical ensemble. Using the eigenvectors of the correlation matrix, the eigen microstates of the statistical ensemble can be defined. The normalized eigenvalues by the number of microstate represent the weight factors of the corresponding eigen microstates in the ensemble. The distribution of eigen microstate in the statistical ensemble can be described by all weight factors.

Our paper is organized as follows. In Section 2, we introduce the correlation between microstate and a correlation matrix. Using its eigenvectors, the eigen microstates of the ensemble are calculated. In one-dimensional and two-dimensional Ising models, their eigen microstates and eigenvalues are studied using the Monte Carlo (MC) simulations. In Section 3, we propose a finite-size scaling relation of the weight factors near critical point, which is confirmed by MC simulation data of Ising models. We make some conclusions finally in Section 4.

## 2 Eigen microstates of statistical ensemble and condensation
We consider an Ising model with the Hamiltonian
$$
H=-\sum_{\langle i, j\rangle} J_{i j} S_{i} S_{j}, \tag{1}
$$
where $S_{i}= \pm 1$ is the spin on site $i$ and $J_{i j}$ is the interaction between spins $i$ and $j$. For the Ising model with $N$ spins, a microstate $I$ of system can be described by a vector with $N$ components as
$$
\boldsymbol{A}^{I}=\frac{1}{\sqrt{N}}\left[\begin{array}{c}
S_{1}^{I} \\
S_{2}^{I} \\
\vdots \\
S_{N}^{I}
\end{array}\right], \tag{2}
$$
which is normalized and $|\boldsymbol{A}^{I}|^{2}=\left[\boldsymbol{A}^{I}\right]^{T} \cdot \boldsymbol{A}^{I}=1$. The total energy of system at microstate $\boldsymbol{A}^{I}$ can be written as $H^{I}=-N\left[\boldsymbol{A}^{I}\right]^{T} \cdot \hat{\boldsymbol{J}} \cdot \boldsymbol{A}^{I}$ with the interaction matrix $\hat{\boldsymbol{J}}$ defined by $J_{i j}$.

At temperature $T$, the microstate $\boldsymbol{A}^{I}$ has a probability
$$
p\left(\boldsymbol{A}^{I}\right)=\frac{1}{Z} e^{-H^{I} / k_{B} T}, \tag{3}
$$
where $Z=\sum_{I} e^{-H^{I} / k_{B} T}$ and $k_{B}$ is the Boltzmann constant. In MC simulations, different microstates of system can be sampled with the probability factor. $M$ microstates from simulation are taken to build up an ensemble. The correlation between microstates $I$ and $J$ is defined as
$$
C_{I J}=\left[\boldsymbol{A}^{I}\right]^{T} \cdot \boldsymbol{A}^{J}. \tag{4}
$$
If $\boldsymbol{A}^{J}=\boldsymbol{A}^{I}, C_{I J}=1$. When $\boldsymbol{A}^{J}=-\boldsymbol{A}^{I}, C_{I J}=-1$. We have $-1 \leqslant C_{I J} \leqslant 1$ in general.

With $C_{I J}$ as its elements, an $M \times M$ correlation matrix $\boldsymbol{C}$ is obtained. We suppose that $\boldsymbol{C}$ has $M$ eigenvectors $\boldsymbol{b}_{1}, \boldsymbol{b}_{2}, \cdots, \boldsymbol{b}_{M}$ with associated eigenvalues $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{M}$. We arrange all eigenvalues in the order $\lambda_{1} \geqslant \lambda_{2} \cdots \geqslant \lambda_{M}$. There is a relation
$$
\boldsymbol{C} \boldsymbol{b}_{I}=\lambda_{I} \boldsymbol{b}_{I}, I=1,2,..., M, \tag{5}
$$
where
$$
\boldsymbol{b}_{I}=\left[\begin{array}{c}
b_{1 I} \\
b_{2 I} \\
\vdots \\
b_{M I}
\end{array}\right]. \tag{6}
$$

The normalized eigenvectors are orthogonal each other and follow the relation
$$
\boldsymbol{b}_{I}^{T} \cdot \boldsymbol{b}_{J}=\sum_{l=1}^{M} b_{l I} b_{l J}=\delta_{I, J}, \tag{7}
$$
where $\delta_{I, J}$ is the Kronecker delta. The trace of the correlation matrix is $\operatorname{tr}[\boldsymbol{C}]=\sum_{I=1}^{M} \lambda_{I}=M$.

From the $M$ eigenvectors, we can define an $M \times M$ matrix
$$
\boldsymbol{U}=\left[\boldsymbol{b}_{1} \boldsymbol{b}_{2} \cdots \boldsymbol{b}_{M}\right] \tag{8}
$$
with elements $U_{I J}=b_{I J}$. $\boldsymbol{U}$ is an orthogonal matrix and satisfies the condition $\boldsymbol{U}^{T} \cdot \boldsymbol{U}=\boldsymbol{U} \cdot \boldsymbol{U}^{T}=\boldsymbol{I}$. After the $\boldsymbol{U}$ transformation of the correlation matrix, we have $\boldsymbol{U}^{T} \cdot \boldsymbol{C} \cdot \boldsymbol{U}=\boldsymbol{\Lambda}$, where $\boldsymbol{\Lambda}$ is a diagonal matrix with elements $\Lambda_{I J}=\lambda_{I} \delta_{I, J}$.

Using the components of an eigenvector $\boldsymbol{b}_{I}$, we can introduce an eigen microstate
$$
\boldsymbol{E}^{I}=\sum_{L=1}^{M} b_{L I} \boldsymbol{A}^{L}, I=1,2, \cdots, M, \tag{9}
$$
which satisfies the relation $|\boldsymbol{E}^{I}|^{2}=\left[\boldsymbol{E}^{I}\right]^{T} \cdot \boldsymbol{E}^{I}=\lambda_{I}$. The correlation between eigen microstates $I$ and $J$ is
$$
C_{I J}^{E}=\left[\boldsymbol{E}^{I}\right]^{T} \cdot \boldsymbol{E}_{J}=\sum_{l, m}^{M} b_{l I} C_{l m} b_{m J}=\lambda_{I} \delta_{I, J}. \tag{10}
$$

Therefore, the correlation matrix $\boldsymbol{C}^{E}$ is diagonal and there is no correlation between eigen microstates.

In the ensemble consisting of original microstates, all microstates have the same weight. The weight factor of microstate $I$
$$
w_{I}=C_{I I} / M=1 / M, \tag{11}
$$


which satisfies the normalization condition $\sum_{I=1}^{M} w_{I}=1$.

In the ensemble consisting of eigen microstates, different microstates have different weights. We define the weight factor of eigen microstate $I$ as
$$
w_{I}^{E}=C_{I I}^{E} / M=\lambda_{I} / M, \quad(12)
$$
which satisfies a normalization condition $\sum_{I=1}^{M} w_{I}^{E}=1$.

In an ensemble without localization of microstate, all weight factors $w_{I}^{E} \rightarrow 0$ in the limit $M \rightarrow \infty$. If the largest weight factor $w_{1}^{E}$ becomes finite in the limit $M \rightarrow \infty$, this indicates a condensation of eigen microstate $\boldsymbol{E}^{1}$ in the ensemble. This condensation of microstate is similar to the Bose-Einstein condensation [2]. Now system has a phase transition with the new phase characterized by the eigen microstate $\boldsymbol{E}^{1}$.

The eigenvalue $\lambda_{I}$ depends on $T, N$, and $M$ and $\lambda_{I}=$ $\lambda_{I}(T, N, M)$. In the limit $M \rightarrow \infty$ at fixed $x=I / M$, an eigenvalue function $\lambda(T, N, x) \equiv \lim _{M \rightarrow \infty} \lambda_{I}(T, N, M)$ is obtained.
The normalized condition of eigenvalue function is
$$
\int_{0}^{1} \lambda(T, N, x) d x=1. \quad(13)
$$

In the limit $M \rightarrow \infty$, the finite $w_{1}^{E}$ implies that the eigenvalue function $\lambda(T, N, x) \rightarrow \infty$ when $x \rightarrow 0$.

Original microstates can be expressed by eigen microstates as
$$
\boldsymbol{A}^{I}=\sum_{J=1}^{M} b_{J I} \boldsymbol{E}^{J}, I=1,2,..., M. \quad(14)
$$

Since $|E^{I}|^{2}=\lambda_{I}$ , a normalized eigen microstate $\overline{E}^{I}=\lambda_{I}^{-1 / 2} E^{I}$ is introduced. With normalized eigen microstates, We have
$$
\boldsymbol{A}^{I}=\sum_{J=1}^{M} b_{J I} \lambda_{J}^{1 / 2} \overline{\boldsymbol{E}}^{J}, I=1,2,..., M. \quad(15)
$$

In the ensemble of original microstate, the magnetization of system can be calculated as
$$
\langle m\rangle=\frac{1}{M} \sum_{I=1}^{M} m_{I}, \quad(16)
$$
where
$$
m_{I}=\frac{1}{\sqrt{N}} \sum_{i=1}^{N} A_{i}^{I} \quad(17)
$$
is the magnetization of original microstate $I$.

Equivalently, we can write the magnetization of system according to Eq. (14) as
$$
\langle m\rangle=\sum_{J=1}^{M} \bar{b}_{J}\left[w_{J}^{E}\right]^{1 / 2} m_{J}^{e}, \quad(18)
$$
where
$$
m_{J}^{e}=\frac{1}{\sqrt{N}} \sum_{i=1}^{N} \bar{E}_{i}^{J}, \quad(19)
$$

$$
\bar{b}_{J}=\frac{1}{\sqrt{M}} \sum_{I=1}^{M} b_{J I}. \quad(20)
$$

Other thermodynamics quantities of system can be calculated in a similar way.

In the following, we will study the eigen microstates and their weight factors in the statistical ensembles of one-dimensional and two-dimensional Ising models.

### 2.1 One-dimensional Ising model

The one-dimensional (1d) Ising model with the nearest-neighbour interaction has the Hamiltonian
$$
H=-J \sum_{i=1}^{N} S_{i} S_{i+1}. \quad(21)
$$

Under the periodic boundary condition $S_{N+1}=S_{1}$, this model can be solved exactly [3]. In the thermodynamic limit $N \rightarrow \infty$, its correlation function has an exponential form
$$
\left\langle S_{i} S_{j}\right\rangle=\exp \left(-\left|x_{i}-x_{j}\right| / \xi\right) \quad(22)
$$
with the correlation length
$$
\xi=\tilde{a}\left(\ln \left[\operatorname{coth}\left(1 / T^{*}\right)\right]\right)^{-1}, \quad(23)
$$
where $\tilde{a}$ is the lattice spacing and $T^{*}=k_{B} T / J$. In a finite1d-Ising chain with periodic boundary condition, the system has susceptibility [4]
$$
\chi\left(T^{*}, N\right)=\left(\frac{1+e^{-\tilde{a} / \xi}}{1-e^{-\tilde{a} / \xi}}\right)\left(\frac{1-e^{-L / \xi}}{1+e^{-L / \xi}}\right), \quad(24)
$$
where $L=N \tilde{a}$. The correlation length $\xi \rightarrow \infty$ when $T \rightarrow 0$. Although it has been well acknowledged that there is no phase transition in such an 1d-Ising model, we can still consider the zero temperature as a critical point since the correlation length diverges. The thermodynamic quantities of1d-Ising model should have similar critical behaviors above $T_{c}$ as that of $d$-dimensional Ising model with $d \geqslant 2$. Near $T=0$, the susceptibility satisfies asymptotically a finite-size scaling relation
$$
\chi\left(T^{*}, N\right)=(L / \tilde{a})^{\gamma / v} f_{\chi}(L / \xi) \quad(25)
$$
with $\gamma / v=1[3]$ and the finite-size scaling function
$$
f_{\chi}(x)=\frac{2}{x} \cdot \frac{1-e^{-x}}{1+e^{-x}}. \quad(26)
$$

Using the hyperscaling relation $d-2 \beta / v=\gamma / v$ for 1d-Ising model, we obtain $\beta=0$, which is in agreement with that of Ref. [3].

![](./images/867752561447272470_1.jpg)

**Figure 1** The largest three normalized eigenvalues of 1d-Ising model with $N = 10^5$ spins.

We simulate the microstates of 1d-Ising model using the Wolff algorithm [5]. Simulations are started with all spins aligned. To get the microstates in equilibrium, the first $10^4$ microstates are not used. The subsequent microstates are chosen at an interval of 205 MC steps to keep their independence. Using the microstates obtained, we can get the correlation matrix $\boldsymbol{C}$. With the eigenvectors and eigenvalues of $\boldsymbol{C}$, we can obtain eigen microstates according to Eq. (9).

The $M$-dependence of eigenvalue has been studied. At $M \approx 10^4$, the $M$-dependence of the largest three normalized eigenvalues can be neglected. We show the largest three normalized eigenvalues at $M = 2 \times 10^4$ in Fig. 1.

We can see from Fig. 1 that the weight factor become finite with the decrease of temperature. This indicates that there will be a phase transition. To identify the new phase of system, the corresponding eigen microstates should be studied.

![](./images/867752561447272470_2.jpg)

**Figure 2** The largest eigen microstate $\sqrt{N}\overline{\boldsymbol{E}}^1$ (a), the second largest eigen microstate $\sqrt{N}\overline{\boldsymbol{E}}^2$ (b), and the third largest eigen microstate $\sqrt{N}\overline{\boldsymbol{E}}^3$ (c) of 1d-Ising model.

At $T^* = 0.5$, the eigen microstates of the largest three eigenvalues are shown in Fig. 2. In these eigen microstates, spin clusters are of micro scales and distributed with alter-nate orientation in the real space.

![](./images/867752561447272470_3.jpg)

**Figure 3** The largest eigen microstate $\sqrt{N}\overline{\boldsymbol{E}}^1$ (a), the second largest eigen microstate $\sqrt{N}\overline{\boldsymbol{E}}^2$ (b), and the third largest eigen microstate $\sqrt{N}\overline{\boldsymbol{E}}^3$ (c) of 1d-Ising model.

The largest three eigen microstates at $T^* = 0.2$ are presented in Fig. 3. The sizes of clusters are comparable to that of system. Only one cluster exists in the largest eigen microstate. The second largest eigen microstate has two clusters with opposite orientation. In the third largest eigen microstate, there are four clusters with alternate orientations.

For an overview of the weight distribution of eigen microstate, we define the cumulant

$$
c(m)=\sum_{l=1}^{m} w_{l}^{E}. \tag{27}
$$

![](./images/867752561447272470_4.jpg)

**Figure 4** Weight cumulant of eigen microstate in 1d-Ising model.

In Fig. 4, the weight cumulants of 1d-Ising model are plotted. At $T^* = 0.2$, the cumulant $c(m)$ reaches nearly 1 at $m \approx 200$. So the original microstates are constituted actually by about 200 eigen microstates. At $T^* = 0.5$, $c(m)$ becomes nearly 1 at $m \approx 8000$, which is still much less than $M = 2 \times 10^4$.

### 2.2 Two-dimensional Ising model

In a two-dimensional (2d) Ising model with linear length $L$ and periodic boundary conditions, there are $N = L \times L$ spins in this system. With the nearest neighbor interaction $J$ and square lattice, this model has a ferromagnetic phase transition at the reduced temperature $T_{c}^{*}=k_{B} T_{c} / J=2 / \ln (1+\sqrt{2}) \approx 2.269[6]$.

![](./images/867752561447272470_5.jpg)

**Figure 5** The largest three weight factor of 2d-Ising model with $L=32$.

The microstates of the 2d-Ising model are simulated using the Wolff algorithm [5] also. In our simulations, we start with all spins aligned. The first 8000 microstates are used to reach the equilibrium. From the subsequent microstates, $M=2 \times 10^{4}$ microstates at each temperature are taken at an interval of 250 MC steps. From the microstates, we can calculate the correlation matrix at first and then its eigenvalues and eigenvectors. The eigen microstates are obtained using the eigenvectors.

The largest three eigenvalues around the critical point are presented in Fig. 5. The normalized eigenvalue by $M$ is equivalent to the weight factor. At temperatures above $T_{c}$, the largest three weight factors are quite small. There is no localization of eigen microstate. The weights of eigen microstates are distributed widely. At temperatures below $T_{c}$, the largest eigenvalues become finite. This indicates a condensation of the eigen microstate . There is now a phase transition, whose nature is characterized by the condensed eigen microstate.

The largest three eigen microstates at $T^{*}=6.2$ are shown in Fig. 6. The sizes of the spin clusters in the eigen microstates are much smaller than system size.

![](./images/867752561447272470_6.jpg)

**Figure 6** The largest eigen microstate $\sqrt{N} \overline{E}^{1}$ (a), the second largest eigen microstate $\sqrt{N} \overline{E}^{2}$ (b), and the third largest eigen microstate $\sqrt{N} \overline{E}^{3}$ (c) of 2d-Ising model above $T_{c}$.

![](./images/867752561447272470_7.jpg)

**Figure 7** The largest eigen microstate $\sqrt{N} \overline{E}^{1}$ (a), the second largest eigen microstate $\sqrt{N} \overline{E}^{2}$ (b), and the third largest eigen microstate $\sqrt{N} \overline{E}^{3}$ (c) of 2d-Ising model at $T_{c}^{*} \approx 2.269$.

![](./images/867752561447272470_8.jpg)

**Figure 8** The largest eigen microstate $\sqrt{N} \overline{E}^{1}$ (a), the second largest eigen microstate $\sqrt{N} \overline{E}^{2}$ (b), and the third largest eigen microstate $\sqrt{N} \overline{E}^{3}$ (c) of 2d-Ising model below $T_{c}$.

![](./images/867752561447272470_9.jpg)

**Figure 9** The largest eigen microstate $\sqrt{N} \overline{E}^{1}$ (a), the second largest eigen microstate $\sqrt{N} \overline{E}^{2}$ (b), and the third largest eigen microstate $\sqrt{N} \overline{E}^{3}$ (c) of 2d-Ising model below $T_{c}$.

In Fig. 7, the eigen microstates of the largest three eigenvalues at $T_{c}^{*} \approx 2.269$ are presented. There is only one cluster in the eigen microstate of the largest eigenvalue.

We plot in Fig. 8 the eigen microstates of the largest three eigenvalues at $T^{*}=2.2$. In the largest eigen microstate, there is only one spin cluster. The large-$M$ limit of its weight factor

is larger than 0.6, as shown in Fig. 10. There is a ferromagnetic phase transition. The second largest eigen microstate has two clusters with opposite orientation. There are four spin clusters in the third largest eigen microstate.

![](./images/867752561447272470_10.jpg)

Figure 10 Weight cumulant of eigen microstate in 2d-Ising model.

With the further decrease of temperature, the largest eigen microstate $E_1$ with one spin cluster becomes more dominant. The weight factor of the largest eigen microstate at $T^*=1.4$ is larger than 0.98, which can be seen in Fig. 10. Other eigen microstates have many small clusters, as shown in Fig. 9.

The weight cumulants of eigen microstate at $T^*$ = 1.4,2.2,2.269,6.2 are shown in Fig. 10. The weight cumulants reach nearly 1 at $m \approx 1000$. The $2 \times 10^4$ original microstates are composed of 1000 eigen microstates approximately.

## 3 Finite-size scaling of weight factor near critical point

In the region near a critical point, thermodynamic functions of finite system are proposed to satisfy finite-size scaling relations [7-9]. For the order parameter, its finite-size relation is
$$
\langle m\rangle(t, L)=L^{-\beta / v} f_{m}\left(t L^{1 / v}\right) \tag{28}
$$
where $t=(T-T_c)/T_c$ is the reduced temperature, $\beta$ is the critical exponent of order parameter, and $v$ is the critical exponent of bulk correlation length $\xi=\xi_0 t^{-v}$. The scaling variable $t L^{1 / v}$ is related to the size ratio $L / \xi$.

The correlation length follows the finite-size scaling form $\xi(t, L)=L X(t L^{1 / v})$ [8]. Recently, a finite-size scaling relation of correlation function was proposed [10]. Using this finite-size relation, the finite-size scaling form of correlation length can be naturally derived. For the principal fluctuation modes of complex system, there is also a finite-size scaling relation [11], which has been confirmed in 2d-Ising model.

Basing on the relation between the weight factor of eigen microstate and the order parameter, we propose a finite-size scaling form
$$
w_{I}^{E}(t, L)=L^{-2 \beta / v} F_{w}^{I}\left(t L^{1 / v}\right). \tag{29}
$$

In one-dimensional Ising model, the critical exponent $\beta=0$ and $w_{I}^{E}(T, L)=F_{w}^{I}(L / \xi)$, where $\xi$ is given in Eq. (23). We present the largest two weight factors with respect to $T^*$ and scaling variable $L / \xi$ in Fig. 11. The finite-size scaling form of Eq. (29) is confirmed in 1d-Ising model.

![](./images/867752561447272470_11.jpg)

Figure 11 The largest two weight factors of 1d-Ising model with respect to $T^*$ and $L/\xi$.

In two-dimensional Ising model, the critical exponents $v=1$ and $\beta=1/8$ [6]. On the left side of Fig. 12, the largest weight factor $w_1^E$ of $L=32,64,128$ are plotted with respect to $T^*$. The finite-scaling form $w_1^E L^{2\beta/v}$ is presented with respect to $t L^{1 / v}$ on the right side. The different curves for different $L$ collapse together. The finite-size relation of Eq. (29) is confirmed in 2d-Ising model.

![](./images/867752561447272470_12.jpg)

Figure 12 The largest weight factor and its finite-size scaling form in 2d-Ising model.

![](./images/867752561447272470_13.jpg)

Figure 13 The second largest weight factor and its finite-size scaling form in 2d-Ising model.

![](./images/867752561447272470_14.jpg)

Figure 14 The third largest weight factor and its finite-size scaling form in 2d-Ising model.

In Figs. 13 and 14, the second and third largest weight factors and their finite-size scaling form are presented.

After taking logarithm of Eq. (29), we obtain

$$
\ln w_{I}^{E}(t, L)=-(2 \beta / v) \ln L+\ln F_{w}^{I}\left(t L^{1 / v}\right), \tag{30}
$$

which depends on $\ln L$ linearly at $t=0$. This property can be used to determine the critical point and the critical exponent ratio $\beta / v$.

![](./images/867752561447272470_15.jpg)

Figure 15 Log-log plot of the largest normalized eigenvalue around $T_{c}$.

In Fig. 15, the log-log plot of the largest weight factor $w_{1}^{E}$ with respect to $L$ is presented at different reduced temperatures. The curves are curved upward at $T>T_{c}$ and downward at $T<T_{c}$. From the straight line at $T_{c}^{*} \approx 2.269$, we can obtain $2 \beta / v=0.246(6)$, which is in agreement with the exact value $2 \beta / v=1 / 4$ [6].

We introduce the ratio of weight factor $R \equiv w_{2}^{E} / w_{1}^{E}$, which follows the finite-size scaling form

$$
R(t, L)=F_{w}^{2} / F_{w}^{1}=\tilde{R}\left(t L^{1 / v}\right). \tag{31}
$$

At the critical point, the ratio $R(0, L)=\tilde{R}(0)$ is independent of $L$. This can be used to determine the critical point also.

![](./images/867752561447272470_16.jpg)

Figure 16 Ratio of the largest eigenvalue to the second largest eigenvalue.

The ratio $R(t, L)$ of 2d-Ising model is plotted in Fig. 16. With $T^{*}$ as the variable, curves of different $L$ have a fixed point at $T_{c}$. Using $t L^{1 / v}$ as the variable, the curves collapse together.

Therefore, the finite-size scaling relation of weight factor in Eq. (29) has been verified in one-dimensional and two-dimensional Ising models. We anticipate that this finite-size relation is valid for general complex systems.

## 4 Conclusions

In the phase space of a complex system, we introduce the eigen microstates of its statistical ensemble. The microstates of the complex system under some conditions can be obtained from computer simulations or experimental studies. We introduce a correlation matrix with correlations between microstates as its elements. Using the eigenvectors of the correlation matrix, the eigen microstates of the ensemble can be defined. The normalized eigenvalues by the number of microstate $M$ can be considered as the weight factor in the ensemble of the corresponding eigen microstates.

In an ensemble without localization of microstate, weight factors of eigen microstate go to zero when $M \to \infty$. If the largest weight factor becomes finite in the limit $M \to \infty$, there is a condensation of the eigen microstate in the ensemble. This condensation indicates a phase transition with the new phase characterized by the eigen microstate corresponding to the finite weight factor. We propose a finite-size scaling relation of the weight factors near critical point using the critical exponents of order parameter and correlation length.

The eigen microstates and their weight factors in an ensemble of one-dimensional and two-dimensional Ising models have been studied using Monte Carlo simulation. The condensation of eigen microstate in the one-dimensional Ising model appears when $T \to 0$. All spins of the condensed eigen microstate have the same orientation and there is a ferromagnetic phase transition. In two-dimensional Ising model, condensations of eigen microstate are found at the reduced temperatures $T^* < T_c^* = 2/\ln(1+\sqrt{2})$. In the condensed eigen microstate, all spins have the same orientation and there is a ferromagnetic phase transition in two-dimensional Ising model. The finite-size scaling relation of weight factors is confirmed by the Monte Carlo simulation results of one-dimensional and two-dimensional Ising models. Further, we will study the eigen microstates and their weight factors of statistical ensemble for complex systems such as confined fluids [12], networks with long-range connections [13], and climate systems [14].

In the studies of phase transitions of complex systems, the definition of order parameter is sometimes a challenge. We can take collective motion as an example. Collective motion exists at almost every scale in nature, from unicellular organisms to bird flocks, fish schools, and human crowds [15]. The simple model of collective motion was introduced by Vicsek and collaborators [16].The transition to collective motion in the Vicsek model (VM) is thought to be critical [16] and discontinuous [17]. More phases such as ordered "Toner-Tu" phase [18] and band phases [19-21] are suggested to exist in the VM. A global understanding and the real order parameter of the transition to collective motion is still lacking. Using the method proposed here, we can determine the critical point, the order parameter, and the critical exponents of complex system at the same time. Our method of analysis is not restricted to systems in equilibrium.

This work was support by Key Research Program of Frontier Sciences, Chinese Academy of Sciences (Grant No. QYZD-SSW-SYS019). Our Monte Carlo simulations are supported by HPC Cluster of ITP-CAS. We are grateful to insight discussions with Prof. Jinghai Li.

Conflict of interest The authors declare that they have no conflict of interest.

1 J. Willard Gibbs. *Elementary Principles in Statistical Mechanics*. New York: Charles Scribner's Sons, 1902.
2 Lev Petrovich Pitaevski and S Stringari. *Bose-Einstein Condensation*. Clarendon Press, 2003.
3 Rodney J Baxter. *Exactly Solved Models in Statistical Mechanics*. Academic Press, London, 1982.
4 XiaoSong Chen and Volker Dohm. Relation between bulk order-parameter correlation function and finite-size scaling. *The European Physical Journal B - Condensed Matter and Complex Systems*, 15(2):283-296, 2000.
5 Ulli Wolff. Collective monte carlo updating for spin systems. *Phys. Rev. Lett.*, 62(4):361-364, 1989.
6 Lars Onsager. Crystal statistics. i. a two-dimensional model with an order-disorder transition. *Phys. Rev.*, 65(3-4):117-149, Feb 1944.
7 Michael E. Fisher and Michael N. Barber. Scaling theory for finite-size effects in the critical region. *Phys. Rev. Lett.*, 28(23):8-11, 1972.
8 Vladimir Privman and Michael E. Fisher. Universal critical amplitudes in finite-size scaling. *Phys. Rev. B*, 30:322-327, Jul 1984.
9 Vladimir Privman, Ammon Aharony, and P.C. Hohenberg. Universal critical-point amplitude relations. In Cyril Domb and Joel Louis Lebowitz, editors, *Phase Transitions and Critical Phenomena*, volume 14, page 1. Academic, New York, 1991.
10 Xin Zhang, GaoKe Hu, YongWen Zhang, XiaoTeng Li, and XiaoSong Chen. Finite-size scaling of correlation functions in finite systems. *Science China Physics, Mechanics & Astronomy*, 61(12):120511, Oct 2018.
11 XiaoTeng Li and XiaoSong Chen. Critical behaviors and finite-size scaling of principal fluctuation modes in complex systems. *Commun. Theor. Phys.*, 66(3):355, 2016.
12 Wei Dong and XiaoSong Chen. Scaled particle theory for bulk and confined fluids: A review. *Science China Physics, Mechanics & Astronomy*, 61(7):070501, Jul 2018.
13 ZiQing Yang, MaoXin Liu and XiaoSong Chen. Criticality of networks with long-range connections. *Science China Physics, Mechanics & Astronomy*, 60(2):020521, Feb 2017.
14 JingFang Fan, Jun Meng, XiaoSong Chen, Yosef Ashkenazy, and Shlomo Havlin. Network approaches to climate science. *Science China Physics, Mechanics & Astronomy*, 60(1):010531, Jan 2017.
15 Tamás Vicsek and Anna Zafeiris. Collective motion. *Physics Reports*, 517(3-4):71-140, Aug 2012.
16 Tams Vicsek, Andrs Czirk, Eshel Ben-Jacob, Inon Cohen, and Ofer Shochet. Novel type of phase transition in a system of self-driven particles. *Phys. Rev. Lett.*, 75(6):1226-1229, Aug 1995.
17 Guillaume Grégoire and Hugues Chaté. Onset of Collective and Cohesive Motion. *Phys. Rev. Lett.*, 92(2):025702, Jan 2004.
18 John Toner and Yuhai Tu. Long-range order in a two-dimensional dynamical XY model: How birds fly together. *Phys. Rev. Lett.*, 75(23):4326, Dec 1995.
19 Eric Bertin, Michel Droz, and Guillaume Grégoire. Boltzmann and hydrodynamic description for self-propelled particles. *Phys. Rev. E*,

74(2):022101, Aug 2006.

20 Shradha Mishra, Aparna Baskaran, and M. Cristina Marchetti. Fluctuations and pattern formation in self-propelled particles. Phys. Rev. E ,
81(6):061916, Jun 2010.

21 Thomas Ihle. Kinetic theory of flocking: Derivation of hydrodynamic equations. Phys. Rev. E , 83(3):030901, Mar 2011.