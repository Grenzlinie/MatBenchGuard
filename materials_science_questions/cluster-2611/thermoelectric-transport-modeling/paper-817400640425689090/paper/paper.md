# Ab initio thermoelectric calculations of ring-shaped bands in two-dimensional $Bi_2Te_3$, $Bi_2Se_3$, and $Sb_2Te_3$: Comparison of scattering approximations

Cameron Rudderham and Jesse Maassen

Department of Physics and Atmospheric Science, Dalhousie University, Halifax, Nova Scotia, Canada B3H 4R2

![](./images/817400640425689090_1.jpg)
(Received 14 September 2020; revised 23 February 2021; accepted 25 March 2021; published 9 April 2021)

Materials with ring-shaped electronic bands are promising thermoelectric (TE) candidates since their unusual dispersion shape is predicted to give large power factors. In this paper, we use density functional theory to investigate single and double quintuple-layer $Bi_2Te_3$, $Bi_2Se_3$, and $Sb_2Te_3$ and to compare the TE properties using three scattering approximations: constant relaxation time, constant mean free path, and scattering rates proportional to the density of states (the so-called DOS model). Focus is placed on elucidating how these particular dispersion shapes influence the TE characteristics and on understanding how each scattering model impacts TE transport. The single quintuple-layer materials possess two ring-shaped valence-band maxima that provide an abrupt increase in conducting channels, which benefits the power factor. Below the band edge a ring-shaped minimum is found to further enhance TE performance within the DOS model due to a sharp drop in the DOS and, thus, scattering. An analytic "octic" dispersion model, designed to capture the observed characteristics of the band structure, is introduced and shown to qualitatively reproduce the first-principles results. The double quintuple-layer materials display notably worse TE properties since their dispersions are significantly modified compared to the single quintuple-layer case and lose much of the ring-shaped character. Our analysis shows that the benefits of ring-shaped bands are sensitive to the alignment of the two ring maxima and to the degree of ring anisotropy. Moreover, the predicted TE performance can vary significantly depending on the choice of scattering approximation, which could benefit from further study to assess the accuracy of these simple scattering models.

DOI: 10.1103/PhysRevB.103.165406

## I. INTRODUCTION

Thermoelectric (TE) materials can convert thermal energy into useful electrical power and, thus, have the potential to re- cuperate the large untapped global energy source that is waste heat [1]. A major goal is to improve the thermoelectric conver- sion efficiency, which is characterized by its figure of merit [2]
$$ZT = S^2\sigma T/(\kappa_e + \kappa_l),$$
where $S$ is the Seebeck coefficient, $\sigma$ is the electrical conductivity, $T$ is the temperature, and $\kappa_{e/l}$ is the electronic/lattice thermal conductivity. In the quest to achieve higher efficiencies, or $ZT$, there are two broad strate- gies based on lowering the lattice thermal conductivity and increasing the power factor (PF), $PF = S^2\sigma$. The former has led to high $ZT$ in many cases, for example, using nanostruc- turing [3-5] or highly anharmonic materials [6-9] to increase phonon scattering and reduce $\kappa_l$. Approaches for improved PF include (among others) distorted electronic states [10,11], band convergence [12-14], low electron-phonon (el-ph) cou- pling materials [15-19], energy filtering [20-24], modulation doping [25-27], and unusually shaped electron dispersions.

Focusing on this last strategy, the idea is to identify or design materials with unique electronic band structures that benefit the power factor, compared to typical effective mass/parabolic dispersions common in semiconductors. Proposed band structures for high PF include, for example, nonparabolic bands [28], "pudding-mold" band [29-31], "camel-back" dispersion [32], semimetals [33,34], topologically protected states [35,36], and ring-shaped bands [37-42]-these dispersions have properties that help circumvent the $\sigma$ versus $S$ trade-off [2] that limits the power factor. Similar improvements have also been proposed in lower-dimensional materials, even those with effective mass bands [43-45]. Focusing specifically on ring-shaped bands (also referred to as "Mexican hat" or "warped" bands), the key characteristic from this unusual dispersion is a finite number of states at the band edge (in the shape of a ring) that results in an abrupt increase in the distribution of modes. This feature allows for simultaneously larger $S$ and $\sigma$, compared to a parabolic band [42]. Ring-shaped bands are often displayed in two-dimensional few-layer materials, such as [39]: GaSe, GaS, InSe, InS, $Bi_2Te_3$, $Bi_2Se_3$, bilayer graphene under an applied electric field, and elemental Bi.

Most theoretical studies on ring-shaped bands were carried out using density functional theory (DFT) to obtain detailed and accurate descriptions of the electronic states but often relyon simple and approximate scattering models [37,39-42,46]; the two most common assume either a constant scattering time or constant mean free path (MFP). Rigorous DFT-based electron-phonon calculations have shown that the scattering rates are often better approximated by the electron density of states (DOS) [47-52] compared to either a constant scattering time or MFP [51]. A recent study, based on analytical band models, showed that the TE properties can depend sensitively

*jmaassen@dal.ca

on the details of the scattering approach and that, in particular, the DOS-scattering model (wherein the scattering rates are assumed to be proportional to the DOS) predicted signifi- cantly better performance for ring-shaped bands compared to assuming a constant relaxation time or MFP [42].

Motivated by these recent findings, this paper focuses on investigating the TE properties of selected materials with ring-shaped bands using DFT and understanding the differ- ences that arise among the three aforementioned scattering models—with an emphasis on the DOS-scattering model, which has not to our knowledge previously been used with ring-shaped bands. The materials investigated in this paper are two-dimensional $Bi_2Te_3$, $Bi_2Se_3$, and $Sb_2Te_3$, in single (1QL) and double quintuple-layer (2QL) form, which possess warped dispersions originating from spin-orbit coupling. The paper is outlined as follows. Section II introduces the theo- retical approach and computational details. The results and accompanying discussions are presented in Sec. III. Finally, our findings are summarized in Sec. IV.

## II. THEORETICAL AND COMPUTATIONAL APPROACH

### A. Transport formalism

Within the linear-transport regime, the electrical conductiv- ity, Seebeck coefficient, and electronic thermal conductivity are defined as [53]
$$
\sigma=\left(\frac{2 q^{2}}{h}\right) I_{0},\qquad(1)
$$

$$
S=-\left(\frac{k_{B}}{q}\right) \frac{I_{1}}{I_{0}},\qquad(2)
$$

$$
\kappa_{e}=\frac{2 k_{B}^{2} T}{h}\left(I_{2}-\frac{I_{1}^{2}}{I_{0}}\right),\qquad(3)
$$
with the quantity $I_j$ written as
$$
I_{j}=\frac{h}{2} \int_{-\infty}^{\infty} \Sigma(E)\left(\frac{E-\mu}{k_{B} T}\right)^{j}\left[-\frac{\partial f_{0}}{\partial E}\right] d E,\qquad(4)
$$
where $\Sigma(E)$ is the transport distribution, $\mu$ is the Fermi level, and $f_0$ is the Fermi-Dirac distribution. $\Sigma(E)$ is the central quantity as it contains all material properties and is expressed as [53–55]
$$
\Sigma(E)=\frac{1}{\Omega} \sum_{k, s, n} v_{x}^{2}(k) \tau(k) \delta[E-\epsilon(k)],\qquad(5)
$$
where $\Omega$ is the sample volume, $\epsilon(k)$ is the electronic dis persion (i.e., band structure), $\tau(k)$ is the scattering time, and $v_{x}=(1/\hbar)(\partial\epsilon/\partial k_{x})$ is the group velocity along the direction of transport (here assumed to be the $\hat{x}$ direction). The sum is performed over band index $n$, spin state $s$, and all $k$ states in the Brillouin zone [note that the explicit $s$ and $n$ dependence of the quantities in Eq. (5) are omitted for clarity].

The TE parameters of a given material depend solely on its transport distribution and, thus, it is a useful function to analyze. As previously discussed [42], two of the desired features for $\Sigma(E)$ include a large overall magnitude (i.e., scaling factor) and a highly asymmetry distribution relative to the Fermi level. The former provides a large electrical conductivity, and the latter results in a large (absolute value) Seebeck coefficient. Using these guidelines, one can easily identify which transport distributions are beneficial for TE transport.

