# On the Optimal Design of Gas-Cooled Peltier Current Leads

Xiangchun Xuan

Abstract—We perform the optimal design of gas-cooled Peltier current leads (PCLs), such that their resulting heat leaking into superconducting magnets can be minimized. Superior to previous investigations, the effect of gas cooling on both the Cu lead and the thermoelectric element in a PCL is taken into consideration. Analytical temperature distribution is derived as well as the concerned heat leaking into superconducting magnets. Numerically iterative calculations are, therefore, avoided. Moreover, temperature-entropy diagrams are constructed to distinguish conventional all-Cu leads from PCLs with and without gas cooling. Both the heat leak and the input power of current leads can be easily identified from the areas subtended by the isotherms on the simple two-dimensional temperature-entropy plane.

Index Terms—Current lead, gas-cooled, heat leak, temperature-entropy diagram, thermoelectric.

## I. INTRODUCTION
N A superconducting magnet system current leads are generally the dominant source of extraneous heat leaking into the magnet cryostat [1]. Therefore, how to decrease and minimize this heat leak has always been an important issue in the design of superconducting magnet systems. Recently, Peltier current leads (PCLs) were suggested to replace conventional all-Cu leads. By inserting a thermoelectric (TE) element into the room temperature end of a Cu lead, the heat leak can be effectively reduced due to TE effect [2].

We have performed the global optimization of conduction-cooled (or contact-cooled, i.e., cooled directly by a refrigerator) PCLs. Temperature-entropy (T-s) diagrams have been constructed to identify the principal energy flows in a thermodynamic cycle formed by two PCLs with opposite direction of electrical current [3], [4]. For gas-cooled (i.e., cooled convectively by an evaporated gas flow) PCLs, however, all previous investigations have omitted the effect of gas cooling on the TE element in a PCL [5]–[7]. Moreover, numerically iterative calculations had to be employed to find the optimum performance figures in those analyses. In this paper, we will account for the effect of gas cooling on the TE element to complete the theoretical analysis of a gas-cooled PCL. Analytical formulas for the temperature distribution and the heat leak of a PCL are derived so that numerically iterative calculations can be avoided. The T-s formulation will also be employed to understand graphically the actual thermodynamic process in a gas-cooled PCL.

![](./images/812402027278630913_1.jpg)

Fig. 1. Schematic of a superconducting magnet system with n- and p-type PCLs.

As shown in Fig. 1, the most general configuration of a PCL consists of three segments, viz., a high-$T_c$ superconductor (HTS), a Cu lead, and a TE element in the order of increasing temperature. We know that a HTS is generally a poor thermal conductor with zero electrical resistivity under the liquid nitrogen temperature. The heat leak can, therefore, be arbitrarily small so long as the HTS is made sufficiently long. Indeed, many investigators have made the approximation that a HTS produces zero heat leak under 77 K [3]–[6]. Sato *et al.*, however, took account of the thermal resistance of not only the HTS itself but also the joint between HTS and Cu [7].

In this paper, we will simply omit the HTS and assume that the remaining two segments, i.e., Cu lead and TE element, are convectively cooled by an evaporated nitrogen gas flow instead of helium gas. The scheme of such a reduced PCL is illustrated in Fig. 2. Okumura and Yamaguchi have made the same assumption [5]. Note that we have assumed a one-dimensional (1-D) heat flow taking placing in the PCL. The cold end temperature $T_c$ of the Cu lead (exactly the hot end temperature of HTS) is, thus, kept at 77 K. The hot end temperature of the TE element (for a PCL) or the Cu lead (for a conventional all-Cu lead) is equal to the room temperature $T_r = 300$ K.

## II. FORMULATION
When the electrical potential gradient $\nabla V$ and the temperature gradient $\nabla T$ exist parallelly and simultaneously in a gen-

Manuscript received March 14, 2003. This paper was recommended by Associate Editor J. Schwartz. A portion of this work was done at the Department of Mechanical Engineering, National University of Singapore. This work is supported in part by the National Science and Technology Board of Singapore.
The author is with the Microfluidics Laboratory, Department of Mechanical and Industrial Engineering, University of Toronto, Toronto, ON M5S 3G8, Canada (e-mail: xchxuan@mie.utoronto.ca).
Digital Object Identifier 10.1109/TASC.2003.811651

![](./images/812402027278630913_2.jpg)

Fig. 2. Scheme of a reduced PCL with nitrogen gas cooling.

eral conductor, the electrical current $\mathbf{I}$ and heat flow $\mathbf{Q}$ are given by [8]

