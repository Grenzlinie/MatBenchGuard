# Exact physical quantities of a competing spin chain in the thermodynamic limit

Pengcheng Lu$^{a,b}$, Yi Qiao$^{a,b1}$, Junpeng Cao$^{b,c,d,e2}$ and Wen-Li Yang$^{a,e,f3}$

$^{a}$ Institute of Modern Physics, Northwest University, Xian 710127, China
$^{b}$ Beijing National Laboratory for Condensed Matter Physics, Institute of Physics, Chinese Academy of Sciences, Beijing 100190, China
$^{c}$ School of Physical Sciences, University of Chinese Academy of Sciences, Beijing 100049, China
$^{d}$ Songshan Lake Materials Laboratory, Dongguan, Guangdong 523808, China
$^{e}$ Peng Huanwu Center for Fundamental Theory, Xian 710127, China
$^{f}$ Shaanxi Key Laboratory for Theoretical Physics Frontiers, Xian 710127, China

## Abstract
We study the exact physical quantities of a competing spin chain which contains many interesting and meaningful couplings including the nearest neighbor, next nearest neighbor, chiral three spins, Dzyloshinsky-Moriya interactions and unparallel boundary magnetic fields in the thermodynamic limit. We obtain the density of zero roots, surface energies and elementary excitations in different regimes of model parameters. Due to the competition of various interactions, the surface energy and excited spectrum show many different pictures from those of the Heisenberg spin chain.

Keywords: Quantum spin chain; Bethe ansatz; Yang-Baxter equation

---
$^{1}$Corresponding author: qiaoyi_joy@foxmail.com
$^{2}$Corresponding author: junpengcao@iphy.ac.cn
$^{3}$Corresponding author: wlyang@nwu.edu.cn

## 1 Introduction

Quantum integrable models [1] are very important to analyze some non-pertubative properties of quantum field/string theory [2,3]. Moreover, the exact solutions and physical properties of these models can provide the strict benchmarks for many important physics issues, and sometimes it can exactly predict and explain the results of experiments [4-6]. In recent years, the study of quantum integrable models play an important role in the non-equilibrium statistical physics [7-10], condensed matter physics [11], cold atom physic [12,13], superstring theory AdS/CFT [14-16] and so on.

For the integrable models with $U(1)$ symmetry, the exact solutions of the models can be obtained by the conventional Bethe ansatz. In addition, due to the homogeneous Bethe ansatz equations (BAEs) and the regular pattern of the Bethe roots, the thermodynamic properties can be directly calculated by the thermodynamic Bethe ansatz (TBA) [17,18]. When the $U(1)$ symmetry of integrable systems is broken, the off-diagonal Bethe ansatz can be used to solve the systems based on the algebraic analysis [19]. However, since the exact solutions of the systems are described by the inhomogeneous $T-Q$ relations [20,21] and the resulting inhomogeneous BAEs have the inhomogeneous term, the pattern of Bethe roots is not clear and the TBA method can not be applied. Recently, a novel Bethe ansatz scheme has been proposed to calculate the physical quantities of quantum integrable systems with or without $U(1)$ symmetry [22,23]. The key point of the scheme lies in parameterizing the eigenvalue of transfer matrix by its zero roots instead of the Bethe roots. Through this method, the homogeneous BAEs and the well-defined patterns of zero roots can be obtained. Based on them, the thermodynamic properties and exact physical quantities of the systems in the thermodynamic limit can also be calculated. In this paper, we study an isotropic quantum spin chain which includes the nearest neighbor (NN) [24], next nearest neighbor (NNN) [25], Dzyloshinsky-Moriya (DM) interactions [26,27], chirality three-spin couplings [28] and unparallel boundary magnetic fields [29]. The density of zero roots, surface energy and elementary excitations in different regimes of model parameters are obtained.

The paper is organized as follows. Section 2 serves as an introduction to the model and explain its integrability. In section 3, we give the patterns of zero roots in the different regimes of model parameters. In section 4, we calculate the surface energies induced by the boundary magnetic fields. In section 5, we study the typical bulk elementary excitations in

the system. The boundary excitations are computed in section 6. In section 7, we calculate the surface energies in ferromagnetic regime. Concluding remarks are given in section 8. A simple method is introduced in Appendix A..

## 2 Integrability of the model

The model Hamiltonian reads

$$
H=H_{b u l k}+H_{L}+H_{R}.\qquad(2.1)
$$

Here $H_{bulk}$ describe the interactions in the bulk which includes the NN, NNN and chiral three spin couplings with the form of

$$
H_{b u l k}=\sum_{j=1}^{2 N-1}\left\{J_{1} \vec{\sigma}_{j} \cdot \vec{\sigma}_{j+1}+J_{2} \vec{\sigma}_{j} \cdot \vec{\sigma}_{j+2}+J_{3}(-1)^{j} \vec{\sigma}_{j+1} \cdot\left(\vec{\sigma}_{j} \times \vec{\sigma}_{j+2}\right)\right\},\qquad(2.2)
$$

where $\sigma_{j}^{\alpha}(\alpha=x, y, z)$ is the Pauli matrix along the $\alpha$-direction on the $j$-th site, and $2 N$ is the number of sites. We note that the convention $\vec{\sigma}_{2 N+1}=0$ has been used. $H_{L}$ quantifies the left boundary terms which includes the boundary magnetic field along the $z$-direction and the anisotropic and DM interactions of the first bond

$$
H_{L}=\frac{1-4 a^{2}}{p^{2}-a^{2}}[p \sigma_{1}^{z}-a^{2} \sigma_{1}^{z} \sigma_{2}^{z}-i a p D_{1}^{z} \cdot(\vec{\sigma}_{1} \times \vec{\sigma}_{2})],\qquad(2.3)
$$

where $p$ is the strength of magnetic field, $a^{2}$ and $a p$ quantify the spin-exchanging and DM interactions respectively, and $D_{1}^{z}$ is the unit vector along the $z$-direction. $H_{R}$ characterizes the right boundary terms which includes the boundary magnetic field lies in the $x-z$ plane, anisotropic and DM interactions of the last bond also constrained in the $x-z$ plane. Thus $H_{R}$ reads

$$
\begin{aligned}
H_{R}= & \frac{4 a^{2}-1}{a^{2} \xi^{2}+a^{2}-q^{2}}[q(\xi \sigma_{2 N}^{x}+\sigma_{2 N}^{z})-a^{2}(\xi \sigma_{2 N-1}^{x}+\sigma_{2 N-1}^{z})(\xi \sigma_{2 N}^{x}+\sigma_{2 N}^{z}) \\
& \left.-i a q(\xi D_{2 N}^{x}+D_{2 N}^{z}) \cdot(\vec{\sigma}_{2 N} \times \vec{\sigma}_{2 N-1})\right],
\end{aligned}\qquad(2.4)
$$

where $q$ and $\xi$ are the boundary parameters, $D_{2 N}^{x}$ is the unit vector along the $x$-direction and $D_{2 N}^{z}$ is the unit vector along the $z$-direction. We should note that the boundary fields are unparallel boundary and the $U(1)$ symmetry of the system are broken. The hermitian of the Hamiltonian (2.1) requires that the model parameter $a$ is pure imaginary and the boundary

parameters $p$, $q$, $\xi$ are real. Moreover, the integrability of the system (2.1) requires that the couplings $J_1$, $J_2$, $J_3$ satisfy the relationships

$$
J_{1}=1+c_{j}\left(\delta_{j, 1}+\delta_{j, 2 N-1}\right), \quad J_{2}=-2 a^{2}, \quad J_{3}=i a, \tag{2.5}
$$

$$
c_{1}=\frac{a^{2}\left(1-2 a^{2}-2 p^{2}\right)}{p^{2}-a^{2}}, \quad c_{2 N-1}=2 a^{2}+\frac{a^{2}\left(4 q^{2}-\xi^{2}-1\right)}{a^{2} \xi^{2}+a^{2}-q^{2}}. \tag{2.6}
$$

