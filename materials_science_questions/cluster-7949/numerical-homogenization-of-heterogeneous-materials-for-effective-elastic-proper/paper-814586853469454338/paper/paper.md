Accepted Manuscript

Evaluation for elastic properties of metal matrix composites with randomly distributed fibers: Two-step mean-field homogenization procedure versus FE homogenization method

Wenlong Tian, Lehua Qi, Junhao Liang, Xujiang Chao, Jiming Zhou

![](./images/814586853469454338_1.jpg)

PII:
S0925-8388(15)31446-8

DOI:
10.1016/j.jallcom.2015.10.190

Reference:
JALCOM 35745

To appear in: Journal of Alloys and Compounds

Received Date: 20 July 2015

Revised Date: 16 October 2015

Accepted Date: 20 October 2015

Please cite this article as: W. Tian, L. Qi, J. Liang, X. Chao, J. Zhou, Evaluation for elastic properties of metal matrix composites with randomly distributed fibers: Two-step mean-field homogenization procedure versus FE homogenization method, *Journal of Alloys and Compounds* (2015), doi: 10.1016/j.jallcom.2015.10.190.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

![](./images/814586853469454338_2.jpg)

# Evaluation for elastic properties of metal matrix composites with randomly distributed fibers: Two-step mean-field homogenization procedure versus FE homogenization method

Wenlong Tian$^\text{a}$, Lehua Qi$^\text{a,*}$, Junhao Liang$^\text{b}$, Xujiang Chao$^\text{a}$, Jiming Zhou$^\text{a}$

$^\text{a}$School of Mechanical Engineering, Northwestern Polytechnical University, Xi'an 710072, P.R.China

$^\text{b}$School of Materials Science and Engineering, Northwestern Polytechnical University, Xi'an 710072, P.R.China

*Corresponding author: Tel.: +86-29-88460447, Fax: +86-29-88491982, Email address: qilehua@nwpu.edu.cn (Lehua Qi)

## Abstract
The modified two-step mean-field homogenization procedure including the quadratic interpolative model on the basis of the Mori-Tanaka (M-T) and interpolative double inclusion (D-I) mean-field homogenization models in the first-step homogenization procedure and the simple interpolative model in the second-step homogenization procedure on the basis of the Voigt and Reuss mean-field homogenization models, and the direct finite element (FE) homogenization method based on the concept of the representative volume element (RVE) and the periodic boundary conditions (the RVE based FE homogenization method), are implemented to predict the effective elastic properties of metal matrix composites with the randomly distributed fibers. Compared with the results measured from the uniaxial tensile experiments, the modified two-step mean-field homogenization procedure and the RVE based FE homogenization method provide the accurate predictions on

the effective elastic properties of metal matrix composites with the randomly distributed fibers. However, in the case of neglecting the detailed stress and strain fields in the metal matrix composites with the randomly distributed fibers, the modified two-step mean-field homogenization procedure gives the far better computational efficiency than the RVE based FE homogenization method.

Keywords: A. Metal matrix composites; C. Elasticity; D. Computer simulations; Finite element analysis (FEA); Two-step homogenization

### 1. Introduction
There is no surprise to claim an essential requirement of the accurate mechanical properties characterization for metal matrix composites (MMCs), which are the leading candidates for the applications in the various industries [1-3] due to their sound lightweight, high specific stiffness and strength [4-6]. Traditionally, the experimental measurement is the most commonly used method to characterize the effective mechanical properties of composites. Due to the time-consuming and costly experimental test, however, the analytical and/or numerical predictions for the mechanical properties of composites are at least considered to be an alternative.

The analytical and/or numerical methods for predicting the mechanical properties of composites can generally be classified into four categories [7-10]: (1). Direct finite element (FE) simulations of a unit cell (assuming periodic microstructures) or a representative volume element (RVE); (2). Transformation field analysis or sub-cell method (where a unit cell or a RVE is subdivided into a number of 2D pixels or 3D voxels); (3). Homogenization based on asymptotic expansion of the displacement field (it assumes a periodic microstructure and ends up with a unit

cell problem to be solved by FE); (4). Mean-field homogenization based on the assumed relations between the average micro-strain and stress fields in each phase. In this paper, the emphasis is on the direct FE simulation based on the RVE and the mean-field homogenization to investigate the effective elastic properties of metal matrix composites with the randomly distributed fibers.

Since the mechanical properties of composites are largely dependent on their microstructures, the methods which can accurately characterize micro-structures of composites have gained the significant success on the prediction of the mechanical properties of composites. So the direct FE computation of the boundary-value problem at each RVE [11, 12] have been well documented for predicting the effective mechanical properties of composites. Lee et al. [13] investigated the Young's modulus and overall elasto-plastic responses during the deformation of random $Al_{18}B_4O_{33}$ whisker-reinforced magnesium matrix composites by using the random sequential adsorption (RSA) algorithm [14, 15] and the three-dimensional FE method. The Young's modulus and stress-strain behavior of the composite predicted by the FE model corresponded well with the experimental results. However, the direct FE approach becomes extremely expensive in the case of the complex micro-structures (e.g., RVEs containing a large number of fibers with the different orientation), and encounters a geometric restriction when applied to the cases with the high fiber volume fractions and high fiber aspect ratios.

To obtain the accurate prediction of the mechanical properties of composites with the reasonable computational cost, the mean-field homogenization approaches are developed and have obtained the satisfying results. The Mori-Tanaka (M-T)

model [16,17] and the interpolative double inclusion (D-I) model proposed by Lielens et al. [18] provide perhaps the best mean-field prediction to date, for the two-phase isothermal composites in which all the inclusions (or reinforcements) have the same material properties, shapes, aspect ratios and orientations within a wide range of the inclusion volume fractions. However, in some cases even if both the matrix and the inclusions are isotropic, composites can usually be anisotropic because of the non-random orientation and distribution of the inclusion such that the aforementioned mean-field homogenization (such as M-T and D-I) models are not suitable anymore and required to be extended or modified for these types of composites. One commonly used method in the literatures consists in a direct homogenization based on the extension of the M-T model [19], which however should be avoided as it might lead to the non-symmetric overall stiffness tensor that is physically unacceptable. The solution was advocated by Pierard et al. [20] and Doghri et al. [10] and consisted in a two-step homogenization procedure. Note that the mean-field homogenization methods can provide the good computational efficiency but not give the detailed strain/stress field in the composites compared with the direct FE approach.

