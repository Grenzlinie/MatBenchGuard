# Thermoelectric properties of graphyne from first-principles calculations

P. H. Jiang, H. J. Liu*, L. Cheng, D. D. Fan, J. Zhang, J. Wei, J. H. Liang, J. Shi

Key Laboratory of Artificial Micro- and Nano-Structures of Ministry of Education and School of Physics and Technology, Wuhan University, Wuhan 430072, China

The two-dimensional graphene-like carbon allotrope, graphyne, has been recently fabricated and exhibits many interesting electronic properties. In this work, we investigate the thermoelectric properties of $\gamma$-graphyne by performing first-principles calculations combined with Boltzmann transport theory for both electron and phonon. The carrier relaxation time is accurately evaluated from the ultra-dense electron-phonon coupling matrix elements calculated by adopting the density functional perturbation theory and Wannier interpolation, rather than the generally used deformation potential theory which only considers the electron-acoustic phonon scattering. It is found that the thermoelectric performance of $\gamma$-graphyne exhibits a strong dependence on the temperature and carrier type. At an intermediate temperature of 600 K, a maximum $ZT$ value of 1.5 and 1.0 can be achieved for the $p$- and $n$-type systems, respectively.

## 1. Introduction

The steady increase in the world's population and its demands for fuel and products cause energy crisis in the past 50 years. Moreover, many industrial and commercial energy utilizations result in excessive rates of waste heat rejection. The thermoelectric technology is believed to be one of the effective methods for energy harvesting since it provides a promising route to convert waste heat into electricity. The efficiency of a thermoelectric material is determined by the dimensionless figure-of-merit
$$ZT=S^{2}\sigma T/\left(\kappa_{e}+\kappa_{ph}\right),$$
where $S$, $\sigma$, $T$, $\kappa_{e}$ and $\kappa_{ph}$ are the Seebeck coefficient, the electrical conductivity, the absolute temperature, the electronic and phonon thermal conductivity, respectively. Good thermoelectric material has larger $ZT$ value

* Corresponding author. E-mail: phlhj@whu.edu.cn (H. J. Liu)

and one therefore must try to maximize the power factor ($S^{2}\sigma$) and/or minimize the thermal conductivity ($\kappa_{e}+\kappa_{ph}$). However, it is extremely difficult to do so since these transport coefficients are usually coupled with each other in conventional thermoelectric materials [1]. In recent years, the successful fabrication of low-dimensional thermoelectric materials has simulated a lot of research interest [2, 3, 4, 5] because the $ZT$ value can be enhanced remarkably due to the quantum confinement effect [6, 7]. On the other hand, it is highly desired that better thermoelectric performance could be realized in the earth-abundant and environment-friendly systems, e.g., carbon materials. In this respect, the two-dimensional graphene seems to be a possible choice since its first fabrication in 2004 [8]. The existence of Dirac-cone band structure makes graphene exhibit numerous novel electronic properties [9]. However, the absence of band gap leads to very smaller Seebeck coefficient of graphene. Together with extraordinarily high thermal conductivity, the thermoelectric performance of graphene is indeed extremely poor [10].

Another two-dimensional candidate in the carbon family is graphyne, which was first proposed theoretically by Baughman *et al.* in 1987 [11]. It can be viewed as modified graphene by inserting the carbon-carbon triple bonds ($sp$ hybridization) into the $sp^{2}$ hybridized graphene. A series of atomic structures, e.g., the $\alpha$-, $\beta$-, $\gamma$-, 6, 6, 12-graphyne and graphdiyne, can be obtained by varying the number and position of the triple bonds [11, 12]. Recently, the successful fabrication of large area graphyne films [13] has inspired extensive studies exploring its mechanical, thermal, electronic and optical properties [14, 15, 16, 17]. Compared with graphene, graphyne exhibits more amazing electronic properties since the Dirac cones with different symmetries are presented [15]. Moreover, the band gap is opened up in the $\gamma$-graphyne and graphdiyne [18, 19]. Such novel characteristics extend the application prospects of the two-dimensional carbon allotropes. The presence of a band gap can drastically increase the Seebeck coefficient [20], and the inserted triple bonds can reduce the

thermal conductivity significantly [19, 21, 22]. All these observations suggest that the graphyne systems with finite band gap could exhibit very favorable thermoelectric performance which deserves a complete understanding.

In this work, the thermoelectric properties of the semiconducting $\gamma$-graphyne is systematically investigated by using first-principles calculations and Boltzmann transport theory, where the carrier relaxation time is accurately evaluated from the ultra-dense electron-phonon coupling matrix elements. We demonstrate that the thermoelectric performance of $\gamma$-graphyne exhibits a marked dependence on the temperature and carrier type. At an intermediate temperature of 600 K, a maximum $ZT$ value of 1.5 and 1.0 can be respectively achieved for the $p$- and $n$-type systems, which suggests that good thermoelectric performance can be also achieved in previously unexpected carbon systems.