where the index $j$ is the summation index in $H_{bulk}$ (2.2). The Hamiltonian (2.1) is constructed by using the $R$-matrix and the reflection matrices $K^{\pm}$ based on the quantum inverse scattering method. The $R$-matrix defined in the tensor space $V_1 \otimes V_2$ is

$$
R_{1,2}(u)=u+P_{1,2}=u+\frac{1}{2}\left(1+\vec{\sigma}_{1} \cdot \vec{\sigma}_{2}\right), \tag{2.7}
$$

where $u$ is the spectral parameter and $P_{1,2}$ is the permutation operator. The $R$-matrix (2.7) satisfies the quantum Yang-Baxter equation (QYBE),

$$
R_{1,2}\left(u_{1}-u_{2}\right) R_{1,3}\left(u_{1}-u_{3}\right) R_{2,3}\left(u_{2}-u_{3}\right)=R_{2,3}\left(u_{2}-u_{3}\right) R_{1,3}\left(u_{1}-u_{3}\right) R_{1,2}\left(u_{1}-u_{2}\right). \tag{2.8}
$$

The reflection matrix $K_1^-(u)$ defined the space $V_1$ is

$$
K_{1}^{-}(u)=\left(\begin{array}{cc}
p+u & \\
& p-u
\end{array}\right), \tag{2.9}
$$

which satisfies the reflection equation (RE)

$$
R_{1,2}(\lambda-u) K_{1}^{-}(\lambda) R_{2,1}(\lambda+u) K_{2}^{-}(u)=K_{2}^{-}(u) R_{1,2}(\lambda+u) K_{1}^{-}(\lambda) R_{2,1}(\lambda-u), \tag{2.10}
$$

where $R_{2,1}(u)=P_{1,2} R_{1,2}(u) P_{1,2}$. The dual reflection matrix $K_1^+(u)$ is

$$
K_{1}^{+}(u)=\left(\begin{array}{cc}
q+u+1 & \xi(u+1) \\
\xi(u+1) & q-u-1
\end{array}\right), \tag{2.11}
$$

satisfying the dual reflection equation

$$
\begin{aligned}
& R_{1,2}(-\lambda+u) K_{1}^{+}(\lambda) R_{2,1}(-\lambda-u-2) K_{2}^{+}(u) \\
& \quad=K_{2}^{+}(u) R_{1,2}(-\lambda-u-2) K_{1}^{+}(\lambda) R_{2,1}(-\lambda+u). \tag{2.12}
\end{aligned}
$$

The monodromy matrix $T_0(u)$ and the reflecting one $\hat{T}_0(u)$ are constructed by the $R$-matrices as

$$
T_{0}(u)=R_{0,2 N}\left(u+a+\theta_{2 N}\right) R_{0,2 N-1}\left(u-a-\theta_{2 N-1}\right) \cdots R_{0,2}\left(u+a+\theta_{2}\right) R_{0,1}\left(u-a-\theta_{1}\right),
$$

$$
\hat{T}_{0}(u)=R_{0,1}\left(u+a+\theta_{1}\right) R_{0,2}\left(u-a-\theta_{2}\right) \cdots R_{0,2 N-1}\left(u+a+\theta_{2 N-1}\right) R_{0,2 N}\left(u-a-\theta_{2 N}\right), \tag{2.13}
$$


where $V_0$ is the auxiliary space, $\otimes_{j=1}^{2N}V_j$ is the quantum space, and $\{\theta_j|j=1,\cdots,2N\}$ are the inhomogeneity parameters. The transfer matrix $t(u)$ is defined as

$$
t(u)=tr_{0}\{K_{0}^{+}(u)T_{0}(u)K_{0}^{-}(u)\hat{T}_{0}(u)\},\tag{2.14}
$$

where $tr_{0}$ means the partial trace over the auxiliary space. The Hamiltonian (2.1) is generated by the transfer matrix as

$$
H=-\left.\frac{1}{2}(4a^{2}-1)\left(\left.\frac{\partial\ln t(u)}{\partial u}\right|_{u=a}+\left.\frac{\partial\ln t(u)}{\partial u}\right|_{u=-a}\right)\right|_{\{\theta_j\}=0}-c_{0},\tag{2.15}
$$

where

$$
\begin{gathered}
c_{0}=-(2N-1)(2a^{2}-1)-\frac{2a^{4}-6a^{2}+1}{a^{2}-1},\\
c_{2}=8(1-4a^{2})^{2N-2}(p^{2}-a^{2})(a^{2}-1)(a^{2}\xi^{2}+a^{2}-q^{2}).\tag{2.16}
\end{gathered}
$$

The QYBE (2.8), the RE (2.10) and its dual (2.12) guarantee the integrability of the model described by the Hamiltonian given by (2.1). Moreover, using the properties of the $R$-matrix one may easily prove that $t(u)=t(-u-1)$ and the following operator identities [19]

$$
t(\theta_{j}+a)t(\theta_{j}+a-1)=a(\theta_{j}+a)d(\theta_{j}+a-1),\quad j=1,\cdots,2N,\tag{2.17}
$$

where

$$
\begin{gathered}
a(u)=\frac{2u+2}{2u+1}(u+p)[(1+\xi^{2})^{\frac{1}{2}}u+q]\prod_{j=1}^{2N}(u+\theta_{j}+a+1)(u-\theta_{j}-a+1),\\
d(u)=a(-u-1).\tag{2.18}
\end{gathered}
$$

From the definition (2.14), we know that the transfer matrix $t(u)$ is a polynomial operator of $u$ with the degree $4N+2$. Denote the eigenvalue of the transfer matrix $t(u)$ as $\Lambda(u)$. From above analysis, we know that the eigenvalue $\Lambda(u)$ satisfies

$$
\Lambda(u)=\Lambda(-u-1),\tag{2.19}
$$

$$
\Lambda(u)=2u^{4N+2}+\cdots,\quad u\rightarrow\pm\infty,\tag{2.20}
$$

$$
\Lambda(0)=2pq\prod_{j=1}^{2N}(1-\theta_{j}-a)(1+\theta_{j}+a)=\Lambda(-1),\tag{2.21}
$$

$$
\Lambda(\theta_{j}+a)\Lambda(\theta_{j}+a-1)=a(\theta_{j}+a)d(\theta_{j}+a-1),\quad j=1,\cdots,2N.\tag{2.22}
$$


Obviously, $\Lambda(u)$ is a degree $4N+2$ polynomial of $u$ and can be parameterized as

$$
\Lambda(u)=2 \prod_{j=1}^{2 N+1}\left(u-z_{j}+\frac{1}{2}\right)\left(u+z_{j}+\frac{1}{2}\right),\tag{2.23}
$$

where $\{z_j | j=1,\cdots,2N+1\}$ are the zero roots of the polynomial. Putting the parameterizing (2.23) into (2.22), we obtain the BAEs

$$
\begin{aligned}
4 \prod_{l=1}^{2 N+1} & \left(\theta_{j}+a-z_{l}+\frac{1}{2}\right)\left(\theta_{j}+a+z_{l}+\frac{1}{2}\right)\left(\theta_{j}+a-z_{l}-\frac{1}{2}\right)\left(\theta_{j}+a+z_{l}-\frac{1}{2}\right) \\
& =a\left(\theta_{j}+a\right) d\left(\theta_{j}+a-1\right), \quad j=1, \cdots, 2 N.
\end{aligned}\tag{2.24}
$$

The above $2N$ equations and (2.21) can determine the $2N+1$ unknowns $\{z_j\}$ completely. In the homogeneous limit $\{\theta_j=0 | j=1,\cdots,2N\}$, Eq. (2.21) is replaced by

$$
\Lambda(0)=2 p q\left(1-a^{2}\right)^{2 N},\tag{2.25}
$$

and Eq. (2.22) becomes

$$
\left.[\Lambda(u+a) \Lambda(u+a-1)]^{(n)}\right|_{u=0}=\left.[a(u+a) d(u+a-1)]^{(n)}\right|_{u=0},\tag{2.26}
$$

where the superscript $(n)$ indicates the $n$-th order derivative and $n=0,1,\cdots,2N-1$. Eqs. (2.25) and (2.26) can determine the $2N+1$ zeros roots $\{z_j\}$ in the homogeneous limit in finite system size. Moreover, the energy spectrum of the Hamiltonian (2.1) can be determined by the zero roots as

