Roberto R. de Avillezⁱ, André Luiz V. da Costa e Silvaⁱⁱ, Ana Rosa F. A. Martinsⁱ,
Fernando C. Rizzo Assunçãoⁱ

ⁱPontifícia Universidade Católica, Rio de Janeiro, RJ-Brazil
ⁱⁱUniversidade Federal Fluminense, Volta Redonda, RJ-Brazil

# The effect of alloying elements on constrained carbon equilibrium due to a quench and partition process

The model proposed by Speer et al. to calculate the constrained carbon equilibrium is expanded to include any number of substitutional solutes and coded with the MatLab and Thermo-Calc programs. This model is used to evaluate the effect of Al, Cr, Cu, Mn, Mo, Ni and Si solutes on the final austenite carbon concentration of ternary Fe–X–C alloys. Comparison is also made with the carbon concentration measured experimentally in some Transformation Induced Plasticity steels.

**Keywords:** Steels; Austempering; Thermodynamics; Constrained carbon equilibrium

## 1. Introduction
Speer et al. [1] recently provided a model for the partition of carbon between quenched martensite and retained austenite that has important consequences in some thermomechanical processes applied to steel. They even proposed a new process concept [2] which they called quenching and partitioning, or Q&P. This process results from the quenching of austenite into a region below the martensite, or bainite, start temperatures, followed by a partition treatment that occurs without the partitioning of the substitutional elements between the martensite and the austenite, a reaction named constrained carbon equilibrium, CCE [2, 3]. Upon a subsequent quenching to room temperature, this process will thus provide carbon-depleted martensite along with carbon-enriched retained austenite, stabilized by the carbon enrichment that occurs during the partitioning stage of the process.

Predicting the partition of carbon is essential to design steel compositions and treatment conditions that will result in the best combinations of mechanical properties. Alloying elements are known to affect the ferrite and the austenite carbon equilibrium concentration. However, during the quench and partition process, the substitutional elements are not allowed to migrate over long distances and the equilibration condition is constrained by the constant amount of substitutional atoms in each phase. This condition must affect the carbon chemical potential and, therefore, it might be important for the CCE in alloyed steels. Since no other study on the effect of alloying elements is known, the model proposed by Speer et al. [1] is expanded to include any number of substitutional solutes and coded with the MatLab [4] and the Thermo-Calc [5] programs. This model is used to evaluate the effect of Al, Cr, Cu, Mn, Mo, Ni and Si solutes on the final austenite carbon concentration of ternary Fe–X–C alloys. Comparison is also made to the carbon concentration measured experimentally in some alloys.

## 2. Constrained carbon equilibrium
The assumptions for modeling the final equilibrium condition during the quench and partition process proposed by Speer et al. [1, 2] are: 1) all long distance diffusion transformations, or reactions, such as bainite formation and cementite or transition carbide precipitation, are suppressed during the quenching and tempering processes; 2) the austenite/martensite interface remains immobile during the tempering (partitioning) stage of the process; and 3) the carbon diffuses until an equilibrium is reached between the martensite and the austenite phases, with carbon chemical potential uniform throughout the system [1]. Therefore, the model predicts the final carbon concentration in the austenite and martensite. It must be emphasized that the substitutional solute and solvent atoms will not necessarily have uniform chemical potential throughout the system.

The program input data are the chemical composition of the iron alloy (steel), the volume fraction of austenite at the end of the quenching stage of the process, the partitioning heat treatment temperature and a convenient thermodynamic database. The martensite is thermodynamically modeled as ferrite phase. The volume fraction of austenite is converted to molar fraction and the total number of moles of atoms in ferrite and in austenite are saved for later calculations. The carbon chemical potential for the austenite and ferrite phases are evaluated as a function of the number of moles of carbon and the constrained equilibrium condition is determined from the intersection of the two carbon chemical potential curves. The output is the carbon chemical potential, the carbon concentration in austenite and ferrite, and the molar fraction of austenite (including the carbon). The program is written in the MatLab language [4] and Thermo-Calc MatLab Toolbox [6]. The database used was the TCFE3 [7].

### 3. Results and discussion

