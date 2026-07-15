# Equations and Type Curves for Predicting the Polymerization of Amorphous Silica in Geothermal Brines

Oleh Weres, Lawrence Berkeley Laboratory
Andrew Yee, Lawrence Berkeley Laboratory
Leon Tsao, Lawrence Berkeley Laboratory

## Abstract
The polymerization of dissolved silica in aqueous solutions up to $100^\circ\text{C}$ and containing up to $1\ M$ NaCl has been studied experimentally and theoretically. In this paper, the results of this work are presented in a form suitable for practical use in interpreting and predicting the chemistry of silica in geothermal brines. Empirical equations for calculating the rate of molecular deposition of silica on surfaces as a function of silica concentration, temperature, pH, and salinity are presented. Theoretically calculated type curves that depict the decrease of dissolved silica concentration by homogeneous nucleation and particle growth are presented, along with the procedures for using them to predict the course of this process under different conditions.

## Introduction
Usually, silica precipitates from geothermal brines as colloidal amorphous silica (AS). The process of AS precipitation consists of the following steps.

1. Random growth of silica polymers past critical nucleus size. Above this size, the polymers become colloidal AS particles that are large enough to grow spontaneously and without interruption. This process is called *homogeneous nucleation*.
2. Growth of the supercritical AS particles by further chemical deposition of silicic acid on their surfaces.
3. Coagulation or flocculation of the colloidal particles to give a floc-like precipitate or gel.
4. Cementation of the coagulated particles by chemical bonding and further deposition of silica between them to form silica scale and other solid deposits.

The preceding sequence of processes occurs when the concentration of dissolved silica is high enough for homogeneous nucleation to occur at a significant rate. Very roughly, this requires supersaturation by a factor of 2.5 or more. If this condition is met, rapid polymerization occurs, and massive precipitation or scale deposition may follow. This is the case with the brine at Niland (CA), Cerro Prieto (Mexico), and Wairakei (New Zealand), after it has been flashed down to atmospheric pressure. The voluminous floc-like silica deposits encountered in these areas consist of colloidal AS that has been flocculated by the salts in the brine. The crumbly gray and white scales associated with this material are cemented aggregates of colloidal silica.

If the concentration of dissolved silica is too low for rapid homogeneous nucleation to occur, relatively slow heterogeneous nucleation and the deposition of dissolved silica directly on solid surfaces become the dominant polymerization processes. The product of the latter process (essentially Step 2 of the preceding sequence alone) is a dense vitreous silica. At higher temperatures, this process may produce scale at a significant rate.

This paper has two purposes: to summarize succinctly and quantitatively what we have learned in our kinetic studies of silica polymerization and to demonstrate by example how our results may be applied to studying practical problems in geothermal energy utilization. Because it is a summary, actual experimental data and most details of derivation have been omitted; they may be found elsewhere. $^{1,2}$ Because some of the material in this paper is condensed from an earlier paper, $^{2}$ it is partly of a review nature. It is an updated version of an earlier article. $^{3}$

Studies of the actual formation of silica scale and the removal of colloidal silica from geothermal brines have been reported elsewhere. $^{4,5}$

## Molecular Deposition on Solid Surfaces
By molecular deposition we mean the formation of compact, nonporous AS deposits by chemical bonding of dissolved silica directly onto solid surfaces. This is also the mechanism by which colloidal silica particles grow once nucleated.

We studied the molecular deposition process in isolation by adding known amounts of colloidal silica of

---
0197-7520/82/0002-9682$00.25
FEBRUARY 1982

![](./images/811951894397190147_1.jpg)

Fig. 1—Each solid curve is labeled with the corresponding concentration of dissolved silica in undissociated form—i.e., $c(1-\alpha)$. The light quadrilateral, dashed line, and dotted line are discussed in the text.

known surface area to our solutions. Our results for the rate of molecular deposition are summarized by

$$
\begin{aligned}
& R_{m d}(\mathrm{~g} \mathrm{SiO})_2-\mathrm{cm}^{-2}-\mathrm{min}^{-1} \\
& \quad=F\left(\mathrm{pH}, \mathrm{pH}_{\mathrm{nom}}\right) k_{\mathrm{OH}}(T) f_{f}\left(S_{a}\right)\left(1-S^{-1}\right), \quad \ldots(1)
\end{aligned}
$$

where $F(\mathrm{pH}, \mathrm{pH}_{\text {nom }})$ accounts for the effect of $\mathrm{pH}$ and salinity on the rate of molecular deposition, $k_{\mathrm{OH}}(T)$ is the "rate constant" that depends only on temperature, $f_{f}\left(S_{a}\right)$ is proportional to the rate of the forward (deposition) reaction alone, uncorrected for the effect of simultaneous dissolution, and the factor $\left(1-S^{-1}\right)$ approximately corrects the calculated deposition rate for the effect of simultaneous dissolution.

The function $F(\mathrm{pH}, \mathrm{pH}_{\text {nom }})$ is defined and discussed in the following section.

In units of $\mathrm{g}-\mathrm{cm}^{-2}-\mathrm{min}^{-1}$,

$$
\log k_{\mathrm{OH}}(T)=3.1171-4296.6 / T. \quad \ldots \ldots \ldots(2)
$$

$S_{a}$ is the value of the saturation ratio corrected for the effect of ionic dissociation of the dissolved silica but not for the direct effect of salinity:

$$
S_{a}=(1-\alpha) c / c_{o}. \quad \ldots \ldots \ldots \ldots \ldots \ldots \ldots(3)
$$

Formulas and tables needed to calculate $\alpha$, the fraction of total monomeric silica in ionic form, are presented in Appendix A.

The equilibrium solubility of AS in pure water may be calculated using the empirical formula given by Fournier and Rowe $^{6}$:

$$
c_{o}\left(\mathrm{~g} \mathrm{SiO}_{2} / \mathrm{kg} \mathrm{H}_{2} \mathrm{O}\right)=\operatorname{antilog}_{10}(1.52-731 / T). \quad .(4)
$$

$S$ is the actual saturation ratio, with all effects of salinity taken into account. In $\mathrm{NaCl}$ solution at room temperature, ${ }^{7,8}$

$$
S=S_{a} \exp \left(0.1134 m_{\mathrm{NaCl}}\right) / a_{w}{ }^{2}. \quad \ldots \ldots \ldots \ldots(5)
$$

In sodium chloride solutions, to a good approximation, the activity of water is

$$
a_{w}=\exp \left(-0.033 m_{\mathrm{NaCl}}\right). \quad \ldots \ldots \ldots \ldots \ldots(6)
$$

Unfortunately, the analysis of our data already had been completed before the data on which Eq. 5 is based were published. To analyze our data, we had been forced to rely on an estimate of the effect of $\mathrm{NaCl}$ on the solubility of AS, which proved incorrect. This estimate was