Despite its utility, the transport distribution can be difficult to interpret physically. Turning to the Landauer formalism, we find that $\Sigma(E)$ can be written as the product of two physically intuitive quantities [42,53,56],
$$
\Sigma(E)=\frac{2}{h} M(E) \lambda(E).\qquad(6)
$$

The first quantity $M(E)$ is known as the distribution of modes (DOM), and is defined as [53]
$$
M(E)=\frac{h}{4 \Omega} \sum_{k, s, n}\left|v_{x}(k)\right|, \delta[E-\epsilon(k)].\qquad(7)
$$

$M(E)$ can be interpreted physically as the number of “chan- nels” available for transport with each channel (or mode) contributing one quantum of conductance $2q^2/h$. Equation (7) counts the number of modes (an integer) per cross-sectional area, which varies with dimensionality—the units are $\mathrm{m}^{-2}$ in three dimensions (3D), $\mathrm{m}^{-1}$ in two dimensions (2D), and unitless in one dimension (1D) [all cases in this paper are in 2D]. The second quantity appearing in Eq. (6) is $\lambda(E)$ the mean free path for backscattering [53],
$$
\lambda(E)=2 \frac{\sum_{k, s, n} v_{x}^{2}(k) \tau(k) \delta[E-\epsilon(k)]}{\sum_{k, s, n}\left|v_{x}(k)\right| \delta[E-\epsilon(k)]}.\qquad(8)
$$

$\lambda(E)$ is defined as the average distance along the transport direction that an electron with energy $E$ will travel before scattering changes the sign of its $v_x$ component.

When the relaxation time $\tau(k)$ is only a function of energy (as considered in this paper), i.e., $\tau(k)=\tau[\epsilon(k)]=\tau(E)$, the mean free path for backscattering can be expressed as $\lambda(E)=V_{\lambda}(E)\tau(E)$ [42]. $V_{\lambda}(E)$ is defined as
$$
V_{\lambda}(E)=2 \frac{\sum_{k, s, n} v_{x}^{2}(k) \delta[E-\epsilon(k)]}{\sum_{k, s, n}\left|v_{x}(k)\right| \delta[E-\epsilon(k)]},\qquad(9)
$$
and can be interpreted as an average velocity of carriers with energy $E$ along the transport direction. In this case, the trans- port distribution takes on the following form:
$$
\Sigma(E)=\frac{2}{h} M(E) V_{\lambda}(E) \tau(E),\qquad(10)
$$
which has a physically transparent interpretation. $\Sigma(E)$ is determined by the number of channels available for transport $M(E)$, the average carrier velocity $V_{\lambda}(E)$, and the average time between scattering events $\tau(E)$.

Both $M(E)$ and $V_{\lambda}(E)$ are calculated directly from a material’s band structure. The carrier relaxation time $\tau(E)$, however, depends on the particular scattering physics. Rig- orous and accurate scattering calculations of electron-phonon and electron-impurity collision processes, for example, based on DFT, are possible but fairly computationally inten- sive [19,49,51,52,57–60]. As a result, simple scattering

approximations are often adopted. In this paper, we compare the results of three scattering models, based on an assumption of a constant mean free path, constant relaxation time, and scattering rates proportional to the DOS.

With a constant MFP $\lambda_0$, the transport distribution takes the following simple form:
$$
\Sigma_{\mathrm{cmfp}}(E)=\frac{2}{h} M(E) \lambda_{0}, \tag{11}
$$
where $\lambda_0$ is an adjustable parameter. We will refer to this scat- tering approach as the constant MFP (cmfp) approximation. A constant MFP is physically expected in the case of a 3D parabolic band with acoustic deformation potential scatter- ing [61] in which case the scattering rate is proportional to $\sqrt{E}$. With a constant scattering time $\tau_0$, the transport distribu- tion is written as
$$
\Sigma_{\mathrm{crt}}(E)=\frac{2}{h} M(E) V_{\lambda}(E) \tau_{0}, \tag{12}
$$
where $\tau_0$ is an adjustable parameter. This scattering model will be referred to as the constant relaxation time (crt) ap- proximation. A constant relaxation time (or rate) can be justified physically in the case of a 2D parabolic band with acoustic deformation potential scattering [61] in which case the MFP is proportional to $\sqrt{E}$. Both cmfp and crt approximations are reasonable as long as the MFPs and re- laxation times are roughly constant within the energy range ($\sim$$10k_BT$) where transport occurs. Although both these simple approximations have a connection to physical scattering due to their simplicity and convenience they are more broadly adopted, including cases in which their validity may be questionable.

Lastly, assuming the scattering rates are proportional to the DOS, the transport distribution is expressed as
$$
\Sigma_{\mathrm{DOS}}(E)=\frac{2}{h} M(E) V_{\lambda}(E) \frac{K_{0}}{D(E)}, \tag{13}
$$
where $K_0$ is an adjustable parameter. (Note that here we choose to place $K_0$ in the numerator, whereas in some pre- vious studies it appears in the denominator [42,48,50].) This approximation will be referred to as the DOS model. $K_0$ is inversely related to the deformation potential squared [61], which has been shown to be an important material descriptor for thermoelectrics [62]. Recent first-principles el-ph cal- culations have shown that the rigorous scattering rates are well described by the DOS-scattering approximation [47–52]. Physically, electron scattering is expected to scale with the number of available final states and should follow the DOS when the coupling matrix is roughly constant. This is a decent approximation for nonpolar el-ph scattering as well as for polar el-ph and electron-impurity scattering in highly doped semiconductors in which screening effects are significant [51,61]. It is worth mentioning that the two physical examples described above for the cmfp and crt ap- proximations are, in fact, specific cases of DOS scattering. The concept of scattering rates following the electron DOS is not new and goes back to earlier work [63–65] and has been adopted in a number of studies [66–69].

In this paper, we compare the transport properties aris- ing from the three scattering models with an emphasis on the DOS-scattering approximation, which has not previously been used to analyze these materials. We note, however, that there are limited studies of scattering in ring-shaped two-dimensional materials [70], thus, further investigation is needed to confirm the validity of the DOS model for this material class.

### B. Numerical details

All DFT calculations were performed with the QUANTUM ESPRESSO package [71,72], using the projector augmented- wave method [73], the Perdew-Burke-Ernzerhof functional of the generalized gradient approximation [74], and fixed occupations. Spin-orbit interaction was included as well as Grimme-D2 van der Waals corrections [75]. A plane-wave cutoff energy of 110 Ry and a Monkhorst-Pack [76] generated $k$ mesh of $11 \times 11 \times 1$ were adopted for all systems studied. A vacuum layer of $15$ Å along the $\hat{z}$ direction was included to prevent interactions between neighboring cells. The ex- perimental lattice constants were used as has been adopted previously [38,77,78], corresponding to an in-plane hexago- nal lattice constant of $a=4.383$ Å for $\mathrm{Bi_2Te_3}$, $4.138$ Å for $\mathrm{Bi_2Se_3}$, and $4.264$ Å for $\mathrm{Sb_2Te_3}$ [79–81]. The atomic coor- dinates were relaxed until the forces on the atoms were less than $0.01$ eV/Å. In this paper, we focus on single and double quintuple-layer $\mathrm{Bi_2Te_3}$, $\mathrm{Bi_2Se_3}$, and $\mathrm{Sb_2Te_3}$—each quintuple layer is five-atoms thick and contains strong intra-atomic bonds, and the different QLs are held together via weak van der Waals interaction. The primitive cell of these two- dimensional materials is hexagonal with each QL containing five atoms: two equivalent Bi or Sb sites, two equivalent Te or Se sites (at the top/bottom surface of each QL), and a third inequivalent Te or Se site (at the center of each QL).

The non-self-consistent DOS calculations were performed using the tetrahedron method [82] on a uniform $51 \times 51 \times 1$ $k$ grid. $M(E)$ and $V_{\lambda}(E)$ are computed using the “band count- ing” method [53,83], which requires the eigenenergies on a uniform $k$ grid with a rectangular Brillouin zone. In this case, the electron energies for a rectangular supercell of size $a \times \sqrt{3}a \times 1$ (with double the area of the primitive cell) were calculated with $115 \times 85 \times 1$ $k$ points.

The scissor operator was used to adjust the DFT-calculated band gaps to those obtained from the more accurate GW method [84,85]—see Table I. All dispersion-related results,