The aim of present study is to evaluate the effective elastic properties of metal matrix composites with the randomly distributed fibers using the two-step mean-field homogenization procedure including the modified quadratic interpolative model on the basis of M-T and D-I mean-field models in the first-step homogenization procedure and the simple interpolative model in the second-step homogenization procedure on the basis of Vogit and Reuss mean-field models [21-

24], and the direct FE homogenization method based on the RVE. The accuracy of the modified two-step mean-field homogenization procedure and the RVE based FE homogenization method is validated by comparing the effective elastic properties measured from the uniaxial tensile experiments of metal matrix composites with the randomly distributed fibers. Meanwhile, the computational efficiency of the modified two-step mean-field homogenization procedure and the RVE based FE homogenization method is compared.

## 2. Finite element simulations

In the recent decades, the finite element analysis is widely adopted to model the mechanical responses of composites based on the concept of RVE. Here, we introduce the RSA technique [14, 15] to generate the RVEs of metal matrix composites with the randomly distributed fibers, which are cubic prisms with the dimensions $L^3$ (as shown in Figure. 1). In the RVEs, the non-overlapping identical cylindrical fibers are randomly distributed and the matrix/fiber length aspect ratio $L/l$ is selected as 2 [25, 26].

Previous investigations have demonstrated that the better approximations for the effective mechanical properties of composites are obtained when the periodic boundary conditions instead of the uniform forces or linear displacements boundary conditions are applied to the RVEs [27, 28], and therefore the periodic RVEs will be required. To generate the periodic RVEs, the fibers penetrating the surfaces of a RVE are slit into the appropriate number of parts which then would be

copied and translated to the opposite surfaces of the RVE [15]. The formulation is given as,

$$
P_{N}\left(x^{i}\right)=P\left(x^{i}\right)-k^{i} L \quad i=1,2 \text { or } 3 \tag{1}
$$

where $P_{N}\left(x^{i}\right)$ are the translated fiber parts, $x^{i}$ are the translated coordinates in the corresponding dimension, $k^{i} \in\{-1,0$ or 1$\}$ is the coefficient depending on the penetrated surface of the RVE. Note that up to three surfaces of a RVE can be penetrated by one single fiber. In order to avoid the finite elements becoming distorted during the simulation, a minimum separation distance (e.g. 5% of the fiber radius) between the surfaces of any two fibers and between the surfaces of any fiber and the cubic matrix is necessary in the generating procedure of RVE [29].

If three concurrent edges of the cubic RVE stand for the axes $x^{1}, x^{2}$ and $x^{3}$ of Cartesian coordinates system $o x^{1} x^{2} x^{3}$, then the applied periodic boundary conditions can be expressed as,

$$
\boldsymbol{u}\left(L, x^{2}, x^{3}\right)-\boldsymbol{u}\left(0, x^{2}, x^{3}\right)=\boldsymbol{u}_{1} \tag{2a}
$$

$$
\boldsymbol{u}\left(x^{1}, L, x^{3}\right)-\boldsymbol{u}\left(x^{1}, 0, x^{3}\right)=\boldsymbol{u}_{2} \tag{2b}
$$

$$
\boldsymbol{u}\left(x^{1}, x^{2}, L\right)-\boldsymbol{u}\left(x^{1}, x^{2}, 0\right)=\boldsymbol{u}_{3} \tag{2c}
$$

where the displacement vectors $\boldsymbol{u}_{1}, \boldsymbol{u}_{2}$ and $\boldsymbol{u}_{3}$ depend on the specified applied loading along the directions of the axis $x^{1}, x^{2}$ and $x^{3}$.

The finite element simulations are implemented in Abaqus/Standard within the framework of the infinitesimal deformation theory. The resulted effective stress $\overline{\boldsymbol{\sigma}}$ and strain $\overline{\boldsymbol{\varepsilon}}$ can be written as,

$$
\begin{aligned}
\left\langle\sigma_{i j}\right\rangle= & \frac{1}{V_{R V E}} \sum_{e} V_{e}\left(\sum_{I=1}^{n_{e_{\text {int }}}} \sigma_{i j}\left(y_{I}\right) \cdot J_{j i}\left(y_{I}\right) \cdot W\left(y_{I}\right)\right)=\frac{1}{V_{R V E}} \sum_{I=1}^{n_{\text {int }}} \sigma_{i j}\left(y_{I}\right) \cdot I V O L\left(y_{I}\right) \\
& i, j=1,2,3 \text { and } y_{I} \in V
\end{aligned} \quad(3 \mathrm{a})
$$

$$
\begin{aligned}
\left\langle\varepsilon_{i j}\right\rangle= & \frac{1}{V_{R V E}} \sum_{e} V_{e}\left(\sum_{I=1}^{n_{e_{\text {int }}}} \varepsilon_{i j}\left(y_{I}\right) \cdot J_{j i}\left(y_{I}\right) \cdot W\left(y_{I}\right)\right)=\frac{1}{V_{R V E}} \sum_{I=1}^{n_{\text {int }}} \varepsilon_{i j}\left(y_{I}\right) \cdot \operatorname{IVOL}\left(y_{I}\right) \\
& i, j=1,2,3 \text { and } y_{I} \in V
\end{aligned} \quad(3 \mathrm{~b})
$$

where $n_{e_{\text {int }}}$ and $n_{\text {int }}$ are the numbers of the integration point in the element $e$ and in the whole RVE, respectively. $J(y_{I})$ and $W(y_{I})$ are the Jacobian matrix and the integration weight, respectively, at an integration point positioned at $y_{I}$ in the element $e$, whose volume is $V_{e}$. Note that here the Jacobian matrix $J(y_{I})$ is the unit matrix here. $IVOL(y_{I})$ is the integration point volume at an integration point positioned at $y_{I}$, which can be expressed by $IVOL(y_{I})=V_{e} \cdot W(y_{I})$ in Abaqus/Standard. Since the symmetry conditions of linear elasticity are fulfilled, the effective elastic stiffness tensor are calculated (in the indicial notation) by

$$
\langle C\rangle_{i j k m}=\frac{\langle\sigma\rangle_{i j}}{\langle\varepsilon\rangle_{k m}}. \tag{4}
$$

### 3. Modified two-step mean-field homogenization procedure