$$
S=S_{a} / a_{w}. \quad \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots(7)
$$

We chose to defer reanalyzing our data using Eq. 5, because it holds only at $25^{\circ} \mathrm{C}$. All other formulas given in this paper are consistent with Eq. 7 and each other and will give good results up to $1 \mathrm{M} \mathrm{NaCl}$ if applied consistently. Therefore, use Eq. 7 with the other formulas in this paper for consistency.

To a good approximation, $S_{a}=S$ at low salinity. At low salinity and $\mathrm{pH}<7, S_{a}=S=c / c_{o}$.

$f_{f}$ varies as the fifth power of $S_{a}$ at low values of $S_{a}$ and is approximately linear in $S_{a}$ above a certain "threshold value" $S_{t}$. The slope is continuous at $S_{t}$:

$$
f_{f}\left(S_{a}\right)=S_{a}{ }^{5} \text { if } S_{a}<S_{t} \quad \ldots \ldots \ldots \ldots \ldots(8 a)
$$

or

$$
f_{f}\left(S_{a}\right)=S_{t}{ }^{5}+5 S_{t}{ }^{4}\left(S_{a}-S_{t}\right) \text { if } S_{a}>S_{t}, \quad \ldots \ldots(8 b)
$$

where

$$
S_{t}=\operatorname{antilog}_{10}(0.0977+75.84 / T). \quad \ldots \ldots \ldots(8 c)
$$

We did not study the rate of dissolution experimentally, and Eq. 1 should not be used to try to predict the rate of dissolution.

The rate of molecular deposition as a function of temperature and $c(1-\alpha)$ is presented in Fig. 1. The rate values in Fig. 1 were calculated with $S$ set equal to $S_{a}$, which is approximately true in low-salinity media. To correct the values read from Fig. 1 for this, multiply them by $(1-1 / S) /\left(1-1 / S_{a}\right)$. (This is usually not necessary.)

The quadrilateral outlined in Fig. 1 approximately corresponds to the range of our experimental data; the rest of the figure is based on extrapolation. The dotted line in Fig. 1 represents the boundary between the domains of fifth and first kinetic order. These lie to the right and left of it, respectively. The dashed line represents the limit above which homogeneous nucleation is so rapid that molecular deposition could not be studied separately with our techniques.

The rate of molecular deposition as calculated using


our empirical formulas compares reasonably well with the predictions of Bohlmann, *et al.*⁹ (in their Fig. 6).

# Effect of pH and Salinity on Rate of Molecular Deposition
The rate of molecular deposition of dissolved silica on the AS surface is proportional to the surface density of ionized silanol groups. The surface charge density enters into Eq. 1 through $F(\text{pH},\text{pH}_{\text{nom}})$, which is proportional to it.

Both ionized silanols, which have cations bound to them (sodium in the case of our experiments), and "bare" ionized silanols, which do not have cations bound to them, contribute to the reaction rate. Therefore, $F(\text{pH},\text{pH}_{\text{nom}})$ consists of two terms, one corresponding to cation paired ionized silanols and the other to "bare" ionized silanols. Overall, our data were best fitted using the expression

$$
F(\text{pH},\text{pH}_{\text{nom}})=0.45f'(\text{pH})+0.55f'(\text{pH}_{\text{nom}}),\ \ \ \ .\ .\ .(9)
$$

where

$$
\text{pH}_{\text{nom}}=\text{pH}+\log([\text{Na}^+]/0.069)\ \ \ .\ .\ .\ .\ .\ .\ .\ .\ .\ .(10)
$$

and $[\text{Na}^+]$ is the activity of sodium ion (in molal units).

$\text{pH}_{\text{nom}}$ may be thought of as being a "nominal pH" value, which reflects the fact that increasing salinity has a chemical effect similar to that of increasing pH. When $[\text{Na}^+]=0.069$, $\text{pH}=\text{pH}_{\text{nom}}$. Formulas for calculating $[\text{Na}^+]$ are given in Appendix A.

$f'(\text{pH})$ was defined so as to be equal to one when $\text{pH}=7.0$. Therefore, $F(7.0,\ 7.0)=1$.

The function $f'(\text{pH})=F(\text{pH},\text{pH})$ is presented in Fig. 2. Formulas used to calculate it are presented in Appendix B, and tabulated values of it are presented in Table 1.

Fluoride ion and hydrogen fluoride both catalyze molecular deposition. This effect may be significant at low pH, where the rate of the base catalyzed pathway is small.

Practically speaking, when $F_{\text{tot}}=10^{-3}$ molal, the fluoride catalyzed mechanisms become dominant below about $\text{pH }4.8$. In the presence of $5\times10^{-5}$ molal $F$, they become dominant below about $\text{pH }3.5$. This sets a natural limit to the degree that silica precipitation from geothermal brines may be inhibited by pH reduction alone. However, aluminum complexes with fluoride and blocks the fluoride-catalyzed pathways. Adding any soluble aluminum salt to an acidified brine in an amount slightly greater than the amount of fluoride present (in moles) will block the fluoride-catalyzed pathway completely. Sec. 3.6 of Ref. 1 gives further information.

![](./images/811951894397190147_2.jpg)

Fig. 2—The function plotted here is $f'(\text{pH})$, to which $F(\text{pH},\\text{pH}_{\text{nom}})$ is equal when $\text{pH}=\text{pH}_{\text{nom}}$.

# Homogeneous Nucleation
With most substances, heterogeneous nucleation dominates and homogeneous nucleation is very slow, rare in nature, and difficult to study in the laboratory. The polymerization of AS apparently is an exception to this because of the very low surface tension of the silica/water interface-between 30 and $50\ \text{erg-cm}^{-2}$ over the range of major practical interest. This means that enormous numbers of particles can be produced by homogeneous nucleation (on the order of $10^{16}$ to $10^{20}$ per liter), and this completely swamps the effect of heterogeneous nucleation. This makes the nucleation process in this system experimentally reproducible and predictable, which is rarely the case with other systems.

The most important variables that affect the rate of homogeneous nucleation were found to be the values of $S$ and the surface tension $\gamma$. The surface tension is itself a function of the temperature and the state of ionization of the silica surface. Our homogeneous nucleation data as a whole could be fitted best using the following expression for $\gamma$.

$$
\gamma=63.68-0.049T-0.2174\ T\ I(\text{pH},\text{pH}_{\text{nom}}),\ \ \ .\ .\ .(11)
$$

where

$$
\begin{aligned}
I(\text{pH},\text{pH}_{\text{nom}})=&0.1189\int_{-\infty}^{\text{pH}} F\left[\text{pH}',\text{pH}_{\text{nom}}(\text{pH}')\right] \\
&\cdot d\text{pH}'.\ .\ .\ .\ .\ .\ .\ .\ .\ .\ .\ .\ .\ .\ .\ .\ .\ .(12)
\end{aligned}
$$

