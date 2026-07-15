# Ab initio study of diffusion of hydrogen, silver and lithium in PbS and $\mathbf{Ag_2S}$

Ricardo R. Oliveira, Bruno N.C. Tenorio, Alexandre B. Rocha*

UFRJ - Universidade Federal do Rio de Janeiro, Instituto de Química, Av. Athos da Silveira Ramos, 149, Rio de Janeiro, RJ 21941-909, Brazil

---

## ARTICLE INFO

**Keywords:**
Diffusion process
Diffusion coefficient
Lead sulfide
Silver sulfide
DFT

---

## ABSTRACT

Lead and silver sulfides are materials with diverse technological applications, such as photovoltaic dispositives, electrodes and catalysts. More recent applications in the formation of quantum dots and catalysts synthesis for hydrogen evolution reactions involves these sulfides and some similar compounds. It is well known that defects, and consequently the diffusion process, can change some properties and performances of such materials. Herein, a study of defect formation and ionic diffusion process were performed in PbS and $\text{Ag}_2\text{S}$ lattice structure. The activation energies for diffusion of $\text{Ag}^+$, $\text{Li}^+$, and $\text{H}^+$ in PbS and $\text{Ag}_2\text{S}$ lattices were calculated at the DFT level and diffusion coefficients were estimated within the Arrhenius approximation. Pb-doped $\text{Ag}_2\text{S}$ exhibited a very small activation energy and an anomalous high diffusion coefficient for $\text{Ag}^+$ diffusion, which is in good agreement with experimental data. Less evident is the fact that $\text{Li}^+$ present lower diffusion coefficients than $\text{Ag}^+$. For $\text{H}^+$ diffusion in PbS lattice, the process is completely different. The hydrogen moves over the lattice from a sulfur site to the other, apparently cleaving and forming H-S bonds. The present work can provide more understanding of the features of defect formation and solid state ionic diffusion mechanism in sulfides from an atomic perspective. Hopefully, this results can help experimentalists in the development of more efficient materials for some important technological applications.

---

## 1. Introduction

Silver ($\text{Ag}_2\text{S}$) and lead (PbS) sulfide-based materials exhibit a wide range of applications, being the focus of several types of research in different areas. One of the first applications of these materials was as ion-selective electrodes in the 70's [1-4]. Ion-selective electrodes are formed by polycrystalline membranes synthesized out of water in-soluble salts as precursors. This type of electrodes exhibits high selectivity to Pb(II) cation [1-4]. Moreover, sensors based on chalcogenide glasses of $\text{Ag}^+$ and $\text{Pb}^{2+}$ were proposed due to their stability in strong acidic and corrosive media as well as due to their higher selectivity compared to conventional crystalline counterparts [5]. Recently, PbS-based electrodes were prepared in different ways, with organic compounds like crown ethers [6] or by electro deposition on stainless steel [7]. The same has been reported for $\text{Ag}_2\text{S}$, prepared by chemical deposition using thiourea as a sulfur source [8].

Over the years, various synthetic techniques were developed for specific lead or silver sulfide structures and properties, revealing the increasing interest in this type of material [9-17]. Moreover, recent interest in these sulfides has also arisen with applications as quantum dots semiconductors [18-31] or in photovoltaic devices [19-21,24,25,32-35].

In 2017, a PbS nanoparticle deposited on roll-graphene oxide electrode was synthesized with photocatalytic properties for photoelectrochemical hydrogen generation [36]. As well as lead sulfide, silver sulfide based catalysts have shown promising electrocatalyst properties [37,38]. Heterostructures of $\text{Ag}_2\text{S}/\text{Ag}$ were synthesized by different groups [38-41] and showed an efficient catalytic activity in the $\text{H}_2$ evolution reaction [38]. Polycrystalline Ag and $\text{Ag}_2\text{S}$ nanofibers were synthesized with general sacrificial template strategy. Further, an electronic device with $\text{Ag}_2\text{S}/\text{Ag}$ nanofibers was built with appreciable diffusion of $\text{Ag}^+$ cation [42]. In another interesting paper, a metallic Ag-$\text{Ag}_2\text{S}$-Ag nanojunctions were built for a simplified fabrication of atomic-scale, robust planar $\text{Ag}_2\text{S}$ memory cells [43]. Recently, a silver ion-selective electrode was presented based on chalcoholide glass membranes containing $\text{Ag}_2\text{S}$. The addition of AgCl to the membrane increases the conductivity of the media [44].

A recent application of silver and lead sulfide is in the controlled synthesis of $\text{PbS}/\text{Ag}_2\text{S}$ films with modified transport properties, namely diffusion of impurity species [45,46]. Lead sulfide with silver atomic impurities were synthesized by different groups and exhibited an effective diffusion of atomic impurities [47-52].

At atomic scale, diffusion process in these sulfides is poorly described. Therefore, ab initio studies can provide a comprehensive

---

* Corresponding author.
E-mail address: rocha@iq.ufrj.br (A.B. Rocha).

https://doi.org/10.1016/j.commatsci.2019.04.046
Received 1 November 2018; Received in revised form 15 April 2019; Accepted 26 April 2019
0927-0256/ © 2019 Elsevier B.V. All rights reserved.

![](./images/812776705449000961_1.jpg)

Fig. 1. First (A) and last (B) structures in the diffusion pathway of $Ag^{+}$ in PbS lattice. Gray atoms are Pb, yellow atoms are S, and blue atoms are Ag atoms.

analysis of this type of process. To the best of our knowledge, there is only one paper which has studied the $Ag^{+}$ diffusion in silver sulfide lattice [53].

