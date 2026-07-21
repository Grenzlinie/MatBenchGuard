# Connection between water's dynamical and structural properties: insights from *ab initio* simulations

Cecilia Herrero, $^{1}$ Michela Pauletti, $^{2}$ Gabriele Tocci, $^{2}$ Marcella Iannuzzi, $^{2}$ and Laurent Joly $^{1,3, *}$

$^{1}$ Univ Lyon, Univ Claude Bernard Lyon 1, CNRS, Institut Lumière Matière, F-69622, Villeurbanne, France
$^{2}$ Department of Chemistry, Universität Zürich, 8057 Zürich, Switzerland
$^{3}$ Institut Universitaire de France (IUF), 1 rue Descartes, 75005 Paris, France
(Dated: December 13, 2021)

Among all fluids, water has always been of special concern for scientists from a broad variety of research fields due to its rich behavior. In particular, some questions remain unanswered nowadays concerning the temperature dependence of bulk and interfacial transport properties of supercooled and liquid water, e.g. regarding the fundamentals of the violation of the Stokes-Einstein relation in the supercooled regime or the subtle relation between structure and dynamical properties. Here we investigated the temperature dependence of the bulk transport properties from *ab initio* molecular dynamics based on density functional theory, down to the supercooled regime. We determined from a selection of functionals, that SCAN better describes the experimental viscosity and self-diffusion coefficient, although we found disagreements at the lowest temperatures. For a limited set of temperatures, we also explored the role of nuclear quantum effects on water dynamics using *ab initio* molecular dynamics that has been accelerated via a recently introduced machine learning approach. We then investigated the molecular mechanisms underlying the different functionals performance and assessed the validity of the Stokes-Einstein relation. We also explored the connection between structural properties and the transport coefficients, verifying the validity of the excess entropy scaling relations for all the functionals. These results pave the way to predict the transport coefficients from the radial distribution function, helping to develop better functionals. On this line, they indicate the importance of describing the long-range features of the radial distribution function.

Water is an ubiquitous liquid, essential for life on earth, and therefore constitutes one of the most important chemical substances. Despite the apparent simplicity of its chemical formula, water is a complex liquid, that after much effort, still evades our complete understanding at the molecular level [1]. Due to its critical relevance with regard to energy harvesting and water purification, several efforts have been carried in order to obtain molecular insights about water behavior under different thermodynamic conditions. Water molecular interactions arise from a balance between van der Waals and hydrogen bonding forces [2, 3], thus a complete description exclusively from classical force field (FF) simulations may hinder some critical mechanisms. *Ab initio* molecular dynamics (AIMD), where interatomic forces are computed from the electronic structure, may play a key role in understanding some important physical processes for bulk and confined water [4-7] as, for instance, the controversial liquid-liquid critical point [8].

A very efficient approach to determine the electronic structure is density functional theory (DFT), based on a formulation of the many-body problem in terms of a functional of the electron density. So far however, many widely used approximations for the exchange-correlation functional do not provide a sufficiently accurate description of many of water properties [9, 10]. The main challenge of semi-local and hybrid density functional approximations in predicting the structure and energetics of water lies in their description of dispersion and exchange-overlap interactions [10, 11]. Additionally, nuclear quantum effects (NQEs) play an important role in determining water structure [12-15]: while on the one hand, NQEs tend to strengthen the hydrogen bond, on the other hand, competing effects due to the spread of the protons in the normal direction tend to weaken it. Although NQEs can be modelled via *ab initio* path integral molecular dynamics (PIMD), accounting for this subtle competition adds an additional level of complexity [12]. Despite recent advances in describing the water structure and thermodynamic properties [16, 17], predicting transport properties from first principles represents a further challenge [18-20]. Limited work has been dedicated to the study of the temperature evolution of the diffusivity and of the shear viscosity with *ab initio* methods [3, 8, 21]. A clearer picture of the molecular mechanisms controlling the water viscosity and diffusion is needed, especially in the supercooled regime [22, 23], where water viscoelasticity is poorly understood [24-26] and the validity of the Stokes-Einstein (SE) relation at low temperatures remains an open question [27-32].

Water dynamics is also crucial in the field of nanoflu-idics [33], where in particular the performances can be boosted by liquid-solid slip, arising from a competition between bulk liquid viscosity and interfacial friction [34-37]. Further, reaching clearer insights into the molecular properties controlling water dynamics would enable to determine a relationship between the structural correlations and molecular transport. Establishing such a thermodynamic link between structure and dynamics would also be instrumental to improve the description of water via DFT.

* laurent.joly@univ-lyon1.fr

Such connection has already been explored in the literature via *e.g.* free-volume models [38, 39], relationships between $g(r)$ and glass transition temperature [40], and the proposition of different structural descriptors [41–43], among which the entropy excess scaling, already employed for AIMD simulations of liquid metals [44] or water [45], stands out [46–48]. The excess of entropy, which can be decomposed in terms on the $N-$body radial distribution functions [49], has been proven to exhibit an exponential relation with the diffusion coefficient for multiple systems [50, 51]. In particular, for glass forming liquids such as supercooled binary mixtures and water, the approximation of the entropy excess by its two body contribution (related to an integral of a function of $g(r)$) has been shown to work well for a broad range of temperatures [48, 52–55]. One of the main limitations for AIMD is its great need of resources as compared to their classical counterparts. Nevertheless, if the link between dynamics and structure is established, we would be able to predict the transport coefficients from structural properties, which require shorter simulation times to converge [56]. Aside of this, entropy excess scaling has also been used as a tool to bring insights into the molecular mechanisms underlying the SE relation [55].

In this report, we determine from a selection of density functionals commonly used to characterise water [10, 11, 57], which one better describes the temperature dependence of the water viscosity and self-diffusion coefficient in its liquid and supercooled state, in comparison with FF simulations using the TIP4P/2005 water model [58]. Additionally, we explore the connection between structural properties and the transport coefficients for all the functionals proposed via the two-body entropy parameter, presenting this physical descriptor as a path to develop better functionals and better compare with experimental results. We used AIMD simulations, describing the electronic structure within DFT, in the NVT ensemble to determine hydrodynamic bulk transport coefficients of three different density functionals: PBE [59] functional with Grimme's D3 corrections [60, 61] (namely PBE-D3), optB88-vdW [62, 63] and SCAN [64]. While describing the electronic structure with the SCAN functional, we also included the role of NQEs by performing PIMD simulations for a limited set of temperatures, by employing a recently introduced machine learning approach to speed-up the calculation of the electronic structure problem [65]. Further simulation details can be found in *Materials and Methods*.

