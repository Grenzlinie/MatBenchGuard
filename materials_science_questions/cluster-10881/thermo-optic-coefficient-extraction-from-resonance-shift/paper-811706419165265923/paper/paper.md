# Influence of heat transfer on thermal effects of the end-pumped laser crystal*

ZHANG Yin-ke(张引科)**, HE Yan-ping(贺艳平), ZAN Hui-ping(昝会萍), and YANG Hao(杨浩)
School of Science, Xi'an University of Architecture and Technology, Xi'an 710055, China

(Received 16 June 2010)
©Tianjin University of Technology and Springer-Verlag Berlin Heidelberg 2010

A thermal model of crystal is established. The temperature field differential equation of the diode-end-pumped laser crystal with circular cross-section and new boundary conditions, in which the convection heat transfer is supposed to exist between laser crystal ends and air, is established. The analytical expressions of temperature field, thermal distortion and additional optical path difference (OPD) of crystal are obtained. By numerical calculation, the influence of heat transfer on the thermal effects of laser crystal Nd:YAG is studied. Results show that crystal's thermal effects, including temperature field, thermal distortion, OPD and thermal focal length, are all weakened as the heat transfer through ends of crystal is strengthened. This conclusion could be used to control thermal effects of laser crystal and improve laser working stability.

Document code: A Article ID: 1673-1905(2010)06-0439-4
DOI 10.1007/s11801-010-9137-0

Diode-pumped solid-state lasers are efficient, compact and stable. They are widely used in fields such as industry, communication, medicine and scientific research $^{[1]}$. As the laser crystal absorbs pump light energy and emits fluorescence radiation, a fraction of absorbed energy is converted to heat energy. It is the heat energy that results in non-uniform temperature rise in crystal. Because the pump light is limited in a small part of crystal, the thermal effects are inevitable $^{[2]}$. Thermal effects seriously affect mode matching between pump light and oscillating laser, and cause dropping of optical conversion efficiency $^{[3]}$.

The temperature field of end-pumped laser crystal has been investigated $^{[4-7]}$. But most researchers supposed that the side face of laser crystal had constant temperature and the end faces were adiabatic. However, research results show that the temperature rise of pumped end is often greater than $100\ ^{\circ}\text{C}$. So there must be heat transfer between pumped end and outside air. In this paper, based on the analysis of working state of diode-end-pumped Nd:YAG crystal, a more realistic thermal model is built. Under the new boundary conditions, the analytical expression of temperature field of end-pumped laser crystal with circular cross-section is obtained and the influence of heat transfer on temperature field, thermal distortion and OPD is also discussed.

The thermal model of diode-end-pumped Nd:YAG crystal is shown in Fig.1. The radius and length of the crystal are $R$ and $L$, respectively. The origin of coordinate system is located at the center of pumped end. There is a reflection reducing film for wavelengths 808 nm and 1064 nm on the pumped end. The pump light propagates forward along $z$-axis. The circulating cooling-water system or semiconductor refrigeration module is used to control the temperature of crystal side face.

![](./images/811706419165265923_1.jpg)

Fig.1 Schematic diagram of the circulating water-cooling laser crystal rod

The pump light from fiber-coupling semiconductor laser passes through an optical system consisting of a plane-convex lens or a coupler composed of self-focusing system and gets to the pumped end of laser crystal. The spatial distribution of pump light intensity could be approximately expressed by Gaussian function $^{[8]}$. The intensity distribution of pump

---
* This work has been supported by the Basic Research Grant Fund of Shaanxi Province Government of China (No.2007A15).
** E-mail: yinkezhang@163.com

light at the pumped end (plane $z=0$) is described by

$$
I(r, 0)=I_{0} \mathrm{e}^{-2 r^{2} / \omega^{2}}, \tag{1}
$$

where $\omega$ is the Gaussian radius of pump light, and $I_{0}$ is the intensity at the center of pumped end and given by

$$
I_{0}=\frac{P}{2 \pi \int_{0}^{\infty} \mathrm{e}^{-2 r^{2} / \omega^{2}} r \mathrm{~d} r}=\frac{2 P}{\pi \omega^{2}}, \tag{2}
$$

where $P$ is the power of pump light.

The absorption coefficient of crystal for pump light is $\beta$. The intensity of pump light decreases as the distance of transmission in crystal increases. According to absorption law, the pump light intensity on $z=z$ plane is