The main objective of mean-field homogenization is to relate the volume averages of stress and strain over a RVE. Consider a RVE $\omega$ of the composites containing the matrix (volume fraction $v_m$) and a large number of fibers (volume fraction $v_f = 1 - v_m$), both of which are assumed to be homogeneous with the isotropic linear elastic properties, respectively. For fibers, each one is characterized by its own unit orientation vector $\boldsymbol{p}$, aspect ratio $l/d$ and material properties. As shown in Figure.2, with respect to the fixed Cartesian coordinate system $ox^1x^2x^3$, $\boldsymbol{p}$ is defined by two Euler orientation angles: $\theta \in [0, \pi]$ between $\boldsymbol{p}$ and the axis $x^1$ and $\varphi \in [0, 2\pi]$ between the projection of $\boldsymbol{p}$ on the plane $ox^2x^3$ and the axis $x^3$,

$$
\boldsymbol{p} = [\cos\theta, \sin\theta\sin\varphi, \sin\theta\cos\varphi]^T. \tag{5}
$$

The fibers can be categorized into $N$ phases $(i)$ of the volume fraction $v_i$:

$$
v_m + \sum_{i=1}^{N} v_i = 1. \tag{6}
$$

For each phase $(i)$, the fibers have the identical aspect ratio $(l/d)_i$, material properties but not necessarily the same orientation $\boldsymbol{p}$, which is represented by the differentiable orientation distribution function (ODF) $\psi_i(\boldsymbol{p})$ defined such that the probability of any fiber belonging to phase $(i)$ and whose orientation is between $\boldsymbol{p}$ and $\boldsymbol{p} + d\boldsymbol{p}$ is $\psi(\boldsymbol{p})d\boldsymbol{p}$. The differentiable ODF $\psi_i(\boldsymbol{p})$ owns the following characters:

$$
\psi_{i}(\boldsymbol{p})=\psi_{i}(-\boldsymbol{p})
\tag{7a}
$$

$$
\oiint \psi_{i}(\boldsymbol{p}) d \boldsymbol{p}=1.
\tag{7b}
$$

The first equality (Eq. (7a)) expresses that the fibers oriented at $\boldsymbol{p}$ and $-\boldsymbol{p}$ are indistinguishable, and the second (Eq. (7b)) is the normalization condition that the summation of the orientation distribution probability of all fibers is 1.

The RVE $\omega$ is then decomposed into a set of infinitesimal pseudo-grains. Each pseudo-grain $\omega_{i, p}$ with the volume $d V \omega_{i, p}$, is a two-phase composite material containing the matrix in concentration $v_{m}$ (the same as in the RVE) and those fibers in concentration $\left(1-v_{m}\right)$ with the orientation between $\boldsymbol{p}$ and $\boldsymbol{p}+d \boldsymbol{p}$. For an arbitrary micro-field $\boldsymbol{\mu}(\boldsymbol{x})$ (e.g., micro-strain or stress field), the volume average of $\boldsymbol{\mu}(\boldsymbol{x})$ over the RVE can be written as follows [10,20]:

$$
\langle\boldsymbol{\mu}\rangle_{\omega}=\sum_{i=1}^{N} \frac{v_{i}}{\left(1-v_{m}\right)}\left\langle\langle\boldsymbol{\mu}\rangle_{\omega_{i, p}}\right\rangle_{\psi_{i}} \equiv\left\langle\langle\boldsymbol{\mu}\rangle_{\omega_{i, p}}\right\rangle_{i, \psi_{i}}
\tag{8}
$$

where $\langle\boldsymbol{\mu}\rangle_{\omega_{i, p}}$ represents the volume average of the micro-field $\boldsymbol{\mu}(\boldsymbol{x})$ over a pseudo-grain $\omega_{i, p}$ and $\langle\bullet\rangle_{\psi_{i}}$ is the $\psi_{i}$-weighted average. The orientation average of the micro-field $\boldsymbol{\mu}(\boldsymbol{p})$ is its ODF-weighted average and defined as follows,

$$
\langle\boldsymbol{\mu}(\boldsymbol{p})\rangle_{\psi_{i}} \equiv \oiint \boldsymbol{\mu}(\boldsymbol{p}) \psi_{i}(\boldsymbol{p}) d \boldsymbol{p}.
\tag{9}
$$


In the compact format Eq. (8), $\langle \bullet \rangle_{i,\psi_{i}}$ is the orientation average over all pseudo-grains, which is over all phases and all orientations. Eq. (8) illustrates that the homogenization of the RVE can be performed in the two steps sequentially (shown in Figure. 3): (1) homogenization of each pseudo-grain individually, and (2) homogenization of all pseudo-grains (i.e."aggregate").

Within the frame of the mean-field homogenization method, the per-phase average strains are related to the macro-strain $\langle \boldsymbol{\varepsilon} \rangle$ of two-phase composites by:

$$
\langle\boldsymbol{\varepsilon}\rangle_{m}=\boldsymbol{B}_{m}:\langle\boldsymbol{\varepsilon}\rangle=\left[v_{f} \boldsymbol{B}^{\varepsilon}+\left(1-v_{f}\right) \boldsymbol{I}\right]^{-1}:\langle\boldsymbol{\varepsilon}\rangle \tag{10a}
$$

$$
\langle\boldsymbol{\varepsilon}\rangle_{f}=\boldsymbol{B}_{f}:\langle\boldsymbol{\varepsilon}\rangle=\boldsymbol{B}^{\varepsilon}:\left[v_{f} \boldsymbol{B}^{\varepsilon}+\left(1-v_{f}\right) \boldsymbol{I}\right]^{-1}:\langle\boldsymbol{\varepsilon}\rangle \tag{10b}
$$

where $\boldsymbol{I}$ designates the fourth-order symmetric identity tensor. $\boldsymbol{B}^{\varepsilon}$ is the strain concentration tensor to relate the strain averages per phase $\boldsymbol{\varepsilon}_{f}=\boldsymbol{B}^{\varepsilon}: \boldsymbol{\varepsilon}_{m}$ [30]. Various homogenization models will differ by the expression of $\boldsymbol{B}^{\varepsilon}$, but for any homogenization model defined by $\boldsymbol{B}^{\varepsilon}$, the macro-stiffness tensor $\boldsymbol{C}$ is written as,

