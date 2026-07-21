This article was downloaded by: [Aston University]
On: 10 January 2014, At: 08:34
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954
Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/811948443999141891_1.jpg)

# Integrated Ferroelectrics: An International Journal

Publication details, including instructions for
authors and subscription information:
http://www.tandfonline.com/loi/ginf20

# MODELING AND SIMULATION OF PIEZOELECTRIC MEMS ENERGY HARVESTING DEVICE

J. H. LIN $^{a}$ , X. M. WU $^{a}$ , T. L. REN $^{a}$ \& L. T. LIU $^{a}$

 $^{a}$ Institute of Microelectronics, Tsinghua University, Beijing, 100084, China
Published online: 20 Sep 2010.

To cite this article: J. H. LIN, X. M. WU, T. L. REN & L. T. LIU (2007) MODELING AND SIMULATION OF PIEZOELECTRIC MEMS ENERGY HARVESTING DEVICE,
Integrated Ferroelectrics: An International Journal, 95:1, 128-141, DOI:
10.1080/10584580701756649

To link to this article: http://dx.doi.org/10.1080/10584580701756649

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

Integrated Ferroelectrics, 95: 128–141, 2007
Copyright © Taylor & Francis Group, LLC
ISSN 1058-4587 print / 1607-8489 online
DOI: 10.1080/10584580701756649

![](./images/811948443999141891_2.jpg)

# Modeling and Simulation of Piezoelectric MEMS Energy Harvesting Device

J. H. Lin, X. M. Wu,* T. L. Ren, and L. T. Liu

Institute of Microelectronics, Tsinghua University, Beijing 100084, China

## ABSTRACT

Piezoelectric MEMS power generator is used to harvest energy from the ambient vibrations in the environment. This paper proposes a structure design of MEMS power generator for low-frequency applications, which is based on bulk MEMS technology and (110) Si wafer. The structure consists of a silicon cantilever with a piezoelectric layer attached. The cantilever is modeled as an Euler-Bernoulli beam with a lumped mass beneath the tip of the cantilever, and then analytical modeling and simulations are carried out using MATLAB. Simulation results show that a tradeoff between the geometric parameters and the proof mass should be made for a high output power of the device. To increase the output power, the length of piezoelectric layer can be optimized, which is not necessarily equal to that of cantilever. Simulation results point out ways to perform the optimization of MEMS power generator. The analytical modeling and simulations are also helpful for the design of macro-scale power generator.

Keywords: MEMS Power generator; Euler-Bernoulli beam; Optimization

## 1. INTRODUCTION

A great deal of attention from both industry and academia has been paid on energy harvesting technologies. Advances in low-power VLSI design open up the possibility of powering wireless sensor notes by harvesting energy from the environment. Such technologies help to break the restrictions of batteries, i.e. the need either to replace or to recharge them periodically and their large volume and weight. There are several potential sources for energy harvesting, such as thermal gradients [1], electromagnetic fields [2], radioisotope energy [3], fluid flow [4, 5]. However, mechanical vibration sources are more ubiquitous

Received June 15, 2007; accepted September 30, 2007.
*Corresponding author. E-mail: imewuxm@mail.tsinghua.edu.cn

[434]/128

and easily accessible through MEMS technologies for conversion to electrical energy.

Mechanical vibrations can be converted into electrical energy mainly by three mechanisms: electro-magnetic [6,7], electrostatic [8,9], and piezoelectric [9, 10]. Piezoelectric materials are more attractive because they can efficiently convert mechanical vibration to electrical energy with relatively high output voltage but without any additional voltage source [11]. It receives a lot of focus in the field of MEMS due to its convenience of implementation by MEMS technologies.

So far, there have been a few reported studies on piezoelectric MEMS power generator [12-14]. However, they are suffering from two main prob- lems. One is their high resonant frequency. Their application scope is limited due to their high resonant frequency, which is up to the range of hundreds to kilos of hertz, since vibration sources of such high frequency aren't so ubiq- uitous. Although adding a proof mass can alleviate this problem, the manual operation results in new problems of convenience and reliability. The other is the lack of modeling and optimization for MEMS power generator. They are very important for the design and fabrication of MEMS power generator.

