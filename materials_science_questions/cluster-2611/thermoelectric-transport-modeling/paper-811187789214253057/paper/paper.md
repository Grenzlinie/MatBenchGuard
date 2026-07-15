Special issue article

Received: 30 June 2016
Accepted: 30 June 2016
Published online in Wiley Online Library: 22 July 2016

(wileyonlinelibrary.com) DOI 10.1002/sia.6095

# Edge-disorder-induced optimization of thermoelectric performance of finite-length graphene nanoribbons

Tetsumi Izawa, $^{a}$ Kengo Takashima $^{a}$ and Takahiro Yamamoto $^{a,b,*}$

Effects of edge disorder on thermoelectric performance of graphene nanoribbons (GNRs) were investigated through computational simulations based on the non-equilibrium Green's function method combined with the tight-binding method. We found that the thermoelectric power factor $PF$ can be optimized by adjusting the length, $L_g$, of GNRs with edge disorder concentration $C_d$. For example, $PF$ of zigzag-edged GNRs with a $C_d$ of 10 % at room temperature and at the Fermi energy shows a maximum value of $33\ \text{mW/(m\ K}^2\text{)}$ at $L_g=210\ \text{nm}$. Both the maximum $PF$ and optimum $L_g$ decrease with increasing $C_d$. The maximum $PF$ is theoretically explained in terms of the crossover from the ballistic transport regime to the Anderson's localization regime. Copyright © 2016 John Wiley & Sons, Ltd.

Keywords: graphene nanoribbons; edge disorder; Seebeck coefficient; thermoelectric power factor; Anderson's localization

## Introduction

Unlike heat engines, thermoelectric materials can efficiently transform small quantities of low-temperature and dispersed thermal energy into electrical energy. Thus, thermoelectric technology contributes to solving the energy problem and developing self-sustaining power sources for wearable devices, and so on. According to a theoretical prediction made by Hicks and Dresselhaus in $1993,^{[1]}$ the thermoelectric efficiency of materials can be significantly enhanced by processing them into one-dimensional nanowires. In fact, diverse nanowires with high thermoelectric performance have been discovered. $^{[2-6]}$ The next challenge in this field is to design eco-friendly and flexible thermoelectric nanowires for wearable devices.

Graphene is a two-dimensional honeycomb lattice consisting of carbon atoms, which is expected as a practical thermoelectric conversion material. $^{[7]}$ Graphene nanoribbons (GNRs) are single-layered graphene in the shape of a nanometer-width ribbon. They have recently been attracting great interest as a potential candidate for a nanowire with high thermoelectric capability $^{[8,9]}$ exceeding that of graphene. In addition to having a high thermoelectric power factor $PF$, GNRs are nontoxic and flexible. However, despite their high $PF$, the thermoelectric efficiency of GNRs is not high, owing to their high thermal conductivity, comparable to those of diamond and carbon nanotubes. $^{[10]}$ In order to improve the thermoelectric efficiency, we have to develop techniques that reduce the thermal conductivity of GNRs without reducing their $PF$.

Even a small degree of edge disorder in GNRs is known to suppress thermal conductivity dramatically. $^{[11]}$ GNRs that retain a high $PF$ after the introduction of edge disorder (ED-GNRs) are promising candidates for high-performance thermoelectric applications.

In this paper, we theoretically derive the $PF$ of ED-GNRs. In particular, we elucidate the effects of edge disorder on the $PF$ of zigzag-edged GNRs (ED-ZGNRs), $^{[12,13]}$ focusing on the dependence of edge disorder concentration on ribbon length at room temperature and the Fermi energy.

## Landauer theory of thermoelectronics

The Landauer theory affords electric current $I$ via

$$
I=-\frac{2q}{h}\int_{-\infty}^{\infty}\zeta(\varepsilon)\left[f(\varepsilon,\mu_{\text{L}},T_{\text{L}})-f(\varepsilon,\mu_{\text{R}},T_{\text{R}})\right]d\varepsilon, \tag{1}
$$

