Modelling and Simulation in Materials Science and Engineering

ACCEPTED MANUSCRIPT

# Numerically efficient microstructure-based calculation of internal stresses in superalloys

To cite this article before publication: Siwen Gao *et al* 2017 *Modelling Simul. Mater. Sci. Eng.* in press https://doi.org/10.1088/1361-651X/aa9ba3

Manuscript version: Accepted Manuscript

Accepted Manuscript is "the version of the article accepted for publication including all changes made as a result of the peer review process, and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an 'Accepted Manuscript' watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors"

This Accepted Manuscript is © 2017 IOP Publishing Ltd.

During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully protected by copyright and cannot be reused or reposted elsewhere.

As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.

After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they adhere to all the terms of the licence https://creativecommons.org/licences/by-nc-nd/3.0

Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.

View the article online for updates and enhancements.

This content was downloaded from IP address 205.208.116.24 on 24/11/2017 at 10:49

# Numerically efficient microstructure-based calculation of internal stresses in superalloys

Siwen Gao¹, Umaaran Gogilan¹, Anxin Ma¹ and Alexander Hartmaier¹

¹ Interdisciplinary Centre for Advanced Materials Simulation, Ruhr-Universität Bochum, 44801 Bochum, Germany

E-mail: Siwen.Gao@ruhr-uni-bochum.de

## Abstract.
According to the classical Eshelby inclusion problem, we introduce a new linear relation to calculate internal stresses in $\gamma/\gamma'$ microstructures of superalloys via an effective stiffness method. To accomplish this, we identify regions with almost uniform deformation behavior within the microstructure. Assigning different eigenstrains to these regions results in a characteristic internal stress state. The linear relation between eigenstrains and internal stresses, as proposed by Eshelby for simpler geometries, is shown to be a valid approximation to the solution for complex microstructures. The Fast Fourier Transformation method is chosen as a very efficient numerical solver to determine the effective stiffness matrix. Numerical validation shows that this generalized method with the effective stiffness matrix is efficient to obtain appropriate internal stresses and that it can be used to consider the influence of internal stresses on plasticity and creep kinetics in superalloys.

Numerically efficient microstructure-based calculation of internal stresses in superalloys

### 1. Introduction

Ni-base and Co-base superalloys are known for their outstanding creep resistance at high temperatures. The creep behavior and corresponding mechanisms related to the dislocation motion in the microstructure of these alloys have been well investigated experimentally by different research groups, such as the general introduction of creep and dislocation structures in some typical superalloys [1, 2, 3], the formation of dislocation networks on $\gamma/\gamma'$ interfaces at high temperatures [4], the orientation dependence of creep under different loading conditions [5, 6], as well as the shearing of $\gamma'$ precipitates with stacking faults [7]. In addition, through comprehensive dislocation dynamics modeling, the important creep mechanisms were clarified and validated [8]. Since the creep behavior is attributed to the particular microstructure where softer face centered cubic (FCC) $\gamma$ matrix is strengthened by stronger cuboidal or spherical L1₂-ordered $\gamma'$ precipitates [9], the crystal plasticity modeling of creep deformation should be also based on this microstructure. Due to the $\gamma/\gamma'$ lattice mismatch and the inhomogeneous deformation in $\gamma$ matrix and $\gamma'$ precipitate during creep, internal stresses are generated, which influences further deformation and rafting of precipitates [10, 11, 12, 13, 14]. Although several dislocation-based constitutive models have taken the importance of internal stresses into account [15, 16, 17], their calculations mainly depend on the common microstructure with narrow $\gamma$ channels and cubic $\gamma'$ precipitate. To overcome this restriction, a new method is developed here to calculate internal stresses in $\gamma/\gamma'$ microstructure of superalloys numerically, by generalization of Eshelby inclusion problem [18, 19] and identification of regions with uniform deformation behavior. This method can be used not only for cubic $\gamma'$ precipitates, but also for different morphologies, such as spherical $\gamma'$ precipitates. It is worthy to note that the calculated internal stresses in the present work result from the eigenstrains in different regions which are sum of the accumulated plastic strains and misfit strains at a certain time, where the microstructure and the deformation state are known. During the deformation, the internal stresses can be updated by using this method in every time step. This method can be easily implemented in crystal plasticity finite element models to consider the evolution of internal stresses while simulating creep or plastic deformation of larger structures or components. In our work we only solve the linear elastic problem relating the eigenstrains to internal stresses, but we note for the sake of completeness that recent developments on spectral solvers also allow them to be used for finite deformations and non-linear materials [20, 21, 22].

### 2. Determination of the effective stiffness matrix

Under external load the lattice mismatch in superalloys leads to the inhomogeneous deformation in different channels [13]. The internal stresses caused by the misfit strain and the deformation heterogeneity play an important role on the deformation. If the elastic and plastic strains are known, the total stress $\boldsymbol{\sigma}_{\text{tot}}$ including the external stress

Numerically efficient microstructure-based calculation of internal stresses in superalloys

$\boldsymbol{\sigma}_{\text{ext}}$ and the internal stress $\boldsymbol{\sigma}_{\text{int}}$ are given as
$$
\boldsymbol{\sigma}_{\text{tot}} = \boldsymbol{\sigma}_{\text{ext}} + \boldsymbol{\sigma}_{\text{int}} = \mathbb{C}: \boldsymbol{\varepsilon}_{\text{el}} + \mathbb{C}'': (\boldsymbol{\varepsilon}_{\text{pl}} + \boldsymbol{\varepsilon}_{\text{mis}}), \tag{1}
$$
where $\mathbb{C}$ is the elastic stiffness matrix, $\boldsymbol{\varepsilon}_{\text{el}}$ is the elastic strain, $\boldsymbol{\varepsilon}_{\text{pl}}$ is the plastic strain, $\boldsymbol{\varepsilon}_{\text{mis}}$ is the misfit strain, and $\mathbb{C}''$ is an assumed effective stiffness matrix connecting the internal stress with plastic strain and misfit strain. In this paper, we aim to determine $\mathbb{C}''$, so as to calculate the internal stress through it.

In view of the characteristic $\gamma/\gamma'$ microstructure of superalloy single crystals, a cubic representative volume element (RVE), similar to that used in [23, 24, 13], containing one cubic $\gamma'$ precipitate surrounded by narrow $\gamma$ matrix channels, is utilized to determine internal stresses. With known eigenstrains in the RVE with periodic boundary conditions (PBC), the internal stresses can be calculated by the Fast Fourier Transformation (FFT) method [25, 26, 27, 13]. The RVE is treated as a material with a reference stiffness $\bar{\mathbb{C}}$, which is a volume average of local elastic stiffnesses. Analogous to the solution of the Eshelby inclusion problem [18, 19], by assigning the eigenstrain $\bar{\varepsilon}$ to the local strain, the internal stress on each FFT grid can be obtained by
$$
\boldsymbol{\sigma}_{\text{int}} = \bar{\boldsymbol{\sigma}}_{\text{int}} + \tilde{\boldsymbol{\sigma}}_{\text{int}}, \tag{2}
$$
where the mean internal stress $\bar{\boldsymbol{\sigma}}_{\text{int}}$ is the volume average of $\boldsymbol{\sigma}_{\text{int}}$. The local internal stress fluctuation $\tilde{\boldsymbol{\sigma}}_{\text{int}}$ is identical to the constraint stress caused by the corresponding strain fluctuation $\tilde{\boldsymbol{\varepsilon}}$:
$$
\tilde{\boldsymbol{\sigma}}_{\text{int}} = \bar{\mathbb{C}}(\mathbf{E} - \mathbf{I})\tilde{\boldsymbol{\varepsilon}}, \tag{3}
$$
where $\mathbf{E}$ is the Eshelby tensor and $\mathbf{I}$ is the unit tensor. We extend Eq. (3) to consider the interaction among FFT grids
$$
\tilde{\sigma}_{\text{int } ij,j} = [\bar{\mathbb{C}}(\mathbf{E} - \mathbf{I})]_{ijkl}\tilde{\varepsilon}_{kl,j} = [\bar{\mathbb{C}}(\mathbf{E} - \mathbf{I})]_{ijkl}\tilde{u}_{k,lj}, \tag{4}
$$
where $\tilde{u}_{k,lj}$ is the displacement to produce $\tilde{\varepsilon}_{kl,j}$. We use the same Fourier transformation method shown in [13] to solve Eq. (4), and finally to gain the internal stress.