## 2. Computational methods

Our first-principles total energy calculations are performed within the framework of density functional theory (DFT), as implemented in the QUANTUM ESPRESSO package [ 23 ]. We use the norm-conserving pseudopotential and the exchange-correlation functional is in the form of Perdew-Burke-Ernzerhof [24]. The system is modeled by adopting a hexagonal supercell geometry where the vacuum distance is set to 14 $\mathring{\text{A}}$ to eliminate the interactions between the graphyne layer and its periodic images. The kinetic energy cutoff is 80 Ry for the wavefunction and 800 Ry for the charge density. For the phonon dispersion relations and the electron-phonon coupling matrix elements, we apply the density functional perturbation theory (DFPT) [25] and Wannier interpolation technique [26]. The calculations are initially done by using a coarse $3{\times}3{\times}1$ $\mathbf{q}$ and $\mathbf{k}$ mesh, and then interpolate to a dense mesh of $120{\times}120{\times}1$ via the maximally localized Wannier functions as implemented in the electron-phonon Wannier (EPW) package [ 27 ]. After obtaining the electron self-energy $\Sigma_{nk}$ for band $n$ and state $\mathbf{k}$ from the interpolated ultra-dense electron-phonon coupling matrix elements, the relaxation time can be readily

determined by $\left(\tau_{nk}\right)^{-1}=2\left[\operatorname{Im}\left(\Sigma_{nk}\right)\right]/\hbar$ [28], where $\hbar$ is the reduced Plank constant.

Based on the energy band structure and carrier relaxation time, the electronic transport coefficients can be calculated by using the following formulas as derived from Boltzmann theory [29]:

$$
S=-\frac{1}{e T} \frac{\sum_{n, \mathbf{k}}\left(E_{n \mathbf{k}}-E_{f}\right) v_{n \mathbf{k}}^{2} \tau_{n \mathbf{k}} \frac{\partial f_{n \mathbf{k}}}{\partial E_{n \mathbf{k}}}}{\sum_{n, \mathbf{k}} v_{n \mathbf{k}}^{2} \tau_{n \mathbf{k}} \frac{\partial f_{n \mathbf{k}}}{\partial E_{n \mathbf{k}}}}, \tag{1}
$$

$$
\sigma=\frac{1}{N V} \sum_{n, \mathbf{k}}-e^{2} v_{n \mathbf{k}}^{2} \tau_{n \mathbf{k}} \frac{\partial f_{n \mathbf{k}}}{\partial E_{n \mathbf{k}}}, \tag{2}
$$

Here $E_{nk}$ is the energy eigenvalue, $E_f$ is the fermi energy, $v_{nk}$ is the group velocity, $\tau_{nk}$ is the relaxation time, $f_{nk}$ is the Fermi occupation, $N$ is the total number of $\mathbf{k}$ points, and $V$ is the volume of the primitive cell (with respect to a vacuum distance of 3.35 Å). The electronic thermal conductivity $\kappa_e$ is derived from the electrical conductivity $\sigma$ according to the Wiedemann-Franz Law $\kappa_e=L\sigma T$ [30], where the Lorenz number $L$ for the two-dimensional system is expressed as [6]:

$$
L=\frac{\kappa_{e}}{\sigma T}=\left(\frac{k_{B}}{e}\right)^{2}\left[\frac{3 F_{2}}{F_{0}}-\left(\frac{2 F_{1}}{F_{0}}\right)^{2}\right]. \tag{3}
$$

with the Fermi integral $F_{i}=F_{i}(\eta)=\int_{0}^{\infty} \frac{x^{i} d x}{e^{(x-\eta)}+1}$ ($\eta$ is the reduced Fermi energy).

The phonon thermal conductivity $\kappa_{ph}$ can be obtained by solving the phonon Boltzmann transport equation as implemented in the so-called ShengBTE code [31], where the second-order and third-order interatomic force constants are calculated with a 4×4×1 supercell. The interactions up to the fourth nearest neighbors are included for the anharmonic one, and a $\mathbf{q}$ point grid of 34×34×1 is chosen to ensure the convergence of $\kappa_{ph}$.

### 3. Results and discussion

The crystal structure of $\gamma$-graphyne is displayed in Figure 1, with 12 carbon atoms included in the primitive cell. Such a graphene-like structure can be viewed as carbon hexagons connected by the carbon-carbon triple bonds, so that the same symmetry ($P6/mmm$) of graphene is maintained. The optimized lattice constants are $a = b = 6.890$ Å, and three different bond lengths exist due to the mixed hybridization of carbon atoms with $sp^2$-$sp^2$ (1.426 Å), $sp^2$-$sp$ (1.408 Å), and $sp$-$sp$ (1.223 Å). These structure parameters are in good agreement with previously calculated using projector-augmented-wave (PAW) approach [12, 19]. To check the stability of the structure, we have calculated the phonon dispersion relations of $\gamma$-graphyne and no imaginary frequency is found, as shown in Figure 2(a). In Fig. 2(b), we plot the band structure of $\gamma$-graphyne. Unlike graphene with a Dirac cone, we see a direct band gap of 0.46 eV opened up due to the presence of $sp$ hybridization. Both the valence band maximum (VBM) and the conduction band minimum (CBM) are located at the M point of the Brillouin zone, instead of the K point for graphene. Our calculated band structure is consistent with previous theoretical studies using PAW [19] and pseudopotential methods [20].