<table>
<caption>TABLE I. DFT and GW band gaps of single and double QL materials: $\mathrm{Bi_2Te_3}$, $\mathrm{Bi_2Se_3}$, and $\mathrm{Sb_2Te_3}$. The GW band gaps are taken from Refs. [84,85].</caption>
<thead>
  <tr>
    <th></th>
    <th>$\mathrm{Bi_2Te_3}$ (1QL)</th>
    <th>$\mathrm{Bi_2Se_3}$ (1QL)</th>
    <th>$\mathrm{Sb_2Te_3}$ (1QL)</th>
    <th>$\mathrm{Bi_2Te_3}$ (2QL)</th>
    <th>$\mathrm{Bi_2Se_3}$ (2QL)</th>
    <th>$\mathrm{Sb_2Te_3}$ (2QL)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>DFT band gap (eV)</td>
    <td>0.23</td>
    <td>0.45</td>
    <td>0.46</td>
    <td>0.046</td>
    <td>0.09</td>
    <td>0.16</td>
  </tr>
  <tr>
    <td>GW band gap (eV)</td>
    <td>0.64</td>
    <td>0.90</td>
    <td>0.82</td>
    <td>0.06</td>
    <td>0.24</td>
    <td>0.25</td>
  </tr>
</tbody>
</table>

![](./images/817400640425689090_2.jpg)

FIG. 1. Single quintuple-layer ${\rm Bi_2Te_3}$. (a) Electron dispersion along high-symmetry points. (b) Energy contour plot of the valence band. (c) Distribution of modes $M(E)$, (d) average velocity $V_\lambda(E)$, and (e) density of states $D(E)$ versus energy for the valence states. Shaded regions indicate the energies of the rings and the moat feature.

including $\epsilon(k)$, $M(E)$, $V_\lambda(E)$, and $D(E)$, correspond to the unadjusted DFT band gaps, whereas the GW band gaps are adopted for the TE transport calculations (to correct for bipolar effects). When evaluating $ZT$, for all the materials considered, we used a lattice thermal conductivity of 1.5 W/m-K obtained from first-principles phonon transport calculations of single QL ${\rm Bi_2Te_3}$ [86]. This requires converting our TE parameters from 2D units to 3D units using the

![](./images/817400640425689090_3.jpg)

FIG. 2. Analytic octic band model. (a) Electron dispersion $\epsilon(k)$ versus $k$. (b) Distribution of modes $M(E)$, (c) average velocity, $V_\lambda(E)$, and (d) density of states $D(E)$ versus energy relative to the valence-band edge. To illustrate the shape of the distributions, we used $\epsilon_0, =$ 0.15 eV, $k_a=2$, and $k_b=1$, which gives a moat energy of $-48$ meV.

![](./images/817400640425689090_4.jpg)

FIG. 3. Single quintuple-layer $\text{Bi}_2\text{Te}_3$. (a) Transport distribution $\Sigma(E)$ of the valence states versus energy. (b) PF and (c) figure-of-merit $ZT$ versus the Fermi level relative to the valence-band edge. Comparison of cmfp-, crt-, and DOS-scattering approximations. $T = 300$ K.

following films thickness values: $7.61$ Å (1QL) and $17.91$ Å (2QL) for $\text{Bi}_2\text{Te}_3$, $7.04$ Å (1QL) and $16.60$ Å (2QL) for $\text{Bi}_2\text{Se}_3$, $7.47$ Å (1QL) and $17.70$ Å (2QL) for $\text{Sb}_2\text{Te}_3$. We set the scattering constants (i.e., $\lambda_0$, $\tau_0$, and $K_0$) for the valence and conduction states separately such that the average MFP for backscattering is equal to 20 nm when the Fermi level is located at either the valence- $(E_v)$ or the conduction- $(E_c)$ band edges (see the Supplemental Material [87] for details on the definition of average MFP for backscattering and how the scattering parameters are determined). This choice was motivated by the fact that most TEs provide optimal performance when the Fermi level is aligned near the band edges [88,89]. This constraint connects the various scattering parameters (one cannot be arbitrarily modified relative to the others) and allows us to make reasonable comparisons among the scattering models. We note, however, that this choice is not unique and other constraints could alter the calculated TE properties. All calculations were performed for $T = 300$ K.

## III. THERMOELECTRIC PROPERTIES

We start by analyzing the thermoelectric properties for each of the materials ($\text{Bi}_2\text{Te}_3$, $\text{Bi}_2\text{Se}_3$, and $\text{Sb}_2\text{Te}_3$) in single QL form then present the results in the case of double QL.

### A. Single quintuple-layer $\text{Bi}_2\text{Te}_3$

The band structure for 1QL $\text{Bi}_2\text{Te}_3$ is shown in Fig. 1(a). The most significant feature is the presence of not one but two ringlike features at the valence-band edge. From the band structure, this simply looks like two valence-band maxima along both $\Gamma \to M$ and $\Gamma \to K$. However, from the contour plot of the valence band presented in Fig. 1(b), we see that the band edges do not correspond to points, but rather have a ringlike shape; specifically a smaller radius (inner) ring and a larger radius (outer) ring. Since this unusual feature in the band structure is the main focus of this paper, combined with the fact that our results show that the TE performance of the warped valence states always surpasses those of the more "regular" conduction states, our analysis will focus on the transport properties of the valence states.

The resulting electronic properties, including $M(E)$, $V_\lambda(E)$, and $D(E)$, are shown Figs. 1(c)-1(e). The ringlike features result in abrupt increases in DOM and DOS near the band edge. Although typical electron dispersions, such as the parabolic or the Kane models (e.g., the conduction band of 1QL $\text{Bi}_2\text{Te}_3$), possess a vanishing number of states near the band edge, the valence band of 1QL $\text{Bi}_2\text{Te}_3$ has a large finite number of states within a few meV of the band gap. This gives a sharp steplike feature in the DOM and a spike in the DOS. The large number of states provided by these ringlike features, originating from spin-orbit coupling, is the main reason why these QL materials are promising as high power factor ($\text{PF} = S^2\sigma$) thermoelectrics [37-40]. $V_\lambda(E)$ by comparison increases smoothly as we move away from the band edge. This happens because $V_\lambda(E)$ corresponds to an *average* velocity over a constant energy surface [as opposed to a sum, such as in the case of $M(E)$ or $D(E)$] and because the states near the band edge have small velocities.

Previously, a 2D analytic dispersion model containing a single ringlike band, known as the quartic or Mexican-hat model, was used to analyze and explore the impact on the TE properties (see Refs. [39,42,90] for details). The features in $M(E)$, $V_\lambda(E)$, and $D(E)$, discussed above, are all in rough agreement with the quartic model near the band edge. However, slightly away from the band edge, we observe abrupt *decreases* in $M(E)$ and $D(E)$ near 0.05 eV below $E_v$ and a smaller abrupt *increase* in $V_\lambda(E)$. Although the quartic model does predict a discontinuous decrease in $D(E)$ at an energy below the band edge, it predicts that $M(E)$ and $V_\lambda(E)$ are continuous and so cannot explain the observed characteristics. To gain further insight into the origin of these features, we examine the contour plot in Fig. 1(b).

The presence of the two aforementioned ringlike local maxima at the band edge necessarily requires the existence of a single ringlike local *minimum* nestled between them; a feature observed in Fig. 1(b), which we will refer to as the "moat feature" (in light of its topographic resemblance to a moat). The bottom of the moat lies at the same energy

![](./images/817400640425689090_5.jpg)

FIG. 4. Single quintuple-layer $\mathrm{Bi_2Se_3}$. (a) Electron dispersion along high-symmetry points. (b) Energy contour plot of the valence band. (c) Distribution of modes $M(E)$, (d) average velocity $V_\lambda(E)$, and (e) density of states $D(E)$ versus energy for the valence states. Shaded regions indicate the energies of the rings and the moat feature.

as the observed discontinuities in $M(E)$, $V_\lambda(E)$, and $D(E)$, suggesting they originate from the disappearance of states below $-0.05$ eV. The near-circular nature of the moat indicates that this particular constant energy line is nearly isotropic.

Although the aforementioned quartic band model can describe the impact of ringlike local maxima at the band edge, it does not capture the effect of a ringlike local minima at energies below the band edge. To investigate what effect such a moat feature would have, we introduce a new analytic dispersion model that we refer to as the "octic model" (it is an eighth-order polynomial in $k$),