Based on this FFT method and assuming the deformation of the RVE follows a simple constitutive equation as
$$
\dot{\varepsilon} = A\sigma_{\text{tot}}^n = A(\sigma_{\text{ext}} + \sigma_{\text{int}})^n, \tag{5}
$$
where $\dot{\varepsilon}$ is the strain rate, $A$ is the reference parameter and $n$ is the stress exponent, the full fields of plastic strain and internal stress in the RVE can be calculated. Before the deformation starts, the misfit strain determines the internal stress. Here, in $\gamma'$ precipitate $\boldsymbol{\varepsilon}_{\text{mis}} = \delta\mathbf{I}$ and in $\gamma$ channels $\boldsymbol{\varepsilon}_{\text{mis}} = 0$, where $\delta$ is the lattice mismatch ratio. As the plastic strain is generated, we combine the misfit strain and the plastic strain as the general eigenstrain to determine the internal stress in each time step. The new internal stress influences the plastic strain in the next time step. From an example for a RVE with approx. 66% volume fraction of a cube $\gamma'$ precipitate in Fig. 1, we can see that the plastic strains and the internal stresses in some regions are similar under a constant uniaxial tensile load of 300 MPa along [001] direction. Meanwhile, the internal

Numerically efficient microstructure-based calculation of internal stresses in superalloys

stress varies with the plastic strain gradually during the deformation. Furthermore, the regions with similar plastic strains are also found in Fig. 2 for other two loading directions. These results depend on the model parameters in Tab. 1 and the elastic constants at room temperature of a Ni-base single crystal superalloy [28]. Since the $\gamma'$ phase is stronger than $\gamma$ phase, we use a smaller $A$ for $\gamma'$ phase.

**Table 1.** Model parameters.

<table>
  <thead>
    <tr>
      <th>$n$</th>
      <th>$3$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$A$ in $\gamma$ [$\text{MPa}^{-n}$]</td>
      <td>$1.0 \times 10^{-12}$</td>
    </tr>
    <tr>
      <td>$A$ in $\gamma'$ [$\text{MPa}^{-n}$]</td>
      <td>$1.0 \times 10^{-14}$</td>
    </tr>
    <tr>
      <td>$\delta$</td>
      <td>$-0.0015$</td>
    </tr>
  </tbody>
</table>

![](./images/813084444159115264_1.jpg)

**Figure 1.** The evolution of full fields of equivalent plastic strains (a) and equivalent von Mises internal stresses (b) in the RVE with a cubic $\gamma'$ precipitate during the deformation under a constant uniaxial tensile load of 300 MPa along [001] direction.

If this RVE is only considered as an integration point in a finite element method, the detailed plastic strains and internal stresses on each FFT node are not required, and it is sufficient to know the solution in the regions of homogeneous deformation behavior. According to the observation and the analysis of plastic strains in the RVE, as well as the approach proposed by Fedelich [16], the plastic deformation can be taken approximately uniform in each channel and in the $\gamma'$ precipitate. Therefore, the RVE generally consists of four main regions which are one $\gamma'$ phase and three $\gamma$ channels in

Numerically efficient microstructure-based calculation of internal stresses in superalloys

![](./images/813084444159115264_2.jpg)

Figure 2. Full fields of equivalent plastic strains in 500 time steps in the RVE with a cubic $\gamma'$ precipitate under a constant uniaxial tensile load of 300 MPa along [110] direction (a) and [111] direction (b).

three given orthogonal directions of cartesian coordinate system, respectively. Based on equation (8) in the literature [16], the uniform plastic strain and the misfit strain in these four regions can be expressed as

$$
\overline{\boldsymbol{\varepsilon}} \begin{cases}
\overline{\varepsilon}^{\mathrm{x}}: & \text { plastic strain in channels normal to } \mathrm{x} \text {-direction; } \\
\overline{\varepsilon}^{\mathrm{y}}: & \text { plastic strain in channels normal to } \mathrm{y} \text {-direction; } \\
\overline{\varepsilon}^{\mathrm{z}}: & \text { plastic strain in channels normal to } \mathrm{z} \text {-direction; } \\
\overline{\varepsilon}^{\mathrm{p}}: & \text { plastic strain and misfit strain in the precipitate, }
\end{cases}
\tag{6}
$$

where $\overline{\varepsilon}^{\mathrm{x}}, \overline{\varepsilon}^{\mathrm{y}}, \overline{\varepsilon}^{\mathrm{z}}$, and $\overline{\varepsilon}^{\mathrm{p}}$ are deemed as eigenstrains for the calculation of internal stresses.

As shown in Fig. 3, when $\overline{\varepsilon}^{\mathrm{x}}, \overline{\varepsilon}^{\mathrm{y}}, \overline{\varepsilon}^{\mathrm{z}}$, and $\overline{\varepsilon}^{\mathrm{p}}$ are assigned to the corresponding FFT grids in x-, y-, z-channels and precipitate, respectively, and the FFT grids in the edge and corner areas take the average values of eigenstrains in adjacent channels, the full field of internal stresses in the RVE can be obtained by the introduced FFT method as well. By averaging the values in the respective regions, the $\overline{\mathbf{S}}^{\mathrm{INTx}}, \overline{\mathbf{S}}^{\mathrm{INTy}}, \overline{\mathbf{S}}^{\mathrm{INTz}}$, and $\overline{\mathbf{S}}^{\mathrm{INTp}}$ are adopted to represent the internal stresses there. For a large precipitate and narrow channels, the areas in the edge and corner can be neglected. The general subdivision of the RVE is displayed in Fig. 4.

Even though the FFT method is an efficient way to calculate internal stresses, it is still time-consuming for long-time deformation of a large component with lots of material points. We introduce a mathematical linear relation between internal stresses and eigenstrains with an effective stiffness matrix as

$$
\overline{\mathbf{S}}^{\mathrm{INT}}=\mathbb{C}^{\prime \prime}: \overline{\boldsymbol{\varepsilon}}.
\tag{7}
$$

Extending $\overline{\mathbf{S}}^{\mathrm{INT}}$ and $\overline{\boldsymbol{\varepsilon}}$ to four sections respectively, Eq. 7 becomes

