# Optical distortion evaluation of an aerodynamically heated window using the interfacial fluid thickness concept

Haosu Xiao,* Zhile Wang, and Zhigang Fan

Research Center for Space Optical Engineering, P.O. Box 307, Harbin Institute of Technology, Harbin 150001, China

*Corresponding author: xiaohaosu1985@gmail.com

Received 10 January 2011; revised 10 April 2011; accepted 2 May 2011;
posted 6 May 2011 (Doc. ID 140797); published 21 June 2011

The interfacial fluid thickness (IFT) concept was used to develop a harmonic-mean refractive index gradient magnitude threshold to retrieve the high refractive index gradient regions of an aerodynamically heated window. The retrieved high-gradient regions were used to reconstruct the refractive index field of the window. The numerical three-dimensional optical distortion evaluation was conducted for both the reconstructed and the original refractive index fields of the window using the ray-tracing program based on a recursive algorithm. Wave aberration results show that the methodology based on the IFT concept reduces the refractive index information required to capture the essential optical distortion of the window. The method can also be used for numerically evaluating the optical distortion of the window. © 2011 Optical Society of America

OCIS codes: 080.2710, 110.3000, 080.2720, 000.4430.

## 1. Introduction
In an aerodynamic thermal environment, an aircraft window is subjected to an aerodynamic flow field that heats the outside surface of the window. The temperature of the window then rises rapidly and forms a gradient distribution due to aerodynamic heating. Both the aerodynamic heating and the strong incoming flow pressure alter the shape of the window, causing deformation and bending. These factors also lead to the refractive index field of the window forming a gradient distribution as a result of the thermo-optical and elasto-optical effects. Recently, there has been increasing interest in the aero-optical issues in the interfacial fluid thickness (IFT) concept applied to the optical distortion evaluation of gradient media, such as highly compressible shear layers and turbulence [1–4]. The IFT was suggested by Catrakis and Aguirre, who saw it as the physical thickness of the refractive fluid interfaces in determining the variation in the optical path length (OPL) of the gradient refractive fluid field [1]. The refractive fluid interfaces physically exhibit a thickness given by the inverse of the refractive index gradient magnitude [1]. Therefore, the IFT is defined as the inverse of the refractive index gradient magnitude [1]. Catrakis and co-workers, using the IFT approach, provided an innovative viewpoint in relating aero-optical distortion to the compressible turbulence structure in terms of the IFT variations [1–3]. Wu *et al.*, using a refractive index gradient magnitude threshold based on the IFT concept to retrieve the high refractive index gradient regions of a hypersonic turbulent flow, showed that these regions are the main cause of the aero-optical distortion in the hypersonic turbulent flow [4]. So far, the IFT concept has only been applied to the in-plane, aero-optical distortion evaluation of a two-dimensional gradient refractive fluid field [1–4]. Far too little attention has been given to its relevance in the

0003-6935/11/193135-10$15.00/0
© 2011 Optical Society of America

1 July 2011 / Vol. 50, No. 19 / APPLIED OPTICS 3135

three-dimensional optical distortion evaluation of the aerodynamically heated window.

This paper focuses on numerically evaluating the three-dimensional optical distortion of the aerodynamically heated window using the IFT concept. A numerical simulation of a standard zinc sulfide window is used to show the validity of the evaluation method.

## 2. Window Analysis
The refractive index grid model of the window is shown in Fig. 1. To obtain a precise calculation, the inhomogeneous refractive index distribution of the window was uniformly divided into 80, 80, and 8 fractions for the $x$, $y$, and $z$ directions, respectively. There were 51,200 hexahedral grids and 59,049 nodes in the grid model. The location of the beam transmission was fixed at the center of the outside surface of the window. For ease of analysis, the medium inside each hexahedral grid was assumed to be uniform and isotropic; hence, the temperature, thermal strain, deformation, and refractive index inside each hexahedral grid were assumed to be uniform, as well. However, the respective temperature, thermal strain, deformation, and refractive index of the eight nodes of each hexahedral grid were assumed to be nonuniform.

### A. Thermo-Optical Effect of the Window
The change in the refractive index of a crystal produced by a temperature field is known as the thermo-optical effect. For an arbitrary node in the refractive index grid model of the window, its refractive index, $n(\lambda, T)$, is as follows [5]:

$$
n(\lambda, T)=n(\lambda, T_{0})+\Delta n_{T}=n(\lambda, T_{0})+\frac{\partial n(\lambda, T)}{\partial T} \Delta T,
\tag{1}
$$

where $n(\lambda, T_{0})$ is the refractive index of the arbitrary node at the reference temperature $T_{0}$, $\Delta n_{T}$ is the refractive index variation caused by the thermo-optical effect, $\frac{\partial n(\lambda, T)}{\partial T}$ is the thermo-optical coefficient, and $\Delta T$ is the temperature variation of the arbitrary node.

![](./images/811653167887417345_1.jpg)

Fig. 1. (Color online) Refractive index grid model of the window.

### B. Elasto-Optical Effect of the Window
The change in the refractive index of a crystal caused by strain or stress is called the elasto-optical effect [6]. Thermal strain or stress changes the optical properties of the window by modifying its dielectric impermeability tensor in the aerodynamic thermal environment. Variation in the dielectric impermeability tensor results in changes in the refractive index of the window.