## RESULTS AND DISCUSSION

We display in Fig. 1a (dashed lines) the temperature evolution of the shear viscosity, determined from the long-time plateau of the Green-Kubo integral, $\eta_{\text{GK}}$ (Eq. (8) in Materials and methods), for the different functionals. No plateau was observed for PBE-D3 at $T < 360$ K and optB88-vdW at $T = 260$ K. To benchmark the results, the same procedure was carried for FF simulations with the TIP4P/2005 water model [58], which provides an excellent description of experimental results for both viscosity and diffusion coefficient [37, 66, 67]. In Fig. 1a one can see that the viscosity obtained from the SCAN functional is in better agreement with FF at 330 K and 360 K, although between 260 K and 300 K it overestimates the viscosity by more than a factor of 1.7. With regard to PBE-D3 and optB88-vdW, one observe from Fig. 1a that both functionals overestimate $\eta_{\text{GK}}$ value. Overall, all functionals fail at describing the temperature evolution of the shear viscosity.

![](./images/867760858590085404_1.jpg)

FIG. 1: Temperature evolution for different functionals of (a) shear viscosity and (b) diffusion coefficient. A good agreement is found between the hydrodynamic radius measures (dotted lines) and the Green-Kubo ones (dashed lines), implying all the functionals verify Stokes-Einstein relation with the same hydrodynamic radius $R_{\text{h}}=1$ Å (see text for detail).

The diffusion coefficient $D_{\text{PBC}}$ was determined from the slope of the mean squared displacement in the diffusive regime (see the supporting information, SI). In practice, because of hydrodynamic interactions between the periodic image boxes, a finite size correction for the diffusion coefficient has to be introduced [66, 68, 69]. For a cubic simulation box of size $L_{\text{box}}$ with periodic boundary conditions:

$$
D_{\text{GK}} = D_{\text{PBC}} + 2.837\frac{k_{\text{B}}T}{6\pi\eta_{\text{GK}}L_{\text{box}}}, \tag{1}
$$

with $k_{\text{B}}$ the Boltzmann constant and $T$ the temperature. We denoted $D_{\text{GK}}$ the diffusion coefficient obtained through Eq. (1) because we used $\eta_{\text{GK}}$ in it. $D_{\text{PBC}}$ could not be determined within our simulation times for PBE-D3 at $T < 360$ K and optB88-vdW at $T = 260$ K because the system did not enter in the diffusive regime. This result is consistent with the absence of a plateau for $\eta_{\text{GK}}$. The corrected diffusion coefficient $D_{\text{GK}}$ results are displayed in Fig. 1b (dashed lines). In analogy to $\eta_{\text{GK}}$, one observes in this figure that SCAN is the functional that better describes water diffusion coefficient at high temperatures, although it fails at low $T$.

![](./images/867760858590085404_2.jpg)

FIG. 2: Dimensionless two-body entropy $s_2/k_\text{B}$ for different functionals and for FF as a function of the temperature.

Generally, viscosity $\eta$ and diffusion $D$ are related through the SE relation:
$$
D = \frac{k_\text{B}T}{6\pi\eta R_\text{h}}, \tag{2}
$$
with $R_\text{h}$ the effective hydrodynamic radius of the molecules [70]. Even though the failure of this relation is well known at low temperatures [27–32], it still remains valid for a broad range of temperature. We verified this statement by computing $R_\text{h}$ for FF simulations, obtaining constant $R_\text{h} \sim 1$ Å for the range of temperatures considered in the present study (see the SI).

Taking into account $D$ size correction Eq. (1) and SE relation Eq. (2), one can relate the viscosity to $D_\text{PBC}$ and to the hydrodynamic radius:
$$
\eta R_\text{h} = \frac{k_\text{B}T}{6\pi D_\text{PBC}} \left( \frac{1}{R_\text{h}} - \frac{2.837}{L_\text{box}} \right). \tag{3}
$$

In the same way, one can also determine a relation for $D_{R_\text{h}}$ independent of $\eta$ from Eq. (1) and Eq. (2):
$$
D_{R_\text{h}} = \frac{D_\text{PBC}}{1 - \frac{2.837 R_\text{h}}{L_\text{box}}}. \tag{4}
$$

Therefore, viscosity and diffusion can be determined exclusively from the slope of the mean squared displacement at long times by imposing the hydrodynamic radius $R_\text{h}$. In order to test the applicability of this prediction, in Fig. 1 we display the results for $\eta_{R_\text{h}}$ from Eq. (3) and $D_{R_\text{h}}$ from Eq. (4) by imposing $R_\text{h} = 1$ Å (value in agreement with the FF measures, see the SI). In Fig. 1 one can see a good match between the Green-Kubo and the hydrodynamic radius measures for both transport coefficients and for all the functionals considered, meaning that, although all the functionals fail in predicting viscosity and diffusion temperature dependence, all of them verify the SE relation with the same constant value of $R_\text{h}$.

Having determined the transport properties for the different functionals, we proceed to explore their connection with the structure of water, given by the radial distribution function, $g(r)$. Specifically, we computed the structural descriptor $s_2$ (two-body excess entropy, see the SI), given by the integral [49]:
$$
\frac{s_2}{k_\text{B}} = -2\pi n \int_{0}^{\infty} r^2(g(r)\ln g(r) - g(r) + 1) \mathrm{d}r, \tag{5}
$$
with $n$ the number density of the system.

![](./images/867760858590085404_3.jpg)

FIG. 3: Radial distribution functions (a) and (b) and $-s_2/k_\text{B}$ running integrals (c) and (c) of water at 300 K and 260 K obtained from the SCAN functional with classical and quantum nuclei (SCAN+NQEs) as well as from the FF simulations.

Figure 2 presents the temperature dependence of the dimensionless two-body entropy $s_2/k_\text{B}$ for the different functionals, compared with FF results. We note that, although the $g(r)$ simulated with the TIP4P/2005 FF exhibits some discrepancies with respect to the experimental $g(r)$ [58], the change of $s_2$ with temperature is in qualitative agreement with experiments for a wide range of temperatures, down to the supercooled regime [71].