$$
\boldsymbol{C}=\left(1-v_{f}\right) \boldsymbol{C}_{m}: \boldsymbol{B}_{m}+v_{f} \boldsymbol{C}_{f}: \boldsymbol{B}_{f} \tag{11}
$$

where $\boldsymbol{C}_{m}$ and $\boldsymbol{C}_{f}$ are the stiffness tensors of the matrix and fibers, respectively.

In the first-step homogenization procedure, the following modified quadratic interpolative model on the basis of M-T and D-I mean-field homogenization models is proposed and implemented to homogenize each pseudo-grain [31],

$$
\boldsymbol{B}_{\omega_{i, p}}^{\varepsilon}=\left\{\left[1-\xi\left(v_{f}\right)\right]\left(\boldsymbol{B}_{M-T}^{\varepsilon}\right)^{-1}+\xi\left(v_{f}\right)\left(\boldsymbol{B}_{D-I}^{\varepsilon}\right)^{-1}\right\}^{-1} \tag{12}
$$

where $\xi(v_f)$ is a smooth interpolation function $\xi(v_f)=v_f(1+v_f)/2$. $\boldsymbol{B}_{M-T}^{\varepsilon}$ and $\boldsymbol{B}_{D-I}^{\varepsilon}$ are the strain concentration tensors for the M-T and D-I homogenization models and are given as,

$$
\boldsymbol{B}_{M-T}^{\varepsilon}=\boldsymbol{H}^{\varepsilon}\left(\boldsymbol{I}, \boldsymbol{C}_{m}, \boldsymbol{C}_{f}\right) \tag{13a}
$$

$$
\boldsymbol{B}_{D-I}^{\varepsilon}=\left\{\left[1-\xi\left(v_{f}\right)\right]\left[\boldsymbol{H}^{\varepsilon}\left(\boldsymbol{I}, \boldsymbol{C}_{m}, \boldsymbol{C}_{f}\right)\right]^{-1}+\xi\left(v_{f}\right)\left[\boldsymbol{H}^{\varepsilon}\left(\boldsymbol{I}, \boldsymbol{C}_{f}, \boldsymbol{C}_{m}\right)\right]\right\}^{-1} \tag{13b}
$$

where the single inclusion strain concentration tensor $\boldsymbol{H}^{\varepsilon}$ is derived as,

$$
\boldsymbol{H}^{\varepsilon}\left(\boldsymbol{I}, \boldsymbol{C}_{m}, \boldsymbol{C}_{f}\right)=\left\{\boldsymbol{I}+\boldsymbol{S}:\left[\boldsymbol{C}_{m}^{-1}: \boldsymbol{C}_{f}-\boldsymbol{I}\right]\right\}^{-1} \tag{14}
$$

where $\boldsymbol{S}$ is Eshelby's tensor depending on the equivalent aspect ratio $\alpha$ of fiber and Poisson's ratio $v_m$ of the matrix (See Appendix. A). Note that the equivalent aspect ratio $\alpha$ of fiber is given as,

$$
\alpha=f \cdot l / d \quad \text{with} \quad 1 \leq f \leq 1.5 \tag{15}
$$

where $l$ and $d$ are the length and diameter of fiber, respectively. Here we select $f=1.25$ [10].

Consequently, the effective stiffness tensor $\langle\boldsymbol{C}\rangle_{\omega_{i, p}}$ of the pseudo-grain is derived by substituting Eq. (12) to Eq. (11).

The Voigt and Reuss mean-field homogenization models in the second-step homogenization procedure ensure physically acceptable results and the symmetric effective stiffness tensors [19]. Therefore, in the second-step homogenization procedure, the following simple interpolative model on the basis of Voigt and Reuss mean-field homogenization models is introduced for the "aggregate" [31],

$$
\langle\boldsymbol{C}\rangle_{\omega}=\frac{1}{2}\langle\boldsymbol{C}\rangle_{\omega}^{\text {Reuss }}+\frac{1}{2}\langle\boldsymbol{C}\rangle_{\omega}^{\text {Voigt }}
\tag{16}
$$

where the effective stiffness tensors $\langle\boldsymbol{C}\rangle_{\omega}^{\text {Voigt }}$ and $\langle\boldsymbol{C}\rangle_{\omega}^{\text {Reuss }}$ are given as,

$$
\langle\boldsymbol{C}\rangle_{\omega}^{\text {Voigt }}=\left\langle\langle\boldsymbol{C}\rangle_{\omega_{i, p}}\right\rangle_{i, \psi_{i}} \quad \text { and } \quad\langle\boldsymbol{C}\rangle_{\omega}^{\text {Reuss }}=\left(\left\langle\left(\langle\boldsymbol{C}\rangle_{\omega_{i, p}}\right)^{-1}\right\rangle_{i, \psi_{i}}\right)^{-1}.
\tag{17}
$$

The physical meaning of the simple interpolative model in the second-step homogenization procedure is actually that the Voigt and Reuss mean-field homogenization models are used for homogenizing all the pseudo-grains, respectively, so that two meso pseudo-grains (see Figure. 3) are obtain. Then the Voigt mean-field homogenization model is adopted again to homogenize those two meso pseudo-grains.

## 4. Results and discussion

In this work, the analyzed composites are Csf/Mg composites, consisting of AZ91D magnesium alloy matrix with $E_{m}=45 GPa, v_{m}=0.35$ and T300 short carbon fibers with $E_{f}=230 GPa, v_{f}=0.25$ and the fiber aspect ratio $l / d=15$, both of which are isotropic linear elastic within the frame of the infinitesimal deformation. The chemical composition of AZ91D magnesium alloy and the physical properties of short carbon fiber are given in Table. 1 and Table. 2, respectively. The liquid-solid extrusion following vacuum infiltration process [32, 33] is adopted to fabricate Csf/Mg composites and the detailed parameters can be found in our previous paper [34]. The microstructures of the tensile fracture surface of Csf/Mg composites is given in Figure. 4, and it can be seen that the pull-out of the carbon fibers on the

fracture surfaces is not significant, which indicates that the fibers and matrix are bonded well at their interfaces [35]. Therefore, here assumes that the fibers and matrix are perfectly bonded at their interfaces, as hypothesized by Pan et al. [25, 36].

