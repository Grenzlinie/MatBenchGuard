# Saint-Venant End Effects of Transversely Isotropic Piezoelectric Materials

Masyuki Tai¹,ᵃ, Anil C. Wijeyewickrema¹,ᵇ and Olivier Llouquet¹,ᶜ

¹Department of Civil Engineering, Tokyo Institute of Technology, O-okayama, Meguro-ku, Tokyo 152-8552, Japan

ᵃtai.m.aa@m.titech.ac.jp, ᵇwijeyewickrema.a.aa@m.titech.ac.jp, ᶜolivier.llouquet@gmail.com

**Keywords:** decay rate, piezoelectric material, semi-infinite strip, transversely isotropic.

Abstract. In this paper, Saint-Venant end effects for plane deformations of transversely isotropic piezoelectric materials are investigated. The stress decay rates in linear piezoelectric strips that are traction free with two kinds of electrical boundary conditions are considered. The characteristic equations for decay rate are obtained for symmetric and antisymmetric deformations. Numerical values are given for the roots with the smallest positive real part, which are associated with the slowest decay. Saint-Venant end effects of piezoelectric materials of crystal class 6mm penetrate much further into strip than those of elastic isotropic materials.

## Introduction
Saint-Venant end effects for plane deformations of linear piezoelectric materials have been previously investigated [1,2,3]. In [1] it was assumed that the gradient of electric potential in the axial direction is very small when compared with the thickness direction, which results in the governing equations in terms of the Airy stress function and induction function being uncoupled. A state-space approach was used in [2]. The case of traction free and surface charge free boundary conditions were considered in [3]. Related problems for linear elastic sandwich composites have been studied in [4,5].

## Formulation of the Problem and Characteristic Equations
Consider the homogeneous piezoelectric semi-infinite strip transversely isotropic about the poling axis which is the $x_3$-axis, with elastic constants $s_{11}, s_{12}, s_{13}, s_{33}, s_{44}$ piezoelectric constants $d_{31}, d_{33}, d_{15}$ and dielectric constants $\varepsilon_{11}, \varepsilon_{33}$ and thickness $2c$ shown schematically in Fig. 1. The Cartesian coordinate system is chosen such that the $x_3$-direction is normal to the free surface of the strip, and the origin $O$ lies at the mid plane of the strip.

![](./images/811868123291451393_1.jpg)

Fig. 1. Transversely isotropic piezoelectric semi-infinite strip of thickness $2c$.

To determine stress decay rates it is sufficient to consider self-equilibrated conditions at the $x_1 = 0$ end. Due to the symmetric geometry of the strip it is sufficient to consider only the upper half of the semi-infinite strip $(0 \leq x_3 \leq +c)$. The relevant mechanical and electrical variables are given in the Appendix.

The mid-plane conditions for symmetric deformations of the strip
$$
\sigma_{31}\left(x_{1}, 0\right)=0, u_{3}\left(x_{1}, 0\right)=0, \phi\left(x_{1}, 0\right)=0, \tag{1}
$$
and for antisymmetric deformations of the strip
$$
\sigma_{33}\left(x_{1}, 0\right)=0, u_{1}\left(x_{1}, 0\right)=0, D_{3}\left(x_{1}, 0\right)=0, \tag{2}
$$
are identically satisfied.

At $x_3 = \pm c$ the traction free mechanical boundary conditions are
$$
\sigma_{33}\left(x_{1}, c\right)=0, \sigma_{13}\left(x_{1}, c\right)=0, \tag{3}
$$
and the electrical boundary conditions are
charge free: $D_{3}\left(x_{1}, c\right)=0$ or
$$
\tag{4}
$$
electric potential free: $\phi\left(x_{1}, c\right)=0$.
$$
\tag{5}
$$

For the different combinations of boundary conditions considered, the mechanical conditions Eq. 3 and electrical conditions Eqs. 4 or 5, yield a system of three equations for the three unknown coefficients associated with the mechanical and electrical variables, which in turn will yield the characteristic equations for the decay rates. The characteristic equations are given below.