The window is made up of standard zinc sulfide crystals. Standard zinc sulfide belongs to the cubic crystal system. In the principal axis system, its indicatrix can be expressed as [6]

$$
B_{11} x_{1}^{2}+B_{22} x_{2}^{2}+B_{33} x_{3}^{2}=1,
\tag{2}
$$

where $x_{1}, x_{2}$, and $x_{3}$ are the principal axes, with $x_{3}$ as the optical axis of the cubic crystal; and $B_{11}, B_{22}$, and $B_{33}$ are the diagonal components of the dielectric impermeability tensor $B$ of the cubic crystal system. $B_{11}, B_{22}$, and $B_{33}$ are related to the refractive index of the standard zinc sulfide $(n_{0})$, expressed as [6]

$$
B_{11}=B_{22}=B_{33}=n_{0}^{-2}.
\tag{3}
$$

As indicated in Eqs. (2) and (3), the indicatrix of the cubic crystal system is a sphere. According to the elasto-optical coefficient tensor of the cubic crystal system, the variation of the dielectric impermeability tensor can be expressed as [6]

$$
\begin{aligned}
\Delta B & =\left[\begin{array}{l}
B_{11}^{\prime}-B_{11} \\
B_{22}^{\prime}-B_{22} \\
B_{33}^{\prime}-B_{33} \\
B_{23}^{\prime}-B_{23} \\
B_{31}^{\prime}-B_{31} \\
B_{12}^{\prime}-B_{12}
\end{array}\right] \\
& =\left[\begin{array}{cccccc}
P_{11} & P_{12} & P_{12} & 0 & 0 & 0 \\
P_{12} & P_{11} & P_{12} & 0 & 0 & 0 \\
P_{12} & P_{12} & P_{11} & 0 & 0 & 0 \\
0 & 0 & 0 & P_{44} & 0 & 0 \\
0 & 0 & 0 & 0 & P_{44} & 0 \\
0 & 0 & 0 & 0 & 0 & P_{44}
\end{array}\right]\left[\begin{array}{l}
\varepsilon_{11} \\
\varepsilon_{22} \\
\varepsilon_{33} \\
\gamma_{23} \\
\gamma_{31} \\
\gamma_{12}
\end{array}\right],(4)
\end{aligned}
$$

where $P_{11}, P_{12}$, and $P_{44}$ are the elasto-optical coefficients; and $\varepsilon_{11}, \varepsilon_{22}, \varepsilon_{33}, \gamma_{23}, \gamma_{31}$, and $\gamma_{12}$ are the strains parallel to the different principal axes.

As shown by Eqs. (2)-(4), the indicatrix of a standard zinc sulfide crystal is no longer a sphere because it has been subjected to strain. Accordingly, the crystal becomes biaxial. The refractive index variations caused by the elasto-optical effect can then be expressed as

$$
\begin{aligned}
\Delta n_{11} & =n_{11}^{\prime}-n_{11}=\left(B_{11}^{\prime}\right)^{-1 / 2}-B_{11}^{-1 / 2} \\
& \approx-0.5 n_{0}^{3}\left(P_{11} \varepsilon_{11}+P_{12} \varepsilon_{22}+P_{12} \varepsilon_{33}\right), \\
\Delta n_{22} & =n_{22}^{\prime}-n_{22}=\left(B_{22}^{\prime}\right)^{-1 / 2}-B_{22}^{-1 / 2} \\
& \approx-0.5 n_{0}^{3}\left(P_{12} \varepsilon_{11}+P_{11} \varepsilon_{22}+P_{12} \varepsilon_{33}\right), \\
\Delta n_{33} & =n_{33}^{\prime}-n_{33}=\left(B_{33}^{\prime}\right)^{-1 / 2}-B_{33}^{-1 / 2} \\
& \approx-0.5 n_{0}^{3}\left(P_{12} \varepsilon_{11}+P_{12} \varepsilon_{22}+P_{11} \varepsilon_{33}\right), \\
\Delta n_{23} & =n_{23}^{\prime}-n_{23}=\left(B_{23}^{\prime}\right)^{-1 / 2}-B_{23}^{-1 / 2} \approx-0.5 n_{0}^{3} P_{44} \gamma_{23}, \\
\Delta n_{31} & =n_{31}^{\prime}-n_{31}=\left(B_{31}^{\prime}\right)^{-1 / 2}-B_{31}^{-1 / 2} \approx-0.5 n_{0}^{3} P_{44} \gamma_{31}, \\
\Delta n_{12} & =n_{12}^{\prime}-n_{12}=\left(B_{12}^{\prime}\right)^{-1 / 2}-B_{12}^{-1 / 2} \approx-0.5 n_{0}^{3} P_{44} \gamma_{12},
\end{aligned}
$$

where $\Delta n_{11}$, $\Delta n_{22}$, $\Delta n_{33}$, $\Delta n_{23}$, $\Delta n_{31}$, and $\Delta n_{12}$ are the refractive index variations of light rays propagating in the crystal, whose electric vectors oscillate parallel to the different principal axes.

### C. Harmonic-Mean Refractive Index Gradient Magnitude Threshold of the Window
As discussed by Catrakis and Aguirre [1], the IFT of an arbitrary node in the refractive index grid model of the window, $h_i(x,y,z)$, is defined as the inverse of its nonzero refractive index gradient magnitude, expressed as [1]
$$
h_{i}(x, y, z)=1 /\left|\nabla n_{i}(x, y, z)\right|, \quad(6)
$$
where $|\nabla n_i(x,y,z)|$ is the nonzero refractive index gradient magnitude of the arbitrary node.