One can observe that SCAN is the functional that better describes the $s_2$ temperature evolution, as compared to FF. Interestingly, accounting for NQEs (see the SCAN+NQE in Fig. 2) does not produce significant changes in the behavior of $s_2/k_\text{B}$, even at the low temperature of 260 K. Whereas at the highest temperature of 360 K the optB88-vdW functional reproduces the water structure – as represented by the $s_2$ order parameter, using this functional in the supercooled regime gives rise to

serious over structuring, thus leading to an overestimation of more than two times in the value of $s_2$ at 260 K. Instead, PBE-D3 fails at recovering the liquid two-body entropy at any temperature, and the integral in Eq. 5 reaches a plateau for the lowest temperatures, *i.e.* the $g(r)$ oscillations amplitude is not significantly affected by temperature, hinting at a possible glass transition [40].

To elucidate the connection between the water structure and the transport coefficients through the $s_2$ order parameter, we compare the radial distribution functions and the $s_2/k_\text{B}$ running integrals for the FF and the SCAN functional at 260 K and at 300 K, both with classical and with quantum nuclei (see Fig. 3), while the comparison with the PBE-D3 and optB88-vdW functionals can be found in the SI. At 300 K the quantum nuclear $g(r)$ displays a lower first peak compared to the classical one and to the $g(r)$ from the FF, while the rise in the first peak also occurs at a slightly shorter distance. Thus, NQEs give rise to a less structured first coordination shell, in qualitative agreement with experimental results in $\text{H}_2\text{O}$ and $\text{D}_2\text{O}$ which display these same characteristics, respectively [72]. Beyond the first peak, an increased structure is observed in the $g(r)$ predicted with SCAN+NQE, compared to the case with classical nuclei and with the FF result, in disagreement with experiments on light and heavy water [72]. Such discrepancy has been observed in previous PIMD simulations obtained with semi-local density functionals [12, 73], where it was pointed out that the origin of the increased structure of the second peak arises from the destabilization of interstitial hydrogen bonded configurations occurring in quantum nuclear simulations, and more accurate descriptions might alter this balance and lead to a less structured second and third solvation shells [16, 74]. Shifting the focus on the $s_2/k_\text{B}$ running integral (see Fig. 3(c)), it can be noticed that although the largest contribution to the limiting value of $s_2/k_\text{B}$ arises from the first solvation shell, a non-negligible part is also due to the oscillations beyond the first solvation shell. Thus, as a result of a less structured first solvation shell and of more structured second and third shells, the SCAN+NQE functional predicts a limiting value of $s_2/k_\text{B}$ that is similar to SCAN with classical nuclei, whereas the $s_2/k_\text{B}$ value predicted with FF is visibly lower. Interestingly, the differences between the quantum and classical nuclear $g(r)$, observed at 300 K, are attenuated at 260 K, also when comparing with the FF results. This leads to a value of $s_2/k_\text{B}$ that is remarkably similar for all the three methods at 260 K, as seen in Fig. 3(d).

Finally, in order to establish a relation between structure and transport coefficients, we proceed to test the entropy excess scaling laws. With that regard, it has been verified that the entropy excess $s_\text{ex}$ can be approximated by the two-body contribution $s_\text{ex} \simeq s_2$ for water and supercooled binary mixtures [52–55]. As described in Ref. 75, $s_2$ is constructed from the oxygen-oxygen, oxygen-hydrogen, and hydrogen-hydrogen pair distributions. Still, the scaling laws hold well by just computing $s_2$ from the oxygen-oxygen $g(r)$, amounting to only con- sidering the translational 2-body entropy, with a difference of a factor 3 between both estimates, so $s_\text{ex} \simeq 3s_2$ from our results. It can be shown [76] (see the SI) that the dimensionless diffusion coefficient $D/D_0$ is expected to scale as:

$$
\frac{D}{D_0}=A\exp(-B\ s_2/k_\text{B}), \tag{6}
$$

with $D_0=l_0\sqrt{k_\text{B}T/m}$ (where $l_0=n^{-1/3}$ is the average interparticle distance and $m$ is the fluid mass), and $A$ and $B$ dimensionless constants at a given fluid density. Considering this Eq. (6), together with the SE equation, and assuming $R_\text{h} \sim l_0$, one can expect a scaling for the dimensionless viscosity $\eta/\eta_0$ as:

$$
\frac{\eta}{\eta_0}=A'\exp(-B'\ s_2/k_\text{B}), \tag{7}
$$

with $\eta_0=\sqrt{mk_\text{B}T}/l_0^2$. From the SE relation one expects $B'=-B$.

![](./images/867760858590085404_4.jpg)

FIG. 4: Reduced (a) viscosity $\eta/\eta_0$ and (b) diffusion coefficient $D/D_0$, defined in Eq. (6) and Eq. (7), as a function of the dimensionless two-body entropy $s_2/k_\text{B}$ for different functionals and FF simulations. In continuum line are represented the respective exponential fits for each functional. The fit results are detailed in Table I. The color and marker style representing the different functionals is the same as in Fig. 2.

We tested Eq. (6) and Eq. (7) for the different functionals. Figure 4 shows the results for the dimensionless transport coefficients as a function of the two-body entropy excess for the different functionals. One can see that, although the functionals predict different transport coefficients (Fig. 1) and $s_2$ results (Fig. 5), all of them verify an exponential scaling of $\eta_\text{GK}/\eta_0$ and $D_\text{GK}/D_0$ with $s_2$. Therefore, we fitted the relations in Eq. (6) and Eq. (7) for optB88-vdW, SCAN, and FF (continuous lines in Fig. 4). No fit was performed for PBE-D3 due to the single value measure we could report for this functional. The fit results are indicated in Table I. One can observe that, although out of the error bars, the fit