$$
E=-\pi\left(4 a^{2}-1\right) \sum_{j=1}^{2 N+1}\left[a_{1}\left(i z_{j}-i a\right)+a_{1}\left(i z_{j}+i a\right)\right]-c_{0},\tag{2.27}
$$

where the function $a_n(u)$ is given by

$$
a_{n}(u)=\frac{1}{2 \pi} \frac{n}{u^{2}+n^{2} / 4}.\tag{2.28}
$$

By solving the BAEs Eqs. (2.25) and (2.26), we can obtain all the eigen-energies of the system (2.1).

## 3 Patterns of zero roots

We first study the solutions of zero roots $\{z_j\}$ at the ground state. For convenient, we choose all the inhomogeneity parameters to be imaginary, $\{\theta_j \equiv i \bar{\theta}_j\}$, and let $\{\bar{z}_j \equiv -i z_j\}$.

In addition, we set the boundary parameters as $p > 0$ and $\bar{q}=q(1+\xi^{2})^{-\frac{1}{2}}$. From the numerical calculation and algebraic analysis, we find that the distribution of the $\bar{z}$-roots at the ground state can be divided into following six different regimes in the upper $p-\bar{q}$ plane, as shown in Fig.1.

![](./images/911926818301280904_1.jpg)

Figure 1: The distribution of $\bar{z}$-roots at the ground state in the upper $p-\bar{q}$ plane.

![](./images/911926818301280904_2.jpg)

Figure 2: Pattern of $\bar{z}$-roots at the ground state in regimes I (a) and II (b) with $2N=8$. The blue asterisks indicate $\bar{z}$-roots for $\{\bar{\theta}_{j}=0|j=1,\cdots,2N\}$ and the red circles specify $\bar{z}$-roots with the inhomogeneity parameters $\{\bar{\theta}_{j}=0.1(j-N-0.5)|j=1,\cdots,2N\}$.

1) In the regime I, where $0\leq p<\frac{1}{2},0\leq \bar{q}<\frac{1}{2}$, all the $\bar{z}$-roots form $2N-2$ conjugate pairs as $\{\bar{z}_{j}\sim \tilde{z}_{j}\pm i|j=1,\cdots,2N-2\}$ with real $\{\tilde{z}_{j}\}$, two boundary conjugate pairs $\{\pm i(|p|+\frac{1}{2}),\pm i(|\bar{q}|+\frac{1}{2})\}$ and two symmetrical real roots $\bar{z}_{\pm}=\pm\alpha$. The numerical check with $2N=8$ is shown in Fig.2(a). In the thermodynamic limit, two symmetrical real roots

![](./images/911926818301280904_3.jpg)

Figure 3: (a)-(d) Patterns of $\bar{z}$-roots for $\{\bar{\theta}_{j}=0|j=1,\cdots,2N\}$ at the ground state in regimes III-VI with $2N=8$.

$\pm\alpha$ would tend to infinity and contribute nothing to the ground state energy. These two real roots correspond to the Majorana modes at the two boundaries.

2) In the regime II, where $0 \leq p < \frac{1}{2}, -\frac{1}{2} \leq \bar{q} < 0$, as shown in Fig.2(b), all the $\bar{z}$-roots form $2N-2$ conjugate pairs, two boundary conjugate pairs $\{\pm i(|p|+\frac{1}{2}),\pm i(|\bar{q}|+\frac{1}{2})\}$ and one pure imaginary conjugate pair $\pm i\beta$ with $\beta > \min(|p|,|\bar{q}|)$.

3) In the regime III, where $p \geq \frac{1}{2},0 \leq \bar{q} < \frac{1}{2}$ or $0 \leq p < \frac{1}{2},\bar{q} \geq \frac{1}{2}$, as shown in Fig.3(a), all the $\bar{z}$-roots form $2N-2$ conjugate pairs, one boundary conjugate pair $\pm i[\min(|p|,|\bar{q}|)+\frac{1}{2}]$, two symmetrical real roots $\bar{z}_{\pm}=\pm\alpha$, and one pure imaginary conjugate pair $\pm i\beta$ with $\beta > \min(|p|,|\bar{q}|)$.

4) In the regime IV, where $p \geq \frac{1}{2},-\frac{1}{2} \leq \bar{q} < 0$ or $0 \leq p < \frac{1}{2},\bar{q} \leq -\frac{1}{2}$, as shown in Fig.3(b), all the $\bar{z}$-roots form $2N$ conjugate pairs and one boundary conjugate pair $\pm i[\min(|p|,|\bar{q}|)+\frac{1}{2}]$.

5) In the regime V, where $p \geq \frac{1}{2},\bar{q} \geq \frac{1}{2}$, as shown in Fig.3(c), all the $\bar{z}$-roots form $2N$ conjugate pairs and two symmetrical real roots $\bar{z}_{\pm}=\pm\alpha$.

6) In the regime VI, where $p \geq \frac{1}{2},\bar{q} \leq -\frac{1}{2}$, as shown in Fig.3(d), all the $\bar{z}$-roots form $2N$ conjugate pairs and one pure imaginary conjugate pair $\pm i\beta$ with $\beta > \min(|p|,|\bar{q}|)$.

We also find that the choice of pure imaginary inhomogeneities $\{\bar{\theta}_{j}\}$ does not change the patterns of zero roots $\{\bar{z}_{j}\}$ but the roots density, as shown in Fig.2. This result allows us to calculate the physical quantities such as the surface energy and the elementary excitations of the system in the thermodynamic limit with the help of suitable $\{\bar{\theta}_{j}\}$ [23].

## 4 Surface energy

Now, we consider the surface energy induced by the boundaries. The surface energy is defined by $E_{b}=E_{g}-E_{p}$, where $E_{g}$ is the ground state energy of present system and $E_{p}$ is the ground state energy of the corresponding periodic chain. In the thermodynamic limit, the distribution of $\bar{z}$-roots can be characterized by the density $\rho(\bar{z})$. Furthermore, we assume that the density of inhomogeneity parameters $1/[2N(\bar{\theta}_{j}-\bar{\theta}_{j-1})]$ has the continuum limit $\sigma(\bar{\theta})$.

In regime I, substituting the corresponding pattern of $\bar{z}$-roots into BAEs (2.24) and taking the logarithm of the absolute value, we have

$$
\begin{aligned}
\ln |4|+ & \sum_{l=1}^{2N-1}\left[\ln \left|\bar{\theta}_{j}+\bar{a}-\tilde{z}_{l}+\frac{3i}{2}\right|+\ln \left|\bar{\theta}_{j}+\bar{a}-\tilde{z}_{l}+\frac{i}{2}\right|+\ln \left|\bar{\theta}_{j}+\bar{a}-\tilde{z}_{l}-\frac{i}{2}\right|+\ln \left|\bar{\theta}_{j}+\bar{a}-\tilde{z}_{l}-\frac{3i}{2}\right|\right] \\
+ & \ln \left|\left(\bar{\theta}_{j}+\bar{a}-\alpha+\frac{i}{2}\right)\left(\bar{\theta}_{j}+\bar{a}-\alpha-\frac{i}{2}\right)\right|+\ln \left|\left(\bar{\theta}_{j}+\bar{a}+\alpha+\frac{i}{2}\right)\left(\bar{\theta}_{j}+\bar{a}+\alpha-\frac{i}{2}\right)\right|
\end{aligned}
$$