This paper brings forward a structure design of MEMS power generator for low-frequency applications and its modeling and simulations. The structure consists of a silicon cantilever and a PZT layer as the transducer for converting mechanical vibration to electrical energy. The cantilever is modeled as an Euler- Bernoulli beam with a lumped mass beneath the tip. Then analytical modeling and simulations, including the geometric parameters of the cantilever and the piezoelectric layer are carried out using MATLAB. General equations of the output and ways to perform optimization are both given.

## 2. MODELING

### 2.1 Structure Design of MEMS Power Generator

A structure design of MEMS power generator is proposed in Fig. 1. The structure consists of a thin-film PZT layer and a silicon cantilever. The silicon cantilever is used as support layer to carry out mechanical vibration, while the thin-film PZT layer serves as the transducer to convert mechanical vibration into electrical energy. Electrical energy will be best harvested if the cantilever resonates with the mechanical vibration. Therefore, a proof mass is added to tune the resonant frequency of the cantilever. Since the cantilever is based on (110) wafer and bulk MEMS technologies, a cubical-shaped silicon mass can be fabricated easily and simultaneously with the silicon cantilever. The technologies aren't hard to carry out, however, make great sense.

The proposed design has two main advantages when compared with those based on surface MEMS technologies. First, the curling of device won't happen

![](./images/811948443999141891_3.jpg)

Figure 1. Conceptual cross-section of piezoelectric MEMS power generator.

with silicon layer as the support layer. Therefore, much longer cantilever can be designed, which give benefits to a low resonant frequency. A low resonant frequency will extend the application scope of the MEMS power generator, since vibration sources of low frequency are more ubiquitous. Second, a proof mass beneath the cantilever can be formed easily by etching in KOH solution. KOH etching is anisotropic and the {111} flat of (110) wafer is perpendicular to the wafer surface. So the proof mass is easily formed to be cubical-shaped. The design of a cubical-shaped silicon mass saves the trouble of bonding additional mass to the cantilever, and also gives benefits to a low resonant frequency. Details of these advantages will be shown in simulations.

### 2.2 Model Solution of Euler-Bernoulli Beam

The modeling of the proposed MEMS power generator is carried out according to Euler-Bernoulli beam theory, which involves the assumptions that the rotation of the differential element is negligible compared to the translation and that the angular distortion due to shear is small in relation to the bending deformation. This theory is valid if the ratio between the length of the beam and its depth is relatively large, say more than 10, and if the beam does not become too "wrinkled" because of flexure [15].

The proposed MEMS power generator is modeled as an Euler-Bernoulli beam with a lumped mass beneath the tip. Schematic illustration of the Euler- Bernoulli beam together with coordinates is shown in Fig. 2. Assuming the Young's modulus $E$, the moment of inertia $I$, and the cross sectional area $A$ are invariant along the beam axis, dynamic behavior of the cantilever beam can be described by [16]

$$
E I \frac{\partial^{4} z(x, t)}{\partial x^{4}}+m \frac{\partial^{2} z(x, t)}{\partial t^{2}}+b \frac{\partial z(x, t)}{\partial t}=f(x, t) \tag{1}
$$

where $m=\rho A$ is the linear mass density of the beam, $\rho$ is the mass density, $b$ is the damping factor per unit length, $f(x,t)$ is force per unit length, and $z(x,t)$

![](./images/811948443999141891_4.jpg)

Figure 2. Schematic illustration of MEMS power generator with coordinates.

denotes the transverse displacement of the mass point that has distance x from the origin.

Equation (1) is separable in the spatial variable x and time t, and can be expressed in the form

$$
z(x, t)=X(x) T(t) \tag{2}
$$

In the method of separation of variables, $z(x, t)$ can be expressed as a linear combination of the natural motions of the form

$$
z(x, t)=\sum_{n=1}^{\infty} X_{n}(x) T_{n}(t) \tag{3}
$$

where $X_{n}(x)$ can be expressed as