<table><caption>Table I: Fit parameters of the two-body excess entropy scaling relation for the dimensionless viscosity and diffusion coefficient, for different functionals and FF simulations. The fit corresponds to the function $y = A\mathrm{exp}(-Bs_2/k_\mathrm{B})$ with $y$ the dimensionless viscosity $\eta_\mathrm{GK}/\eta_0$, following Eq. (7), and diffusion coefficient $D_\mathrm{GK}/D_0$, following Eq. (6).</caption>
    <thead>
        <tr>
            <th rowspan="2"></th>
            <td colspan="2">$\eta_\mathrm{GK}/\eta_0$</td>
            <td colspan="2">$D_\mathrm{GK}/D_0$</td>
        </tr>
        <tr>
            <td>$A'$</td>
            <td>$B'$</td>
            <td>$A$</td>
            <td>$B$</td>
        </tr>
        <tr>
            <th></th>
            <td colspan="2">($\times 10^{-1}$)</td>
            <td colspan="2">($\times 10^{-1}$)</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>optB88-vdW</th>
            <td>$4.29(1.39)$</td>
            <td>$4.11(0.34)$</td>
            <td>$3.52(0.29)$</td>
            <td>$-3.97(0.09)$</td>
        </tr>
        <tr>
            <th>SCAN</th>
            <td>$1.79(0.48)$</td>
            <td>$5.31(0.31)$</td>
            <td>$8.17(2.49)$</td>
            <td>$-5.24(0.36)$</td>
        </tr>
        <tr>
            <th>FF</th>
            <td>$1.92(0.26)$</td>
            <td>$4.52(0.18)$</td>
            <td>$7.73(1.25)$</td>
            <td>$-4.58(0.21)$</td>
        </tr>
    </tbody>
</table>

parameters for SCAN and FF are the closest ones and that, for all functionals, $B'=-B$, implying a verification of the SE relation, Eq. (2).

One can exploit the exponential relationship between the transport coefficients and $s_2$ to predict transport properties from structural ones: once the fitting parameters in Eqs. (6-7) have been extracted by calculating the dependence of $\eta$ and $D$ on $s_2$ for a limited set of temperatures, the value of the transport coefficients can be obtained just from the calculation of the $s_2$ order parameter via the radial distribution function also for a wider temperature range. Indeed, generally structural properties such as the $g(r)$ require shorter simulations to converge, especially when using force based methods, as the one proposed in Ref. 56, to reduce the variance when compared to the conventional strategies based on particles positions binning. Figure 5 presents the Green-Kubo results and their comparison with the prediction resulting from the fit via $s_2$. One can see good agreement between the explicit calculation of transport coefficients and their and predictions via $s_2$ for all the data. Also, although the transport coefficients could not be calculated explicitly for the optB88-vdWfunctional at the lowest temperature of $260\,\mathrm{K}$, they could be determined from the exponential relationship with $s_2$, yielding an exceedingly high viscosity and low diffusion, and thus verifying the failure of this functional in reproducing the temperature dependence of both transport coefficients.

## CONCLUSIONS

In summary, among the selected DFT functionals, SCAN best captures the temperature evolution of water transport properties - as described by the the accurate TIP4P/2005 FF - despite the disagreement observed at temperatures of $300\,\mathrm{K}$ and below. We detected large discrepancies between functionals, with a major failure of PBE-D3, which is far too viscous. Despite these discrepancies, the SE relation was observed to hold in the considered temperature range for all the functionals and, moreover, all of them predicted the same hydrodynamic radius $R_\mathrm{h}\sim 1\,\mathring{\mathrm{A}}$. This property, together with the finite size correction for the diffusion coefficient, allowed us to propose a measure of viscosity $\eta_{R_\mathrm{h}}$ and diffusion coefficient $D_{R_\mathrm{h}}$, based only on the slope of the mean squared displacement in the diffusive regime $D_\mathrm{PBC}$, for known box size and fixed $R_\mathrm{h}$.

![](./images/867760858590085404_5.jpg)

FIG. 5: Temperature evolution for different functionals of (a) shear viscosity from Eq. (7) and (b) diffusion coefficient from Eq. (6) with fit parameters from Table I. A good agreement is found between the $s_2$ based prediction (dotted lines) and the explicit calculation (dashed lines), verifying the link between the structure and the transport coefficients. The color and marker style representing the different functionals is the same as in Fig. 1.

Motivated by a possible connection between dynamics and structure, we computed the radial distribution functions for the different functionals. Analogously to the transport coefficient results, we observed that SCAN radial distribution function is the one that better compares to FF, with little differences at the lowest temperatures in the second and third solvation shells, whereas PBE-D3 was far more structured that SCAN and optB88-vdW at high temperatures, in agreement with the high viscosity value measured for this functional. An explicit relationship between dynamic and structure can be established through the two-body entropy excess, which is an integral of a function of the radial distribution function. We verified the exponential relation on $s_2$ for both reduced bulk transport coefficients and, although the connection between $s_2$ and transport properties is not univocal, as different fitting parameters were used for each functional, the fitting parameters all have the same order of magnitude. We suggest that the non-universality of the exponential relation is due to the use of the translational two-body excess entropy; a more universal relation could be observed by using the full two-body excess entropy, although the related structural features would be less easy to interpret.

Finally, based on the established exponential relation between the bulk transport coefficients, we computed

both viscosity and diffusion coefficient from the $s_2$ results and the fitting parameters. This allowed us to estimate transport coefficients for functionals strongly structured (for instance optB88-vdW at 260 K), which present such a high viscosity value that longer simulations are needed in order to observe a well-defined plateau in the Green-Kubo integral. Therefore we propose here that, once the exponential dependence has been determined for a few temperatures, the viscosity and diffusion coefficient can be determined only from structural properties, which typically require shorter simulation times to converge [56]. This can be a useful technique to apply in order to calculate transport coefficients for very viscous systems, where the associated time-scales are far from the ones computationally reachable with AIMD simulations. The connection between transport coefficients and the radial distribution function via the two-body entropy excess also establishes some guidelines to choose a functional for simulations of nanofluidic systems, where a functional which better reproduces water's structure will more likely reproduce its dynamical properties. The $s_2$ order parameter can be also employed as an instrumental tool to gauge the potential of DFT or of high accuracy methods in describing dynamics without computing transport properties explicitly, where the comparison between different $s_2$ values becomes more straightforward than the comparison between two $g(r)$ profiles, or just the value of the $g(r)$ minimum or maximum, which does not ensure a full structure correlation. Indeed, from the $s_2(r)$ running integrals, we showed the importance of reproducing not only the first solvation shell of the $g(r)$ but also the long range structure, which is a non-negligible contribution to $s_2$ value. This feature, together with the scaling behavior of the bulk transport coefficients as a function of entropy, suggests that it is important that DFT reproduces not only the first peak in the $g(r)$, but also its long range behavior, which is critical to obtain an accurate description of dynamical properties such as viscosity and diffusion coefficient.