$$
I(r, z)=I(r, 0) \mathrm{e}^{-\beta z}. \tag{3}
$$

The absorbed pump light energy caused by fluorescence quantum effect and inner absorption loss of crystal is much greater than that caused by others. Therefore, only the former is considered. The heat power density on $z=z$ plane absorbed by crystal is

$$
q_{v}(r, z)=\eta \beta I(r, z)=\eta \beta I_{0} \mathrm{e}^{-2 r^{2} / \omega^{2}-\beta z}, \tag{4}
$$

where $\eta$ is heat conversion factor decided by fluorescence quantum effect and inner absorption loss, and given by

$$
\eta=1-\lambda_{\mathrm{p}} / \lambda_{\mathrm{L}}, \tag{5}
$$

in which $\lambda_{\mathrm{p}}$ is the wavelength of pump light and is equal to 808 nm, and $\lambda_{\mathrm{L}}$ is the wavelength of oscillating laser and is equal to 1064 nm.

Since the side face of laser crystal is cooled by circulating-water, its temperature can be supposed to be constant and equal to $u_{w}$, which is the temperature of circulating-water. For convenience, the relative temperature of side face is set to be zero. The actual temperature in crystal could be obtained by adding $u_{w}$ to the calculated relative temperature. Two ends of crystal are contacted with air, so the boundary conditions of convection heat transfer are adopted.

The temperature field in crystal obeys Poisson equation. Both thermal model and heat source have axial symmetry, so temperature field $u(r, \ddot{o}, z)$ is independent of $\ddot{o}$. The heat conduction equation and boundary conditions are given by

$$
\frac{\partial^{2} u}{\partial r^{2}}+\frac{1}{r} \frac{\partial u}{\partial r}+\frac{\partial^{2} u}{\partial z^{2}}=-\frac{q_{v}}{\lambda}, \tag{6}
$$

$$
\left.u\right|_{r=R}=0,\left.u\right|_{r=0}<+\infty, \tag{7}
$$

$$
\left.\left(-\frac{\partial u}{\partial z}+\sigma u\right)\right|_{z=0}=\sigma T,\left.\quad\left(\frac{\partial u}{\partial z}+\sigma u\right)\right|_{z=L}=\sigma T, \tag{8}
$$

where $\lambda$ is the coefficient of crystal heat conductivity, $T$ is the relative temperature of surrounding air, $h$ is the heat conduction coefficient of air, and $\sigma=h / \lambda$.

The above equations cannot be solved by general method due to the complexity of $q_{v}$ and boundary conditions. Here a novel method is proposed. Detail steps are as follows.

Firstly, the eigenfunctions of heat conduction Eq.(6) can be determined according to boundary conditions. Secondly, general solution $u(r, z)$ composed of eigenfunctions is substituted into Eq.(6) to calculate undetermined constants. $u(r, z)$ satisfies both the equation and the boundary conditions. Therefore it must be the unique solution of Eq.(6). The expression of temperature field in laser crystal is given by

$$
\begin{aligned}
u(r, z)= & \sum_{n=1}^{\infty}\left[A_{n} \operatorname{ch}\left(\frac{\alpha_{n} z}{R}\right)+B_{n} \operatorname{sh}\left(\frac{\alpha_{n} z}{R}\right)+\right. \\
& \left.\frac{R}{\alpha_{n}} \int_{0}^{z} \operatorname{sh}\left(\frac{\alpha_{n}}{R} z-\frac{\alpha_{n}}{R} \tau\right) f_{n}(\tau) \mathrm{d} \tau\right] J_{0}\left(\frac{\alpha_{n}}{R} r\right),
\end{aligned} \tag{9}
$$

where

$$
A_{n}=\frac{-\sigma \phi_{n}^{\prime}(0) \operatorname{sh}\left(\frac{\alpha_{n}}{R} L\right)-\frac{\alpha_{n}}{R} \phi_{n}^{\prime}(0) \operatorname{ch}\left(\frac{\alpha_{n}}{R} L\right)+\frac{\alpha_{n}}{R} \phi_{n}^{\prime}(L)+P_{n}}{\sigma^{2} \operatorname{sh}\left(\frac{\alpha_{n}}{R} L\right)+\left(\frac{\alpha_{n}}{R}\right)^{2} \operatorname{sh}\left(\frac{\alpha_{n}}{R} L\right)+2 \sigma \frac{\alpha_{n}}{R} \operatorname{ch}\left(\frac{\alpha_{n}}{R} L\right)}, \tag{10}
$$

