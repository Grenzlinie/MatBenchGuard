![](./images/811870823345291265_1.jpg)

Available online at www.sciencedirect.com
![](./images/811870823345291265_2.jpg)
Acta Materialia 57 (2009) 2210-2216

![](./images/811870823345291265_3.jpg)

# Phase-field model study of the effect of interface anisotropy on the crystal morphological evolution of cubic metals

R.S. Qin $^{a, *}$ , H.K.D.H. Bhadeshia $^{a,b}$

$^{a}$ Graduate Institute of Ferrous Technology, Pohang University of Science and Technology, San 31, Hyojia-Dong Nam Gu, Pohang 790-784, Republic of Korea
$^{b}$ Department of Materials Science and Metallurgy, University of Cambridge, Pembroke Street, Cambridge CB2 3QZ, UK

Received 27 December 2008; received in revised form 19 January 2009; accepted 19 January 2009
Available online 23 February 2009

## Abstract
An expression is proposed for the anisotropy of interfacial energy of cubic metals, based on the symmetry of the crystal structure. The associated coefficients can be determined experimentally or assessed using computational methods. Calculations demonstrate an average relative error of $<3\%$ in comparison with the embedded-atom data for face-centred cubic metals. For body-centred-cubic metals, the errors are around 7% due to discrepancies at the {332} and {433} planes. The coefficients for the {100}, {110}, {111} and {210} planes are well behaved and can be used to simulate the consequences of interfacial anisotropy. The results have been applied in three-dimensional phase-field modelling of the evolution of crystal shapes, and the outcomes have been compared favourably with equilibrium shapes expected from Wulff's theorem.

© 2009 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

Keywords: Phase-field modeling; Interfaces; Crystal morphology; Crystal structure

---

### 1. Introduction
Crystals are by their very nature anisotropic and interfaces between crystals similarly have energies and structures that are orientation dependent. Phase-field models used to simulate microstructural development have attempted to incorporate this interfacial anisotropy in a variety of ways. The free energy density for a heterogeneous system with contributions from the chemical free energy and interface energy is represented by:

$$
g(\varphi, c, T)=g_{0}(\varphi, c, T)+\frac{1}{2} \varepsilon^{2}|\nabla \varphi|^{2},
\tag{1}
$$

where $g$ is the system free energy density, $g_{0}$ is the chemical free energy density, $\varphi$ is phase-field order parameter, $c$ is solute concentration, $T$ is temperature and $\varepsilon$ is the gradient energy coefficient. Interfacial anisotropy is generally introduced by making $\varepsilon$ orientation-dependent. For example, in the two-dimensional simulation of cubic crystals it is common to assume that [1]:

$$
\varepsilon=\bar{\varepsilon}\left[1+\gamma_{\varepsilon} \cos \left(k_{\varepsilon} \theta\right)\right],
\tag{2}
$$

where $\bar{\varepsilon}$ is the mean value of $\varepsilon$, $\theta$ is the polar angular coordinate of the interface normal, and $\gamma_{\varepsilon}$ and $k_{\varepsilon}$ are anisotropy parameters. Eq. (2) has been modified into other formats to fulfil specific simulation targets [2,3]. In three-dimensional phase-field models, the Cahn-Hoffman $\xi$ vector theory has been applied to describe the interface anisotropy [4,5]. A suggestion made by Karma and Rappel for cubic crystals is [6]:

$$
\varepsilon=\bar{\varepsilon}\left[1+\gamma_{\varepsilon}\left(n_{x}^{4}+n_{y}^{4}+n_{z}^{4}\right)\right],
\tag{3}
$$

where $n_{x}$, $n_{y}$ and $n_{z}$ are Cartesian coordinates of the interface normal. More recently, Haxhimali et al. suggested that the gradient energy coefficient takes the following format to represent interface anisotropy in the context of phase fields [7]:

$$
\varepsilon=\bar{\varepsilon}\left[1+\varepsilon_{1} K_{1}(\theta, \Phi)+\varepsilon_{2} K_{2}(\theta, \Phi)+\cdots\right],
\tag{4}
$$

---

* Corresponding author. Tel.: +82 54 2794407; fax: +82 54 2794499.
E-mail address: rsqin@postech.ac.kr (R.S. Qin).

1359-6454/$36.00 © 2009 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.actamat.2009.01.024

where $\theta$ and $\Phi$ represent the orientation of the interface in spherical coordinates, $\varepsilon_{1}$ and $\varepsilon_{2}$ are coefficients reflecting the extents of anisotropy, $K_{1}$ and $K_{2}$ are cubic harmonics that are combinations of standard spherical harmonics with cubic symmetry. The addition of the $\varepsilon_{2} K_{2}$ term in Eq. (4) (cf. Eq. (3)) is a result of reviewing molecular dynamics simulations for dendrite growth which suggest that this gives a better representation of anisotropy [8].

The motivation for the present work was to develop a generic expression for interface anisotropy of cubic metals, to specify coefficients in the resulting expression and to validate the concept against existing knowledge of crystal growth.

