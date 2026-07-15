![](./images/813085369993003009_1.jpg)

Fluid Phase Equilibria 125 (1996) 195-203

![](./images/813085369993003009_2.jpg)

# Molecular dynamics simulation of interphase transport at liquid surfaces

## Mitsuhiro Matsumoto

Department of Applied Physics, School of Engineering, Nagoya University, Chikusa-ku, Nagoya 464-01, Japan

## Abstract

Molecular dynamics computer simulations were carried out to investigate transport phenomena near liquid-vapor interfaces. The phenomena examined were: (1) the evaporation-condensation dynamics of pure substances (argon and water) in a wide range of temperature; (2) the evaporation-condensation dynamics of water molecules through a surface-adsorbed methanol layer; and (3) the dynamics of gas ($CO_2$ and $SO_2$) absorption on a water surface. Various dynamic phenomena, e.g., molecular exchange and surface migration, were observed.

Keywords: Molecular simulation; Vapor-liquid equilibria; Liquid surface; Evaporation; Condensation; Gas absorption

## 1. Introduction

Transport phenomena at a liquid-vapor interface are fundamental and important in various fields of science and engineering. They have a long history of experimental and theoretical study from the macroscopic point of view, but the mechanism at a molecular level is still not very clear. There are several reasons behind this, such as experimental difficulties (temperature control, surface contamination, etc.) and conceptual confusion. For example, the evaporation and condensation rates of pure substances at a given temperature are clearly defined physical constants, which are conceptually very similar to chemical reaction rates, and are described in terms of the condensation coefficient [1]. However, measured values scatter over several orders of magnitude, and it is only quite recently that accurate measurements have been made possible for several substances under some limited conditions [2,3]. Furthermore, we have recently shown using a molecular dynamics (MD) computer simulation technique that the conventional microscopic condensation model, which is based on the transition state theory and assumes that the condensation is a unimolecular process, is incorrect [4-9].

In this paper, we show the usefulness of MD simulation for investigating these interphase transport phenomena. Two topics are presented here, namely, the evaporation-condensation dynamics (pure argon, pure water, and methanol-water mixture) and the gas adsorption dynamics; these two are very similar from the viewpoint of transport mechanism at a molecular level.

0378-3812/96/$15.00 Copyright © 1996 Elsevier Science B.V. All rights reserved.
PII S0378-3812(96)03123-8

<table>
<caption>Table 1
Simulational conditions for argon and water. The number of molecules and the total simulation time depend on the system temperature</caption>
<tbody>
<tr>
<th>System</th>
<td>Argon</td>
<td>Water</td>
</tr>
<tr>
<th>Temperature/K</th>
<td>80-130</td>
<td>350-500</td>
</tr>
<tr>
<th>Number of molecules</th>
<td>1000-6000</td>
<td>864-2000</td>
</tr>
<tr>
<th>Time step/fs</th>
<td>7.5</td>
<td>0.5</td>
</tr>
<tr>
<th>Total time/ns</th>
<td>0.7-2.0</td>
<td>0.15-0.50</td>
</tr>
<tr>
<th>Molecular interaction</th>
<td>Lennard-Jones [5]</td>
<td>TIP4P [10]</td>
</tr>
</tbody>
</table>

It is certain that these kinds of interphase transport become more important under non-equilibrium conditions, but here we concentrate on systems under (macroscopically) equilibrium conditions; similarly to chemical reactions, microscopic transport still exists under equilibrium.

## 2. Simulation method

A microcanonical ensemble MD method was adopted. Molecules are confined in a rectangular unit cell with periodic boundary conditions for all three directions. Molecular interactions are realized by the Lennard-Jones (12-6) model for argon, a rigid rotor model with Lennard-Jones and Coulombic site-site interactions for water and methanol, or a rigid rotor with Lennard-Jones interaction sites and a point electric dipole on the center of mass for $\mathrm{CO}_{2}$ and $\mathrm{SO}_{2}$.

Initially all molecules form a liquid membrane in the central part of the cell, but after an equilibrating process (typically for 100 ps), some of the molecules are evaporated, and the vapor-liquid equilibrium is reached. The technical details are very similar to our previous studies [5,6]. Simulation conditions are described in Table 1 for pure substances (argon and water) and in Table 2 for mixtures.

## 3. Pure substances

This section is a brief summary of simulational results that we previously reported elsewhere for pure substances [5-9].