Ab initio studies, at DFT level, of diffusion processes were con- ducted in other systems, such as diffusion of carbon, nickel and hy- drogen atoms in nickel lattice [54,55]; transition metals, hydrogen and oxygen atoms in cobalt lattice [56-58]; hydrogen, boron, carbon, ni- trogen and oxygen atoms in aluminum lattice [59]; arsenic atom in GaAs [60], and noble metal atoms in $Mo_{2}S$ monolayer [61], proving to be a powerful tool for the study of this type of process.

Despite the large number of publications focused on $PbS/Ag_{2}S$, there is no systematic study of impurities diffusion with DFT calcula- tions in these two sulfides. Herein, we approach this problem by using DFT calculations in both sulfide structures with impurities of silver, lead, hydrogen and lithium atoms. We also report the estimated diffu- sion coefficient by an Arrhenius form, based on transition state theory, as done by Liu et al. [58].

Silver diffusion has many applications in materials based on PbS/ $Ag_{2}S$ polycrystalline films [45,46] for which diffusion coefficients were measured by different groups [62-64]. Hydrogen diffusion, on the other hand, is relevant due to applications in catalysis [36-38,65] where diffusion from bulk to surface is essential at the final stage of the hy- drogenation reaction [65]. Lithium diffusion also play a central role in applications of solid-state electrodes based on lithium sulfides [66]. Diffusion coefficients for lithium self-diffusion [67], for diffusion in $TiO_{2}$ [68] and for diffusion in silicon [69,70] and carbon [71,72] based materials are also available in the literature.

In the present work, we have conducted a DFT study of diffusion of $Ag^{+},Li^{+}$, and $H^{+}$ species in PbS and $Ag_{2}S$ lattices. An atomic view of diffusion mechanism can be inferred from the present calculations. Activation energies and diffusion coefficient were obtained from them and the results are in good agreement with the available experimental data.

## 2. Computational details

All calculations were performed within the Density Functional Theory (DFT), with PBE [73] functional in a plane-waves basis set, defined by a 30 Ry energy cutoff. Since the predominant interactions are electrostatic, corrections for Van der Waals interaction were not considered. The pseudo-potential method was used within Vanderbilt's ultrasoft approximation scheme [74]. Integration over the First Bril- louin Zone was done by the Monkhorst-Pack [75] method in a $3×3×3$ k-point mesh for silver and lead sulfide unit cells as well as for lead sulfide supercells. For silver sulfide supercell the k-point mesh was $2×2×2$. All diffusion pathways were obtained by the Climbing image-nudged elastic bands method (CI-NEB) [76,77]. The first and last images are minimum in the potential energy surface and, accordingly, were kept fixed. All calculations were done at Quantum Espresso suite of programs [78].

### 2.1. PbS supercell

Lead sulfide, PbS, also known as galena has the face-centered cubic (FCC) structure. Our optimized lattice parameter was $5.936\AA$, which is in good agreement with experimental value of $5.93\AA$ [79].

For the diffusion pathways, a supercell was constructed by ex- panding the unitary FCC cell two times in each direction, resulting in a 64-atom supercell. This supercell is chosen as a compromise of accuracy and computational cost. A larger cell would certainly be more re- presentative of the situation but it is impractical due to computational cost, for the time being. To create a defect and maintain the neutrality in the PbS lattice, one lead atom was removed and two impurity silver atoms were added, one in an interstitial position, and the other in the previous lead site with a minimal distance of $13\AA$ between impurity atoms along the diffusion path. The two structures were optimized with impurity atoms in equivalent neighboring positions without changing the galena lattice parameter. The first and final structures of diffusion pathway are represented in Fig. 1, and discussed below, for $Ag^{+}$ dif- fusion. Another representation for the first and last structures in the diffusion pathway is presented in Fig. 1S of the Supporting Information (SI). Minimum energy path and activation energy were obtained with CI-NEB method for the diffusion pathways between the equivalent in- terstitial positions.

### 2.2. $Ag_{2}S$ supercell

Our optimized lattice parameters for monoclinic silver sulfide, $Ag_{2}S$, also known as acanthite, were $a=4.25\AA,b=7.06\AA,c=9.59\AA$ and $\beta=124.95^{\circ}$. The parameters are in good agreement with experimental data, $a=4.231\AA,b=6.93\AA,c=9.526\AA$ and $\beta=125.48^{\circ}$ [80].

For diffusion pathway calculations, a supercell was constructed by expanding the monoclinic unit cell two times in each direction, arriving at a 96-atom supercell. First, a neutral supercell was constructed by removing two silver atoms and adding one lead atom to one of the vacant positions. Consequently, the resulting structure presents a va- cant site. In Fig. 2 we present the first and the last optimized structures of the diffusion pathway for $Ag^{+}$ in Pb-doped $Ag_{2}S$ lattice. Another representation with fewer atoms is presented in Fig. 3S of SI, in order to make the diffusion path more explicit. The distance between the lead atom and the nearest vacancy is $11.4\AA$. The diffusion path of the silver ion from the interstitial position to the neighboring vacant site was obtained.

Furthermore, a system with a Frenkel-type defect has been proposed

![](./images/812776705449000961_2.jpg)

Fig. 2. First (A) and last (B) structures in the diffusion pathway of $Ag^{+}$ in a Pb-doped $Ag_{2}S$ lattice. Gray atoms are Ag, yellow atoms are S, red atom is Pb and blue is the Ag diffusing atom. Dashed line represents Ag atom vacancy and red arrow indicates the direction of diffusion.

in which one silver atom was displaced at an interstitial position in the $Ag_{2}S$ supercell.

For cases involving other migrating species, the same unit cells were used, by substitution of $Ag^{+}$ by $H^{+}$ or $Li^{+}$. The structures with impurity atoms at the interstice and at the lattice position were optimized and minimum energy paths and activation energies were obtained. In Fig. 3 the first and the final structure of the diffusion pathway were represented for the Ag impurity case. Another representation with fewer atoms is also presented in Fig. 2S of SI.

For all diffusion pathways studied in this work, the first and the final optimized structures are presented in SI.