The average IFT of the window, $h_T$, can be expressed as [4]
$$
h_{T}=\sum_{i=1}^{N} h_{i} / N, \quad(7)
$$
where $N$ is the number of nodes whose refractive index gradient magnitudes are nonzero.

The refractive index gradient magnitude threshold of the window, $G_T$, is related to the average IFT and is expressed as [4]
$$
\begin{aligned}
G_{T} & =1 / h_{T}=N /\left(\sum_{i=1}^{N} h_{i}\right) \\
& =N /\left[\sum_{i=1}^{N}\left(1 /\left|\nabla n_{i}(x, y, z)\right|\right)\right].
\end{aligned}
$$

As indicated in Eq. (8), the threshold is the harmonic mean for all the nonzero refractive index gradient magnitudes of the window. The harmonic-mean threshold can specifically reflect the influence exerted by the nodes with small refractive index gradient magnitudes on the refractive index distribution of the window [4].

### 3. Optical Transmission of the Window
The optical transmission of the window was simulated using a ray-tracing program based on a recursive algorithm [7]. The rays transmitted grid by grid in the refractive index grid model of the window. The rays transmitted in straight lines inside the grids but were refracted when transmitting through the grid surfaces. Therefore, the optical path of each ray transmitting through the window was separated by the refractive index grids of the window. Figure 2 shows one discrete optical path $(PP_1)$ of an arbitrary ray in a refractive index grid of the window [8]. The arbitrary ray was refracted on the top and bottom surfaces of the grid, whereas it transmitted in a straight line inside the grid. The OPL of this ray was obtained by summing up all the discrete optical paths over the entire path of this ray. The refractive index of point $P$ was evaluated in each step of the algorithm using the refractive indices of the eight nodes (i.e., $G_1$, $G_2$, $G_3$, $G_4$, $G_5$, $G_6$, $G_7$, and $G_8$) of the refractive index grid (Fig. 2). The refractive index of point $P$ was obtained by [9]
$$
\begin{gathered}
n_{P}=\left[\sum_{i=1}^{8}\left(n_{i} \prod_{\substack{j=1 \\
j \neq i}}^{8} d_{j}\right)\right] /\left[\sum_{i=1}^{8}\left(\prod_{\substack{j=1 \\
j \neq i}}^{8} d_{j}\right)\right], \\
d_{j}=\left[\left(x_{P}-x_{j}\right)^{2}+\left(y_{P}-y_{j}\right)^{2}+\left(z_{P}-z_{j}\right)^{2}\right]^{1 / 2},
\end{gathered}
$$
where
- $n_P$ is the refractive index of point $P$,
- $n_i$ is the refractive index of the node $G_i$ of the refractive index grid ($i=1,2,3,...,8$),
- $d_j$ is the spatial distance from point $P$ to the node $G_j$ of the refractive index grid ($j=1,2,3,...,8$),
- $x_P$, $y_P$, and $z_P$ are the coordinates of point $P$, and
- $x_j$, $y_j$, and $z_j$ are the coordinates of the node $G_j$ of the refractive index grid ($j=1,2,3,...,8$).

![](./images/811653167887417345_2.jpg)

Fig. 2. Discrete optical path in a refractive index grid of the window. $P$ is the point of propagation in the optical path $PP_1$. The cubic is the closest refractive index grid encircling $P$. $G_1$, $G_2$, $G_3$, $G_4$, $G_5$, $G_6$, $G_7$, and $G_8$ are the nodes of the refractive index grid. The $z$ axis is parallel to the $z$ direction of the window.

The diameters of the incident beam and exit pupil of the window were 80 and 60 mm, respectively. Incident angles were defined with respect to the window, as in Fig. 3. The location of the lower left corner of the window specified the origin of the coordinate system. The azimuth incident angle was measured relative to the x axis. In the plot, the azimuth incident angle increased in a counterclockwise direction, with 0° at the x axis. The elevation incident angle increased toward the z axis in a counterclockwise direction, with 90° at the z axis. The optical transmission axis was aligned with the z axis.

### A. Fitting the Deformed Surfaces of the Window Using the Least Square Method

The window was deformed in the aerodynamic thermal environment. Thus, only the coordinates of the nodes on the deformed surfaces could be obtained from the refractive index grid model [10]. Using the least square method, the deformed surfaces of the window should be fitted to obtain the normal vectors of the deformed surfaces while tracing the rays on the surfaces [10].

As illustrated in Fig. 4, the normal vector $\mathbf{n}$ of the deformed surface grid encircling the intersection point $E$ can be computed using the least square method based on the coordinates of the four nodes (i.e., $A'$, $B'$, $C'$, and $D'$) [10]. The direction vector of the refractive ray can then be computed according to Snell's optical law of refraction [10].

### B. Optical Distortion Evaluation of the Window

For an arbitrary ray transmitting through the window, its OPL at the $i$th step of the ray-tracing procedure can be expressed as [8,10]

