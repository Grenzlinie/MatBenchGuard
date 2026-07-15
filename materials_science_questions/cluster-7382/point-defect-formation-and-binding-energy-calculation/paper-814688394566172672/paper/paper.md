# Vacancy formation enthalpy of filled $d$-band noble metals by hybrid functionals

Weiwei Xing, Peitao Liu, Xiyue Cheng, Haiyang Niu, Hui Ma, Dianzhong Li, Yiyi Li, and Xing-Qiu Chen*

Shenyang National Laboratory for Materials Science, Institute of Metal Research, Chinese Academy of Sciences, Shenyang 110016, China

(Received 9 September 2014; revised manuscript received 29 September 2014; published 16 October 2014)

First-principles determination of the vacancy formation enthalpies has been long-term believed to be highly successful for metals. However, a widely known fact is that the various conventional density functional theory (DFT) calculations with the typical semilocal approximations show apparent failures to yield accurate enthalpies of Ag and Au. Recently, the previously commonly assumed linear Arrhenius extrapolation to determine the vacancy formation enthalpies at $T=0$ K from the high-temperature measured concentration of thermally created vacancies has been demonstrated to have to be replaced by the non-Arrhenius local Grüneisen theory (LGT) [A. Glensk, B. Grabowski, T. Hickel, and J. Neugebauer, *Phys. Rev. X* **4**, 011018 (2014)]. The large discrepancies between the conventional DFT-PBE data and the unrevised experimental vacancy formation enthalpies disappear for Cu and Al. Even by following the same LGT revisions for Ag, the large discrepancies still remain substantial at $T=0$ K. Here, we show that the hybrid functional (HSE), by including nonlocal exchange interactions to extend the conventional DFT method, can further correct these substantial failures. Upon a comparison of the experimental valence-band spectra for Cu, Ag, and Au, we have determined the HSE exchange-correlated mixing parameters $\alpha$ of 0.1, 0.25, and 0.4, and further derived the HSE enthalpies of vacancy formation of 1.09, 0.94, and 0.72 eV, respectively; in nice agreement with available LGT-revised experimental data. Our HSE results shed light on how to improve the theoretical predictions to accurately determine the defect formation energies and related thermodynamical properties.

DOI: 10.1103/PhysRevB.90.144105

PACS number(s): 61.72.jj, 71.15.Mb, 73.90.+f

## I. INTRODUCTION

In comparison with semiconductors and insulators, the defect formation energies in metals have been thought to be more successfully derived through first-principles density functional theory (DFT) [1]. For the former, the dominant intrinsic error is due to the band-gap problem and can be traced back to the spurious self-interaction in DFT with the traditional local density (LDA) or generalized gradient (GGA) approximations (i.e., PBE [2] and PW91 [3]). In metals, the so-called self-interaction artifacts are less significant due to the highly efficient electron screening. Therefore the defect formation energies obtained from standard first-principles calculations for metals are in general more accurate than for semiconductors and insulators. However, to date, all DFT-based calculations (LDA, PBE, PW91) have an obvious failure in deriving the enthalpies of formation for the filled $d$-band noble metals (such as fcc-type noble metals Ag and Au, etc.). There exist large discrepancies between DFT and experimental values. DFT-calculated enthalpies of vacancy formation are approximately half (or even smaller) of the experimental values [4]. For instance, the DFT-calculated values are 0.42 eV (PBE), 0.39 eV (PW91), and 0.62 (LDA) eV for Au and 0.72 eV (PBE), 0.69 eV (PW91), and 0.99 eV (LDA) for Pt, whereas their respective experimental enthalpies of vacancy formation are $0.93\pm0.04$ and $1.35\pm0.05$ eV, see Landolt-Börnstein [5]. For these two cases, although the LDA seems to give better enthalpies of vacancy formation than the PBE or PW91 data, their deviations are, indeed, still large with respect to the experimental data. The discrepancies between LDA and GGA have been interpreted mainly according to the different abilities of the LDA and GGA in describing surface energies, since a vacancy can be viewed as an inner surface in an otherwise perfect bulk matrix [1,4]. In addition, it needs to be emphasized for metals that the exchange-correlation (xc) errors for both GGA and LDA are certainly larger for vacancies, at which the density gradients are strongest and chemical bonds are broken [1]. In general, these two factors (the inner surface problem and the xc errors) are believed to be the main cause of the failures of the first-principles calculations of vacancy formation enthalpies in some cases [1,4,5].