It is worth discussing the possible origins of the discrepancies of the temperature evolution of of the viscosity and of the diffusion coefficient, especially striking for the SCAN functional, which shows good agreement with FF and experiments at high temperatures but it overestimates the viscosity and underestimates the diffusivity at low temperatures. Although one might expect that the inclusion of zero-point energy and quantum tunneling, which become increasingly relevant at lower temperatures, would play an important role, we have shown that taking NQEs into account did not improve upon the results obtained with classical nuclei. As such, the most likely source of discrepancy lies in the approximate description of the electronic structure with the chosen functionals. Capturing the delicate balance between van der Waals dispersion and exchange interactions constitutes the main challenge for the description of water [10] and it is also critical in order to predict water transport properties below room temperature. It remains to be seen whether the use of high-accuracy methods such as the random-phase approximation (RPA), Møller-Plesset perturbation theory [11] and quantum Monte Carlo [77] would improve upon the current description of water transport properties also in super-cooled conditions. Recent results on the diffusion coefficient for a wide range of temperatures obtained with RPA, also including the role of NQEs are promising in this regard [78]. As a further interesting perspective of this work, the established connection between the structure and dynamics might reveal what tips the balance between the strengthening and the weakening quantum delocalization effects of the H-bond network in water. Since diffusion is found experimentally to vary significantly between $D_2O$ and $H_2O$ [12], and $s_2$ is directly connected to diffusion, one can gauge the impact of the competing H-bond strengthening and weakening NQEs on the structure and the dynamics directly from the experimental measurements of the diffusivity and of the radial distribution function of light and heavy water at different temperatures.

## MATERIALS AND METHODS

### Simulation Details

We performed AIMD simulations of 32 water molecules in bulk using DFT with the CP2K code (development version) [79], which employs the Gaussian and Plane waves (GPW) method to describe the wave-function and the electron density and to solve the Kohn-Sham equations [80]. Three different density functionals were considered: PBE [59] functional with Grimme's D3 corrections [60, 61], optB88-vdW [62, 63] and SCAN [64]. The electronic structure problem was solved within the Born-Oppenheimer approximation for 5 different temperatures $(T = \{260,270,300,330,360\}$ K (the two lowest ones corresponding to the expected supercooled regime) controlled via the Nosé-Hoover thermostat. We worked at constant volume with a box size such that $\rho=1$ g/cm$^3$ ($L_{\rm box}=9.85$ Å for 32 water molecules). The running time was $\simeq$ 120 ps for all functionals and temperatures except optB88-vdW and $T=\{260,270\}$ K, with running time $\simeq$ 240 ps. The timestep considered was 0.5 ps. The initial configuration for all the functionals corresponded to the steady state at the given temperature obtained from force field (FF) MD after a running time of 200 ps. The energy cutoff for plane waves was 600 Ry for PBE-D3 and optB88-vdW, and 800 Ry for SCAN, and the localized Gaussian basis set was short range molecularly optimized double-$\zeta$ valence polarized (DZVP-MOLOPT-SR) [81].

NQEs were modelled using PIMD simulations with a thermostatted ring polymer contraction scheme using 24 replicas [82, 83]. PIMD simulations were performed using the i-PI code [84] together with CP2K, where the former is used to propagate the quantum nuclear dynamics, whereas the latter is used for the optimization of the

wave-function and to calculate the forces on each atom.
Sampling in the canonical ensemble has been carried out
at 260 K and at 300 K for 35 ps. Further, in the case of the
PIMD simulations, the electronic structure problem is
solved using subsystem density functional theory within
the Kim-Gordon (KG) scheme, where the shortcomings
of the electronic kinetic energy term of KG-DFT are ad-
dressed by correcting this term via a $\Delta$-machine learn-
ing approach [85]. Specifically, we use a neural-network
potential based on the Behler-Parrinello scheme [86] to
learn the difference in the total energy and atomic forces
between KS-DFT and KG-DFT (see Ref. 65 and the
SI for further details). The resulting $\Delta$-learning method
provides the same accuracy of KS-DFT at the lower com-
putational cost of KG-DFT.

We also performed force field (classical MD) simula-
tions via the LAMMPS package [87]. Analogously to
AIMD, we worked in the NVT ensemble with the temper-
ature controlled via a Nosé-Hoover thermostat and with a
volume such that $\rho=1\,\text{g/cm}^3$. Three different box sizes
were considered: 32 water molecules ($L_{\text{box}}=9.85\,\text{\AA}$),
64 water molecules ($L_{\text{box}}=12.42\,\text{\AA}$) and 128 water
molecules ($L_{\text{box}}=15.64\,\text{\AA}$). The water model considered
in all the cases was TIP4P/2005 [58].

## Shear Viscosity and Diffusion Coefficient

For all the simulations, we determined the shear vis-
cosity from the Green-Kubo relation:

$$
\eta_{\mathrm{GK}}=\frac{V}{k_{\mathrm{B}} T} \int_{0}^{\infty}\left\langle p_{i j}(t) p_{i j}(0)\right\rangle \mathrm{d} t,
\tag{8}
$$

with $V$ the volume, $k_{\mathrm{B}}$ the Boltzmann constant, $T$ the
temperature and $p_{i j}=\{p_{xy},p_{xz},p_{yz}\}$ the non-diagonal
components of the stress tensor.

The error bars were computed within $60\%$ of confi-
dence level. For viscosity, the total MD stress was di-
vided in three time slots of equal length, each of them
containing three independent measures of $\eta$. $\eta_{\mathrm{GK}}$ was
measured at the time where the $\eta(t)$ running integral
reached a time plateau (see the SI). Therefore 9 indepen-
dent viscosity values were computed for each functional
at a given temperature. For the diffusion coefficient, the
first 20 ps were removed from the trajectory so the system
equilibration from the initial configuration does not af-
fect the mean squared displacement results. From them,
3 independent measures of $D_{\mathrm{PBC}}$ were obtained from the
three independent Cartesian components.

## ACKNOWLEDGMENTS

The authors thank G. Galliero, S. Gelin and J.-M. Si-
mon for fruitful discussions. We are also grateful for HPC
resources from GENCI/TGCC (grants A0050810637 and
A0070810637), from the PSMN mesocenter in Lyon and
from the Swiss National Supercomputing Centre (CSCS)
under project ID uzh1. LJ is supported by the Insti-
tut Universitaire de France. GT is supported by the
Swiss National Science Foundation through the project
PZ00P2_179964.

[1] P. Gallo, K. Amann-Winkel, C. A. Angell, M. A. Anisi-
mov, F. Caupin, C. Chakravarty, E. Lascaris, T. Loert-
ing, A. Z. Panagiotopoulos, J. Russo, J. A. Sellberg, H. E.
Stanley, H. Tanaka, C. Vega, L. Xu, and L. G. M. Petters-
son, Water: A Tale of Two Liquids, Chemical Reviews
116, 7463 (2016).