To evaluate the partition of carbon, several simulations were initially performed for a simple Fe-0.5 % C alloy, with no alloying elements. This reproduces the first calculation presented by Speer [1]. Figure 1 shows the carbon chemical potential for two different conditions: The first condition, termed unconstrained equilibrium, is calculated in the absence of carbide precipitation, considering that the amounts of austenite and ferrite are not fixed, and only carbon can move between these phases. This is equivalent to a metastable equilibrium with respect to carbides and, since there are no substitutional elements in this case, also to a typical "paraequilibrium" calculation between austenite and ferrite [8]. The second condition is the constrained carbon equilibrium, as defined by Speer et al. [1]. For this condition calculations are performed for three volume fractions of austenite: 10, 20 and 50 %. It is observed that in the constrained carbon equilibrium case the carbon chemical potential depends strongly on the amount of retained austenite, in addition to depending on the temperature.

Figure 2 shows that the carbon concentration in the austenite under the conditions of Fig. 1, compared to the $T_0$ concentration line, the locus point where ferrite and austenite phases have the same Gibbs molar energy and the same composition. It is evident that both under unconstrained equilibrium and under constrained carbon equilibrium the austenite carbon concentration may reach values well above the carbon concentration for the $T_0$ line. The $T_0$ line is considered the maximum carbon concentration, at a given temperature, that will allow austenite decomposition via diffusionless transformation, such as bainite or martensite growth from an austenite matrix with the same carbon concentration. So if during an austempering process with bainite or martensite formation, only diffusionless transformations occurred, one would not expect to find any austenite with carbon concentration greater than the $T_0$ composition.

Furthermore, the results for a 50 % volume fraction of austenite in Fig. 2 indicate that below $453\,^\circ\text{C}$, the application of a quench and partition process to a 0.5 % C alloy may result in an austenite with carbon concentration lower than the value estimated by the $T_0$. Indeed, if the 0.5 % C alloy is quenched to $177.6\,^\circ\text{C}$, which corresponds to approximately 50 % martensite formation using the Koistinen and Marburger expression for retained austenite [9] and the Victor et al. expression for martensite start temperature [10], and then heat treated at higher temperature but below $453\,^\circ\text{C}$ for carbon partition, the carbon content in the austenite will reach about 1 %, a value below the $T_0$ line. So, the quench and partition process may also lead to an austenite with carbon concentration lower than the values given by the unconstrained equilibrium or the $T_0$ line.

Figure 2 is identical to Figure 6 in Speer's article [1] but for the addition of the unconstrained equilibrium and the $T_0$ lines which were drawn to emphasize the very large enrichment of carbon that may result from this process, or similar heat treatments, for example, the austempering of TRIP (TRansformation Induced Plasticity) steels [11] and ductile cast iron [12]. However, the very large carbon enrichment will only be possible if the stable carbide phases do not precipitate during the typical heat treatment times, or the austenite phase fraction does not change by either growth or dissolution. So there will be a competition between the carbon diffusion toward the austenite and carbide precipitation, or between the carbon diffusion and the austenite/ferrite interface movement. Indeed, these parallel processes may even start during the quenching process.

The effect of alloying elements will be discussed for ternary Fe–X–C alloys with 10 % austenite and the addition of 1 % X (mass) and 0.5 % C to provide a comparison. The amount of austenite is consistent with typical retained austenite measurements for TRIP steels. Figure 3 shows that the addition of austenite stabilizers, Cu, Mn and Ni, barely changes the carbon concentration in austenite for the constrained equilibrium. However, some ferrite stabilizers show a definite effect as presented in Fig. 4. Al, Mo and Cr reduce the carbon concentration of the austenite, P increases the carbon concentration and Si has no measurable effect. It is interesting to observe that Cr and Mo have the same overall effect. The effects presented in Fig. 4 are potential effects since the addition of 1 % Cr, or Mo, may result in the precipitation of carbides depending on the partition time, while 1 % of P is outside the usually accepted

![](./images/811871692157616129_1.jpg)

Fig. 1. Chemical potential for constrained carbon equilibrium and unconstrained equilibrium between ferrite and austenite for a Fe-0.5 % C alloy.

![](./images/811871692157616129_2.jpg)

Fig. 2. Constrained carbon equilibrium for different austenite fractions of Fe-0.5 % C alloy superimposed with the $T_0$ and $A_3$ lines. This result was obtained with the proposed program. It reproduces Speer's calculation and allows checking of the program.

---

Int. J. Mat. Res. (formerly Z. Metallkd.) 99 (2008)

