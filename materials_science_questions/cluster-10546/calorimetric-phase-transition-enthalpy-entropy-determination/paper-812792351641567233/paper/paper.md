Cite as: P. M. Celliers et al., Science
10.1126/science.aaw1970 (2019).

# Response to Comment on "Insulator-metal transition in dense fluid deuterium"

Peter M. Celliers,¹* Marius Millot,¹ Stephanie Brygoo,² R. Stewart McWilliams,³
Dayne E. Fratanduono,¹ J. Ryan Rygg,¹⁴ Alexander F. Goncharov,⁵ Paul Loubeyre,²
Jon H. Eggert,¹ J. Luc Peterson,¹ Nathan B. Meezan,¹ Sebastien Le Pape,¹
Gilbert W. Collins,¹⁴ Raymond Jeanloz,⁶ Russell J. Hemley⁷

¹Lawrence Livermore National Laboratory, Livermore, CA 94550, USA. ²CEA, DAM, DIF, F-91297 Arpajon, France. ³School of Physics and Astronomy and Centre for Science at Extreme Conditions, University of Edinburgh, Edinburgh EH9 3FD, UK. ⁴Department of Mechanical Engineering, Physics and Astronomy and Laboratory for Laser Energetics, University of Rochester, Rochester, NY 14623, USA. ⁵Carnegie Institution of Washington, Washington, DC 20015, USA. ⁶Department of Earth and Planetary Science and Department of Astronomy, University of California, Berkeley, CA 94720, USA. ⁷Institute of Materials Science and Department of Civil and Environmental Engineering, The George Washington University, Washington, DC 20052, USA.

*Corresponding author. Email: celliers1@llnl.gov

In their comment, Desjarlais et al. claim that a small temperature drop occurs after isentropic compression of fluid deuterium through the first-order insulator-metal transition. We show that their calculations do not correspond to the experimental thermodynamic path, and that thermodynamic integrations with parameters from first-principles calculations produce results in agreement with our original estimate of the temperature drop.

The recent experiments reported in Celliers et al. (1) and earlier experiments of Knudson et al. (2) compressed samples of liquid deuterium to higher than 300 GPa using quasi-isentropic compression methods. Optical reflectance signals from the two experiments show distinct transitions at two different pressures, $P_1 \approx 200$ GPa (1) and $P_2 \approx 300$ GPa (2). According to our interpretation of both experiments, in (1) the samples were inertially confined because of short time scales and the optical reflectance tracked the initial stages of the first-order insulator-metal (IM) transition at pressure $P_1$; in (2), much longer time scales and lateral gradients resulted in turbulent mixing, which suppressed the optical reflectance signal until the IM transition was complete, at pressure $P_2$. Therefore, we think the two experiments identify the pressures at the start and completion of the IM transition, respectively (i.e., the pressure extent over which the isentrope passes through the coexistence region). The transformation observed in the experiments spans a pressure change of $\Delta P_{\text{IM}} \approx 95$ GPa and a relative specific volume change of $\Delta V/V_1 \approx -0.2$ while conserving entropy $\Delta S \approx 0$. Assuming the temperature is $T_1$ at the start of the transition, the goal is to estimate $T_2$ at $P_2$. First, we review the method used by Desjarlais et al. (3), then follow with a detailed thermodynamic analysis.