### 2. Interface energy anisotropy

In a cubic system, the normal to a plane with Miller indices (hkl) plane is the direction [hkl]. The unit normal $\hat{n}$ has Cartesian coordinates $n_{x}, n_{y}$ and $n_{z}$. Fig. 1 illustrates how these can be represented in polar or spherical coordinates:
$$
n_{x}=\sin \theta \cos \phi=\frac{h}{\sqrt{h^{2}+k^{2}+l^{2}}}
\tag{5.1}
$$
$$
n_{y}=\sin \theta \sin \phi=\frac{k}{\sqrt{h^{2}+k^{2}+l^{2}}}
\tag{5.2}
$$
$$
n_{z}=\cos \theta=\frac{l}{\sqrt{h^{2}+k^{2}+l^{2}}}.
\tag{5.3}
$$

Anisotropy energy, in general, can be represented as expansions of $n_{x}, n_{y}$ and $n_{z}$ in various orders. In discussing magnetocrystalline anisotropy [9], the interface anisotropy is represented by:
$$
\sigma(\hat{n})=k_{0}+\sum_{i, j} k_{1} n_{i} n_{j}+\sum_{i, j, u, w} k_{1} n_{i} n_{j} n_{u} n_{w}+\cdots,
\tag{6}
$$
where $k_{0}, k_{1}, k_{2}$ and $k_{3}$ are the defining coefficients. The subscripts of $n$ represent the Cartesian coordinates. For cubic symmetry, this simplifies into [10]:
$$
\begin{aligned}
\sigma(\hat{n})= & k_{0}+k_{1}\left(n_{x}^{2} n_{y}^{2}+n_{y}^{2} n_{z}^{2}+n_{z}^{2} n_{x}^{2}\right)+k_{2} n_{x}^{2} n_{y}^{2} n_{z}^{2} \\
& +k_{3}\left(n_{x}^{2} n_{y}^{2}+n_{y}^{2} n_{z}^{2}+n_{z}^{2} n_{x}^{2}\right)^{2}+\cdots.
\end{aligned}
\tag{7}
$$

![](./images/811870823345291265_4.jpg)

Fig. 1. Relation between Miller indices, and Cartesian and polar coordinates in a cubic system.

Ignoring the higher-order terms and using Miller indices, Eqs. (5) and (7) give:
$$
\begin{aligned}
\sigma(h, k, l)= & k_{0}+k_{1} \frac{h^{2} k^{2}+k^{2} l^{2}+l^{2} h^{2}}{\left(h^{2}+k^{2}+l^{2}\right)^{2}}+k_{2} \frac{h^{2} k^{2} l^{2}}{\left(h^{2}+k^{2}+l^{2}\right)^{3}} \\
& +k_{3} \frac{\left(h^{2} k^{2}+k^{2} l^{2}+l^{2} h^{2}\right)^{2}}{\left(h^{2}+k^{2}+l^{2}\right)^{4}}.
\end{aligned}
\tag{8}
$$

For given anisotropy coefficients $k_{0}, k_{1}, k_{2}$ and $k_{3}$, Eq. (8) can express the interfacial energy as a function of orientation.

Eq. (8) is different from the expansion based on cubic harmonics [6,7] – for example, the leading anisotropic term in Eq. (7) is not $\left(n_{x}^{4}+n_{y}^{4}+n_{z}^{4}\right)$ but $\left(n_{x}^{2} n_{y}^{2}+n_{y}^{2} n_{z}^{2}+n_{z}^{2} n_{x}^{2}\right)$. Critical assessment of those two different expressions for representing crystal anisotropy is important but is beyond the scope of the present work. However, it is obvious that Eq. (8) is consistent with cubic symmetry. For example, the interfacial energy for all directions of the form $<100>$ is $k_{0}$. For $<110>$ it is $k_{0}+k_{1}+k_{3}$, for $<111>$ it is $k_{0}+k_{1} / 3+k_{2} / 9+k_{3} / 9$, etc. So, in conclusion, although the individual coefficients cannot be identified with symmetry elements the equation as a whole is consistent with cubic symmetry.

It is required to validate the description inherent in Eq. (8) for cubic anisotropy. The method here was fitted to results from the embedded-atom method (EAM) [11,12]. These EAM calculations are based on embedding atomic functions and electronic densities given by Baskes et al. [13–15]. The least-squares method was used to fit the data with the following objective function:
$$
\delta=\sum_{i}\left[\sigma(h, k, l)-\sigma_{E A M}(h, k, l)\right]^{2},
\tag{9}
$$
where $i$ is the total number of EAM data, $\sigma(h, k, l)$ is from Eq. (8) and $\sigma_{E A M}(h, k, l)$ from EAM data. The best values of $k_{0}, k_{1}, k_{2}$ and $k_{3}$ are obtained when $\delta$ achieves a minimum, i.e. at $\partial \delta / \partial k_{j}=0$ with $j=0,1,2$ and 3. Fig. 2 demonstrates the efficacy of Eq. (8) for 10 face-centred cubic (fcc) crystals, and the corresponding derived values of anisotropy coefficients together with the average relative errors (AvRE) are listed in Table 1. AvRE is defined as $A v R E=\overline{\left|[\sigma(h, k, l)-\sigma_{E A M}(h, k, l)] / \sigma_{E A M}(h, k, l)\right|}$. It can be seen that 9 out of 10 fits have $<2 \%$ average relative errors.