maximum concentration for this element in steels. Figures 3 and 4 show that the thermodynamic effect of substitutional alloying elements on the maximum carbon concentration in ternary alloys is small. Much higher alloy content than the simple ternary alloys presented in this article would be necessary to have a significant effect based on thermodynamics. Indeed, the steels employed by Speer and co-workers [1, 2] and the steels [13–15] presented in Table 1 do have large amounts of alloying elements. Therefore, one may infer that the observed experimental data are probably related to kinetics effects and concurrent phase transformations, as mentioned before. Nonetheless, the extension of the Constrained Carbon Equilibrium calculations provides an estimate of the maximum carbon concentration that could be reached during a quench and partition process in alloyed steels.

The proposed program is used to estimated the carbon content of retained austenite for some TRIP steels as shown in Table 1. This special class of steel has attracted growing interest because of its improved plasticity with very high strength. These steels depend on the presence of a controlled amount of retained austenite that may transform into martensite during plastic deformation. Their processing includes an intercritical heat treatment in the austenite–ferrite field of the phase diagram which will result in a two phase matrix, with carbon enriched austenite. The steel is then quenched to an austempering temperature where partial transformation of the austenite into either martensite or bainite may occur and is kept at this temperature for a short period of time, sufficient to allow carbon to diffuse from the ferrite into the retained austenite. Therefore, the austenite is further enriched in carbon. This enrichment should be sufficient to lower the $M_{\text{s}}$ temperature to below room temperature, stabilizing the austenite against cooling to room temperature, but allowing the martensite transformation during the plastic deformation process necessary to reach the final shape. The intercritical treatment temperature and time is assumed to be high enough to allow the carbon to reach a paraequilibrium in the austenite–ferrite system but it may not be sufficient to allow the unconstrained equilibrium due to the slower diffusion of substitutional solutes. Nonetheless, in the following examples, the amount of austenite and its concentration were calculated for the unconstrained equilibrium condition and these values were used to determine the maximum carbon content for the constrained carbon equilibrium. The results in Table 1 show that the experimentally determined carbon concentrations (Exp) approach the values calculated for the constrained

![](./images/811871692157616129_3.jpg)

Fig. 3. The effect of Cu, Mn and Ni on the constrained carbon equilibrium for Fe-1% X-0.5% C alloys with 10% of retained austenite.

![](./images/811871692157616129_4.jpg)

Fig. 4. The effect of Al, Cr, Mo, Si and P on the constrained carbon equilibrium for Fe-1% X-0.5% C alloys with 10% of retained austenite.

Table 1. Calculated carbon content for the constrained carbon equilibrium (CCE) in the retained austenite in some TRIP steels compared with the experimentally determined values (Exp). $V\gamma$ is the experimental volume fraction of retained austenite, $T_{\text{Zero}}$ is the carbon concentration when austenite and ferrite have the same Gibbs energy and Para is the carbon concentration under paraequilibrium condition.

<table>
<thead>
<tr>
<th rowspan="2">Steel Composition (%)</th>
<th rowspan="2">Processing</th>
<th colspan="6">Carbon Concentration in the Retained Austenite (%)</th>
</tr>
<tr>
<th>$V\gamma$</th>
<th>$T_{\text{Zero}}$</th>
<th>Exp</th>
<th>CCE</th>
<th>Para</th>
<th>Ref.</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.19C 1.57Mn 1.46Si 0.06Al</td>
<td>$I$ 800 $A$ 400–4 min</td>
<td>9.7</td>
<td>1.00</td>
<td>1.83</td>
<td>1.88</td>
<td>3.48</td>
<td>[13]</td>
</tr>
<tr>
<td></td>
<td>$I$ 770 $A$ 400–4 min</td>
<td>9.9</td>
<td>0.97</td>
<td>1.56</td>
<td>1.85</td>
<td>3.42</td>
<td>[13]</td>
</tr>
<tr>
<td></td>
<td>$I$ 770 $A$ 450–4 min</td>
<td>10.2</td>
<td>0.81</td>
<td>1.52</td>
<td>1.79</td>
<td>2.92</td>
<td>[13]</td>
</tr>
<tr>
<td>0.31C 1.57Mn 0.34Si 1.23Al</td>
<td>$I$ 800 $A$ 400–4 min</td>
<td>13.3</td>
<td>1.04</td>
<td>1.83</td>
<td>2.16</td>
<td>3.46</td>
<td>[13]</td>
</tr>
<tr>
<td></td>
<td>$I$ 770 $A$ 400–4 min</td>
<td>12.1</td>
<td>1.02</td>
<td>1.83</td>
<td>2.40</td>
<td>3.40</td>
<td>[13]</td>
</tr>
<tr>
<td></td>
<td>$I$ 770 $A$ 450–4 min</td>
<td>13.3</td>
<td>0.86</td>
<td>1.79</td>
<td>2.19</td>
<td>2.90</td>
<td>[13]</td>
</tr>
<tr>
<td>0.11C 1.53Mn 1.50Si</td>
<td>$I$ 750 $A$ 450–1.5 min</td>
<td>10.8</td>
<td>0.77</td>
<td>0.83</td>
<td>1.50</td>
<td>2.80</td>
<td>[14]</td>
</tr>
<tr>
<td>0.218C 1.539Mn 0.267Si 1.750Al</td>
<td>$I$ 840 $A$ 400–0.5 min</td>
<td>8.8</td>
<td>1.07</td>
<td>0.6–1.3</td>
<td>2.12</td>
<td>3.44</td>
<td>[15]</td>
</tr>
</tbody>
</table>