Within this context, various approaches to overcome these two shortcomings have been proposed. Firstly, in order to cure the vacancy-induced inner surface problem, Carling *et al.* employed a postprocessing correction scheme using jellium surfaces to estimate the error [6] and good improvements of the prediction of the vacancy formation enthalpy for Al [6], Pt, Pd, and Mo [7] have been achieved. Recently, a revised version [4] of the postprocessing correction scheme established by Carling *et al.* [6] has been proposed without making assumptions about the size and shape of the inner surface, and reduces the difference (typically less than 0.1 eV) between the LDA and the various GGA results [4]. Secondly, for the xc-error problem, a so-called AM05 xc functional has been proposed in describing point defects (including the vacancy formation enthalpies) [8,9]. The accuracy of the AM05 xc functional has been subsequently doubly checked for three fcc-type metals (Al, Cu, and Ni) [10] and the conclusion was that, compared to the recommended experimental vacancy formation enthalpies, the LDA is the most reliable approximation in these metals and provides a better agreement with the experimental data than both the GGA and AM05 functionals.

However, all the above mentioned correction schemes are limited to vacancies [1] and their accuracy was checked with respect to the recommended experimental values [5]. Unexpectedly, Glensk *et al.* has most recently elaborated that the traditional Arrhenius law to extrapolate the experimental

*Corresponding author: xingqiu.chen@imr.ac.cn

$T=0$ K enthalpy of vacancy formation is not accurate [11]. They found that the almost universally accepted linear Arrhe- nius assumption needs to be replaced by a local Grüneisen theory (LGT). It shows that the experimental Gibbs free energy of vacancy formation $(G_{f})$ is strongly nonlinear upon temperature as follows [11]:

$$
G_{f}(T)=H_{0 K, f}-\frac{1}{2} T^{2} S^{\prime}, \quad(1)
$$

where $S'$ is constant resulting in an vacancy formation entropy $S=\frac{1}{2} T S'$, which increases linearly with temperature. This equation shows a nearly $T^{2}$ scaling in the $G_{f}$. Applying this LGT-revised method to treat the previously experimen- tally measured positron annihilation spectroscopy (PAS) and differential dilatometry (DD) data [12] for Al and Cu, the experimental enthalpies of vacancy formation are 0.66 and 1.06 eV, respectively [11], which are in perfect agreement with the standard DFT-PBE values. On the one hand, this finding implies that the early experimentally recommended values [5] obtained via a linear Arrhenius law need to be revised and, on the other hand, the previously developed methods of the surface corrections [4,6,7] or the AM05 xc functional [8-10], which aim at correcting DFT errors in describing the vacancy formation enthalpy, hence, need to be further studied [11].

Therefore given the fact that currently the non-Arrhenius behavior of the Gibbs energy of vacancy formation has been only validated for both Al and Cu [11], it poses a highly urgent task to answer whether or not the agreement between the LGT-revised experimental $T=0$ K vacancy formation enthalpies and the DFT-PBE values can be improved also for the aforementioned metals of Ag and Au in the IB group of Cu with the same valence number in the periodic table. Those metals were already demonstrated to show large discrepancies [4] between the standard DFT values and the previously experimental $T=0$ K extrapolated values from the linear traditional Arrhenius law. In fact, as illustrated below for Ag, the LGT-revised experimental enthalpy of vacancy formation still shows large discrepancies when comparing with the $T=0$ K DFT-PBE values. This situation is intrinsically different from Cu. Interestingly, we demonstrated that their discrepancies between the non-Arrhenius LGT-revised data and the DFT-PBE values for Ag can be indeed rectified by the inclusion of medium-range exchange interactions in the exchange-correction energy functional. Here, through the hybrid functional that properly mixes exact exchange with a semilocal exchange-correlation functional, we have derived theoretically the $T=0$ K enthalpies of vacancy formation of Ag and Au, in nice agreement with the available LGT-revised experimental data. A robust validation of our conclusion can be achieved by extending the inclusion of nonlocal exchange interaction to other $4d$ and $5d$ metals (Pd and Pt), for which a good agreement can be also expected.

## II. COMPUTATIONAL DETAILS

We performed DFT calcualtions using the Vienna $ab$ initio simulation package (VASP) code [13] with the projector- augmented wave (PAW) scheme. Different approximations have been used to treat the xc energy: the semilocal GGA of Pedew, Burke, and Ernzerhof (PBE) [2] and the hybrid xc developed by Heyd, Scuseria, and Ernzerhof (HSE), which was already supplemented in VASP [14,15]. In particular, the hybrid functional mixes the exact exchange in the Hartee-Fock (HF) with a semilocal PBE xc function:

$$
\begin{aligned}
E_{\mathrm{XC}}^{\mathrm{HSE}}= & \alpha E_{x}^{\mathrm{HF}, \mathrm{sr}}(\mu)+(1-\alpha) E_{X}^{\mathrm{PBE}, \mathrm{sr}}(\mu) \\
& +\alpha E_{x}^{\mathrm{PBE}, \operatorname{lr}}(\mu)+E_{c}^{\mathrm{PBE}}, \quad(2)
\end{aligned}
$$

where $\mu=0.20 \AA^{-1}$ controls the range separation between the short-range (sr) and long-range (lr) parts of the Coulomb kernel, and the parameter $\alpha$ determines the fraction of exact HF exchange incorporated. It needs to be mentioned that the optimum value $\alpha$ that leads to the best agreement with experimental data (i.e., band gaps, magnetic properties, and electronic properties) is material specific and often deviates significantly from the standard choice of $\alpha=0.25$ for the HSE calculations [16-19]. It is clear that, when $\alpha$ is 0, the HSE functional reduces to the standard DFT-PBE functional. The energy cutoff for the plane-wave expansion of the electronic orbitals is 500 eV. To derive the enthalpy of vacancy formation, we used the 64-atom supercells and the $3 \times 3 \times 3 k$ mesh in the Brillouin zone.

## III. LGT-REVISED EXPERIMENTAL ENTHALPIES OF VACANCY FORMATION

As shown in Fig. 1, we first revised the previously Arrhenius-extrapolated enthalpies of Cu and Ag using the non-Arrhenius LGT method [11] based on the early exper- imentally measured Gibbs energies of vacancy formation in the high-temperature regions for Cu and Ag. The LGT-revised experimental enthalpies of vacancy formation $(H_{0 \mathrm{K}, f}^{\mathrm{LGT}-\mathrm{Ave} \text {. }})$ are further compiled in Table I, together with the various DFT calculations and experimental findings. For Cu, our LGT-revised experimental data are in full agreement with those values reported by Glensk et al. [11]. From Table I, the LGT-revised value is 1.06 eV, in perfect agreement with

![](./images/814688394566172672_1.jpg)

FIG. 1. (Color online) Experimental (solid symbols), theoretical linear Arrhenius interpolated (dashed lines) and non-Arrhenius LGT fitting (solid curves) Gibbs energies of vacancy formation as a function of temperatures in fcc-type Cu and Ag. The experimental PAS (positron annihilation spectroscopy, open circles) and DD (differential dilatometry, solid circles) data [12] are all located in the high-temperature region close to their melting point.

TABLE I. Enthalpies of vacancy formation for Cu, Ag, and Au. The experimental values of $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{PAS}}$ and $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{DD}}$ refer to the data extrapolated from the measured PAS data and the DD data via the conventional linear Arrheniuns law. $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\mathrm{PAS}}$, $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\mathrm{DD}}$, and $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\mathrm{Ave} \text {. }}$ are the revised values from the measured PAS and the DD data and their averaged value, respectively, according to the extrapolation of the non-Arheniuns LGT-revised scheme. $H_{0 \mathrm{K}, \mathrm{f}}^{\text {Rec. }}$ stands for the experimentally recommended data [5]. $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{HSE}}$ stands for the derived data through the nonlocal xc hybrid functional. $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{PBE}}$ and $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LDA}}$ are the calculated values within the semi(local) exchange-correction xc functionals of PBE and LDA, respectively [4]. $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{AM} 05}$, $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{PBE}-\text { Surf }}$ and $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LDA}-\text { Surf }}$ are the data derived from the AM05 xc functional, the PBE, and LDA surface-corrected treatments in Ref. [4], respectively. $H_{0 \mathrm{K}, \mathrm{f}}^{\text {FP-LMTO }}$, $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{TB}}$, $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{EAM}}$, and $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LSGF}}$ are the data calculated by the full potential linear muffin-tin orbital [21], tight-binding [22], embedded-atom [23], and locally self-consistent Green's-function methods [24], respectively. Note that all data cited for $\mathrm{Cu}$ have been taken from Ref. [11].