$$
\begin{aligned}
\mathrm{OPL}_{i}=& \int_{T_{0}}^{T_{0}+\Delta T}\left(n_{i} \frac{\partial l_{i}}{\partial T}+l_{i} \frac{\partial n_{i}}{\partial T}\right) \mathrm{d} T \\
&+\int_{\varepsilon_{0}}^{\varepsilon_{0}+\Delta \varepsilon}\left(n_{i} \frac{\partial l_{i}}{\partial \varepsilon}+l_{i} \frac{\partial n_{i}}{\partial \varepsilon}\right) \mathrm{d} \varepsilon,
\end{aligned} \quad(10)
$$

where

![](./images/811653167887417345_3.jpg)

Fig. 3. Definitions of the azimuth and elevation incident angles. The curved arrows indicate positive angles.

![](./images/811653167887417345_4.jpg)

Fig. 4. Ray tracing on the deformed surface of the window.$A'$, $B'$, $C'$, and $D'$ are the nodes of the deformed surface grid encircling intersection point $E$ of the incident ray and the deformed surface. $A$, $B$, $C$, and $D$ are also the counterparts of the nondeformed surface grid encircling intersection point $E$.

$l_i$ is the actual distance traversed by the ray at the $i$th step,
$n_i$ is the refractive index of the point of propagation evaluated at the $i$th step,
$\frac{\partial l_{i}}{\partial T}$ is the thermal expansion coefficient,
$\frac{\partial n_{i}}{\partial T}$ is the thermo-optical coefficient,
$\varepsilon$ is the strain,
$\frac{\partial l_{i}}{\partial \varepsilon}$ is the deformation caused by the strain, and
$\frac{\partial n_{i}}{\partial \varepsilon}$ is the elasto-optical coefficient.

The entire OPL of this ray can be expressed as [10]

$$
\mathrm{OPL}=\sum_{i} \mathrm{OPL}_{i}. \quad(11)
$$

The wave aberration of an arbitrary ray transmitting through the window can be expressed as [10]

$$
W_{k}(x, y)=\frac{2 \pi}{\lambda}\left(\mathrm{OPL}_{k}-\mathrm{OPL}_{0}\right), \quad(12)
$$

where $\mathrm{OPL}_{k}$ is the entire OPL of the arbitrary ray transmitting through the window, and $\mathrm{OPL}_{0}$ is the ensemble averaged OPL, expressed as [10]

$$
\mathrm{OPL}_{0}=\frac{1}{N_{r}} \sum_{k} \mathrm{OPL}_{k} \quad(13)
$$

where $N_r$ is the number of rays transmitting through the window.

The wave aberration of the entire exit pupil can be expressed as [10]

$$
W(x, y)=\sum_{k} W_{k}(x, y)=\sum_{k} \frac{2 \pi}{\lambda}\left(\mathrm{OPL}_{k}-\mathrm{OPL}_{0}\right). \quad(14)
$$

## 4. Results and Discussion

### A. Thermal–Structural Analysis of the Window

The cuboid-shaped window took the form of a side-mounted window of a maneuvering missile. It had a length of 80 mm, width of 80 mm, and thickness

of 8 mm. The boundary conditions of the window were simplified because of the lack of sufficient experimental data. Fluid dynamic equations were not considered in this study because the focus was mainly on numerically evaluating the optical distor- tion of the window in the aerodynamic thermal envir- onment. The initial temperature of the window was 300 K. The heat flux distribution on the outside sur- face of the window was obtained from the wind tun- nel experiment. The outside surface of the window was divided into nine regions, as shown in Fig. 5. The heat flux distribution on the outside surface of the window was simplified due to the lack of suffi- cient experimental data. Specifically, the heat flux was evenly distributed in the same region, but it var- ied in different regions. Heat fluxes in regions 1-9 were $2.60 \times 10^{4}$, $7.97 \times 10^{3}$, $5.03 \times 10^{3}$, $4.20 \times 10^{4}$, $1.21 \times 10^{5}$, $4.40 \times 10^{4}$, $4.70 \times 10^{4}$, $5.91 \times 10^{4}$, and $7.39 \times 10^{4}\ \text{W/m}^2$, respectively. For the maneuvering missile studied in this research, its time of the term- inal guidance was 15 s. Therefore, the entire expo- sure time of the window in the aerodynamic flow was determined to be 15 s. The flow incident angle was assumed to be at $0^{\circ}$. The aerodynamic pressure and inner air pressure of the window were also ob- tained from the wind tunnel experiment. The aerody- namic pressure exerted on the outside surface of the window (as in Fig. 5) was $5.00 \times 10^{5}\ \text{Pa}$, whereas the internal air pressure exerted on the inside surface and four sides of the window was $1.00 \times 10^{5}\ \text{Pa}$. The main physical properties of the standard zinc sulfide are listed in Table 1 [11].

Finite element simulation for the standard zinc sulfide window in the aerodynamic thermal environ- ment was conducted to investigate the time evolution of the temperature, deformation, and strain fields of the window. The aerodynamic heating exerted the largest cumulative influences on the temperature, deformation, and strain distributions of the window at 15 s. To investigate the largest cumulative influ- ences of the aerodynamic heating on the tempera- ture, deformation, and strain distributions of the window, the temperature, sum deformation, and equivalent von Mises strain fields of the window at 15 s were obtained from the finite element simula- tion and are shown in Figs. 6(a)-6(c).

![](./images/811653167887417345_5.jpg)

Fig. 5. Simplified heat flux distribution on the outside surface of the window obtained from the wind tunnel experiment.