$$
\mathbf{I}=-\left(\nabla V+\eta \nabla T\right) \frac{A}{\rho} \tag{1}
$$

$$
\mathbf{Q}=-k A \nabla T+\mathbf{I} \eta T \tag{2}
$$

where $\eta, \rho$, and $k$ are, respectively, the Seebeck coefficient, electrical resistivity, and thermal conductivity of the conductor, $A$ is the cross-sectional area, and $T$ the absolute temperature. Then, the energy balance $\nabla \cdot \mathbf{Q}+H=\mathbf{I} \cdot(-\nabla V)$ leads to the following 1-D equation in a homogeneous conductor:

$$
\frac{d}{d x}\left(k A \frac{d T}{d x}\right)-I\left(T \frac{d \eta}{d T}\right) \frac{d T}{d x}-H+\frac{I^{2} \rho}{A}=0 \tag{3}
$$

where $H$ is the heat transfer rate from a control volume to its surrounding, and $I=|\mathbf{I}|$.

For the case of a conduction-cooled current lead, we have $H=0$. For a gas-cooled current lead, we follow Wilson with $H=f \dot{m} C_{p} d T / d x$, where $f$ is the efficiency of convective heat transfer varying between 0 and $1, C_{p}=1.04 \mathrm{~J} /(\mathrm{g} \cdot \mathrm{K})$ the specific heat of nitrogen gas at constant pressure [1]. At $f=0$, the gas-cooled current lead turns out to be a conduction-cooled one. The mass flow rate $\dot{m}$ of the boiled nitrogen gas is determined by $\dot{m}=w / C_{L}$, where $w$ is the heat leaking into the liquid nitrogen, and $C_{L}=199 \mathrm{~J} / \mathrm{g}$ the latent heat of evaporation of liquid nitrogen. As a result, (3) is rewritten as

$$
\frac{d^{2} T}{d z^{2}}-\left(T \frac{d \eta}{d T}+2 \alpha\right) \frac{d T}{d z}+k \rho=0 \tag{4}
$$

$$
d z=\frac{I d x}{(k A)} \tag{5}
$$

$$
\alpha=\frac{f q u}{2} \tag{6}
$$

$$
q=\frac{w}{I} ; u=\frac{C_{p}}{C_{L}}. \tag{7}
$$

Here, $q$ indicates the typically employed heat leak per unit current that we are concerned about. Note that $T d \eta / d T$ in (4) is the so-called Thomson coefficient in thermoelectrics.

Now, we can derive the temperature distribution and, thus, the heat leak of a PCL by solving (4). A unified space coordinate $x$ is constructed as shown in Fig. 2. Only the p-type TE element and its coupled Cu lead are analyzed in the following.

### A. Cu Lead
Metals usually have a very small Seebeck coefficient, so we can reasonably assume $\eta=0$ for the Cu lead. Further considering the Widemann-Franz law for metals $k \rho=L_{0} T$, (4) is reduced to

$$
\frac{d^{2} T}{d z^{2}}-2 \alpha \frac{d T}{d z}+L_{0} T=0 \tag{8}
$$

where $L_{0}=2.45 \times 10^{-8} \mathrm{~W} \Omega / \mathrm{K}^{2}$ is the Lorenz number¹. With the boundary conditions $T(0)=T_{c}$ and $T\left(Z_{1}\right)=T_{j}$, temperature distribution along the Cu lead in a PCL can be derived as

$$
\begin{aligned}
T(z)=& T_{j} \frac{e^{\alpha z} \sin \beta z}{e^{\alpha Z_{1}} \sin \beta Z_{1}} \\
&+T_{c} e^{\alpha z}\left(\cos \beta z-\sin \beta z \cot \beta Z_{1}\right) \tag{9}
\end{aligned}
$$

$$
\beta=\sqrt{L_{0}-\alpha^{2}} \tag{10}
$$

where $T_{j}$ indicates the junction temperature between the Cu lead and the TE element, and $Z_{1}=\left(I / A_{1}\right) \int_{0}^{L_{1}} d x / k$ with $A_{1}$ and $L_{1}$ being the physical cross-sectional area and length of the Cu lead. The objective of the present optimal design for a PCL is exactly to find the optimum $Z_{1}$ and the following $Z_{2}$ for the TE element simultaneously. The heat leak $q$ at the 77 K cold end of the Cu lead is now expressed by