$$
\left(\begin{array}{c}
\overline{\mathbf{S}}^{\mathrm{INTx}} \\
\overline{\mathbf{S}}^{\mathrm{INTy}} \\
\overline{\mathbf{S}}^{\mathrm{INTz}} \\
\overline{\mathbf{S}}^{\mathrm{INTp}}
\end{array}\right)=\left(\begin{array}{llll}
\mathbb{C}_{\mathrm{xx}}^{\prime \prime} & \mathbb{C}_{\mathrm{xy}}^{\prime \prime} & \mathbb{C}_{\mathrm{xz}}^{\prime \prime} & \mathbb{C}_{\mathrm{xp}}^{\prime \prime} \\
\mathbb{C}_{\mathrm{yx}}^{\prime \prime} & \mathbb{C}_{\mathrm{yy}}^{\prime \prime} & \mathbb{C}_{\mathrm{yz}}^{\prime \prime} & \mathbb{C}_{\mathrm{yp}}^{\prime \prime} \\
\mathbb{C}_{\mathrm{zx}}^{\prime \prime} & \mathbb{C}_{\mathrm{zy}}^{\prime \prime} & \mathbb{C}_{\mathrm{zz}}^{\prime \prime} & \mathbb{C}_{\mathrm{zp}}^{\prime \prime} \\
\mathbb{C}_{\mathrm{px}}^{\prime \prime} & \mathbb{C}_{\mathrm{py}}^{\prime \prime} & \mathbb{C}_{\mathrm{pz}}^{\prime \prime} & \mathbb{C}_{\mathrm{pp}}^{\prime \prime}
\end{array}\right) \cdot\left(\begin{array}{c}
\overline{\varepsilon}^{\mathrm{x}} \\
\overline{\varepsilon}^{\mathrm{y}} \\
\overline{\varepsilon}^{\mathrm{z}} \\
\overline{\varepsilon}^{\mathrm{p}}
\end{array}\right).
\tag{8}
$$

Numerically efficient microstructure-based calculation of internal stresses in superalloys6

![](./images/813084444159115264_3.jpg)

Figure 3. Schematic diagram of one eighth of the periodic RVE, indicating the subdivision into regions with uniform deformation behavior. The eigenstrains in these regions are correlated to internal stresses via the FFT method with a regular grid. The different colors represent different regions.

![](./images/813084444159115264_4.jpg)

Figure 4. Schematic diagram of subdivision of RVE with a cubic $\gamma'$ precipitate.

Taking six components of each stress (strain) tensor into account, there are 24 independent stress (strain) components totally. Hence, the entire effective stiffness $\mathbb{C}''$ should be a $24 \times 24$ matrix. In order to determine the effective stiffness matrix, we assign the value of "1" to each of strain component (e.g., $\bar{\varepsilon}_{11}^{x}$, $\bar{\varepsilon}_{22}^{x}$, $\bar{\varepsilon}_{33}^{x}$, $\dots$), keeping other strain components to "0". By means of the method mentioned above, the obtained stress components could be one column values in the effective stiffness matrix. For instance, if the first strain component is "1" and the rest of them are "0", the calculated stress components are the first column values of matrix. By repeating this calculation for 24 times, the completed effective stiffness matrix can be obtained. As long as the geometry of RVE and elastic constants are unaltered, this effective stiffness matrix is fixed and can be simply applied to determine the internal stresses.

### Numerically efficient microstructure-based calculation of internal stresses in superalloys

Our new method is derived from the RVE with a cubic $\gamma'$ precipitate, and it can extend to the case for a spherical $\gamma'$ precipitate. However, the effective stiffness matrix has to be modified, because the different morphology of precipitate leads to a different stress state in the RVE. For the approx. 40% volume fraction of precipitate and the lattice mismatch ratio of -0.0015, under uniaxial tensile stress of 300 MPa along x-direction, the stress is more concentrated in small areas of the $\gamma$ matrix for the spherical $\gamma'$ precipitate than the cubic one. Furthermore, the values are even higher, as displayed in Fig. 5. This will cause more inhomogeneous deformation in the microstructure. In addition, the stress field in large corner areas around the spherical $\gamma'$ precipitate is considerable. Therefore, the stress state in the whole RVE with a spherical precipitate can not be represented by four regions as simple as the cubic case.

![](./images/813084444159115264_5.jpg)

Figure 5. Full fields of equivalent von Mises stresses in the RVE with a cubic $\gamma'$ precipitate (a) and a spherical $\gamma'$ precipitate (b) under uniaxial tensile load of 300 MPa in x-direction, respectively. The volume fraction of precipitate is approx. 40% and the lattice mismatch ratio is -0.0015. These stresses are calculated by FFT method without the subdivision of regions.

Making use of the same FFT method and Eq. 5 with the same model parameters, the full fields of plastic strains in the RVE with approx. 40% volume fraction of a spherical $\gamma'$ precipitate for different loading conditions in a certain time step are obtained, which are shown in Fig. 6. By analyzing the geometrical symmetry and the similarity of deformation behavior, as well as considering the efficiency and accuracy of the calculation of internal stresses, the RVE with a spherical $\gamma'$ precipitate is divided into 10 regions as shown in Fig. 7. Thus, internal stresses can be calculated by Eq. 9 as

$$
\begin{pmatrix}
\overline{\mathrm{S}}^{\mathrm{INT}1} \\
\overline{\mathrm{S}}^{\mathrm{INT}2} \\
\vdots \\
\overline{\mathrm{S}}^{\mathrm{INT}10}
\end{pmatrix}
=
\begin{pmatrix}
\mathbb{C}_{11}^{\prime\prime} & \mathbb{C}_{12}^{\prime\prime} & \cdots & \mathbb{C}_{110}^{\prime\prime} \\
\mathbb{C}_{21}^{\prime\prime} & \mathbb{C}_{22}^{\prime\prime} & \cdots & \mathbb{C}_{210}^{\prime\prime} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbb{C}_{101}^{\prime\prime} & \mathbb{C}_{102}^{\prime\prime} & \cdots & \mathbb{C}_{1010}^{\prime\prime}
\end{pmatrix}
\cdot
\begin{pmatrix}
\overline{\boldsymbol{\varepsilon}}^{1} \\
\overline{\boldsymbol{\varepsilon}}^{2} \\
\vdots \\
\overline{\boldsymbol{\varepsilon}}^{10}
\end{pmatrix}.
\tag{9}
$$

This is a simplified equation similar to Eq. 7. In fact, the whole effective stiffness matrix contains 60×60 components.

Numerically efficient microstructure-based calculation of internal stresses in superalloys

![](./images/813084444159115264_6.jpg)

Figure 6. Full fields of equivalent plastic strains in 500 time steps in the RVE with a spherical $\gamma'$ precipitate under a constant uniaxial tensile load of 300 MPa along [001] direction (a), [110] direction (b) and [111] direction (c).

![](./images/813084444159115264_7.jpg)

Figure 7. Schematic diagram of subdivision of RVE with a spherical $\gamma'$ precipitate. The numbers indicate different regions.

As the expense of a certain accuracy, the subdivision method overcomes the limit of the computer memory for a long-time full field calculation and increases the efficiency. The subdivisions for two shapes of $\gamma'$ phase proposed in our paper are only two of feasible ways. If the more accurate solution is required, a more complex subdivision can be made by the analysis of specific local stresses and deformations.

### 3. Validation of the effective stiffness matrix

#### 3.1. Comparison of internal stresses

We assume that the volume fraction of $\gamma'$ precipitate is approx. 66% and the total number of FFT grids in the RVE with a cubic $\gamma'$ precipitate is $32{\times}32{\times}32$. Thus, the precipitate occupies $28{\times}28{\times}28$ grids and each channel occupies $28{\times}28{\times}4$ grids. Based on this microstructure and elastic constants [28], the effective stiffness matrix with $24{\times}24$ components can be determined. Since various loading conditions give rise to distinct eigenstrains in the RVE, we assigned many different values to eigenstrains to validate the reliability of Eq. 7 with the effective stiffness matrix. Here, we purposefully