![](./images/867750433060291180_1.jpg)

Figure 1 The atomic structure of $\gamma$-graphyne. The blue dashed lines indicate the primitive cell with basis vectors $\boldsymbol{a}$ and $\boldsymbol{b}$. The conventional $x$- and $y$-axis are also indicated.

When dealing with the electronic transport properties, the carrier relaxation time should be carefully treated. Earlier attempts in addressing this fundamentally important issue either adopt the ballistic transport model without consideration of the scattering [20, 21], or apply deformation potential (DP) theory which only considers the electron-acoustic phonon scattering [19, 32]. In the present work, the carrier relaxation time is accurately evaluated by considering the complete electron-phonon coupling within the EPW framework. It should be emphasized that a very dense $\mathbf{k}$ and $\mathbf{q}$ mesh should be used to obtain the electron-phonon coupling matrix elements, which can be done by adopting the Wannier interpolation technique based on the DFT and DFPT calculations. In Fig. 2(c) and 2(d), we respectively plot the interpolated phonon dispersion relations and the electronic band structure, which agree well with those obtained directly from DFPT and DFT approaches and indicate the accuracy and convergence of the Wannier interpolation. Figure 3(a) shows the calculated electron-phonon scattering rate (reciprocal of the relaxation time $\tau_{nk}$) and the electronic density of states (DOS) as a function of energy. We see that the scattering rate is proportional to the DOS, which is expected since the DOS reflects the phase space available for carrier scattering [33, 34]. In addition, the scattering rate increases with increasing temperature, indicating that the relaxation time is smaller at higher temperature. In most of previous works, the DP theory is generally used to predict the relaxation time [19, 35, 36, 37] for the VBM and CBM states. For example, the room temperature relaxation times of $\gamma$-graphyne given by DP theory are $4.9{\times}10^{-13}$ s and $14.1{\times}10^{-13}$ s for the $p$-type (VBM) and $n$-type (CBM) systems, respectively [19]. In contrast, our relaxation time obtained from the EPW method is energy dependent ($\tau_{nk}$). For comparison, we depict in Fig. 3(b) the temperature dependent relaxation times for the VBM and CBM states. It is clear to find that our results are obviously lower than those predicted from the simple DP theory. The reason is that only the acoustic phonon scattering is considered in the DP theory [38] while the scattering

from all the phonon modes is included in our EPW approach. Such difference also suggests that the optical phonon scattering could play an important role in determining the relaxation time and cannot be neglected in the $\gamma$-graphyne system. The overestimated relaxation time in previous work may lead to an unexpected high thermoelectric performance [19], as will be discussed later.

![](./images/867750433060291180_2.jpg)

Figure 2 The phonon dispersion relations and electronic band structures of $\gamma$-graphyne calculated by using (a) DFPT, (b) DFT, (c) Wannier interpolations based on DFPT (Wan+DFPT), and (d) Wannier interpolations based on DFT (Wan+DFT).

![](./images/867750433060291180_3.jpg)

Figure 3 (a) The electron-phonon scattering rate of $\gamma$-graphyne at 300 K, 600 K and 1000 K (left), and the corresponding density of states (right). (b) The temperature dependent relaxation time of the energy states at VBM and CBM.

The electronic transport coefficients of $\gamma$-graphyne can be now evaluated from Eq. (1) and (2) by inserting the energy dependent relaxation time. The room temperature Seebeck coefficient $S$, the electrical conductivity $\sigma$, and the power factor $S^2\sigma$