[2] F. H. Stillinger, Water revisited, Science 209,
10.1126/science.209.4455.451 (1980).

[3] T. Morawietz, A. Singraber, C. Dellago, and J. Behler,
How van der waals interactions determine the unique
properties of water, Proceedings of the National
Academy of Sciences of the United States of America
113, 8368 (2016), arXiv:1606.07775.

[4] H.-S. Lee and M. E. Tuckerman, Structure of liquid water
at ambient temperature from ab initio molecular dynam-
ics performed in the complete basis set limit, The Journal
of chemical physics 125, 154507 (2006).

[5] G. Cicero, J. C. Grossman, E. Schwegler, F. Gygi, and
G. Galli, Water confined in nanotubes and between
graphene sheets: A first principle study, Journal of the
American Chemical Society 130, 1871 (2008).

[6] O. Wohlfahrt, C. Dellago, and M. Sega, Ab ini-
tio structure and thermodynamics of the rpbe-d3 wa-
ter/vapor interface by neural-network molecular dynam-
ics, The Journal of Chemical Physics 153, 144710 (2020),
https://doi.org/10.1063/5.0021852.

[7] Z. Ye, A. Prominski, B. Tian, and G. Galli, Prob-
ing the electronic properties of the electrified sili-
con/water interface by combining simulations and
experiments, Proceedings of the National Academy
of Sciences 118, 10.1073/pnas.2114929118 (2021),
https://www.pnas.org/content/118/46/e2114929118.full.pdf.

[8] T. E. Gartner, L. Zhang, P. M. Piaggi, R. Car, A. Z.
Panagiotopoulos, and P. G. Debenedetti, Signatures of
a liquid-liquid transition in an ab initio deep neural
network model for water, Proceedings of the National
Academy of Sciences 117, 26040 (2020).

[9] A. Bankura, A. Karmakar, V. Carnevale, A. Chandra,
and M. L. Klein, Structure, dynamics, and spectral dif-
fusion of water from first-principles molecular dynamics,
The Journal of Physical Chemistry C 118, 29401 (2014).

[10] M. J. Gillan, D. Alfè, and A. Michaelides, Per-
spective: How good is DFT for water?, Journal
of Chemical Physics 144, 10.1063/1.4944633 (2016),
arXiv:1603.01990.

[11] M. D. Ben, J. Hutter, and J. VandeVondel, Probing
the structural and dynamical properties of liquid water
with models including non-local electron correlation, The

Journal of Chemical Physics 143, 54506 (2015).

[12] M. Ceriotti, W. Fang, P. G. Kusalik, R. H. McKenzie, A. Michaelides, M. A. Morales, and T. E. Markland, Nu-clear Quantum Effects in Water and Aqueous Systems: Experiment, Theory, and Current Challenges, Chemical Reviews 116, 7529 (2016).

[13] O. Marsalek and T. E. Markland, Quantum dynamics and spectroscopy of ab initio liquid water: The interplay of nuclear and electronic quantum effects, The journal of physical chemistry letters 8, 1545 (2017).

[14] M. Rossi, V. Kapil, and M. Ceriotti, Fine tuning clas-sical and quantum molecular dynamics using a gener-alized Langevin equation, Journal of Chemical Physics 148, 10.1063/1.4990536 (2018), arXiv:1704.05099.

[15] M. Ceriotti, G. Bussi, and M. Parrinello, Nuclear quan-tum effects in solids using a colored-noise thermostat, Physical Review Letters 103, 1 (2009), arXiv:0903.4551.

[16] B. Cheng, E. A. Engel, J. Behler, C. Dellago, and M. Ce-riotti, Ab initio thermodynamics of liquid and solid wa-ter, Proceedings of the National Academy of Sciences 116, 1110 (2019).

[17] A. Reinhardt and B. Cheng, Quantum-mechanical explo-ration of the phase diagram of water, Nature communi-cations 12, 1 (2021).

[18] T. D. Kühne, M. Krack, and M. Parrinello, Static and dy-namical properties of liquid water from first principles by a novel car-parrinello-like approach http://pubs.acs.org, Journal of Chemical Theory and Computation 5, 235 (2009).

[19] M. Chen, H. Y. Ko, R. C. Remsing, M. F. Calegari An-drade, B. Santra, Z. Sun, A. Selloni, R. Car, M. L. Klein, J. P. Perdew, and X. Wu, Ab initio theory and modeling of water, Proceedings of the National Academy of Sci-ences of the United States of America 114, 10846 (2017), arXiv:1709.10493.

[20] H. S. Lee and M. E. Tuckerman, Dynamical properties of liquid water from ab initio molecular dynamics per-formed in the complete basis set limit, Journal of Chem-ical Physics 126, 10.1063/1.2718521 (2007).

[21] D. Alfè and M. J. Gillan, First-Principles Calculation of Transport Coefficients, Physical Review Letters 81, 5161 (1998).

[22] P. Gallo, F. Sciortino, P. Tartaglia, and S.-H. H. Chen, Slow Dynamics of Water Molecules in Supercooled States, Physical Review Letters 76, 2730 (1996).

[23] P. G. Debenedetti, Supercooled and glassy water, Jour-nal of Physics Condensed Matter 15, 10.1088/0953-8984/15/45/R01 (2003).

[24] J. C. F. Schulz, A. Schlaich, M. Heyden, R. R. Netz, and J. Kappler, Molecular interpretation of the non-Newtonian viscoelastic behavior of liquid water at high frequencies, Physical Review Fluids 5, 103301 (2020).

[25] I. de Almeida Ribeiro and M. de Koning, Non-Newtonian flow effects in supercooled water, Physical Review Re-search 2, 1 (2020).

[26] T. J. O'Sullivan, S. K. Kannam, D. Chakraborty, B. D. Todd, and J. E. Sader, Viscoelasticity of liquid water in-vestigated using molecular dynamics simulations, Physi-cal Review Fluids 4, 123302 (2019).

[27] Y. Jung, J. P. Garrahan, and D. Chandler, Excitation lines and the breakdown of Stokes-Einstein relations in supercooled liquids, Physical Review E 69, 61205 (2004).