Numerically efficient microstructure-based calculation of internal stresses in superalloys9

take arbitrary large eigenstrains shown in Tab. 2 as an example to demonstrate the generality of our method. The calculated internal stress fields by FFT method are shown in Fig. 8. The corresponding effective values in the four sections of the RVE determined by averaging the FFT results within these regions are listed in Tab. 3. The calculated internal stresses by effective stiffness method are listed in Tab. 4. These internal stresses calculated by two methods are almost equivalent. Tab. 5 shows that the deviation of each stress component in the RVE between two methods, which is the absolute percentage of difference of individual stress component between two methods accounting for the corresponding stress component determined by FFT method. It can be seen that the maximum and average deviations are approx. 5.9% and 0.7%, respectively. Although the maximum difference of individual stress component could be in the order of $10^3$ MPa for these given large eigenstrains, the deviation is small. If the magnitude of eigenstrains decreases, the value of internal stresses will decrease and the maximum difference of internal stresses would be smaller than 10 MPa which is negligible.

When the volume fraction of $\gamma'$ precipitate changes, the average deviation varies a little, but the fluctuation of maximum deviation is larger, as shown in Fig. 9. There is no monotonic regulation between deviations and volume fractions. Nevertheless, these deviations are generally acceptable. Furthermore, if the precipitate is a cuboid, which occupies 28×30×26 grids, the maximum and average deviations are approx. 6.8% and 0.6%, respectively. Therefore, the simple effective stiffness method is valid for calculation of internal stresses in both cubic and cuboid cases with different volume fractions of $\gamma'$ precipitates, and the accuracy increases with decreasing magnitude of eigenstrains.

When we use different elastic constants of $\gamma$ and $\gamma'$ phases [13] to redo the calculation for cubic precipitate with 66% volume fraction, the maximum and average deviations are approx. 2.9% and 0.4%, respectively. This demonstrates that the unequal elastic constants for two phases do not worsen the accuracy of this new method, and the same indication is also found for other volume fractions.

Table 2. Assigned eigenstrains in the four sections of RVE with a cubic $\gamma'$ precipitate.

<table>
  <thead>
    <tr>
      <th>Strain component</th>
      <th>11</th>
      <th>22</th>
      <th>33</th>
      <th>12</th>
      <th>13</th>
      <th>23</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\bar{\bar{\varepsilon}}^x$</td>
      <td>0.7</td>
      <td>0.8</td>
      <td>0.9</td>
      <td>0.8</td>
      <td>0.7</td>
      <td>0.6</td>
    </tr>
    <tr>
      <td>$\bar{\bar{\varepsilon}}^y$</td>
      <td>0.5</td>
      <td>0.4</td>
      <td>0.3</td>
      <td>0.2</td>
      <td>0.1</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\bar{\bar{\varepsilon}}^z$</td>
      <td>1.0</td>
      <td>0.1</td>
      <td>0.2</td>
      <td>0.3</td>
      <td>0.4</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>$\bar{\bar{\varepsilon}}^p$</td>
      <td>0.1</td>
      <td>0.2</td>
      <td>0.3</td>
      <td>0.4</td>
      <td>0.5</td>
      <td>0.6</td>
    </tr>
  </tbody>
</table>

For given arbitrary values of eigenstrains in the 10 sections of the RVE with a spherical $\gamma'$ precipitate as shown in Tab. 6, the maximum and average deviation between FFT method and effective stiffness method are approx. 4.7% and 0.4%, respectively, as displayed in Tab. 7. The influence of volume fractions is shown in Fig. 10. It is found that for volume fraction of 20%, one stress component has a large deviation, however,

Numerically efficient microstructure-based calculation of internal stresses in superalloys 10

![](./images/813084444159115264_8.jpg)

Figure 8. Calculated internal stress fields in the RVE with a cubic $\gamma'$ precipitate by FFT method, where a local internal stress value is defined in every grid point.

Table 3. Effective internal stresses [MPa] in the four sections of RVE with a cubic $\gamma'$ precipitate obtained by averaging FFT results within these regions.

<table>
  <thead>
    <tr>
      <th>Stress component</th>
      <th>11</th>
      <th>22</th>
      <th>33</th>
      <th>12</th>
      <th>13</th>
      <th>23</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\mathbf{S}^{\text{INT}_{\text{X}}}$</td>
      <td>0.351e+04</td>
      <td>-0.108e+06</td>
      <td>-0.111e+06</td>
      <td>-0.657e+04</td>
      <td>-0.114e+05</td>
      <td>-0.508e+04</td>
    </tr>
    <tr>
      <td>$\mathbf{S}^{\text{INT}_{\text{Y}}}$</td>
      <td>-0.372e+05</td>
      <td>0.780e+04</td>
      <td>-0.714e+04</td>
      <td>-0.162e+04</td>
      <td>0.876e+05</td>
      <td>0.827e+04</td>
    </tr>
    <tr>
      <td>$\mathbf{S}^{\text{INT}_{\text{Z}}}$</td>
      <td>-0.103e+06</td>
      <td>-0.172e+05</td>
      <td>0.745e+04</td>
      <td>0.232e+05</td>
      <td>-0.893e+04</td>
      <td>0.415e+04</td>
    </tr>
    <tr>
      <td>$\mathbf{S}^{\text{INT}_{\text{P}}}$</td>
      <td>0.212e+05</td>
      <td>0.191e+05</td>
      <td>0.178e+05</td>
      <td>-0.318e+04</td>
      <td>-0.124e+05</td>
      <td>0.282e+03</td>
    </tr>
  </tbody>
</table>

Table 4. Calculated internal stresses [MPa] in the four sections of RVE with a cubic $\gamma'$ precipitate by effective stiffness method.

<table>
  <thead>
    <tr>
      <th>Stress component</th>
      <th>11</th>
      <th>22</th>
      <th>33</th>
      <th>12</th>
      <th>13</th>
      <th>23</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\mathbf{S}^{\text{INT}_{\text{X}}}$</td>
      <td>0.359e+04</td>
      <td>-0.108e+06</td>
      <td>-0.110e+06</td>
      <td>-0.657e+04</td>
      <td>-0.114e+05</td>
      <td>-0.478e+04</td>
    </tr>
    <tr>
      <td>$\mathbf{S}^{\text{INT}_{\text{Y}}}$</td>
      <td>-0.371e+05</td>
      <td>0.786e+04</td>
      <td>-0.697e+04</td>
      <td>-0.162e+04</td>
      <td>0.878e+05</td>
      <td>0.827e+04</td>
    </tr>
    <tr>
      <td>$\mathbf{S}^{\text{INT}_{\text{Z}}}$</td>
      <td>-0.103e+06</td>
      <td>-0.171e+05</td>
      <td>0.750e+04</td>
      <td>0.234e+05</td>
      <td>-0.893e+04</td>
      <td>0.414e+04</td>
    </tr>
    <tr>
      <td>$\mathbf{S}^{\text{INT}_{\text{P}}}$</td>
      <td>0.213e+05</td>
      <td>0.191e+05</td>
      <td>0.178e+05</td>
      <td>-0.318e+04</td>
      <td>-0.124e+05</td>
      <td>0.279e+03</td>
    </tr>
  </tbody>