Case A (TF-CF): Traction free and charge free boundaries at $x_3 = \pm c$
Symmetric deformation:
$$
\begin{aligned}
&F_{A S}(\gamma)= \\
&\beta_{1} \bar{A}_{3} \sin \left(\beta_{1} \gamma\right)\left[\cos \left(2 \beta_{2} \gamma\right)+\cosh \left(2 \alpha_{2} \gamma\right)\right]+\cos \left(\beta_{1} \gamma\right)\left[\bar{p}_{1} \sin \left(2 \beta_{2} \gamma\right)+\bar{p}_{2} \sinh \left(2 \alpha_{2} \gamma\right)\right]=0.
\end{aligned} \tag{6}
$$

Antisymmetric deformation is:
$$
\begin{aligned}
&F_{A A}(\gamma)= \\
&\beta_{1} \bar{A}_{3} \cos \left(\beta_{1} \gamma\right)\left[\cos \left(2 \beta_{2} \gamma\right)-\cosh \left(2 \alpha_{2} \gamma\right)\right]+\sin \left(\beta_{1} \gamma\right)\left[-\bar{p}_{1} \sin \left(2 \beta_{2} \gamma\right)+\bar{p}_{2} \sinh \left(2 \alpha_{2} \gamma\right)\right]=0,
\end{aligned} \tag{7}
$$
where $\bar{p}_{1}=\alpha_{2}\left(\bar{A}_{1}-\bar{A}_{2}\right)-\beta_{2} \bar{A}_{3}, \quad \bar{p}_{2}=\beta_{2}\left(\bar{A}_{1}-\bar{A}_{2}\right)+\alpha_{2} \bar{A}_{3}$. The Eqs. 6 and 7 agree with Eq. 46 of [3].

Case B (TF-EPF): Traction free and electric potential free boundaries at $x_3 = \pm c$
Symmetric deformation:

$$
\begin{aligned}
& F_{B S}(\gamma)= \\
& \bar{p}_{5} \cos \left[\beta_{1} \gamma\right]\left(\cos \left[2 \beta_{2} \gamma\right]-\cosh \left[2 \alpha_{2} \gamma\right]\right)+\sin \left[\beta_{1} \gamma\right]\left(\bar{p}_{3} \sin \left[2 \beta_{2} \gamma\right]-\bar{p}_{4} \sinh \left[2 \alpha_{2} \gamma\right]\right)=0.
\end{aligned}
\tag{8}
$$

Antisymmetric deformation:

$$
\begin{aligned}
& F_{B A}(\gamma)= \\
& \bar{p}_{5} \sin \left[\beta_{1} \gamma\right]\left(\cos \left[2 \beta_{2} \gamma\right]+\cosh \left[2 \alpha_{2} \gamma\right]\right)-\cos \left[\beta_{1} \gamma\right]\left(\bar{p}_{3} \sin \left[2 \beta_{2} \gamma\right]+\bar{p}_{4} \sinh \left[2 \alpha_{2} \gamma\right]\right)=0,
\end{aligned}
\tag{9}
$$

where $\bar{p}_{3}=K_{7} \alpha_{2}-K_{8} \beta_{1},\ \bar{p}_{4}=-K_{7} \beta_{2}+K_{9} \beta_{1},\ \bar{p}_{5}=K_{9} \alpha_{2}-K_{8} \beta_{2}$.

## Numerical Results and discussion

Four piezoelectric materials of class 6mm are considered. The material properties used for the numerical results are given in Table 1 [1]. Decay rates for Case A are given in Tables 1 and 2, and compared with previous results in Table 3.