$$
\begin{aligned}
+ & \ln \left|\left(\bar{\theta}_{j}+\bar{a}-i|p|\right)\left(\bar{\theta}_{j}+\bar{a}+i|p|\right)\right|+\ln \left|\left(\bar{\theta}_{j}+\bar{a}-i|p|-i\right)\left(\bar{\theta}_{j}+\bar{a}+i|p|+i\right)\right| \\
+ & \ln \left|\left(\bar{\theta}_{j}+\bar{a}-i|\bar{q}|\right)\left(\bar{\theta}_{j}+\bar{a}+i|\bar{q}|\right)\right|+\ln \left|\left(\bar{\theta}_{j}+\bar{a}-i|\bar{q}|-i\right)\left(\bar{\theta}_{j}+\bar{a}+i|\bar{q}|+i\right)\right| \\
= & \ln \left|\left(\bar{\theta}_{j}+\bar{a}+i\right)\left(\bar{\theta}_{j}+\bar{a}-i\right)\right|-\ln \left|\left(\left(\bar{\theta}_{j}+\bar{a}\right)+\frac{i}{2}\right)\left(\left(\bar{\theta}_{j}+\bar{a}\right)-\frac{i}{2}\right)\right| \\
& +\ln \left|\left(\bar{\theta}_{j}+\bar{a}+i p\right)\left(\bar{\theta}_{j}+\bar{a}-i p\right)\right|+\ln \left|\left(\left(1+\xi^{2}\right)^{\frac{1}{2}}\left(\bar{\theta}_{j}+\bar{a}\right)+i q\right)\left(\left(1+\xi^{2}\right)^{\frac{1}{2}}\left(\bar{\theta}_{j}+\bar{a}\right)-i q\right)\right| \\
& +\sum_{k=1}^{2 N}\left[\left(\ln \left|\left(\bar{\theta}_{j}-\bar{\theta}_{k}+i\right)\left(\bar{\theta}_{j}-\bar{\theta}_{k}-i\right)\right|+\ln \left|\left(\bar{\theta}_{j}-\bar{\theta}_{k}+2 \bar{a}+i\right)\left(\bar{\theta}_{j}-\bar{\theta}_{k}+2 \bar{a}-i\right)\right|\right],\right.
\end{aligned}
$$

where $\bar{a}=-i a$. In the thermodynamic limit, we assume that the zero roots and inhomogeneities have continuum densities
$$
\rho(\tilde{z})=\frac{1}{2 N\left(\tilde{z}_{j+1}-\tilde{z}_{j}\right)}, \quad \sigma(\bar{\theta})=\frac{1}{2 N\left(\bar{\theta}_{j+1}-\bar{\theta}_{j}\right)}.
$$

Taking the continuum limit of Eq. (4.1) and replacing $\bar{\theta}_{j}$ with $\lambda$, we obtain
$$
\begin{gathered}
2 N \int_{-\infty}^{\infty}\left[b_{1}(\lambda+\bar{a}-\tilde{z})+b_{3}(\lambda+\bar{a}-\tilde{z})\right] \rho(\tilde{z}) d \tilde{z}+b_{1}(\lambda+\bar{a}+\alpha)+b_{1}(\lambda+\bar{a}-\alpha) \\
=2 N \int_{-\infty}^{\infty}\left[b_{2}(\lambda-\bar{\theta})+b_{2}(\lambda+\bar{\theta}+2 \bar{a})\right] \sigma(\bar{\theta}) d \bar{\theta}+b_{2}(\lambda+\bar{a})-b_{1}(\lambda+\bar{a}) \\
-b_{2|p|+2}(\lambda+\bar{a})-b_{2|\bar{q}|+2}(\lambda+\bar{a}),
\end{gathered}
$$

where $b_{n}(\lambda)=\frac{1}{2 \pi} \frac{2 \lambda}{\lambda^{2}+n^{2} / 4}$. Eq.(4.2) is a convolution equation and can be solved by the Fourier transformation. The solution of $\tilde{z}$-roots density is
$$
\begin{aligned}
\tilde{\rho}(k)= & {\left[4 N \tilde{b}_{2}(k) \cos (\bar{a} k) \tilde{\sigma}(k)+\tilde{b}_{2}(k)-\tilde{b}_{1}(k)-\tilde{b}_{2|p|+2}(k)\right.} \\
& \left.-\tilde{b}_{2|\bar{q}|+2}(k)-2 \tilde{b}_{1}(k) \cos (\alpha k)\right] /\left[2 N\left(\tilde{b}_{1}(k)+\tilde{b}_{3}(k)\right)\right],
\end{aligned}
$$

where $\tilde{b}_{n}(k)=\operatorname{sign}(k) i e^{-|n k|}$. From now on, we use $\sigma(\theta)=\delta(\theta)$. In the thermodynamic limit, $\alpha$ tends to infinity. The ground state energy of the Hamiltonian (2.1) can thus be expressed as
$$
\begin{aligned}
E_{g 1}= & N\left(4 a^{2}-1\right) \int_{-\infty}^{\infty}\left[\tilde{a}_{1}(k)-\tilde{a}_{3}(k)\right] \cos (\bar{a} k) \tilde{\rho}(k) d k-c_{0} \\
& -\left(4 a^{2}-1\right)\left[\frac{|p|}{a^{2}-p^{2}}-\frac{|p|+1}{a^{2}-(|p|+1)^{2}}+\frac{|\bar{q}|}{a^{2}-\bar{q}^{2}}-\frac{|\bar{q}|+1}{a^{2}-(|\bar{q}|+1)^{2}}\right],
\end{aligned}
$$


where $\tilde{a}_{n}(k)=e^{-|n k|}$ is the Fourier transformation of $a_{n}(\lambda)$. The ground state energy of the system with periodic boundary condition can be obtained similarly. After tedious calculation, we obtain the surface energy in the regime I as

$$
E_{b 1}=e_{b}(p)+e_{b}(q)+e_{b 0},\tag{4.5}
$$

$$
e_{b}(p)=\frac{\left(4 a^{2}-1\right)}{4} \int_{-\infty}^{\infty}\left(1-e^{-|k|}\right) \cosh (a k) \frac{e^{-|p k|}}{e^{-|k| / 2} \cosh (k / 2)} d k,\tag{4.6}
$$

$$
e_{b}(q)=\frac{\left(4 a^{2}-1\right)}{4} \int_{-\infty}^{\infty}\left(1-e^{-|k|}\right) \cosh (a k) \frac{e^{-\left|\left(q / \sqrt{1+\xi^{2}}\right) k\right|}}{e^{-|k| / 2} \cosh (k / 2)} d k,\tag{4.7}
$$

$$
e_{b 0}=\frac{\left(4 a^{2}-1\right)}{4} \int_{-\infty}^{\infty}\left(1-e^{-|k|}\right) \cosh (a k) \frac{e^{-|k|}-e^{-|k| / 2}}{e^{-|k| / 2} \cosh (k / 2)} d k.\tag{4.8}
$$

From Eq.(4.5), we see that the surface energy $E_{b 1}$ can be divided into three terms. $e_{b}(p)$ and $e_{b}(q)$ are the contributions of left and right boundaries, respectively. $e_{b 0}$ exactly equals to the surface energy induced by the free boundaries.

In the regime II, taking the logarithm then the derivative of the absolute value of BAE (2.24), we have

$$
\begin{aligned}
2 N \int_{-\infty}^{\infty} & {\left[b_{1}(\lambda+\bar{a}-\tilde{z})+b_{3}(\lambda+\bar{a}-\tilde{z})\right] \rho(\tilde{z}) d \tilde{z} } \\
= & 2 N \int_{-\infty}^{\infty}\left[b_{2}(\lambda-\bar{\theta})+b_{2}(\lambda+\bar{\theta}+2 \bar{a})\right] \sigma(\bar{\theta}) d \bar{\theta}+b_{2}(\lambda+\bar{a})-b_{1}(\lambda+\bar{a}) \\
& \quad-b_{2|p|+2}(\lambda+\bar{a})-b_{2|\bar{q}|+2}(\lambda+\bar{a})-b_{2|\beta|+1}(\lambda+\bar{a})-b_{2|\beta|-1}(\lambda+\bar{a}). \quad(4.9)
\end{aligned}
$$

The Fourier transform gives

$$
\begin{aligned}
\tilde{\rho}(k)= & {\left[4 N \tilde{b}_{2}(k) \cos (\bar{a} k) \tilde{\sigma}(k)+\tilde{b}_{2}(k)-\tilde{b}_{1}(k)-\tilde{b}_{2|p|+2}(k)-\tilde{b}_{2|\bar{q}|+2}(k)\right.} \\
& \left.-\tilde{b}_{2|\beta|+1}(k)-\tilde{b}_{2|\beta|-1}(k)\right] /\left[2 N\left(\tilde{b}_{1}(k)+\tilde{b}_{3}(k)\right)\right].\tag{4.10}
\end{aligned}
$$

Then we obtain the surface energy in this regime as

$$
E_{b 2}=e_{b}(p)+e_{b}(q)+e_{b 0},\tag{4.11}
$$

where $e_{b}(p), e_{b}(q)$ and $e_{b 0}$ are given by Eqs.(4.6)-(4.8), respectively. It is clear that the forms of surface energies in the regimes I and II are the same, although the resulted values are different.


We further calculate the surface energies in the rest regimes and the result is that all the surface energies can be expressed as the form of Eq.(4.5). The reason is that the bare contributions of the boundary conjugate pairs to the ground state energy are exactly canceled by those of the back flow of continuum root density, as happened in the diagonal open boundary case.

The surface energies $E_b$ with certain $a$ versus the different values of boundary parameter $p$ are shown in Fig.4(a). If $a=0$, all the NNN, chiral three spin and DM interactions are zero and the system (2.1) degenerates into the Heisenberg spin chain with unparallel boundary fields. From the blue dotted lines in Fig.4(a), we see that the surface energy of Heisenberg spin chain is smaller than zero, and is monotonically increasing with the increasing of $|p|$. When $p=0$, the surface energy is divergent, this is because that the strength of boundary magnetic field is quantified by $1/p$. The results are similar to the those of the Heisenberg spin chain with parallel boundary fields [30,31]. While for the present model with $a\neq0$, the surface energies can be larger or smaller than zero, and have two peaks and three minimums at some special values of $|p|$. At the point of $p=0$, the surface energy arrives at its minimum. The surface energy is smaller than that of Heisenberg spin chain if $|p|$ is large, and is larger than that of Heisenberg spin chain if $|p|$ is smalle.

The surface energies $e_b(p)$ with fixed $a$ versus $p$ are shown in Fig.4(b). Comparing Figs.4(a) and (b), we find that if $|p|$ is large which means that the boundary field is small, due to the existence of NNN, chiral three spin and DM interactions, the surface energy is smaller than that of the Heisenberg spin chain. We should note that the relation between $e_b(\bar{q})$ and $\bar{q}$ is the same as that between $e_b(p)$ and $p$, where $\bar{q}=q/\sqrt{1+\xi^2}$.

The strength of boundary magnetic field along the $z$-direction is quantified by $p$ or $q$ up to a normalized scalar factor. The further numerical calculation of the analytical expression of surface energy shows that the curves of $E_b$ versus $q$ are similar with those of $E_b$ versus $p$. Thus we omit the figure of $E_b$ with the changing of $q$ here. In Fig.4(c), we show the surface energies $E_b$ with given $a$ versus the boundary parameter $\xi$. The $\xi$ quantifies the twisted angle between two unparallel boundary magnetic fields, and quantifies the strength of magnetic field on the right boundary. If $\xi$ is large, the twisted angle is large. At the same time, the right boundary magnetic field is small. From the blue dotted lines in Fig.4(c), which corresponds to the Heisenberg spin chain, we see clearly that if $\xi$ is small, the magnetic field is strong thus the induced surface energy is large, as it should be. For the present system

with $a \neq 0$, if $\xi$ is small, the contributions of NNN, chiral three spin and DM interactions are large, which leads to the surface energy becomes small. Thus the behaviors of surface energies with $a=0$ and $a \neq 0$ are totally different.

The surface energies $e_{b 0}$ versus the different values of parameter $a$ are shown in Fig.4(d). We note that the value of $e_{b 0}$ at the point of $a=0$ is the surface energy of the Heisenberg spin chain with free open boundaries.

From above explanations, we conclude that the surface energy of present system is quite different from that of the Heisenberg spin chain.

![](./images/911926818301280904_4.jpg)

Figure 4: (a) The surface energy $E_b$ versus the boundary parameter $p$, where $a=0,0.6i,0.8i$, $p=1$ and $\xi=1.2$. (b) The surface energy $e_b(p)$ versus the boundary parameter $p$. (c) The surface energy $E_b$ versus the boundary parameter $\xi$. (d) The surface energy $e_{b0}$ versus $a$.

## 5 Bulk elementary excitations

Next, we study the elementary excitations in the system. We first consider the excitations in the bulk. The bulk excitations in different regimes of boundary parameters are the same.

From the patterns of zero roots in the low-lying excited states, we find that the excitations can be characterized by breaking several conjugate pairs and putting the corresponding zero roots into the real axis, or the zero roots forming the conjugate pairs on the imaginary axis with more larger imaginary parts $\pm \frac{ni}{2}(n > 2)$. Thus the system has two kinds of bulk elementary excitations. The first one is quantified by four finite real roots $\{\pm \bar{z}_1, \pm \bar{z}_2\}$ and the second one is quantified by two conjugate pairs $\{\tilde{z}_n \pm \frac{ni}{2}, -\tilde{z}_n \pm \frac{ni}{2}\}$, where the distribution of rest zero roots almost does not change and the related difference between ground and excited states can be erased by the rearrangement of Fermi sea in the thermodynamic limit.

As an example, we give the pattern of zero roots at the ground state (blue asterisks) and that at the first kind of excited sate (red circles) in the regime V with $2N = 8$, which is shown in Fig.5(a). It is clear that there are four new real roots at the excited state. In the thermodynamic limit, the density difference $\delta \tilde{\rho}_{e_1}(k)$ between the ground state and the excited state is

$$
\delta \tilde{\rho}_{e_{1}}(k)=-\frac{\cos \left(\bar{z}_{1} k\right)+\cos \left(\bar{z}_{2} k\right)}{2 N e^{-|k| / 2} \cosh (k / 2)},\tag{5.1}
$$

where $\bar{z}_1$ and $\bar{z}_2$ can take arbitrary continuous values in the real axis. Thus the energy carried by this kind of excitation is

$$
\begin{aligned}
\delta_{e}= & \delta_{e_{1}}\left(\bar{z}_{1}\right)+\delta_{e_{1}}\left(\bar{z}_{2}\right), \\
\left.\delta_{e_{1}}(\bar{z})\right|_{\bar{z}=\bar{z}_{1}, \bar{z}_{2}}= & -\frac{1}{2}\left(4 a^{2}-1\right)\left[\int_{-\infty}^{\infty}\left(1-e^{-|k|}\right) \cosh (a k) \cos (\bar{z} k) \cosh ^{-1}(k / 2) d k\right. \\
& \left.+\left.\frac{1}{(\bar{z}-i a)^{2}+\frac{1}{4}}+\frac{1}{(\bar{z}+i a)^{2}+\frac{1}{4}}\right]\right|_{\bar{z}=\bar{z}_{1}, \bar{z}_{2}} \\
= & -\left(4 a^{2}-1\right) \cdot\left(\frac{\pi}{\cosh (\bar{z}+i a)}+\frac{\pi}{\cosh (\bar{z}-i a)}\right),\tag{5.2}
\end{aligned}
$$

which covers the previous results obtained by using the conventional Bethe ansatz method for the periodic staggered $(a \neq 0)$ spin chain [32]. The excited energies $\delta_{e_1}$ with given values of model parameter $a$ versus $\bar{z}_1$ are shown in Fig.5(b). From it, we see that the excited energy of the Heisenberg spin chain $(a = 0)$ only has one peak at the point of $\bar{z} = 0$, while for the present model $(a \neq 0)$, the excited energies have two peaks at finite $\pm \bar{z}$.

Now, we focus on the second kind of elementary excitation. In order to see the high strings $(n > 2)$ excitations more clearly, we show the pattern of zero roots at the $n = 3$ excited state in Fig.6, where the ground state is still in the regime V. In the thermodynamic

![](./images/911926818301280904_5.jpg)
![](./images/911926818301280904_6.jpg)

Figure 5: (a) The distribution of zero roots for $\{\bar{\theta}_{j}=0|j=1,\cdots,2N\}$ at the ground state (blue asterisks) and at the first kind of excited state (red circles) with $2N=8$, $a=0.66i$, $p=1.2$, $\bar{q}=0.7$ and $\xi=1.2$. (b) The excited energies $\delta_{e_1}$ with fixed $a$ versus $\bar{z}_1$ in the thermodynamic limit.

limit, the density difference $\delta\tilde{\rho}_{e_n}(k)$ between the ground state and the excited state is
$$
\delta \tilde{\rho}_{e_{n}}(k)=-\frac{\left(e^{-|(n+1) k| / 2}+e^{-|(n-1) k| / 2}\right) \cos \left(\tilde{z}_{n} k\right)}{2 N e^{-|k| / 2} \cosh (k / 2)},\tag{5.3}
$$
where $\tilde{z}_n$ is free. The related elementary excitation energy is
$$
\begin{aligned}
\delta_{e_{n}}= & -\frac{\left(4 a^{2}-1\right)}{2}[\int_{-\infty}^{\infty}\left(1-e^{-|k|}\right) \cosh (a k) \frac{\left(e^{-|(n+1) k| / 2}+e^{-|(n-1) k| / 2}\right) \cos \left(\tilde{z}_{n} k\right)}{e^{-|k| / 2} \cosh (k / 2)} d k \\
& \left.+2 \pi\left(a_{n+1}\left(\tilde{z}_{n}+i a\right)+a_{n+1}\left(\tilde{z}_{n}-i a\right)-a_{n-1}\left(\tilde{z}_{n}+i a\right)-a_{n-1}\left(\tilde{z}_{n}-i a\right)\right)\right] \\
= & 0,
\end{aligned}\tag{5.4}
$$
which indicates that the bare contributions of the conjugate pairs with $n>2$ to the energy is exactly canceled by that of the back flow of the continuum root density. Thus the conjugate pairs with $n>2$ contribute nothing to the energy. However, the conjugate pairs do affect the scattering matrix among the real roots [33].

## 6 Boundary elementary excitations

Next, we consider the boundary excitations. Comparing with the zero roots distributions at the ground state, we find that the boundary excitations can exist in the regimes I-IV, where the boundary parameter $-\frac{1}{2}<p<\frac{1}{2}$ or $-\frac{1}{2}<\bar{q}<\frac{1}{2}$. The typical boundary excitation is

![](./images/911926818301280904_7.jpg)

Figure 6: The distribution of $\bar{z}$-roots for $\{\bar{\theta}_{j}=0|j=1,\cdots,2N\}$ at the second kind of excited state with $n=3$. Here $2N=8$, $a=0.66i$, $p=1.2$, $\bar{q}=0.7$ and $\xi=1.2$.

![](./images/911926818301280904_8.jpg)

Figure 7: (a) The distribution of $\bar{z}$-roots for $\{\bar{\theta}_{j}=0|j=1,\cdots,2N\}$ with $2N=8$, $a=0.66i$, $p=0.1$, $\bar{q}=1.2$ and $\xi=1.2$. Here the blue asterisks represent the pattern of zero roots at the ground state and the red circles denote those at the excited state with boundary string $i(\frac{1}{2}-|p|)$. (b) The boundary excited energy versus the boundary parameter $p$.

putting the boundary string from $i(|p|+\frac{1}{2})$ to $i(\frac{1}{2}-|p|)$, or from $i(|\bar{q}|+\frac{1}{2})$ to $i(\frac{1}{2}-|\bar{q}|)$. These two new boundary strings indeed are the solutions of BAEs (2.24) and would appear at the low-lying excited states.

As an example, we show the pattern of zero roots at the ground state (blue asterisks) and that at the excited state (red circles) with boundary string $i(\frac{1}{2}-|p|)$ in the regime III with $2N=8$, which is shown in Fig.7(a). We can find in the excitation, the 4 roots at $\pm\alpha$ and $\pm\beta$ of the ground state jump into the bulk string parts at $\pm i$ axes. The change of the zero roots $\pm\alpha$ and $\pm i\beta$ contribute nothing to the energy. Therefore, we omit the zero roots $\pm\alpha$ and $\pm i\beta$ in the following. The resulted density change $\delta\tilde{\rho}(k)$ between ground and excited states reads

$$
\delta \tilde{\rho}_{p}(k)=-\frac{e^{|p k|}-e^{-|p k|}}{4 N \cosh (k / 2)}.\tag{6.1}
$$

The corresponding excited energy is

$$
\begin{aligned}
\delta_{e_{p}}= & -\frac{\left(4 a^{2}-1\right)}{2}\left[\int_{-\infty}^{\infty}\left(1-e^{-|k|}\right) \cosh (a k) \frac{\cosh (|p| k)}{e^{|k| / 2} \cosh (k / 2)} d k\right. \\
& \left.+\frac{4|p|}{p^{2}-a^{2}}-\frac{2(|p|+a)}{(|p|+a)^{2}-1}-\frac{2(|p|-a)}{(|p|-a)^{2}-1}\right] \\
= & -\pi\left(4 a^{2}-1\right) \cdot\left(\csc (\pi(|p|+a))+\csc (\pi(|p|-a))\right).
\end{aligned}\tag{6.2}
$$

The excited energies $\delta_{e_{p}}$ with fixed values of $a$ versus $p$ are shown in Fig.7(b). From it, we see that the excited energy of present model is increasing with the increasing of boundary parameter $|p|$ and has a minimum at the point of $p=0$, which is very different from that of the Heisenberg spin chain. For the latter, the excited energy is decreasing with the increase of $|p|$.

We have computed the boundary excitations in other regimes and found that the excited energies has an unified form (6.2), although the resulted values are different. Please note that when considering the boundary excitations in the regime of $-\frac{1}{2}<\bar{q}<\frac{1}{2}$, the $p$ in Eq.(6.2) should be replaced by the $\bar{q}$.

## 7 Surface energy in ferromagnetic regime

Furthermore, we study the surface energy in ferromagnetic regime. The corresponding Hamiltonian $H^{ferr}$ is the negative of Hamiltonian (2.1), namely

$$
H^{f e r r}=-H=-\left(H_{b u l k}+H_{L}+H_{R}\right),\tag{7.1}
$$

In region III $(p \geq \frac{1}{2}, 0 \leq \bar{q} < \frac{1}{2}$ or $0 \leq p < \frac{1}{2}, \bar{q} \geq \frac{1}{2})$, all the zeros $\{\bar{z}_j|j = 1, \cdots, N\}$ are real as shown in Fig.8(a). Taking the logarithm then the derivative of the absolute value of BAE (2.24), we have

$$
\begin{aligned}
2 N \int_{-\infty}^{\infty} & b_{1}(u+\bar{a}-\tilde{z}) \rho^{f e r r}(\tilde{z}) d \tilde{z}-b_{2|p|}(u+\bar{a})-b_{2|\bar{q}|}(u+\bar{a}) \\
& =2 N \int_{-\infty}^{\infty}\left[b_{2}(u-\bar{\theta})+b_{2}(u+\bar{\theta}+2 \bar{a})\right] \sigma(\bar{\theta}) d \bar{\theta}+b_{2}(u+\bar{a})-b_{1}(u+\bar{a}). \quad(7.2)
\end{aligned}
$$

The Fourier transform gives

![](./images/911926818301280904_9.jpg)

Figure 8: (a) Patterns of $\bar{z}$-roots for $\{\bar{\theta}_{j}=0 \mid j=1, \cdots, 2 N\}$ at the ground state of the ferromagnetic case in regimes III with $2 N=8$. (b) The surface energy $E_{b}^{f e r r}$ versus the boundary parameter $p$ in ferromagnetic case, where $a=0,0.6 i, 0.8 i, p=1$ and $\xi=1.2$.

$$
\begin{aligned}
\tilde{\rho}^{f e r r}(k) & =\left[4 N \tilde{b}_{2}(k) \cos (\bar{a} k) \tilde{\sigma}(k)+\tilde{b}_{2}(k)-\tilde{b}_{1}(k)+\tilde{b}_{2|p|}(k)+\tilde{b}_{2|\bar{q}|}(k)\right] /\left[2 N \tilde{b}_{1}(k)\right] \\
& =2 \tilde{a}_{1}(k) \cos (\bar{a} k) \tilde{\sigma}(k)+\frac{1}{2 N}\left[\tilde{a}_{1}(k)-1+\tilde{a}_{2|p|-1}(k)+\tilde{a}_{2|\bar{q}|-1}(k)\right].
\end{aligned}
$$

The ground state energy of the Hamiltonian (7.1) can thus be expressed as

$$
\begin{aligned}
E_{g}^{f e r r} & =N\left(4 a^{2}-1\right) \int_{-\infty}^{\infty} \tilde{a}_{1}(k) \cos (\bar{a} k) \tilde{\rho}(k) d k+c_{0} \\
& =(2 N+1)\left(2 a^{2}-1\right)-\frac{2 a^{4}-6 a^{2}+1}{a^{2}-1}+E_{b}^{f e r r},
\end{aligned}
$$

where the surface energy $E_{b}^{f e r r}$ in this regime as

$$
\begin{aligned}
E_{b}^{f e r r} & =\frac{\left(4 a^{2}-1\right)}{2} \int_{-\infty}^{\infty}\left[\tilde{a}_{2}(k)-\tilde{a}_{1}(k)+\tilde{a}_{2|p|}(k)+\tilde{a}_{2|\bar{q}|}(k)\right] \cos (\bar{a} k) d k \\
& =\frac{\left(4 a^{2}-1\right)}{2}\left[\frac{2|p|}{p^{2}-a^{2}}+\frac{2|\bar{q}|}{\bar{q}^{2}-a^{2}}+\frac{2}{1-a^{2}}-\frac{1}{\frac{1}{4}-a^{2}}\right].
\end{aligned}
$$


After calculation, the energy expressions in the other regions are found to be identical to Eq. (7.5) in region III. The surface energies $E_b^{ferr}$ with certain $a$ versus the different values of boundary parameter $p$ are shown in Fig. 8(b).

## 8 Conclusions

In this paper, we have studied the exact physical quantities of a competing spin chain including the NN, NNN, chiral three-spin couplings, DM interactions and unparallel boundary magnetic fields in the thermodynamic limit. We obtained the density of zero roots, surface energy and elementary excitations in different regimes of model parameter. Due to the competition of various interactions, the excited spectrum have different behaviors from those of the isotropic Heisenberg spin chain.

## Acknowledgments

We would like to thank Prof. Y. Wang for his valuable discussions and continuous encouragement. The financial supports from National Key R&D Program of China (Grant No.2021YFA1402104), the National Natural Science Foundation of China (Grant Nos. 12247103, 12074410, 12047502, 12147160, 11934015 and 11975183), Major Basic Research Program of Natural Science of Shaanxi Province (Grant Nos. 2021JCW-19 and 2017ZDJC-32), Australian Research Council (Grant No. DP 190101529), Strategic Priority Research Program of the Chinese Academy of Sciences (Grant No. XDB33000000), and the fellowship of China Postdoctoral Science Foundation (2020M680724) are gratefully acknowledged.

## Appendix: A simple method

In the review process, one anonymous referee recommends a clear and simple method to derive the surface energy and the bulk excitations. Here, we list the referee's method. Under the simplifications that take place in the thermodynamic limit (dense distribution of zeros) one can apply techniques introduced in [34] for the excitations and in [35,36] for the bulk properties. In the thermodynamic limit the functional relations (2.22) means

$$
\Lambda(u) \Lambda(u-1)=a(u) d(u-1)=a(u) a(-u), \tag{A.1}
$$

for all $u$ out of the physical strip. Of course this means literally for the bulk and surface terms

$$
\Lambda(u)=\Lambda_{b u l k}(u) \cdot \Lambda_{s u r}(u), \tag{A.2}
$$

$$
a(u)=a_{b u l k}(u) \cdot a_{s u r}(u), \quad a_{s u r}(u):=\frac{u+1}{u+\frac{1}{2}}(u+p)(u+\bar{q}), \tag{A.3}
$$

that for instance

$$
\Lambda_{s u r}(u) \Lambda_{s u r}(u-1)=a_{s u r}(u) a_{s u r}(-u). \tag{A.4}
$$

Now introducing

$$
\tilde{\Lambda}(u):=\Lambda_{s u r}(-i u) \tag{A.5}
$$

allows for the ansatz of a Fourier transform

$$
\frac{d}{d u} \log \tilde{\Lambda}(u)=\int_{-\infty}^{\infty} d k L(k) e^{i k u} \tag{A.6}
$$

with a yet unknown function $L(k)$. This function can be calculated from (A.4) by taking the logarithm, the derivative and then the Fourier transform (the RHS gives an explicit function):

$$
L(k) \cdot\left(1+e^{k}\right)=-i \cdot \operatorname{sign}(k) \cdot\left(e^{-|p k|}+e^{-|\bar{q} k|}+e^{-|k|}-e^{-|k| / 2}\right). \tag{A.7}
$$

From the last equation one gets $L(k)$ and from this $\frac{d}{d u} \log \tilde{\Lambda}(u)$ Fourier transform. The energy is simply obtained by

$$
E_{s u r}=-\frac{1}{2}\left(4 a^{2}-1\right)\left(\left.i \frac{d}{d u} \log \tilde{\Lambda}(u)\right|_{u=i a}+\left.i \frac{d}{d u} \log \tilde{\Lambda}(u)\right|_{u=-i a}\right), \tag{A.8}
$$

which straight away gives (4.5) of the paper.

Next, the referee derives the bulk excitations. He starts with a remark: The result (5.2) can be presented in a simplified, explicit form, by doing the Fourier integral resulting in:

$$
\delta_{e_{1}}(\bar{z})=-\left(4 a^{2}-1\right) \cdot\left(\frac{\pi}{\cosh (\bar{z}+i a)}+\frac{\pi}{\cosh (\bar{z}-i a)}\right). \tag{A.9}
$$

How to derive this in a most transparent manner? Define for an arbitrary excited state, actually for an eigenvalue $\Lambda_{x}(u)$ the ratio to the leading eigenvalue $\Lambda(u)$ of the transfer matrix

$$
l(u):=\frac{\Lambda_{x}(u)}{\Lambda(u)}. \tag{A.10}
$$

In the thermodynamic limit this function satisfies the functional equation (derived from two times (A.1) for $\Lambda(u)$ and for $\Lambda_x(u)$)

$$
l(u) l(u-1)=1. \tag{A.11}
$$

This is solved uniquely for a given set of zeros $z_m$ in the physical strip by tanh resp. tan function (for any distribution of inhomogeneity parameters $\theta_j$). Let us assume there are only two such zeros $z_1$ and $z_2$ , then

$$
l(u)=\tan \left(\frac{\pi}{2}(u-z_1)+\frac{1}{2}\right)\left(\frac{\pi}{2}(u-z_2)+\frac{1}{2}\right). \tag{A.12}
$$

The shift $+\frac{1}{2}$ is due to the convention (2.23). The logarithmic derivative and then inserting $u=\pm a$ and $z_m=i\bar{z}_m$ gives directly (5.2).

However, the method requires that there do not exist the zeros between the lines $\operatorname{Re}(z)=$ 0 and $\operatorname{Re}(z)=-1$ at the ground state. For example, we can know that zeros of the ground state in ferromagnetic regime are mainly located in line $\operatorname{Re}(z)=-\frac{1}{2}{ }^{4}$ from Section 7 . This will lead to an error in the Fourier transform (A.7).

# References

[1] R. J. Baxter, *Exactly Solved Models in Statistical Mechanics*, Academic Press, London, (1982), doi:10.1142/9789814415255_0002.

[2] J. Maldacena, The Large-$N$ limit of superconformal field theories and supergravity, *Int. J. Theor. Phys.* **38**, 1113 (1999), doi:10.1023/A:1026654312961.

[3] N. Beisert, C. Ahn, L. F. Alday, Z. Bajnok, J. M. Drummond, et al., Review of AdS/CFT Integrability: An Overview, *Lett. Math. Phys.* **99**, 1 (2012), doi:10.1007/s11005-011-0529-2.

[4] L. Onsager, Crystal Statistics. I. A Two-Dimensional Model with an Order-Disorder Transition, *Phys. Rev.* **65**, 117 (1944), doi:10.1103/PhysRev.65.117.

[5] E. H. Lieb and F. Y. Wu, Absence of Mott Transition in an Exact Solution of the Short-Range, One-Band Model in One Dimension, *Phys. Rev. Lett.* **20**, 1445 (1968), doi:10.1103/PhysRevLett.20.1445.

\footnotetext{${ }^{4}$Due to the convention (2.23), the zeros shift $+\frac{1}{2}$ and locate in real axis in Fig. 8(a).}

[6] L. D. Faddeev and L. A. Takhtajan, What is the spin of a spin wave? *Phys. Lett. A* **85**, 375 (1981), doi:10.1016/0375-9601(81)90335-2.

[7] M. Vanicat, Integrable Floquet dynamics, generalized exclusion processes and “fuse” matrix ansatz, *Nucl. Phys. B* **929**, 298 (2018), doi:10.1016/j.nuclphysb.2018.02.007.

[8] R. Frassek, C. Giardina and J. Kurchan, Duality and hidden equilibrium in transport models, *SciPost Phys.* **9**, 054 (2020), doi:10.21468/SciPostPhys.9.4.054.

[9] Z. Chen, J. de Gier and M. Wheeler, Integrable Stochastic Dualities and the Deformed Knizhnik–Zamolodchikov Equation, *Int. Math. Res. Not.* **19**, 5872 (2020), doi:10.1093/imrn/rny159.

[10] U. Godreau and S. Prolhac, Spectral gaps of open TASEP in the maximal current phase, *J. Phys. A* **53**, 385006 (2020), doi:10.1088/1751-8121/aba575.

[11] N. Andrei et al., Boundary and defect CFT: open problems and applications, *J. Phys. A* **53**, 453002 (2020), doi:10.1088/1751-8121/abb0fe.

[12] A. Bastianello, L. Piroli and P. Calabrese, Exact Local Correlations and Full Counting Statistics for Arbitrary States of the One-Dimensional Interacting Bose Gas, *Phys. Rev. Lett.* **120**, 190601 (2018), doi:10.1103/PhysRevLett.120.190601.

[13] M. Mestyán, B. Bertini, L. Piroli, et al., Spin-charge separation effects in the low-temperature transport of one-dimensional Fermi gases, *Phys. Rev. B* **99**, 014305 (2019), doi:10.1103/PhysRevB.99.014305.

[14] A. Fontanella and A. Torrielli, Massless AdS₂ scattering and Bethe ansatz, *JHEP* **09**, 75 (2017), doi:10.1007/JHEP09(2017)075.

[15] Y. Jiang, S. Komatsu and E. Vescovi, Structure constants in $\mathcal{N}=4$ SYM at finite coupling as worldsheet $g$-function, *JHEP* **07**, 37 (2020) ,doi:10.1007/JHEP07(2020)037.

[16] M. De Leeuw, C. Paletta, A. Pribytok, et al., 2020 global reassessment of the neutrino oscillation picture, *JHEP* **02**, 71 (2021), doi:10.1007/JHEP02(2021)071.

[17] C. N. Yang and C. P. Yang, Thermodynamics of a One-Dimensional System of Bosons with Repulsive Delta-Function Interaction, *J. Math. Phys* **10**, 1115 (1969), doi:10.1063/1.1664947.

[18] C. N. Yang, One-Dimensional System of Bosons with Repulsive $\delta$-Function Interactions at a Finite Temperature $T$ , *Phys. Rev. A* **2**, 154 (1970), doi:10.1103/PhysRevA.2.154.

[19] Y. Wang, W. -L. Yang, J. Cao and K. Shi, *Off-Diagonal Bethe Ansatz for Exactly Solvable Models*, Springer Press, (2015), doi:10.1007/978-3-662-46756-5.

[20] J. Cao, W.-L. Yang, K. Shi and Y. Wang, Off-Diagonal Bethe Ansatz and Exact Solution of a Topological Spin Ring, *Phys. Rev. Lett.* **111**, 137201 (2013), doi:10.1103/PhysRevLett.111.137201.

[21] R. I. Nepomechie, An inhomogeneous $T-Q$ equation for the open XXX chain with general boundary terms: completeness and arbitrary spin, *J. Phys. A* **46**, 442002 (2013), doi:10.1088/1751-8113/46/44/442002.

[22] Y. Qiao, P. Sun, J. Cao, W.-L. Yang, K. Shi and Y. Wang, Exact ground state and elementary excitations of a topological spin chain, *Phys. Rev. B* **102**, 085115 (2020), doi:10.1103/PhysRevB.102.085115.

[23] Y. Qiao, J. Cao, W.-L. Yang, K. Shi and Y. Wang, Exact surface energy and helical spinons in the XXZ spin chain with arbitrary nondiagonal boundary fields, *Phys. Rev. B* **103**, L220401 (2021), doi:10.1103/PhysRevB.103.L220401.

[24] W. Heisenberg, Mehrkörperproblem und Resonanz in der Quantenmechanik, *Z. Phys.* **49**, 619 (1928), doi:10.1007/BF01397160.

[25] C. K. Majumdar and D. K. Ghosh, On Next-Nearest-Neighbor Interaction in Linear Chain. I, *J. Math. Phys.* **10**, 1388 (1969), doi:10.1063/1.1664978.

[26] I. E. Dzyaloshinsky, A thermodynamic theory of "weak" ferromagnetism of antiferromagnetics, *J. Phys. Chem. Solids* **4**, 241 (1958), doi:10.1016/0022-3697(58)90076-3.

[27] T. Moriya, New Mechanism of Anisotropic Superexchange Interaction, *Phys. Rev. Lett.* **4**, 228 (1960), doi:10.1103/PhysRevLett.4.228.

[28] H. Frahm and C. Rödenbeck, Properties of the chiral spin liquid state in generalized spin ladders, *J. Phys. A: Math. Gen.* **30**, 4467 (1997), doi:10.1088/0305-4470/30/13/005.

[29] J. Wang, Y. Qiao, J. Cao and W.-L. Yang, Exact solution of an integrable quantum spin chain with competing interactions, *Chin. Phys. B* **30**, 117501 (2021), doi:10.1088/1674-1056/abfa0a.

[30] M. T. Grisaru, L. Mezincescu and R. I. Nepomechie, Direct calculation of the bound- ary $S$-matrix for the open Heisenberg chain, *J. Phys. A: Math. Gen.* **28** 1027 (1995), doi:10.1088/0305-4470/28/4/025.

[31] A. Kapustin and S. Skorik, Surface excitations and surface energy of the antiferromag- netic $XXZ$ chain by the Bethe ansatz approach, *J. Phys. A: Math. Gen.* **29** 1629 (1996), doi:10.1088/0305-4470/29/8/011.

[32] H. Frahm and C. Rödenbeck, Integrable models of coupled Heisenberg chains, *Europhys. Lett.* **33** 47-52 (1996), doi:10.1209/epl/i1996-00302-7.

[33] N. Andrei, K. Furuya and J. H. Lowenstein, Solution of the Kondo problem, *Rev. Mod. Phys.* **55**, 331 (1983), doi:10.1103/RevModPhys.55.331.

[34] A. Klümper, New results for $q$-state vertex models and the pure biquadratic spin-1 Hamiltonian, *Europhys. Lett.* **9**, 815-820 (1989), doi:10.1209/0295-5075/9/8/013.

[35] F. H. Essler, H. Frahm, F. Göhmann, A. Klümper and V. E. Kore- pin, *The one-dimensional Hubbard model*, Cambridge University Press (2005), doi:10.1017/cbo9780511534843.

[36] G. A. P. Ribeiro, A. Klümper and P. A. Pearce, On the partition function of the $Sp(2n)$ integrable vertex model, *J. Stat. Mech.* **11**, 113102 (2022), doi:10.1088/1742-5468/acc730.