$$
\begin{aligned}
X_{n}(x)= & \left\{\left[\cos \left(k_{n} x\right)-\cosh \left(k_{n} x\right)\right]\right. \\
& \left.-\frac{\cos \left(k_{n} L\right)+\cosh \left(k_{n} L\right)}{\sin \left(k_{n} L\right)+\sinh \left(k_{n} L\right)}\left[\sin \left(k_{n} x\right)-\sinh \left(k_{n} x\right)\right]\right\}
\end{aligned} \tag{4}
$$

where $k_{n}^{4}=\omega_{n}^{2} \frac{m}{E I}$, $\omega_{n}$ is the $n$th natural frequency of the beam, and $L$ is the length of the beam.

Eigenvalues $\lambda_{n}=k_{n} L$ of the cantilever beam with a lumped proof mass $M$ beneath the tip can be determined through [15]

$$
\begin{aligned}
& -\left(1+\cos \left(k_{n} L\right) \cosh \left(k_{n} L\right)\right)+\frac{M}{m L}\left(k_{n} L\right)\left(\sin \left(k_{n} L\right) \cosh \left(k_{n} L\right)\right. \\
& \left.-\sinh \left(k_{n} L\right) \cos \left(k_{n} L\right)\right)=0
\end{aligned} \tag{5}
$$

Meanwhile, the orthogonal conditions for a beam with a lumped mass at $x=L$ is

$$
\int_{0}^{L} m X_{r}(x) X_{s}(x) d x+M X_{r}(L) X_{s}(L)=0, r, s=1,2, \ldots ; \quad r \neq s \tag{6}
$$

### 2.3 Response to Harmonic Excitations

In this section, we are concerned with the case in which $f(x,t)$ represents a harmonic force, which can be expressed for convenience in the form

$$
f(x, t)=m \ddot{z}_{b}=m z_{b 0} \omega^{2} \cos (\omega t) \tag{7}
$$

where $z_b=-z_{b0}\cos(\omega t)$ is the displacement of base, and $\omega$ is the driving angular frequency.

So that Eq. (1) turns into

$$
\sum_{n=1}^{\infty} X_{n}(x)\left[\ddot{T}(t)+2 \xi \omega_{n} \dot{T}(t)+\omega_{n}^{2} T(t)\right]=z_{b 0} \omega^{2} \cos (\omega t) \tag{8}
$$

where $\xi=\frac{b}{2 m \omega_{n}}$ is the damping ratio.

Multiplying Eq. (7) by $X_n(x)$, integrating over the length, and citing the orthogonal conditions, we obtain

$$
\begin{aligned}
& {\left[\ddot{T}(t)+2 \xi \omega_{n} \dot{T}(t)+\omega_{n}^{2} T(t)\right]} \\
& \quad=\frac{\int_{0}^{L} X_{n}(x) d x}{\int_{0}^{L} X_{n}^{2}(x) d x-\frac{M}{m} X_{n}(L) \sum_{m=1, m \neq n}^{\infty} X_{m}(L)} z_{b 0} \omega^{2} \cos (\omega t) \\
& \quad=A_{n}(L) z_{b 0} \omega^{2} \cos (\omega t)
\end{aligned} \tag{9}
$$

Therefore, the expression of $T_n(t)$ is

$$
T_{n}(t)=Y(\omega) \cos (\omega t-\phi) \tag{10}
$$

where

$$
Y(\omega)=\frac{A_{n}(L) z_{b 0} \omega^{2}}{\left[\left(\omega_{n}^{2}-\omega^{2}\right)^{2}+\left(2 \xi \omega_{n} \omega\right)^{2}\right]^{\frac{1}{2}}}
$$

$$
\phi_{n}=\tan ^{-1} \frac{2 \xi \omega_{n} \omega}{\omega_{n}^{2}-\omega^{2}}
$$

Consider the situation that the cantilever beam thickness is much less than the radius of the torque curvature. The axial strain with radius of curvature \(R\) is [17]