</table>

Table 5. The deviation [%] of the internal stresses in the four sections of RVE with a cubic $\gamma'$ precipitate between the results obtained by FFT method and effective stiffness method.

<table>
  <thead>
    <tr>
      <th>Stress component</th>
      <th>11</th>
      <th>22</th>
      <th>33</th>
      <th>12</th>
      <th>13</th>
      <th>23</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\mathbf{D}^{\text{INT}_{\text{X}}}$</td>
      <td>2.3</td>
      <td>0.0</td>
      <td>0.9</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.9</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT}_{\text{Y}}}$</td>
      <td>0.3</td>
      <td>0.8</td>
      <td>2.4</td>
      <td>0.0</td>
      <td>0.2</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT}_{\text{Z}}}$</td>
      <td>0.0</td>
      <td>0.6</td>
      <td>0.7</td>
      <td>0.9</td>
      <td>0.0</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT}_{\text{P}}}$</td>
      <td>0.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>

its absolute difference is only 25 MPa. Furthermore, the assigned eigenstrains in this paper are complex, which may increase the deviation. The calculated internal stresses

Numerically efficient microstructure-based calculation of internal stresses in superalloys 11

![](./images/813084444159115264_9.jpg)

Figure 9. The average and maximum deviations of calculated internal stresses in the
RVE with a cubic $\gamma'$ precipitate between FFT method and effective stiffness method
as a function of volume fractions of $\gamma'$ precipitate.

would be more accurate in the simple deformation case. Hence, the effective stiffness
method is also available to obtain the reasonable results for spherical $\gamma'$ precipitates.

Table 6. Assigned eigenstrains in the 10 sections of RVE with a spherical $\gamma'$ precipitate.

<table>
  <thead>
    <tr>
      <th>Strain component</th>
      <th>11</th>
      <th>22</th>
      <th>33</th>
      <th>12</th>
      <th>13</th>
      <th>23</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\bar{\varepsilon}^{1}$</td>
      <td>0.5</td>
      <td>0.1</td>
      <td>0.5</td>
      <td>0.7</td>
      <td>0.04</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>$\bar{\varepsilon}^{2}$</td>
      <td>-0.1</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>0.8</td>
      <td>0.8</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\bar{\varepsilon}^{3}$</td>
      <td>0.3</td>
      <td>0.4</td>
      <td>-0.4</td>
      <td>0.1</td>
      <td>0.2</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>$\bar{\varepsilon}^{4}$</td>
      <td>0.2</td>
      <td>-0.2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>$\bar{\varepsilon}^{5}$</td>
      <td>0.5</td>
      <td>-0.2</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>$\bar{\varepsilon}^{6}$</td>
      <td>0.2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-0.2</td>
      <td>0.7</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\bar{\varepsilon}^{7}$</td>
      <td>0.3</td>
      <td>0.0</td>
      <td>-0.2</td>
      <td>0.4</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\bar{\varepsilon}^{8}$</td>
      <td>0.0</td>
      <td>0.2</td>
      <td>0.5</td>
      <td>0.05</td>
      <td>-0.6</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\bar{\varepsilon}^{9}$</td>
      <td>0.4</td>
      <td>0.3</td>
      <td>0.4</td>
      <td>0.7</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\bar{\varepsilon}^{10}$</td>
      <td>0.4</td>
      <td>0.4</td>
      <td>0.0</td>
      <td>0.007</td>
      <td>0.3</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>

### 3.2. Comparison of plastic strains

Following the present subdivision and assigning the internal stresses in different regions
obtained by the FFT method or the effective stiffness method to Eq. 5, the plastic
strain in each region in every time step can be calculated. Thus, the general equivalent
plastic strain of RVE is given by

$$
\varepsilon_{\mathrm{g}}=\sum_{i=1}^{m} f_{i} \varepsilon_{i}, \tag{10}
$$

Numerically efficient microstructure-based calculation of internal stresses in superalloys12

Table 7. The deviation [%] of the internal stresses in the 10 sections of RVE with a spherical $\gamma'$ precipitate between the results obtained by FFT method and effective stiffness method.

<table>
  <thead>
    <tr>
      <th>Stress component</th>
      <th>11</th>
      <th>22</th>
      <th>33</th>
      <th>12</th>
      <th>13</th>
      <th>23</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\mathbf{D}^{\text{INT1}}$</td>
      <td>0.0</td>
      <td>0.4</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.2</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT2}}$</td>
      <td>0.6</td>
      <td>0.2</td>
      <td>0.8</td>
      <td>0.2</td>
      <td>0.2</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT3}}$</td>
      <td>4.7</td>
      <td>0.5</td>
      <td>0.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT4}}$</td>
      <td>0.2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.3</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT5}}$</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT6}}$</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.4</td>
      <td>0.1</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT7}}$</td>
      <td>0.4</td>
      <td>0.7</td>
      <td>0.2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT8}}$</td>
      <td>0.4</td>
      <td>0.0</td>
      <td>1.5</td>
      <td>0.9</td>
      <td>0.0</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT9}}$</td>
      <td>0.0</td>
      <td>0.2</td>
      <td>0.0</td>
      <td>0.8</td>
      <td>0.0</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>$\mathbf{D}^{\text{INT10}}$</td>
      <td>2.3</td>
      <td>0.0</td>
      <td>0.7</td>
      <td>0.2</td>
      <td>0.0</td>
      <td>0.1</td>
    </tr>
  </tbody>
</table>

![](./images/813084444159115264_10.jpg)

Figure 10. The average and maximum deviations of calculated internal stresses in the RVE with a spherical $\gamma'$ precipitate between FFT method and effective stiffness method as a function of volume fractions of $\gamma'$ precipitate.

where $f_i$ and $\varepsilon_i$ are the volume fraction and the equivalent plastic strain of each region $i$, respectively, and $m$ is the total number of regions. The used model parameters are the same as that in Tab. 1. Fig. 11 shows that the comparisons of the equivalent plastic strains for different methods in some typical regions of the RVEs with a cubic $\gamma'$ precipitate and a spherical $\gamma'$ precipitate, respectively, which demonstrates that the FFT method and the effective stiffness method almost lead to the same results, where small deviations occur at rather large strains. For [110] and [111] loading conditions, the general equivalent plastic strains obtained by two methods are nearly identical as shown in Fig. 12. These results denote that, in general, the deviation increases with increasing strain. This is consistent with the previous indication that the accuracy of internal stresses calculated by the effective stiffness method decreases with increasing magnitude of eigenstrains. Moreover, the deviation in the case of a cubic precipitate is

Numerically efficient microstructure-based calculation of internal stresses in superalloys
larger than that in the case of a spherical precipitate for the same strain. Due to the more subsections in the RVE with a spherical precipitate, the description of the stress states is improved, so that the precision is enhanced.

![](./images/813084444159115264_11.jpg)

Figure 11. Equivalent plastic strains in the RVE with a cubic $\gamma'$ precipitate (66% volume fraction) (a) and a spherical $\gamma'$ precipitate (40% volume fraction) (b) as a function of the time step under a constant uniaxial tensile load of 300 MPa along [001] direction, obtained by FFT method and effective stiffness method, respectively.

## 4. Application in crystal plasticity finite element model

### 4.1. Crystal plasticity constitutive equations

Based on the dislocation slip controlled phenomenological crystal plasticity model [29], a new flow rule for $\langle 110\rangle\{111\}$ slip in each $\gamma$ matrix channel is