are plotted in Figure 4 as a function of carrier concentration. From the inset of Fig.
4(a), we can see that the Seebeck coefficient exhibits peak values at very low carrier
concentration, and the absolute values can be as high as 670 μV/K and 620 μV/K for
the $p$-type and $n$-type systems, respectively. These values are much larger than those
of the conventional thermoelectric materials such as $Bi_2Te_3$ [39], which is very
beneficial for its thermoelectric performance. With increasing carrier concentration,
however, the Seebeck coefficient decreases obviously and becomes vanished when
the concentration is larger than $10^{13}\ \text{cm}^{-2}$. On the contrary, the electrical conductivity
(Fig. 4(b)) increases sharply when the carrier concentration is larger than $10^{12}\ \text{cm}^{-2}$
but maintains a rather small value at low carrier concentration range where the
Seebeck coefficient is large enough. Such an opposite behavior calls for a
compromise between the Seebeck coefficient and the electrical conductivity, so that
the maximum power factor can be achieved (Fig. 4(c)). At moderate carrier
concentrations of $2.39×10^{12}\ \text{cm}^{-2}$ and $1.54×10^{12}\ \text{cm}^{-2}$, the optimized power factors are
$0.37\ \text{W/mK}^2$ and $0.24\ \text{W/mK}^2$ for the $p$-type and $n$-type systems, respectively. In
addition, the electronic thermal conductivity $\kappa_e$ is derived from the
Wiedemann-Franz Law, where the Lorentz number is $1.2-1.4×10^{-8}\ \text{WΩ/K}^2$ calculated
from Eq. (3). The electronic thermal conductivity shows similar behavior with the
electrical conductivity and is thus not shown here. It should be noted that the transport
coefficients, particularly the electrical conductivity, exhibit an obvious dependence on
the direction, which can be explained by the anisotropic group velocity of $\gamma$-graphyne.
In Figure 5(a), we plot the group velocity for the highest valence band, which is quite
different at different direction. For example, the group velocity along $k_x$ and $k_y$
directions are calculated to be $3.02×10^5\ \text{m/s}$ and $1.31×10^5\ \text{m/s}$ at the M point,
respectively. Similar behavior can be found for the lowest conduction band, as
indicated in Fig. 5(b). Such anisotropic electronic transport would lead to the direction
dependence of the $ZT$ value, which will be discussed later.

![](./images/867750433060291180_4.jpg)

Figure 4 The room temperature (a) Seebeck coefficient $S$, (b) electrical conductivity $\sigma$, and (c) power factor $S^{2}\sigma$ of $\gamma$-graphyne as a function of carrier concentration along the $x$- and $y$-directions for both $p$-type and $n$-type systems. The inset of (a) plots the Seebeck coefficient in a large range of carrier concentration to display the peak value.

![](./images/867750433060291180_5.jpg)

Figure 5 The group velocity of $\gamma$-graphyne for (a) the highest valence band, and (b) the lowest conduction band.

We now focus on the phonon transport properties of $\gamma$-graphyne. As mentioned above, the phonon thermal conductivity $\kappa_{ph}$ can be obtained by solving the phonon Boltzmann transport equation. Figure 6 shows the calculated $\kappa_{ph}$ as a function of temperature from 300 K to 1000 K (left side). We see that the $\kappa_{ph}$ along the $x$- and $y$-directions coincides with each other, and the room temperature value is 76.4 W/mK (calculated with respect to a vacuum distance of 3.35 Å), which is almost two orders of magnitude lower than that of graphene (3080~5150 W/mK in Ref. 40). The significant reduction of $\kappa_{ph}$ mainly results from the existence of the $sp$ hybridization of carbon atoms. It was demonstrated that the $sp$ bonds in graphyne are weaker than the $sp^2$ bonds in graphene, thus an inefficient heat transfer by lattice vibrations is introduced [22]. On the other hand, the lower atomic density of graphyne is also believed to be an important factor to reduce the phonon induced thermal conductivity [21]. We further find that the $\kappa_{ph}$ is almost inversely proportional to the temperature, revealing that the Umklapp process predominate the phonon scattering in the temperature range considered [41].

![](./images/867750433060291180_6.jpg)

Figure 6 The temperature dependence of phonon thermal conductivity $\kappa_{ph}$ of $\gamma$-graphyne along the $x$- and $y$-directions (left), and the corresponding $ZT$ values (right).

With all the transport coefficients obtained, we can now evaluate the thermoelectric performance of $\gamma$-graphyne. The right side of Fig. 6 gives the $ZT$ values of $p$-type and $n$-type systems as a function of temperature, where the results for the $x$- and $y$-directions are both shown. In the whole temperature range considered, we see that the $ZT$ values of $p$-type graphyne is much larger than those of the $n$-type system, and this is the case for both the $x$- and $y$-directions. On the other hand, we see that the $ZT$ values exhibit obvious direction dependence, especially for the $p$-type graphyne, which can be attributed to the anisotropic group velocity discussed above. It is interesting to note that regardless of the directions and carrier types, the maximum $ZT$ value always appears at 600 K, which is 1.5 for the $p$-type system along the $x$-direction and 1.0 for the $n$-type system along the $y$-direction. Moreover, we see that in a broad temperature range from 300 K to 1000 K, the $p$-type $ZT$ values are always