$$
q=\left.\frac{d T}{d z}\right|_{z=0}=\frac{T_{j} \beta}{e^{\alpha Z_{1}} \sin \beta Z_{1}}+T_{c}\left(\alpha-\beta \cot \beta Z_{1}\right). \tag{11}
$$

For a conduction-cooled PCL with $f=0$, we can simply set $\alpha=0$ in (9) and (11), so that

$$
\begin{aligned}
T_{f=0}(z)=& T_{j} \frac{\sin \beta_{0} z}{\sin \beta_{0} Z_{1}} \\
&+T_{c}\left(\cos \beta_{0} z-\sin \beta_{0} z \cot \beta_{0} Z_{1}\right) \tag{12}
\end{aligned}
$$

$$
q_{f=0}=\left(T_{j}-T_{c} \cos \beta_{0} Z_{1}\right) \frac{\beta_{0}}{\sin \beta_{0} Z_{1}} \tag{13}
$$

where $\beta_{0}=\sqrt{L_{0}}$. Similarly, it is for the case of an all-Cu lead that $T_{j}$ is replaced by $T_{r}$ in (9) and (11)-(13).

### B. TE Element
In thermoelectric devices, TE element properties are usually assumed to be independent of temperature and taken as the average values at the mean operating temperature, so that the control equation can be linearized [8]. Mahan has numerically proved that the full solutions of TE generators performance

¹In fact, the Lorenz number is seldom exactly the same value as we give in the main text. It is dependent on both the metal and the temperature. Here, we specifically choose Cu as the lead material, but the analysis in this paper is theoretically applicable to any material that meets the Widemann-Franz law. As to the real value of Lorenz number, we select the well-known constant for generality, though we acknowledge that it is just an approximation especially in a broad range of temperature.

only slightly deviate from the linear solutions, as long as the dimensionless figure of merit $ZT = \eta^2 T/(\rho k)$, is not too big, say more than three [9]. Thus, the term with the Thomson coefficient in (4) vanishes. From the literature [3]–[7], we know that TE elements in PCLs are usually operated optimally at the temperature range of 200 K–300 K. Therefore, we will simply refer to the average properties of commercially available TE materials from MELCOR, USA² at 250 K. They include: $\eta = 0.19 \times 10^{-3}$ V/K, $\rho = 0.85 \times 10^{-5}$ $\Omega \cdot$ m, $k = 1.90$ W/(m $\cdot$ k), and $ZT \approx 0.56$. Here, TE properties for n- and p-type elements have been assumed identical. Please note, however, that $\eta$ is negative for n-type TE element. In defining $M_0 = k\rho$, (4) is reduced to

$$
\frac{d^2 T}{dz^2} - 2\alpha \frac{dT}{dz} + M_0 = 0. \tag{14}
$$

Its boundary conditions are $T(0) = T_j$ and $T(Z_2) = T_r$, where $Z_2 = IL_2/(kA_2)$ with $A_2$ and $L_2$ the physical cross-sectional area and length of the TE element.

We have noticed the phenomenon that the temperature gradient at the hot end of TE element is zero, when a PCL produces the minimum heat leak. It has been demonstrated for both a conduction-cooled PCL and that with $H$ in (3) being the radiative heat transfer rate [3], [4]. Consequently, we can change the first boundary condition of (14) to $dT/dz|_{z=Z_2} = 0$, such that the solution of (14) can be found as

$$
T(z) = T_r + \left( \frac{M_0}{2\alpha} \right) (z - Z_2) + \left( \frac{M_0}{4\alpha^2} \right) \left[ 1 - e^{2\alpha(z-Z_2)} \right]. \tag{15}
$$

Then, the junction temperature $T_j$ is given by

$$
T_j = T_r - \left( \frac{M_0}{2\alpha} \right) Z_2 + \left( \frac{M_0}{4\alpha^2} \right) (1 - e^{-2\alpha Z_2}). \tag{16}
$$

At the junction between the Cu lead and TE element, however, another continuous condition for the heat flow (2), i.e., $(-dT/dz|_{z=Z_1})_{Cu} = (-dT/dz|_{z=0} + \eta T_j)_{TE}$ should be satisfied, which yields

$$
(\alpha + \eta + \beta \cot \beta Z_1) T_j = \left( \frac{M_0}{2\alpha} \right) (1 - e^{-2\alpha Z_2}) + \frac{T_c \beta e^{\alpha Z_1}}{\sin \beta Z_1}. \tag{17}
$$

In the case of a conduction-cooled PCL with $f = \alpha = 0$, the temperature distribution in the TE element and the junction temperature are, respectively, reduced to