For validating the modified two-step mean-field homogenization procedure and the RVE based FE homogenization method, the predicted effective elastic properties of Csf/Mg composites with the fiber volume fraction $v_1$ of 0.10 are compared with that measured from the uniaxial tensile experiments and listed in Table. 3. It is illustrated that both the modified two-step mean-field homogenization procedure and the RVE based FE homogenization method give the accurate predictions on the effective elastic properties of Csf/Mg composites. Therefore, hereafter the RVE based FE homogenization method is used to provide the reference prediction on the effective elastic properties of composites [12, 37]. To more confirm the accuracy of the proposed two-step mean-field homogenization procedure, the results predicted by the proposed two-step mean-field homogenization procedure are compared with that published in the open literature [36]. The results are listed in Table. 4, which confirms that the modified two-step mean-field homogenization procedure proposed here provides the accurate estimation on the effective elastic properties of composites with the randomly distributed fibers in-plane.

From Table. 3 and Table. 4, it is observed that the difference of the predicted elastic properties of Csf/Mg composites between the modified two-step mean-field

homogenization procedure and the RVE based FE homogenization method might be neglected, while the difference of the computational efficiency between the modified two-step mean-field homogenization procedure and the RVE based direct FE homogenization method is quite large. The FE simulations are implemented in the Abaqus/Standard and the meshing is performed with 4-node tetrahedron elements (C3D4 in ABAQUS). The typical numbers of elements and nodes of a RVE with the matrix/fiber length aspect ratio $L/l$ of 2 and the fiber volume fraction $v_1$ of 0.1 are about 2,500,000 and 500,000, respectively. The total computation of one FE simulation and the post-processing time on the DELL Precision M4800 workstation (CPU: Intel(R) Core(TM) i7-4800MQ 2.70GHz, ROM: 16.0GB) is about 8 hours, while the total computation time of the modified two-step mean-field homogenization procedure coded by the program Matlab in the same computer is about 10 seconds. Thus, in the case of neglecting the detailed stress and strain fields, the modified two-step mean-field homogenization procedure including the quadratic interpolative model on the basis of M-T and D-I mean-field homogenization models in the first-step homogenization procedure and the simple interpolative homogenization model in the second-step homogenization procedure on the basis of Vogit and Reuss mean-field homogenization models is an excellent method with the acceptable accuracy and better computational efficiency, to predict the macro-mechanical properties of composites. However, in the case of obtaining the detailed stress and strain fields in the composites, the RVE based FE homogenization method is the better choice to predict the effective mechanical properties of composites. In addition, the RVE

based FE homogenization method is very useful for validating other methods, in which the results obtained by the RVE based FE homogenization method are viewed as the reference results [37]. The homogenized effective elastic stiffness matrices $\langle\boldsymbol{C}\rangle_{M F}$ and $\langle\boldsymbol{C}\rangle_{F E}$ of Csf/Mg composites by the modified two-step mean-field homogenization procedure and the RVE based FE homogenization method are presented in the Voigt contracted notation (in GPa) as follows,

$$
\langle\boldsymbol{C}\rangle_{M F}=\left[\begin{array}{llllll}
81.4226 & 41.9190 & 41.9349 & 0.0000 & 0.0000 & 0.0000 \\
41.9190 & 81.3415 & 41.9196 & 0.0000 & 0.0000 & 0.0000 \\
41.9349 & 41.9196 & 81.4071 & 0.0000 & 0.0000 & 0.0000 \\
0.0000 & 0.0000 & 0.0000 & 19.7113 & 0.0000 & 0.0000 \\
0.0000 & 0.0000 & 0.0000 & 0.0000 & 19.7368 & 0.0000 \\
0.0000 & 0.0000 & 0.0000 & 0.0000 & 0.0000 & 19.7123
\end{array}\right]
$$

and

$$
\langle\boldsymbol{C}\rangle_{F E}=\left[\begin{array}{llllll}
80.7517 & 41.5028 & 41.4485 & 0.0000 & 0.0000 & 0.0000 \\
41.5026 & 80.7970 & 41.4660 & 0.0000 & 0.0000 & 0.0000 \\
41.4486 & 41.4663 & 80.5847 & 0.0000 & 0.0000 & 0.0000 \\
0.0000 & 0.0000 & 0.0000 & 19.7284 & 0.0000 & 0.0000 \\
0.0000 & 0.0000 & 0.0000 & 0.0000 & 19.7020 & 0.0000 \\
0.0000 & 0.0000 & 0.0000 & 0.0000 & 0.0000 & 19.7705
\end{array}\right]
$$

Since the computed values of the off-diagonal entries in the 4th- 6throws and columns of the stiffness matrix $\langle\boldsymbol{C}\rangle_{M F}$ and $\langle\boldsymbol{C}\rangle_{F E}$ are four or five orders of magnitude smaller than the other entries and, thus, can be considered as null. To investigate the isotropy of Csf/Mg composites, the parameter defined in Ref. [15,38] is adopted,

$$
a_{i j}=\frac{\min \left(2\langle C\rangle_{(9-i-j)(9-i-j)},\langle C\rangle_{i j}^{T}-\langle C\rangle_{i j}\right)}{\max \left(2\langle C\rangle_{(9-i-j)(9-i-j)},\langle C\rangle_{i j}^{T}-\langle C\rangle_{i j}\right)} \quad \text { with } \quad i, j=1,2,3 \quad \text { and } \quad i \neq j \quad(18)
$$

where $\langle C\rangle_{ij}^{T}=\left(\langle C\rangle_{ii}+\langle C\rangle_{jj}\right)/2$ and $a_{ij}$ takes the value 1 for an isotropic material. By substituting the entries in the stiffness matrix $\langle C\rangle_{MF}$ and $\langle C\rangle_{FE}$, the values of $a_{ij}$ are calculated and listed in Table. 5, which illustrates that the effective elastic behavior of Csf/Mg composites can be approximated to that of an isotropic material, resulting from the random fiber distribution.

Meanwhile, the effective elastic properties of Csf/Mg composites for a range of the fiber volume fraction are predicted by using the traditional two-step mean-field homogenization procedures including the D-I/Reuss and M-T/Voigt models, the modified two-step mean-field homogenization procedure and the RVE based FE homogenization method, and are plotted in Figure. 5. We can find that the effective elastic properties of Csf/Mg composites predicted by the modified two-step mean-field homogenization procedure agree well with that predicted by the RVE based FE homogenization method and are in the range of that predicted by the traditional two-step mean-field homogenization models within a range of the fiber volume fraction. Thus, the modified two-step mean-filed homogenization procedure gives more accurate prediction on the effective elastic properties of Csf/Mg composites, compared with the traditional two-step mean-filed homogenization procedures.