$$
\dot{\gamma}_{\alpha}=\dot{\gamma}_{0}\left|\frac{\tau_{\alpha}+\tau_{\alpha}^{\mathrm{INT}}}{\hat{\tau}_{\alpha}^{\mathrm{slip}}+\tau^{\mathrm{oro}}}\right|^{p_{1}} \operatorname{sign}\left(\tau_{\alpha}+\tau_{\alpha}^{\mathrm{INT}}\right),
\tag{11}
$$

where $\alpha$ represents the slip system, $\dot{\gamma}_{\alpha}$ is the shear rate in a certain slip system, $\dot{\gamma}_{0}$ is the reference shear rate, $\tau^{\text {oro }}$ is the Orowan stress, and $p_{1}$ is the inverse value of the strain

Numerically efficient microstructure-based calculation of internal stresses in superalloys 14

![](./images/813084444159115264_12.jpg)

Figure 12. Comparisons of the general equivalent plastic strains between the results obtained by FFT method and effective stiffness method in the RVE with a cubic $\gamma'$ precipitate (66% volume fraction) (a) and a spherical $\gamma'$ precipitate (40% volume fraction) (b) as a function of the time step under a constant uniaxial tensile load of 300 MPa along [001], [110], and [111] directions, respectively.

rate sensitivity. The resolved shear stress $\tau_{\alpha}$ is given by
$$
\tau_{\alpha}=\frac{\mathbb{C}}{2}\left(\mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}}-\mathbf{I}\right) \cdot \mathbf{M}_{\alpha}, \tag{12}
$$
where $\mathbf{F}_{\mathrm{e}}$ is the elastic deformation gradient, and $\mathbf{M}_{\alpha}$ is the Schmid matrix. The internal stress gives rise to an additional resolved shear stress as
$$
\tau_{\alpha}^{\mathrm{INT}}=\overline{\mathbf{S}}^{\mathrm{INT}} \cdot \mathbf{M}_{\alpha}. \tag{13}
$$
$\hat{\tau}_{\alpha}^{\text{slip}}$ is the slip resistance determined by
$$
\dot{\hat{\tau}}_{\alpha}^{\text{slip}}=\sum_{\beta=1}^{12} h_{0} \chi_{\alpha \beta}\left(1-\frac{\hat{\tau}_{\beta}^{\text{slip}}}{\hat{\tau}^{\text{sat}}}\right)^{p_{2}}\left|\dot{\gamma}_{\beta}\right|, \tag{14}
$$
where $\beta$ is the slip system, $h_{0}$ is the reference hardening parameter, $\chi_{\alpha \beta}$ is the cross hardening matrix, $\hat{\tau}^{\text{sat}}$ is the saturated slip resistance due to dislocation density

Numerically efficient microstructure-based calculation of internal stresses in superalloys15
accumulation, and $p_2$ is a fitting parameter. Due to the shearing of $\gamma'$ precipitate by stacking faults [7, 16], the flow rule for $\langle 112\rangle\{111\}$ slip in $\gamma'$ precipitate is

$$
\dot{\gamma}_{\alpha}=\dot{\gamma}_{0}\left|\frac{\tau_{\alpha}+\tau_{\alpha}^{\mathrm{INT}}}{\hat{\tau}_{\alpha}^{\text {slip }}}\right|^{p_{1}} \operatorname{sign}\left(\tau_{\alpha}+\tau_{\alpha}^{\mathrm{INT}}\right). \tag{15}
$$

Taking the RVE with a cubic $\gamma'$ precipitate as an example, the plastic velocity gradients in the four subsections as discussed above are given by

$$
\mathbf{L}_{\mathrm{p}}^{\mathrm{x}}=\sum_{\alpha=1}^{12} \dot{\gamma}_{\alpha}^{\mathrm{x}} \mathbf{M}_{\alpha}, \tag{16}
$$

$$
\mathbf{L}_{\mathrm{p}}^{\mathrm{y}}=\sum_{\alpha=1}^{12} \dot{\gamma}_{\alpha}^{\mathrm{y}} \mathbf{M}_{\alpha}, \tag{17}
$$

$$
\mathbf{L}_{\mathrm{p}}^{\mathrm{z}}=\sum_{\alpha=1}^{12} \dot{\gamma}_{\alpha}^{\mathrm{z}} \mathbf{M}_{\alpha}, \tag{18}
$$

$$
\mathbf{L}_{\mathrm{p}}^{\mathrm{p}}=\sum_{\alpha=1}^{12} \dot{\gamma}_{\alpha}^{\mathrm{p}} \mathbf{M}_{\alpha}. \tag{19}
$$

With the known plastic deformation gradient in the previous time step, the current plastic deformation gradients for different regions are

$$
\mathbf{F}_{\mathrm{p}}^{\mathrm{x}(t)}=\left(\mathbf{I}+\mathbf{L}_{\mathrm{p}}^{\mathrm{x}} \cdot \Delta t\right) \mathbf{F}_{\mathrm{p}}^{\mathrm{x}(t-\Delta t)}, \tag{20}
$$

$$
\mathbf{F}_{\mathrm{p}}^{\mathrm{y}(t)}=\left(\mathbf{I}+\mathbf{L}_{\mathrm{p}}^{\mathrm{y}} \cdot \Delta t\right) \mathbf{F}_{\mathrm{p}}^{\mathrm{y}(t-\Delta t)}, \tag{21}
$$

$$
\mathbf{F}_{\mathrm{p}}^{\mathrm{z}(t)}=\left(\mathbf{I}+\mathbf{L}_{\mathrm{p}}^{\mathrm{z}} \cdot \Delta t\right) \mathbf{F}_{\mathrm{p}}^{\mathrm{z}(t-\Delta t)}, \tag{22}
$$

$$
\mathbf{F}_{\mathrm{p}}^{\mathrm{p}(t)}=\left(\mathbf{I}+\mathbf{L}_{\mathrm{p}}^{\mathrm{p}} \cdot \Delta t\right) \mathbf{F}_{\mathrm{p}}^{\mathrm{p}(t-\Delta t)}, \tag{23}
$$

and the total plastic deformation gradient $\mathbf{F}_{\mathrm{p}}$ is calculated by

$$
\mathbf{F}_{\mathrm{p}}^{(t)}=\left(\mathbf{I}+\left(f^{\mathrm{x}} \cdot \mathbf{L}_{\mathrm{p}}^{\mathrm{x}}+f^{\mathrm{y}} \cdot \mathbf{L}_{\mathrm{p}}^{\mathrm{y}}+f^{\mathrm{z}} \cdot \mathbf{L}_{\mathrm{p}}^{\mathrm{z}}+f^{\mathrm{p}} \cdot \mathbf{L}_{\mathrm{p}}^{\mathrm{p}}\right) \cdot \Delta t\right) \mathbf{F}_{\mathrm{p}}^{(t-\Delta t)}, \tag{24}
$$

where $f^{\mathrm{x}}$, $f^{\mathrm{y}}$, $f^{\mathrm{z}}$, and $f^{\mathrm{p}}$ are volume fractions of each $\gamma$ channel and precipitate, respectively. $\Delta t$ is the time step. The eigenstrains in each subsection originated from the plastic deformation gradients are

$$
\overline{\boldsymbol{\varepsilon}}^{\mathrm{x}}=\frac{1}{2}\left(\mathbf{F}_{\mathrm{p}}^{\mathrm{xT}} \mathbf{F}_{\mathrm{p}}^{\mathrm{x}}-\mathbf{I}\right), \tag{25}
$$