$$
T_{f=0}(z) = T_r - M_0 \frac{(z - Z_2)^2}{2}, \tag{18}
$$

$$
T_{j,f=0} = T_r - M_0 \frac{Z_2^2}{2}. \tag{19}
$$

The continuous (17) at the junction is now given by³

$$
(\eta + \beta_0 \cot \beta_0 Z_1) T_{j,f=0} = M_0 Z_2 + \frac{T_c \beta_0}{\sin \beta_0 Z_1}. \tag{20}
$$

![](./images/812402027278630913_3.jpg)

Fig. 3. Graphic relations of $Z_2$ and $q$ against $Z_1$ for PCLs and all-Cu leads at $f = 0$ and 1, respectively.

Now that the junction temperature $T_j$ has been found, the heat leak $q$ in (11) or (13) becomes a function of only $Z_1$ and $Z_2$. Moreover, there exists a constraint condition to $Z_1$ and $Z_2$ such as (17) or (20). Therefore, the optimization of a PCL has actually been reduced to solve for the minimum $q$ with just one variable of $Z_1$ or $Z_2$, which will be discussed in Section III.

### III. OPTIMAL DESIGN

Substituting (16) into (11) and (17) gives the constrained heat leak equation as follows for a gas-cooled PCL ($f \neq 0$):

$$
\begin{aligned}
q &= T_c (\alpha - \beta \cot \beta Z_1) \\
& \quad + \frac{\left[ T_r - \left( \frac{M_0}{2\alpha} \right) Z_2 + \left( \frac{M_0}{4\alpha^2} \right) (1 - e^{-2\alpha Z_2}) \right] \beta}{e^{\alpha Z_1} \sin \beta Z_1} \tag{21a}
\end{aligned}
$$

$$
\begin{aligned}
& T_r - \left( \frac{M_0}{2\alpha} \right) Z_2 + \left( \frac{M_0}{4\alpha^2} \right) (1 - e^{-2\alpha Z_2}) \\
& \quad = \frac{\left( \frac{M_0}{2\alpha} \right) (1 - e^{-2\alpha Z_2}) + \frac{T_c \beta e^{\alpha Z_1}}{\sin \beta Z_1}}{\alpha + \eta + \beta \cot \beta Z_1}. \tag{21b}
\end{aligned}
$$

According to (6) and (10), $\alpha$ and $\beta$ are both dependent on $q$. Therefore, (21) is an implicit function of $q$ with only one independent variable of either $Z_1$ or $Z_2$. If $Z_1$ (or $Z_2$) is given, we can solve (21) for $q$ and $Z_2$ (or $Z_1$). Then, the minimum $q$ and the corresponding optimum $Z_1$ and $Z_2$ can be found. This can be done graphically or numerically.

For a conduction-cooled PCL ($f = 0$), the constrained heat leak equation can be obtained from (13), (19), and (20)

$$
\begin{aligned}
q_{f=0} &= \left( T_r - \frac{M_0 Z_2^2}{2} - T_c \cos \beta_0 Z_1 \right) \\
& \quad \times \frac{\beta_0}{\sin \beta_0 Z_1} \tag{22a}
\end{aligned}
$$

$$
T_r - \frac{M_0 Z_2^2}{2} = \frac{M_0 Z_2 + \frac{T_c \beta_0}{\sin \beta_0 Z_1}}{\eta + \beta_0 \cot \beta_0 Z_1}. \tag{22b}
$$

Different from (21), (22) becomes an explicit function of $q$ because $\beta_0$ is independent of $q$. It is, therefore, much easier to solve (22) than (21).

²MELCOR, USA: http://www.melcor.com
³At small $\alpha$, we have $1 - e^{-2\alpha Z_2} = 2\alpha Z_2$, and the first term on the right-hand side (RHS) of (17) is, thus, reduced to $M_0 Z_2$.