## 5. Conclusion

The effective elastic properties of metal matrix composites with the randomly distributed fibers are investigated by using the modified two-step mean-filed homogenization procedure, which includes the quadratic interpolative model on the basis of M-T and D-I mean-field models in the first-step homogenization procedure

and the simple interpolative model in the second-step homogenization procedure on the basis of Vogit and Reuss mean-field models, and by using the RVE based FE homogenization method. Compared with results measured from the uniaxial tensile experiments, both the modified two-step mean-filed homogenization procedure and the RVE based FE homogenization method provide the accurate predictions on the effective elastic properties of metal matrix composites with the randomly distributed fibers. However, in the case of neglecting the detailed stress and strain fields, the two-step mean-field homogenization procedure is more computational efficient than the RVE based FE homogenization method, but to obtain the detailed stress and strain fields in the composites, the RVE based FE homogenization method is the better choice. Compared with the traditional two-step mean-field homogenization procedures, the modified two-step mean-field homogenization procedure provides more accurate prediction on the effective elastic properties of metal matrix composites with the randomly distributed fibers.

**Acknowledgement**

The authors wish to thank the National Nature Science Foundation of China (Nos.51472203 and 51432008), National High Tech Research and Development Program of China (2014AA8011004B), the Doctorate Foundation of Northwestern Polytechnical University (CX201312) and China Scholarship Council for their financial support.

**Appendix A. Eshelby's tensor**

The components of Eshelby's tensor $S$ for an elastic fiber of the equivalent aspect ratio $\alpha=1.25 \cdot l / d$ with the axis parallel to the $x$ axis embedded in an isotropic elastic matrix of Poisson's ratio $v_{m}$ are given as follows [37]:

$$
S_{1111}=\frac{1}{2 h\left(v_{m}\right)}\left[\frac{4 f(\alpha)+2}{f(\alpha)}+2 h\left(v_{m}\right)-2-g(\alpha)\left(2 h\left(v_{m}\right)-1+\frac{3 f(\alpha)+3}{f(\alpha)}\right)\right]
$$

$$
S_{2222}=S_{3333}=\frac{1}{4 h\left(v_{m}\right)}\left[\frac{3 f(\alpha)+3}{2 f(\alpha)}+g(\alpha)\left(2 h\left(v_{m}\right)-1-\frac{9}{4 f(\alpha)}\right)\right]
$$

$$
S_{2211}=S_{3311}=\frac{1}{2 h\left(v_{m}\right)}\left[-\frac{f(\alpha)+1}{f(\alpha)}-2 h\left(v_{m}\right)+2+g(\alpha)\left(2 h\left(v_{m}\right)-1+\frac{3}{2 f(\alpha)}\right)\right]
$$

$$
S_{2211}=S_{3311}=\frac{1}{2 h\left(v_{m}\right)}\left[-\frac{f(\alpha)+1}{f(\alpha)}+\frac{g(\alpha)}{2}\left(\frac{3 f(\alpha)+3}{2 f(\alpha)}-2 h\left(v_{m}\right)+1\right)\right]
$$

$$
S_{2233}=S_{3322}=\frac{1}{4 h\left(v_{m}\right)}\left[\frac{f(\alpha)+1}{2 f(\alpha)}-g(\alpha)\left(2 h\left(v_{m}\right)-1+\frac{3}{4 f(\alpha)}\right)\right]
$$

$$
S_{1212}=S_{1313}=\frac{1}{4 h\left(v_{m}\right)}\left[-\frac{2}{f(\alpha)}+2 h\left(v_{m}\right)-2-\frac{g(\alpha)}{2}\left(2 h\left(v_{m}\right)-1-\frac{3 f(\alpha)+6}{f(\alpha)}\right)\right]
$$

$$
S_{2323}=\frac{S_{2222}-S_{2233}}{2}
$$

where $g(\alpha)$ is the following function,

$$
g(\alpha)=\frac{(f(\alpha)+1)^{1 / 2}}{(f(\alpha))^{3 / 2}}\left[((f(\alpha)+1) f(\alpha))^{1 / 2}-a \cosh (\alpha)\right]
$$

with $h(v_{m})=1-v_{m}$ and $f(\alpha)=\alpha^{2}-1$. Note that the Eshelby's tensor has the minor symmetries and all other components are nil.

References

[1] I. Kientzl, I. Orbulov, J. Dobranszky, A. Nemeth, Mechanical behaviour Al-matrix composite wires in double composite structures, Advances in Science and Technology 50 (2006) 147 – 150.

[2] L. Qi, L. Su, J. Zhou, J. Guan, X. Hou, H. Li, Infiltration characteristics of liquid AZ91D alloy into short carbon fiber preform, Journal of Alloys and Compounds 527 (0) (2012)10 – 15.

[3] J. Rams, A. Urea, M. Escalera, M. Snchez, Electroless nickel coated short carbon fibres in aluminium matrix composites, Composites Part A: Applied Science and Manufacturing 38 (2) (2007) 566 – 575.

[4] L. Qi, Y. Ma, J. Zhou, X. Hou, H. Li, Effect of fiber orientation on mechanical properties of 2D-$C_f$/Al composites by liquid solid extrusion following vacuum infiltration technique, Materials Science and Engineering: A 625 (0) (2015) 343 – 349.

[5] I, Kientzl, A. Németh, Infiltration characteristics of carbon fiber reinforced MMCs, Materials Science Forum 659 (2010) 229-234.

[6] I, Kientzl, I. Orbulov, J. Dobranszky, A. Németh, The processing and testing of aluminium matrix composite wires, double composites and block composites. In: Lamon J, Torres Marques A (eds.) Proceedings of 12th European Conference on Composite Materials: From the Science of Composites to Engineering Applications: the drawing future of composites, Biarritz, France, 29 August - 1 September 2006.[7] Y. Peng, K. Deng, Study on the mechanical properties of the novel Sn-Bi/Graphene nanocomposite by finite element simulation, Journal of Alloys and Compounds 625 (0) (2015) 44 – 51.

[8] J. Aboudi, M. Pindera, S. Arnold, Higher-order theory for periodic multiphase materials with inelastic phases, International Journal of Plasticity 19 (6) (2003) 805 -847.