$$
\delta_{P}=\frac{z_{N}-z_{P}}{R}=\frac{\partial^{2} z(x, t)}{\partial x^{2}}\left(z_{N}-z_{P}\right) \tag{11}
$$

where \(z_{N}\) denotes the height of the neutral axis and \(z_{P}\) is the center of the area of the PZT layer. Then the axial stress on the PZT layer is

$$
\sigma_{P}=E_{P} \delta=E_{P} \frac{\partial^{2} z(x, t)}{\partial x^{2}}\left(z_{N}-z_{P}\right) \tag{12}
$$

The electric field displacement of the PZT layer can be expressed as

$$
D=d_{31} \sigma_{P}+\varepsilon_{p} E_{z}=d_{31} E_{P} \frac{\partial^{2} z(x, t)}{\partial x^{2}}\left(z_{N}-z_{P}\right)+\varepsilon_{p} E_{z} \tag{13}
$$

where \(D\) is the electric field displacement in \(z\) direction, \(E_{P}\) is the Young's modulus of the PZT, \(d_{31}\) is the piezoelectric constant, and \(E_{z}\) is the electric field in \(z\) direction. So the total strain-induced charge \(Q\) is

$$
\begin{aligned}
Q &=\int_{0}^{L_{P}} D w_{d} d x \\
&=\int_{0}^{L_{P}} d_{31} E_{P}\left(z_{N}-z_{P}\right) w_{d} \frac{\partial^{2} z(x, t)}{\partial x^{2}} d x+\varepsilon_{p} E_{z} w_{d} L_{P} \\
&=\left.d_{31} E_{P}\left(z_{N}-z_{P}\right) w_{d} \frac{\partial z(x, t)}{\partial x}\right|_{x=L_{P}}+\varepsilon_{p} E_{z} w_{d} L_{P}
\end{aligned} \tag{14}
$$

where \(w_{d}\) is the width of the piezoelectric beam, and \(L_{P}\) is the length of the piezoelectric layer, which is not more than the length of the piezoelectric beam \(L\).

Then the strain-induced current is

$$
I=\frac{\partial Q}{\partial t}=j \omega Q=j \omega\left(\left.d_{31} E_{P}\left(z_{N}-z_{P}\right) w_{d} \frac{\partial z(x, t)}{\partial x}\right|_{x=L_{P}}+\varepsilon_{p} E_{z} w_{d} L_{P}\right) \tag{15}
$$

### 2.4 Lumped Circuit Model

Consider the situation that a resistor \(R\) is connected directly with the vibrating piezoelectric beam as the load. The output voltage can also be expressed as

$$
V=-E_{z} t_{p}=I R \tag{16}
$$

![](./images/811948443999141891_5.jpg)

Figure 3. Lumped circuit model of the piezoelectric beam.

Combining Eq. (15) and (16), the output voltage can be expressed as

$$
V = \frac{j\omega C_P R}{1 + j\omega C_P R} V_{OC} = \frac{R}{1 + j\omega C_P R} I_P \tag{17}
$$

where

$$
\begin{aligned}
I_P &= j\omega C_P V_{OC} = \left.j\omega d_{31} E_P(z_N - z_P)w_d \frac{\partial z(x, t)}{\partial x}\right|_{x=L_P} \\
C_P &= \frac{\varepsilon_p w_d L_P}{t_P}
\end{aligned} \tag{18}
$$

Lumped circuit models can be extracted from Eq. (17). As shown in Fig. 3(a), the vibrating piezoelectric beam can be modeled as a sinusoidal current source $i_P(t)$ in parallel with its internal electrode capacitance $C_P$, which is often used in piezoelectric element modeling [12, 18, 19]. Similarly, it can also be modeled as a sinusoidal voltage source $v_P(t)$ in series with $C_P$ as shown in Fig. 3(b).

The average power on $R$ is

$$
\bar{P} = \frac{|V|^2}{2R} = \frac{1}{2} \frac{\omega^2 C_P^2 |V_{oc}|^2 R}{1 + (\omega R C_P)^2} \tag{19}
$$