Formulas and tables needed to calculate $\gamma$ are given in Appendix B.

The results of this work are embodied in a computer code (SILNUC; written in CDC FORTRAN), which is able to reproduce much of our experimental data to within experimental error. This code is listed, documented, and demonstrated in Chap. 6 of Ref. 1. Figs. 3 through 6 present "homogeneous nucleation curves" generated by SILNUC.

# Methods of Practical Prediction
Most of our work was with "buffer only" solutions, in

![](./images/811951894397190147_3.jpg)

Fig. 3-Homogeneous nucleation curves for $50^{\circ} C$ calculated using SILNUC. Concentration values are in terms of monomeric silica as in SILNUC. $pH=pH_{nom }=5.71$ was used because $F(5.71,5.71)=0.100$.

![](./images/811951894397190147_4.jpg)

Fig. 4-Homogeneous nucleation curves for $75^{\circ} C$ calculated using SILNUC.

which the only cation present was sodium, and with solutions that contained a moderate concentration of add- ed sodium chloride. Some work we did with other salts suggested that their effect is comparable with that of NaCl. These data suggested that silica polymerization in mixed salt solutions can be predicted using the concept of an "effective sodium chloride concentration," de- fined in Appendix A. Calculate the "effective sodium chloride concentration," and proceed to predict the chemical behavior of the silica in the solution as though sodium chloride at this concentration were the only salt present.

To evaluate $R_{m d}$ using a computer, proceed as follows. First, convert all concentrations to units of moles or grams per kilogram of water using Eq. A-1. Calculate $\gamma_{Na^{+}}$ using Eq. A-2 and the data in Table 2, and then calculate $[Na^{+}]$ using Eq. A-4 and $pH_{nom }$ us ing Eq. 10. Calculate $F(pH, pH_{nom })$ using the formulas in Appendix B. Finally, calculate $R_{m d}$ using Eqs. 1 through 8.

To calculate $R_{m d}$ using a calculator, proceed as follows. Assume that $\gamma_{Na^{+}}=0.77$, and calculate $[Na^{+}]$  and $pH_{nom }$ as above. Calculate $F(pH, pH_{nom })$ using Eq.9 and values of $f^{\prime}(pH)$ and $f^{\prime}(pH_{nom })$ read from Fig. 2 or Table 1. Calculate $c(1-\alpha)$ (at $pH<7$ , this is simply equal to $c$ ). Read the value of $R_{m d}$ at $pH=pH_{nom }=7$ that corresponds to this value and the given temperature from Fig. 1, and multiply this value by $F(pH, pH_{nom })$ as deter mined above. If $S$ is close to unity, multiply this product by $(1-1 / S) /(1-1 / S_{a})$ to obtain $R_{m d}$.

![](./images/811951894397190147_5.jpg)

Fig. 5-Homogeneous nucleation curves for $100^{\circ} C$ calculated using SILNUC.

![](./images/811951894397190147_6.jpg)

Fig. 6-Homogeneous nucleation curves for $125^{\circ} C$ calculated using SILNUC.

The course of homogeneous nucleation at constant temperature and $pH$ may be estimated by calculator us ing the calculated homogeneous nucleation curves presented in Figs. 3 through 6. If the temperature of in- terest is near that of one of these figures, the procedure is as follows.

1. Determine the concentration of dissolved silica and the "effective sodium chloride concentration" in units of grams and moles per kilogram of water, respectively.

2. Determine the true value of $S$ under the given con ditions, remembering to account for the dissociation of monosilicic acid $[Si(OH)_{4}]$ and the effect of dissolved salt on solubility (Eq. 7).

3. Calculate the values of $pH_{nom }, F(pH, pH_{nom })$ and y using the tables, formulas in Appendix B, and Eq. 11.

4. Referring to the top part of Table 3, find the com- bination of temperature and concentration for which the value of $S_{ref }$ (the reference value of $S$ ) is closest to that calculated above. This identifies the calculated "reference curve" that is closest to the conditions of in- terest. Read off the corresponding value of $S_{ref }$ and that of $F_{ref }$ from the bottom part of the table.

If the calculated $S$ value is lower than the tabulated values of $S_{ref }$ for the given temperature, heterogeneous nucleation is probably dominant and this procedure can- not be used with confidence in any case. Values of $S$  much higher than those tabulated are unlikely to be en- countered in practice.

The reference curve selected in Step 4 is that one among the curves in Figs. 3 through 6 whose overall
12
SOCIETY OF PETROLEUM ENGINEERS JOURNAL

