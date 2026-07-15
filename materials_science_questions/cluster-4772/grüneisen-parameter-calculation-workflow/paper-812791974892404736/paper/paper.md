Cite as: M. P. Desjarlais et al., Science
10.1126/science.aaw0969 (2019).

# Comment on "Insulator-metal transition in dense fluid deuterium"

Michael P. Desjarlais¹*, Marcus D. Knudson¹, Ronald Redmer²

¹Sandia National Laboratories, Albuquerque, NM, USA. ²Institute of Physics, University of Rostock, Rostock, Germany.

*Corresponding author. Email: mpdesja@sandia.gov

Celliers et al. (Reports, 17 August 2018, p. 677), in an attempt to reconcile differences in inferred metallization pressures, provide an alternative temperature analysis of the Knudson et al. experiments (Reports, 26 June 2015, p. 1455). We show that this reanalysis implies an anomalously low specific heat for the metallic fluid that is clearly inconsistent with first-principles calculations.

Celliers et al. (1) recently reported observation of the insulator-metal transition in deuterium at a substantially lower pressure (~200 GPa) than that reported by Knudson et al. (2) (~280 GPa). To reconcile this difference in metallization pressure, they suggest a correction to the inferred temperatures reported by Knudson et al. Their reanalysis assumes that (i) both sets of experiments—referred to as the NIF and Z experiments, respectively—sample the same first-order phase boundary; (ii) the NIF and Z pressure states are accurate and reflect the entry and exit of the coexistence region, respectively; and (iii) the boundary exhibits constant latent heat. From these assumptions, and applying a Clausius-Clapeyron analysis, they derive a correction factor $\Delta T = -0.49T_0$; that is, the temperatures in the Z experiments decrease by ~600 K for the lowest-$T$ loading path and by nearly 900 K for the highest-$T$ loading path.

Here, we show that the $\Delta T$ obtained in their analysis has severe thermodynamic implications, namely an anomalously low specific heat for the metallic fluid. Because the compression path is isentropic, $\Delta T$ must be such that the system follows an isentrope, as illustrated by the simplified schematic in Fig. 1. Traversal of the phase boundary isothermally (at $S_1$ and $T_0$) results in an increase in entropy, $\Delta S$, governed by $\Delta H = T_0\Delta S$. The $\Delta T$ (= $T_0 - T_1$) required to account for this $\Delta S$, within the simplified diagram of Fig. 1, can be approximated from the specific heat at constant pressure,

$$
C_{\mathrm{P}}=T\left.\frac{d S}{d T}\right|_{\mathrm{P}} \tag{1}
$$

If we assume that $C_{\mathrm{P}}$ depends weakly on $T$ and $P$ away from the coexistence boundary,

$$
\Delta S \approx C_{\mathrm{P}} \ln \frac{T_{0}}{T_{1}} \tag{2}
$$

Thus, given $C_{\mathrm{P}}$, one can determine $\Delta T$ for a given isentrope. Likewise, given $\Delta T$, one can determine the thermodynamically consistent $C_{\mathrm{P}}$.

Although $\Delta H$ is expected to vary along the phase boundary (going to zero at the critical point), we use $\Delta H = 2.75$ kJ/g for illustration (average of the range given by Celliers et al.). In that case, at $T_0 = 1400$ K, $\Delta S = 0.48$ $k_{\mathrm{B}}$/atom across the phase boundary. In their reanalysis, Celliers et al. concluded that the temperature drops by ~50%, so the logarithm term in Eq. 2 is equal to 0.69. This implies $C_{\mathrm{P}} = 0.70$ $k_{\mathrm{B}}$/atom, much lower than expected on physical grounds [$C_{\mathrm{P}} = 3.5$ $k_{\mathrm{B}}$/atom for liquid lithium metal (3)].