higher than 1.0 along both directions, which is very desirable in the application of thermoelectric materials. It should be mentioned that the maximum $ZT$ value of 1.5 is much lower than previously predicted result of 2.9 at 760 K [19], which is caused by the overestimation of the relaxation time in that work using the simple DP theory that do not consider the contribution from the optical phonon scattering. On the other hand, our calculated $ZT$ values are significantly larger than that of graphene ($ZT < 0.01$ in Ref. 42), which originates from the increased Seebeck coefficient and reduced thermal conductivity as discussed above. Table I summarizes the optimized $ZT$ values and the corresponding transport coefficients at different temperature. We see that both the power factor and the phonon thermal conductivity decrease with increasing temperature, which could lead to the maximum $ZT$ values at intermediate temperature of 600 K. If we compare the contribution of the thermal conductivity from the electronic and phonon parts, we find that the thermal transport is dominated by the phonon at low temperature. When the temperature becomes higher, the two parts are comparable to each other. All these findings provide useful means to effectively modulate the transport coefficients so that the thermoelectric performance of $\gamma$-graphyne can be further enhanced.

Table I Optimized $ZT$ values of $p$-type and $n$-type $\gamma$-graphyne along the $x$- and $y$-directions at different temperature. The corresponding carrier concentration, the transport coefficients, and the Lorenz number are also given.