<table>
<caption>TABLE 1—VALUES OF f'(pH) vs. pH</caption>
<thead>
  <tr>
    <th>pH</th>
    <th>0.0</th>
    <th>0.02</th>
    <th>0.04</th>
    <th>0.06</th>
    <th>0.08</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>5.0</td>
    <td>0.0208</td>
    <td>0.0218</td>
    <td>0.0228</td>
    <td>0.0238</td>
    <td>0.0249</td>
  </tr>
  <tr>
    <td>5.1</td>
    <td>0.0261</td>
    <td>0.0273</td>
    <td>0.0285</td>
    <td>0.0299</td>
    <td>0.0312</td>
  </tr>
  <tr>
    <td>5.2</td>
    <td>0.0327</td>
    <td>0.0342</td>
    <td>0.0357</td>
    <td>0.0374</td>
    <td>0.0391</td>
  </tr>
  <tr>
    <td>5.3</td>
    <td>0.0409</td>
    <td>0.0427</td>
    <td>0.0447</td>
    <td>0.0467</td>
    <td>0.0488</td>
  </tr>
  <tr>
    <td>5.4</td>
    <td>0.0511</td>
    <td>0.0534</td>
    <td>0.0558</td>
    <td>0.0583</td>
    <td>0.0609</td>
  </tr>
  <tr>
    <td>5.5</td>
    <td>0.0637</td>
    <td>0.0665</td>
    <td>0.0695</td>
    <td>0.0726</td>
    <td>0.0758</td>
  </tr>
  <tr>
    <td>5.6</td>
    <td>0.0792</td>
    <td>0.0827</td>
    <td>0.0863</td>
    <td>0.0901</td>
    <td>0.0941</td>
  </tr>
  <tr>
    <td>5.7</td>
    <td>0.0982</td>
    <td>0.1025</td>
    <td>0.1069</td>
    <td>0.1116</td>
    <td>0.1164</td>
  </tr>
  <tr>
    <td>5.8</td>
    <td>0.1214</td>
    <td>0.1265</td>
    <td>0.1319</td>
    <td>0.1375</td>
    <td>0.1433</td>
  </tr>
  <tr>
    <td>5.9</td>
    <td>0.1493</td>
    <td>0.1555</td>
    <td>0.1620</td>
    <td>0.1687</td>
    <td>0.1783</td>
  </tr>
  <tr>
    <td>6.0</td>
    <td>0.185</td>
    <td>0.193</td>
    <td>0.201</td>
    <td>0.209</td>
    <td>0.217</td>
  </tr>
  <tr>
    <td>6.1</td>
    <td>0.225</td>
    <td>0.234</td>
    <td>0.243</td>
    <td>0.253</td>
    <td>0.262</td>
  </tr>
  <tr>
    <td>6.2</td>
    <td>0.273</td>
    <td>0.283</td>
    <td>0.294</td>
    <td>0.305</td>
    <td>0.316</td>
  </tr>
  <tr>
    <td>6.3</td>
    <td>0.328</td>
    <td>0.340</td>
    <td>0.353</td>
    <td>0.366</td>
    <td>0.379</td>
  </tr>
  <tr>
    <td>6.4</td>
    <td>0.392</td>
    <td>0.407</td>
    <td>0.421</td>
    <td>0.436</td>
    <td>0.451</td>
  </tr>
  <tr>
    <td>6.5</td>
    <td>0.467</td>
    <td>0.483</td>
    <td>0.500</td>
    <td>0.517</td>
    <td>0.534</td>
  </tr>
  <tr>
    <td>6.6</td>
    <td>0.552</td>
    <td>0.570</td>
    <td>0.589</td>
    <td>0.608</td>
    <td>0.627</td>
  </tr>
  <tr>
    <td>6.7</td>
    <td>0.648</td>
    <td>0.668</td>
    <td>0.689</td>
    <td>0.710</td>
    <td>0.732</td>
  </tr>
  <tr>
    <td>6.8</td>
    <td>0.754</td>
    <td>0.777</td>
    <td>0.800</td>
    <td>0.824</td>
    <td>0.848</td>
  </tr>
  <tr>
    <td>6.9</td>
    <td>0.872</td>
    <td>0.897</td>
    <td>0.922</td>
    <td>0.948</td>
    <td>0.974</td>
  </tr>
  <tr>
    <td>7.0</td>
    <td>1.000</td>
    <td>1.027</td>
    <td>1.054</td>
    <td>1.082</td>
    <td>1.109</td>
  </tr>
  <tr>
    <td>7.1</td>
    <td>1.138</td>
    <td>1.166</td>
    <td>1.195</td>
    <td>1.225</td>
    <td>1.254</td>
  </tr>
  <tr>
    <td>7.2</td>
    <td>1.284</td>
    <td>1.315</td>
    <td>1.345</td>
    <td>1.376</td>
    <td>1.408</td>
  </tr>
  <tr>
    <td>7.3</td>
    <td>1.439</td>
    <td>1.471</td>
    <td>1.503</td>
    <td>1.535</td>
    <td>1.568</td>
  </tr>
  <tr>
    <td>7.4</td>
    <td>1.601</td>
    <td>1.634</td>
    <td>1.668</td>
    <td>1.701</td>
    <td>1.735</td>
  </tr>
  <tr>
    <td>7.5</td>
    <td>1.769</td>
    <td>1.804</td>
    <td>1.839</td>
    <td>1.873</td>
    <td>1.909</td>
  </tr>
  <tr>
    <td>7.6</td>
    <td>1.94</td>
    <td>1.98</td>
    <td>2.02</td>
    <td>2.05</td>
    <td>2.09</td>
  </tr>
  <tr>
    <td>7.7</td>
    <td>2.12</td>
    <td>2.16</td>
    <td>2.20</td>
    <td>2.24</td>
    <td>2.27</td>
  </tr>
  <tr>
    <td>7.8</td>
    <td>2.31</td>
    <td>2.35</td>
    <td>2.39</td>
    <td>2.42</td>
    <td>2.46</td>
  </tr>
  <tr>
    <td>7.9</td>
    <td>2.50</td>
    <td>2.54</td>
    <td>2.58</td>
    <td>2.62</td>
    <td>2.66</td>
  </tr>
  <tr>
    <td>8.0</td>
    <td>2.70</td>
    <td>2.74</td>
    <td>2.78</td>
    <td>2.82</td>
    <td>2.86</td>
  </tr>
  <tr>
    <td>8.1</td>
    <td>2.90</td>
    <td>2.94</td>
    <td>2.98</td>
    <td>3.02</td>
    <td>3.06</td>
  </tr>
  <tr>
    <td>8.2</td>
    <td>3.10</td>
    <td>3.14</td>
    <td>3.18</td>
    <td>3.22</td>
    <td>3.27</td>
  </tr>
  <tr>
    <td>8.3</td>
    <td>3.31</td>
    <td>3.35</td>
    <td>3.39</td>
    <td>3.43</td>
    <td>3.47</td>
  </tr>
  <tr>
    <td>8.4</td>
    <td>3.52</td>
    <td>3.56</td>
    <td>3.60</td>
    <td>3.64</td>
    <td>3.68</td>
  </tr>
</tbody>
</table>

shape best matches the course of the homogeneous nucleation process under the given conditions. The shift along the $\log t$ axis that will give the reference curve its correct time scale remains to be calculated. This shift may be calculated by the following equation.

$$
\begin{aligned}
\Delta \log t= & -1-\log F\left(\mathrm{pH}, \mathrm{pH}_{\mathrm{nom}}\right)+1,412\left(\gamma / T\right)^{3} \\
& \cdot(\ln S)^{-2}-F_{\text {ref. }} \ldots \ldots \ldots \ldots \ldots \ldots(13)
\end{aligned}
$$

The remaining steps in the calculation are these:
5. Evaluate $\Delta \log t$ from Eq. 13 using the values of $\gamma$, $T$, and $S$ determined in Steps 2 and 3 and the value of $F_{\text {ref }}$ determined in Step 4.
6. Shift the reference curve chosen in Step 4 by $\Delta \log t$ along the $\log t$ axis in the corresponding figure either graphically or mentally. The shift is in this sense: If the value of $\Delta \log t$ is positive, shift the reference curve to the right (i.e., "slow it down"); if $\Delta \log t$ is negative, shift the curve to the left (i.e., "speed it up").

If the desired temperature is not close to that of any of the figures, run through this procedure twice, bracketing the actual temperature with the two nearest tabulated temperatures.

Alternatively, SILNUC may be used to predict the course of homogeneous nucleation in detail.¹