$$
\overline{\boldsymbol{\varepsilon}}^{\mathrm{y}}=\frac{1}{2}\left(\mathbf{F}_{\mathrm{p}}^{\mathrm{yT}} \mathbf{F}_{\mathrm{p}}^{\mathrm{y}}-\mathbf{I}\right), \tag{26}
$$

$$
\overline{\boldsymbol{\varepsilon}}^{\mathrm{z}}=\frac{1}{2}\left(\mathbf{F}_{\mathrm{p}}^{\mathrm{zT}} \mathbf{F}_{\mathrm{p}}^{\mathrm{z}}-\mathbf{I}\right), \tag{27}
$$

$$
\overline{\boldsymbol{\varepsilon}}^{\mathrm{p}}=\frac{1}{2}\left(\mathbf{F}_{\mathrm{p}}^{\mathrm{pT}} \mathbf{F}_{\mathrm{p}}^{\mathrm{p}}-\mathbf{I}\right)+\delta \mathbf{I}. \tag{28}
$$

The internal stresses can be determined from these eigenstrains at each time step by Eq. 7 efficiently. The same method is able to be used for the RVE with a spherical $\gamma'$ precipitate.

Numerically efficient microstructure-based calculation of internal stresses in superalloys 16

### 4.2. Finite element model
The crystal plasticity constitutive equations are able to be implemented in the ABAQUS [30] platform by using a user-defined subroutine UMAT. A simple 3D finite element (FE) model with dimensions of 80 mm × 40 mm × 40 mm is set up to represent a sample of single crystal superalloys. As shown in Fig. 13, the 1/8 complete sample is discretized with 2000 regular C3D8 elements, in which each integration point is represented by the previous RVE. The symmetric boundary conditions are applied in x-, y-, z-direction, respectively. The common model parameters are shown in Tab. 8. According to different shapes and volume fractions of $\gamma'$ precipitate, as well as different $\gamma$ channel widths, $\tau^{\text{oro}}$ can be determined by the Orowan threshold equations proposed in [13, 31]. Assuming the volume fraction of $\gamma'$ precipitate is 40% and the length of the RVE is 500 nm, the Orowan stresses are 71 MPa and 22 MPa for cubic $\gamma'$ and spherical $\gamma'$ precipitates, respectively.

Loading in z-direction (i.e., [001] crystallographic orientation) with a constant stress of 300 MPa for $1.0\times10^{5}$ s, the sample deforms almost homogeneously and the plastic strain evolving with time is displayed in Fig. 14. Since the internal stresses in the whole sample are nearly same, we select one arbitrary element to show the evolution of internal stresses during the deformation. For the cubic $\gamma'$ precipitate, from Fig. 15(a), it can be seen that the internal stresses in $\gamma$ channels decrease in the beginning and increase gradually afterwards, but the internal stress in the precipitate increases continuously. Initially, the internal stresses are determined by the lattice mismatch. The following deformation accommodates the misfit strain first, so that the high internal stresses in channels decrease. This is also observed in the full field calculation shown in Fig. 1(b). However, when they reach certain values, they will increase again, because the further accumulation of deformation in the microstructure will cause the increase of internal stresses. In addition, due to the high strength of $\gamma'$ precipitate, the inhomogeneous deformation in the channels and the precipitate leads to increasing internal stresses. The previous deformation state determines the current internal stresses, the current internal stresses influence the further deformation as well. The similar phenomenon of internal stresses during the creep in the superalloy has been discussed in [32]. For the spherical $\gamma'$ precipitate, the evolution of internal stresses is shown in Fig. 15(b). It is found that the different shapes of $\gamma'$ precipitates result in different internal stresses which give rise to different plastic strains. Our method can discriminate the influence of the various shapes of $\gamma'$ precipitate on deformation behavior for the same volume fraction.

The present FE model is one simple application of our effective stiffness method. The detailed analysis of deformation in this model is not the focus of this paper. In the future, the effective stiffness method can be used in more complex and more realistic models, in which the simulation results are able to rationalize the experimental observations.

Numerically efficient microstructure-based calculation of internal stresses in superalloys 17

![](./images/813084444159115264_13.jpg)

Figure 13. The 1/8 3D finite element model with boundary conditions.

Table 8. Crystal plasticity model parameters. $\hat{\tau}_{0}^{\text{slip}}$ is the initial slip resistance.

<table>
  <thead>
    <tr>
      <th>$\dot{\gamma}_{0}$ [$\text{s}^{-1}$]</th>
      <td>$4.0 \times 10^{-6}$</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>$\hat{\tau}_{0}^{\text{slip}} \langle 110 \rangle \{ 111 \}$ [MPa]</th>
      <td>60</td>
    </tr>
    <tr>
      <th>$\hat{\tau}_{0}^{\text{slip}} \langle 112 \rangle \{ 111 \}$ [MPa]</th>
      <td>500</td>
    </tr>
    <tr>
      <th>$p_1$</th>
      <td>10</td>
    </tr>
    <tr>
      <th>$p_2$</th>
      <td>0.05</td>
    </tr>
    <tr>
      <th>$h_0$ [MPa]</th>
      <td>60</td>
    </tr>
    <tr>
      <th>$\hat{\tau}^{\text{sat}}$ [MPa]</th>
      <td>800</td>
    </tr>
    <tr>
      <th>$\chi_{\alpha \beta}$ coplanar$\{111\}$</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>$\chi_{\alpha \beta}$ non-coplanar$\{111\}$</th>
      <td>1.4</td>
    </tr>
    <tr>
      <th>$\delta$</th>
      <td>-0.0015</td>
    </tr>
  </tbody>
</table>

## 5. Conclusions

On the basis of typical $\gamma/\gamma'$ microstructures of superalloys, the internal stresses due to eigenstrains resulting from lattice mismatch and deformation heterogeneity can be calculated by an efficient linear relation with an effective stiffness matrix. The effective stiffness method can be considered as a generalization of the Eshelby inclusion problem for more complex microstructures. It relies on a subdivision of the microstructure into regions with uniform deformation behavior. The feasibility of such a subdivision has been demonstrated for $\gamma/\gamma'$ microstructures with cubic and spherical precipitates. Compared with direct simulations with the Fast Fourier Transformation (FFT) method, which determines the internal stress fields with the full spatial resolution, this simplified method is numerically much more efficient and thus well suitable for applications in macroscopic simulations of deformation and creep with finite element method or other mechanics solvers. The effective stiffness matrix is calculated by the FFT method and

Numerically efficient microstructure-based calculation of internal stresses in superalloys 18

![](./images/813084444159115264_14.jpg)

Figure 14. The plastic strain as a function of time under uniaxial tensile load of 300 MPa in z-direction for single crystal superalloys with cubic $\gamma'$ and spherical $\gamma'$ precipitates, respectively.

![](./images/813084444159115264_15.jpg)

Figure 15. The von Mises internal stresses in one element for the cubic $\gamma'$ precipitate (a) and the spherical $\gamma'$ precipitate (b) as a function of time under uniaxial tensile load of 300 MPa in z-direction.

its dimension varies with different morphologies of $\gamma'$ precipitates. The accuracy of this method increases with decreasing magnitude of eigenstrains, but it is not significantly influenced by the volume fraction of $\gamma'$ precipitate and elastic constants. Furthermore, if the volume fraction and shape of $\gamma'$ phase in superalloys remain unchanged during the deformation, the effective stiffness matrix will be constant throughout the simulation.