<table>
  <thead>
    <tr>
      <th></th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{PAS}}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{DD}}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\mathrm{PAS}}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\mathrm{DD}}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\text { Ave. }}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\text {Rec. }}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{PBE}}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LDA}}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{HSE}}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{AM} 05}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{PBE}-\text { Surf }}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LDA}-\text { Surf }}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\text {FP-LMTO }}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{TB}}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{EAM}}$</th>
      <th>$H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LSGF}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cu</td>
      <td>1.20</td>
      <td>1.30</td>
      <td>1.05</td>
      <td>1.07</td>
      <td><b>1.06</b></td>
      <td>1.28</td>
      <td><b>1.06</b></td>
      <td>1.26</td>
      <td><b>1.09</b></td>
      <td>1.29</td>
      <td>1.37</td>
      <td>1.42</td>
      <td>1.33</td>
      <td>1.29</td>
      <td>0.72</td>
      <td>1.33</td>
    </tr>
    <tr>
      <td>Ag</td>
      <td>0.92</td>
      <td>1.10</td>
      <td>0.99</td>
      <td>0.88</td>
      <td><b>0.94</b></td>
      <td></td>
      <td></td>
      <td></td>
      <td><b>0.94</b></td>
      <td>1.00</td>
      <td>1.09</td>
      <td>1.16</td>
      <td>1.24</td>
      <td>1.31</td>
      <td>0.83</td>
      <td>0.96</td>
    </tr>
    <tr>
      <td>Au</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.93</td>
      <td>0.42</td>
      <td>0.62</td>
      <td><b>0.72</b></td>
      <td>0.56</td>
      <td>0.67</td>
      <td>0.72</td>
      <td>0.82</td>
      <td>1.24</td>
      <td>0.71</td>
      <td>0.71</td>
    </tr>
  </tbody>
</table>

the DFT-PBE data [11]. But, it is significantly smaller by about 0.22 eV than the one (1.28 eV) recommended by Landoldt-Börnstein [5], which was certainly obtained by the traditional linear Arrhenius extrapolation. However, it has been also noted that the previously attributed good agreement for the DFT-LDA, AM05 xc functional, and surface-corrected values of PBE or LDA with the experimental data extrapolated to $T=0$ K via the linear Arrhenius law is accidental [11], because those theoretical values are significantly too large when comparing with the LGT-revised $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\text { Ave. }}$ (see Table I).

From Fig. 1, it can be seen that the non-Arrhenius LGT-revised experimental $T=0$ K enthalpy of vacancy formation $(H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\text { Ave. }})$ is 0.94 eV for Ag. Firstly, as evidenced in Table I, this value is also smaller by about 0.2 eV than the recommended experimental values obtained by traditional linear Arrhenius extrapolation. Secondly, the AM05 xc functional basically fails to catch the good agreement with the LGT-revised experimental enthalpies of vacancy formation for Ag. Thirdly, both surface-corrected $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{GGA}-\text { Surf }}$ and $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LDA}-\text { Surf }}$ are not successful for all two cases of Cu and Ag due to the consistently much larger corrected values in comparison with the LGT-revised experimental data (Table I). Fourthly, the previously calculated data by FP-LMTO [21], tight-binding [22], and embedded-atom [23] methods all exhibited large deviations from the LGT-revised experimental values in Table I. Although a good agreement between the LGT-revised enthalpies and the theoretical data obtained through locally self-consistent Green's-function (LSGF) method [24] seems to exist for Ag, their largest discrepancy, however, appears for Cu. These comparisons reveal the substantial difference between Cu and Ag: the LGT-revised experimental value $(H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\text { Ave. }})$ for Ag is even significantly larger by 17% than the corresponding DFT-PBE value (0.78 eV for Ag in Table I), but for Cu the perfect agreement appears between $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{LGT}-\text { Ave. }}$ and $H_{0 \mathrm{K}, \mathrm{f}}^{\mathrm{PBE}}$. In particular, it needs to be emphasized that no experimentally measured PAS or DD vacancy concentration is available for Au. Although the Gibbs energy of the vacancy formation can be also derived by the equilibrium vacancy concentrations reported in Ref. [20], which were obtained in a fitting to the experimentally measured high-temperature heat capacity, detailed investigations already demonstrated that such a procedure to yield the vacancy concentration (even deriving Gibbs energy) is not reliable [25]. Therefore, currently, for Au, we have not revised the experimental enthalpy of the vacancy formation using the non-Arrhenius LGT method. However, it should be reasonable to expect that for Au the non-Arrhenius LGT extrapolated value may be smaller than the experimentally recommended value of 0.93 eV by Landolt-Börnstein [5] because this common trend has been already observed for both Cu and Ag. Even when comparing with this recommended value of 0.93 eV, it can be seen that for Au, the large discrepancies from Table I still exist for both DFT-PBE and DFT-LDA values.

## IV. HSE RESULTS AND DISCUSSIONS