<table>
<caption>Table 2
Simulational conditions for aqueous mixtures</caption>
<tbody>
<tr>
<th>Solute</th>
<td>Methanol</td>
<td>$\mathrm{CO}_{2}$</td>
<td>$\mathrm{SO}_{2}$</td>
</tr>
<tr>
<th>Temperature/K</th>
<td>400</td>
<td>300</td>
<td>300</td>
</tr>
<tr>
<th>Number of water molecules</th>
<td>1000</td>
<td>1156</td>
<td>1112</td>
</tr>
<tr>
<th>Number of solute molecules</th>
<td>280</td>
<td>20</td>
<td>40</td>
</tr>
<tr>
<th>Time step/fs</th>
<td>0.6</td>
<td>0.5</td>
<td>0.5</td>
</tr>
<tr>
<th>Total time/ns</th>
<td>0.18</td>
<td>0.50</td>
<td>0.75</td>
</tr>
<tr>
<th>Interaction for water</th>
<td>TIP4P[10]</td>
<td>TIP4P[10]</td>
<td>TIP4P[10]</td>
</tr>
<tr>
<th>Interaction for solute</th>
<td>TIPS[11]</td>
<td>Murthy et al.[12]</td>
<td>Hayashi et al.[13]</td>
</tr>
</tbody>
</table>

Let us consider a system under vapor-liquid equilibrium, where evaporation and condensation rates should be equal. If vapor molecules colliding with the surface always become condensed, the rate of condensation is estimated from the collision flux, or the number of vapor molecules incident on the surface of unit area per unit time, $J_{\text{coll}}$.

When the temperature is low and the vapor can be regarded as an ideal gas, we can use the well-known Hertz-Knudsen formula [1] to calculate the collision flux as

$$
J_{\text{coll}} = \frac{N_{\text{A}} P}{\sqrt{2 \pi M R T}} \tag{1}
$$

where $P$ is the vapor pressure, $N_{\text{A}}$ the Avogadro number, $M$ the molecular weight, $R$ the gas constant, and $T$ the temperature. However, all incident molecules are not necessarily caught on the surface; thus, the condensation coefficient $\alpha$ defined as the number ratio of condensed molecules to the incident ones is not always unity.

Experimental values of $\alpha$ scatter widely [1] because subtle differences in the experimental conditions (impurity on the surface, ill-controlled temperature, etc.) can drastically change the results. Thus, a more detailed investigation is necessary from various points of view.

Molecular dynamics (MD) computer simulation is free from such difficulties and is suitable for the study of these evaporation-condensation dynamics at a molecular level. With this technique, we can investigate the dynamics in the condition as close to the true liquid-vapor equilibrium as possible, which is not accessible with the usual experiments.

In Fig. 1, we show four types of molecular dynamics near the free liquid surface, which were observed during the simulation. The first three, i.e., evaporation, condensation, and self-reflection, are simple and can be regarded as unimolecular reactions, and the models which have been proposed to predict the condensation-evaporation rate already take these three dynamics into account [14]. However, the remaining "molecular exchange" is a rather complex event; vapor molecules colliding with the liquid surface drive other molecules out of the liquid. Apparently, this event is not a unimolecular process, and all evaporation-condensation models have neglected it.

![](./images/813085369993003009_3.jpg)

Fig. 1. Schematic figure of molecular dynamic processes near a free liquid surface.

![](./images/813085369993003009_4.jpg)

Fig. 2. Temperature dependence of the ratio of self-reflection, molecular exchange, total reflection, and the condensation coefficient for argon and water. The temperature $T$ is normalized with the experimental value of the vapor-liquid critical temperature $T_{\mathrm{c}}$. The range of statistical fluctuations in the simulation is about $\pm 5 \%$.

We have developed correlation function methods to estimate the number ratio of self-reflection to collision $\beta_{\text {self }}$ and the ratio of molecular exchange to collision $\beta_{\text {exch }}[5,6]$. The total reflection ratio is expressed as $\beta_{\text {total }} \equiv \beta_{\text {self }}+\beta_{\text {exch }}$, and the condensation coefficient is $\alpha \equiv 1 \beta_{\text {total }}$.

In Fig. 2, the results are plotted against the reduced temperature $T / T_{\mathrm{c}}$, where $T_{\mathrm{c}}$ is the vapor-liquid critical temperature. The $T_{\mathrm{c}}$ of the TIP4P model water used in our simulation is not known, so an experimental value of $T_{\mathrm{c}}=647.3 \mathrm{~K}$ is used, which may cause a slight shift in the abscissa. In the case of argon, the simulational result of $T_{\mathrm{c}}=150.7 \mathrm{~K}$ was used.