We use tables S-IV and S-V in the supporting information for Pierleoni et al. (4) to extract a realistic value for $C_{\mathrm{P}}$ in the metallic fluid, including nuclear quantum effects. A value of 2.6 $k_{\mathrm{B}}$/atom for the metallic fluid is found by differencing the hydrogen results (interpolated to constant $P$) on the metallic fluid branches away from the phase boundary. Using this value for $C_{\mathrm{P}}$ and $\Delta S = 0.48$ $k_{\mathrm{B}}$/atom, one finds $T_1/T_0 = \mathrm{exp}(-\Delta S/C_{\mathrm{P}}) = 0.83$ at 1400 K, or $\Delta T = 240$ K, in reasonable agreement with the direct isentrope calculation shown in figure 1 (green curve) of Knudson et al. (2) and much smaller than $\Delta T = 700$ K suggested by Celliers et al.

The above analysis is meant to be illustrative but neglects the real behavior of the isentropes close to the phase boundary. In actuality, an isentrope's $T$ varies with $P$ and exhibits negative slope close to the transition, consistent with a negative Grüneisen $\gamma$. See, for example, the isentropes obtained by thermodynamic integration in figure 1 of Knudson et al. (2). To fully account for the phase boundary slope

and the curvature of the isentropes near the boundary, we consider the exact expression for the entropy change along the coexistence line, derived from $S(P, T)$:

$$
\left.d S d T\right)_{\text {coex }}=C_{\mathrm{P}} T\left[1-C_{\mathrm{V}} C_{\mathrm{P}} \gamma T B_{\mathrm{T}} \cdot d P d T\right)_{\text {coex }}\right] \tag{3}
$$

where $B_{\mathrm{T}}$ is the isothermal bulk modulus, $C_{\mathrm{V}}$ is the specific heat at constant volume, and $\gamma$ is the Grüneisen $\gamma$.

For this expression, we again take advantage of the published hydrogen values in the supporting information for Pierleoni *et al.* (4). Using their figure S-1 for the compressibility, along with their tables S-IV and S-V for 1500 K and 1200 K, respectively, and spanning the coexistence region in the vicinity of 1350 K from the molecular to atomic branches, we find $B_{\mathrm{T}}=385 \mathrm{GPa}, C_{\mathrm{V}}=5.16 k_{\mathrm{B}} /$ atom (at $r_{\mathrm{s}}=1.43$ ), $C_{\mathrm{P}}$ $=8.94 k_{\mathrm{B}} /$ atom (interpolating at 189 GPa), and $\gamma=-2.3$. In the metallic fluid away from the boundary, we note, in comparison to the $2.6 k_{\mathrm{B}} /$ atom found above, a substantial increase in $C_{\mathrm{P}}$ on the boundary, typical of a first-order phase transition. As a consistency check on these values, we consider the general relation between $C_{\mathrm{P}}$ and $C_{\mathrm{V}}, C_{\mathrm{P}}=C_{\mathrm{V}}(1+$ $\left.\gamma^{2} T C_{\mathrm{V}} / V B_{\mathrm{T}}\right)=8.93 k_{\mathrm{B}} /$ atom, and find very good agreement with the extracted value. Note especially that increasing the isentrope curvature through $\gamma^{2}$ increases $C_{\mathrm{P}}$. For the slope of the coexistence boundary $d P / d T_{\text {coex }}$ in the vicinity of 1350 K, we use $-0.12 \mathrm{GPa} / \mathrm{K}$, which agrees well with the coexistence lines for vdW-DF1 and vdW-DF2, including nuclear quantum effects, around that temperature. Regarding the phase boundary slope, we note that the NIF and Z boundary slopes are very similar, and that both are considerably steeper than the vdW-DF1, vdW-DF2, and CEIMC (4) boundaries.

Combining terms and inserting in Eq. 3, we find

$$
\left.d S d T\right)_{\text {coex }}=4.05 k_{\mathrm{B}} / \text { atom } T \tag{4}
$$

nearly six times larger than implied by the Celliers *et al.* analysis. For a value of $\Delta S=0.48 k_{\mathrm{B}} /$ atom, and integrating, we estimate $T_{1} / T_{0}=0.89$ centered at 1350 K. Applying this to the isentrope that enters the coexistence region at 1416 K in figure 1 of Knudson *et al.* (2) (green curve), we estimate an exit at 1260 K, in very good agreement with the isentrope obtained there by thermodynamic integration. We conclude from this analysis that the factor of 2 reduction in $T$ along the coexistence boundary suggested by Celliers *et al.* is not consistent with the equation of state for the metallic liquid, whereas the estimated temperature drops reported in Knudson *et al.* are consistent. Thus, the argument presented in Celliers *et al.* is not a viable reconciliation of the two sets of experimental results, and the apparent discrepancy remains.