![](./images/811870823345291265_5.jpg)

Fig. 2. Comparison of interface energy of fcc crystals calculated by Eq. (8) with data from the embedded-atom method.

<table>
<caption>Table 1<br>Anisotropy coefficients $k_0$, $k_1$, $k_2$, $k_3$ and AvRE determined by least-squares fitting of EAM data. The units for coefficients are in erg cm$^{-2}$. AvRE4% is for the data plotted in Fig. 4.</caption>
<thead>
<tr>
<th>Metal</th>
<th>$K$</th>
<th>$K$</th>
<th>$k_2$</th>
<th>$k_3$</th>
<th>AvRE (%)</th>
<th>AvRE4 (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cu</td>
<td>1666.87</td>
<td>733.621</td>
<td>−1873.19</td>
<td>−3260.43</td>
<td>1.959</td>
<td>2.802</td>
</tr>
<tr>
<td>Ag</td>
<td>1287.51</td>
<td>110.57</td>
<td>−642.8</td>
<td>−1401.67</td>
<td>1.527</td>
<td>2.369</td>
</tr>
<tr>
<td>Au</td>
<td>1101.41</td>
<td>917.506</td>
<td>−2658.9</td>
<td>−3358.65</td>
<td>1.850</td>
<td>2.586</td>
</tr>
<tr>
<td>Ni</td>
<td>2462.4</td>
<td>723.47</td>
<td>−2970.25</td>
<td>−4075.9</td>
<td>1.637</td>
<td>2.426</td>
</tr>
<tr>
<td>Pd</td>
<td>1685.19</td>
<td>975.872</td>
<td>−2015.65</td>
<td>−4055.37</td>
<td>1.782</td>
<td>2.478</td>
</tr>
<tr>
<td>Pt</td>
<td>2197.7</td>
<td>926.172</td>
<td>−6581.9</td>
<td>−4542.32</td>
<td>1.854</td>
<td>2.676</td>
</tr>
<tr>
<td>Al</td>
<td>922.344</td>
<td>1363.19</td>
<td>−5690.92</td>
<td>−4478.54</td>
<td>2.856</td>
<td>3.568</td>
</tr>
<tr>
<td>Pb</td>
<td>430.362</td>
<td>280.798</td>
<td>−493.042</td>
<td>−1082.85</td>
<td>1.614</td>
<td>2.463</td>
</tr>
<tr>
<td>Rh</td>
<td>2934.53</td>
<td>1495.79</td>
<td>−486.378</td>
<td>−6338.95</td>
<td>1.671</td>
<td>2.357</td>
</tr>
<tr>
<td>Ir</td>
<td>2943.61</td>
<td>2547.81</td>
<td>1421.33</td>
<td>−8266</td>
<td>1.445</td>
<td>2.179</td>
</tr>
</tbody>
</table>

![](./images/811870823345291265_6.jpg)

Fig. 3. Comparison of interface energy of bcc crystals calculated by Eq. (8) with numerical results from the embedded-atom method.

<table>
<caption>Table 2<br>Anisotropy coefficients $k_0$, $k_1$, $k_2$, $k_3$ and AvRE determined by least-squares fitting of EAM data. The units for coefficients are in erg cm$^{-2}$. AvRE4% is for the data plotted in Fig. 4.</caption>
<thead>
<tr>
<th>Metal</th>
<th>$K$</th>
<th>$K$</th>
<th>$k_2$</th>
<th>$K$</th>
<th>AvRE (%)</th>
<th>AvRE4(%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Li</td>
<td>442.723</td>
<td>−1163.95</td>
<td>4554.7</td>
<td>1123.37</td>
<td>8.713</td>
<td>9.640</td>
</tr>
<tr>
<td>Na</td>
<td>295.162</td>
<td>−578.775</td>
<td>1914.79</td>
<td>476.77</td>
<td>7.195</td>
<td>7.707</td>
</tr>
<tr>
<td>K</td>
<td>186.96</td>
<td>−347.872</td>
<td>1021.95</td>
<td>281.641</td>
<td>7.038</td>
<td>7.543</td>
</tr>
<tr>
<td>V</td>
<td>2561.47</td>
<td>−3584.81</td>
<td>11986.8</td>
<td>2134.02</td>
<td>6.059</td>
<td>6.100</td>
</tr>
<tr>
<td>Nb</td>
<td>2861.21</td>
<td>−4256.08</td>
<td>14414.2</td>
<td>2764.52</td>
<td>6.202</td>
<td>6.291</td>
</tr>
<tr>
<td>Ta</td>
<td>3381.3</td>
<td>−5271.41</td>
<td>15268.7</td>
<td>3735.67</td>
<td>6.367</td>
<td>6.596</td>
</tr>
<tr>
<td>Cr</td>
<td>1286.05</td>
<td>−1306.83</td>
<td>9485.12</td>
<td>1917.94</td>
<td>6.909</td>
<td>6.623</td>
</tr>
<tr>
<td>Mo</td>
<td>2184.48</td>
<td>−343.473</td>
<td>7098.62</td>
<td>−1783.23</td>
<td>5.202</td>
<td>4.660</td>
</tr>
<tr>
<td>W</td>
<td>2726.18</td>
<td>−1493.07</td>
<td>11203.9</td>
<td>−639.744</td>
<td>5.427</td>
<td>5.083</td>
</tr>
<tr>
<td>Fe</td>
<td>2258.53</td>
<td>−3291.47</td>
<td>12959.9</td>
<td>1880.74</td>
<td>6.069</td>
<td>6.052</td>
</tr>
</tbody>
</table>

In the case of aluminium, the error is <2.9%. This shows that Eq. (8) gives a good description of interface anisotropy in fcc crystals.

The corresponding data for body-centred cubic (bcc) crystals are given in Fig. 3 and Table 2, with most AvRE values at ~6%. Lithium has the largest AvRE at 8.7%. The discrepancies are especially severe for the (332) and (433) planes for all the considered bcc metals. This suggests a potential problem with the EAM calculations and atomic potential and electronic densities for those two orientations. Without those two discrepancies, the fitness could be improved substantially.

It is worth pointing out that $k_0$ in Tables 1 and 2 does not equal the averaged interface energy. However, this value can be easily obtained by a stepped least-squares method of using $\sigma(h, k, l)=k_0$ to fit data and determine $k_0$ first. Other parameters are determined subsequently. Despite the advantage that $k_0$ reproduces the average interface energy exactly, it is found that the stepped least-squares method gives less accurate data fitting. Application of the stepped least-squares method for Cu, Ag and Au results in AeRV values of 4.043%, 3.276% and 5.025%, respectively.

In Eq. (8) there are only four unknown coefficients, which can be fully determined by calculating or measuring the interfacial energy at just four different orientations. Fig. 4 illustrates the comparison of all EAM calculations with Eq. (8) where the anisotropy coefficients $k_0$, $k_1$, $k_2$ and $k_3$ are determined by only using the interface energies at (100), (110), (111) and (210). The corresponding AvRE values based on this calculation are listed in Tables 1 and 2 in the column labelled AvRE4. All data show that AvRE4 is less than 1% larger than AvRE. AvRE4 values for Cr, Mo, W and Fe are even smaller than the corresponding AvRE values. It is seen that the accuracy of this computation is comparable to the large data-fitting illustrated in Figs. 2 and 3. This suggests that there is redundant information in the EAM calculations: hence such computations could be done more economically by focusing just on the solution of the four coefficients of Eq. (8), and thus on the study of just four interface orientations.

![](./images/811870823345291265_7.jpg)

Fig. 4. Comparison of Eq. (8) calculation where coefficients are determined by (100), (110), (111) and (210) with all available EAM data: (a) fcc crystal; (b) bcc crystal.

### 3. Phase-field model consideration

Eqs. (7) and (8) are for the interfacial energy per unit area, $\sigma$, which in a phase-field model is implicitly represented by the gradient energy coefficient $\varepsilon$. We now consider the relationship between these two quantities in the context of the simplest phase-field model (Eq. (1)). For the system in which the phase transition takes place from $\varphi=0$ to $\varphi=1$, the chemical free energy density $g_{0}$ can be described by a double-well potential function [16,17]:

$$
g_{0}(\varphi, c, T)=g_{b}(\varphi)+\frac{1}{4 \omega} \varphi^{2}(1-\varphi)^{2},
\tag{10}
$$

where $g_{b}$ is the chemical free energy of $\varphi=0$ and $\varphi=1$ bulk phases, and $\omega$ is a coefficient reflecting the kinetic barrier between two minima. The governing equation for the evolution of the phase-field order parameter $\varphi$ is [5]:

$$
\frac{\partial \varphi}{\partial t}=M_{\phi}\left(\nabla \frac{\partial g}{\partial \nabla \varphi}-\frac{\partial g}{\partial \varphi}\right),
\tag{11}
$$

where $M_{\varphi}$ is the phase-field mobility and its value can be derived from interface kinetics [5,18,19]. Inserting Eqs. (1) and (10) into (11) leads to [6]:

$$
\begin{aligned}
\frac{\partial \varphi}{\partial t}= & M_{\varphi}\left\{\frac{\partial}{\partial x}\left[|\nabla \varphi|^{2} \varepsilon(\hat{n}) \frac{\partial \varepsilon(\hat{n})}{\partial\left(\varphi_{x}\right)}\right]+\frac{\partial}{\partial y}\left[|\nabla \varphi|^{2} \varepsilon(\hat{n}) \frac{\partial \varepsilon(\hat{n})}{\partial\left(\varphi_{y}\right)}\right]\right. \\
& +\frac{\partial}{\partial z}\left[|\nabla \varphi|^{2} \varepsilon(\hat{n}) \frac{\partial \varepsilon(\hat{n})}{\partial\left(\varphi_{z}\right)}\right]+\nabla\left[\varepsilon(\hat{n})^{2} \nabla \varphi\right] \\
& \left.+\frac{1}{2 \omega} \varphi(1-\varphi)(1-2 \varphi)-\frac{\partial g_{b}}{\partial \varphi}\right\}.
\end{aligned}
\tag{12}
$$

In the one-dimensional system where the interface is constant along the axis, Eq. (12) is reduced at equilibrium to:

$$
\varepsilon^{2} \frac{d^{2} \varphi}{d x^{2}}-\frac{1}{2 \omega} \varphi(1-\varphi)(1-2 \varphi)=0.
\tag{13}
$$

The solution of the equation for the boundary conditions $\varphi=1$ at $x=-\infty$ and $\varphi=0$ at $x=+\infty$ is:

$$
\varphi(x)=\frac{1}{2}\left[1-\tan \frac{x}{2 \sqrt{2 \omega} \varepsilon}\right].
\tag{14}
$$

Let:

$$
\lambda=2.2 \sqrt{2 \omega} \varepsilon.
\tag{15}
$$

Eqs. (14) and (15) give $\varphi(-\lambda)=0.90025$ and $\varphi(-\lambda)=0.0975$, which is a good approximation of interface thickness. $\lambda$ is called the half-interface thickness because the interface starts from $-\lambda$ and ends at $\lambda$. Multiplying Eq. (13) by $d \varphi / d x$ and integrating leads to:

$$
\frac{1}{2} \varepsilon^{2}\left(\frac{d \varphi}{d x}\right)^{2}=\frac{1}{4 \omega} \varphi^{2}(1-\varphi)^{2}.
\tag{16}
$$

The interface energy is all the excess energy at the interfacial region, which is:

$$
\sigma=\int_{-\infty}^{+\infty}\left[\frac{1}{2} \varepsilon^{2}\left(\frac{d \varphi}{d x}\right)^{2}+\frac{1}{4 \omega} \varphi^{2}(1-\varphi)^{2}\right]=\varepsilon^{2} \int_{-\infty}^{+\infty}\left(\frac{d \varphi}{d x}\right)^{2} d x.
\tag{17}
$$

Inserting Eq. (14) into Eq. (17) leads to:

$$
\sigma=\frac{\sqrt{2} \varepsilon}{12 \sqrt{\omega}}.
\tag{18}
$$

Eqs. (15) and (18) give:

$$
\sigma=\frac{1.1}{3 \lambda} \varepsilon^{2}.
\tag{19}
$$

A similar derivation is found in Ref. [17]. However, it is emphasized here that Eq. (19) is not only valid for a particular orientation but for any direction. This requires more

rigorous mathematical derivation. Based on Eq. (19), one has:
$$
\sigma(\hat{n})=\frac{1.1}{3 \lambda} \varepsilon(\hat{n})^{2}. \quad(20)
$$

Suppose the gradient energy coefficient has the following format:
$$
\begin{aligned}
\varepsilon(\hat{n})= & \varepsilon_{0}+\varepsilon_{1}\left(n_{x}^{2} n_{y}^{2}+n_{y}^{2} n_{z}^{2}+n_{z}^{2} n_{x}^{2}\right)+\varepsilon_{2} n_{x}^{2} n_{y}^{2} n_{z}^{2} \\
& +\varepsilon_{3}\left(n_{x}^{2} n_{y}^{2}+n_{y}^{2} n_{z}^{2}+n_{z}^{2} n_{x}^{2}\right)^{2}.
\end{aligned}
$$

Bringing Eq. (21) into Eq. (20), ignoring the higher-order terms and comparing the results with Eq. (7), gives:
$$
\varepsilon_{0}=\lambda_{0} \sqrt{k_{0}} \quad(22.1)
$$

$$
\varepsilon_{1}=\frac{\lambda_{0} k_{1}}{2 \sqrt{k_{0}}} \quad(22.2)
$$

$$
\varepsilon_{2}=\frac{\lambda_{0} k_{2}}{2 \sqrt{k_{0}}} \quad(22.3)
$$

$$
\varepsilon_{3}=\frac{\lambda_{0} k_{3}}{2 \sqrt{k_{0}}}-\frac{\lambda_{0} k_{1}^{2}}{8 k_{0} \sqrt{k_{0}}} \quad(22.4)
$$
where $\lambda_{0}=\sqrt{3 \lambda / 1.1}$. Eq. (22) fully determines the coefficients of gradient energy coefficient function in terms of the coefficients in the anisotropic interface energy function. The theory is now closed. Table 3 lists some of the results obtained from data given in Table 1.

The interface normal vector in the phase-field model is computed by:
$$
\hat{n}=\frac{\nabla \varphi}{|\nabla \varphi|}, \quad(23)
$$

This gives $n_{j}=\varphi_{j} / \sqrt{\sum_{j} \varphi_{j}^{2}}$, where $j$ represents one of the axes in Cartesian coordinates and $\varphi_{j}=\partial \varphi / \partial x_{j}$. Other basic terms in the further expansion of Eq. (12) include $\partial n_{j} / \partial x_{k}=\varphi_{j k} /|\nabla \varphi|-\varphi_{j} \sum_{m} \varphi_{m} \varphi_{m k} /|\nabla \varphi|^{3}, \partial n_{j} / \partial \varphi_{k}=\delta_{j k} /|\nabla \varphi|$ $-\varphi_{j} \varphi_{k} /|\nabla \varphi|^{3}$, etc. The computation of Eq. (12) also requires the definition of the format of $g_{b}(\varphi)$. In the isothermal and composition-invariant phase transitions, it can be represented as [6]:
$$
g_{b}(\varphi)=[1-h(\varphi)] g_{0}+h(\varphi) g_{1}, \quad(24)
$$
where $g_{0}$ and $g_{1}$ are free energy densities of the bulk phases $\varphi=0$ and $\varphi=1$, respectively. $h(\varphi)=\varphi^{2}\left(6 \varphi^{2}-15 \varphi+10\right)$ can be considered as the fraction of the phase $\varphi=1$, so that:
$$
\frac{\partial g_{b}}{\partial \varphi}=30 \varphi^{2}(1-\varphi)^{2}\left(g_{0}-g_{1}\right). \quad(25)
$$

There are other suggestions for dealing with different systems [20,21]. The phase-field computation involves solving Eq. (11) by discrete methods under specified material parameters.

<table>
<caption>Table 3 Coefficients in gradient energy equation.</caption>
<thead>
<tr>
<th>Metal</th>
<th>$\varepsilon_{1}/\varepsilon_{0}$</th>
<th>$\varepsilon_{2}/\varepsilon_{0}$</th>
<th>$\varepsilon_{3}/\varepsilon_{0}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cu</td>
<td>0.22</td>
<td>−0.56</td>
<td>−1.00</td>
</tr>
<tr>
<td>Ag</td>
<td>0.04</td>
<td>−0.25</td>
<td>−0.55</td>
</tr>
<tr>
<td>Au</td>
<td>0.42</td>
<td>−1.21</td>
<td>−1.61</td>
</tr>
<tr>
<td>Ni</td>
<td>0.15</td>
<td>−0.60</td>
<td>−0.84</td>
</tr>
<tr>
<td>Pd</td>
<td>0.29</td>
<td>−0.60</td>
<td>−1.25</td>
</tr>
<tr>
<td>Pt</td>
<td>0.21</td>
<td>−1.50</td>
<td>−1.06</td>
</tr>
<tr>
<td>Al</td>
<td>0.74</td>
<td>−3.09</td>
<td>−2.70</td>
</tr>
<tr>
<td>Pb</td>
<td>0.33</td>
<td>−0.57</td>
<td>−1.31</td>
</tr>
<tr>
<td>Rh</td>
<td>0.25</td>
<td>−0.08</td>
<td>−1.11</td>
</tr>
<tr>
<td>Ir</td>
<td>0.43</td>
<td>0.24</td>
<td>−1.50</td>
</tr>
</tbody>
</table>

## 4. Numerical computation and discussion

Phase-field computations were carried out to study the effect of interface anisotropy on crystal morphology evolution. In order to reduce other effects it is supposed that all the parameters are fixed in the calculations except the interface anisotropy. Three sets of parameters are applied, as listed in Table 4. The polar diagrams of Eq. (21) with those three sets of parameters are demonstrated in Fig. 5.

The following values are chosen for the simulations: $g_{0}-g_{1}=3.6 \times 10^{8} \mathrm{~J} \mathrm{~m}^{-3}, k_{0}=0.8 \mathrm{~J} \mathrm{~m}^{-2}, M_{\varphi}=100$ and $\lambda=14.3 \mathrm{~nm}$. $k_{0}$ and $\lambda$ give $\omega=1.3547 \times 10^{-9} \mathrm{~m}^{3} \mathrm{~J}^{-1}$ and $\varepsilon_{0}=2.488 \times 10 \mathrm{~J}^{1 / 2} \mathrm{~m}^{-1 / 2}$. Eq. (12) is solved by a six-neighbour implicit finite-difference method with three-dimensional uniform $128^{3}$ grids. The grid size is chosen as $\Delta x=0.5 \lambda$ so that interface covers four elements [20,22]. The initial condition is to put a spherical seed at the centre of the logistic frame with the phase-field order parameter configured to:
$$
\begin{cases}\varphi(r, t=0)=1 & \text { for } r<\Delta x \\ \varphi(r, t=0)=\frac{2}{1+\exp (r-1)} & \text { for } \Delta x<r<4 \Delta x \\ \varphi(r, t=0)=0 & \text { for } r \geq 4 \Delta x\end{cases}
$$

The crystal morphologies at 5000 time steps for all three different interface anisotropy cases are demonstrated in Fig. 6. It can clearly be seen that the crystal morphologies are completely different for different interface anisotropy even when all other parameters are fixed. In other words, interfacial anisotropy can have an important impact on crystal morphological evolution.

In the phase-field simulation of crystal growth, $\partial g_{b} / \partial \varphi$ plays the role of driving force for the phase transition. The phase-field simulation in the current work assumes a

<table>
<caption>Table 4 Coefficients applied in phase-field calculation.</caption>
<thead>
<tr>
<th></th>
<th>Case A</th>
<th>Case B</th>
<th>Case C</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\varepsilon_{1}/\varepsilon_{0}$</td>
<td>−0.863</td>
<td>0.402</td>
<td>1.8655</td>
</tr>
<tr>
<td>$\varepsilon_{2}/\varepsilon_{0}$</td>
<td>0.395</td>
<td>0.00144</td>
<td>0.2555</td>
</tr>
<tr>
<td>$\varepsilon_{3}/\varepsilon_{0}$</td>
<td>0.0238</td>
<td>0.00066</td>
<td>0.0</td>
</tr>
</tbody>
</table>

![](./images/811870823345291265_8.jpg)

Fig. 5. Polar diagram of Eq. (21) with various coefficients: (a) Case A, (b) Case B and (c) Case C.

![](./images/811870823345291265_9.jpg)

Fig. 6. Crystal morphology at 5000 time steps as a function of interfacial anisotropy: (a) Case A, (b) Case B and (c) Case C.

constant $(g_{0}-g_{1})$ without consideration of thermal and solute diffusion. This means that there is no equilibrium mechanism for the growing crystals to approach their equilibrium shape. It is observed, as is expected based on earlier considerations, that the shapes of crystals at different time steps are similar. The interface thickness maintains the 4-grid-distance value throughout the growth.

Although the crystal shapes obtained in the current work are not equilibrium, it is interesting to compare the non-equilibrium crystal shapes with the equilibrium ones. The equilibrium shape of a crystal, according to Wulff's theorem, takes the inner envelope of the polar interface energy diagram so that the crystal interface energy for a given volume is minimized [23]. Fig. 7 shows the polar interface energy diagram, phase-field model simulated non-equilibrium crystal shape, and the equilibrium crystal shape predicted by Wulff's theorem, for the three sets of anisotropic parameters listed in Table 4. It is found that the non-equilibrium crystal shapes, especially the growing crystal tips, possess some favorable correlations with the equilibrium crystal shape. For example, Fig. 7a and c show a sharp crystal tip but Fig. 7b shows round corners. The evolution of crystal geometry from non-equilibrium to equilibrium has been studied by phase-field modelling as well as other methods [24,25].

It is worth-pointing out that although phase-field simulation can sometimes produce a crystal shape which is the same as that of the equilibrium shape predicted by Wulff's theorem, the crystal is not at equilibrium. Equilibrium shape must correspond to an equilibrium state.

For example, choosing $(g_{0}-g_{1})=1.358\times 10^{9}\ \text{J}\ \text{m}^{-3}$ and retaining all the other parameters the same as the early definition, the Case A anisotropy will lead to missing orientations and cusps, which is exactly the equilibrium shape illustrated in Fig. 7a though this is a non-equilibrium crystal.

## 5. Conclusions
(1) The anisotropic interface energy of cubic crystals has been analyzed and is suggested to be represented as $\sigma(\hat{n})=k_{0}+k_{1}\left(n_{x}^{2}n_{y}^{2}+n_{y}^{2}n_{z}^{2}+n_{z}^{2}n_{x}^{2}\right)+k_{2}n_{x}^{2}n_{y}^{2}n_{z}^{2}+k_{3}\left(n_{x}^{2}n_{y}^{2}+n_{y}^{2}n_{z}^{2}+n_{z}^{2}n_{x}^{2}\right)^{2}$. Using Miller indices it is represented as $\sigma(h,k,l)=k_{0}+k_{1}\frac{h^{2}k^{2}+k^{2}l^{2}+l^{2}h^{2}}{\left(h^{2}+k^{2}+l^{2}\right)^{2}}+k_{2}\frac{h^{2}k^{2}l^{2}}{\left(h^{2}+k^{2}+l^{2}\right)^{3}}+k_{3}\frac{\left(h^{2}k^{2}+k^{2}l^{2}+l^{2}h^{2}\right)^{2}}{\left(h^{2}+k^{2}+l^{2}\right)^{4}}$. The coefficients of $k_{0}$, $k_{1}$, $k_{2}$ and $k_{3}$ can be determined by experimental measurements or atomistic computations. The fitting of data obtained by EAM calculations of fcc and bcc metals show good agreement. This proves that the suggested expression is reasonable.

(2) The parameters $k_{0}$, $k_{1}$, $k_{2}$ and $k_{3}$ that are specified by just the interface energies at (100), (110), (111) and (210) give good predictions of other orientations of planes. This suggests that fewer measurements or computations are required to determine the interface anisotropy.

![](./images/811870823345291265_10.jpg)

Fig. 7. Two-dimensional sections of three-dimensional polar diagrams of interface energy, equilibrium crystal shape predicted by Wulff's theorem, and phase-field simulated non-equilibrium crystal shape in the X-Y plane where $\theta=\pi / 2$ with interface anisotropy parameters defined by (a) Case A, (B) Case B and (C) Case C.

(3) The gradient energy coefficient in the phase-field model should take the format $\varepsilon(\hat{n})=\varepsilon_{0}+$ $\varepsilon_{1}\left(n_{x}^{2} n_{y}^{2}+n_{y}^{2} n_{z}^{2}+n_{z}^{2} n_{x}^{2}\right)+\varepsilon_{2} n_{x}^{2} n_{y}^{2} n_{z}^{2}+\varepsilon_{3}\left(n_{x}^{2} n_{y}^{2}+n_{y}^{2} n_{z}^{2}+\right.$ $n_{z}^{2} n_{x}^{2}$ ) $^{2}$, where the coefficients can be determined by $\varepsilon_{0}=\lambda_{0} \sqrt{k_{0}}, \varepsilon_{1}=\frac{\lambda_{0} k_{1}}{2 \sqrt{k_{0}}}, \varepsilon_{2}=\frac{\lambda_{0} k_{2}}{2 \sqrt{k_{0}}}$ and $\varepsilon_{3}=\frac{\lambda_{0} k_{3}}{2 \sqrt{k_{0}}}-$ $\frac{\lambda_{0} k_{1}^{2}}{8 k_{0} \sqrt{k_{0}}}$.

(4) Phase-field simulations show that the interface anisotropy has a considerable impact on the evolution of crystal morphology. Just a small change in interface anisotropy, while keeping all the other parameters unchanged, causes the crystal to grow into a completely different shape.

(5) The effect of interface anisotropy on the equilibrium shape of a crystal is determined by Wulff's theorem. The non-equilibrium crystal shape may have some characteristics that differ in important respects compared with its equilibrium counterpart.

## Acknowledgements
The authors are grateful to Professor Hae-Geon Lee for the provision of laboratory facilities at GIFT.

## References
[1] Wheeler AA, Murray BT. Physica D 1993;66:243.
[2] Moelans N, Blanpain B, Wollants P. Phys Rev Lett 2008;101:025502.
[3] Loginova I, Ågren J, Amberg G. Acta Mater 2004;52:4055.
[4] Wheeler AA, McFadden GB. Proc R Soc Lond A 1997;453:1611.
[5] Nestler B, Wheeler AA. Phys Rev E 1998;57:2602.
[6] Karma A, Rappel WJ. Phys Rev E 1998;57:4323.
[7] Haxhimali T, Karma A, Gonzales F, Rappaz M. Nat Mater 2006;5:660.
[8] Hoyt JJ, Asta M, Karma A. Mater Sci Eng R 2003;41:121-63.
[9] Braun A. Physica B 2006;373:346.
[10] Braun A, Feldmann B, Wuttig M. J Magn Magn Mater 1997;171:16.
[11] Zhang JM, Ma F, Xu KW. Appl Surf Sci 2004;229:34.
[12] Zhang JM, Ma F, Xu KW. Surf Interface Anal 2003;35:662.
[13] Baskes MI. Phys Rev Lett 1987;59:2666.
[14] Baskes MI, Nelson JS, Wright AF. Phys Rev B 1989;40:6086.
[15] Baskes MI. Phys Rev B 1992;46:2727.
[16] Wheeler AA, Boettinger WJ, McFadden GB. Phys Rev A 1992;45:7424.
[17] Kim SG, Kim WT, Suzuki T. Phys Rev E 1998;58:3316.
[18] Qin RS, Wallach ER. J Cryst Growth 2003;253:549.
[19] Qin RS, Wallach ER. Acta Mater 2003;51:6199.
[20] Qin RS, Wallach ER, Thomson RC. J Cryst Growth 2005;279:163.
[21] Chen LQ, Yang W. Phys Rev B 1994;50:15752.
[22] Warren JA, Boettinger WJ. Acta Metall Mater 1995;43:689.
[23] Wulff G. Z Kristallogr 1901;34:449.
[24] Eggleston JJ, McFadden GB, Voorhees PW. Physica D 2001;150: 91.
[25] Zhang W. J Cryst Growth 2006;297:169.