$$
B_{n}=\frac{\frac{\alpha_{n}}{R} \phi_{n}^{\prime}(0) \operatorname{sh}\left(\frac{\alpha_{n}}{R} L\right)+\sigma \phi_{n}^{\prime}(0) \operatorname{ch}\left(\frac{\alpha_{n}}{R} L\right)+\sigma^{2} \phi_{n}(L)+Q_{n}}{\sigma^{2} \operatorname{sh}\left(\frac{\alpha_{n}}{R} L\right)+\left(\frac{\alpha_{n}}{R}\right)^{2} \operatorname{sh}\left(\frac{\alpha_{n}}{R} L\right)+2 \sigma \frac{\alpha_{n}}{R} \operatorname{ch}\left(\frac{\alpha_{n}}{R} L\right)}, \tag{11}
$$

$$
\phi_{n}(z)=\frac{R}{\alpha_{n}} \int_{0}^{z} \operatorname{sh}\left(\frac{\alpha_{n} z}{R}-\frac{\alpha_{n} \tau}{R}\right) f_{n}(\tau) \mathrm{d} \tau, \tag{12}
$$

$$
f_{n}(z)=\frac{2 q_{v}}{\lambda R^{2}\left[J_{0}^{\prime}\left(\alpha_{n}\right)\right]^{2}} \int_{0}^{R} r J_{0}\left(\frac{\alpha_{n} r}{R}\right) \mathrm{d} r, \tag{13}
$$

$$
\begin{aligned}
P_{n}= & \sigma \phi_{n}^{\prime}(L)-\frac{2 \sigma \alpha_{n} T}{R \alpha_{n} J_{0}^{\prime}\left(\alpha_{n}\right)} \operatorname{sh}\left(\frac{\alpha_{n}}{R} L\right)- \\
& \frac{2 \sigma^{2} T}{\alpha_{n} J_{0}^{\prime}\left(\alpha_{n}\right)} \operatorname{ch}\left(\frac{\alpha_{n}}{R} L\right)+\frac{2 \sigma^{2} T}{\alpha_{n} J_{0}^{\prime}\left(\alpha_{n}\right)},
\end{aligned} \tag{14}
$$

$$
Q_{n}=\frac{2 \sigma^{2} T}{\alpha_{n} J_{0}^{\prime}\left(\alpha_{n}\right)} \operatorname{sh}\left(\frac{\alpha_{n}}{R} L\right)+\frac{2 \sigma \alpha_{n} T}{R \alpha_{n} J_{0}^{\prime}\left(\alpha_{n}\right)} \operatorname{ch}\left(\frac{\alpha_{n}}{R} L\right)+\frac{2 \sigma \alpha_{n} T}{R \alpha_{n} J_{0}^{\prime}\left(\alpha_{n}\right)}, \tag{15}
$$

where $J_{0}$ and $J_{1}$ denote the zeroth rank and the first rank Bessel functions, respectively, and $\alpha_{n}$ denotes the $n$th zero point of $J_{0}$.

The power of pump light from diode laser is 20 W. The relative temperature of surrounding air is $5^{\circ} \mathrm{C}$. The Gaussian radius of pump beam is 0.32 mm. Parameters of crystal are shown in Tab.1. The distributions of calculated temperature fields in laser crystal are shown in Fig.2.

<table><caption>Tab.1 Physical properties of Nd:YAG crystal</caption>
<thead>
  <tr>
    <th>Parameters</th>
    <th>Values</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Diameter ($R$)</td>
    <td>3 mm</td>
  </tr>
  <tr>
    <td>Length ($L$)</td>
    <td>2 mm</td>
  </tr>
  <tr>
    <td>$\text{d}n/\text{d}t$</td>
    <td>$7.3 × 10^{-5}$/K</td>
  </tr>
  <tr>
    <td>Absotption coefficient ($\beta$)</td>
    <td>$20.7\ \text{cm}^{-1}$</td>
  </tr>
  <tr>
    <td>Thermal expansion ($\alpha$)</td>
    <td>$8.2 × 10^{-5}$/K</td>
  </tr>
  <tr>
    <td>Heat conductivity ($\lambda$)</td>
    <td>$13\ \text{Wm}^{-1}\text{K}^{-1}$</td>
  </tr>
  <tr>
    <td>Refractive index ($n_0$)</td>
    <td>1.82</td>
  </tr>