In the lower temperature region, the condensation coefficient of water is much smaller than that of argon. We obtained similar results for methanol and acetic acid [9], so this is considered to be a general tendency for associating fluids. The reason for small $\alpha$ for associating fluids is simple; the molecular exchange is much more important than the self-reflection for these fluids. Thus, we have to properly take this molecular exchange into account when constructing a condensation-evaporation model [8].

However, in the higher temperature region, even the $\alpha$ of argon quickly decreases due to the molecular exchange. As far as we know, there is no report (experimental or theoretical) on this strong temperature dependence of $\alpha$, and accurate experimental measurements in a wide temperature range are urgently required.

## 4. Liquid mixture

One of the experimental difficulties in measuring the condensation coefficient $\alpha$ comes from the surface contamination [1]. In particular, in the case of water, organic contaminants, e.g., oil and

![](./images/813085369993003009_5.jpg)

Fig. 3. A snapshot of aqueous methanol solution at $T = 400$ K. The methanol molecules are shown as thick lines. It is clear that methanol is dominant in the first layer of the surface.

surfactants, are strongly adsorbed on the surface, which can greatly affect the condensation-evapora- tion rate.

In this study, we examine an aqueous solution of methanol as a model system. A rather high temperature (400 K) is chosen in order to observe many events of water evaporation and condensa- tion.

A snapshot is shown in Fig. 3, and the density profile is in Fig. 4, where surface adsorption of methanol is clearly seen.

Using similar methods as described above, we estimate the self-reflection ratio $\beta_{\text{self}}$ and the molecular exchange ratio $\beta_{\text{exch}}$. The results are $\beta_{\text{self}} \simeq 16\%$ and $\beta_{\text{exch}} \simeq 14\%$. Comparing them with the values for pure water at the same temperature ( $\beta_{\text{self}} \simeq 6\%$ and $\beta_{\text{exch}} \simeq 64\%$), we conclude that the surface-adsorbed methanol layer strongly hinders both self-condensation and molecular exchange. Analysis in more detail, e.g., the possibility of molecular exchange between water and methanol, is under way.

![](./images/813085369993003009_6.jpg)

Fig. 4. Density profile of aqueous methanol solution. The existence of an absorbed methanol layer near the surface is apparent.

It would be interesting to investigate the aqueous solutions of an alcohol with a longer alkyl chain, because such "contaminant" is less soluble than methanol and may form a monolayer on the water surface; the evaporation-condensation of water through a monolayer has apparent practical impor- tance in many fields of engineering.

## 5. Gas absorption

The final topic is the gas absorption dynamics on liquid surfaces, which is one of the fundamental processes in chemical engineering. Moreover, the absorption mechanism of various gases ($\text{CO}_2$, $\text{SO}_2$, $\text{NO}_x$ etc.) on the surface of water has also recently become important in environmental and earth science. Therefore, we have studied the $\text{CO}_2$ + water and $\text{SO}_2$ + water systems at room temperature (300 K).

Fig. 5 shows snapshots for each system. Because $\text{CO}_2$ has a low solubility in water, almost all the $\text{CO}_2$ molecules exist in the vapor phase. On the other hand, nearly half the $\text{SO}_2$ molecules are in the liquid region, but interestingly, they sometimes form a weak self-assembly as shown in the snapshot.

![](./images/813085369993003009_7.jpg)

Fig. 5. Snapshots of the $\text{CO}_2$ + water system and the $\text{SO}_2$ + water system at $T=300$ K. The solute molecules are shown as thick lines.

![](./images/813085369993003009_8.jpg)

Fig. 6. Density profile of the $CO_{2}+$ water system and the $SO_{2}+$ water system.

Thus, in the density profile (Fig. 6), the $CO_{2}+$ water system hardly shows surface adsorption, while the $SO_{2}+$ water system has a strong surface adsorption; in the latter case, the density profile is asymmetric due to insufficient statistics.

Examples of molecular trajectories are shown in Fig. 7. Trajectory analysis shows that the ratio of self-reflection, defined similarly to the case of pure substances, is $70-80\%$ for the $CO_{2}+$ water

![](./images/813085369993003009_9.jpg)

Fig. 7. Some examples of molecular trajectories of the solute for the $CO_{2}+$ water and $SO_{2}+$ water systems.

system and 50-60% for the $\mathrm{SO}_{2}+$ water system. These values are much larger than those of pure substances (typically 10%), and thus, we conclude that vapor molecules of low solubility are more often reflected on the solution surface. At this temperature $(T=300 \mathrm{~K})$, water molecules rarely exist in the vapor phase, and no "molecular exchange" (exchange between the gas and the water) is observed.