$$
\epsilon(k)=-\frac{\epsilon_0}{\left(k_a k_b\right)^4}\left(k^2-k_a^2\right)^2\left(k^2-k_b^2\right)^2. \tag{14}
$$

The octic model possesses three ring-shaped critical lines (two maxima and one local minimum) and a single critical point at $k=0$, which are illustrated in Fig. 2(a). The parameters $k_a$ and $k_b$ correspond to the radii of the critical lines at the band edge $[\epsilon(k)=0]$, i.e., the inner and outer ring radii. The constant $\epsilon_0$ determines the energy at the $\Gamma$ point: $\epsilon(k=0)=-\epsilon_0$. From the three parameters $\epsilon_0$, $k_a$, and $k_b$, the bottom of the moat has an energy of $-\epsilon_0(k_a^2-k_b^2)^4/(16k_a^4k_b^4)$. For comparison, the quartic model captures a single ring-shaped maximum and a minimum at $k=0$.

The resulting $M(E)$, $V_\lambda(E)$, and $D(E)$ distributions for the octic model are plotted in Figs. 2(b)-2(d) with the analytic expressions provided in the Appendix and in the Supplemental Material [87]. The presence of ring-shaped critical surfaces at the band edge results in a $M(E)$ distribution that turns on, such as a step function, just like in the case of the quartic model. This discontinuity is, of course, sharper than the corresponding feature in the case of 1QL $\mathrm{Bi_2Te_3}$ since the DFT dispersion shows some small amount of anisotropy resulting in the energy of a ring being spread over a couple meV. In our discussion we will refer to abrupt features, arising from both the analytic model and the DFT-computed results as being discontinuous, even though only the former is technically discontinuous.

The octic model also contains a second discontinuity in $M(E)$ at the location of the moat in the form of a steplike decrease. This occurs because a large number of transport channels, provided by the moat feature, abruptly vanishes. Again, this discontinuity is also observed in 1QL $\mathrm{Bi_2Te_3}$. Since these states have small velocities near the bottom of the moat, $V_\lambda(E)$ discontinuously increases below the moat since the average no longer includes a large number of zero-velocity states. A singularity in the DOS occurs at the moat energy for the same reason as the observed singularity at the band edge; any constant energy containing a continuum of critical points will cause the DOS to diverge (for 2D materials). Overall, the features in $M(E)$, $V_\lambda(E)$, and $D(E)$ obtained from DFT are found to have a strong resemblance with those from the octic model—confirming that the two ring-shaped maxima in

![](./images/817400640425689090_6.jpg)

FIG. 5. Single quintuple-layer $\text{Bi}_2\text{Se}_3$. (a) Transport distribution $\Sigma(E)$ of the valence states versus energy. (b) PF and (c) figure-of-merit $ZT$ versus Fermi level relative to the valence-band edge. Comparison of cmfp-, crt-, and DOS-scattering approximations. $T =$ 300 K.

addition to the ring-shaped minimum are key to understanding the observed transport properties.

Next, we examine the transport distribution of 1QL $\text{Bi}_2\text{Te}_3$ for each scattering approximation (cmfp, crt, and DOS), which are shown in Fig. 3(a). First, we note that $\Sigma(E)$ for each scattering model is qualitatively different at the energy of the moat ($-0.05$ eV). In the case of a constant MFP, the transport distribution is simply proportional to $M(E)$ and, hence, decreases abruptly just below the moat energy. With the crt, the transport distribution is proportional to the product of $M(E)$ and $V_\lambda(E)$; the latter of which steps abruptly upwards once the moat states disappear. The resulting transport distribution still steps downwards at the moat energy but less than in the constant MFP case.

Lastly, with the DOS model, the transport distribution steps abruptly upwards below the moat due to the discontinuity in the $D(E)$ distribution. This results in the DOS model having the largest magnitude in transport distribution, compared to the cmfp and crt, over most of the relevant energy range (several $k_BT$ around the Fermi level), coupled with a sharp rise with increasing hole energy. Consequently, among the different scattering approximations, the DOS model predicts the largest power factor and $ZT$ for 1QL $\text{Bi}_2\text{Te}_3$. This improved PF is mainly due to a higher Seebeck coefficient from the sharp rise in $\Sigma_{\text{DOS}}(E)$, which is independent of the scattering parameter value ($\sigma$ and $S$ for the 1QL materials are presented in the Supplemental Material [87]). This shows that the presence of a moatlike feature can produce an abrupt decrease in $D(E)$ and increase in $V_\lambda(E)$ both of which are desirable for thermoelectric performance. As such, single QL $\text{Bi}_2\text{Te}_3$ may be a better thermoelectric than previously predicted using the cmfp and crt approximations.

A similar result was previously shown with the quartic model in which an abrupt decrease in DOS (and, hence, scattering) provided improved power factor when comparing the DOS model to the cmfp and crt [42]. One difference between the quartic and the octic band models is that the decrease in DOS originates from the removal of paraboliclike states and ringlike states, respectively. As a result, only the octic model presents discontinuities in $M(E)$ and $V_\lambda(E)$ below the band edge; these sharper features may be more resilient to small deviations from isotropicity that spread the critical points of the ring over a small energy range [as seen in Fig. 1(b)].

### B. Single quintuple-layer $\text{Bi}_2\text{Se}_3$

Next, we analyze the thermoelectric performance of single QL $\text{Bi}_2\text{Se}_3$. The electronic structure of this material is shown in Fig. 4(a). We observe that the valence band possesses two ringlike features at the band edge, analogous to 1QL $\text{Bi}_2\text{Te}_3$. As before, this results in a rapid increase in $M(E)$ near the band edge. For this case, however, there are two noticeable steps in the DOM. This occurs because both rings are slightly misaligned in energy—the inner ring is roughly 0.03 eV below the outer ring as seen in Fig. 4(b). This also gives a peak in $D(E)$ at the inner and outer ring energies.

Unlike with 1QL $\text{Bi}_2\text{Te}_3$, however, there are no abrupt features in $M(E)$ and $V_\lambda(E)$ due to the presence of a moat feature. To help understand why, we examine the energy contour plot in Fig. 4(b). We observe a moat feature that is highly anisotropic, varying in energy between roughly $-0.12$ and $-0.07$ eV as indicated by the presence of multiple shallow-energy valleys. This anisotropy results in a “smearing out” of the sharp features that would have resulted from a more isotropic moat feature as the abrupt disappearance of a large constant energy surface now happens gradually over an energy range of non-negligible width.

The resulting transport distributions and thermoelectric properties are shown in Fig. 5. There is a distinct lack of sharp features in any of the transport distributions, compared to 1QL $\text{Bi}_2\text{Te}_3$ as a consequence of the aforementioned anisotropy in the moat feature in addition to the misalignment in energy of the inner and outer rings. Nevertheless, the DOS-model transport distribution displays the largest values and slope over a significant portion of the relevant energy range near the moat feature (around $-0.1$ eV), which yields the highest PF among the scattering models. This suggests that 1QL $\text{Bi}_2\text{Se}_3$ may also be a better thermoelectric than previously reported. We note, however, that the relative improvement is not as significant as with 1QL $\text{Bi}_2\text{Te}_3$, indicating that the TE characteristics are

![](./images/817400640425689090_7.jpg)

sensitive to the degree of anisotropy of the rings/moat and their relative alignment in energy.

The $\Sigma_{\text{DOS}}(E)$ for 1QL $\text{Bi}_2\text{Te}_3$ benefits from abrupt increases, which help increase its Seebeck coefficient, however, 1QL $\text{Bi}_2\text{Se}_3$ shows larger PF and $ZT$. This happens because the transport distribution of 1QL $\text{Bi}_2\text{Se}_3$, while relatively smooth, has an overall larger magnitude resulting in higher conductivity.

### C. Single quintuple-layer $\text{Sb}_2\text{Te}_3$

The third and final single QL material investigated is $\text{Sb}_2\text{Te}_3$. Its electronic structure properties are presented in Fig. 6. Similar to the previous two 1QL systems, there are two ringlike features near the valence-band edge, however, the $M(E)$, $V_\lambda(E)$, and $D(E)$ distributions display sharp features not shared with the other cases. Namely, we observe large increases in the DOM and DOS roughly 0.03 eV below the band edge, accompanied with a sharp decrease in $V_\lambda(E)$. To understand the origin of these features, we examine the energy contour plot presented in Fig. 6(b).