Numerically efficient microstructure-based calculation of internal stresses in superalloys 19

## 6. Acknowledgments

The authors are grateful for funding by the Deutsche Forschungsgemeinschaft (DFG) through Project C4 of the collaborative research center SFB/Transregio 103 superalloy single crystals under grant number INST 213/747-2.

## 7. References

[1] T.M. Pollock and A.S. Argon. Creep resistance of CMSX-3 nickel base superalloy single crystals. Acta Metallurgica et Materialia, 40:1-30, 1992.

[2] J.X. Zhang, T. Murakumo, H. Harada, Y. Koizumi, and T. Kobayashi. Creep deformation mechanisms in some modern single-crystal superalloys. Superalloys 2004, pages 189-195, 2004.

[3] C.M.F. Rae and R.C. Reed. Primary creep in single crystal superalloys: Origins, mechanisms and effects. Acta Materialia, 55:1067-1081, 2007.

[4] G. Eggeler and A. Dlouhy. On the formation of <010>-dislocations in the $\gamma'$-phase of superalloy single crystals during high temperature low stress creep. Acta Materialia, 45:4251-4262, 1997.

[5] V. Sass and M. Feller-Kniepmeier. Orientation dependence of dislocation structures and deformation mechanisms in creep deformed CMSX-4 single crystals. Materials Science and Engineering A, 245:19-28, 1998.

[6] L. Agudo Jácome, P. Nörtershäuser, J.K. Heyer, A. Lahni, J. Frenzel, A. Dlouhy, C. Somsen, and G. Eggeler. High-temperature and low-stress creep anisotropy of single-crystal superalloys. Acta Materialia, 61:2926-2943, 2013.

[7] D.M. Knowles and S. Gunturi. The role of $\langle 112\rangle\{111\}$ slip in the asymmetric nature of creep of single crystal superalloy CMSX-4. Materials Science and Engineering A, 328:223-237, 2002.

[8] S. Gao, M. Fivel, A. Ma, and A. Hartmaier. 3D discrete dislocation dynamics study of creep behavior in Ni-base single crystal superalloys by a combined dislocation climb and vacancy diffusion model. Journal of the Mechanics and Physics of Solids, 102:209-223, 2017.

[9] R.C. Reed. The superalloys: fundamentals and applications. Cambridge University Press, 2008.

[10] M. Kamaraj, C. Mayr, M. Kolbe, and G. Eggeler. On the influence of stress state on rafting in the single crystal superalloy CMSX-6 under conditions of high temperature and low stress creep. Scripta Materialia, 38:589-594, 1998.

[11] L. Müller, U. Glatzel, and M. Feller-Kniepmeier. Calculation of the internal stresses and strains in the microstructure of a single crystal nickel-base superalloy during creep. Acta Metallurgica et Materialia, 41(12):3401-3411, 1993.

[12] T. Ichitsubo, D. Koumoto, M. Hirao, K. Tanaka, M. Osawa, T. Yokokawa, and H. Harada. Rafting mechanism for Ni-base superalloy under external stress: elastic or elasticplastic phenomena? Acta Materialia, 51:4033-4044, 2003.

[13] S. Gao, M. Fivel, A. Ma, and A. Hartmaier. Influence of misfit stresses on dislocation glide in single crystal superalloys: A three-dimensional discrete dislocation dynamics study. Journal of the Mechanics and Physics of Solids, 76:276-290, 2015.

[14] S. Gao, M.K. Rajendran, M. Fivel, A. Ma, O. Shchyglo, A. Hartmaier, and I. Steinbach. Primary combination of phase-field and discrete dislocation dynamics methods for investigating athermal plastic deformation in various realistic Ni-base single crystal superalloy microstructures. Modelling and Simulation in Materials Science and Engineering, 23:075003, 2015.

[15] J. Svoboda and P. Lukáš. Modelling of recovery controlled creep in nickel-base superalloy single crystals. Acta Materialia, 45:125-135, 1997.

[16] B. Fedelich. A microstructure based constitutive model for the mechanical behavior at high temperatures of nickel-base single crystal superalloys. Computational Materials Science, 16:248-258, 1999.

[17] B. Fedelich. A microstructural model for the monotonic and the cyclic mechanical behavior of

Numerically efficient microstructure-based calculation of internal stresses in superalloys20

single crystals of superalloys at high temperatures. *International Journal of Plasticity*, 18:1–49, 2002.

[18] J.D. Eshelby. The determination of the elastic field of an ellipsoidal inclusion, and related problems. *Proceedings of the Royal Society A*, 241:376–396, 1957.

[19] J.D. Eshelby. Elastic inclusions and inhomogeneities. *Progress in Solid Mechanics*, pages 89–140, 1961.

[20] S.-B. Lee, R.A. Lebensohn, and A.D. Rollett. Modeling the viscoplastic micromechanical response of two-phase materials using Fast Fourier Transforms. *International Journal of Plasticity*, 27(5):707–727, 2011.

[21] P. Eisenlohr, M. Diehl, R.A. Lebensohn, and F. Roters. A spectral method solution to crystal elasto-viscoplasticity at finite strains. *International Journal of Plasticity*, 46:37–53, 2013.

[22] T.W.J. de Geus, J. Vondřejc, J. Zeman, R.H.J. Peerlings, and M.G.D. Geers. Finite strain FFT-based non-linear solvers made simple. *Computer Methods in Applied Mechanics and Engineering*, 318:412–430, 2017.

[23] J. Svoboda and P. Lukáš. Creep deformation modelling of superalloy single crystals. *Acta Materialia*, 48:2519–2528, 2000.

[24] A. Ma, D. Dye, and R. C. Reed. A model for the creep deformation behaviour of single-crystal superalloy CMSX-4. *Acta Materialia*, 56:1657–1670, 2008.

[25] J.C. Michel, H. Moulinec, and P. Suquet. A computational method based on augmented lagrangians and fast Fourier transforms for composites with high contrast. *CMES(Computer Modelling in Engineering & Sciences)*, 1:79–88, 2000.

[26] J.C. Michel, H. Moulinec, and P. Suquet. A computational scheme for linear and non-linear composites with arbitrary phase contrast. *International Journal for Numerical Methods in Engineering*, 52:139–160, 2001.

[27] R.A. Lebensohn. N-site modeling of a 3D viscoplastic polycrystal using fast Fourier transform. *Acta Materialia*, 49:2723–2737, 2001.

[28] K. Demtröder, G. Eggeler, and J. Schreuer. Influence of microstructure on macroscopic elastic properties and thermal expansion of nickel-base superalloys ERBO/1 and LEK94. *Materialwissenschaft und Werkstofftechnik*, 46(6):563–576, 2015.

[29] F. Roters, P. Eisenlohr, L. Hantcherli, D.D. Tjahjanto, T.R. Bieler, and D. Raabe. Overview of constitutive laws, kinematics, homogenization and multiscale methods in crystal plasticity finite-element modeling: Theory, experiments, applications. *Acta Materialia*, 58(4):1152–1211, 2010.

[30] *ABAQUS/Analysis users Manual.* Version 6.11. ABAQUS Inc.

[31] G.E. Dieter. *Mechanical Metallurgy*. McGraw Hill Inc, U.S.A., 1986.

[32] T. Kuttner and R.P. Wahi. Modelling of internal stress distribution and deformation behaviour in the precipitation hardened superalloy SC16. *Materials Science and Engineering A*, 242(1):259–267, 1998.