<table>
  <thead>
    <tr>
      <th>$T$ (K)</th>
      <th>system</th>
      <th>carrier concentration ($10^{12}$ cm$^{-2}$)</th>
      <th>$S$ ($\mu$V/K)</th>
      <th>$\sigma$ ($10^6$S/m)</th>
      <th>$S^2\sigma$ (W/mK$^2$)</th>
      <th>$L$ ($10^{-8}$ W$\Omega$/K$^2$)</th>
      <th>$\kappa_e$ (W/mK)</th>
      <th>$\kappa_{ph}$ (W/mK)</th>
      <th>$ZT$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">300</td>
      <td>$x$-$p$</td>
      <td>1.43</td>
      <td>238</td>
      <td>6.15</td>
      <td>0.35</td>
      <td>1.20</td>
      <td>22.1</td>
      <td rowspan="4">76.4</td>
      <td>1.06</td>
    </tr>
    <tr>
      <td>$x$-$n$</td>
      <td>1.24</td>
      <td>−217</td>
      <td>3.92</td>
      <td>0.18</td>
      <td>1.22</td>
      <td>14.3</td>
      <td>0.61</td>
    </tr>
    <tr>
      <td>$y$-$p$</td>
      <td>1.29</td>
      <td>238</td>
      <td>5.53</td>
      <td>0.31</td>
      <td>1.20</td>
      <td>19.8</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>$y$-$n$</td>
      <td>1.02</td>
      <td>−227</td>
      <td>4.54</td>
      <td>0.24</td>
      <td>1.21</td>
      <td>16.4</td>
      <td>0.76</td>
    </tr>
    <tr>
      <td rowspan="4">400</td>
      <td>$x$-$p$</td>
      <td>1.58</td>
      <td>246</td>
      <td>4.28</td>
      <td>0.26</td>
      <td>1.19</td>
      <td>20.4</td>
      <td rowspan="4">59.7</td>
      <td>1.30</td>
    </tr>
    <tr>
      <td>$x$-$n$</td>
      <td>1.50</td>
      <td>−228</td>
      <td>2.90</td>
      <td>0.15</td>
      <td>1.21</td>
      <td>14.0</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>$y$-$p$</td>
      <td>1.46</td>
      <td>246</td>
      <td>3.84</td>
      <td>0.23</td>
      <td>1.19</td>
      <td>18.2</td>
      <td>1.19</td>
    </tr>
    <tr>
      <td>$y$-$n$</td>
      <td>1.22</td>
      <td>−244</td>
      <td>3.23</td>
      <td>0.18</td>
      <td>1.20</td>
      <td>15.5</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td rowspan="4">500</td>
      <td>$x$-$p$</td>
      <td>1.67</td>
      <td>255</td>
      <td>2.94</td>
      <td>0.19</td>
      <td>1.18</td>
      <td>17.3</td>
      <td rowspan="4">49.5</td>
      <td>1.43</td>
    </tr>
    <tr>
      <td>$x$-$n$</td>
      <td>1.82</td>
      <td>−231</td>
      <td>2.22</td>
      <td>0.12</td>
      <td>1.20</td>
      <td>13.4</td>
      <td>0.94</td>
    </tr>
    <tr>
      <td>$y$-$p$</td>
      <td>1.65</td>
      <td>249</td>
      <td>2.76</td>
      <td>0.17</td>
      <td>1.19</td>
      <td>16.4</td>
      <td>1.30</td>
    </tr>
    <tr>
      <td>$y$-$n$</td>
      <td>1.44</td>
      <td>−238</td>
      <td>2.32</td>
      <td>0.13</td>
      <td>1.20</td>
      <td>13.8</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td rowspan="4">600</td>
      <td>$x$-$p$</td>
      <td>2.08</td>
      <td>246</td>
      <td>2.44</td>
      <td>0.15</td>
      <td>1.19</td>
      <td>17.4</td>
      <td rowspan="4">42.4</td>
      <td>1.48</td>
    </tr>
    <tr>
      <td>$x$-$n$</td>
      <td>2.38</td>
      <td>−222</td>
      <td>1.90</td>
      <td>0.09</td>
      <td>1.22</td>
      <td>13.8</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>$y$-$p$</td>
      <td>2.12</td>
      <td>238</td>
      <td>2.33</td>
      <td>0.13</td>
      <td>1.20</td>
      <td>16.7</td>
      <td>1.34</td>
    </tr>
    <tr>
      <td>$y$-$n$</td>
      <td>1.87</td>
      <td>−227</td>
      <td>1.91</td>
      <td>0.10</td>
      <td>1.21</td>
      <td>13.8</td>
      <td>1.05</td>
    </tr>
    <tr>
      <td rowspan="4">700</td>
      <td>$x$-$p$</td>
      <td>2.51</td>
      <td>234</td>
      <td>2.06</td>
      <td>0.11</td>
      <td>1.20</td>
      <td>17.3</td>
      <td rowspan="4">37.1</td>
      <td>1.46</td>
    </tr>
    <tr>
      <td>$x$-$n$</td>
      <td>3.23</td>
      <td>−204</td>
      <td>1.76</td>
      <td>0.07</td>
      <td>1.24</td>
      <td>15.3</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>$y$-$p$</td>
      <td>2.68</td>
      <td>224</td>
      <td>2.04</td>
      <td>0.10</td>
      <td>1.21</td>
      <td>17.3</td>
      <td>1.31</td>
    </tr>
    <tr>
      <td>$y$-$n$</td>
      <td>2.67</td>
      <td>−204</td>
      <td>1.79</td>
      <td>0.07</td>
      <td>1.24</td>
      <td>15.5</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td rowspan="4">800</td>
      <td>$x$-$p$</td>
      <td>3.31</td>
      <td>214</td>
      <td>1.96</td>
      <td>0.09</td>
      <td>1.22</td>
      <td>19.2</td>
      <td rowspan="4">33.0</td>
      <td>1.38</td>
    </tr>
    <tr>
      <td>$x$-$n$</td>
      <td>4.36</td>
      <td>−183</td>
      <td>1.69</td>
      <td>0.06</td>
      <td>1.27</td>
      <td>17.2</td>
      <td>0.91</td>
    </tr>
    <tr>
      <td>$y$-$p$</td>
      <td>3.43</td>
      <td>206</td>
      <td>1.89</td>
      <td>0.08</td>
      <td>1.23</td>
      <td>18.6</td>
      <td>1.24</td>
    </tr>
    <tr>
      <td>$y$-$n$</td>
      <td>3.56</td>
      <td>−183</td>
      <td>1.67</td>
      <td>0.06</td>
      <td>1.27</td>
      <td>17.0</td>
      <td>0.89</td>
    </tr>
    <tr>
      <td rowspan="4">900</td>
      <td>$x$-$p$</td>
      <td>4.25</td>
      <td>195</td>
      <td>1.88</td>
      <td>0.07</td>
      <td>1.27</td>
      <td>21.1</td>
      <td rowspan="4">29.7</td>
      <td>1.27</td>
    </tr>
    <tr>
      <td>$x$-$n$</td>
      <td>5.75</td>
      <td>−164</td>
      <td>1.64</td>
      <td>0.04</td>
      <td>1.31</td>
      <td>19.4</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>$y$-$p$</td>
      <td>4.58</td>
      <td>186</td>
      <td>1.86</td>
      <td>0.06</td>
      <td>1.27</td>
      <td>21.2</td>
      <td>1.13</td>
    </tr>
    <tr>
      <td>$y$-$n$</td>
      <td>4.94</td>
      <td>−160</td>
      <td>1.65</td>
      <td>0.04</td>
      <td>1.33</td>
      <td>19.7</td>
      <td>0.77</td>
    </tr>
    <tr>
      <td rowspan="4">1000</td>
      <td>$x$-$p$</td>
      <td>5.14</td>
      <td>179</td>
      <td>1.77</td>
      <td>0.06</td>
      <td>1.28</td>
      <td>22.6</td>
      <td rowspan="4">27.0</td>
      <td>1.14</td>
    </tr>
    <tr>
      <td>$x$-$n$</td>
      <td>7.69</td>
      <td>−145</td>
      <td>1.65</td>
      <td>0.04</td>
      <td>1.37</td>
      <td>22.5</td>
      <td>0.70</td>
    </tr>
    <tr>
      <td>$y$-$p$</td>
      <td>5.87</td>
      <td>169</td>
      <td>1.82</td>
      <td>0.05</td>
      <td>1.31</td>
      <td>23.7</td>
      <td>1.02</td>
    </tr>
    <tr>
      <td>$y$-$n$</td>
      <td>6.76</td>
      <td>−141</td>
      <td>1.65</td>
      <td>0.03</td>
      <td>1.37</td>
      <td>22.7</td>
      <td>0.66</td>
    </tr>
  </tbody>
</table>


### 4. Summary