Desjarlais et al. use specific heat to estimate $T_2/T_1$. They provide two evaluations using parameters obtained from ab initio models: $C_{\text{P}}$, the specific heat at constant pressure in the metallic fluid (their equation 2, here called DKR-2), and $C_{\text{coex}}$, the specific heat in the coexisting two-phase fluid (their equation 3; DKR-3). The definition of specific heat $C_X = dQ/dT|_X = T\ dS/dT|_X$ describes the temperature change associated with heat transfer under constraint $\Delta X = 0$; note that entropy is not conserved ($\Delta S = \Delta Q/T$). To obtain a temperature drop, Desjarlais et al. need $\Delta Q < 0$, so they extract the latent heat ($-\Delta H_{\text{IM}}$) from the fluid (i.e., cooling) even though $\Delta S = 0$ in the experiments. As justification, Desjarlais et al. state: "Traversal of the phase boundary isothermally ... results in an increase in entropy"; however, there can be no increase in entropy during isentropic compression, and isothermal traversal cannot occur in the experiments. DKR-2 constrains $\Delta X = \Delta P = 0$, whereas DKR-3 constrains cooling to be along the coexistence line. Using the Maxwell relations, we can reduce DKR-3 to equation 4.19 in (4): $C_{\text{coex}} = T(dS/dT)_{\text{coex}} = C_{\text{P}} - T(dV/dT|_{\text{P}})(dP/dT)_{\text{coex}}$, which gives the specific heat of a substance in two-phase coexistence at constant $V$, such as liquid water and its vapor in a sealed container; that is, the constraint is $\Delta X = \Delta V = 0$. The constraint $\Delta V = 0$ causes $P$ to increase as $T$ decreases, like the experiments, but cooling transforms metal to insulator, contrary to the experiments. To recapitulate: Desjarlais et al. calculate cooling ($\Delta S = -\Delta H_{\text{IM}}/T$), either isobaric ($\Delta P = 0$, DKR-2) or isochoric ($\Delta V = 0$, DKR-3), in both cases transforming metal to insulator. There is no correspondence to the experiments where isentropic ($\Delta S = 0$) compression ($\Delta P_{\text{IM}} \approx 95$ GPa and $\Delta V/V_1 \approx -0.2$) transforms insulator to metal.

The compression path, sketched in Fig. 1, follows isen- trope $S_{1}^{I}$ to the coexistence line at $(P_{1}, T_{1})$, then enters the mixed-phase region and follows the coexistence line to $(P_{2}$, $T_{2})$ where the transformation is complete; further compres- sion continues along $S_{2}^{M}$. Because the process is isentropic, $S_{2}^{M}=S_{1}^{I}$. The superscripts I and M refer to the insulating and metallic phases, respectively. Two other isentropes, $S_{2}^{I}$ and $S_{1}^{M}$, intersect the coexistence line at $(P_{2}, T_{2})$ and $(P_{1}, T_{1})$, respectively. At $(P_{1}, T_{1})$ the phase transition can be accom plished by heating at constant $T$ and $P$ with heat energy $\Delta Q_{1}$ equal to the latent heat at $T_{I}: \Delta Q_{1}=\Delta H_{IM}(T_{i})=T_{1} \Delta S_{IM}(T_{1})$ where $\Delta S_{IM}(T_{1})=S_{1}^{M}-S_{1}^{I}$; in general, $\Delta S_{IM}$ is a function of $T$. Because $S_{2}^{M}=S_{1}^{I}$, it follows that $\Delta S_{IM}(T_{1})=S_{1}^{M}-S_{2}^{M}$, and $\Delta S_{IM}(T_{2})=S_{1}^{I}-S_{2}^{I}$.