As with 1QL $\text{Bi}_2\text{Se}_3$, the inner and outer rings of 1QL $\text{Sb}_2\text{Te}_3$ are slightly misaligned in energy by roughly 0.03 eV. However, the resulting effect on the electronic distributions is somewhat stronger in this case because the inner ring turns on before the outer ring (i.e., the outer ring has lower energy). The outer ring tends to have a stronger effect since its larger radius includes more states compared to the inner ring. The sudden contribution from the outer ring at $-0.03$ eV causes the abrupt increases in $M(E)$ and $D(E)$, which are somewhat washed out due to the anisotropy of the outer ring. Because the states near the top of the outer ring have very small velocities, $V_\lambda(E)$ is dragged down. All these features are similar to 1QL $\text{Bi}_2\text{Se}_3$ but are more pronounced in this case.

The effect of this lower-energy outer ring is exactly opposite to that of the moat feature in 1QL $\text{Bi}_2\text{Te}_3$. In the latter case, the abrupt turn *off* of a ring-like dispersion feature caused sharp decreases in $M(E)$ and $D(E)$ and a sharp increase in $V_\lambda(E)$, whereas in this case the abrupt turn *on* of a ringlike feature has the opposite effect. Since the moat feature in 1QL $\text{Bi}_2\text{Te}_3$ was shown to benefit TE performance (within the DOS-scattering model), we anticipate the misaligned outer ring in 1QL $\text{Sb}_2\text{Te}_3$ may have a detrimental effect. The resulting transport distributions and their corresponding thermoelectric properties are shown in Fig. 7.

Although $\Sigma_{\text{DOS}}(E)$ takes on the largest values near the band edge, the increased scattering and decreased velocity that arise from the outer ring at $-0.03$ eV causes the transport distribution to abruptly step down. As a result, it takes on the smallest value of the three transport distributions over a significant portion of the relevant energy range. Moreover, having a segment of the transport distribution decrease with increasing hole energy negatively impacts the Seebeck coefficient. Examining the PF and $ZT$ distributions, we observe that the DOS-scattering case predicts the worst performance for the reasons outlined above.

![](./images/817400640425689090_8.jpg)

FIG. 7. Single quintuple-layer Sb₂Te₃. (a) Transport distribution Σ(E) of the valence states versus energy. (b) PF and (c) figure-of-merit ZT versus Fermi level relative to the valence-band edge. Comparison of cmfp-, crt-, and DOS-scattering approximations. T = 300 K.

From our findings on the single quintuple-layer materials, we conclude that the ring-shaped bands in addition to the moat feature can benefit TE performance. This mainly comes from abrupt increases in M(E) from the rings at the band edge, coupled with an abrupt decrease in D(E) from the moat feature (which decreases the scattering rates with the DOS model). We also found that these benefits can be sensitive to the relative alignment of the inner and outer rings, and to the degree of anisotropy of the rings/moat that smooths out the desired sharp features. When comparing the scattering models we observe larger changes in PF than in ZT. This occurs because: (i) the changes in PF are smaller when the Fermi level is aligned near the peak in ZT (compared to the variations in maximum PF), and (ii) increases in PF are partially canceled by an accompanying increase in κₑ (our results show that κₑ ≈ κᵢ near the optimum ZT).

Lastly, with 1QL Bi₂Te₃ and 1QL Bi₂Se₃ the DOS-scattering model predicts a peak in PF for a slightly lower Fermi level compared to the other scattering models. This happens because the Seebeck coefficient is larger (see the Supplemental Material [87]) due to the decrease in DOS from the moat feature, which allows the PF to continue increasing slightly as the Fermi level moves deeper before rolling over. With 1QL Sb₂Te₃ as mentioned above, the DOS-scattering model yields the smallest Seebeck coefficient, which results in a PF peak located just above the valence-band edge in the band gap. In all cases, the PF maxima from the different scattering approximations are within a factor of 3 in hole concentration.

### D. Double quintuple-layer Bi₂Te₃, Bi₂Se₃, and Sb₂Te₃

Next, we analyze the thermoelectric properties of Bi₂Te₃, Bi₂Se₃, and Sb₂Te₃ in double quintuple-layer form. The 2QL materials are composed of two stacked 1QL layers held together via van der Waals interaction. Although the interlayer coupling is relatively weak, as we will show this has a significant effect on the electronic and thermoelectric characteristics.

Figure 8 presents the electron dispersions and energy contour plots for all three 2QL materials. First, we note that all three band gaps are significantly smaller than in the 1QL case. This typically has a negative effect on thermoelectric performance as it increases bipolar effects. Perhaps more importantly, we observe a dramatic change in the band structure near the valence-band edge. Although the 1QL materials display two ring-shaped maxima, in the 2QL systems one of the rings is pushed away from the band edge and loses most of its ringlike character. Both 2QL Bi₂Se₃ and Sb₂Te₃ show a small radius ring at the band edge with lower-energy states near −0.1 eV showing a "starfish" like shape with six "arms" stretching out from the zone center. However, the trend is reversed with 2QL Bi₂Te₃, which presents a star-shaped dispersion near the band edge with a large radius ring near −0.15 eV.

The distribution of modes M(E), average velocity V_λ(E), and density of states D(E) for the 2QL materials are shown in Figs. 9(a)-9(c). Similar to the 1QL case, all three 2QL materials display an abrupt increase in M(E) and D(E) at the band edge. However, in this case the magnitudes of these discontinuities are not nearly as large as those of their 1QL counterparts. This is particularly evident with 2QL Bi₂Se₃ and Sb₂Te₃ due to their rings having small radii and, thus, containing fewer states. The starfish-shaped band of 2QL Bi₂Te₃ includes many states within a small energy range and results in an appreciable increase in M(E) (although roughly half the value of 1QL Bi₂Te₃).

After their small but abrupt initial rise, the M(E) and D(E) distributions of 2QL Bi₂Se₃ and Sb₂Te₃ remain roughly constant until approximately −0.1 eV at which point we observe sharp increases due to the starfish feature that contributes many states. With 2QL Bi₂Te₃, however, M(E) and D(E) remain mostly constant throughout the relevant energy range for transport. V_λ(E) increases gradually from the band edge, then eventually drops with the presence of a local maxima (e.g., the starfish feature at roughly −0.1 eV in 2QL Bi₂Se₃ and Sb₂Te₃). As mentioned earlier, such features contribute a large number of low-velocity states that drag down V_λ(E).

![](./images/817400640425689090_9.jpg)

FIG. 8. Double quintuple-layer Bi₂Te₃, Bi₂Se₃, and Sb₂Te₃. (a)-(c) Electron dispersion along high-symmetry points. (d)-(f) Energy contour plot of the valence band.

Next, we analyze the thermoelectric properties presented in Figs. 9(d)-9(f). Note that we focus here on the results of the DOS-scattering model, which is believed to be the most physical and accurate (a comparison of all three scattering models for the 2QL materials is provided in the Supplemental Material [87]). The transport distributions for 2QL Bi₂Se₃ and

![](./images/817400640425689090_10.jpg)

FIG. 9. Double quintuple-layer Bi₂Te₃, Bi₂Se₃, and Sb₂Te₃. (a) Distribution of modes $M(E)$, (b) average velocity $V_\lambda(E)$, and (c) density of states $D(E)$ versus energy for the valence states. (d) Transport distribution $\Sigma(E)$ versus energy. (e) PF and (c) figure-of-merit $ZT$ versus Fermi level. $\Sigma(E)$, PF, and $ZT$ are calculated using the DOS-scattering model. $T=300$ K.

$Sb_2Te_3$ initially rise but suddenly decrease below $-0.1$ eV. This occurs as a result of the large DOS and, thus, scattering, associated with the starfish feature. Similar behavior is observed with 2QL $Bi_2Te_3$, however, the decrease is more gradual and begins below roughly $-0.15$ eV; this gives a higher $\Sigma(E)$ over a larger energy range compared to 2QL $Bi_2Se_3$ and $Sb_2Te_3$. These drops in $\Sigma(E)$ due to sudden increases in DOS negatively affect the Seebeck coefficient and conductivity.