Table 1. Decay rate and decay length of Case A (symmetric case).
<table>
  <tr>
    <td></td>
    <td>Root with smallest real part</td>
    <td>$F_{AS}(\gamma)$</td>
    <td>Decay rate</td>
    <td>Decay length</td>
  </tr>
  <tr>
    <td>PZT-5H</td>
    <td>$0.382776+1.398492\text{i} \times 10^{-25}$</td>
    <td>$-1.23159 \times 10^{-18}-1.48147\text{i} \times 10^{-26}$</td>
    <td>0.383/c</td>
    <td>$6.015 \times (2\text{c})$</td>
  </tr>
  <tr>
    <td>PZT-5</td>
    <td>$1.460487+1.582468\text{i} \times 10^{-23}$</td>
    <td>$1.90582 \times 10^{-21}-3.10270\text{i} \times 10^{-27}$</td>
    <td>1.460/c</td>
    <td>$1.577 \times (2\text{c})$</td>
  </tr>
  <tr>
    <td>PZT-4</td>
    <td>$1.375904+7.888609\text{i} \times 10^{-30}$</td>
    <td>$2.37169 \times 10^{-20}-2.30979\text{i} \times 10^{-33}$</td>
    <td>1.376/c</td>
    <td>$1.674 \times (2\text{c})$</td>
  </tr>
  <tr>
    <td>Ceramic-B</td>
    <td>$1.460152+3.205869\text{i} \times 10^{-17}$</td>
    <td>$2.03288 \times 10^{-20}-5.69929\text{i} \times 10^{-21}$</td>
    <td>1.460/c</td>
    <td>$1.577 \times (2\text{c})$</td>
  </tr>
</table>

Table 2. Decay rate and decay length of Case A (antisymmetric case).
<table>
  <tr>
    <td></td>
    <td>Root with smallest real part</td>
    <td>$F_{AA}(\gamma)$</td>
    <td>Decay rate</td>
    <td>Decay length</td>
  </tr>
  <tr>
    <td>PZT-5H</td>
    <td>$0.547458+6.530365\text{i} \times 10^{-25}$</td>
    <td>$-1.08312 \times 10^{-16}-2.33555\ \text{i} \times 10^{-24}$</td>
    <td>0.547/c</td>
    <td>$4.206 \times (2\text{c})$</td>
  </tr>
  <tr>
    <td>PZT-5</td>
    <td>$2.919872+5.664959\text{i} \times 10^{-22}$</td>
    <td>$2.62580 \times 10^{-20}-2.87482\text{i} \times 10^{-25}$</td>
    <td>2.920/c</td>
    <td>$0.789 \times (2\text{c})$</td>
  </tr>
  <tr>
    <td>PZT-4</td>
    <td>$2.738617+1.195282\text{i} \times 10^{-26}$</td>
    <td>$-1.76183 \times 10^{-19}-9.08787\text{i} \times 10^{-30}$</td>
    <td>2.739/c</td>
    <td>$0.841 \times (2\text{c})$</td>
  </tr>
  <tr>
    <td>Ceramic-B</td>
    <td>$2.914914+3.221132\text{i} \times 10^{-21}$</td>
    <td>$-1.69407 \times 10^{-20}-1.39566\text{i} \times 10^{-24}$</td>
    <td>2.915/c</td>
    <td>$0.790 \times (2\text{c})$</td>
  </tr>
</table>

Table 3. Comparison of decay length with previous results (symmetric case).
<table>
  <tr>
    <td></td>
    <td>Present analysis</td>
    <td>Ruan et al. (2000)</td>
    <td>Borrelli et al. (2006)</td>
  </tr>
  <tr>
    <td>PZT-5H</td>
    <td>$6.015 \times (2\text{c})$</td>
    <td>$1.35 \times (2\text{c})$</td>
    <td>$2.083 \times (2\text{c})$</td>
  </tr>
  <tr>
    <td>PZT-5</td>
    <td>$1.577 \times (2\text{c})$</td>
    <td>$1.19 \times (2\text{c})$</td>
    <td>$2.106 \times (2\text{c})$</td>
  </tr>
  <tr>
    <td>PZT-4</td>
    <td>$1.674 \times (2\text{c})$</td>
    <td>$1.22 \times (2\text{c})$</td>
    <td>$1.720 \times (2\text{c})$</td>
  </tr>
  <tr>
    <td>Ceramic-B</td>
    <td>$1.577 \times (2\text{c})$</td>
    <td>$1.13 \times (2\text{c})$</td>
    <td>$2.263 \times (2\text{c})$</td>
  </tr>
</table>

The results obtained in [1] are after an approximation is used in the formulation. The authors feel that the numerical results given by [3] are not accurate. From Tables 1 and 2, it can be seen that for Case A the decay length for the antisymmetric case is less than for the symmetric case.