In Fig. 7, we notice that the colliding gas molecule sticks to the surface for a while (typically 10 ps) and finally detaches from the surface (in most cases) or is absorbed into the liquid. This is the first time that this kind of migration has been observed. Analysis of this phenomenon from the viewpoint of energy transfer between the gas molecule and the substrate (liquid surface) is under way.

## 6. Summary

Molecular dynamics simulations can reveal various gas-liquid interphase transport phenomena at a microscopic level. In this paper, we have shown three examples, evaporation and condensation of liquid substances (pure and mixture systems) and gas absorption dynamics.

In the case of evaporation-condensation of pure liquids, the importance of molecular exchange phenomena was found. It is necessary to properly take into account both self reflection and molecular exchange for developing a microscopic model. For both simple and associating fluids, a strong temperature dependence of the condensation coefficient is predicted.

For the aqueous methanol solution, methanol adsorption on the surface is observed, and the adsorption layer hinders greatly both the self-condensation and molecular exchange.

MD simulations are also useful to investigate the gas absorption on a water surface, and calculations of the $\mathrm{CO}_{2}$ and $\mathrm{SO}_{2}$ cases show that the ratio of self-reflection is much larger than that for pure liquid systems. Migration of gas molecules before detachment is also found.

## 7. List of symbols

$J_{\text {coll }}$ flux of vapor molecule collision on liquid surface, given in Eq. (1)
$\alpha$ condensation coefficient
$\beta_{\text {self }}$ ratio of self reflection to $J_{\text {coll }}$
$\beta_{\text {exch }}$ ratio of molecular exchange to $J_{\text {coll }}$
$\beta_{\text {total }}$ ratio of total reflection to $J_{\text {coll }}$

## Acknowledgements

The author greatly appreciates the collaborations with Prof. Y. Kataoka (Hosei University), Prof. S. Fujikawa (Toyama Prefectural University), and Mr. K. Yasuoka (Nagoya University). Discussions with Prof. S. Komori (Kyushu University) and Prof. S. Koda (University of Tokyo) are also acknowledged. A part of this work has been financially supported in part by the Grants-in-Aid for Scientific Research on Priority Area (Micro Heat Transfer in Materials Processing) from the Ministry of Education, Science and Culture, Japan.

## References

[1] H.K. Cammenga, in E. Kaldis (Ed.), Current Topics in Materials Science 5, North-Holland, Amsterdam, 1980, pp. 335-446.

[2] S. Fujikawa, M. Kotani and H. Sato, Proc. ASME/JSME Thermal Engineering Joint Conf., Lahaina, USA, March 19-24, 1995, ASME, New York, (1995) H0933B:454-458.

[3] S. Fujikawa, M. Kotani and H. Sato, Therm. Sci. Eng., 3 (1995) 45-50.

[4] K. Yasuoka, M. Matsumoto and Y. Kataoka, Bull. Chem. Soc. Jpn., 67 (1994) 859-862.

[5] K. Yasuoka, M. Matsumoto and Y. Kataoka, J. Chem. Phys., 101 (1994) 7904-7911.

[6] M. Matsumoto, K. Yasuoka and Y. Kataoka, J. Chem. Phys., 101 (1994) 7912-7917.

[7] K. Yasuoka, M. Matsumoto and Y. Kataoka, Proc. ASME/JSME Thermal Engineering Joint Conf., Lahaina, USA, March 19-24, 1995, ASME, New York, H0933B:459-464.

[8] M. Matsumoto, K. Yasuoka and Y. Kataoka, Proc. ASME/JSME Thermal Engineering Joint Conf., Lahaina, USA, March 19-24, 1995, ASME, New York, H0933B:465-470.

[9] . Matsumoto, K. Yasuoka and Y. Kataoka, Therm. Sci. Eng., 3 (1995) 27-31.

[10] W.L. Jorgensen, J. Am. Chem. Soc, 103 (1981) 335-340.

[11] W.L. Jorgensen, J. Phys. Chem., 90 (1986) 1276-1284.

[12] C.S. Murthy, K. Singer and I.R. McDonald, Mol. Phys., 44 (1981) 135-143.

[13] S. Hayashi, M. Oobatake, T. Ooi and K. Machida, Bull. Chem. Soc. Jpn., 58 (1985) 1105-1108.

[14] E.M. Mortensen and H. Eyring, J. Chem. Phys., 64 (1960) 846-849.