[9] J. Fish, K. Shek, M. Pandheeradi, M. Shephard, Computational plasticity for composite structures based on mathematical homogenization: Theory and practice, Computer Methods in Applied Mechanics and Engineering 148 (12) (1997) 53 - 73.

[10] I. Doghri, L. Tinel, Micromechanical modeling and computation of elasto-plastic materials reinforced with distributed-orientation fibers, International Journal of Plasticity 21 (10) (2005) 1919 - 1940.

[11] S. Lomov, D. Ivanov, I. Verpoest, M. Zako, T. Kurashiki, H. Nakai, J. Molimard, A. Vautrin, Full-field strain measurements for validation of meso-FE analysis of textile composites, Composites Part A: Applied Science and Manufacturing 39 (8) (2008) 1218 - 1231.

[12] C. Gonzalez, J. Segurado, J. LLorca, Numerical simulation of elasto-plastic deformation of composites: evolution of stress micro-fields and implications for homogenization models, Journal of the Mechanics and Physics of Solids 52 (7) (2004) 1573 - 1593.

[13] W. Lee, J. Son, N. Kang, I. Park, Y. Park, Finite-element analysis of deformation behaviors in random-whisker-reinforced composite, Scripta Materialia 61 (6) (2009) 580- 583.

[14] L. Harper, C. Qian, T. Turner, S. Li, N. Warrior, Representative volume elements for discontinuous carbon fibre composites- part 2: Determining the critical size, Composites Science and Technology 72 (2) (2012) 204 - 210.

[15] W. Tian, L. Qi, J. Zhou, J. Liang, Y. Ma, Representative volume element for composites reinforced by spatially randomly distributed discontinuous fibers and its applications, Composite Structures 131 (0) (2015) 366 - 373.

[16] T. Mori, K. Tanaka, Average stress in matrix and average elastic energy of materials with misfitting inclusions, Acta Metallurgica 21 (5) (1973) 571 - 574.

[17] J. Ma, S. Zhang, P. Wriggers, W. Gao, L. Lorenzis, Stochastic homogenized effective properties of three-dimensional composite material with full randomness and correlation in the microstructure, Computers & Structures 144 (0) (2014) 62 - 74.

[18] G. Lielens, P. Pirotte, A. Couniot, F. Dupret, R. Keunings, Prediction of thermomechanical properties for compression moulded composites, Composites Part A: Applied Science and Manufacturing 29 (12) (1998) 63 - 70.

[19] Y. Benveniste, A new approach to the application of Mori-Tanaka's theory in composite materials, Mechanics of Materials 6 (2) (1987) 147 - 157.

[20] O. Pierard, C. Friebel, I. Doghri, Mean-field homogenization of multi-phase thermoelastic composites: a general framework and its validation, Composites Science and Technology 64 (1011) (2004) 1587 - 1603.

[21] W. Voigt, Ueber die beziehung zwischen den beiden elasticittsconstanten isotroper krper, Annalen der Physik 274 (12) (1889) 573-587.

[22] A. Reuss, Berechnung der fliegrenze von mischkristallen auf grund der plastizittsbedingung fr einkristalle, Journal of Applied Mathematics and Mechanics 9 (1) (1929)49-58.

[23] M. Wu, L. Wen, B. Tang, L. Peng, W. Ding, First-principles study of elastic and electronic properties of MgZn₂ and ScZn₂ phases in Mg-Sc-Zn alloy, Journal of Alloys and Compounds 506 (1) (2010) 412 – 417.

[24] Y. Lee, B. Harmon, First principles calculation of elastic properties of AlMgB₁₄, Journal of Alloys and Compounds 338 (12) (2002) 242 – 247.

[25] Y. Pan, L. Iorga, A. Pelegri, Numerical generation of a random chopped fiber composite RVE and its elastic properties, Composites Science and Technology 68 (13) (2008) 2792– 2798.

[26] Z. Lu, Z. Yuan, Q. Liu, 3D numerical simulation for the elastic properties of random fiber composites with a wide range of fiber aspect ratios, Computational Materials Science 90 (0) (2014) 123 – 129.

[27] J. Segurado, J. Llorca, A numerical approximation to the elastic properties of sphere reinforced composites, Journal of the Mechanics and Physics of Solids 50 (10) (2002) 2107 – 2121.

[28] Y. Kogure, Simulation of mechanical damping in nanostructures, Journal of Alloys and Compounds 355 (12) (2003) 188 – 195.

[29] H. Bohm, A. Eckschlager, W. Han, Multi-inclusion unit cell models for metal matrix composites with randomly oriented discontinuous reinforcements, Computational Materials Science 25 (12) (2002) 42 – 53.

[30] R. Hill, Elastic properties of reinforced solids: Some theoretical principles, Journal of the Mechanics and Physics of Solids 11 (5) (1963) 357 – 372.

[31] W. Tian, L. Qi, J. Zhou, C. Su, J. Liang, Numerical evaluation on mechanical properties of short-fiber-reinforced metal matrix composites: Two-step mean-field homogenization procedure, Composite Structures (2015) Under Review.

[32] J. Liu, L. Qi, J. Guan, Y. Ma, J. Zhou, Compressive behavior of Csf/AZ91D composites by liquid-solid extrusion directly following vacuum infiltration technique, Materials Science and Engineering: A 531 (2012): 164-170.[33] Orbulov IN, Kientzl I, Blücher J, Ginsztler J, Németh Á, Dobránszky J: Production and investigation of a metal matrix composite pipe, In: Kollár LP, Czigány T, Karger-Kocsis J (eds.) Proceedings of 14th European Conference on Composite Materials, Budapest, Hungary, 7 - 10 June 2010.

[34] L. Qi, J. Liu, J. Guan, J. Zhou, H. Li, Tensile properties and damage behaviors of C sf/Mg composite at elevated temperature and containing a small fraction of liquid, Composites Science and Technology 72 (14) (2012): 1774-1780.

[35] H. Ouyang, H. Li, L. Qi, Z. Li, L. Su, J. Wei, Fabrication of Short Carbon Fiber Reinforced AZ91D Alloy by Infiltration-Extrusion Integrated Technique, Rare Metal Materials and Engineering 38 (2009): 100-104.