</tbody>
</table>

![](./images/811706419165265923_2.jpg)

Fig.2 Temperature field distribution on the cross section along crystal axis

The temperature along $z$-axis decreases quickly. When the pumped end is considered to be adiabatic ($\sigma = 0$), the maximum temperature occurs at the center of pumped end and is equal to $142.7\ \mathrm{^\circ C}$. When the heat transfer exists between ends and air ($\sigma = 0.6$), the maximum temperature occurs at the center of pumped end and is equal to $117.6\ \mathrm{^\circ C}$. The maximum temperature drops by $25.1^\circ\text{C}$ compared with that under $\sigma$=0. Supposing that the value of $\sigma$ tends to infinity (i.e. temperatures of ends and air are the same), the maximum temperature is at point $(0, 0.34)$ and is equal to $62.6\ \mathrm{^\circ C}$. Obviously, the heat transfer has influence on temperature distribution in crystal. When heat transfer is more intensive, which corresponds to greater value of $\sigma$, the temperature rise at the center of pumped end gets lower. So thermal effects could be weakened by strengthening heat transfer.

The initial temperature of crystal is supposed to be zero. In steady working state, the temperature rise at point $(r, z)$ is $u(r, z)$. It is the non-uniform temperature rise that causes thermal distortion. The thermal expansion of line element $\text{d}z$ along $z$-axis at that point is
$$\mathrm{d}l_{z}=\alpha u\left(r,z\right)\mathrm{d}z\,, \tag{16}$$
where $\alpha$ is the coefficient of thermal expansion of laser crystal along $z$-axis. The total thermal distortion (heave height) of crystal along $z$-axis is
$$l_{z}(r)=\alpha \int_{0}^{L} u(r, z) \mathrm{d} z \. \tag{17}$$

The thermal distortion distributions at pumped end of crystal with different values of $\sigma$ are shown in Fig.3. The thermal distortion in pumped area is most serious, and that near the edge of pumped end is less. The maximum thermal distortion occurs at the center of pumped end. When $\sigma$ is 0, 0.6 and $\infty$, the maximum thermal distortion of pumped end is $0.99\ \mathrm{\mu m}$, $0.88\ \mathrm{\mu m}$ and $0.52\ \mathrm{\mu m}$, respectively. So under ordinary conditions, the thermal distortion at center of pumped end is in the range from $0.99\ \mathrm{\mu m}$ to $0.52\ \mathrm{\mu m}$. The results show that thermal distortion decreases with the increase of $\sigma$.

![](./images/811706419165265923_3.jpg)

Fig.3 Thermal distortion distribution of Nd:YAG crystal at, the pumped end

The thermal lens effect mainly depends on thermal expansion of laser crystal, the variation of refractive index resulting from thermal gradient and thermally induced birefringence. All these factors cause OPD. The thermal focal length can be derived from OPD along crystal axis⁽⁹⁾. The OPD is given by
$$\begin{aligned}
\text{OPD} & = \text{OPD}_{1} + \text{OPD}_{2} + \text{OPD}_{3}= \\
& \int_{0}^{L} \frac{\partial n}{\partial u} u(r, z) \mathrm{d} z + (n_{0}-1) \alpha \int_{0}^{L} u(r, z) \mathrm{d} z + \sum_{i,j=10}^{2} \int_{0}^{L} \frac{\partial n}{\partial \varepsilon_{i,j}} \varepsilon_{i,j}(r, z) \mathrm{d} z,
\tag{18}
\end{aligned}$$
where $n$ and $n_0$ denote refractive indices of crystal at temperature $u$ and at initial temperature, respectively; $\varepsilon_{i,j}$ denotes strain tensor of laser crystal; $\varepsilon_{r}, \varepsilon_{\theta}$ and $\varepsilon_{z}$ denote thermal strains along radial, tangent and axial directions, respectively.

The optical-elastic coefficients $p_{11}, p_{12}$ and $p_{44}$ are used to describe optical-elastic effects, and here $p_{11} = -0.0290$, $p_{12} = 0.0091$ and $p_{44} = -0.0615$. The crystal refractive index gradients by strain are given by⁽¹⁰⁾
$$\frac{\partial n}{\partial \varepsilon_{r}}=-\frac{n_{0}^{3}}{12}\left(3 p_{11}+3 p_{12}+6 p_{44}\right), \tag{19}$$