Parameters of the lumped circuit model, i.e. $v_P(t)$, $i_P(t)$ and $C_P$, are determined together with the piezoelectric device and the vibration source. In other words, they have nothing to do with the resistive load. So that optimization of the generated power on $R$ can be carried out. Therefore the optimal resistive load and the corresponding average output power are

$$
\begin{aligned}
R_{opt} &= \frac{1}{\omega C_P} \\
\bar{P}_{\text{max}} &= \frac{\omega C_P |V_{OC}|^2}{4}
\end{aligned} \tag{20}
$$

With the optimal resistive load, the output voltage on the load is

$$
V_{opt} = \frac{V_{OC}}{2} \tag{21}
$$

From the equations above, it is found that the output voltage and power are dependent upon several parameters. Such parameters mainly include the resistive load $R$, angular frequency of the vibration source $\omega$, length of piezoelectric beam $L$, thickness of silicon support $t_{Si}$, proof mass $M$, thickness of piezoelectric layer $t_{P}$, and length of piezoelectric layer $L_{P}$. These parameters are all the important design factors for piezoelectric power generator. Detailed discussions will be carried out in the next section.

## 3. SIMULATIONS

The open-circuit voltage and the optimal average power, which are shown in Eq. (18) and (20), are targeted in the simulations about effects of the parameters of the piezoelectric device. In the simulations, a vibration source with an acceleration of $10\ \text{m/s}^2$ at $100\ \text{Hz}$ is used, since vibration sources of similar level and frequency are ubiquitous in the environment. Material parameters of the PZT layer are listed in Table 1. For the convenience of discussion, one set of the device parameters is selected: size of the silicon layer is $7.1\ \text{mm} \times 0.5\ \text{mm} \times 17\ \mu\text{m}$, length and thickness of the piezoelectric layer are $7.1\ \text{mm}$ and $2.0\ \mu\text{m}$, and the damping factor is $0.01$. These parameters are used as default values in the simulations. They are moderate but not optimal, and act as benchmark of the optimization.

As shown in Fig. 4, the output power decreases quickly with the driving frequency deviating from the resonant frequency. Therefore, the resonant frequency of the piezoelectric device must be adjusted to match that of the vibration source. Fortunately adjustment can be achieved by designing the geometric parameters and the proof mass. However, in the following simulations, only the proof mass is adjusted for the constant resonant frequency, $100\ \text{Hz}$.

Table 1
Material parameters of the PZT

| Item                     | Value | Unit  |
|--------------------------|-------|-------|
| Young's modulus          | 86    | GPa   |
| Piezoelectric constant   | 60.2  | pC/N  |
| Relative permittivity    | 504   | $-$ |

![](./images/811948443999141891_6.jpg)

**Figure 4.** Optimal average power as a function of input frequency with three different damping factors $\zeta = 0.005, 0.01, 0.02$.

From simulations in Fig. 5, it is found that a thicker and shorter piezoelec- tric beam results in a larger generated power. Accordingly, as shown in Fig. 6, a larger normalized proof mass (to the beam mass) is needed for keeping a constant resonant frequency. However, too large a proof mass is impractical. Too large a proof mass isn't easy to fabricate by MEMS technologies and more- over, will reduce the reliability of the device. So there is a tradeoff between the dimensions of beam and the proof mass. As for the set of parameters above, the open-circuit voltage, optimal average power and normalized proof mass are $1.44\ \text{V}$, $2.59\ \mu\text{W}$, and $4.70$, respectively.

As shown in Fig. 7, the optimal average power increases linearly with the width of the piezoelectric beam. While the width increases, the eigenvalues and corresponding natural motions of the Euler-Bernoulli beam equations remain

![](./images/811948443999141891_7.jpg)

**Figure 5.** Optimal average power as a function of beam length with silicon thickness $\text{t}_{Si}=12, 15, 18\ \mu\text{m}$.

![](./images/811948443999141891_8.jpg)

**Figure 6.** The beam length dependence of normalized proof mass (to beam mass) for keeping a constant resonant frequency of 100 Hz (silicon thickness $t_{Si}=12,15,18\ \mu$m).