<table>
<caption>Table 1. Main Physical Properties of the Standard Zinc Sulfide Crystal Near 300 K</caption>
<thead>
<tr>
<th>Physical Properties</th>
<th>Performance Parameters</th>
</tr>
</thead>
<tbody>
<tr>
<td>Density ($\text{kg·m}^{-3}$)</td>
<td>4102</td>
</tr>
<tr>
<td>Melting point (K)</td>
<td>1973</td>
</tr>
<tr>
<td>Expansion coefficient ($10^{-6}\ \text{K}^{-1}$)</td>
<td>7.0</td>
</tr>
<tr>
<td>Heat capacity ($\text{J·kg}^{-1}·\text{K}^{-1}$)</td>
<td>470</td>
</tr>
<tr>
<td>Young's modulus ($10^{9}\ \text{Pa}$)</td>
<td>74</td>
</tr>
<tr>
<td>Thermal conductivity ($\text{W·m}^{-1}·\text{K}^{-1}$)</td>
<td>19</td>
</tr>
<tr>
<td>Poisson ratio</td>
<td>0.29</td>
</tr>
<tr>
<td>Mean strength ($10^{6}\ \text{Pa}$)</td>
<td>100</td>
</tr>
</tbody>
</table>

As shown in Fig. 6(a), the temperature distribution of the window was influenced by the heat flux distri- bution. The region with a high temperature corre- sponded to the region with a large heat flux. The region having the maximum temperature was lo- cated at the center of the outside surface of the win- dow because the region having the maximum heat flux was located in the same place. The regions with drastic temperature variations were mostly confined to the outside surface of the window. As shown in Figs. 6(b) and 6(c), the sum deformation and equiva- lent von Mises strain distributions of the window were influenced by both the heat flux distribution and the aerodynamic pressure field. Therefore, the maximum sum deformation and maximum equiva- lent von Mises strain of the window were not at the center of the outside surface of the window but near the lower right corner of the window. The tempera- ture, sum deformation, and equivalent von Mises strain fields of the window were inhomogeneous due to the uneven heat flux distribution on the out- side surface. Consequently, the refractive index field of the window was inhomogeneous and formed a gradient distribution due to the thermo-optical and elasto-optical effects.

### B. Analysis of the Refractive Index Variations of the Window

The working wavelength of the window was $10\ \mu\text{m}$. At 300 K, the refractive index of the standard zinc sulfide was 2.20 at a wavelength of $10\ \mu\text{m}$ [11], and, accordingly, the thermo-optical coefficient of the standard zinc sulfide $\left[\frac{\partial n(\lambda,T)}{\partial T}\right]$ was $4.10 \times 10^{-5}\ \text{K}^{-1}$ [11]. The elasto-optical coefficients of the standard zinc sulfide (i.e., $P_{11}$, $P_{12}$, and $P_{44}$) were 0.091, $-0.01$, and 0.075 [12], respectively.

The optical axis of the standard zinc sulfide crystal ($x_3$ axis) was parallel to the transmission axis ($z$ axis) (Fig. 3), mitigating the influence exerted by the elas- to-optical effect on the optical transmission of the window. According to Eqs. (1) and (5), the refractive index variations of two points at 15 s were obtained (Table 2) to investigate the influences exerted by the thermo-optical and elasto-optical effects on the re- fractive index variation of the window. These refer to both the point with maximum temperature variation

1 July 2011 / Vol. 50, No. 19 / APPLIED OPTICS 3139

![](./images/811653167887417345_6.jpg)

Fig. 6. (Color online) Color-scale maps of the (a) temperature, (b) sum deformation, and (c) equivalent von Mises strain fields of the window at 15 s.

[i.e., in the region mostly red in color, at the center of the window outside surface in Fig. 6(a)] and the point with maximum equivalent von Mises strain variation [i.e., in the region mostly red in color, near the lower right corner of the window in Fig. 6(c)].

As indicated in Table 2, for the point with maximum temperature variation, its maximum refractive index variation caused by the elasto-optical effect $(\Delta n_{11})$ was only 1.1% of its refractive index variation produced by the thermo-optical effect $(\Delta n_{T})$ at 15 s. For the point with maximum equivalent von Mises strain variation, its maximum refractive index variation caused by the elasto-optical effect $(\Delta n_{33})$ was only 7.2% of its refractive index variation produced by the thermo-optical effect $(\Delta n_{T})$ at 15 s. Therefore, the thermo-optical effect was observed to exert a much greater influence on the refractive index variation of the window than the elasto-optical effect. Only the influence of the thermo-optical effect was considered in computing the refractive index field of the window. Based on the theory of the thermo-optical effect, the refractive index field of the window was calculated from the temperature field of the window, as expressed in Eq. (1).

Overall, results of the analysis suggest that the thermo-optical effect may have a much greater influence on the optical transmission through the window than the elasto-optical effect. This finding is similar to that of a previous study [8], in which the thermo-optical effect is considered the dominant factor affecting the wavefront error of the aero-optical window.

### C. Modeling Approach to Retrieving the High Refractive Index Gradient Regions and to Reconstructing the Refractive Index Field of the Window