where $q$ is the charge of an electron, $h$ Planck's constant, $\zeta(\varepsilon)$ the transmission function of an electron with energy $\varepsilon$, and $f$ the Fermi Dirac distribution function of a left (right) lead at chemical potential $\mu_{\text{L(R)}}$ and temperature $T_{\text{L(R)}}.{^{[14]}}$ In this study, we chose the Fermi energy as the origin of the energy axis ($\varepsilon=0$).

In the case of small chemical-potential difference and small temperature difference, Eq. (1) becomes

$$
\Delta I\approx\Delta\mu\frac{-2q}{h}\int_{-\infty}^{\infty}\zeta(\varepsilon)\frac{\partial f}{\partial\mu}d\varepsilon+\Delta T\frac{-2q}{h}\int_{-\infty}^{\infty}\zeta(\varepsilon)\frac{\partial f}{\partial T}d\varepsilon, \tag{2}
$$

where $\Delta\mu=\mu_{\text{L}}-\mu_{\text{R}}$ and $\Delta T=T_{\text{L}}-T_{\text{R}}$. Using Eq. (2), the electric conductance $G$ and Seebeck coefficient $S$ of a material can be expressed, respectively, as

* Correspondence to: Takahiro Yamamoto, Department of Liberal Arts (Physics), Tokyo University of Science, Niijuku 6-3-1, Katsushika, Tokyo 125-8585, Japan.
E-mail: takahiro@rs.tus.ac.jp

a Department of Electrical Engineering, Tokyo University of Science, Niijuku 6-3-1, Katsushika, Tokyo, 125-8585, Japan

b Department of Liberal Arts (Physics), Tokyo University of Science, Niijuku 6-3-1, Katsushika, Tokyo, 125-8585, Japan

Surf. Interface Anal. 2016, 48, 1210-1213
Copyright © 2016 John Wiley & Sons, Ltd.

$$
G \equiv \lim _{\Delta V \to 0}\left(\frac{\Delta I}{\Delta V}\right)_{\Delta T=0}=q^{2} K_{0}, \tag{3}
$$

$$
S \equiv \lim _{\Delta T \to 0}\left(\frac{\Delta V}{\Delta T}\right)_{\Delta I=0}=-\frac{1}{q T} \frac{K_{1}}{K_{0}}, \tag{4}
$$

where the intermediate function $K_{n}$ is defined as

$$
K_{n}=\frac{2}{h} \int_{-\infty}^{\infty} \zeta(\varepsilon)\left(-\frac{\partial f}{\partial \varepsilon}\right)(\varepsilon-\mu)^{n} d \varepsilon. \tag{5}
$$

The maximum thermoelectric power is determined by the thermoelectric power factor $PF$,

$$
P F=\sigma S^{2}. \tag{6}
$$

Here, $\sigma$ is the electric conductivity related to $G$ via

$$
\sigma=\frac{L_{\mathrm{g}}}{A} G, \tag{7}
$$

where $L_{\mathrm{g}}$ and $A=W \times d$ ($W$: GNR width, $d$: GNR thickness) are the GNR length (central scattering region, next section) and the effective cross-section of the GNR, respectively. We adopted a $d$ value of 0.335 nm, which corresponds to twice the van der Waals radius of carbon.

## Simulation model and method

Our simulation models consist of three regions: a central scattering region, the left and right electrodes. The scattering region comprises an ED-ZGNR with an averaged width $W$ and a ribbon length $L_{\mathrm{g}}$, as shown in Fig. 1. The left and right electrodes are pristine ZGNRs with a width $W$ and a semi-infinite length. Each edge carbon atom is terminated by a hydrogen atom.

In the present study, we conducted a thermoelectric simulation for ED-ZGNRs with a fixed width $W$ of 1.78 nm and various $L_{\mathrm{g}}$ values between 8.7 and 296.7 nm. The edge disorder, which was modeled by the addition and removal of carbon atoms at the edges, was taken to be randomly distributed in the central region, as shown in Fig. 1. In addition, it was assumed that the numbers of carbon atoms added and removed ($N_{\mathrm{a}}$ and $N_{\mathrm{r}}$, respectively) were the same, i.e., $N_{\mathrm{a}}=N_{\mathrm{r}}$. We then defined the edge disorder concentration $C_{\mathrm{d}}$ as