We can calculate $T_{2}/T_{1}$ along a path comprising a con nected sequence of reversible thermodynamic process steps, $\alpha$, spanning the IM transition and subject to the constraints $\sum_{\alpha} \Delta S_{\alpha}=0$ and $\sum_{\alpha} \Delta P_{\alpha}=\Delta P_{IM}$. One possibility is sketched in Fig. 1, on both the $T-P$ and $S-P$ planes: three steps starting with $100\%$ fraction of the insulating phase at $(P_{1}, T_{1})$. We label each step, and its $T$ at completion, with the subscripts $a$, $b$, and $c$, respectively. Step $a$ is isobaric and isothermal heating by the latent heat $\Delta Q_{a}=\Delta H_{IM}(T_{1})=T_{1} \Delta S_{IM}(T_{1})$ to transform from insulator to metal; therefore, $\Delta S_{a}=$ $+\Delta S_{IM}(T_{1}), \Delta P_{a}=0$, and $\Delta T_{a}=0$. Step $b$ is isentropic com pression from $(P_{1}, T_{a})$ to $(P_{2}, T_{b})$ along $S_{1}^{M}$ in the pure metal lic phase: $\Delta S_{b}=0$ and $\Delta P_{b}=95$ GPa. Finally, step $c$ is isobaric cooling (i.e., DKR-2) from $(P_{2}, T_{b}, S_{1}^{M})$ to $(P_{2}, T_{c}, S_{2}^{M})$: $\Delta S_{c}=-\Delta S_{IM}(T_{1})$ and $\Delta P_{c}=0$. By construction, $\sum_{\alpha} \Delta S_{\alpha}=0, \sum_{\alpha}$ $\Delta P_{\alpha}=\Delta P_{IM}$, and insulator transforms to metal. After step $a$, $T_{a}=T_{1}$ because $\Delta T_{a}=0$; therefore, $T_{2}/T_{1}=(T_{b}/T_{a})(T_{c}/T_{b})$. The DKR-2 calculation provides $T_{c}/T_{b} \approx 0.83$ (step $c$). The re maining term, $T_{b}/T_{a}$, can be determined from the slope of the isentrope in the pure metallic phase. From basic ther modynamic principles, $T\ dP/dT|_{S}=B_{S}/\gamma$, where $B_{S}$ is the is entropic bulk modulus and $\gamma$ is the Grüneisen parameter. Integration along the isentrope from $(P_{1}, T_{a})$ to $(P_{2}, T_{b})$ leads to
$$
\int_{T_{a}}^{T_{b}} d T / T=\int_{P_{1}}^{P_{2}} d P \gamma / B_{\mathrm{S}} \tag{1}
$$
or
$$
T_{b} / T_{a}=\exp \left[\int_{P_{1}}^{P_{2}} d P \gamma / B_{\mathrm{S}}\right] \tag{2}
$$

The slope is negative because $\gamma<0$ (as noted in Desjarlais $et$ $al.$); therefore, $T_{b}<T_{a}$. We estimate $\gamma \approx-1.2$ by examining the isentropes plotted in figure 1 of (2); note that the value $\gamma=-2.3$ from Desjarlais $et$ $al.$ does not apply because it was evaluated within the coexistence region, not the pure metal lic phase. Substituting $B_{S} \approx 525$ GPa [interpolated from Pierleoni $et$ $al.$ (5) supplementary table 5 near 240 GPa, midway along the isentrope between $(P_{1}, T_{a})$ and $(P_{2}, T_{b})$]and $\gamma \approx-1.2$, we find $T_{b}/T_{a} \approx 0.80$; thus, $T_{2}/T_{1}=(T_{b}/T_{a})(T_{c}/T_{b})$ $\approx 0.80 \times 0.83 \approx 0.66$. The path chosen for the calculation is not unique. [A similar calculation on the insulating side of the transition is as follows: $a^{*}$, isobaric cooling from $(P_{1}, T_{1})$ to reduce the entropy by $-\Delta S_{IM}(T_{2})$; $b^{*}$, isentropic compres sion along $S_{2}^{I}$ from $P_{1}$ to $(P_{2}, T_{2}, S_{2}^{I})$; and $c^{*}$, isothermal and isobaric heating by $+\Delta H_{IM}(T_{2})=T_{2} \Delta S_{IM}(T_{2})$ to transform from insulator to metal, reaching $(P_{2}, T_{2}, S_{2}^{M})$.]