<table>
<thead>
<tr>
<th colspan="7">PCL</th>
<th colspan="5">All-Cu lead</th>
</tr>
<tr>
<th>f</th>
<th>Z₁</th>
<th>Z₂</th>
<th>Tⱼ</th>
<th>q</th>
<th>pₙₑₜ</th>
<th>p<sup>c</sup><sub>tot</sub></th>
<th>Z₁</th>
<th>q</th>
<th>pₙₑₜ</th>
<th>p<sub>tot</sub></th>
<th>t<sup>a</sup></th>
</tr>
<tr>
<th></th>
<th>V⁻¹K</th>
<th>V⁻¹K</th>
<th>K</th>
<th>mWA⁻¹</th>
<th>mWA⁻¹</th>
<th>mWA⁻¹</th>
<th>V⁻¹K</th>
<th>mWA⁻¹</th>
<th>mWA⁻¹</th>
<th>mWA⁻¹</th>
<th>%</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>5900</td>
<td>3207</td>
<td>216.97</td>
<td>33.461</td>
<td>90.461</td>
<td>425.071</td>
<td>8380</td>
<td>45.384</td>
<td>45.384</td>
<td>499.224</td>
<td>26.27</td>
</tr>
<tr>
<td>0.2</td>
<td>6200</td>
<td>3321</td>
<td>213.93</td>
<td>29.698</td>
<td>93.620</td>
<td>390.596</td>
<td>8960</td>
<td>38.843</td>
<td>47.896</td>
<td>436.322</td>
<td>23.54</td>
</tr>
<tr>
<td>0.4</td>
<td>6460</td>
<td>3420</td>
<td>211.31</td>
<td>26.829</td>
<td>96.336</td>
<td>364.629</td>
<td>9460</td>
<td>34.125</td>
<td>50.033</td>
<td>391.282</td>
<td>21.38</td>
</tr>
<tr>
<td>0.6</td>
<td>6700</td>
<td>3506</td>
<td>209.08</td>
<td>24.557</td>
<td>98.729</td>
<td>344.298</td>
<td>9920</td>
<td>30.543</td>
<td>51.900</td>
<td>357.330</td>
<td>19.60</td>
</tr>
<tr>
<td>0.8</td>
<td>6900</td>
<td>3588</td>
<td>206.92</td>
<td>22.704</td>
<td>100.872</td>
<td>327.914</td>
<td>10320</td>
<td>27.721</td>
<td>53.566</td>
<td>330.771</td>
<td>18.10</td>
</tr>
<tr>
<td>1</td>
<td>7100</td>
<td>3659</td>
<td>205.12</td>
<td>21.160</td>
<td>102.820</td>
<td>314.415</td>
<td>10700</td>
<td>25.433</td>
<td>55.073</td>
<td>309.401</td>
<td>16.80</td>
</tr>
<tr>
<td colspan="7">36.76%<sup>b</sup></td>
<td colspan="5">43.96%<sup>b</sup></td>
</tr>
</tbody>
</table>

(a) $t$ denotes the decreased percentage of heat leak of a PCL compared to an all-Cu lead.
(b) The two numbers indicate the decreased percentage of heat leak at $f = 1$ compared to $f = 0$.
(c) The COP of real refrigerators in (26) is 0.1.

In the case of a gas-cooled all-Cu lead ($f \neq 0$), the constrained heat leak equation is given by

$$
q=\frac{T_{r} \beta}{\left(e^{\alpha Z_{1}} \sin \beta Z_{1}\right)}+T_{c}\left(\alpha-\beta \cot \beta Z_{1}\right) \tag{23a}
$$

$$
T_{r}\left(\alpha+\beta \cot \beta Z_{1}\right)=\frac{T_{c} \beta e^{\alpha Z_{1}}}{\sin \beta Z_{1}}. \tag{23b}
$$

The last constraint condition is derived from the zero temperature gradient at the hot end of Cu leads [3], [4]. Please note that the solved $q$ and $Z_1$ from (23) have already been their respective optimums. At $f = 0$, (23) is reduced to

$$
q_{f=0, \min }=\beta_{0} \sqrt{T_{r}^{2}-T_{c}^{2}} \tag{24a}
$$

$$
\cos \beta_{0} Z_{1, \mathrm{opt}}=\frac{T_{c}}{T_{r}}. \tag{24b}
$$

Fig. 3 illustrates the graphic relations of $Z_2$ and $q$ against $Z_1$ for both PCLs and all-Cu leads at $f = 0$ and 1, respectively. As $f$ varies between 0 and 1, optimum performance figures are summarized in Table I. With the increase of $f$, the minimum heat leak is reduced for both the PCL and the all-Cu lead. However, the optimum $Z_1$ for Cu leads and the optimum $Z_2$ for TE elements should be increased. PCLs can always decrease the heat leak by more than 16% relative to corresponding all-Cu leads. Moreover, the smaller $f$, the larger reduction is received.

Fig. 4 comprises temperature profiles at $f = 0$ and 1 when current leads are operated optimally. The abscissas are normalized by their respective optimums as presented in Table I. Note that the abscissa of Cu leads has been shifted left by unity, such that the temperature is successive at the junction between the Cu lead and the TE element in a PCL. It is clearly the temperature decrease along the entire current lead that reduces the heat leak, when it is gas-cooled.