<table>
<caption>TABLE 2—VALUES OF PARAMETERS USED IN EQS. A-2 and A-3</caption>
<tbody>
  <tr>
    <th>Species</th>
    <th>a</th>
    <th>b</th>
    <th>Use to Calculate</th>
  </tr>
  <tr>
    <td>Na⁺</td>
    <td>4</td>
    <td>0.075</td>
    <td>$\gamma_{\text{Na}^+},[\text{Na}^+]$</td>
  </tr>
  <tr>
    <td>H₃SiO₄⁻</td>
    <td>4</td>
    <td>0.0</td>
    <td>$\gamma_{\text{sil},\alpha}$</td>
  </tr>
  <tr>
    <th>Temperature
      <br>(°C)
    </th>
    <th>$\text{pK}_{\text{sil}}$</th>
    <th>$A_{\text{DH}}$</th>
    <th>$B_{\text{DH}}$</th>
  </tr>
  <tr>
    <td>50</td>
    <td>9.50</td>
    <td>0.534</td>
    <td>0.333</td>
  </tr>
  <tr>
    <td>75</td>
    <td>9.27</td>
    <td>0.562</td>
    <td>0.337</td>
  </tr>
  <tr>
    <td>100</td>
    <td>9.10</td>
    <td>0.596</td>
    <td>0.341</td>
  </tr>
  <tr>
    <td>125</td>
    <td>8.98</td>
    <td>0.644</td>
    <td>0.348</td>
  </tr>
</tbody>
</table>

<table>
<caption>TABLE 3—REFERENCE VALUES TO BE USED WITH FIGS. 3 THROUGH 6</caption>
<thead>
  <tr>
    <th rowspan="2">$c_i(\text{g/kg H}_2\text{O})$</th>
    <th colspan="4">Temperature (°C)</th>
  </tr>
  <tr>
    <th>50</th>
    <th>75</th>
    <th>100</th>
    <th>125</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>$S_{\text{ref}}$</th>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>0.6</td>
    <td>3.31</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>0.7</td>
    <td>3.86</td>
    <td>2.66</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>0.8</td>
    <td>4.42</td>
    <td>3.04</td>
    <td>2.20</td>
    <td></td>
  </tr>
  <tr>
    <td>0.9</td>
    <td>4.97</td>
    <td>3.42</td>
    <td>2.47</td>
    <td></td>
  </tr>
  <tr>
    <td>1.0</td>
    <td>5.52</td>
    <td>3.80</td>
    <td>2.75</td>
    <td>2.07</td>
  </tr>
  <tr>
    <td>1.1</td>
    <td>6.07</td>
    <td>4.18</td>
    <td>3.02</td>
    <td>2.28</td>
  </tr>
  <tr>
    <td>1.2</td>
    <td></td>
    <td>4.56</td>
    <td>3.30</td>
    <td>2.48</td>
  </tr>
  <tr>
    <td>1.3</td>
    <td></td>
    <td></td>
    <td>3.57</td>
    <td>2.69</td>
  </tr>
  <tr>
    <td>1.4</td>
    <td></td>
    <td></td>
    <td></td>
    <td>2.90</td>
  </tr>
  <tr>
    <th>$F_{\text{ref}}$</th>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>0.6</td>
    <td>3.12</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>0.7</td>
    <td>2.45</td>
    <td>3.45</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>0.8</td>
    <td>2.03</td>
    <td>2.67</td>
    <td>3.97</td>
    <td></td>
  </tr>
  <tr>
    <td>0.9</td>
    <td>1.74</td>
    <td>2.18</td>
    <td>3.02</td>
    <td></td>
  </tr>
  <tr>
    <td>1.0</td>
    <td>1.53</td>
    <td>1.85</td>
    <td>2.41</td>
    <td>3.53</td>
  </tr>
  <tr>
    <td>1.1</td>
    <td>1.38</td>
    <td>1.61</td>
    <td>2.02</td>
    <td>2.75</td>
  </tr>
  <tr>
    <td>1.2</td>
    <td></td>
    <td>1.44</td>
    <td>1.73</td>
    <td>2.26</td>
  </tr>
  <tr>
    <td>1.3</td>
    <td></td>
    <td></td>
    <td>1.52</td>
    <td>1.91</td>
  </tr>
  <tr>
    <td>1.4</td>
    <td></td>
    <td></td>
    <td></td>
    <td>1.65</td>
  </tr>
</tbody>
</table>

## Sample Calculation
This sample calculation approximately describes brine at Cerro Prieto that has been flashed rapidly down to 100°C in one step. In the flashed brine at Cerro Prieto, the total concentration of Cl⁻ is about 0.3 mol kg⁻¹, and we can set the "effective NaCl concentration" equal to this. The dissolved silica concentration and pH immediately after flashing are typically about 1.0 g·kg⁻¹ and 7.2, respectively. We wish to estimate $R_{md}$ under the initial conditions and to determine approximately the course of silica polymerization by homogeneous nucleation.

$$m_{\mathrm{NaCl}}=I=0.3.$$

$$T=373.15\ \text{K}.$$

$$c_{i}=1.0\ \text{g·kg}^{-1}.$$

$$\mathrm{pH}=7.2.$$

From Eqs. A-2 and A-3 and Table 2,

$$\gamma_{\text{Na}^+}=0.685,$$

$$\gamma_{\text{sil}}=0.650,$$