invariable. Finally, in the lumped circuit model of Fig. 3, the internal electrode capacitance increases linearly with the width, however, the open-circuit voltage and the normalized proof mass remain invariable. In the case of a 15 um silicon thick beam in Fig. 7, the open-circuit voltage and the normalized proof mass remain 1.30 V and 3.65, respectively.

A thick PZT layer is worthy consideration, since the outputs increase approximately linearly with the thickness of PZT layer (Fig. 8). The thickness of PZT layer and its change are far less than the thickness of the silicon beam because it is difficult to deposit very thick PZT film. Therefore, just small adjustment of proof mass is needed to keep a constant resonant frequency. The normalized proof mass changes from 4.73 to 4.86 when the thickness of PZT

![](./images/811948443999141891_9.jpg)

**Figure 7.** Optimal average power as a function of beam width with silicon thickness $t_{Si}=12,15,18\ \mu$m.

![](./images/811948443999141891_10.jpg)

Figure 8. Open-circuit voltage and optimal average power as a function of the thickness of piezoelectric layer with a small adjustment of the normalized proof mass (from 4.73 to 4.86).

layer increases from 0.5 um to 3.0 um. Figure 8 shows that thickening the PZT layer seems a great choice for a higher output.

One of the most important findings of the simulations is that the length of the piezoelectric layer can also be optimized, which is usually neglected. As shown in Fig. 9, the optimal average power reaches its peak value at an optimal length while the open-circuit voltage is inversely proportional to the length of the piezoelectric layer. When setting the length of piezoelectric layer to be the optimal value, i.e. 4.69 mm, the open-circuit voltage and the optimal average power are 1.93V and 3.09 uW, which are increased by 34.3% and 19.5%, respectively, when compared to those of the default values. Although an analytical expression of the optimal length is hard to find out, it is also obvious that it doesn't benefit to set the length of the piezoelectric layer being

![](./images/811948443999141891_11.jpg)

Figure 9. Open-circuit voltage and optimal average power as a function of the length of piezoelectric layer.

![](./images/811948443999141891_12.jpg)

**Figure 10.** Strain of the piezoelectric layer as the distance $x$ from the origin with three different lengths of the beam $L = 6.0$, 6.5, 7.1 mm.

equal to that of the beam. This will be much clearer when we look into the strain distributing of the piezoelectric, which is shown in Fig. 10. Figure 10 shows that the absolute value of the strain decreases with the distance $x$ from the origin and down to approximately zero at $x = L$. Therefore, it is clear that the benefit of putting the piezoelectric layer on the far side of the beam is very small.

## 4. CONCLUSIONS

This paper has proposed a structure design of piezoelectric MEMS power generator to harvest energy from the ambient vibrations. The design is based on thin film PZT and bulk MEMS technologies, which is utilized to fabricate a silicon cantilever with cubical-shaped silicon mass. Without adhesion of an additional proof mass, the resonant frequency of the cantilever can be tuned to low-level such as 100 Hz, which is suitable for the ubiquitous vibrations in the environment.

Based on the proposed design, the modeling and simulations are carried out. The design is modeled through the Euler-Bernoulli beam theory and analytical simulations are carried out. Simulations and findings point out ways to perform the optimization of MEMS power generator, including a tradeoff between the dimensions of beam and the proof mass, increase of the thickness of piezoelectric layer, and optimization of the piezoelectric layer. Such simulation results are very important for the development of MEMS power generator.

In this paper, the design is modeled as an Euler-Bernoulli beam with a lumped mass beneath the tip. However, a more complicated modeling may be needed when considering a relatively large proof mass, which can't be modeled as a lumped mass. A two-degree plate may be more suitable for the modeling of the device when the width of the cantilever isn't far less than the length.

Such work is underway and modification of the model will be performed to obtain an accurate model. However, the present modeling and simulations can already provide ways to better design MEMS power generator, and also helpful for macro-scale power generator.

## REFERENCES

1. C. Watkins, B. Shen, and R. Venkatasubramanian, "Low-grade-heat energy harvesting using superlattice thermoelectrics for applications in implantable medical devices and sensors," *24th International Conference on Thermoelectrics*, 265-267 (2005).