$I$ – Intercritical temperature ($^\circ$C); $A$ – Austempering temperature ($^\circ$C)

![](./images/811871692157616129_5.jpg)

Fig. 5. Gibbs energy diagram as a function of carbon concentration related to bainite nucleation and growth from an austenite matrix for an Fe-1Si alloy. The silicon content in the ferrite and austenite phases is kept fixed. The dashed straight lines may be used to determine the chemical potential for carbon in austenite (point 4) and ferrite (point 3).

carbon condition (CCE) for the longer austempering times but are much smaller than those for the paraequilibrium condition (Para). These results suggest that the final equilibrium condition in these TRIP alloys are more closely related to the CCE condition than the paraequilibrium condition.

Further, the carbon content due to the CCE process is usually greater than the values associated with the $T_{0}$ condition, which shows that the bainite growth (the austenite in these steels transforms mostly to bainite) was not restricted by the condition of equal Gibbs energy of austenite and ferrite.

It must be pointed that a common argument that justifies incomplete bainitic transformation is a source of confusion with what happens during the quenching and partitioning process. If one assumes that bainite is formed without solute redistribution it should never be possible to form bainite from austenite richer in carbon than the $T_{0}$ composition ($T_{0}$ in Fig. 5). Furthermore, if the bainite forms from an austenite lower in carbon than this composition (1 in Fig. 5), and then rejects the excess carbon to the remaining austenite, a condition of no further bainite nucleation will be reached when the austenite composition reaches the $T_{0}$ point in Fig. 5. However, there is no reason why the carbon enrichment of austenite by diffusion must stop before the carbon chemical potential is the same for both phases. So, should there still be a difference in carbon potential between the austenite and the ferrite, only the mass balance will limit the extent of carbon diffusion from ferrite to austenite, as the interface is not mobile and provided that there is sufficient carbon mobility. Even when carbon diffusion continues to position 3 in the figure, for instance, there is still driving force for the partitioning of carbon to continue and to form austenite that is richer in carbon than the $T_{0}$ composition until the constrained carbon equilibrium condition is reached. Hence, even though the bainite nucleation and growth depend on the driving force present while the austenite carbon concentration is below the $T_{0}$ line for the quenched temperature, constrained carbon equilibrium may be reached whenever the temperature and time is enough for carbon diffusion. The data on Table 1 suggests that 4 min were enough to reach the CCE condition but the smaller times were not. This carbon redistribution has been observed before also in the context of bainite formation [16].

The larger carbon content related to the paraequilibrium condition results from the smaller fraction of austenite, since the austenite/ferrite interface must be mobile under this condition. Carbon concentrations for the shorter austempering times are smaller than the value calculated from the constrained carbon equilibrium probably due to the shorter diffusion times which may not be enough to reach the equal carbon chemical potential condition.

## 4. Conclusion

A simple computer program is developed to extend the Speer et al. model [1,2] and estimate the effect of alloying elements on the carbon content of austenite under constrained carbon equilibrium. The effect is usually small for most common alloying elements considered individually. Aluminum and phosphorous are the elements with the larger effect. Silicon has almost no effect from the thermodynamic equilibrium standpoint, so its effect must be mostly related to the kinetics of the phase transformations, in particular, the effect on carbide precipitation.