The refractive index gradient (three-dimensional) magnitude field of the window at 15 s was computed from the refractive index field using the finite difference method. To investigate the structure of the refractive index gradient magnitude field, slices of the gradient magnitude field were obtained at the planes of $x=40$ mm and $y=40$ mm, as shown in Fig. 7. The high-gradient regions (regions in red) were block-shaped and mostly confined to the top borders of the slices. This illustrates the drastic refractive index variations on the outside surface of the window, corresponding to the drastic temperature variations observed in the same place [in Fig. 6(a)].

These observations were used to develop a modeling approach to retrieve the high-gradient regions and to reconstruct the refractive index field of the window. The modeling approach is summarized in three steps [1–3] based on the harmonic-mean refractive index gradient magnitude threshold in Subsection 2.C:

1. the regions with gradient magnitudes above the threshold were identified as high-gradient blocks, and their spatial locations, refractive indices, and refractive index gradients were retrieved;
2. the regions with gradient magnitudes below the threshold were identified as zero-gradient regions; hence, their refractive index gradients were set to zero; and
3. the zero-gradient regions were approximated as uniform refractive index regions. The refractive index of each zero-gradient region was computed using the refractive index gradient of its closest

<table>
<caption>Table 2. Refractive Index Variations of the Point with Maximum Temperature Variation and the Point with Maximum Equivalent Von Mises Strain Variation at 15 s¹</caption>
<thead>
<tr>
<th>Point</th>
<th>$\Delta n_{T}$</th>
<th>$\Delta n_{11}$</th>
<th>$\Delta n_{22}$</th>
<th>$\Delta n_{33}$</th>
<th>$\Delta n_{23}$</th>
<th>$\Delta n_{31}$</th>
<th>$\Delta n_{12}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>$3.62 \times 10^{-3}$</td>
<td>$4.02 \times 10^{-5}$</td>
<td>$3.45 \times 10^{-5}$</td>
<td>$3.45 \times 10^{-5}$</td>
<td>$-1.09 \times 10^{-7}$</td>
<td>$5.23 \times 10^{-9}$</td>
<td>$-3.29 \times 10^{-6}$</td>
</tr>
<tr>
<td>2</td>
<td>$2.28 \times 10^{-3}$</td>
<td>$-7.59 \times 10^{-5}$</td>
<td>$-1.59 \times 10^{4}$</td>
<td>$1.64 \times 10^{-4}$</td>
<td>$1.16 \times 10^{-4}$</td>
<td>$3.78 \times 10^{-5}$</td>
<td>$-1.74 \times 10^{-5}$</td>
</tr>
</tbody>
</table>

¹Point 1 denotes the point with maximum temperature variation. Point 2 denotes the point with maximum equivalent von Mises strain variation. $\Delta n_{T}$ is the refractive index variation caused by the thermo-optical effect. $\Delta n_{11}$, $\Delta n_{22}$, $\Delta n_{33}$, $\Delta n_{23}$, $\Delta n_{31}$, and $\Delta n_{12}$ are the refractive index variations caused by the elasto-optical effect.

high-gradient block, which the beam propagated through as it entered each zero-gradient region.

The harmonic-mean gradient magnitude threshold, $G_{T}$, was determined as $4.03 \times 10^{-5}\ \text{mm}^{-1}$, as expressed in Eq. (8). Based on the harmonic-mean threshold, the function of the modeling approach was demonstrated using the original refractive index and gradient magnitude data of the window. Figure 8(a) shows the reconstructed refractive index field of the window at 15 s, where the threshold retained only 65.7% of the original refractive index values compared with the original refractive index field in Fig. 8(b). The reconstructed refractive index field proved to be in agreement with the original refractive index field.

Let $R_{1}$ denote the reconstructed refractive index field of the window, and $R$ denote the original refractive index field of the window. The correlation coefficient of these two fields, $r$, can be expressed as

$$
r=\frac{\operatorname{Cov}\left(R_{1}, R\right)}{\left[D\left(R_{1}\right) D(R)\right]^{1 / 2}}=\frac{\sum_{i=1}^{81} \sum_{j=1}^{81} \sum_{k=1}^{9}\left(R_{1 i j k}-R_{1 a}\right)\left(R_{i j k}-R_{a}\right)}{\left\{\left[\sum_{i=1}^{81} \sum_{j=1}^{81} \sum_{k=1}^{9}\left(R_{1 i j k}-R_{1 a}\right)^{2}\right]\left[\sum_{i=1}^{81} \sum_{j=1}^{81} \sum_{k=1}^{9}\left(R_{i j k}-R_{a}\right)^{2}\right]\right\}^{1 / 2}}, \qquad (15)
$$

where
- $\operatorname{Cov}(R_{1},R)$ is the covariance of $R_{1}$ and $R$;
- $D(R_{1})$, and $D(R)$ are the variances of $R_{1}$ and $R$;
- $R_{1a}$, and $R_{a}$ are the average values of $R_{1}$ and $R$; and
- $i$, $j$, and $k$ are the $x$-, $y$-, and $z$-directional serial numbers of $R_{1}$ and $R$.

According to the Cauchy–Schwarz inequality, the absolute value of $r$ is less than or equal to 1.0. The closer it approaches to 1.0, the more linearly correlated these two fields are. The correlation coefficient of these two fields, $r$, was determined to be 0.97 according to Eq. (15). Therefore, the reconstructed and original refractive index fields were nearly linearly correlated, indicating a satisfactory agreement between these two fields.

### D. Validation of the Ray-Tracing Program