The above comparison between the LGT-revised experimental enthalpies of vacancy formation and the standard DFT-PBE findings demonstrates that the semilocal PBE functional still fails to catch the good agreement for Ag, although it is a widely used xc approximation in solid systems. Therefore we have applied the HSE hybrid functional calculations by including the nonlocal exchange interactions. Concerning our current metals of Cu, Ag, and Au, we first optimized the mixing xc parameter $\alpha$ among a series of tests varying $\alpha$ from 0 to 0.6 within the HSE framework. The best $\alpha$ value has been selected by comparing the theoretically derived densities of states (DOSs) with the experimentally measured valence-band spectra. For instance, as illustrated in Fig. 2, we compiled a series of the DOSs calculated within the HSE hybrid functional for $\alpha=0$ (namely, DFT-PBE), 0.1, 0.2, 0.3, 0.4, and 0.6 for the fcc-type Au. The results uncovered that, with increasing the mixing parameter of $\alpha$, the electronic bands significantly shift downwards the lower energy with respect to the Fermi level. In particular, with $\alpha=0.4$, a good agreement with the experimental valence-band spectrum [26] has been reached. The two main peaks at $-3.5$ eV and $-6$ eV of the theoretically obtained HSE DOS $(\alpha=0.4)$ match well with the experimentally observed ones, as marked by the arrows in Fig. 2 (left panel). In similarity, as evidenced in Fig. 3 for the fcc-type Ag, with increasing the mixing parameter $\alpha$, the HSE hydrid functional has apparently shifted the derived DOS down to the low-lying energetic region with respect to the standard DFT-PBE functional (namely, $\alpha=0$). In comparison with the experimental valence-band spectrum [27], it is clear that the DOS derived with $\alpha=0.25$ (the recommended value by the standard HSE calculations) exhibits a nice agreement for Ag. Furthermore, for the fcc-type Cu, the DOS derived by the

![](./images/814688394566172672_2.jpg)

FIG. 2. (Color online) (Left) Density of states of Au by increasing the xc mixing parameter $\alpha$ within the HSE hybrid functional framework, along with the experimental valence-band spectrum [26]. (Right) Optimized lattice constants of fcc-type Au as a function of the HSE mixing parameter of $\alpha$.

HSE method with $\alpha=0.1$ reproduces well the experimentally observed valence-band spectra [27–29] and captures basically the DOS features (Fig. 3). However, it needs to be emphasized that in the case of Cu, the standard semilocal DFT-PBE functional also derived a relatively good DOS, matching the experimentally observed spectrum, as compared with the DFT-PBE DOSs for both Ag and Au. This fact implies that in the case of Cu the nonlocal exchange interaction is not as strong as what both Ag and Au exhibit.

![](./images/814688394566172672_3.jpg)

FIG. 3. (Color online) The density of states (DOSs) of Cu and Ag by increasing the xc mixing parameter $\alpha$ within the HSE hybrid functional framework, as compared with available experimental valence-band spectra [27–29].

<table>
<caption>TABLE II. PBE and HSE calculated lattice constants ($a_{\text{PBE}}$ and $a_{\text{HSE}}$ in angstroms) of Cu, Ag, and Au as compared with the experimental data [30] ($a_{\text{expt}}$ in angstroms). The relative errors of $(a_{\text{PBEorHSE}} - a_{\text{expt}})/a_{\text{expt}}$ are also shown together in the corresponding parentheses. In addition, the optimized HSE mixing parameter $\alpha$ has been compiled.</caption>
<thead>
  <tr>
    <th>
    </th>
    <th>Cu</th>
    <th>Ag</th>
    <th>Au</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>$a_{\text{expt}}$</th>
    <td>3.615</td>
    <td>4.069</td>
    <td>4.077</td>
  </tr>
  <tr>
    <th>$a_{\text{PBE}}$</th>
    <td>3.634 (0.5%)</td>
    <td>4.147 (1.9%)</td>
    <td>4.168 (2.2%)</td>
  </tr>
  <tr>
    <th>$a_{\text{HSE}}$</th>
    <td>3.623 (0.2%)</td>
    <td>4.142 (1.7%)</td>
    <td>4.124 (0.7%)</td>
  </tr>
  <tr>
    <th>HSE, $\alpha$</th>
    <td>0.1</td>
    <td>0.25</td>
    <td>0.40</td>
  </tr>
</tbody>
</table>