<table><caption>TABLE 4—VALUES OF i (pH) vs. pH</caption>
<tbody><tr><th>pH</th><th>0.0</th><th>0.02</th><th>0.04</th><th>0.06</th><th>0.08</th></tr>
<tr><td>5.0</td><td>0.0011</td><td>0.0011</td><td>0.0012</td><td>0.0012</td><td>0.0013</td></tr>
<tr><td>5.1</td><td>0.0014</td><td>0.0014</td><td>0.0015</td><td>0.0016</td><td>0.0016</td></tr>
<tr><td>5.2</td><td>0.0017</td><td>0.0018</td><td>0.0019</td><td>0.0020</td><td>0.0020</td></tr>
<tr><td>5.3</td><td>0.0021</td><td>0.0022</td><td>0.0023</td><td>0.0025</td><td>0.0026</td></tr>
<tr><td>5.4</td><td>0.0027</td><td>0.0028</td><td>0.0029</td><td>0.0031</td><td>0.0032</td></tr>
<tr><td>5.5</td><td>0.0034</td><td>0.0035</td><td>0.0037</td><td>0.0039</td><td>0.0040</td></tr>
<tr><td>5.6</td><td>0.0042</td><td>0.0044</td><td>0.0046</td><td>0.0048</td><td>0.0050</td></tr>
<tr><td>5.7</td><td>0.0053</td><td>0.0055</td><td>0.0058</td><td>0.0060</td><td>0.0063</td></tr>
<tr><td>5.8</td><td>0.0066</td><td>0.0069</td><td>0.0072</td><td>0.0075</td><td>0.0078</td></tr>
<tr><td>5.9</td><td>0.0082</td><td>0.0085</td><td>0.0089</td><td>0.0093</td><td>0.0097</td></tr>
<tr><td>6.0</td><td>0.0102</td><td>0.0106</td><td>0.0111</td><td>0.0116</td><td>0.0121</td></tr>
<tr><td>6.1</td><td>0.0126</td><td>0.0132</td><td>0.0138</td><td>0.0144</td><td>0.0150</td></tr>
<tr><td>6.2</td><td>0.0156</td><td>0.0163</td><td>0.0170</td><td>0.0177</td><td>0.0184</td></tr>
<tr><td>6.3</td><td>0.0192</td><td>0.0200</td><td>0.0208</td><td>0.0217</td><td>0.0225</td></tr>
<tr><td>6.4</td><td>0.0235</td><td>0.0244</td><td>0.0254</td><td>0.0264</td><td>0.0274</td></tr>
<tr><td>6.5</td><td>0.0285</td><td>0.0296</td><td>0.0308</td><td>0.0320</td><td>0.0332</td></tr>
<tr><td>6.6</td><td>0.0345</td><td>0.0358</td><td>0.0372</td><td>0.0386</td><td>0.0400</td></tr>
<tr><td>6.7</td><td>0.0415</td><td>0.0431</td><td>0.0447</td><td>0.0463</td><td>0.0480</td></tr>
<tr><td>6.8</td><td>0.0497</td><td>0.0515</td><td>0.0534</td><td>0.0553</td><td>0.0572</td></tr>
<tr><td>6.9</td><td>0.0592</td><td>0.0613</td><td>0.0634</td><td>0.0656</td><td>0.0679</td></tr>
<tr><td>7.0</td><td>0.0702</td><td>0.0725</td><td>0.0750</td><td>0.0775</td><td>0.0801</td></tr>
<tr><td>7.1</td><td>0.0827</td><td>0.0854</td><td>0.0882</td><td>0.0911</td><td>0.0940</td></tr>
<tr><td>7.2</td><td>0.0970</td><td>0.1001</td><td>0.1032</td><td>0.1064</td><td>0.1098</td></tr>
<tr><td>7.3</td><td>0.1131</td><td>0.1166</td><td>0.1202</td><td>0.1238</td><td>0.1275</td></tr>
<tr><td>7.4</td><td>0.1313</td><td>0.1352</td><td>0.1391</td><td>0.1432</td><td>0.1473</td></tr>
<tr><td>7.5</td><td>0.1516</td><td>0.1559</td><td>0.1603</td><td>0.1648</td><td>0.1694</td></tr>
<tr><td>7.6</td><td>0.1741</td><td>0.1789</td><td>0.1837</td><td>0.1887</td><td>0.1937</td></tr>
<tr><td>7.7</td><td>0.1989</td><td>0.2041</td><td>0.2095</td><td>0.2149</td><td>0.2204</td></tr>
<tr><td>7.8</td><td>0.2261</td><td>0.2318</td><td>0.2376</td><td>0.2435</td><td>0.2495</td></tr>
<tr><td>7.9</td><td>0.2556</td><td>0.2618</td><td>0.2681</td><td>0.2745</td><td>0.2809</td></tr>
<tr><td>8.0</td><td>0.2875</td><td>0.2942</td><td>0.3009</td><td>0.3078</td><td>0.3147</td></tr>
<tr><td>8.1</td><td>0.3217</td><td>0.3288</td><td>0.3360</td><td>0.3433</td><td>0.3507</td></tr>
<tr><td>8.2</td><td>0.3582</td><td>0.3657</td><td>0.3733</td><td>0.3810</td><td>0.3888</td></tr>
<tr><td>8.3</td><td>0.3966</td><td>0.4045</td><td>0.4125</td><td>0.4206</td><td>0.4288</td></tr>
<tr><td>8.4</td><td>0.4370</td><td>0.4452</td><td>0.4535</td><td>0.4619</td><td>0.4704</td></tr>
</tbody>
</table>

and

$$\alpha=0.019.$$

From Eqs. 4 and 6, $c_{o}=0.364$, and $a_{w}=0.990$. Then, using Eqs. A-4, 3, and 7,

$$\left[\mathrm{Na}^{+}\right]=0.3 \times 0.685=0.205,$$

$$c_{i}(1-\alpha)=0.981,$$

$$S_{a}=c_{i}(1-\alpha) / c_{o}=0.981 / 0.364=2.695,$$

and

$$S=2.695 / 0.990=2.722$$

From Eq. 10,

$$\mathrm{pH}_{\mathrm{nom}}=7.20+\log (0.205 / 0.069)=7.67.$$

From Tables 1 and 4 and Eqs. 9, B-2, and 11,

$$F(7.20,7.67)=0.45 \times 1.284+0.55 \times 2.070=1.716,$$

$$\begin{aligned}
I(7.20,7.67) & =0.45 \times 0.0970+0.55 \times 0.1912 \\
& =0.1488, \text { and }
\end{aligned}$$

$$\begin{aligned}
\gamma & =63.68-(0.049+0.2174 \times 0.1488) \times 373.15 \\
& =33.32.
\end{aligned}$$

From Table 3, the reference curve is the one for $c_{i}=1.0$ and $100^{\circ} \mathrm{C}$ in Fig. 5, and $F_{\text {ref }}=2.41$.

From Fig. 1, we determine that, at $100^{\circ} \mathrm{C}$, $c_{i}(1-\alpha)=0.981$, and $\mathrm{pH}=\mathrm{pH}_{\mathrm{nom}}=7.0$, $R_{md}$ $=2.2 \times 10^{-7} \mathrm{~g} \cdot \mathrm{cm}^{-2} \cdot \mathrm{min}^{-1}=0.53 \mathrm{~mm}-\mathrm{yr}^{-1}$. Multiplying the value read off of Fig. 1 by the value of $F(\mathrm{pH}, \mathrm{pH}_{\mathrm{nom}})$, we obtain

$$\begin{aligned}
R_{m d} & =2.2 \times 10^{-7} \mathrm{~g} \cdot \mathrm{cm}^{-2} \cdot \mathrm{min}^{-1} \times 1.716 \\
& =3.8 \times 10^{-7} \mathrm{~g} \cdot \mathrm{cm}^{-2} \cdot \mathrm{min}^{-1}=0.9 \mathrm{~mm} \cdot \mathrm{yr}^{-1}.
\end{aligned}$$

From Eq. 13,

$$\Delta \log t=-1-0.24+1.00-2.41=-2.64.$$

Therefore, the reference curve in Fig. 5 is to be "speeded up" by multiplying its time scale by antilog $(-2.64)=2.29 \times 10^{-3}$. Examining the reference curve, we see that under the reference conditions, the concentrations would have dropped to $0.8 \mathrm{~g} \cdot \mathrm{kg}^{-1}$ after about 70 minutes. "Speeding this up" by a factor of $436=1 / 2.29 \times 10^{-3}$ makes it reach $0.8 \mathrm{~g} \cdot \mathrm{kg}^{-1}$ after about 0.16 minutes.