### 2.3. Diffusion coefficient calculation

The diffusion coefficients were calculated by the expression presented by Liu et al. [58],

$$
D=l\left(\frac{2 E_{a}}{m}\right)^{1 / 2} \times \exp \left(-\frac{E_{a}}{k_{B} T}\right), \tag{1}
$$

where $l$ is the diffusion distance translated by the atom, $E_{a}$ is the activation energy for the diffusion process and $k_{B}$ is the Boltzmann constant, $m$ is the mass of the diffusing atom and $T$ is the temperature.

They have based their approach on the transition state description of the jump probability of an individual atom and on some additional approximations due to Kutner [81], Wert and Zener [82,83]. See those paper for details. The working equation for the jump rate is

$$
\Gamma=\frac{1}{l}\left(\frac{2 E_{a}}{m}\right)^{1 / 2} \times \exp \left(-\frac{E_{a}}{k_{B} T}\right) \tag{2}
$$

## 3. Results and discussion

### 3.1. Lead sulfide

Diffusion pathways had the same profile for diffusion of $Li^{+}$ and $Ag^{+}$ in PbS lattice. The activation energy for silver was 0.54 eV and for lithium was 0.76 eV. Minimum energy path (MEP) obtained with CI-NEB method for $Ag^{+}$ and $Li^{+}$ diffusion in PbS are shown in Figs. 4 and 5, respectively. The reaction path is described as a function of the diffusion distance.

Diffusion coefficient for $Li^{+}$ was $2.26 \times 10^{-15} \mathrm{cm}^{2} \mathrm{s}^{-1}$ which is lower than the diffusion coefficient for $Ag^{+}$, which was $1.80 \times 10^{-13} \mathrm{cm}^{2} \mathrm{s}^{-1}$. Even the $Li^{+}$ ion being smaller than the $Ag^{+}$, a higher activation energy was obtained for $Li^{+}$ and, as result, our calculations indicates that $Ag^{+}$ diffuses more easily than $Li^{+}$ in PbS lattice. There is no diffusion coefficients available in the literature for diffusion of $Li^{+}$ in PbS. Consequently, we can only compare the order of magnitude of this coefficient with other known values for $Li^{+}$ diffusion in different lattices. The diffusion coefficients are similar to $Li^{+}$ diffusion in anatase ($TiO_{2}$), varying from $10^{-12}$ to $10^{-17} \mathrm{cm}^{2} \mathrm{s}^{-1}$ [68].

![](./images/812776705449000961_3.jpg)

Fig. 3. First (A) and last (B) structures in the diffusion pathway of $Ag^{+}$ in $Ag_{2}S$ lattice. Gray atoms are Ag, yellow atoms are S, and blue is the Ag diffusing atom. Dashed line represents Ag atom vacancy and red arrow indicates the direction of diffusion.

![](./images/812776705449000961_4.jpg)

Fig. 4. Diffusion pathway of $Ag^{+}$ in PbS lattice. The path is that shown in Fig. 1.

![](./images/812776705449000961_5.jpg)

Fig. 5. Diffusion pathway of $Li^{+}$ in PbS lattice.The path is that shown in Fig. 1 by replacing $Ag^{+}$ by $Li^{+}$.

Furthermore, the activation energy is twice as higher in PbS than in other chalcogenide [84]. This results could be explained by the stronger interaction of $Li^{+}$ with $S^{2-}$ when compared to the interaction of $Ag^{+}$ with $S^{2-}$ in the sulfide lattice. In other words, $Li^{+}$ can polarize $S^{2-}$ more effectively than $Ag^{+}$.

For $H^{+}$ in PbS, the diffusion mechanism is completely different from that in silver sulfide (discussed later) and from those reported in the literature [58,59,65,85]. The hydrogen ion $(H^{+})$ moves in the lattice from a sulfur site to the other, cleaving and forming the H-S bond. The S-H distance in the first and last images are $1.35\ \text{Å}$ and $1.36\ \text{Å}$, respectively. These values are close to H-S bond distance in $H_2S$ and methanethiol, $1.33\ \text{Å}$. The highest S-H distance in diffusion pathway was $1.65\ \text{Å}$, indicating an uncompleted cleavage of the H-S bond. These values support the idea of a mechanism based on the formation and breakage of H-S bonds. The minimum energy path is presented in Fig. 6 and exhibits a different profile from that of $Li^{+}$ and $Ag^{+}$ MEPs. The activation energy for this process was 0.19 eV. It is interesting to notice that the $H^{+}$ is captured by the second sulfur site before the bond with the first site is completely broken. We can attribute the relatively small activation energy of $H^{+}$ in PbS lattice to this H-S bond cleavage behavior in which S-H bonds are formed and broken along the diffusion path. The diffusion coefficient for this case was $1.41\times 10^{-5}\text{cm}^2\text{s}^{-1}$, much higher than the coefficients for $Li^{+}$ and $Ag^{+}$.

In order to conduct an additional analysis of the insertion of the impurities in the lattices, the formation energies, the distances from the nearest neighbors atoms and the charge density difference (CDD) plots were performed and are presented in SI. For PbS lattice and all defects, the formation energies are negative and the largest absolute value of a defect was obtained for $Li^{+}$. These results indicates that formation of all defects is favorable. Concerning the nearest neighbors, all defects are surrounded by four sulfur and four lead atoms and the charge density between the defect atom and the nearest sulfur atoms decreased in all cases. For more details, see SI.

![](./images/812776705449000961_6.jpg)

Fig. 6. Diffusion pathway of a $H^{+}$ in PbS lattice. The diffusion mechanism is based on cleaving and forming H-S bonds.

### 3.2. Silver sulfide