In addition, from Table II, the HSE nonlocal exchange interaction calculations have substantially improved the predictions for the lattice constants of both Ag and Au. As illustrated in Fig. 2 (right panel), with increasing the HSE mixing parameter $\alpha$, the theoretically derived lattice constants decrease. With the optimum $\alpha$ parameters for Ag ($\alpha=0.25$) and Au ($\alpha=0.4$), the HSE lattice constants $a=4.142$ and $4.124$ Å, respectively, in better agreement with the available experimental findings [30] ($a=4.069$ and $4.077$ Å) than the DFT-PBE values at sufficiently low temperature. In particular, for Cu, both DFT-PBE and HSE ($\alpha=0.10$) calculations yield a nice agreement with the experimental data [30], with a very small relative error within $0.5\%$. All our current calculations show consistency with the reported facts in the previous literature [15,32]. However, in Refs. [15,32], all HSE calculations were performed within the standard mixing xc parameter of $\alpha=0.25$ hydrid functional. These facts indicate that the nonlocal exchange interactions in the exchange-correlation functions play an important role in the energetic, electronic, and lattice properties of Ag and Au, but do not show a large impact on Cu.

Now, we further turn to perform the HSE hybrid functional calculations to include their nonlocal exchange interaction to the vacancy formation enthalpies of Cu, Ag, and Au. For Ag, the standard PBE calculations exhibit a significant deviation from the non-Arrhenius LGT-revised experimental values (Table I and Fig. 4), as discussed above. It needs to be emphasized that we have performed the HSE hybrid calculations self-consistently, and fully relax all cell-internal degrees of freedom surrounding the vacancy. The obtained HSE-derived enthalpies of vacancy formation ($H_{0\text{K}}^{\text{HSE}}$) for Cu, Ag, and Au have been further compiled in Table I. For Cu, the HSE-derived enthalpy of vacancy formation is 1.09 eV, which is only slightly larger by 0.03 eV than the DFT-PBE data. Hence both HSE- and PBE-derived data are in perfect agreement with the LGT-revised data [11]. Consequently, the HSE calculations for Ag significantly improved the accuracy of the standard DFT-PBE predictions of their enthalpies of vacancy formation and yielded, remarkably, a perfect agreement with the non-Arrheniuns LGT-revised experimental values (HSE versus Expt: 0.94 eV versus 0.94 eV for Ag, see Table I). For Au, the HSE calculation yields the value of 0.72 eV. Although no LGT-revised experimental value is available for comparison, we trust that a good agreement should also be expected. The reasons are twofold. On the one

![](./images/814688394566172672_4.jpg)

FIG. 4. (Color online) The Cu-Ag-Au trend of PBE, LDA, and HSE calculated enthalpies of vacancy formation as compared with available experimentally measured data (experimentally recom- mended data and other reported Expt-1 and Expt-2 data [4,5,33]) and the non-Arrhenius LGT revised value at $T=0$ K according to the previous experimental measurements. The lines are guides to the eye.

hand, the non-Arrhenius LGT-revised data are in general lower than the experimentally recommended value [31] and, on the other hand, it is because the HSE-derived data point of 0.72 eV is indeed higher than both the DFT-PBE and the DFT-LDA values, showing a similar trend to what both Cu and Ag exhibited. Mechanically, such a significant improvement of the HSE prediction by including the nonlocal Hartree-Fock-like exchange reflects well the shifting towards the lower energy for fully occupied shells of the $d$-band orbitals with respect to the standard PBE functional (see Fig. 3). Therefore a reduced Pauli repulsion between the $d$ states can be expected, as accompanied with the appearance of the decreased lattice constants (Table II). In line with our results, most recently, nonlocal first-principles calculations in the binary alloying intermetallic systems including the Au element also seem to correct significantly the previously theoretical failures of phase stabilities performed by the standard DFT scheme, in partic- ular, in Au-rich compositions [32]. All these results clearly uncover that the inaccurate description of $d$ orbitals for filled $4d$ or $5d$ metal-containing alloying systems at the PBE level is a serious issue for the precise description of defect formation energies of metals and related intermetallic compounds.