We conclude that the conversion of dissolved to colloidal silica is practically instantaneous under these conditions. Experimental studies confirm this. $^{4,5}$

These results (as well as those generated by SILNUC) must be used carefully and with full awareness of their limitations. First of all, $R_{m d}$ as calculated above is not the rate of scale deposition on a flat surface. Under the conditions of this problem, by far the major mechanism of scale deposition involves electrostatic adhesion of colloidal silica to surfaces followed by cementation by molecular deposition of dissolved silica between the particles. This process results in scale deposition rates much greater than the value of $R_{m d}$ calculated above. $^{4,5}$

Of course, this whole procedure is reliable only if homogeneous nucleation is actually the dominant nucleation process-i.e., when polymerization is rapid.

Finally, we worked up to only $1 \mathrm{M} \mathrm{NaCl}$. Therefore, our results and the various formulas, figures, and tables presented here should not be relied on at higher salt concentrations.

### Nomenclature
$a, b, A_{\mathrm{DH}}, B_{\mathrm{DH}}$ = parameters that appear in the expression for ion activity coefficients (Eq. A-2)
$a_{w}$ = activity of water in brine
$c$ = concentration of dissolved silica, $\mathrm{g} / \mathrm{kg} \mathrm{H}_{2} \mathrm{O}$
$c_{i}$ = initial concentration of dissolved silica, $\mathrm{g} / \mathrm{kg} \mathrm{H}_{2} \mathrm{O}$
$c_{o}$ = equilibrium solubility of AS in pure water at given $T$, $\mathrm{g} / \mathrm{kg} \mathrm{H}_{2} \mathrm{O}$
$f'(pH)$ = function used in the calculation of $F(\mathrm{pH}, \mathrm{pH}_{\mathrm{nom}})$
$f_{f}\left(S_{a}\right)$ = function that expresses the concentration dependence of the rate of molecular deposition uncorrected for simultaneous redissolution

---
SOCIETY OF PETROLEUM ENGINEERS JOURNAL

$F(\mathrm{pH}, \mathrm{pH}_{\mathrm{nom}}) =$ function proportional to the surface density of ionized silanol groups on the surface of AS at given values of $\mathrm{pH}$ and $\mathrm{pH}_{\mathrm{nom}}$

$i(\mathrm{pH}) =$ function used in the calculation of $I(\mathrm{pH}, \mathrm{pH}_{\mathrm{nom}})$

$I =$ ionic strength, molal units

$I(\mathrm{pH}, \mathrm{pH}_{\mathrm{nom}}) =$ function that expresses the effect of surface ionization on the value of $\gamma$ and is proportional to the integral of $F$ over $\mathrm{pH}$

$k_{\mathrm{OH}}(T) =$ apparent rate constant for molecular deposition at $\mathrm{pH} = \mathrm{pH}_{\mathrm{nom}} = 7.0$

$m_{\mathrm{NaCl}} =$ concentration of $\mathrm{NaCl}, \mathrm{mol}/\mathrm{kg}$ $\mathrm{H}_2\mathrm{O}$

$M_{\mathrm{Nacl}} =$ concentration of $\mathrm{NaCl}$ at room temperature, $\mathrm{mol}/\mathrm{L}$

$R_{md} =$ rate of molecular deposition of dissolved silica on solid surfaces, $\mathrm{g\cdot cm^{-2}\cdot min^{-1}}$

$S =$ absolute saturation ratio, corrected for effects of salinity and ionic dissociation

$S_a =$ saturation ratio corrected for effect of ionic dissociation but not for direct effect of salinity

$S_t =$ "threshold value" of $S_a$ above which the rate of molecular deposition is first order in dissolved silica concentration

$T =$ absolute temperature, $\mathrm{K}$

$\alpha =$ fraction of dissolved silica in ionic form-i.e., $\mathrm{H}_3\mathrm{SiO}_4^-$

$\gamma =$ surface tension of AS/water interface, $\mathrm{erg-cm^{-2}}$

$\gamma_{\mathrm{Na}^+} =$ activity coefficient of $\mathrm{Na^+}$

$\gamma_{\mathrm{sil}} =$ activity coefficient of $\mathrm{H}_3\mathrm{SiO}_4^-$

## Acknowledgments
We thank C. Carnahan and C.F. Tsang for helpful comments on this manuscript. This work was supported by the Assistant Secretary for Resource Applications, Office of Industrial and Utility Applications and Operations, Geothermal Energy Div., U.S. DOE, under Contract W-7405-ENG-48.

## References
1. Weres, O., Yee, A., and Tsao, L.: "Kinetics of Silica Polymerization," Report LBL-7033, Lawrence Berkeley Laboratory, Berkeley, CA (July 1980).
2. Weres, O., Yee, A., and Tsao, L.: "Kinetics of Silica Polymerization," J. Colloidal and Interface Sci. (Feb. 1981) 379-402.
3. Weres, O., Yee, A., and Tsao, L.: "Kinetic Equations and Type Curves for Predicting the Precipitation of Amorphous Silica From Geothermal Brines," Proc., SPE 1979 Intl. Symposium on Oilfield and Geothermal Chemistry, Dallas (1979) 249-256.
4. Weres, O., Tsao, L., and Inglesias, E.: "The Chemistry of Silica in Cerro Prieto Brines," Report LBL-10166, Lawrence Berkeley Laboratory, Berkeley, CA (April 1980).
5. Weres, O. and Tsao, L.: "The Chemistry of Silica in Cerro Prieto Brines," Geothermics (April-May 1981) 255-276.
6. Fournier, R.O. and Rowe, J.J.: "The Solubility of Amorphous Silica in Water at High Temperatures and High Pressures," American Mineralogist (1977) 62, 1052-1056.
7. Marshall, W.L. and Warakomski, J.M.: "Amorphous Silica Solubilities-II. Effect of Aqueous Salt Solutions at $25^{\circ}$C. Geochimica et Cosmochimica Acta (1980) 44, 915-924.
8. Marshall, W.L.: "Amorphous Silica Solubilities-III. Activity Coefficient Relations and Predictions of Solubility Behavior in Salt Solutions, $0$-$350^{\circ}$C," Geochimica et Cosmochimica Acta (1980) 44, 925-931.
9. Bohlmann, E.G., Mesmer, R.E., and Berlinski, P.: "Kinetics of Silica Deposition from Simulated Geothermal Brines," Soc. Pet. Eng. J. (Aug. 1980) 239-248.
10. Busey, R.H. and Mesmer, R.E.: "The Ionization of Water in NaCl Media to $300^{\circ}$C," J. Solution Chem. (1976) 5, 147-152.
11. Busey, R.H. and Mesmer, R.E.: "Ionization Equilibrium of Silicic Acid and Polysilicate Formation in Aqueous Sodium Chloride Solutions to $300^{\circ}$C," Inorganic Chem. (1977) 16, 2444-2450.