$$
C_{\mathrm{d}}=\frac{N_{\mathrm{a}}+N_{\mathrm{r}}}{N_{\text {edge }}}. \tag{8}
$$

Here, $N_{\text {edge }}$ is the total number of edge carbon atoms.

We utilized Atomistix ToolKit ver. $2014.2^{[15]}$ to compute the transmission function $\zeta(\varepsilon)$ of each ED-ZGNR sandwiched between two pristine ZGNR leads with semi-infinite length. The computation was based on the non-equilibrium Green's function (NEGF) method combined with the tight-binding method. The transfer integrals between each pair of $2 s, 2 p_{x}, 2 p_{y}, 2 p_{z}$ orbitals of carbon atoms were obtained by the Slater-Koster parameter. $^{[16]}$

![](./images/811187789214253057_1.jpg)

Figure 1. The scattering region sandwiched between two electrodes. The scattering region consists of an ED-ZGNR with average width $W$ and ribbon length $L_{\mathrm{g}}$. Gray and white balls represent carbon and hydrogen atoms, respectively.

Using Eqs. (3)-(7), we calculated the electric conductivity $\sigma$, Seebeck coefficient $S$, and thermoelectric power factor $PF$ values of 1,000 ED-ZGNRs with different configurations of edge disorder for fixed $L_{\mathrm{g}}$ and $C_{\mathrm{d}}$. Then, we estimated the averaged conductivity $<\sigma>$, Seebeck coefficient $<S>$, and power factor $<PF>$ by averaging the $\sigma$, $S$ and $PF$ values over 1,000 ED-ZGNRs. All simulations were performed at room temperature (300 K).

## Simulation results

### Electric conductivity

Figure 2 plots the ribbon length $L_{\mathrm{g}}$ dependence of the averaged conductivity $<\sigma>$ for ED-ZGNRs with various edge disorder concentrations $C_{\mathrm{d}}$ values at the Fermi energy $(\varepsilon=0)$. As seen in Fig. 2, for any $L_{\mathrm{g}}$, $<\sigma>$ decreases with $C_{\mathrm{d}}$. This is because electron scattering events increase with $C_{\mathrm{d}}$.

Pristine ZGNRs show ballistic transport and $\sigma$ becomes proportional to $L_{\mathrm{g}} \cdot{ }^{[17]}$ At finite $C_{\mathrm{d}}$, the electronic transport in ZGNRs deviates from ballistic behavior. Indeed, the $<\sigma>$ at $C_{\mathrm{d}}=5 \%$ is almost independent of $L_{\mathrm{g}}$ for $100 \mathrm{~nm}<L_{\mathrm{g}}<300 \mathrm{~nm}$; the electronic transport is diffusive. $^{[18]}$ It is known that the $L_{\mathrm{g}}$ dependence of $<\sigma>$ is

$$
\langle\sigma\rangle \propto \frac{L_{\mathrm{g}} L_{0}}{L_{\mathrm{g}}+L_{0}}, \tag{9}
$$

where $L_{0}$ is the mean free path. Eq. (9) can be rewritten as $\sigma \propto L_{0}$ (=const.with $L_{\mathrm{g}}$) in the $L_{\mathrm{g}} \gg L_{0}$ limit. By contrast, $<\sigma>$ at $C_{\mathrm{d}}=10$, 15 and $20 \%$ peaks at certain $L_{\mathrm{g}}$ and then exhibits exponential decay via

$$
\langle\sigma\rangle \propto L_{\mathrm{g}} e^{-\frac{L_{\mathrm{g}}}{\zeta}}, \tag{10}
$$

where $\zeta$ is the localization length $^{[17]}$ that characterizes the

![](./images/811187789214253057_2.jpg)