The power factor and $ZT$ of 2QL $Bi_2Te_3$ are higher than 2QL $Bi_2Se_3$ and $Sb_2Te_3$ because the increase in DOS from the low-energy ring is located far enough from the Fermi level that it has a minimal negative impact unlike the starfish features. A comparison of the different scattering models (see the Supplemental Material [87]) shows that the $ZT$ values are somewhat similar, but that the cmfp and crt approximations predict large PF peaks deeper in the valence band—such peaks are suppressed with the DOS model due to the large number of states at lower energies. The PF peaks from the different scattering models are separated by roughly one order of magnitude in hole concentration. Finally, comparing the 2QL materials to their 1QL counterparts, the latter present overall better TE performance as a result of their ring-shaped dispersion which is mostly lost when going to 2QL.

## IV. CONCLUSIONS

In this paper we employed first-principles modeling to calculate the thermoelectric properties of two-dimensional single and double quintuple-layer $Bi_2Te_3$, $Bi_2Se_3$, and $Sb_2Te_3$ using the cmfp-, crt-, and DOS-scattering approximations. The focus was to investigate how the unusual ring-shaped dispersions of these materials impact the TE characteristics and to understand how the different scattering approximations influence TE transport—with an emphasis on the DOS-scattering model, which had not (to our knowledge) previously been adopted when studying these materials.

The single QL materials display two ring-shaped valence-band maxima between which is nestled one ring-shaped local minimum (i.e., the moat feature). The ring-shaped states at the band edge result in discontinuous increases in $M(E)$ and $D(E)$ that benefit TE performance. This was previously pointed out [38–40] but within the discussion of a single ring-shaped maximum. Interestingly, below the band edge, the moat produces an abrupt drop in $D(E)$ as those states are removed. This feature further enhances the power factor and $ZT$ with the DOS model as a result of reduced scattering compared to either the cmfp or the crt. To confirm the role played by the two ring-shaped maxima and single ring-shaped minimum, we introduced an analytical octic band model that generally resembles the DFT dispersion. The octic model is found to reproduce the observed discontinuities in the DFT-computed $M(E)$, $V_\lambda(E)$, and $D(E)$.

The 1QL materials show high TE performance with maximum $ZT$ values above 3 in all cases and PF values roughly three to ten times larger than those for a 2D parabolic band (scaled for the same average MFP) [42]. The TE properties of both 1QL $Bi_2Te_3$ and $Bi_2Se_3$ vary significantly with the choice of scattering model with the maximum values predicted using the DOS model. This arises because of the discontinuities brought about by the ring-shaped maxima and moat. Our findings indicate that the benefits of these unusually shaped bands are sensitive to the relative alignment of the both ring maxima and to the degree of ring anisotropy—the latter smooths out the desired abrupt features in the transport distribution. For these reasons, 1QL $Sb_2Te_3$ does not show as much improvement in PF and $ZT$ with the DOS model, compared to the other 1QL materials.

With the 2QL materials, the electron dispersions are qualitatively different than their 1QL counterparts. 2QL $Bi_2Te_3$ shows a star-shaped dispersion near the band edge with a ring feature near $-0.15$ eV. The 2QL $Bi_2Se_3$ and 2QL $Sb_2Te_3$ both possess a small ring near the band edge with starfish-shaped bands at roughly $-0.1$ eV. Due to the relatively large misalignment in energy of these features, lack of a distinctive minimum (i.e., moat), and the small radii of the rings at the band edge, these materials present significantly lower PF and $ZT$ compared to the 1QL case. Double QL $Bi_2Te_3$ shows the best TE performance, among the 2QL materials since the star-shaped dispersion provides a large number of states at the band edge, similar to a ring-shaped band. The different scattering models predict widely varying TE properties; 2QL $Bi_2Te_3$ shows the best performance with the DOS model, whereas 2QL $Bi_2Se_3$ and $Sb_2Te_3$ show the worst performance with the DOS model.

When comparing the TE properties, it is important to remember that the scattering parameters ($\lambda_0$, $\tau_0$, and $K_0$) act as scaling factors to the transport distributions, which are fixed by setting the average MFP for backscattering to be 20 nm with the Fermi level at the band edge. This choice connects the scattering parameters such that one cannot be arbitrarily changed relative to the others and for a given material yields the same conductivity when the Fermi level is aligned at the band edge (where typically the TE properties are near optimal). A different choice in constraint could alter the relative scaling of $\Sigma(E)$ but not its shape. This means that the particular values in $\sigma$ and $\kappa_e$ could change ($S$ depends on the shape of $\Sigma(E)$ not its magnitude) along with PF and $ZT$.

Overall, the ring-shaped dispersion materials investigated in this paper display high PF compared to more typical parabolic bands with the 1QL form of $Bi_2Te_3$ and $Bi_2Se_3$ predicted as most promising due to the double-ring maxima at the band edge in combination with the local ring minimum. The TE properties are found to be sensitive to the choice of scattering approximation. This indicates that further study of rigorous scattering in ring-shaped dispersions is needed to validate which scattering model is best. If the DOS-scattering model is ultimately the most physical and accurate, this paper suggests that these materials may be even better thermoelectrics than previously believed.

## ACKNOWLEDGMENTS

This work was partially supported by DARPA MATRIX (Award No. HR0011-15-2-0037) and NSERC (Discovery Grant No. RGPIN-2016-04881) with computational resources provided by Compute Canada. C.R. acknowledges support from an NSERC Canada Graduate Scholarship and Nova Scotia Graduate Scholarship.

## APPENDIX: ELECTRONIC PROPERTIES OF THE OCTIC BAND MODEL

Here we summarize the expressions for $M(E)$, $V_\lambda(E)$, and $D(E)$ [42] for the octic dispersion model given by Eq. (14). More details are provided in the Supplemental Material [87]. Since the octic model is two dimensional and isotropic in $k$ space, the constant energy surfaces are circles. There are as many as four constant energy circles with the octic band model and their radii in reciprocal space are given by the following expressions:

$$
k_{1}(E)=\frac{1}{\sqrt{2}} \sqrt{k_{a}^{2}+k_{b}^{2}-\sqrt{\left(k_{b}^{2}-k_{a}^{2}\right)^{2}+4 k_{a}^{2} k_{b}^{2} \frac{|E|}{\epsilon_{0}}}}, \tag{A1}
$$

$$
k_{2}(E)=\frac{1}{\sqrt{2}} \sqrt{k_{a}^{2}+k_{b}^{2}-\sqrt{\left(k_{b}^{2}-k_{a}^{2}\right)^{2}-4 k_{a}^{2} k_{b}^{2} \frac{|E|}{\epsilon_{0}}}}, \tag{A2}
$$

$$
k_{3}(E)=\frac{1}{\sqrt{2}} \sqrt{k_{a}^{2}+k_{b}^{2}+\sqrt{\left(k_{b}^{2}-k_{a}^{2}\right)^{2}-4 k_{a}^{2} k_{b}^{2} \frac{|E|}{\epsilon_{0}}}}, \tag{A3}
$$

$$
k_{4}(E)=\frac{1}{\sqrt{2}} \sqrt{k_{a}^{2}+k_{b}^{2}+\sqrt{\left(k_{b}^{2}-k_{a}^{2}\right)^{2}+4 k_{a}^{2} k_{b}^{2} \frac{|E|}{\epsilon_{0}}}}. \tag{A4}
$$

The distribution of modes $M(E)$, average velocity $V_\lambda(E)$, and density of states $D(E)$ can be written compactly in terms of these constant-energy radii. Their expressions are provided below,

$$
M(E)= \begin{cases}\frac{1}{\pi}\left[k_{1}(E)+k_{2}(E)+k_{3}(E)+k_{4}(E)\right], & -\frac{\left(k_{a}^{2}-k_{b}^{2}\right)^{4}}{16 k_{a}^{4} k_{b}^{4}} \epsilon_{0} \leqslant E<0, \\ \frac{1}{\pi}\left[k_{1}(E)+k_{4}(E)\right], & -\epsilon_{0} \leqslant E<-\frac{\left(k_{a}^{2}-k_{b}^{2}\right)^{4}}{16 k_{a}^{4} k_{b}^{4}} \epsilon_{0}, \\ \frac{1}{\pi} k_{4}(E), & E<-\epsilon_{0},\end{cases} \tag{A5}
$$