Decay rates for Case B are given in Tables 4 and 5.

Table 4. Decay rate and decay length of Case B (symmetric case).
<br>

<table>
<thead>
<tr>
<th></th>
<th>Root with smallest real part</th>
<th>$F_{BS}\left(\gamma\right)$</th>
<th>Decay rate</th>
<th>Decay length</th>
</tr>
</thead>
<tbody>
<tr>
<td>PZT-5H</td>
<td>0.386688+2.56414i×10⁻²⁴</td>
<td>-6.26669×10⁻¹⁷+4.90639i×10⁻²⁴</td>
<td>0.387/c</td>
<td>5.955×(2c)</td>
</tr>
<tr>
<td>PZT-5</td>
<td>1.857440+1.078930i</td>
<td>-1.66533×10⁻¹⁶+8.32667i×10⁻¹⁷</td>
<td>1.857/c</td>
<td>1.240×(2c)</td>
</tr>
<tr>
<td>PZT-4</td>
<td>1.801437+1.052000i</td>
<td>-5.55112×10⁻¹⁷-6.24500i×10⁻¹⁷</td>
<td>1.801/c</td>
<td>1.278×(2c)</td>
</tr>
<tr>
<td>Ceramic-B</td>
<td>1.988510+1.145175i</td>
<td>-2.77556×10⁻¹⁷+2.77556i×10⁻¹⁶</td>
<td>1.989/c</td>
<td>1.158×(2c)</td>
</tr>
</tbody>
</table>

Table 5. Decay rate and decay length of Case B (antisymmetric case).

<table>
<thead>
<tr>
<th></th>
<th>Root with smallest real part</th>
<th>$F_{BA}\left(\gamma\right)$</th>
<th>Decay rate</th>
<th>Decay length</th>
</tr>
</thead>
<tbody>
<tr>
<td>PZT-5H</td>
<td>0.547075-7.921125i×10⁻¹⁹</td>
<td>-2.77556×10⁻¹⁷+1.05370i×10⁻¹⁸</td>
<td>0.547/c</td>
<td>4.209×(2c)</td>
</tr>
<tr>
<td>PZT-5</td>
<td>1.460763+1.163538i×10⁻¹⁶</td>
<td>-1.49403×10⁻¹⁶+1.89662i×10⁻¹⁷</td>
<td>1.461/c</td>
<td>1.576×(2c)</td>
</tr>
<tr>
<td>PZT-4</td>
<td>1.379322-2.492800i×10⁻²⁸</td>
<td>1.47451×10⁻¹⁷-1.46770i×10⁻²⁹</td>
<td>1.379/c</td>
<td>1.669×(2c)</td>
</tr>
<tr>
<td>Ceramic-B</td>
<td>1.461497+2.411209i×10⁻¹⁶</td>
<td>2.81893×10⁻¹⁸+1.31530i×10⁻¹⁷</td>
<td>1.461/c</td>
<td>1.575×(2c)</td>
</tr>
</tbody>
</table>

From Tables 4 and 5, for Case B other than for PZT-5H, the decay length for the symmetric case is less than for the antisymmetric case. Normalized stresses are shown in Fig. 2.

![](./images/811868123291451393_2.jpg)

Fig. 2. Stress decay for: (a) Case A and (b) Case B.

### Acknowledgements
The authors are pleased to acknowledge financial support from Monbukagakusho (Ministry of Education, Culture, Sports, Science and Technology), Japan, under Grant-in-Aid for Scientific Research (C) No. 19560075.

### Appendix
The mechanical and electrical variables for symmetric deformation of the layer are given by,

$$
\frac{\sigma_{33}\left(x_{1}, x_{3}\right)}{\left(\gamma / c\right)^{2} e^{-\gamma x_{1} / c}}=C_{1} \cos \left(\beta_{1} \overline{x}_{3}\right)+C_{3} \cosh \left(\alpha_{2} \overline{x}_{3}\right) \cos \left(\beta_{2} \overline{x}_{3}\right)+C_{5} \sinh \left(\alpha_{2} \overline{x}_{3}\right) \sin \left(\beta_{2} \overline{x}_{3}\right), \tag{A.1}
$$