![](./images/812402027278630913_4.jpg)

Fig. 4. Temperature profiles for PCLs and all-Cu leads at $f = 0$ and 1, respectively.

### IV. INPUT POWER

Aside from the heat leak, the input power of current leads is another important performance figure in the design of superconducting magnet systems. For a current lead, the net input power per unit current $p_{\text{net}}$ indicates the energy loss solely due to Joule heating. However, if we should account for the required room-temperature refrigeration power so as to provide the cooling rate equal to the heat leak, the total input power $p_{\text{net}}$ (per unit current) is actually what we really care.

Since the electrical resistivity of Cu leads is dependent on temperature, it is not easy to compute $p_{\text{net}}=\int I \rho d x / A$ directly. However, if we consider the thermal exchange between the current lead and the nitrogen gas, we can find

$$
p_{\text{net}}=q+r+f q u\left(T_{r}-T_{c}\right) \tag{25}
$$

where $r$ denotes the thermal communication per unit current between the surrounding and the current lead at the room-temperature end, and for PCLs $r=\left|(-d T / d z+\eta T)_{T E, z=Z_{2}}\right|$ while for all-Cu leads $r=\left|(-d T / d z)_{C u, z=Z_{1}}\right|$. The total input power is given by

$$
p_{\text{tot}}=p_{\text{net}}+\frac{q}{\mathrm{COP}} \tag{26}
$$

where COP is the coefficient of performance of refrigerators operating between $T_c$ and $T_r$.