[28] S.-H. Chen, F. Mallamace, C.-Y. Mou, M. Broccio, C. Corsaro, A. Faraone, and L. Liu, The violation of the Stokes-Einstein relation in supercooled water, Pro-ceedings of the National Academy of Sciences 103, 12974 (2006).

[29] P. Kumar, S. V. Buldyrev, S. R. Becker, P. H. Poole, F. W. Starr, and H. E. Stanley, Relation between the Widom line and the breakdown of the Stokes-Einstein re-lation in supercooled water, Proceedings of the National Academy of Sciences of the United States of America 104, 10.1073/pnas.0702608104 (2007).

[30] L. Xu, F. Mallamace, Z. Yan, F. W. Starr, S. V. Buldyrev, and H. E. Stanley, Appearance of a fractional Stokes-Einstein relation in water and a structural inter-pretation of its onset, Nature Physics 5, 565 (2009).

[31] Z. Shi, P. G. Debenedetti, and F. H. Stillinger, Relaxation processes in liquids: Variations on a theme by Stokes and Einstein, The Journal of Chemical Physics 138, 12A526 (2013).

[32] T. Kawasaki and K. Kim, Identifying time scales for vio-lation/preservation of Stokes-Einstein relation in super-cooled water, Science Advances 3, e1700399 (2017).

[33] L. Bocquet and E. Charlaix, Nanofluidics, from bulk to interfaces, Chemical Society Reviews 39, 1073 (2010).

[34] A. Boțan, B. Rotenberg, V. Marry, P. Turq, and B. Noetinger, Hydrodynamics in clay nanopores, Jour-nal of Physical Chemistry C 115, 16109 (2011).

[35] B. Cross, C. Barraud, C. Picard, L. Léger, F. Restagno, and É. Charlaix, Wall slip of complex fluids: Interfacial friction versus slip length, Physical Review Fluids 3, 1 (2018).

[36] G. Tocci, M. Bilichenko, L. Joly, and M. Iannuzzi, Ab initio nanofluidics: Disentangling the role of the energy landscape and of density correlations on liquid/solid fric-tion, Nanoscale 12, 10.1039/d0nr02511a (2020).

[37] C. Herrero, G. Tocci, S. Merabia, and L. Joly, Fast in-crease of nanofluidic slip in supercooled water: the key role of dynamics, Nanoscale 12, 20396 (2020).

[38] M. H. Cohen and D. Turnbull, Molecular transport in liquids and glasses, The Journal of Chemical Physics 31, 1164 (1959).

[39] D. Turnbull and M. H. Cohen, Free-volume model of the amorphous phase: Glass transition, The Journal of Chemical Physics 34, 120 (1961).

[40] M. I. Ojovan and D. V. Louzguine-Luzgin, Revealing Structural Changes at Glass Transition via Radial Distri-bution Functions, Journal of Physical Chemistry B 124, 3186 (2020).

[41] J. Russo and H. Tanaka, Understanding water's anoma-lies with locally favoured structures, Nature Communi-cations 5, 3556 (2014), arXiv:1308.4231.

[42] R. Shi, J. Russo, and H. Tanaka, Origin of the emer-gent fragile-to-strong transition in supercooled water, Proceedings of the National Academy of Sciences of the United States of America 115, 9444 (2018).

[43] H. Tong and H. Tanaka, Structural order as a genuine control parameter of dynamics in simple glass formers, Nature Communications 10, 4 (2019).

[44] M. Gao and M. Widom, Information entropy of liquid metals, The Journal of Physical Chemistry B 122, 3550 (2018).

[45] C. Zhang, L. Spanu, and G. Galli, Entropy of liquid wa-ter from ab initio molecular dynamics, The Journal of Physical Chemistry B 115, 14190 (2011).

[46] M. Dzugutov, A universal scaling law for atomic diffusion

in condensed matter, Nature 381, 137 (1996).

[47] I. Yokoyama, A relationship between excess entropy and diffusion coefficient for liquid metals near the melting point, Physica B: Condensed Matter 254, 172 (1998).

[48] T. S. Ingebrigtsen and H. Tanaka, Structural predictor for nonlinear sheared dynamics in simple glass-forming liquids, Proceedings of the National Academy of Sciences of the United States of America 115, 87 (2018).

[49] A. Baranyai and D. J. Evans, Direct entropy calcula- tion from computer simulation of liquids, Journal of Non- Crystalline Solids 117-118, 593 (1990).

[50] Y. D. Fomin, V. N. Ryzhov, B. A. Klumov, and E. N. Tsiok, How to quantify structural anomalies in fluids?, The Journal of Chemical Physics 141, 34508 (2014).

[51] M. K. Nandi, A. Banerjee, S. Sengupta, S. Sastry, and S. M. Bhattacharyya, Unraveling the success and failure of mode coupling theory from consideration of entropy, The Journal of Chemical Physics 143, 174504 (2015).

[52] J. Mittal, J. R. Errington, and T. M. Truskett, Quanti- tative Link between Single-Particle Dynamics and Static Structure of Supercooled Liquids, The Journal of Physi- cal Chemistry B 110, 18147 (2006).

[53] J. Mittal, J. R. Errington, and T. M. Truskett, Rela- tionships between Self-Diffusivity, Packing Fraction, and Excess Entropy in Simple Bulk and Confined Fluids, The Journal of Physical Chemistry B 111, 10054 (2007).

[54] R. Chopra, T. M. Truskett, and J. R. Errington, On the use of excess entropy scaling to describe single-molecule and collective dynamic properties of hydrocarbon iso-mer fluids, Journal of Physical Chemistry B 114, 16487 (2010).

[55] I. H. Bell, J. C. Dyre, and T. S. Ingebrigtsen, Excess- entropy scaling in supercooled binary mixtures, Nature Communications 11, 4300 (2020).

[56] B. Rotenberg, Use the force! Reduced variance estima- tors for densities, radial distribution functions, and lo- cal mobilities in molecular simulations, The Journal of Chemical Physics 153, 150902 (2020).

[57] L. Zheng, M. Chen, Z. Sun, H.-Y. Ko, B. Santra, P. Dhu- vad, and X. Wu, Structural, electronic, and dynamical properties of liquid water by ab initio molecular dynam- ics based on scan functional within the canonical ensem- ble, The Journal of Chemical Physics 148, 164505 (2018), https://doi.org/10.1063/1.5023611.

[58] J. L. Abascal and C. Vega, A general purpose model for the condensed phases of water: TIP4P/2005, Journal of Chemical Physics 123, 1 (2005).