$$
V_{\lambda}(E)= \begin{cases}\frac{2 \pi \sqrt{\epsilon_{0}|E|}\left(k_{a}^{2}+k_{b}^{2}\right)}{\hbar k_{a}^{2} k_{b}^{2}}\left(\frac{k_{4}^{2}(E)-k_{1}^{2}(E)+k_{3}^{2}(E)-k_{2}^{2}(E)}{k_{1}(E)+k_{2}(E)+k_{3}(E)+k_{4}(E)}\right), & -\frac{\left(k_{a}^{2}-k_{b}^{2}\right)^{4}}{16 k_{a}^{4} k_{b}^{4}} \epsilon_{0} \leqslant E<0, \\ \frac{2 \pi \sqrt{\epsilon_{0}|E|}\left(k_{a}^{2}+k_{b}^{2}\right)}{\hbar k_{a}^{2} k_{b}^{2}}\left(\frac{k_{4}^{2}(E)-k_{1}^{2}(E)}{k_{1}(E)+k_{4}(E)}\right), & -\epsilon_{0} \leqslant E<-\frac{\left(k_{a}^{2}-k_{b}^{2}\right)^{4}}{16 k_{a}^{4} k_{b}^{4}} \epsilon_{0}, \\ \frac{2 \pi \sqrt{\epsilon_{0}|E|}}{\hbar k_{a}^{2} k_{b}^{2}}\left[k_{4}^{2}(E)-k_{1}^{2}(E)\right] k_{4}(E), & E<-\epsilon_{0},\end{cases} \tag{A6}
$$

$$
D(E)= \begin{cases}\frac{k_{a}^{2} k_{b}^{2}}{2 \pi \sqrt{\epsilon_{0}|E|}}\left(\frac{1}{k_{4}^{2}(E)-k_{1}^{2}(E)}+\frac{1}{k_{3}^{2}(E)-k_{2}^{2}(E)}\right), & -\frac{\left(k_{a}^{2}-k_{b}^{2}\right)^{4}}{16 k_{a}^{4} k_{b}^{4}} \epsilon_{0} \leqslant E<0, \\ \frac{k_{a}^{2} k_{b}^{2}}{2 \pi \sqrt{\epsilon_{0}|E|}}\left(\frac{1}{k_{4}^{2}(E)-k_{1}^{2}(E)}\right), & -\epsilon_{0} \leqslant E<-\frac{\left(k_{a}^{2}-k_{b}^{2}\right)^{4}}{16 k_{a}^{4} k_{b}^{4}} \epsilon_{0}, \\ \frac{k_{a}^{2} k_{b}^{2}}{4 \pi \sqrt{\epsilon_{0}|E|}}\left(\frac{1}{k_{4}^{2}(E)-k_{1}^{2}(E)}\right). & E<-\epsilon_{0}.\end{cases} \tag{A7}
$$

[1] C. Forman, I. K. Muritala, R. Pardemann, and B. Meyer, Renewable Sustainable Energy Rev. 57, 1568 (2016).

[2] G. J. Snyder and E. S. Toberer, Nat. Mater. 7, 105 (2008).

[3] A. I. Hochbaum, R. Chen, R. D. Delgado, W. Liang, E. C. Garnett, M. Najarian, A. Majumdar, and P. Yang, Nature (London) 451, 163 (2008).

[4] B. Poudel, Q. Hao, Y. Ma, Y. Lan, A. Minnich, B. Yu, X. Yan, D. Wang, A. Muto, D. Vashaee, X. Chen, J. Liu, M. S. Dresselhaus, G. Chen, and Z. Ren, Science 320, 634 (2008).

[5] K. Biswas, J. He, I. D. Blum, C.-I. Wu, T. P. Hogan, D. N. Seidman, V. P. Dravid, and M. G. Kanatzidis, Nature (London) 489, 414 (2012).

[6] O. Delaire, J. Ma, K. Marty, A. F. May, M. A. McGuire, M.-H. Du, D. J. Singh, A. Podlesnyak, G. Ehlers, M. D. Lumsden, and B. C. Sales, Nat. Mater. 10, 614 (2011).

[7] C. W. Li, J. Hong, A. F. May, D. Bansal, S. Chi, T. Hong, G. Ehlers, and O. Delaire, Nat. Phys. 11, 1063 (2015).

[8] L.-D. Zhao, S.-H. Lo, Y. Zhang, H. Sun, G. Tan, C. Uher, C. Wolverton, V. P. Dravid, and M. G. Kanatzidis, Nature (London) 508, 373 (2014).

[9] M. E. Manley, O. Hellman, N. Shulumba, A. F. May, P. J. Stonaha, J. W. Lynn, V. O. Garlea, A. Alatas, R. P. Hermann, J. D. Budai, H. Wang, B. C. Sales, and A. J. Minnich, Nat. Commun. 10, 1928 (2019).

[10] J. P. Heremans, V. Jovovic, E. S. Toberer, A. Saramat, K. Kurosaki, A. Charoenphakdee, S. Yamanaka, and G. J. Snyder, Science 321, 554 (2008).

[11] J. P. Heremans, B. Wiendlocha, and A. M. Chamoire, Energy Environ. Sci. 5, 5510 (2012).

165406-12

[12] Y. Pei, X. Shi, A. LaLonde, H. Wang, L. Chen, and G. J. Snyder, Nature (London) **473**, 66 (2011).

[13] W. Liu, X. Tan, K. Yin, H. Liu, X. Tang, J. Shi, Q. Zhang, and C. Uher, Phys. Rev. Lett. **108**, 166601 (2012).

[14] Y. Tang, Z. M. Gibbs, L. A. Agapito, G. Li, H.-S. Kim, M. B. Nardelli, S. Curtarolo, and G. J. Snyder, Nat. Mater. **14**, 1223 (2015).

[15] H. Wang, Y. Pei, A. D. LaLonde, and G. J. Snyder, Proc. Natl. Acad. Sci. U.S.A. **109**, 9705 (2012).

[16] X. Liu, T. Zhu, H. Wang, L. Hu, H. Xie, G. Jiang, G. J. Snyder, and X. Zhao, Adv. Energy Mater. **3**, 1238 (2013).

[17] Z. Liu, Y. Wang, J. Mao, H. Geng, J. Shuai, Y. Wang, R. He, W. Cai, J. Sui, and Z. Ren, Adv. Energy Mater. **6**, 1502269 (2016).

[18] X. Su, S. Hao, T. P. Bailey, S. Wang, I. Hadar, G. Tan, T.-B. Song, Q. Zhang, C. Uher, C. Wolverton, X. Tang, and M. G. Kanatzidis, Adv. Energy Mater. **8**, 1800659 (2018).

[19] J. Zhou, H. Zhu, T.-H. Liu, Q. Song, R. He, J. Mao, Z. Liu, W. Ren, B. Liao, D. J. Singh, Z. Ren, and G. Chen, Nat. Commun. **9**, 1721 (2018).

[20] D. Vashaee and A. Shakouri, Phys. Rev. Lett. **92**, 106103 (2004).

[21] J. P. Heremans, C. M. Thrush, and D. T. Morelli, J. Appl. Phys. **98**, 063703 (2005).

[22] J.-H. Bahk, Z. Bian, and A. Shakouri, Phys. Rev. B **87**, 075204 (2013).

[23] J.-H. Bahk, Z. Bian, and A. Shakouri, Phys. Rev. B **89**, 075204 (2014).

[24] M. Thesberg, H. Kosina, and N. Neophytou, J. Appl. Phys. **120**, 234302 (2016).

[25] M. Zebarjadi, G. Joshi, G. Zhu, B. Yu, A. Minnich, Y. Lan, X. Wang, M. Dresselhaus, Z. Ren, and G. Chen, Nano Lett. **11**, 2225 (2011).

[26] M. Zebarjadi, B. Liao, K. Esfarjani, M. Dresselhaus, and G. Chen, Adv. Mater. **25**, 1577 (2013).

[27] N. Neophytou and M. Thesberg, J. Comput. Electron. **15**, 16 (2016).

[28] X. Chen, D. Parker, and D. J. Singh, Sci. Rep. **3**, 3168 (2013).