Experimentally determined carbon concentrations in retained austenite for some TRIP steels are closer to the values estimated for the constrained carbon equilibrium than for the values estimated based on the assumption of paraequilibrium or the $T_{0}$ values.

The authors acknowledge the support for this research by the Conselho Nacional de Desenvolvimento Científico e Tecnológico, CNPq, and Fundação de Amparo à Pesquisa do Estado do Rio de Janeiro, FAPERJ.

### References

[1] J.G. Speer, B.C. de Cooman, J.G. Schroth: Acta Mater. 51 (2003) 2611. http://dx.doi.org/10.1016/S1359-6454(03)00059-4

[2] J.G. Speer, D.V. Edmonds, F.C. Rizzo, D.K. Matlock: Current Opinion in Solid State and Materials Science 8 (2004) 219. http://dx.doi.org/10.1016/j.cossms.2004.09.003

[3] H. Hillert, J. Agren: Scripta Mater. 50 (2004) 697. http://dx.doi.org/10.1016/j.scriptamat.2003.11.020

[4] MATLAB, version 6.5, The MatWorks, Inc. (2002).

[5] J.O. Andersson, T. Helander, L. Höglund, P.F. Shi, B. Sundman: Calphad 26 (2002) 273. http://dx.doi.org/10.1016/S0364-5916(02)00037-8

[6] L. Höglund: TC MATLAB Toolbox Programer's Guide and Examples, version 4.00, Foundation of Computational Thermodynamics, Stockholm (2006).

[7] Thermo-calc Software (TCS) Steels/Fe-alloys database, version 3, TCAB, Stockholm (2003).

[8] M. Hillert: Jernkont Ann 136 (1952) 25.

[9] D.P. Koinstinen and R.E. Marburger: Acta Metall. 7 ( 1959 ) 59.

[10] M. Victor Li, D.V. Niebur, L.L. Meekisho, D.G. Alteridge: Metall. Mater. Trans. B 29 (1998) 661.

[11] N.H. van Dijk, A.M. Butt, L. Zhao, J. Sietsma, S.E. Offerman, J.P. Wright, S. van der Zwaag: Scripta Mater. 53 (2005) 5439. http://dx.doi.org/10.1016/j.actamat.2005.08.017

[12] M.A. Yescas, H.K.D.H. Bhadeshia: Materials Science and Engineering A 333 (2002) 60. http://dx.doi.org/10.1016/S0921-5093(01)01840-8

[13] M. De Meyer, D. Vandershueren, B.C. De Cooman: ISIJ International 39 (1999) 813.

R. R. de Avillez et al.: The effect of alloying elements on constrained carbon equilibrium due to quench

[14] E. Girault, P. Jacques, P. Ratcher, J. Van Humbeeck, B. Verlin- den, A. Aernoudt: Mat. Sci. Engineering A 273 (1999) 471.

[15] E. Jimenez-Melero, N.H. van Dijk, L. Zhao, J. Sietsma, S. Offer- man, J.P. Wright, S. van der Zwaag: Scripta Materialia 56 (2007) 421. http://dx.doi.org/10.1016/j.scriptamat.2006.10.041

[16] F.G. Caballero, H.K.D.H. Bhadeshia, K.J.A. Mawella, D.G. Jones, P. Brown: Materials Science and Technology 18 (2002) 279.

(Received November 17, 2007; accepted August 27, 2008)

## Bibliography

DOI 10.3139/146.101764
Int. J. Mat. Res. (formerly Z. Metallkd.)
99 (2008) 11: page 1280–1284
© Carl Hanser Verlag GmbH & Co. KG
ISSN 1862-5282

### Correspondence address
Prof. Dr. Roberto R. de Avillez
Pontifícia Universidade Católica
Rua Marquês de São Vicente, 225 – DCMM
22453-900 Rio de Janeiro, RJ-Brazil
Tel.: +55 21 3527 1250
Fax: +55 21 3527 1236
E-mail: avillez@puc-rio.br

You will find the article and additional material by enter- ing the document number MK101764 on our website at
www.ijmr.de

---

1284
Int. J. Mat. Res. (formerly Z. Metallkd.) 99 (2008)