$$
\begin{aligned}
\frac{\sigma_{31}\left(x_{1}, x_{3}\right)}{(\gamma / c)^{2} e^{-\gamma x_{1} / c}}= & -C_{1} g_{1} \sin \left(\beta_{1} \bar{x}_{3}\right)+C_{3}\left[g_{2} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{3} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{5}\left[g_{2} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{3} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.2}
$$

$$
\begin{aligned}
\frac{u_{1}\left(x_{1}, x_{3}\right)}{-(\gamma / c) e^{-\gamma x_{1} / c}}= & C_{1} g_{4} \cos \left(\beta_{1} \bar{x}_{3}\right)+C_{3}\left[g_{5} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{6} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{5}\left[g_{5} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{6} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.3}
$$

$$
\begin{aligned}
\frac{u_{3}\left(x_{1}, x_{3}\right)}{-(\gamma / c) e^{-\gamma x_{1} / c}}= & -C_{1} g_{7} \sin \left(\beta_{1} \bar{x}_{3}\right)+C_{3}\left[g_{8} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{9} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{5}\left[g_{8} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{9} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.4}
$$

$$
\begin{aligned}
\frac{D_{3}\left(x_{1}, x_{3}\right)}{(\gamma / c)^{2} e^{-\gamma x_{1} / c}}= & C_{1} g_{10} \cos \left(\beta_{1} \bar{x}_{3}\right)+C_{3}\left[g_{11} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{12} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{5}\left[g_{11} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{12} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.5}
$$

$$
\begin{aligned}
\frac{\phi\left(x_{1}, x_{3}\right)}{(\gamma / c) e^{-\gamma x_{1} / c}}= & -C_{1} g_{13} \sin \left(\beta_{1} \bar{x}_{3}\right)+C_{3}\left[g_{14} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{15} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{5}\left[g_{14} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{15} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.6}
$$

and for antisymmetric deformation of the layer are given by,

$$
\frac{\sigma_{33}\left(x_{1}, x_{3}\right)}{(\gamma / c)^{2} e^{-\gamma x_{1} / c}}=C_{2} \sin \left(\beta_{1} \bar{x}_{3}\right)+C_{4} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+C_{6} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right), \tag{A.7}
$$

$$
\begin{aligned}
\frac{\sigma_{31}\left(x_{1}, x_{3}\right)}{(\gamma / c)^{2} e^{-\gamma x_{1} / c}}= & C_{2} g_{1} \cos \left(\beta_{1} \bar{x}_{3}\right)+C_{4}\left[g_{2} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{3} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{6}\left[g_{2} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{3} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.8}
$$

$$
\begin{aligned}
\frac{u_{1}\left(x_{1}, x_{3}\right)}{-(\gamma / c) e^{-\gamma x_{1} / c}}= & C_{2} g_{4} \sin \left(\beta_{1} \bar{x}_{3}\right)+C_{4}\left[g_{5} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{6} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{6}\left[g_{5} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{6} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.9}
$$

$$
\begin{aligned}
\frac{u_{3}\left(x_{1}, x_{3}\right)}{-(\gamma / c) e^{-\gamma x_{1} / c}}= & C_{2} g_{7} \cos \left(\beta_{1} \bar{x}_{3}\right)+C_{4}\left[g_{8} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{9} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{6}\left[g_{8} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{9} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.10}
$$

$$
\begin{aligned}
\frac{D_{3}\left(x_{1}, x_{3}\right)}{(\gamma / c)^{2} e^{-\gamma x_{1} / c}}= & C_{2} g_{10} \sin \left(\beta_{1} \bar{x}_{3}\right)+C_{4}\left[g_{11} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{12} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{6}\left[g_{11} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{12} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.11}
$$

$$
\begin{aligned}
\frac{\phi\left(x_{1}, x_{3}\right)}{(\gamma / c) e^{-\gamma x_{1} / c}}= & C_{2} g_{13} \cos \left(\beta_{1} \bar{x}_{3}\right)+C_{4}\left[g_{14} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)+g_{15} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)\right] \\
& +C_{6}\left[g_{14} \cosh \left(\alpha_{2} \bar{x}_{3}\right) \cos \left(\beta_{2} \bar{x}_{3}\right)-g_{15} \sinh \left(\alpha_{2} \bar{x}_{3}\right) \sin \left(\beta_{2} \bar{x}_{3}\right)\right],
\end{aligned} \tag{A.12}
$$

where $C_{i}(i=1, \ldots 6)$ are arbitrary constants, $\bar{x}_{3}=\gamma x_{3} / c$ and $q_{i}(i=1, \ldots 6)$ given by
$q_{1}=i \beta_{1}, q_{2}=\bar{q}_{1}, q_{3}=\alpha_{2}+i \beta_{2}, q_{4}=\bar{q}_{3}, q_{5}=-\alpha_{2}+i \beta_{2}$ and $q_{6}=\bar{q}_{5}$ are the roots of the equation,

$$
\begin{aligned}
& a_{11} \delta_{11} q^{6}+\left[a_{11} \delta_{22}+\left(2 a_{12}+a_{33}\right) \delta_{11}+\left(b_{21}+b_{13}\right)^{2}\right] q^{4}+\left[a_{22} \delta_{11}+\left(2 a_{12}+a_{33}\right) \delta_{22}\right. \\
& \left.+2 b_{22}\left(b_{21}+b_{13}\right)\right] q^{2}+\left(a_{22} \delta_{22}+b_{22}^{2}\right)=0,
\end{aligned} \tag{A.13}
$$

and $a_{11}, a_{12}, a_{22}, a_{33}, b_{21}, b_{22}, b_{13}, \delta_{11}, \delta_{22}$ are given in Eq. 18 of [3]. The constants $g_{i}(i=1, \ldots 15)$ are given by

$$
\begin{aligned}
& g_{1}=\beta_{1}, g_{2}=\alpha_{2}, g_{3}=\beta_{2}, g_{4}=K_{1}, g_{5}=K_{2}, g_{6}=K_{3}, g_{7}=K_{4}, g_{8}=K_{5}, g_{9}=K_{6}, \\
& g_{10}=\bar{A}_{1}, g_{11}=\bar{A}_{2}, g_{12}=\bar{A}_{3}, g_{13}=K_{7}, g_{14}=K_{8} \text { and } g_{15}=K_{9},
\end{aligned} \tag{A.14}
$$

where

$$
\begin{aligned}
& K_{1}=b_{21} \bar{A}_{1}+\left(-a_{11} \beta_{1}^{2}+a_{12}\right), \quad K_{2}=b_{21} \bar{A}_{2}+a_{11}\left(\alpha_{2}^{2}-\beta_{2}^{2}\right)+a_{12}, \quad K_{3}=b_{21} \bar{A}_{3}+2 a_{11} \alpha_{2} \beta_{2}, \\
& K_{4}=\left[\left(b_{13}+b_{21}\right) \bar{A}_{1}+\left(-a_{11} \beta_{1}^{2}+a_{12}+a_{33}\right)\right] \beta_{1}, \\
& K_{5}=\left[\left(b_{13}+b_{21}\right) \bar{A}_{4}+a_{11}\left(\alpha_{2}^{2}-3 \beta_{2}^{2}+a_{12}+a_{33}\right)\right] \alpha_{2}, \\
& K_{6}=\left[\left(b_{13}+b_{21}\right) \bar{A}_{5}+a_{11}\left(3 \alpha_{2}^{2}-\beta_{2}^{2}+a_{12}+a_{33}\right)\right] \beta_{2}, \\
& K_{7}=\left(\delta_{11} \bar{A}_{1}-b_{13}\right) \beta_{1}, \quad K_{8}=\left(\delta_{11} \bar{A}_{4}-b_{13}\right) \alpha_{2}, \quad K_{9}=\left(\delta_{11} \bar{A}_{5}-b_{13}\right) \beta_{2},
\end{aligned} \tag{A.15}
$$

and $\bar{A}_{i}=A_{i} / B_{4} \quad(i=1, \ldots 5)$ where

$$
\begin{aligned}
& A_{1}=B_{1} \beta_{1}^{4}-B_{2} \beta_{1}^{2}+B_{3}, \quad A_{2}=B_{1}\left(\alpha_{2}^{4}-6 \alpha_{2}^{2} \beta_{2}^{2}+\beta_{2}^{4}\right)+B_{2}\left(\alpha_{2}^{2}-\beta_{2}^{2}\right)+B_{3}, \\
& A_{3}=2 \alpha_{2} \beta_{2}\left[2 B_{1}\left(\alpha_{2}^{2}-\beta_{2}^{2}\right)+B_{2}\right], \quad A_{4}=B_{1}\left(\alpha_{2}^{4}-10 \alpha_{2}^{2} \beta_{2}^{2}+5 \beta_{2}^{4}\right)+B_{2}\left(\alpha_{2}^{2}-3 \beta_{2}^{2}\right)+B_{3}, \\
& A_{5}=B_{1}\left(5 \alpha_{2}^{4}-10 \alpha_{2}^{2} \beta_{2}^{2}+\beta_{2}^{4}\right)+B_{2}\left(3 \alpha_{2}^{2}-\beta_{2}^{2}\right)+B_{3}, \quad B_{1}=\delta_{11} a_{11}, \\
& B_{2}=\delta_{11}\left(2 a_{12}+a_{33}\right)+\left(b_{21}+b_{13}\right)^{2}, \quad B_{3}=\delta_{11} a_{22}+b_{22}\left(b_{21}+b_{13}\right), \quad B_{4}=\delta_{22}\left(b_{21}+b_{13}\right)-\delta_{11} b_{22} .
\end{aligned} \tag{A.16}
$$

## References

[1] X. Ruan, S. C. Danforth, A. Safari and T. Chou: Int. J. Solids and Structures Vol. 37 (2000), p. 2625-2637.

[2] J. Tarn and L. Huang: Int. J. Solids and Structures Vol. 39 (2002), p. 4979-4998.

[3] A. Borrelli, C. O. Horgan and C. M. Patria: Int. J. Solids and Structures Vol. 43 (2006), p. 943-956.

[4] I. Choi and C. O. Horgan: ASME Journal of Applied Mechanics Vol. 44 (1977), p. 424-430.

[5] A. C. Wijeyewickrema, C. O. Horgan and J. Dundurs: Int. J. Solids and Structures Vol. 33 (1996), p. 4327-4336.

Advances in Fracture and Materials Behavior
10.4028/www.scientific.net/AMR.33-37

Saint-Venant End Effects of Transversely Isotropic Piezoelectric Materials
10.4028/www.scientific.net/AMR.33-37.725

DOI References

[1] X. Ruan, S. C. Danforth, A. Safari and T. Chou: Int. J. Solids and Structures Vol. 37 (2000), p. 625-2637.
doi:10.1016/S0020-7683(99)00034-7

[2] J. Tarn and L. Huang: Int. J. Solids and Structures Vol. 39 (2002), p. 4979-4998.
doi:10.1016/S0020-7683(02)00011-2

[3] A. Borrelli, C. O. Horgan and C. M. Patria: Int. J. Solids and Structures Vol. 43 (2006), p. 943- 56.
doi:10.1016/j.ijsolstr.2005.03.058

[4] I. Choi and C. O. Horgan: ASME Journal of Applied Mechanics Vol. 44 (1977), p. 424-430.
doi:10.1115/1.3424070

[5] A. C. Wijeyewickrema, C. O. Horgan and J. Dundurs: Int. J. Solids and Structures Vol. 33 1996), p. 4327-4336.
doi:10.1016/0020-7683(95)00232-4

[1] X. Ruan, S. C. Danforth, A. Safari and T. Chou: Int. J. Solids and Structures Vol. 37 (2000), p. 2625-2637.
doi:10.1016/S0020-7683(99)00034-7

[3] A. Borrelli, C. O. Horgan and C. M. Patria: Int. J. Solids and Structures Vol. 43 (2006), p. 943956.
doi:10.1016/j.ijsolstr.2005.03.058

[5] A. C. Wijeyewickrema, C. O. Horgan and J. Dundurs: Int. J. Solids and Structures Vol. 33 (1996), p. 4327-4336.
doi:10.1016/0020-7683(95)00232-4