Generally, the term associated with heat leak $q$ dominates the total input power $p_{\text{tot}}$, because the COP in (26) is usually very small in reality. For example, the efficiency of a real refrigerator operated between 77 K–300 K is typically 0.1 (the efficiency of a Carnot refrigerator operated in the same temperature range is

$77/(300 - 77) = 0.345$ [6]. In other words, as long as $q$ is minimized, $p_{\text{net}}$ is probably the minimum in the mean time. Of course, it is just our assumption. The real solution should be finally based on the optimization of (26). Moreover, the boundary condition with zero temperature gradient at the room temperature end of Cu leads or PCLs might not be valid any more.

As $f$ varies between 0 and 1, the *net* input power $p_{\text{net}}$ and the total input power $p_{\text{tot}}$ at the mode of minimum heat leak are listed in Table I. One can see that when current leads are operated at minimum heat leak, only at small $f$ including $f = 0$ for conduction-cooled leads, is the total input power of a PCL lower than that of an all-Cu lead. It might be due to the operating mode. We will discuss the optimization of total input power elsewhere. However, at least one thing is clear: PCLs prefer to the conduction-cooled applications.

## V. TEMPERATURE-ENTROPY DIAGRAMS

In this section, we apply the recently derived T-s formulation for TE devices [10], [11] to the present gas-cooled PCLs. We have successfully constructed T-s diagrams for conduction-cooled PCLs, on which both heat leak and input power can be easily identified from areas subtended by the isotherms [3], [4].

At a steady state operating condition, the general entropy balance equation is given by [10]

$$
T\nabla \cdot \mathbf{J}_s = -\nabla \cdot \mathbf{J}_q + T\left[\sigma_{\text{tot}} - \mathbf{J}_q \cdot \nabla\left(\frac{1}{T}\right)\right] \tag{27}
$$

where $\mathbf{J}_s$ is the internal entropy flux density circulating within a thermodynamic cycle that we intend to track, $\mathbf{J}_q$ the heat flux density for the thermal exchange between the working fluid and reservoirs that one cares, and $\sigma_{\text{tot}}$ the rate of total entropy generation per unit volume that includes the thermal communication $\mathbf{J}_q$. According to the irreversible thermodynamics of thermoelectricity and an Onsager reciprocal relation [12], one can have

$$
\mathbf{S} \equiv A\mathbf{J}_s = \frac{-kA\nabla T}{T} + \mathbf{I}\eta \equiv \frac{\mathbf{Q}}{T} \tag{28}
$$

$$
\sigma_{\text{tot}} = -k\nabla T \cdot \nabla\left(\frac{1}{T}\right) + \frac{\mathbf{I} \cdot \mathbf{I}\rho}{(A^2T)} \tag{29}
$$

where $\mathbf{S}$ is the entropy flux in a given control volume of the working fluid. Obviously, the two terms on the RHS of (29) represent the rates of entropy generation due to heat conduction and Joule heating, respectively.

We select in turn the p-type PCL, the external power source, the n-type PCL and the superconducting magnet to complete a thermodynamic cycle. At the interface between PCLs and the superconducting magnet, (27) reduces to

$$
T_c\nabla \cdot \mathbf{J}_s = -\nabla \cdot \mathbf{J}_q \text{ or } T_c\nabla \cdot \mathbf{S} = -\nabla \cdot \mathbf{w} \tag{30}
$$

where $\mathbf{w}$ is the heat flux leaking into the superconducting magnet or the liquid nitrogen (i.e., the cold reservoir), and $w = |\mathbf{w}|$. At the interface between PCLs and the external power source, a similar equation to (30) can be obtained

$$
T_r\nabla \cdot \mathbf{S} = -\nabla \cdot \mathbf{R} \tag{31}
$$

where $\mathbf{R}$ is the heat flux rejected into the hot reservoir, and $r = |\mathbf{R}| / I$.

![](./images/812402027278630913_5.jpg)

Fig. 5. T-s diagrams for gas-cooled PCLs and all-Cu leads at $f = 1$.

To be identical with previous definition of symbols, (28) is rewritten as the following 1-D form:

$$
s = \frac{-\left(\frac{dT}{dz}\right)}{T} + \eta \tag{32}
$$

where $s = |\mathbf{S}| I$. Therefore, when the temperature distribution is found, T-s relation can be established parametrically via their spatial dependence.

From (30) and (31), we notice that the areas subtended by the cold and hot isotherms on the T-s plane now indicate the heat leak $q$ and heat rejection $r$ in (25), respectively. As all other parameters in (25) and (26) are known, we can make the conclusion that the T-s diagram can identify both the heat leak and the input power of current leads freely.

Fig. 5 constitutes T-s plots for gas-cooled PCLs and all-Cu leads at $f = 1$. The graphic identifications of the principal energy flows such as $q$ and $r$ are illustrated. The insertion of TE elements decreases the hot end temperature of Cu leads, and should reduce the heat leak at the cold end of Cu leads theoretically. However, TE elements also release heat to Cu leads, which can be ascertained from the T-s return circuit at the junction between TE and Cu as labeled in Fig. 5. This effect will definitely increases the heat leak. The real factor resulting in the reduction of heat leak in PCLs is attributed to the shift of T-s curves. From Fig. 5, one can see the n- and p-type TE elements both shift the T-s curves of all-Cu leads to smaller entropy flows. While the shift lowers the heat leak at the cold end of Cu leads, it produces dissipative heat meanwhile at the room temperature end of TE elements. Consequently, the less heat leaking into superconducting magnets is gained at the cost of more input power.

According to Fig. 5, we can now do some quantitative comparisons to clarify the effect of TE elements in PCLs. Detailed performance data should be referred to Table I. The reduction of heat leak $2q$ of PCLs⁴ relative to all-Cu leads can be discerned simply from the area difference underneath the straight lines

⁴Note that the T-s diagram consists of two PCLs, one is with n-type TE element and the other is with p-type TE elements as labeled in Fig.5

![](./images/812402027278630913_6.jpg)

Fig. 6. Comparison of T-s diagrams for PCLs and all-Cu leads at $f=0$ and 1, respectively.

(i.e., cold isotherms) $3' \to 4'$ and $3 \to 4$, which are $2 \times 25.433$ mW/A and $2 \times 21.160$ mW/A, respectively. The heat exchange $2r$ at the room temperature end is zero for all-Cu leads, and $2 \times 57.000$ mW/A for PCLs that are represented by the area below the line $1 \to 2$. Therefore, the net input power in (25) is definitely increased when TE elements are inserted into the hot end of Cu leads.

Fig. 6 comprises T-s graphs for PCLs and all-Cu leads with and without gas cooling, respectively. In [3], we have demonstrated that the area below the straight line $5' \to 6'$ is exactly the net input power $p_{\text{net}}$ of conduction-cooled Cu leads, while the area sum underneath lines $5 \to 6$ and $1 \to 2$ is the $p_{\text{net}}$ for conduction-cooled PCLs. This fact can also be extracted from (25) at $f=0$. For the present case of gas-cooled current leads, the gas cooling term related to $f$ in the net input power $p_{\text{net}}$ cannot be identified directly from the T-s diagram. However, it is reflected by the reduction of heat leak, for example, from the line $5' \to 6'$ to $3' \to 4'$ for all-Cu leads. In addition, the effect of gas cooling is more significant for all-Cu leads compared with PCLs, which has been demonstrated in Table I.

### VI. CONCLUSION

We have performed the optimization of nitrogen gas-cooled PCLs and all-Cu leads as well. The objective is to minimize their resulting heat leaking into superconducting magnets. With the effect of gas cooling on the TE element in a PCL being accounted for, a general analytical formula for the heat leak has been derived. The heat leak of conduction-cooled PCLs can be easily determined from this formula. Moreover, the T-s formulation has been successfully applied to the present PCL's. The heat leak and the input power of a PCL can be easily discerned from areas subtended by the isotherms in the T-s diagram.

In this work, the reduction of heat leak is always 16%–26% when PCLs are employed to replace conventional all-Cu leads, no matter how efficiently they are cooled by nitrogen gas (i.e., varying $f$ from 0 to 1). If helium gas flows past current leads, however, this reduction will be much smaller. That is because the value of $u=C_p/C_L$ for helium gas is far higher than for nitrogen gas. Namely, helium gas can provide much more effective cooling. For example, if helium gas cools a PCL (still TE + Cu) operating between 4.2 K–300 K, the reduction of heat leak is only 3.46% at $f=1$ or 7.27% at $f=0.2$ compared with an all-Cu lead. The corresponding reduction is 26.86% at $f=0$. Therefore, the PCL prefers to applications requiring conduction-cooled current leads, such as the electrical connection to infrared detectors in remote sensing instruments [4].

### REFERENCES

[1] M. N. Wilson, *Superconducting Magnets*. London, U.K.: Clarendon, 1983, pp. 256–78.

[2] S. Yamaguchi, K. Takita, and O. Motojima, “A proposal for a peltier current lead,” in *Proc. 16th Int. Cryogenics Engineering Conf.*, 1996, pp. 1159–1162.

[3] X. C. Xuan, K. C. Ng, C. Yap, and H. T. Chua, “Optimization and thermodynamic understanding of conduction-cooled peltier current leads,” *Cryogenics*, vol. 42, no. 2, pp. 141–145, 2002.

[4] ——, “On minimizing the heat leak of current leads in cryogenic vacuum systems,” *Cryogenics*, vol. 42, no. 12, pp. 779–785, 2002.

[5] H. Okumura and S. Yamaguchi, “One dimensional simulation for peltier current leads,” *IEEE Trans. Appl. Supercond.*, vol. 7, pp. 715–8, June 1997.

[6] L. W. Whitlow, A. Yamamoto, and T. Ohta, “Computational analysis of peltier current leads,” in *Proc. 17th Int. Conf. Thermoelectrics*, Nagoya, Japan, 1998, pp. 64–8.

[7] K. Sato, H. Okumura, and S. Yamaguchi, “Numerical calculations of peltier current designing,” *Cryogenics*, vol. 41, pp. 497–503, 2001.

[8] H. Goldsmid, *Electronic Refrigeration*. London, U.K.: Pion, 1986.

[9] G. D. Mahan, “Inhomogeneous thermoelectrics,” *J. Appl. Phys.*, vol. 70, no. 8, pp. 4551–4554, 1991.

[10] H. T. Chua, K. C. Ng, X. C. Xuan, C. Yap, and J. M. Gordon, “Temperature-entropy formulation of thermoelectric thermodynamic cycles,” *Phys. Rev. E, Stat. Phys. Plasmas Fluids Relat. Interdiscip. Top.*, vol. 65, pp. 056111-1–056111-6, 2002.

[11] X. C. Xuan, K. C. Ng, C. Yap, and H. T. Chua, “A general model for studying effects of interface layers on thermoelectric devices performance,” *Int. J. Heat Mass Trans.*, vol. 45, no. 26, pp. 5159–5170, 2002.

[12] S. R. De Groot and P. Mazur, *Non-Equilibrium Thermodynamics*. Amsterdam, The Netherlands: North-Holland, 1962, pp. 338–55.

![](./images/812402027278630913_7.jpg)

Xiangchun Xuan was born in Anhui, China, on February 15, 1973. He received the B.E. degree in engineering thermophysics from the University of Science and Technology of China, Hefei, Anhui, China, in 1995, and the D.E. degree in physical electronics from Shanghai Institute of Technical Physics, Chinese Academy of Sciences, Shanghai, China, in 2000. He is currently working toward the Ph.D degree at the Department of Mechanical and Industrial Engineering, University of Toronto, Toronto, ON, Canada.

His current research is focused on the microfluidic transport phenomena.