Figure 2. $L_{\mathrm{g}}$ dependence of $<\sigma>$ for ED-ZGNRs with various $C_{\mathrm{d}}$ values at the Fermi energy $(\varepsilon=0)$. Dotted line plots $\sigma$ for $C_{\mathrm{d}}=0 \%$. Circles, squares, diamonds, and triangles represent $<\sigma>$ for $C_{\mathrm{d}}=5,10,15,20 \%$, respectively.

broadening of localized wave functions. The exponential decay of $<\sigma>$ occurs due to the interference between electron waves scattered by edge disorder. This type of electron localization is known as Anderson's localization. $^{[18]}$

## Seebeck coefficient and power factor
In Fig. 3, we plot the $L_{\mathrm{g}}$ dependence of the averaged Seebeck coefficient $<S>$ for ED-ZGNRs with various $C_{\mathrm{d}}$ values at the Fermi energy $(\varepsilon=0)$. In contrast to $<\sigma>$ shown in Fig. 2, $<S>$ increases monotonically with $L_{\mathrm{g}}$ even for $C_{\mathrm{d}}$ values of more than 10 % (i.e., $C_{\mathrm{d}}=10,15$, and 20 %).

Figure 4 plots the $L_{\mathrm{g}}$ dependence of the averaged power factor $<PF>$ for ED-ZGNRs with various $C_{\mathrm{d}}$ values at the Fermi energy $(\varepsilon=0)$.

As shown in Fig. 4, $<PF>$ for $C_{\mathrm{d}}=5$ % increases monotonically with $L_{\mathrm{g}}$ because the transport regime for $L_{\mathrm{g}}<300 \mathrm{~nm}$ is diffusive transport, as mentioned in previous section. Interestingly, the $<PF>$ values for $C_{\mathrm{d}}=10,15$, and 20 % have maxim at certain $L_{\mathrm{g}}$ values resulting from the exponential decay of $<\sigma>$ with respect to $L_{\mathrm{g}}$. In other words, the decay of $<PF>$ is caused by Anderson's localization, which occurs when $L_{\mathrm{g}}$ is much longer than the localization length $\xi$. Thus, the peak of $<PF>$ characterizes the crossover between the ballistic and Anderson's localization regimes.

![](./images/811187789214253057_3.jpg)

Figure 3. $L_{\mathrm{g}}$ dependence of $<S>$ for ED-ZGNRs with various $C_{\mathrm{d}}$ values at the Fermi energy $(\varepsilon=0)$. Circles, squares, diamonds, and triangles represent $<S>$ for $C_{\mathrm{d}}=5,10,15,20 \%$, respectively.

![](./images/811187789214253057_4.jpg)

Figure 4. $L_{\mathrm{g}}$ dependence of $<PF>$ for ED-ZGNRs with various $C_{\mathrm{d}}$ values at the Fermi energy $(\varepsilon=0)$. Circles, squares, diamonds, and triangles represent $<PF>$ for $C_{\mathrm{d}}=5,10,15,20 \%$, respectively.

From the data in Fig. 4, we can extract a relationship between the maximum power factor $<PF>_{\max }$ and $C_{\mathrm{d}}$ as well as between optimum $L_{\mathrm{g}}$ and $C_{\mathrm{d}}$. Here, optimum $L_{\mathrm{g}}$ means the GNR length where $<PF>$ is maximum.

As seen in Fig. 5, both $<PF>_{\max }$ and optimum $L_{\mathrm{g}}$ decrease monotonically as $C_{\mathrm{d}}$ increases. More qualitatively, we can see from the inset in Fig. 5 that $<PF>_{\max }$ and optimum $L_{\mathrm{g}}$ decrease with the square of $C_{\mathrm{d}}$. This means that we can obtain $<PF>_{\max }$ by adjusting $L_{\mathrm{g}}$ with respect to $C_{\mathrm{d}}$.

![](./images/811187789214253057_5.jpg)