In summary, we have studied the thermoelectric properties of $\gamma$-graphyne via first-principles calculations combined with the Boltzmann transport equations for both electron and phonon. As the generally used DP theory does not consider the contribution from the optical phonon scattering, the carrier relaxation time in the present work is carefully treated within the framework of complete electron-phonon coupling. It is thus anticipated that our calculated $ZT$ values could give a better prediction of the thermoelectric performance of $\gamma$-graphyne. The maximum $ZT$ value appears at 600 K, which is 1.5 for the $p$-type system along the $x$-direction and 1.0 for the $n$-type system along the $y$-direction. The significantly superior thermoelectric performance of $\gamma$-graphyne compared with graphene is originated from the existence of the carbon-carbon triple bonds and the opening of the band gap. Our theoretical work suggests that good thermoelectric performance can be also achieved in previously unexpected carbon materials, which has very promising prospect containing the earth-abundant and environment-friendly elements.

### Acknowledgments

We thank financial support from the National Natural Science Foundation (grant No. 11574236 and 51172167) and the "973 Program" of China (Grant No. 2013CB632502).

### Reference

[1] G.J. Snyder, E.S. Toberer, Complex thermoelectric materials, Nat. Mater. 7 (2008) 105–114.

[2] M.S. Dresselhaus, G. Chen, M.Y. Tang, R. Yang, H. Lee, D. Wang, et al., New directions for low-dimensional thermoelectric materials, Adv. Mater. 19 (2007) 1043–1053.

[3] H. Guo, T. Yang, P. Tao, Y. Wang, Z. Zhang, High pressure effect on structure, electronic structure, and thermoelectric properties of $\text{MoS}_2$, J. Appl. Phys. 113 (1) (2013) 013709.

[4] S.Z. Butler, S.M. Hollen, L. Cao, Y. Cui, J.A. Gupta, H.R. Gutiérrez, et al., Progress, challenges, and opportunities in two-dimensional materials beyond graphene, ACS Nano 7 (4) (2013) 2898–2926.

[5] H.Y. Lv, W.J. Lu, D.F. Shao, Y.P. Sun, Enhanced thermoelectric performance of phosphorene by strain-induced band convergence, Phys. Rev. B 90 (8) (2014) 085433.

[6] L.D. Hicks, M.S. Dresselhaus, Effect of quantum-well structures on the thermoelectric figure of merit, Phys. Rev. B 47 (19) (1993) 12727–12731.

[7] L.D. Hicks, M.S. Dresselhaus, Thermoelectric figure of merit of a one-dimensional conductor, Phys. Rev. B 47 (24) (1993) 16631–16634.

[8] K.S. Novoselov, A.K. Geim, S.V. Morozov, D. Jiang, Y. Zhang, S.V. Dubonos, et al., Electric field effect in atomically thin carbon films, Science 306 (5696) (2004) 666–669.

[9] A.H. Castro Neto, F. Guinea, N.M.R. Peres, K.S. Novoselov, A.K. Geim, The electronic properties of graphene, Rev. Mod. Phys. 81 (1) (2009) 109–162.

[10] Y. Xu, Z. Li, W. Duan, Thermal and thermoelectric properties of graphene, Small 10 (11) (2014) 2182–2199.

[11] R.H. Baughman, H. Eckhardt, M. Kertesz, Structure-property predictions for new planar forms of carbon: Layered phases containing $sp^2$ and $sp$ atoms, J. Chem. Phys. 87 (11) (1987) 6687–6699.

[12] B.G. Kim, H.J. Choi, Graphyne: Hexagonal network of carbon with versatile

Dirac cones, Phys. Rev. B 86 (11) (2012) 115435.

[13] G. Li, Y. Li, H. Liu, Y. Guo, Y. Li, D. Zhu, Architecture of graphdiyne nanoscale films, Chem. Commun. 46 (20103) 256-3258.

[14] J. Kang, J. Li, F. Wu, S.S. Li, J.B. Xia, Elastic, electronic, and optical properties of two-dimensional graphyne sheet, J. Phys. Chem. C 115 (2011) 20466-20470.

[15] D. Malko, C. Neiss, F. Viñes, A. Gröling, Competition for graphene: Graphynes with direction-dependent Dirac cones, Phys. Rev. Lett. 108 (8) (2012) 086804.

[16] T. Ouyang, Y. Chen, L.M. Liu, Y. Xie, X. Wei, J. Zhong, Thermal transport in graphyne nanoribbons, Phys. Rev. B 85 (23) (2012) 235436.

[17] Y.Y. Zhang, Q.X. Pei, C.M. Wang, Mechanical properties of graphynes under tension: A molecular dynamics study, Appl. Phys. Lett. 101 (8) (2012) 081909.

[18] N. Narita, S. Nagai, S. Suzuki, K. Nakao, Optimized geometries and electronic structures of graphyne and its family, Phys. Rev. B 58 (16) (1998) 11009-11014.