$$
\frac{\partial n}{\partial \varepsilon_{\theta}}=-\frac{n_{0}^{3}}{12}\left(p_{11}+5 p_{12}-2 p_{44}\right),\qquad(20)
$$

$$
\frac{\partial n}{\partial \varepsilon_{z}}=-\frac{n_{0}^{3}}{12}\left(2 p_{11}+4 p_{12}-4 p_{44}\right).\qquad(21)
$$

$\text{OPD}_3$ is as follows

$$
\mathrm{OPD}_{3}=\int_{0}^{L}\left(\frac{\partial n}{\partial \varepsilon_{r}} \varepsilon_{r}+\frac{\partial n}{\partial \varepsilon_{\theta}} \varepsilon_{\theta}+\frac{\partial n}{\partial \varepsilon_{z}} \varepsilon_{z}\right) \mathrm{d} z.\qquad(22)
$$

The OPD along $z$-axis of crystal is shown in Fig.4. It can be found that corresponding to $\sigma=0$, $\sigma=0.6$ and $\sigma=\infty$, OPD are $1.78\ \mu\text{m}$, $1.57\ \mu\text{m}$ and $0.94\ \mu\text{m}$, respectively. Evidently OPD is dependent on heat transfer condition. And OPD decreases in the range from $1.78\ \mu\text{m}$ to $0.94\ \mu\text{m}$ as $\sigma$ increases.

![](./images/811706419165265923_4.jpg)

Fig.4 OPD distribution of Nd:YAG crystal

The end-pumped laser crystal can be described as an ideal thin lens with effective thermal focal length $f$. The lens is located at the center of laser crystal. And its thermal focusing properties depend on additional phase difference caused by the thermal effects

$$
\Delta \phi=k \times \text{OPD}.\qquad(23)
$$

The relation between $\Delta \phi$ and $f$ is $^{[5]}$

$$
\Delta \phi=\frac{k r^{2}}{2 f}.\qquad(24)
$$

So the effective thermal focal length is

$$
f=\frac{r^{2}}{2 \mathrm{OPD}},\qquad(25)
$$

where $r$ is effective radius of pump light.

The calculated thermal focal lengths of Nd:YAG crystal are 38.5 mm, 44.2 mm and 77.6 mm, respectively, when $\sigma$ are 0, 0.6 and $\infty$. The greater the thermal focal length, the less the influence of thermal effects on the quality of laser beams. So the heat transfer also affects the thermal lens effect.

In the paper, based on more realistic boundary conditions, the influence of heat transfer on thermal effects of end-pumped Nd:YAG crystal is investigated. Through numerical calculation, temperature field, thermal distortion, OPD and thermal focal length of laser crystal are analyzed. Research results reveal that temperature rise, thermal distortion and OPD all decrease with the increase of heat transfer.

## References

[1] LV B D, Solid-State Laser, Beijing: Beijing University of Post and Telecommunication Press, 201 (2002). (in Chinese)

[2] Wang Fei, Feng Jinliang, Wei Jianwei, Li Gang and Chen Meng, Journal of Optoelectronics•Laser 17, 219 (2006). (in Chinese)

[3] Sa Yu, Zhang Gui-zhong, Cao Qi-ming, Wang Sheng-ping and Ye Zhi-sheng, Journal of Optoelectronics • Laser 21, 256 (2010). (in Chinese)

[4] Yaakov Lumer, Inon Moshe, Zvika Horovitz, Steven Jackel, Galina Machavariani and Avi Meir, Applied Optics 47, 3886 (2008).

[5] Li Zhigang, Huai Xiulan, Tao Yujia and Guo Ziyi, Applied Optics 48, 598 (2009).

[6] T. Liu, Z. M. Yang and S. H. Xu, Optics Express 17, 12875 (2009).

[7] Yaakov Lumer, Inon Moshe, Avi Meir, Yotam Paiken, Galina Machavariani and Steven Jackel, Journal of the Optical Society of America B 24, 2279 (2007).

[8] Shi Peng, Li Long, Gans Ansheng and Chen Wen, Chin J. Lasers 33, 1324 (2006). (in Chinese)

[9] Shi Peng, Li Jin Ping, Li Long and Gan Ansheng, Chin J. Lasers 35, 643 (2008). (in Chinese)

[10] Peng Shi, Wen Chen, Long Li and Ansheng Gan, Applied Optics 46, 6655 (2007).