$T_{2}/T_{1}$ can also be calculated by direct integration of the Clausius-Clapeyron equation along the coexistence line:
$$
\int_{T_{1}}^{T_{2}} d T / T=\int_{P_{1}}^{P_{2}} d P \Delta V_{\mathrm{IM}}(P) / \Delta H_{\mathrm{IM}}(P) \tag{3}
$$
where the integration starts at $(T_{1}, P_{1})$ and terminates at $(T_{2}$, $P_{2})$. Here, $\Delta V_{IM}(P)$ and $\Delta H_{IM}(P)$ are the volume change and latent heat as a function of pressure along the coexistence line. From this equation,
$$
T_{2} / T_{1}=\exp \left[\int_{P_{1}}^{P_{2}} d P \Delta V_{\mathrm{IM}}(P) / \Delta H_{\mathrm{IM}}(P)\right] \tag{4}
$$

Using estimates for $\Delta H_{IM} \approx 2.62$ kJ/g from Pierleoni $et$ $al.$(5), a $3\%$ volume discontinuity $\Delta V_{IM} \approx-0.015$ cm$^{3}$/g estimat ed from several studies (5-8), and from the experiments $(P_{2}$ $-P_{1}) \approx 95$ GPa, we find $T_{2}/T_{1} \approx 0.58$. The original estimate in Celliers $et$ $al.$ (1), based on a finite difference evaluation of the Clausius-Clapeyron equation, resulted in a scaling factor for $\Delta T=T_{2}-T_{1}=f T_{1}$, where $f=-0.49 \pm 0.16$; therefore, $T_{2}/T_{1}$ $=f+1=0.51 \pm 0.16$. Our study (1) also accounted for cooling from the aluminum piston in (2), which, combined with long time scales, turbulent mixing, and convective heat ex change, might account for a large temperature drop; howev er, quantitative calculations found a small effect $(\sim 100 ~K)$ because the heat capacity of the aluminum piston is much lower than that of the deuterium fluid. Thus, the experi mental path is isentropic to a good approximation, and to simplify the discussion in this response we considered pure ly isentropic processes. The two new estimates given here agree within the uncertainty stated in (1).

To summarize: Thermodynamic path integration is in reasonable agreement with Clausius-Clapeyron integration; all estimates are within the uncertainty range quoted in (1); and finally, anomalous specific heat is not required to ex plain the temperature drop, contrary to the conclusion of Desjarlais $et$ $al.$ Key to these calculations are accurate values

for $\gamma$, $B_{\mathrm{S}}$, and $C_{\mathrm{P}}$ near the IM transition, as well as $\Delta V_{\mathrm{IM}}(P)$ and $\Delta H_{\mathrm{IM}}(P)$.

REFERENCES
1. P. M. Celliers, M. Millot, S. Brygoo, R. S. McWilliams, D. E. Fratanduono, J. R. Rygg, A. F. Goncharov, P. Loubeyre, J. H. Eggert, J. L. Peterson, N. B. Meezan, S. Le Pape, G. W. Collins, R. Jeanloz, R. J. Hemley, Insulator-metal transition in dense fluid deuterium. *Science* **361**, 677–682 (2018). doi:10.1126/science.aat0970 Medline
2. M. D. Knudson, M. P. Desjarlais, A. Becker, R. W. Lemke, K. R. Cochrane, M. E. Savage, D. E. Bliss, T. R. Mattsson, R. Redmer, Direct observation of an abrupt insulator-to-metal transition in dense liquid deuterium. *Science* **348**, 1455–1460 (2015). doi:10.1126/science.aaa7471 Medline
3. M. P. Desjarlais, M. D. Knudson, R. Redmer, Comment on "Insulator-metal transition in dense fluid deuterium". *Science* **363**, eaaw0969 (2019).
4. L. E. Reichl, *A Modern Course in Statistical Physics* (University of Texas, 1980), chapter 4, p. 93.
5. C. Pierleoni, M. A. Morales, G. Rillo, M. Holzmann, D. M. Ceperley, Liquid-liquid phase transition in hydrogen by coupled electron-ion Monte Carlo simulations. *Proc. Natl. Acad. Sci. U.S.A.* **113**, 4953–4957 (2016). doi:10.1073/pnas.1603853113 Medline
6. M. A. Morales, C. Pierleoni, E. Schwegler, D. M. Ceperley, Evidence for a first-order liquid-liquid transition in high-pressure hydrogen from ab initio simulations. *Proc. Natl. Acad. Sci. U.S.A.* **107**, 12799–12803 (2010). doi:10.1073/pnas.1007309107 Medline
7. W. Lorenzen, B. Holst, R. Redmer, First-order liquid-liquid phase transition in dense hydrogen. *Phys. Rev. B* **82**, 195107 (2010). doi:10.1103/PhysRevB.82.195107
8. G. Mazzola, R. Helled, S. Sorella, Phase Diagram of Hydrogen and a Hydrogen-Helium Mixture at Planetary Conditions by Quantum Monte Carlo Simulations. *Phys. Rev. Lett.* **120**, 025701 (2018). doi:10.1103/PhysRevLett.120.025701 Medline