[19] X. Tan, H. Shao, T. Hu, G Liu, J. Jiang, H. Jiang, High thermoelectric performance in two-dimensional graphyne sheets predicated by first-principles calculations, Phys. Chem. Chem. Phys. 17 (2015) 22872-22881.

[20] X.M. Wang, D.C. Mo, S.S. Lu, On the thermoelectric transport properties of graphyne by the first-principles method, J. Chem. Phys. 138 (20) (2013) 204704.

[21] H. Sevinçli, C. Sevik, Electronic, phononic, and thermoelectric properties of graphyne sheets, Appl. Phys. Lett. 105 (22) (2014) 223108.

[22] Y.Y. Zhang, Q.X. Pei, C.M. Wang, A molecular dynamics investigation on thermal conductivity of graphynes, Comput. Mater. Sci. 65 (2012) 406-410.

[23] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, et al., QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials, J. Phys.: Condens. Matter 21 (2009) 395502.

[24] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (18) (1996) 3865-3868.

[25] S. Baroni, S. de Gironcoli, A. Dal Corso, P. Giannozzi, Phonons and related crystal properties from density-functional perturbation theory, Rev. Mod. Phys. 73 (2)

(2001) 515-562.

[26] F. Giustino, M.L. Cohen, S.G. Louie, Electron-phonon interaction using Wannier functions, Phys. Rev. B 76 (16) (2007) 165108.

[27] J. Noffsinger, F. Giustino, B.D. Malone, C.H. Park, S.G. Louie, M.L. Cohen, EPW: A program for calculating the electron-phonon coupling using maximally localized Wannier functions, Comput. Phys. Commun. 181 (2010) 2140-2148.

[28] S. Poncé, E.R. Margine, C. Verdi, F. Giustino, EPW: Electron-phonon coupling, transport and superconducting properties using maximally localized Wannier functions, arXiv:1604.03525.

[29] B. Liao, J. Zhou, B. Qiu, M.S. Dresselhaus, G. Chen, Ab initio study of electron-phonon interaction in phosphorene, Phys. Rev. B 91 (23) (2015) 235419.

[30] C. Kittel, Introduction to Solid State Physics, John Wiley and Sons, New York, 2005.

[31] W. Li, J. Carrete, N.A. Katcho, N. Mingo, ShengBTE: A solver of the Boltzmann transport equation for phonons, Comput. Phys. Commun. 185 (2014) 1747-1758.

[32] L. Sun, P.H. Jiang, H.J. Liu, D.D. Fan, J.H. Liang, J. Wei, et al., Graphdiyne: A two-dimensional thermoelectric material with high figure of merit, Carbon 90 (2015) 255-259.

[33] M. Bernardi, D. Vigil-Fowler, J. Lischner, J.B. Neaton, S.G. Louie, Ab initio study of hot carriers in the first picosecond after sunlight absorption in silicon, Phys. Rev. Lett. 112 (25) (2014) 257402.

[34] N. Tandon, J.D. Albrecht, L.R. Ram-Mohan, Electron-phonon interaction and scattering in Si and Ge: Implications for phonon engineering, J. Appl. Phys. 118 (4) (2015) 045713.

[35] A. Janotti, C.G. Van de Walle, Absolute deformation potentials and band alignment of wurtzite ZnO, MgO, and CdO, Phys. Rev. B 75 (12) (2007) 121201(R).

[36] P.H. Jiang, H.J. Liu, D.D. Fan, L. Cheng, J. Wei, J. Zhang, et al., Enhanced thermoelectric performance of carbon nanotubes at elevated temperature, Phys. Chem. Chem. Phys. 17 (2015) 27558-27564.

[37] J. Kang, H. Sahin, H.D. Ozaydin, R.T. Senger, F.M. Peeters, TiS₃ nanoribbons: Width-independent band gap and strain-tunable electronic properties, Phys. Rev. B 92 (7) (2015) 075413.

[38] J. Bardeen, W. Shockley, Deformation potentials and mobilities in non-polar crystals, Phys. Rev. 80 (1) (1950) 72–80.

[39] L. Cheng, H.J. Liu, J. Zhang, J. Wei, J.H. Liang, J. Shi, et al., Effects of van der Waals interactions and quasiparticle corrections on the electronic and transport properties of Bi₂Te₃, Phys. Rev. B 90 (8) (2014) 085118.

[40] S. Ghosh, I. Calizo, D. Teweldebrhan, E.P. Pokatilov, D.L. Nika, A.A. Balandin, et al., Extremely high thermal conductivity of graphene: Prospects for thermal management applications in nanoelectronic circuits, Appl. Phys. Lett. 92 (15) (2008) 151911.

[41] H.J. Goldsmid, Introduction to Thermoelectricity, Springer, Heidelberg, 2009.

[42] R. Verma, S. Bhattacharya, S. Mahapatra, Thermoelectric performance of a single-layer graphene sheet for energy harvesting, IEEE Trans. Electron Devices 60 (16) (2013) 2064–2070.