In order to further validate our findings, we have even examined the vacancy formation enthalpies ($H_{0\text{K}}$) of two other metals ($4d$-Pd and $5d$-Pt), which have just one valence electron less than both Ag and Au, respectively. Within the standard DFT-PBE framework, their $H_{0\text{K}}$ values have been reported to be 1.19 eV (PBE) and 1.16 eV (PW91) for Pd and 0.72 eV (PBE) and 0.69 eV (PW91) for Pt [4]. In comparison with the various experimentally reported values (Pd: 1.40–1.87, 1.50, 1.70, and 1.85 eV; Pt: 1.35, 1.26–1.44, and 1.15–1.60 eV) [5,33–35], the DFT data show very large deviations with relative errors as large as over 40%~60%, indicating typically the same situation as discussed above for Ag and Au. Therefore we adopted HSE calculations for both Pd and Pt. Note that the mixing parameter of $4d$ Pd is selected to be $\alpha=0.25$, which is similar to Ag in the fourth row in the periodic table. For $5d$ Pt, we took $\alpha=0.40$, as performed also for Au. Importantly, the resultant HSE-derived enthalpies of vacancy formation of Pd and Pt are 1.32 and 1.28 eV, respectively. With respect to the conventional DFT-PBE findings, for Pt, the HSE exhibits a significant improvement, being much closer to the previously reported experimental data extrapolated to $T=0$ K via the linear Arrhenius law. However, it is a pity that currently no non-Arrhenius LGT- revised experimental enthalpy is available due to the lack of the experimentally measured temperature-dependent vacancy concentrations. In fact, it should be noted that the LGT-revised experimental enthalpy is in general lower than what the linear Arrhenius extrapolated value is and, hence, the HSE data should be expected to show a better agreement even for Pt. Additionally, for Pd, the HSE-derived enthalpy of vacancy formation does also show a significant revision, as compared with the PBE-derived value. It is close to the experimental data, although the currently available experimental findings are still relatively larger and show scattering for Pd, which may need further accurate measurements. Finally, we would like to mention that for Pd, the magnetic interaction also plays a role in determining accurately the enthalpy of vacancy formation. Without the spin-polarized HSE calculations, the enthalpy of vacancy formation is about 1.21 eV, whereas this value is further increased to 1.32 eV by the spin-polarized inclusion. The HSE calculation even revealed that Pd carries a local and sizable magnetic moment of about $0.5\ \mu_B$ and around the vacancy the magnetic moment exhibits a slight increase up to about $0.62\ \mu_B$.

### V. CONCLUSIONS
Our results clearly demonstrated the importance of the nonlocal exchange in filled $3d^{10}$, $4d^{10}$, and $5d^{10}$ metals. It is our conventional wisdom that the nonlocal exchange is only of relevance for insulators and semiconductors, whereas the standard DFT calculations yielded more accurate vacancy formation enthalpies for metals. In fact, from our current calculations, the nonlocal interactions significantly influence the electronic structures of those filled $d$-band metals, especially for Ag and Au. Using HSE calculations with the hybrid functional, the previous failures of the standard DFT-description of the vacancy formation enthalpies of Ag and Au have been substantially improved. The derived data are in nice agreement with the non-Arrhenius LGT-revised experimental data. The current results will have significant implications on the accurate description of the various defect formation energies and related thermodynamical properties as well as phase stabilities for many alloying systems, not only for those metals and their containing alloying systems, but also beyond.

Finally, we also noted that for some partially filled $d$-band metals (such as bcc-type Fe, V, Nb, Ta, Cr, Mo, W, etc.) the enthalpies of vacancy formation and the defect solution enthalpies of impurities have been derived well through conventional first-principles calculations [36–38]. Certainly, it is interesting to further see whether or not the nonlocal exchange interaction plays an important role in affecting their values.

## ACKNOWLEDGMENTS

We thank A. Glensk and C. Franchini for useful discussions. This work was supported by the "Hundred Talents Project" of the Chinese Academy of Sciences, the National Natural Science Foundation of China (Grand Nos. 51474202 and 51174188) and Beijing Supercomputing Center of CAS (including its Shenyang branch) as well as Vienna Supercomputing Center (VSC cluster).

[1] C. Freysoldt, B. Grabowski, T. Hickel, J. Neugebauer, G. Kresse, A. Janotti, and C. G. Van de Walle, *Rev. Mod. Phys.* **86**, 253 (2014).

[2] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **78**, 1396 (1997).

[3] J. P. Perdew, in *Electronic Structure of Solids* (Akademie Verlag, Berlin, 1991).

[4] R. Nazarov, T. Hickel, and J. Neugebauer, *Phys. Rev. B* **85**, 144118 (2012).

[5] P. Ehrhart, P. Jung, H. Schultz, and H. Ullmaier, in *Atomic Defects in Metal*, Landolt-Börnstein, New Series Group III Vol. 25 (Springer-Verlag, Berlin, 1991).

[6] K. Carling, G. Wahnström, T. R. Mattsson, A. E. Mattsson, N. Sandberg, and G. Grimvall, *Phys. Rev. Lett.* **85**, 3862 (2000).

[7] T. R. Mattsson and A. E. Mattsson, *Phys. Rev. B* **66**, 214110 (2002).

[8] R. Armiento and A. E. Mattsson, *Phys. Rev. B* **72**, 085108 (2005).

[9] A. E. Mattsson, R. Armiento, J. Paier, G. Kresse, J. M. Wills, and T. R. Mattsson, *J. Chem. Phys.* **128**, 084714 (2008).

[10] L. Delczeg, E. K. Delczeg-Czirjak, B. Johansson, and L. Vitos, *Phys. Rev. B* **80**, 205121 (2009).