Starting by MEP analysis for diffusion of $Ag^{+}$ in Pb-doped $Ag_2S$, results are presented in Fig. 7. The activation energy is very small, 0.015 eV, indicating a possible non-activated process. The diffusion coefficients is very large, $2.60\times 10^{-4}\text{cm}^2\text{s}^{-1}$. This value, as large as it is for a solid state diffusion, is in good agreement with experimental results, which range from $10^{-3}$ to $10^{-5}\text{cm}^2\text{s}^{-1}$ [62-64].

Concerning the diffusion of $Ag^{+}$, $Li^{+}$ and $H^{+}$ in pure (non-doped) $Ag_2S$ lattice, similar MEP profiles are obtained and are shown in Figs. 8-10 respectively. The activation energies are 0.40 eV for $Ag^{+}$, 0.41 for $H^{+}$ and 0.52 eV for $Li^{+}$. Once more, the activation energy for $Li^{+}$ was larger than activation energies for $Ag^{+}$ and $H^{+}$. The diffusion coefficients for $H^{+}$ and $Li^{+}$ are $3.97\times 10^{-9}\text{cm}^2\text{s}^{-1}$ and $2.65\times 10^{-11}\text{cm}^2\text{s}^{-1}$ respectively. There are no diffusion coefficients available in the literature for diffusion of $Li^{+}$ in $Ag_2S$. Once more, we compare the values here obtained with diffusion of $Li^{+}$ in other lattices. This value is close to diffusion coefficients in silicon and carbon based materials, which lies from $10^{-11}$ to $10^{-12}\text{cm}^2\text{s}^{-1}$ [70,69,71] and it is larger than the coefficient in PbS.

For the $Ag^{+}$, the value was $7.34\times 10^{-10}\text{cm}^2\text{s}^{-1}$. These results indicate that $Ag^{+}$ diffuses more easily than $Li^{+}$. Once again, the

![](./images/812776705449000961_7.jpg)

Fig. 7. Diffusion pathway of $Ag^{+}$ in Pb-doped $Ag_2S$ lattice. The activation energy is very small indicating a non-activated process. The path is that shown in Fig. 2.

![](./images/812776705449000961_8.jpg)

Fig. 8. Diffusion pathway of $Ag^{+}$ in $Ag_{2}S$ lattice. The path is that shown in Fig. 3.

![](./images/812776705449000961_9.jpg)

Fig. 9. Diffusion pathway of $Li^{+}$ in $Ag_{2}S$ lattice. The path is that shown in Fig. 3 by replacing $Ag^{+}$ by $Li^{+}$.

![](./images/812776705449000961_10.jpg)

Fig. 10. Diffusion pathway of $H^{+}$ in $Ag_{2}S$ lattice. The path is that shown in Fig. 3 by replacing $Ag^{+}$ by $H^{+}$.

stronger interaction between $Li^{+}$ and $S^{2-}$, when compared to the $Ag^{+}$ and $S^{2-}$ interaction, is ascribed as a possible explanation for this behavior. It worth emphasizing that this value is several orders of magnitude smaller that the diffusion coefficient in Pb-doped $Ag_{2}S$ reported above.

Once again, the formation energies, the distances from the nearest neighbors and the CDD plots were performed and are presented in SI. Results are very similar to those of PbS case. The most noticeable difference is that all defects are surrounded by two sulfur and six silver atoms. For more details, see SI.