[29] H. Usui, K. Suzuki, K. Kuroki, S. Nakano, K. Kudo, and M. Nohara, Phys. Rev. B **88**, 075140 (2013).

[30] K. Mori, H. Sakakibara, H. Usui, and K. Kuroki, Phys. Rev. B **88**, 075141 (2013).

[31] H. Usui and K. Kuroki, J. Appl. Phys. **121**, 165101 (2017).

[32] X. G. Wang, L. Wang, J. Liu, and L. M. Peng, Appl. Phys. Lett. **104**, 132106 (2014).

[33] M. Markov, X. Hu, H.-C. Liu, N. Liu, S. J. Poon, K. Esfarjani, and M. Zebarjadi, Sci. Rep. **8**, 9876 (2018).

[34] M. Markov, S. E. Rezaei, S. N. Sadeghi, K. Esfarjani, and M. Zebarjadi, Phys. Rev. Mater. **3**, 095401 (2019).

[35] P. Ghaemi, R. S. K. Mong, and J. E. Moore, Phys. Rev. Lett. **105**, 166603 (2010).

[36] K. Pal, S. Anand, and U. V. Waghmare, J. Mater. Chem. C **3**, 12130 (2015).

[37] F. Zahid and R. Lake, Appl. Phys. Lett. **97**, 212102 (2010).

[38] J. Maassen and M. Lundstrom, Appl. Phys. Lett. **102**, 093103 (2013).

[39] D. Wickramaratne, F. Zahid, and R. K. Lake, J. Appl. Phys. **118**, 075101 (2015).

[40] G. Zhou and D. Wang, Sci. Rep. **5**, 8099 (2015).

[41] J. Liang, L. Cheng, J. Zhang, H. Liu, and Z. Zhang, Nanoscale **8**, 8855 (2016).

[42] C. Rudderham and J. Maassen, J. Appl. Phys. **127**, 065105 (2020).

[43] L. D. Hicks and M. S. Dresselhaus, Phys. Rev. B **47**, 12727 (1993).

[44] L. D. Hicks and M. S. Dresselhaus, Phys. Rev. B **47**, 16631(R) (1993).

[45] R. Kim, S. Datta, and M. Lundstrom, J. Appl. Phys. **105**, 034506 (2009).

[46] M. R. Diznab, I. Maleki, S. M. V. Allaei, Y. Xia, and S. S. Naghavi, ACS Appl. Mater. Interfaces **11**, 46688 (2019).

[47] P. H. Jiang, H. J. Liu, L. Cheng, D. D. Fan, J. Zhang, J. Wei, J. H. Liang, and J. Shi, Carbon **113**, 108 (2017).

[48] E. Witkoske, X. Wang, M. Lundstrom, V. Askarpour, and J. Maassen, J. Appl. Phys. **122**, 175102 (2017).

[49] D. A. Pshenay-Severin, Y. V. Ivanov, and A. T. Burkov, J. Phys.: Condens. Matter **30**, 475501 (2018).

[50] X. Wang, V. Askarpour, J. Maassen, and M. Lundstrom, J. Appl. Phys. **123**, 055104 (2018).

[51] V. Askarpour and J. Maassen, Phys. Rev. B **100**, 075201 (2019).

[52] P. Graziosi, C. Kumarasinghe, and N. Neophytou, J. Appl. Phys. **126**, 155701 (2019).

[53] C. Jeong, R. Kim, M. Luisier, S. Datta, and M. Lundstrom, J. Appl. Phys. **107**, 023707 (2010).

[54] T. Thonhauser, T. J. Scheidemantel, J. O. Sofo, J. V. Badding, and G. D. Mahan, Phys. Rev. B **68**, 085201 (2003).

[55] G. K. H. Madsen and D. J. Singh, Comput. Phys. Commun. **175**, 67 (2006).

[56] M. Lundstrom and C. Jeong, *Near Equilibrium Transport: Fundamentals and Applications* (World Scientific, Singapore, 2013).

[57] F. Giustino, M. L. Cohen, and S. G. Louie, Phys. Rev. B **76**, 165108 (2007).

[58] B. Qiu, Z. Tian, A. Vallabhaneni, B. Liao, J. M. Mendoza, O. D. Restrepo, X. Ruan, and G. Chen, Europhys. Lett. **109**, 57006 (2015).

[59] S. Ponce, E. R. Margine, C. Verdi, and F. Giustino, Comput. Phys. Commun. **209**, 116 (2016).

[60] J.-J. Zhou and M. Bernardi, Phys. Rev. B **94**, 201201(R) (2016).

[61] M. Lundstrom, *Fundamentals of Carrier Transport* (Cambridge University Press, Cambridge, U.K., 2000).

[62] P. Graziosi, C. Kumarasinghe, and N. Neophytou, ACS Appl. Energy Mater. **3**, 5913 (2020).

[63] M. V. Fischetti, IEEE Trans. Electron Devices **38**, 634 (1991).

[64] P. B. Allen, Phys. Rev. Lett. **37**, 1638 (1976).

[65] P. B. Allen, T. P. Beaulac, F. S. Khan, W. H. Butler, F. J. Pinski, and J. C. Swihart, Phys. Rev. B **34**, 4331 (1986).

[66] J. Zhou, R. Yang, G. Chen, and M. S. Dresselhaus, Phys. Rev. Lett. **107**, 226601 (2011).

[67] R. W. McKinney, P. Gorai, V. Stevanovic, and E. S. Toberer, J. Mater. Chem. A **5**, 17302 (2017).

[68] C. Kumarasinghe and N. Neophytou, Phys. Rev. B **99**, 195202 (2019).

[69] A. Putatunda and D. J. Singh, Mater. Today Phys. **8**, 49 (2019).

[70] P. Das, D. Wickramaratne, B. Debnath, G. Yin, and R. K. Lake, Phys. Rev. B **99**, 085409 (2019).

[71] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti *et al.*, J. Phys.: Condens. Matter **21**, 395502 (2009).

165406-13

[72] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. B. Nardelli, M. Calandra, R. Car, C. Cavazzoni *et al.*, J. Phys.: Condens. Matter **29**, 465901 (2017).

[73] P. E. Blöchl, Phys. Rev. B **50**, 17953 (1994).

[74] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

[75] S. Grimme, J. Comput. Chem. **27**, 1787 (2006).

[76] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. B **13**, 5188 (1976).

[77] O. V. Yazyev, J. E. Moore, and S. G. Louie, Phys. Rev. Lett. **105**, 266806 (2010).

[78] C.-X. Liu, H. J. Zhang, B. Yan, X.-L. Qi, T. Frauenheim, X. Dai, Z. Fang, and S.-C. Zhang. Phys. Rev. B **81**, 041307(R) (2010).

[79] S. Nakajima, J. Phys. Chem. Solids **24**, 479 (1963).

[80] R. W. G. Wyckoff, *Crystal Structures* (Wiley-Interscience, New York, 1965).

[81] T. L. Anderson and H. B. Krause, Acta Crystallogr., Sect. B: Struct. Crystallogr. Cryst. Chem. **30**, 1307 (1974).

[82] P. E. Blöchl, O. Jepsen, and O. K. Andersen, Phys. Rev. B **49**, 16223 (1994).

[83] A. Paul, S. Salamat, C. Jeong, G. Klimeck, and M. Lundstrom, J. Comput. Electron. **11**, 56 (2012).

[84] T. Forster, P. Kruger, and M. Rohlfing, Phys. Rev. B **92**, 201404(R) (2015).

[85] T. Forster, P. Kruger, and M. Rohlfing, Phys. Rev. B **93**, 205442 (2016).

[86] C. Shao and H. Bao, Sci. Rep. **6**, 27492 (2016).

[87] See Supplemental Material at https://link.aps.org/supplemental/10.1103/PhysRevB.103.165406 for a description of how the scattering parameters are determined, expressions for the octic band model, and additional thermoelectric properties of 1QL and 2QL $Bi_2Te_3$, $Bi_2Se_3$ and $Sb_2Te_3$.

[88] Y. Pei, H. Wang, and G. J. Snyder, Adv. Mater. **24**, 6125 (2012).

[89] X.-L. Shi, J. Zou, and Z.-G. Chen, Chem. Rev. **120**, 7399 (2020).

[90] H. Sevincli, Nano Lett. **17**, 2589 (2017).