## APPENDIX A
### Additional Formulas for Calculating Activity Coefficients and Related Quantities
Brine composition data are reported most often in units of moles or grams per liter as determined at room temperature. To determine the "effective NaCl concentration," proceed as follows. First, set the effective concentration of NaCl in molar units equal to the sum of the molar concentrations of chloride and bicarbonate. (Bicarbonate may be ignored if much smaller than chloride, as is usually the case.) Then,

$$
\begin{align*}
m_{\mathrm{NaCl}} &= 1.003/[1-(0.0164+0.00253\ m_{\mathrm{NaCl}}^{1/2}) \\
&\cdot M_{\mathrm{NaCl}}]. \quad \text{.................(A-1)}
\end{align*}
$$

This equation is easy to solve by the method of successive substitutions.

To convert the concentration of dissolved silica from units of grams per liter at room temperature to grams per kilogram of water, multiply the former by $m_{\mathrm{NaCl}}/M_{\mathrm{NaCl}}$ as determined above.

With low-salinity brines, set $m_{\mathrm{NaCl}}$ equal to $M_{\mathrm{NaCl}}$ at room temperature.

To calculate the ion activity coefficients $\gamma_{\mathrm{sil}}$ and $\gamma_{\mathrm{Na}^+}$, use

$$\log\gamma_{\text{sil or Na}^+} = -A_{\mathrm{DH}}I^{1/2}/(1+aB_{\mathrm{DH}}I^{1/2})+b\ I. \ (\text{A-2})$$

To calculate $\alpha$, use

$$\alpha=1/[1+\gamma_{\mathrm{sil}}\text{antilog}(\mathrm{pK}_{\mathrm{sil}}-\mathrm{pH})]. \quad \text{..........(A-3)}$$

In each case, find the appropriate values for the constants that appear in these equations in Table 2.

To calculate $[\mathrm{Na}^+]$, use

$$[\mathrm{Na}^+]=\gamma_{\mathrm{Na}^+}m_{\mathrm{NaCl}}. \quad \text{..................(A-4)}$$

Look up the value of $\mathrm{pK}_{\mathrm{sil}}$ in Table 2 or use $^{10,11}$

$$
\begin{align*}
\mathrm{pK}_{\mathrm{sil}} &=624.9234-33,632.69/T-97.55319\ \ln\ T \\
&+0.097611T+2,170,870/T^2. \quad \text{........(A-5)}
\end{align*}
$$

In Eq. A-5, $T$ is the absolute temperature in degrees Kelvin:

$$T=^\circ\text{C}+273.15. \dots \dots \dots \dots \dots \dots \dots \dots \text{(A-6)}$$

## APPENDIX B

### Formulas and Tables for Calculating $F(\text{pH},\text{pH}_\text{nom})$ and $I(\text{pH},\text{pH}_\text{nom})$
To calculate the value of the function $f'$ (pH) or $f'$ ($\text{pH}_\text{nom}$), proceed as follows. First calculate $f$, a function that is proportional to $f'$. ($f$ is the fraction of surface silanols that are ionized). At $\text{pH}<5.97$, use

$$x=\text{pH}-7.6 \dots \dots \dots \dots \dots \dots \dots \dots \dots \text{(B-1a)}$$

and

$$\log f=\text{antilog } x/(1+6.2 \text{ antilog } x). \dots \dots \dots \text{(B-1b)}$$

At $5.97<\text{pH}<8.73$, use

$$\begin{aligned}
\log f=&x-2.113 \log [1+\text{antilog}(x/2.113)] \\
&-x/(9.654+1.790x+4.181x^2). \dots \dots \text{(B-1c)}
\end{aligned}$$

When $\text{pH}>8.73$, use the symmetry relation:

$$f(x)=1-f(2.258-x) \dots \dots \dots \dots \dots \dots \text{(B-1d)}$$

and either Eq. B-1b or B-1c to evaluate $f$ on the right-hand side.

Then,

$$f'(\text{pH})=f(\text{pH})/0.1189$$

and

$$F(\text{pH},\text{pH}_\text{nom})=0.45f'(\text{pH})+0.55f'(\text{pH}_\text{nom}).$$

The values of $f'$ (pH) are presented in tabular form in Table 1 and in graphical form in Fig. 2.

The integral function defined by Eq. 12 is

$$I(\text{pH},\text{pH}_\text{nom})=0.45i(\text{pH})+0.55i(\text{pH}_\text{nom}), \dots \text{(B-2)}$$

where

$$i(\text{pH})=\int_{-\infty}^{\text{pH}} f(\text{pH}')d\text{pH}'.$$

To calculate $i(\text{pH})$ at $\text{pH}<5.97$, use

$$i=\text{antilog } (1+6.2 \text{ antilog } x)/6.2, \dots \dots \dots \dots \text{(B-3a)}$$

with $x$ as above.

For $5.97<\text{pH}<8.73$, use

$$i=\text{antilog } (-0.759+0.590x-0.1129x^2). \dots \text{(B-3b)}$$

For $\text{pH}>8.73$, use the symmetry relation:

$$i(x)=i(2.258-x)+x-1.129, \dots \dots \dots \dots \dots \text{(B-3c)}$$

using Eq. B-3a or Eq. B-3b to calculate $i$ on the right-hand side.

The values of $i(\text{pH})$ are presented in Table 4.

Finally, use Eq. 11 to calculate $\gamma$.

### SI Metric Conversion Factors
<table>
  <tr>
    <td>erg</td>
    <td>× 1.0*</td>
    <td>E-07</td>
    <td>= J</td>
  </tr>
  <tr>
    <td>°F</td>
    <td>(°F-32)/1.8</td>
    <td></td>
    <td>= °C</td>
  </tr>
  <tr>
    <td>in.</td>
    <td>× 2.54*</td>
    <td>E+01</td>
    <td>= mm</td>
  </tr>
  <tr>
    <td>L</td>
    <td>× 1.0*</td>
    <td>E+00</td>
    <td>= dm³</td>
  </tr>
  <tr>
    <td>lbm</td>
    <td>× 4.535 924</td>
    <td>E-01</td>
    <td>= kg</td>
  </tr>
</table>

*Conversion factor is exact.
SPEJ

Original manuscript received in Society of Petroleum Engineers office Oct. 14, 1980.
Paper (SPE 9682) accepted for publication Sept. 2, 1981. Revised manuscript received Dec. 14, 1981.