<table>
<caption>Table 1 Summary of the results.</caption>
<thead>
<tr>
<th>Impurity</th>
<th>Lattice</th>
<th>Activation Energy (eV)</th>
<th>Diffusion Coefficient ($\mathrm{cm^{2}s^{-1}}$)</th>
<th>Jump rate ($\mathrm{s^{-1}}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ag</td>
<td>PbS</td>
<td>0.54</td>
<td>$1.80\times10^{-13}$</td>
<td>$2.83\times10^{4}$</td>
</tr>
<tr>
<td>Li</td>
<td>PbS</td>
<td>0.76</td>
<td>$2.26\times10^{-15}$</td>
<td>$2.56\times10^{0}$</td>
</tr>
<tr>
<td>H</td>
<td>PbS</td>
<td>0.19</td>
<td>$1.41\times10^{-5}$</td>
<td>$5.31\times10^{9}$</td>
</tr>
<tr>
<td>Ag</td>
<td>Pb-doped $Ag_{2}S$</td>
<td>0.01</td>
<td>$2.60\times10^{-4}$</td>
<td>$3.21\times10^{11}$</td>
</tr>
<tr>
<td>Ag</td>
<td>$Ag_{2}S$</td>
<td>0.40</td>
<td>$7.34\times10^{-10}$</td>
<td>$4.18\times10^{5}$</td>
</tr>
<tr>
<td>Li</td>
<td>$Ag_{2}S$</td>
<td>0.52</td>
<td>$2.65\times10^{-11}$</td>
<td>$1.52\times10^{4}$</td>
</tr>
<tr>
<td>H</td>
<td>$Ag_{2}S$</td>
<td>0.41</td>
<td>$3.97\times10^{-9}$</td>
<td>$2.94\times10^{6}$</td>
</tr>
</tbody>
</table>

Table 1 is a summary of the results presented through the text and shows the values of activation energies, jump rates and diffusion coefficients for all cases studied in this work.

Except for the $H^{+}$, all other species exhibit lower activation energy for diffusion in silver sulfide than in lead sulfide. This observation can be rationalized by the fact that the hydrogen diffusion mechanism in PbS is completely different. For Pb-doped silver sulfide, the presence of lead atoms creating vacancies dramatically decrease the activation energy for $Ag^{+}$ diffusion with the resulting diffusion coefficient being in agreement with experimental data. In general, lithium ion exhibit lower diffusion coefficient than silver ion. This fact could not be anticipated on qualitative grounds.

Moreover, Li ion exhibit diffusion coefficient compatible with that obtained in other lattices, indicating that lithium ion can contribute to the ionic conductivity in solid electrolytes. This result is in agreement with the properties of lithium sulfide phase in lithium solid state batteries [66]. Table 2 shows a comparison of the diffusion coefficients with available experimental data and resumes the above discussion. In cases in which there is no experimental determination of the diffusion coefficients in the lattices considered in the present work, the diffusion coefficients of the ions in other lattices are reported. Table 2 also reveals that the diffusion coefficients can vary by several orders of magnitude, depending on the diffusing impurity and lattice combination. Present theoretical results reproduce the general trend of the experimental results. This is a significant result since the properties following Arrhenius equation are quite sensitive to the determination of the activation energy. It is in this sense, we stated that results are in good agreement with available experimental data in the above discussion.

Furthermore, the small activation energy and high diffusion coefficient of silver ion in Pb-doped $Ag_{2}S$ combined with a relatively small activation energy for $Ag^{+}$ in non Pb-doped silver sulfide help to justify the interest in $Ag_{2}S$/PbS films for electronic devices applications [46].

### 4. Conclusion
All the studies ions exhibit lower activation energy for diffusion in $Ag_{2}S$ than PbS except for hydrogen ion, which diffuses in PbS by a particular mechanism, in which S-H bonds are formed and broken along the diffusion path. This result is different from other $H^{+}$ diffusion mechanism [58,65,85].

Our results suggest that PbS can be successfully applied for hydrogen evolution reaction due to the mobility of hydrogen ion inside the lattice. Diffusion of hydrogen ion is important in catalysis applications [36-38,65].

The lithium ion exhibit lower diffusion coefficient than silver ion but with compatible diffusion coefficients when referred to values of other lattices indicating that lithium-doped sulfides can contribute to ionic conductivity in solid electrolytes.

For Pb-doped $Ag_{2}S$, the activation energy for $Ag^{+}$ diffusion is very small with consequent large diffusion coefficient, which is in agreement with experimental data. The calculated diffusion coefficient is

**Table 2**
Diffusion coefficients compared to available experimental values. In cases in which there is no experimental determination of the diffusion coefficients in the lattices considered in the present work, the diffusion coefficients of the ions in other lattices are reported (see text). Diffusion coefficients are in $\text{cm}^2\text{s}^{-1}$ units.

<table>
<thead>
<tr>
<th>Impurity</th>
<th>Lattice (This work)</th>
<th>Diffusion Coefficient (This work)</th>
<th>Lattice (Experimental)</th>
<th>Diffusion Coefficient (Experimental)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Li</td>
<td>PbS</td>
<td>$2.26 × 10^{-15}$</td>
<td>TiO₂</td>
<td>$10^{-12}$-$10^{-17(a)}$</td>
</tr>
<tr>
<td>Ag</td>
<td>Pb-doped Ag₂S</td>
<td>$2.60 × 10^{-4}$</td>
<td>Ag₂S</td>
<td>$10^{-3}$-$10^{-5(b,c,d)}$</td>
</tr>
<tr>
<td>Li</td>
<td>Ag₂S</td>
<td>$2.65 × 10^{-11}$</td>
<td>C and Si</td>
<td>$10^{-11}$-$10^{-12(e,f,g)}$</td>
</tr>
</tbody>
</table>

$^{(a)}$from [68], $^{(b,c,d)}$from [62-64], $^{(e,f,g)}$from [69-71].

$2.60 × 10^{-4}\text{cm}^2\text{s}^{-1}$, while for non-doped Ag₂S the coefficient is $7.34 × 10^{-10}\text{cm}^2\text{s}^{-1}$, demonstrating that the mobility of species in regions with vacancies dominates the diffusion phenomena and justifies the interest in Ag₂S/PbS films for applications as electronic devices.

### CRediT authorship contribution statement

Ricardo R. Oliveira: Conceptualization, Investigation, Methodology, Visualization, Writing - review & editing. Bruno N.C. Tenorio: Investigation, Software, Visualization, Writing - review & editing. Alexandre B. Rocha: Conceptualization, Writing - original draft, Project administration, Supervision.

### Acknowledgement

The authors acknowledge CAPES, CNPq and FAPERJ for financial support.

### Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, athttps://doi.org/10.1016/j.commatsci.2019.04.046.

### References

[1] H. Hirata, K. Higashiyama, A new type of lead (II) ion-selective ceramic membrane electrode, Anal. Chim. Acta 54 (1971) 415-422.
[2] M. Mascini, A. Liberti, Preparation and analytical evaluation of a new Lead(II) heterogeneous membrane electrode, Anal. Chim. Acta 60 (1972) 405-412.
[3] M.S. Mohan, G.A. Rechnitz, Preparation and properties of the sulfate ion selective membrane electrode, Anal. Chem. 45 (1973) 1323-1326.
[4] G. Heijne, W. Van Der Linden, G. Den Boef, The formation and properties of mixed lead sulfide-silver sulfide membranes for lead(II)-selective electrodes, Anal. Chim. Acta 100 (1978) 193-205.
[5] Yu.G. Vlasov, E.A. Bychkov, Electrochemical ion-selective chalcogenide glasses*, Sens. Actuators 12 (1987) 275-283.
[6] S.-R. Sheen, J.-S. Shih, Lead(II) ion-selective electrodes based on crown ethers, Analyst 117 (1992) 1691.
[7] A. Aghassi, M. Jafarian, I. Danaee, F. Gobal, M.G. Mahjani, AC impedance and cyclic voltammetry studies on PbS semiconducting film prepared by electro-deposition, J. Electroanal. Chem. 661 (2011) 265-269.
[8] K. Murali, Preparation and characterization of chemically deposited CuInSe2 films, Thin Solid Films 167 (1988) L19-L22.
[9] D. Wang, T. Xie, Q. Peng, Y. Li, Ag, Ag2S, and Ag2Se nanocrystals: Synthesis, assembly, and construction of mesoporous structures, J. Am. Chem. Soc. 130 (2008) 4016-4022.
[10] S. Xiong, B. Xi, K. Zhang, Y. Chen, J. Jiang, J. Hu, H.C. Zeng, Ag nanoprisms with Ag2S attachment, Sci. Rep. 3 (2013) 1-9.
[11] A. Svane, N.E. Christensen, M. Cardona, A.N. Chantis, M. Van Schilfgaarde, T. Kotani, Quasiparticle self-consistent GW calculations for PbS, PbSe, and PbTe: band structure and pressure coefficients, Phys. Rev. B - Condensed Matter Mater. Phys. 81 (2010) 1-10.
[12] W.P. Lim, Z. Zhang, H.Y. Low, W.S. Chin, Preparation of Ag2S nanocrystals of predictable shape and size, Angew. Chem. - Int. Ed. 43 (2004) 5685-5689.
[13] L. Kubie, L.A. King, M.E. Kern, J.R. Murphy, S. Kattel, Q. Yang, J.T. Stecher, W.D. Rice, B.A. Parkinson, Synthesis and characterization of ultrathin silver sulfide nanoplatelets, ACS Nano 11 (2017) 8471-8477.
[14] G. Henshaw, I.P. Parkin, G. Shaw, Convenient, low-energy synthesis of metal sulfides and selenides; PbE, Ag2E, ZnE, CdE (E = S, Se), Chem. Commun. 2 (1996) 1095.
[15] F. Gao, Q. Lu, D. Zhao, Controllable assembly of ordered semiconductor Ag2S nanostructures, Nano Lett. 3 (2003) 85-88.
[16] J. Chen, L. Wang, Y. Chen, J. Guo, A DFT study of the effect of natural impurities on the electronic structure of galena, Int. J. Miner. Process. 98 (2011) 132-136.

[17] M. Arita, Thermodynamics and defect structures of silver sulfide, J. Phys. Chem. Solids 68 (2007) 1730-1744.
[18] Y. Zhang, G. Hong, Y. Zhang, G. Chen, F. Li, H. Dai, Q. Wang, Ag2S quantum dot: a bright and biocompatible fluorescent nanoprobe in the second near-infrared window, ACS Nano 6 (2012) 3695-3702.
[19] J. Zhang, J. Gao, E.M. Miller, J.M. Luther, M.C. Beard, Diffusion-controlled synthesis of PbS and PbSe quantum dots with in situ halide passivation for quantum dot solar cells, ACS Nano 8 (2014) 614-622.
[20] R. Wang, X. Wu, K. Xu, W. Zhou, Y. Shang, H. Tang, H. Chen, Z. Ning, Highly efficient inverted structural quantum dot solar cells, Adv. Mater. 1704882 (2018) 1704882.
[21] A. Tubtimtae, K.L. Wu, H.Y. Tung, M.W. Lee, G.J. Wang, Ag2S quantum dot-sensitized solar cells, Electrochem. Commun. 12 (2010) 1158-1160.
[22] J.A. Suárez, J.J. Plata, A.M. Márquez, J.F. Sanz, Ag2S quantum dot-sensitized solar cells by first principles: the effect of capping ligands and linkers, J. Phys. Chem. A 121 (2017) 7290-7296.
[23] Z. Ren, J. Sun, H. Li, P. Mao, Y. Wei, X. Zhong, J. Hu, S. Yang, J. Wang, Bilayer PbS quantum dots for high-performance photodetectors, Adv. Mater. 29 (2017) 1-7.
[24] P. Rekemeyer, C.-H.M. Chuang, M.G. Bawendi, S. Gradecak, Minority carrier transport in lead sulfide quantum dot photovoltaics, Nano Lett. (2017) acs.nanolett.7b02916.
[25] S. Pradhan, A. Stavrinadis, S. Gupta, G. Konstantatatos, Reducing interface recombination through mixed nanocrystal interlayers in PbS quantum dot solar cells, ACS Appl. Mater. Interfaces 9 (2017) 27390-27395.
[26] J.J. Peterson, T.D. Krauss, Fluorescence spectroscopy of single lead sulfide quantum dots, Nano Lett. 6 (2006) 510-514.
[27] R. Ihly, J. Tolentino, Y. Liu, M. Gibbs, M. Law, The photothermal stability of PbS quantum dot solids, ACS Nano 5 (2011) 8175-8186.
[28] V.M. Huxter, T. Mirkovic, P.S. Nair, G.D. Scholes, Demonstration of bulk semiconductor optical properties in processable Ag2S and EuS nanocrystalline systems, Adv. Mater. 20 (2008) 2439-2443.
[29] J.H. Heo, M.H. Jang, M.H. Lee, D.H. Shin, D.H. Kim, S.H. Moon, S.W. Kim, B.J. Park, S.H. Im, High-performance solid-state pbs quantum dot-sensitized solar cells prepared by introduction of hybrid perovskite interlayer, ACS Appl. Mater. Interfaces 9 (2017) 41104-41110.
[30] H. He, L. Yi, T. Zhi-Quan, Z. Dong-Liang, Z. Zhi-Ling, P. Dai-Wen, Ultrasmall Pb:Ag2S quantum dots with uniform particle size and bright tunable fluorescence in the NIR-II window, Small 14 (2018) 1703296.
[31] P.R. Brown, D. Kim, R.R. Lunt, N. Zhao, M.G. Bawendi, J.C. Grossman, V. Bulović, Energy level modification in lead sulfide quantum dot thin films through ligand exchange, ACS Nano 8 (2014) 5863-5872.
[32] C. Leiggener, G. Calzaferri, Synthesis and luminescence properties of Ag2S and PbS clusters in zeolite A, Chem. - A Eur. J. 11 (2005) 7191-7198.
[33] Q. Jiang, W. Zeng, C. Zhang, Z. Meng, J. Wu, Q. Zhu, D. Wu, H. Zhu, Broadband absorption and enhanced photothermal conversion property of optodop-like Ag@Ag2S core@shell structures with gradually varying shell thickness, Sci. Rep. 7 (2017) 17782.
[34] B.R. Hyun, J.J. Choi, K.L. Seyler, T. Hanrath, F.W. Wise, Heterojunction pbs nanocrystal solar cells with oxide charge-transport layers, ACS Nano 7 (2013) 10938-10947.
[35] N. Arad-Vosk, R. Beach, A. Ron, T. Templeman, Y. Golan, G. Sarusi, A. Sa'ar, Infrared photoconductivity and photovoltaic response from nanoscale domains of pbs alloyed with thorium and oxygen, Nanotechnology 29 (2018) 115202 .
[36] M. Shaban, M. Rabia, A.M. El-Sayed, A. Ahmed, S. Sayed, Photocatalytic properties of PbS/graphene oxide/polyaniline electrode for hydrogen generation, Sci. Rep. 7 (2017) 1-13.
[37] M. Rabia, H.S.H. Mohamed, M. Shaban, S. Taha, Preparation of polyaniline/PbS core-shell nano/microcomposite and its application for photocatalytic H2 electrogeneration from H2O, Sci. Rep. 8 (2018) 1107.
[38] M. Basu, R. Nazir, C. Mahala, P. Fageria, S. Chaudhary, S. Gangopadhyay, S. Pande, Ag2S/Ag heterostructure: a promising electrocatalyst for the hydrogen evolution reaction, Langmuir 33 (2017) 3178-3186.
[39] S.I. Sadovnikov, A.I. Gusev, Facile synthesis, structure, and properties of Ag2S/Ag heteronanostructure, J. Nanopart. Res. 18 (2016) 1-12.
[40] S. Sadovnikov, Structure and properties of Ag2S/Ag semiconductor/metal heteronanostructure, J. Nanotechnol. Mater. Sci. 3 (2016) 1-10.
[41] S.I. Sadovnikov, A.A. Rempel', A.I. Gusev, Ag2S/Ag heteronanostructure, JETP Lett. 106 (2017) 587-592.
[42] H. Wang, L. Qi, Controlled synthesis of Ag2S, Ag2Se, and Ag nanofibers by using a general sacrificial template and their application in electronic device fabrication, Adv. Funct. Mater. 18 (2008) 1249-1256.
[43] A. Gubicza, D.Z. Manrique, L. Pósa, C.J. Lambert, G. Mihály, M. Csontos,

A. Halbritter, Asymmetry-induced resistive switching in Ag-Ag2S-Ag memristors enabling a simplified atomic-scale memory design, Sci. Rep. 6 (2016) 1-9.

[44] L. Li, H. Yin, Y. Wang, J. Zheng, H. Zeng, G. Chen, A chalcohalide glass/alloy based Ag+ ion - selective electrode with nanomolar detection limit, Sci. Rep. 7 (2017) 16752.

[45] Y. Zheng, S. Wang, W. Liu, Z. Yin, H. Li, X. Tang, C. Uher, Thermoelectric transport properties of p-type silver-doped PbS with in situ Ag2S nanoprecipitates, J. Phys. D: Appl. Phys. 47 (2014).

[46] Y.M. Zhang, L. Chen, H.C. Pan, Co-electrodeposition and characterization of Ag- Ag2S-PbS thin films on indium-tin-oxide coated glass, Adv. Mater. Res. 900 (2014) 397-400.

[47] K. Xu, J. Heo, Effect of silver ion-exchange on the precipitation of lead sulfide quantum dots in glasses, J. Am. Ceram. Soc. 95 (2012) 2880-2884.

[48] K. Xu, J. Heo, Lead sulfide quantum dots in glasses controlled by silver diffusion, J. Non-Cryst. Solids 358 (2012) 921-924.

[49] K. Xu, J. Heo, Electric field-assisted Ag+ migration for PbS quantum dot formation in glasses, J. Non-Cryst. Solids 377 (2013) 254-256.

[50] K. Xu, J. Heo, Precipitation of PbS quantum dots in glasses by thermal diffusion of Ag+ ions from silver pastes, J. Non-Cryst. Solids 387 (2014) 76-78.

[51] N.N. Umarova, N.I. Movchan, R.A. Yusupov, E.A. Korolev, V.P. Morozov, Ion ex- change of silver(I) on thin PbS films as influenced by diffusion, Russ. J. Gen. Chem. 73 (2003) 999-1004.

[52] E. Sarica, V. Bilgin, Study of some physical properties of ultrasonically spray de- posited silver doped lead sulphide thin films, Mater. Sci. Semicond. Process. 68 (2017) 288-294.

[53] Z. Wang, T. Gu, T. Kadohira, T. Tada, S. Watanabe, Migration of Ag in low-tem- perature Ag2S from first principles, J. Chem. Phys. 128 (2008) 2-8.

[54] E. Wimmer, W. Wolf, J. Sticht, P. Saxe, C.B. Geller, R. Najafabadi, G.A. Young, Temperature-dependent diffusion coefficients from ab initio computations: hy- drogen, deuterium, and tritium in nickel, Phys. Rev. B - Condensed Matter Mater. Phys. 77 (2008) 1-12.

[55] D.J. Siegel, C. Hamilton, First-principles study of the solubility, diffusion, and clustering of C in Ni, Phys. Rev. B - Condensed Matter Mater. Phys. 68 (2003) 1-7.

[56] S. Neumeier, H.U. Rehman, J. Neuner, C.H. Zenk, S. Michel, S. Schuwalow, J. Rogal, R. Drautz, M. Göken, Diffusion of solutes in fcc Cobalt investigated by diffusion couples and first principles kinetic Monte Carlo, Acta Mater. 106 (2016) 304-312.

[57] S.S. Naghavi, V.I. Hegde, C. Wolverton, Diffusion coefficients of transition metals in fcc cobalt, Acta Mater. 132 (2017) 467-478.

[58] W. Liu, N. Miao, L. Zhu, J. Zhou, Z. Sun, Adsorption and diffusion of hydrogen and oxygen in FCC-Co: a first-principles study, PCCP 19 (2017) 32404-32411.

[59] M. David, D. Connétable, Diffusion of interstitials in metallic systems, illustration of a complex study case: aluminum, J. Phys. Condensed Matter 29 (2017).

[60] A.F. Wright, N.A. Modine, Migration processes of the As interstitial in GaAs, J. Appl. Phys. 120 (2016) 11.

[61] P. Wu, N. Yin, P. Li, W. Cheng, M. Huang, The adsorption and diffusion behavior of noble metal adatoms (Pd, Pt, Cu, Ag and Au) on a MoS2 monolayer: a first-prin- ciples study, Phys. Chem. Chem. Phys. 19 (2017) 20713-20722.

[62] R.L. Allen, W.J. Moore, Diffusion of silver in silver sulfide, J. Phys. Chem. 63 (1959) 223-226.

[63] R.P. Buck, V.R. Shepard, Reversible metal/salt interfaces and the relation of second kind and "All-Solid-State" membrane electrodes, Anal. Chem. 46 (1974) 2097-2103.

[64] P.T. Martinhon, J. Carreño, C.R. Sousa, O.E. Barcia, O.R. Mattos, Electrochemical impedance spectroscopy of lead(II) ion-selective solid-state membranes, Electrochim. Acta 51 (2006) 3022-3028.

[65] R.R. Oliveira, A.S. Rocha, V. Teixeira Da Silva, A.B. Rocha, Investigation of hy- drogen occlusion by molybdenum carbide, Appl. Catal. A: Gen. 469 (2014) 139-145.

[66] A. Manthiram, X. Yu, S. Wang, Lithium battery chemistries enabled by solid-state electrolytes, Nat. Rev. Mater. 2 (2017) 1-16.

[67] Y. Oishi, Y. Kamei, M. Akiyama, T. Yanagi, Self-diffusion coefficient of lithium in lithium oxide, J. Nucl. Mater. 87 (1979) 341-344.

[68] C. Arrouvel, T.C. Peixoto, M.E. Valerio, S.C. Parker, Lithium migration at low concentration in TiO2polymorphs, Comput. Theor. Chem. 1072 (2015) 43-51.

[69] N. Ding, J. Xu, Y.X. Yao, G. Wegner, X. Fang, C.H. Chen, I. Lieberwirth, Determination of the diffusion coefficient of lithium ions in nano-Si, Solid State Ionics 180 (2009) 222-225.

[70] F.W. Tang, X.Y. Song, C. Hou, X.M. Liu, H.B. Wang, Z.R. Nie, Modeling of Li dif- fusion in nanocrystalline Li-Si anode material, PCCP 20 (2018) 7132-7139.

[71] T.L. Kulova, A.M. Skundin, E.A. Nizhnikovskii, A.V. Fesenko, Temperature effect on the lithium diffusion rate in graphite, Russ. J. Electrochem. 42 (2006) 259-262.

[72] S. Loftager, J.M. García-Lastra, T. Vegge, A density functional theory study of the carbon-coating effects on lithium iron borate battery electrodes, Phys. Chem. Chem. Phys. 19 (2017) 2087-2094.

[73] J. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865-3868.

[74] D. Vanderbilt, Soft self-consistent pseudopotentials in a generalized eigenvalue formalism, Phys. Rev. B 41 (1990) 7892-7895.

[75] H.J. Monkhorst, J.D. Pack, Special points for Brillonin-zone integrations*, Phys. Rev. B 13 (1976) 5188-5192.

[76] K.J. Caspersen, E.a. Carter, Finding transition states for crystalline solid-solid phase transformations, Proc. Natl. Acad. Sci. USA 102 (2005) 6738-6743.

[77] G. Henkelman, B.P. Uberuaga, H. Jónsson, Climbing image nudged elastic band method for finding saddle points and minimum energy paths, J. Chem. Phys. 113 (2000) 9901-9904.

[78] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G.L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Braccia, S. Scandolo, G. Sclauzero, A.P. Seitsonen, A. Smogunov, P. Umari, R.M. Wentzcovitch, QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials, J. Phys. Condensed Matter: Inst. Phys. J. 21 (2009) 395502 .

[79] G.U. Von Oertzen, R.T. Jones, A.R. Gerson, Electronic and optical properties of Fe, Zn and Pb sulfides, Phys. Chem. Miner. 32 (2005) 255-268.

[80] S. Kashida, N. Watanabe, T. Hasegawa, H. Iida, M. Mori, S. Savrasov, Electronic structure of Ag2S, band calculation and photoelectron spectroscopy, Solid State Ionics 158 (2003) 167-175.

[81] R. Kutner, Chemical diffusion in the lattice gas of non-interacting particles, Phys. Lett. A 81 (1981) 239-240.

[82] C. Wert, C. Zener, Interstitial atomic diffusion coefficients, Phys. Rev. 76 (1949) 1169-1175.

[83] C. Zener, Theory of Do for atomic diffusion in metals, J. Appl. Phys. 22 (1951) 372-375.

[84] X. Sun, Z. Wang, Ab initio study of adsorption and diffusion of lithium on transition metal dichalcogenide monolayers, Beilstein J. Nanotechnol. 8 (2017) 2711-2718.

[85] E.W. Keong Koh, C.H. Chiu, Y.K. Lim, Y.W. Zhang, H. Pan, Hydrogen adsorption on and diffusion through MoS2 monolayer: First-principles study, Int. J. Hydrogen Energy 37 (2012) 14323-14328.