Figure 5. $C_{\mathrm{d}}$ dependence of $<PF>_{\max }$ and optimum $L_{\mathrm{g}}$. Circles represent $<PF>_{\max }$ (the left axis) and squares denote optimum $L_{\mathrm{g}}$ (the right axis). The inset exhibits $1 / C_{\mathrm{d}}^{2}$ dependence of $<PF>_{\max }$ and optimum $L_{\mathrm{g}}$.

## Conclusions
We theoretically investigated the effects of edge disorder on the thermoelectric power factor of ZGNRs using the NEGF method combined with the tight-binding method. We found that the power factor of an ED-ZGNR exhibits a maximum at a certain ribbon length. As edge disorder concentration increases, both the maximum power factor and the optimum ribbon length decrease, owing to Anderson's localization resulting from the interference of electron waves scattered by edge disorder. Our findings afford a guiding principle for designing high-efficiency thermoelectric devices by processing graphenes into nanoribbons and optimizing the edge disorder and ribbon length.

## Acknowledgements
We would like to thank Satoru Konabe for his valuable comments on this work. We acknowledge partial financial support from Grants-in-Aid for Scientific Research B (No.15H03523) and C (No.26390007) from the Ministry of Education, Culture, Sports, Science and Technology of Japan.

## References
[1] L. D. Hicks, M. S. Dresselhaus, *Phys. Rev. B*, 1993, 47, 16631.
[2] Y. M. Lin, X. Sun, M. S. Dresselhaus, *Phys. Rev. B*, 2000, 62, 4610.

Optimization of thermoelectric performance of ED-GNRs

![](./images/811187789214253057_6.jpg)

[3] O. Rabin, Y. M. Lin, M. S. Dresselhaus, *Appl. Phys. Lett.*, **2001**, *79*, 81.
[4] J. P. Heremans, C. M. Thrush, D. T. Morelli, M. Wu, *Phys. Rev. Lett.*, **2002**, *88*, 216801.
[5] A. Hochbaum et al., *Nature*, **2008**, *451*, 163.
[6] A. Boukai et al., *Nature*, **2008**, *168*, 451.
[7] H. Kageshima, *Jpn. J. Appl. Phys.*, **2010**, *49*, 100207.
[8] T. Kato, S. Usui, T. Yamamoto, *Jpn. J. Appl. Phys.*, **2013**, *52*, 06GD05.
[9] Y. Yokomizo, J. Nakamura, *Appl. Phys. Lett.*, **2013**, *103*, 113901.
[10] J. Hu, X. Ruan, Y. P. Chen, *Nano Lett.*, **2009**, *9*, 2730.
[11] H. Karamitaheri, M. Pourfath, H. Kosina, N. Neophytou, *Phys. Rev. B*, **2015**, *91*, 165410.

[12] M. Fujita, K. Wakabayashi, K. Nakada, K. Kusakabe, *J. Phys. Soc. Jpn.*, **1996**, *65*, 1920.
[13] K. Nakada, M. Fujita, G. Dresselhaus, M. S. Dresselhaus, *Phys. Rev. B*, **1996**, *54*, 17954.
[14] S. Datta, *Electronic Transport in Mesoscopic Systems*, Cambridge University Press, Cambridge, U. K., **1995**, Chap.2.
[15] K. Stokbro, D. E. Petersen, S. Smidstrup, A. Blom, M. Ipsen, K. Kaasbjerg, *Phys. Rev. B*, **2010**, *82*, 075420.
[16] J. C. Slater, G. F. Koster, *Phys. Rev.*, **1954**, *94*, 1498.
[17] K. Takashima, T. Yamamoto, *Appl. Phys. Lett.*, **2014**, *104*, 093105.
[18] P. W. Anderson, *Phys. Rev.*, **1958**, *109*, 1492.

---

*Surf. Interface Anal.* **2016**, *48*, 1210–1213

Copyright © 2016 John Wiley & Sons, Ltd.

wileyonlinelibrary.com/journal/sia

<div style="position:absolute;right:0;bottom:0;width:50px;height:200px;background-color:#003399;color:white;writing-mode:vertical-rl;padding:5px;">1213</div>