2. T. von Büren and G. Tröster, "Design and optimization of a linear vibration-driven electromagnetic micro-power generator," *Sensors and Actuators A: Physical* **135**, 765-775 (2007).

3. R. Duggirala, R. Polawich, E. Zakar, M. Dubey, H. Li, and A. Lal, "MEMS radioisotope-powered piezoelectric $\mu$-power generator (RPG)," *MEMS*, 94-97 (2006).

4. C.-T. Chen, R. A. Islam, and S. Priya, "Electric energy generator," *IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency control* **53**, 656-661 (2006).

5. S. Pobering and N. Schwesinger, "A novel hydropower harvesting device," *Proceedings of the 2004 International Conference on MEMS, NANO and Smart Systems*, 2004 pp. 480-485.

6. X. Cao and Y.-K. Lee, "Design and fabrication of mini vibration power generator system for micro sensor networks," *Proceedings of the 2006 IEEE International Conference on Information Acquisition*, 2006, pp. 91-95.

7. C. B. Williams, C. Shearwood, M. A. Harradine, P. H. Mellor, T. S. Birch, and R. B. Yates, "Development of an electromagnetic micro-generator," *IEEE Proceedings of Circuits, Devices and Systems* **148**, 337-342 (2001).

8. B. C. Yen, and J. H. Lang, "A variable-capacitance vibration-to-electric energy harvester," *IEEE Transactions on Circuit and Systems* **53**, 288-295, (2006).

9. S. Roundy, P. K. Wright, and J. R., "A study of low level vibrations as a power source for wireless sensor nodes," *Computer Communications* **26**, 1131-1144, (2003).

10. S. R. Platt, S. Farritor, and H. Haider, "On low-frequency electric power generation with PZT ceramics," *IEE/ASME Transactions on Mechatronics* **10**, 240-252 (2005).

11. S. Roundy, E. S. Leland, J. Baker, E. Carleton, E. Reilly, E. Lai, B. Otis, J. M. Rabaey, P. K. Wright, and V. Sundararajan, "Improving power output for vibration-based energy scavengers," *IEEE Pervasive Computing* **4**, 28-36 (2005).

12. Y. B. Jeon, R. Sood, J.-H. Jeong, and S.-G. Kim, “MEMS power generator with transverse mode thin film PZT,” *Sensors and Actuators A* **122**, 16–22 (2005).

13. K. Dogheche, B. Cavallier, P. Delobelle, L. Hirsinger, S. Ballandras, E. Cattan, and D. Rèmiens, “Piezoelectric micro-machined ultrasonic trans- ducer (pMUT) for energy harvesting,” *Proceedings of IEEE Ultrasonics Symposium* **20**, 939–942.

14. H.-B. Fang, J.-Q. Liu, Z.-Y. Xu, L. Dong, L. Wang, D. Chen, B.-C. Cai, and Y. Liu, “Fabrication and performance of MEMS-based piezoelectric power generator for vibration energy harvesting,” *Microelectronics Journal* **37**, 1280–1284 (2006).

15. L. Meirovitch, “Fundamentals of vibrations,” New York: McGraw-Hill Book Co., 2001.

16. S. N. Chen, G. J. Wang, and M. C. Chien, “Analytical modeling of piezo- electric vibration-induced micro power generator,” *Mechatronics* **16**, 379–387 (2006).

17. M. S. Weinberg, “Working equations for piezoelectric actuators and sen- sors,” *J. Microelectromech. Syst.* **8**, 529–533 (1999).

18. G. K. Ottman, H. F. Hofmann, A. C. Bhatt, and G. A. Lesieutre, “Adaptive piezoelectric energy harvesting circuit for wireless remote power supply,” *IEEE Transactions on Power Electronics* **17**, 669–676 (2002).

19. L. Mateu and F. Moll, “Appropriate charge control of the storage capacitor in a piezoelectric energy harvesting device for discontinuous load opera- tion,” *Sensors and Actuators A* **132**, 303–310 (2006).