Validating the aero-optic methods was complicated mainly because of the lack of reliable experimental data [13]. Nevertheless, the point spread function (PSF) evaluation capability of the ray-tracing program was explored. To this end, a tiltlike gradient-index slab was defined. Its refractive index distribution can be expressed as [13]

$$
n(x,y)=c+\alpha x, \qquad (16)
$$

where $c$ is the refractive index of the initial point of propagation ($x=0\ \text{mm}$), and $\alpha$ is the distributional constant of the gradient-index slab. The optical axis of the gradient-index slab is parallel to the $z$ axis.

An ideal lens with a focal length of $f'$ was fixed at the back of the slab. An incoming plane wave picked up a linear phase distortion while transmitting along the optical axis through this slab. The linear phase distortion can be expressed as [13]

$$
\phi(x,y)=\frac{2\pi}{\lambda}n(x,y)d=\frac{2\pi}{\lambda}cd+\frac{2\pi}{\lambda}\alpha xd, \qquad (17)
$$

where $\lambda$ is the wavelength of the incident wave, and $d$ is the thickness of the slab.

Therefore, the pupil function of this gradient-index slab can be expressed as

$$
A(x,y)=\operatorname{circ}[2(x^{2}+y^{2})^{1/2}/D]\exp[j\phi(x,y)], \qquad (18)
$$

where $\operatorname{circ}[\cdot]$ is the circular domain function, and $D$ is the diameter of the exit pupil of the gradient-index slab.

According to the Huygens principle, the PSF of this gradient-index slab can be related to the Fourier transformation of the pupil function, expressed as [14]

![](./images/811653167887417345_7.jpg)

Fig. 7. (Color online) Color-scale maps of the slices of the refractive index gradient magnitude field of the window at 15s at the planes of (a) $x=40$ mm and (b) $y=40$ mm.

$$
\begin{aligned}
\operatorname{PSF}(x', y')= & \left|\iint A(x, y) \exp \left[-j \frac{2 \pi}{\lambda f^{\prime}}\left(x x^{\prime}+y y^{\prime}\right)\right] \mathrm{d} x \mathrm{~d} y\right|^{2} \\
= & \left|\frac{\lambda f^{\prime} D}{2\left[\left(x^{\prime}-d \alpha f^{\prime}\right)^{2}+y^{\prime 2}\right]^{1 / 2}}\right. \\
& \left.\times J_{1}\left\{\frac{\pi D}{\lambda f^{\prime}}\left[\left(x^{\prime}-d \alpha f^{\prime}\right)^{2}+y^{\prime 2}\right]^{1 / 2}\right\}\right|^{2}, \quad(19)
\end{aligned}
$$

where $J_{1}\{\cdot\}$ is the first-order Bessel function of the first kind.

As indicated in Eq. (19), for the PSF of this gradient-index slab, its $x$ coordinate of the peak position, $x_{\text {Peak }}{ }^{\prime}$, can be expressed as

$$
x_{\text {Peak }}{ }^{\prime}=d \alpha f^{\prime} . \quad(20)
$$

The refractive index of the standard zinc sulfide crystal was 2.20 at a wavelength of $10 \mu \mathrm{m}$ and its thermo-optical coefficient was $4.1 \times 10^{-5} \mathrm{~K}^{-1}$. The diameter of the exit pupil of the window was 60 mm, and the thickness of the window was 8 mm. An ideal lens with a 150 mm focal length was fixed at the back of the window. To make the validation become an effective gauge of the uncertainty of the ray-tracing program, the following parameters were used according to the design details and the refractive index parameters of the window: $c=2.20, \alpha=0.02 \mathrm{~mm}^{-1}$, $\lambda=10 \mu \mathrm{m}, d=8 \mathrm{~mm}, D=60 \mathrm{~mm}$, and $f^{\prime}=150 \mathrm{~mm}$. The $x$ coordinate of the peak position for the normalized PSF result of the ray-tracing program, $x_{\text {Peak }}^{\prime}$,

![](./images/811653167887417345_8.jpg)

Fig. 8. (Color online) Color-scale maps of the (a) reconstructed and (b) original refractive index fields of the window at 15 s.

was 24.02 mm, which was in satisfactory agreement with the theoretical prediction of 24.00 mm given by Eq. (20). Therefore, the ray-tracing program can obtain satisfactory accuracy using the appropriate parameters. The program can be used for simulating the optical transmission through the window.

## E. Optical Distortion Evaluation of the Original and Reconstructed Refractive Index Fields of the Window

The thermo-optical effect may have a much greater influence on the optical transmission through the window compared with the elasto-optical effect. Therefore, the influence exerted by the elasto-optical effect was excluded in this section, and only the optical transmission of the ordinary ray was considered. An ideal lens with a 150 mm focal length was fixed at the back of the window to single out the optical distortion caused by aerodynamic heating.

Using Eqs. (10)-(14), wave aberrations of the exit pupil at 15 s were obtained at the $0^{\circ} / 75^{\circ}$ (azimuth/ elevation) incident angle through the ray-tracing program. Figure 9 presents the comparison between the wave aberration obtained from the original refractive index field and that obtained from the reconstructed refractive index field. The results show an evident satisfactory agreement in terms of the wave aberration distribution.

![](./images/811653167887417345_9.jpg)

Fig. 9. (Color online) Wave aberration results of the window obtained from (a) the original refractive index field and (b) the reconstructed refractive index field for the $0^\circ/75^\circ$ (azimuth/elevation) incident angle.