[36] Y. Pan, L. Iorga, A. Pelegri, Analysis of 3D random chopped fiber reinforced composites using FEM and random sequential adsorption, Computational Materials Science 43 (3) (2008) 450-461.

[37] O. Pierard, C. Gonzlez, J. Segurado, J. LLorca, I. Doghri, Micromechanics of elastoplastic materials reinforced with ellipsoidal inclusions, International Journal of Solids and Structures 44 (21) (2007) 6945 - 6962.

[38] T. Kanit, F. N'Guyen, S. Forest, D. Jeulin, M. Reed, S. Singleton, Apparent and effective physical properties of heterogeneous materials: Representativity of samples of two materials from food industry, Computer Methods in Applied Mechanics and Engineering 195 (33-36) (2006) 3960 - 3982.

Figures:

![](./images/814586853469454338_3.jpg)

Figure. 1: Periodic geometry and meshes of RVE for metal matrix composites with the randomly distributed fibers with matrix/fiber aspect ratio of 2, fiber aspect ratio of 15 and fiber volume fraction of 10%: (a) RVE, (b) Mesh

![](./images/814586853469454338_4.jpg)

Figure. 2: Unit fiber orientation vector $\boldsymbol{p}$ defined by two Euler orientation angles $\theta \in [0,\pi]$ and $\varphi \in [0, \, 2\pi]$ in the fixed Cartesian coordinate system $ox^1x^2x^3$

![](./images/814586853469454338_5.jpg)

Figure. 3: Two-step homogenization scheme: The RVE is decomposed into a set of grains, each of which is then individually homogenized (First step). The second homogenization is performed over all the grains (Second step).

![](./images/814586853469454338_6.jpg)

Figure. 4: The microstructures of tensile fracture surface of Csf/Mg composites fabricated by the liquid-solid extrusion following vacuum infiltration process.

![](./images/814586853469454338_7.jpg)

Figure. 5: Effective elastic modulus E and shear modulus G of Csf/Mg composites predicted by the traditional two-step mean-field homogenization procedures, modified two-step mean-field homogenization procedure and RVE based FE homogenization method.

Tables:

<table>
  <tr>
    <th>Element</th>
    <td>Al</td>
    <td>Zn</td>
    <td>Mn</td>
    <td>Si</td>
    <td>Cu</td>
    <td>Ni</td>
    <td>Fe</td>
    <td>Mg</td>
  </tr>
  <tr>
    <th>Content (wt.%)</th>
    <td>9.1</td>
    <td>0.7</td>
    <td>0.28</td>
    <td>0.02</td>
    <td>0.02</td>
    <td>0.005</td>
    <td>0.005</td>
    <td>remaining</td>
  </tr>
</table>

Table. 1: Chemical composition of AZ91D alloy matrix

<table>
  <tr>
    <th>Properties</th>
    <td>Average diameter</td>
    <td>Average length</td>
    <td>Tensile strength</td>
  </tr>
  <tr>
    <th>Value</th>
    <td>7 µm</td>
    <td>105 µm</td>
    <td>3500 MPa</td>
  </tr>
  <tr>
    <th>Properties</th>
    <td>Young's modulus</td>
    <td>Fracture strain</td>
    <td>Density</td>
  </tr>
  <tr>
    <th>Value</th>
    <td>230 GPa</td>
    <td>1.5%</td>
    <td>1.76 g/cm³</td>
  </tr>
</table>

Table. 2: Physical properties of T300 short carbon fiber

<table>
    <thead>
        <tr>
            <th></th>
            <th>Tensile experiment</th>
            <th>Two-step model</th>
            <th>Error #1</th>
            <th>FE homogenization</th>
            <th>Error #2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>E ($GPa$)</td>
            <td>50.45</td>
            <td>52.85</td>
            <td>4.76%</td>
            <td>52.57</td>
            <td>4.20%</td>
        </tr>
        <tr>
            <td>G ($GPa$)</td>
            <td>19.02</td>
            <td>19.72</td>
            <td>3.68%</td>
            <td>19.73</td>
            <td>3.73%</td>
        </tr>
        <tr>
            <td>ν</td>
            <td>0.3425</td>
            <td>0.3401</td>
            <td>0.91%</td>
            <td>0.3394</td>
            <td>0.91%</td>
        </tr>
    </tbody>
</table>

Table. 3: Effective elastic properties of Csf/Mg composites obtained from the modified two-step mean-field homogenization procedure, FE homogenization and uniaxial tensile experiment

<table>
    <thead>
        <tr>
            <th></th>
            <th rowspan="2">Two-step model</th>
            <th colspan="2">Elastic properties from Ref. [36]</th>
            <th colspan="2">Relative Error</th>
        </tr>
        <tr>
            <th></th>
            <th>FEM</th>
            <th>Halpin-Tsai</th>
            <th></th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>E (GPa)</td>
            <td>5.15</td>
            <td>5.21</td>
            <td>5.53</td>
            <td>1.15%</td>
            <td>6.87%</td>
        </tr>
        <tr>
            <td>G (GPa)</td>
            <td>1.96</td>
            <td>1.99</td>
            <td>2.02</td>
            <td>1.51%</td>
            <td>2.97%</td>
        </tr>
        <tr>
            <td>ν</td>
            <td>0.35</td>
            <td>0.33</td>
            <td>0.37</td>
            <td>6.06%</td>
            <td>5.41%</td>
        </tr>
    </tbody>
</table>

Table. 4: Comparison of results predicted by the proposed two-step mean-field homogenization procedure and from Ref. [36].

<table>
    <thead>
        <tr>
            <th></th>
            <th>$a_{12}$</th>
            <th>$a_{13}$</th>
            <th>$a_{23}$</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Two-step homogenization</td>
            <td>0.9990</td>
            <td>0.9998</td>
            <td>0.9992</td>
        </tr>
        <tr>
            <td>FE homogenization</td>
            <td>0.9932</td>
            <td>0.9953</td>
            <td>0.9941</td>
        </tr>
    </tbody>
</table>

Table. 5: Isotropy parameter of the homogenized stiffness matrix of Csf/Mg composites

### Highlights

1. Elastic properties of short-fiber reinforced metal matrix composites are evaluated;

2. Modified two-step mean-field homogenization procedure is introduced;

3. RVE based FE homogenization method is implemented to provide reference results;

4. Computational efficiency of FE method and mean-field procedure is compared.