[59] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Physical Review Letters 77, 3865 (1996).

[60] S. Grimme, Accurate description of van der Waals com- plexes by density functional theory including empiri- cal corrections, Journal of Computational Chemistry 25, 1463 (2004).

[61] S. Grimme, Semiempirical GGA-type density functional constructed with a long-range dispersion correction, Journal of Computational Chemistry 27, 1787 (2006).

[62] J. Klimeš, D. R. Bowler, and A. Michaelides, Chemi- cal accuracy for the van der Waals density functional, Journal of Physics Condensed Matter 22, 22201 (2010), arXiv:0910.0438.

[63] J. Klimeš, D. R. Bowler, and A. Michaelides, Van der Waals density functionals applied to solids, Physical Re- view B - Condensed Matter and Materials Physics 83, 195131 (2011), arXiv:1102.1358.

[64] J. Sun, A. Ruzsinszky, and J. Perdew, Strongly Con- strained and Appropriately Normed Semilocal Density Functional, Physical Review Letters 115, 36402 (2015).

[65] M. Pauletti, V. V. Rybkin, and M. Iannuzzi, Subsystem density functional theory augmented by a delta learn- ing approach to achieve kohn-sham accuracy, Journal of Chemical Theory and Computation 17, 6423 (2021).

[66] S. Tazi, A. Boţan, M. Salanne, V. Marry, P. Turq, and B. Rotenberg, Diffusion coefficient and shear viscosity of rigid water models, Journal of Physics: Condensed Matter 24, 284117 (2012).

[67] E. Guillaud, S. Merabia, D. de Ligny, and L. Joly, Decoupling of viscosity and relaxation processes in su- percooled water: a molecular dynamics study with the TIP4P/2005f model, Physical Chemistry Chemical Physics 19, 2124 (2017).

[68] I.-C. Yeh and G. Hummer, System-Size Dependence of Diffusion Coefficients and Viscosities from Molecular Dy- namics Simulations with Periodic Boundary Conditions, The Journal of Physical Chemistry B 108, 15873 (2004).

[69] P. M. de Hijes, E. Sanz, L. Joly, C. Valeriani, and F. Caupin, Viscosity and self-diffusion of supercooled and stretched water from molecular dynamics simulations, The Journal of Chemical Physics 149, 94503 (2018).

[70] L. B. Weiss, V. Dahirel, V. Marry, and M. Jardat, Computation of the hydrodynamic radius of charged nanoparticles from nonequilibrium molecular dynamics, The Journal of Physical Chemistry B 122, 5940 (2018).

[71] G. Camisasca, H. Pathak, K. T. Wikfeldt, and L. G. M. Pettersson, Radial distribution functions of water: Mod- els vs experiments, The Journal of Chemical Physics 151, 044502 (2019).

[72] A. Soper and C. Benmore, Quantum differences be- tween heavy and light water, Physical review letters 101, 065502 (2008).

[73] P. Gasparotto, A. A. Hassanali, and M. Ceriotti, Probing defects and correlations in the hydrogen-bond network of ab initio water, Journal of chemical theory and compu- tation 12, 1953 (2016).

[74] M. Del Ben, J. Hutter, and J. VandeVondele, Probing the structural and dynamical properties of liquid water with models including non-local electron correlation, The Journal of chemical physics 143, 054506 (2015).

[75] M. Agarwal, M. P. Alam, and C. Chakravarty, Ther- modynamic, diffusional, and structural anomalies in rigid-body water models, The Journal of Physical Chemistry B 115, 6935 (2011), pMID: 21553909, https://doi.org/10.1021/jp110695t.

[76] J. C. Dyre, Perspective: Excess-entropy scaling, The Journal of chemical physics 149, 210901 (2018).

[77] A. Zen, Y. Luo, G. Mazzola, L. Guidoni, and S. Sorella, Ab initio molecular dynamics simulation of liquid water by quantum monte carlo, The Journal of chemical physics 142, 144111 (2015).

[78] Y. Yao and Y. Kanai, Nuclear quantum effect and its temperature dependence in liquid water from random phase approximation via artificial neural network, The journal of physical chemistry letters 12, 6354 (2021).

[79] T. D. Kühne, M. Iannuzzi, M. Del Ben, V. V. Ry- bkin, P. Seewald, F. Stein, T. Laino, R. Z. Khaliullin, O. Schütt, F. Schiffmann, et al., Cp2k: An electronic structure and molecular dynamics software package- quickstep: Efficient and accurate electronic structure cal-

culations, The Journal of Chemical Physics 152, 194103 (2020).

[80] J. VandeVondele, M. Krack, F. Mohamed, M. Parrinello, T. Chassaing, and J. Hutter, Quickstep: Fast and accu- rate density functional calculations using a mixed Gaus- sian and plane waves approach, Computer Physics Com- munications 167, 103 (2005).

[81] J. VandeVondele and J. Hutter, Gaussian basis sets for accurate calculations on molecular systems in gas and condensed phases, The Journal of Chemical Physics 127, 114105 (2007).

[82] I. R. Craig and D. E. Manolopoulos, Quantum statistics and classical mechanics: Real time correlation functions from ring polymer molecular dynamics, The Journal of chemical physics 121, 3368 (2004).

[83] S. Habershon, D. E. Manolopoulos, T. E. Markland, and T. F. Miller III, Ring-polymer molecular dynamics: Quantum effects in chemical dynamics from classical tra- jectories in an extended phase space, Annual review of physical chemistry 64, 387 (2013).

[84] V. Kapil, M. Rossi, O. Marsalek, R. Petraglia, Y. Lit- man, T. Spura, B. Cheng, A. Cuzzocrea, R. H. Meißner, D. M. Wilkins, et al., i-pi 2.0: A universal force engine for advanced molecular simulations, Computer Physics Communications 236, 214 (2019).

[85] R. Ramakrishnan, P. O. Dral, M. Rupp, and O. A. von Lilienfeld, Big data meets quantum chemistry approx- imations: the $\delta$-machine learning approach, Journal of chemical theory and computation 11, 2087 (2015).

[86] J. Behler and M. Parrinello, Generalized neural-network representation of high-dimensional potential-energy sur- faces, Physical review letters 98, 146401 (2007).

[87] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolin- tineanu, W. M. Brown, P. S. Crozier, P. J. in 't Veld, A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, and S. J. Plimpton, Lammps - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales, Computer Physics Communications 271, 108171 (2022).