The root-mean-square (RMS) wave aberration results at the $0^\circ/75^\circ$ (azimuth/elevation) incident angle at 15 s were obtained to compare further the wave aberration obtained from the original refractive index field with that obtained from the reconstructed refractive index field. The RMS wave aberration obtained from the reconstructed refractive index field was 0.543 waves, while the RMS wave aberration obtained from the original refractive index field was 0.552 waves. The absolute error was 0.009 waves, accounting for only 1.6% of the RMS wave aberration obtained from the original refractive index field (0.552 waves). Significant robustness was evident, as only a 1.6% difference in the RMS wave aberration was caused by the reduction of nearly 34.3% in the refractive index information of the window. This robustness can be realized by understanding the fact that high-gradient regions may produce the dominant optical distortion of the window. This finding is similar to that of a previous study [2], in which a less than 5% discrepancy in the RMS optical path difference was caused by a reduction of up to 40% in the refractive fluid field information by retaining only high refractive gradient interfaces.

Results from the analysis indicate that the IFT concept can be used to evaluate the optical distortion of the window numerically. Moreover, the harmonic-mean gradient magnitude threshold can capture the essential optical distortion of the window in the aerodynamic thermal environment.

### 5. Conclusions
This study investigated the possibility of utilizing the IFT concept for the numerical three-dimensional optical distortion evaluation of the aerodynamically heated window. The IFT concept was used to develop a modeling approach to retrieve the high refractive index gradient regions and to reconstruct the refractive index field of the window. The three-dimensional optical distortion was numerically evaluated for the reconstructed and original refractive index fields of the window using the ray-tracing program based on a recursive algorithm [7].

The methodology based on the IFT concept aims to reduce the refractive index information required to capture the essential optical distortion of the window. It can also be used to evaluate the optical distortion of the window numerically. Moreover, the methodology can optimize the optical transmission

through the window, as the optical distortion of the window can effectively be modified by altering the structure of the high refractive index gradient re- gions [2]. Therefore, this methodology can expand the application range of the pioneering studies done by Catrakis and co-workers [1–3].

The boundary conditions of the simulation were simplified for an easier analysis. In the same way, a number of actual engineering conditions, such as gas ionization and refrigeration, were not considered in the simulation [10]. Therefore, the applicability of the methodology can further be tested by considering the actual engineering conditions. The experimental validation of the mathematical model of the optical transmission through the window will be pursued in future research.

This research was supported by the Aeronautical Science Fund of China under contract 20080177003. The authors are grateful to Lin Wu and Jiancheng Fan for their insightful advice, guidance, and sugges- tions. The present work is inspired by the previous work with Yaping Zhang and by the pioneering work of Haris J. Catrakis and Roberto C. Aguirre. Invalu- able and helpful comments by the reviewers and editors are also gratefully acknowledged.

### References

1. H. J. Catrakis and R. C. Aguirre, "New interfacial fluid thick- ness approach in aero-optics with applications to compressible turbulence," AIAA J. 42, 1973–1981 (2004).

2. H. J. Catrakis, R. C. Aguirre, J. C. Nathman, and P. J. Garcia, "Large-scale refractive turbulent interfaces and aero-optical interactions in high Reynolds number compressible separated shear layers," J. Turbul. 7, 1–21 (2006).

3. R. C. Aguirre, "Turbulent fluid interfaces with applications to mixing and aero-optics," Ph.D. dissertation (Henry Samueli School of Engineering, University of California, Irvine, 2005).

4. L. Wu, J. C. Fang, and Z. H. Yang, "Study on aero-optical dis- tortion simulation of high refraction index gradient regions in hypersonic turbulent flow," Acta Opt. Sin. 29, 2952–2957 (2009).

5. D. Yang, M. E. Thomas, and S. G. Kaplan, "Measurement of the infrared refractive index of sapphire as a function of tem- perature," Proc. SPIE 4375, 53–63 (2001).

6. J. F. Nye, *Physical Properties of Crystals* (Oxford Univ. Press, 1985).

7. T. Wang, Y. Zhao, D. Xu, and Q. Y. Yang, "Numerical study of evaluating the optical quality of supersonic flow fields," Appl. Opt. 46, 5545–5551 (2007).

8. Y. P. Zhang and Z. G. Fan, "Study on the optical path difference of aero-optical window," Optik 118, 557–560 (2007).

9. D. H. Feng, S. Pan, Z. Y. Tian, and H. Li, "Research on ray tracing method in 3D discrete space with discretionary refrac- tion index," Acta Opt. Sin. 30, 696–701 (2010).

10. H. S. Xiao and Z. G. Fan, "Imaging quality evaluation of aero- dynamically heated optical dome using ray tracing," Appl. Opt. 49, 5049–5058 (2010).

11. D. C. Harris, *Materials for Infrared Windows and Domes* (SPIE, 1999).

12. W. H. Yu and W. Y. Liu, *Crystal Physics* (University of Science and Technology of China Press, 1998).

13. E. Frumker and O. Pade, "Generic method for aero-optic evaluations," Appl. Opt. 43, 3224–3228 (2004).

14. J. W. Goodman, *Introduction to Fourier Optics* (McGraw- Hill, 1996).
<br>
3144 APPLIED OPTICS / Vol. 50, No. 19 / 1 July 2011