## REFERENCES

1. P. M. Celliers, M. Millot, S. Brygoo, R. S. McWilliams, D. E. Fratanduono, J. R. Rygg, A. F. Goncharov, P. Loubeyre, J. H. Eggert, J. L. Peterson, N. B. Meezan, S. Le Pape, G. W. Collins, R. Jeanloz, R. J. Hemley, Insulator-metal transition in dense fluid deuterium. *Science* **361**, 677–682 (2018). [doi:10.1126/science.aat0970](https://doi.org/10.1126/science.aat0970)

2. M. D. Knudson, M. P. Desjarlais, A. Becker, R. W. Lemke, K. R. Cochrane, M. E. Savage, D. E. Bliss, T. R. Mattsson, R. Redmer, Direct observation of an abrupt insulator-to-metal transition in dense liquid deuterium. *Science* **348**, 1455–1460 (2015). [doi:10.1126/science.aaa7471](https://doi.org/10.1126/science.aaa7471)

3. M. W. Chase, *NIST-JANAF Thermochemical Tables* (American Institute of Physics, ed. 4, 1998).

4. C. Pierleoni, M. A. Morales, G. Rillo, M. Holzmann, D. M. Ceperley, Liquid-liquid phase transition in hydrogen by coupled electron-ion Monte Carlo simulations. *Proc. Natl. Acad. Sci. U.S.A* **113**, 4953–4957 (2016). [doi:10.1073/pnas.1603853113](https://doi.org/10.1073/pnas.1603853113)

## ACKNOWLEDGMENTS

Sandia National Laboratories is a multimission laboratory managed and operated by National Technology and Engineering Solutions of Sandia LLC, a wholly owned subsidiary of Honeywell International Inc., for the U.S. Department of Energy's National Nuclear Security Administration under contract DE-NA0003525. This paper describes objective technical results and analysis. Any subjective views or opinions that might be expressed in the paper do not necessarily represent the views of the U.S. Department of Energy or the United States Government. Supported by Deutsche Forschungsgemeinschaft grants SFB 652 and FOR 2440 (R.R.).

16 November 2018; accepted 27 February 2019
Published online 22 March 2019
10.1126/science.aaw0969

Publication date: 22 March 2019
www.sciencemag.org

![](./images/812791974892404736_1.jpg)

Fig. 1. Notional schematic of the $PT$ phase diagram for deuterium where the latent heat is assumed to vary along the phase boundary. Isentropes, denoted as the colored lines, exhibit varying $\Delta T$ across the first-order, insulator-metal phase boundary ($\Delta H$ goes to zero at the critical point).

# Comment on "Insulator-metal transition in dense fluid deuterium"
Michael P. Desjarlais, Marcus D. Knudson and Ronald Redmer

Science 363 (6433), eaaw0969.
DOI: 10.1126/science.aaw0969

---

ARTICLE TOOLS
http://science.sciencemag.org/content/363/6433/eaaw0969

RELATED CONTENT
http://science.sciencemag.org/content/sci/363/6433/eaaw1970.full
http://science.sciencemag.org/content/sci/361/6403/677.full

REFERENCES
This article cites 3 articles, 3 of which you can access for free
http://science.sciencemag.org/content/363/6433/eaaw0969#BIBL

PERMISSIONS
http://www.sciencemag.org/help/reprints-and-permissions

---

Use of this article is subject to the [Terms of Service](http://www.sciencemag.org/help/reprints-and-permissions)

Science (print ISSN 0036-8075; online ISSN 1095-9203) is published by the American Association for the Advancement of
Science, 1200 New York Avenue NW, Washington, DC 20005. 2017 © The Authors, some rights reserved; exclusive licensee
American Association for the Advancement of Science. No claim to original U.S. Government Works. The title Science is a
registered trademark of AAAS.