ACKNOWLEDGMENTS
This work was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under contract DE-AC52-07NA27344.

11 December 2018; accepted 27 February 2019
Published online 22 March 2019
10.1126/science.aaw1970

Publication date: 22 March 2019
www.sciencemag.org

![](./images/812792351641567233_1.jpg)

Fig. 1. Thermodynamic paths for compression. The upper and lower frames show thermodynamic paths on the $T$-$P$ and $S$-$P$ planes, respectively; both frames share the same $P$ scale. The experimental compression path (red solid line segments) enters the mixed-phase coexistence region at $(P_1, T_1, S_1^I)$ and follows the coexistence line at equilibrium (blue chain-dashed curve in upper frame) until the transformation is complete at $(P_2, T_2, S_2^M = S_1^I)$. For $T$ calculations, an alternate path (purple dashed curves) consists of step $a$, isobaric and isothermal heating by $+\Delta H_{IM}(T_1)=T_1\Delta S_{IM}(T_1)$ to transform from insulator $(P_1, T_1, S_1^I)$ to metal $(P_1, T_1, S_1^M)$; step $b$, isentropic compression along $S_1^M$ from $(P_1, T_a=T_1, S_1^M)$ to $(P_2, T_b, S_1^M)$; and step $c$, isobaric cooling from $T_b$ to $T_c$ to reach $(P_2, T_c=T_2, S_2^M=S_1^I)$. Step $c$ corresponds to Desjarlais *et al.* Eq. 2 (DKR-2). Desjarlais *et al.* Eq. 3 (DKR-3) follows an isochore in the coexistence region and drives the transition from metal to insulator, contrary to the experiments (see text). Neither DKR-2 nor DKR-3 corresponds to the experimental path.

# Response to Comment on "Insulator-metal transition in dense fluid deuterium"

Peter M. Celliers, Marius Millot, Stephanie Brygoo, R. Stewart McWilliams, Dayne E. Fratanduono, J. Ryan Rygg, Alexander F. Goncharov, Paul Loubeyre, Jon H. Eggert, J. Luc Peterson, Nathan B. Meezan, Sebastien Le Pape, Gilbert W. Collins, Raymond Jeanloz and Russell J. Hemley

Science 363 (6433), eaaw1970.
DOI: 10.1126/science.aaw1970

---

ARTICLE TOOLS
http://science.sciencemag.org/content/363/6433/eaaw1970

RELATED CONTENT
http://science.sciencemag.org/content/sci/361/6403/677.full
http://science.sciencemag.org/content/sci/363/6433/eaaw0969.full

REFERENCES
This article cites 7 articles, 4 of which you can access for free
http://science.sciencemag.org/content/363/6433/eaaw1970#BIBL

PERMISSIONS
http://www.sciencemag.org/help/reprints-and-permissions

---

Use of this article is subject to the [Terms of Service](http://www.sciencemag.org/help/reprints-and-permissions)

Science (print ISSN 0036-8075; online ISSN 1095-9203) is published by the American Association for the Advancement of Science, 1200 New York Avenue NW, Washington, DC 20005. 2017 © The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original U.S. Government Works. The title Science is a registered trademark of AAAS.