[11] A. Glensk, B. Grabowski, T. Hickel, and J. Neugebauer, *Phys. Rev. X* **4**, 011018 (2014).

[12] T. H. Hehenkamp, *J. Phys. Chem. Solids* **55**, 907 (1994).

[13] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

[14] J. Heyd, G. E. Scuseria, and M. Ernzerhof, *J. Chem. Phys.* **124**, 219906 (2006).

[15] J. Pair, M. Marsman, K. Hummer, G. Kresse, I. C. Gerber, and J. G. Ańgyań, *J. Chem. Phys.* **127**, 024103 (2007).

[16] T. Kawakami, Y. Tsujimoto, H. Kageyama, X.-Q. Chen, C. L. Fu, C. Tassel, A. Kitada, S. Suto, K. Hirama, Y. Sekiya, Y. Makino, T. Okada, T. Yagi, N. Hayashi, K. Yoshimura, S. Nasu, R. Podloucky, and M. Takano, *Nat. Chem.* **1**, 371 (2009).

[17] X.-Q. Chen, C. L. Fu, C. Franchini, and R. Podloucky, *Phys. Rev. B* **80**, 094527 (2009).

[18] J. He, M. X. Chen, X.-Q. Chen, and C. Franchini, *Phys. Rev. B* **85**, 195135 (2012).

[19] F. F. Wang, P. Y. Wei, X. Y. Ding, X. R. Xing, and X.-Q. Chen, *Chin. Phys. Lett.* **31**, 027402 (2014).

[20] Y. Kraftmakher, *Phys Rep.* **299**, 79 (1998).

[21] T. Korhonen, M. J. Puska, and R. M. Nieminen, *Phys. Rev. B* **51**, 9526 (1995).

[22] M. J. Mehl and D. A. Papaconstantopoulos, *Phys. Rev. B* **54**, 4519 (1996).

[23] S. M. Foiles, M. I. Baskes, and M. S. Daw, *Phys. Rev. B* **33**, 7983 (1986).

[24] P. A. Korzhavyi, I. A. Abrikosov, B. Johansson, A. V. Ruban, and H. L. Skriver, *Phys. Rev. B* **59**, 11693 (1999).

[25] M. Forsblom, N. Sandberg, and G. Grimvall, *Phys. Rev. B* **69**, 165106 (2004).

[26] L. Duo, J. A. Evans, A. D. Laine, G. Mondio, P. T. Andrewst, D. Norman, and P. Weightman, *J. Phys.: Condens. Matter* **3**, 989 (1991).

[27] J. D. Riley, R. Leckey, J. Jenkin, J. Liesegang, and R. Poole, *J. Phys. F* **6**, 293 (1976).

[28] J. F. Janak, A. R. Williams, and V. L. Moruzzi, *Phys. Rev. B* **11**, 1522 (1975).

[29] V. Dose and G. Reusing, *J. Electron Spectrosc. Relat. Phenom.* **27**, 261 (1982).

[30] M. Ellner, K. Kolatschek, and B. J. Predel, *Less-Common Met.* **170**, 171 (1991).

[31] Here, we still want to emphasize that via the LGT model the LGT-revised experimental enthalpy of vacancy formation is in general lower than the experimentally recommended values. However, it needs to be noted that, in some cases with very low entropies (almost constant formation energies) of vacancy formation, the LGT-revised result could, in principle, be close to an Arrhenius extrapolation. Yet, no such case has been observed.

[32] Y. S. Zhang, G. Kresse, and C. Wolverton, *Phys. Rev. Lett.* **112**, 075502 (2014).

[33] H.-E. Schaefer, *Phys. Stat. Sol. A* **102**, 47 (1987).

[34] H.-E. Schaefer and F. Banhart, *Phys. Stat. Sol. A* **104**, 263 (1987).

[35] D. Schumacher, A. Seeger, and O. Härlin, *Phys. Stat. Sol.* **25**, 359 (1968).

[36] W. W. Xing, X.-Q. Chen, Q. Xie, G. Lu, D. Z. Li, and Y. Y. Li, *Int. J. Hydrogen Energy* **39**, 11321 (2014).

[37] P. T. Liu, W. W. Xing, X. Y. Cheng, D. Z. Li, Y. Y. Li, and X.-Q. Chen, *Phys. Rev. B* **90**, 024103 (2014).

[38] W. W. Xing, X.-Q. Chen, D. Z. Li, Y. Y. Li, C. L. Fu, S. V. Meschel, and X. Y. Ding, *Intermetallics* **28**, 16 (2012).