# Boron nitride nanotube as a delivery system for platinum drugs: Drug encapsulation and diffusion coefficient prediction

Zahra Khatti, Seyed Majid Hashemianzadeh *

Molecular Simulation Research Laboratory, Department of Chemistry, Iran University of Science and Technology, Tehran, Iran

---

## ARTICLE INFO

**Article history:**
Received 16 December 2015
Received in revised form 8 April 2016
Accepted 10 April 2016
Available online xxxx

**Keywords:**
Boron nitride nanotube
Molecular dynamics simulation
Carboplatin
Drug delivery
Encapsulation

## ABSTRACT

Molecular dynamics (MD) simulation has been applied to investigate a drug delivery system based on boron ni- tride nanotubes, particularly the delivery of platinum-based anticancer drugs. For this propose, the behavior of carboplatin drugs inserted in boron nitride nanotubes (BNNT) as a carrier was studied. The diffusion rate of water molecules and carboplatin was investigated inside functionalized and pristine boron nitride nanotubes. The penetration rate of water and drug in functionalized BNNT was higher than that in pristine BNNT due to fa- vorable water-mediated hydrogen bonding in hydroxyl edge-functionalized BNNT. Additionally, the encapsula- tion of multiple carboplatin drugs inside functionalized boron nitride nanotubes with one to five drug molecules confined inside the nanotube cavity was examined. At high drug loading, the hydrogen bond formation between adjacent drugs and the non-bonded van der Waals interaction between carboplatin and functionalized BNNT inner surface were found to be influential in drug displacement within the functionalized BNNT cavity for higher drug-loading capacity.

© 2016 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Boron nitride nanotubes (BNNTs) are structural analogues of carbon nanotubes (CNTs), in which B—N bonds replace C—C bonds. Carbon nanotubes (CNTs) have been widely explored for use in designing novel delivery platforms for medical applications due to their unique physical and chemical properties (Adeli et al., 2011; Baughman et al., 2002; Sharma et al., 2013; Wong and Vijayaraghavan, 2014). However, the inherent cytotoxicity of CNTs has imposed limitations on biological applications to human cells and other live biosystems (Bottini et al., 2006; Lewinski et al., 2008). Alternatively, high-purity and high- quality BNNTs have been confirmed to be inherently nontoxic to health and the environment due to their chemical inertness and structural sta- bility (Chen et al., 2009; Cohen and Zettl, 2010). Furthermore, many other results highlight the biosafety of BNNTs (Ciofani et al., 2014) and indicate that BNNTs are biocompatible without inducing oxidative DNA damage and apoptosis (Salvetti et al., 2015). Therefore, BNNTs show better biocompatibility than CNTs (Ciofani et al., 2008; Lahiri et al., 2010), and are more appropriate for medical applications such as nanomedicine and drug delivery. On the other hand, BNNTs are ex- pected to have unique electronic and mechanical properties, for in- stance, to be semiconducting independent of tube chirality, number of layers and diameter (Wang et al., 2010). Boron and nitrogen atoms forming boron nitride nanotubes have partial charges, and become further polarized in the presence of water. Therefore, in comparison to CNTs, BNNTs have shown superior water permeation properties with similar diameter and length due to the partial charges that cause reduc- tion in the water permeation barrier (Won and Aluru, 2008a; Won and Aluru, 2008b). Notably, applications of BNNTs for biological domains re- main largely unexplored; the main reason is the high chemical stability and poor dispersibility in physiological solutions. Like CNTs, BNNTs are insoluble in aqueous media with regard to suitable hydrophobicity (Lee et al., 2009). Nevertheless, some applications of BNNTs have been studied in the biomedical field, especially nanomedicine and drug nanocarriers in recent years (Ciofani, 2010; Ciofani et al., 2012; Li et al., 2013; Saikia et al., 2013; Weng et al., 2014). Consequently, much interest has been evinced in non-covalent and covalent functionalization methods for solubilizing BNNTs (Ciofani et al., 2013; Ikuno et al., 2007; Pal et al., 2007; Xie et al., 2005; Zhi et al., 2011). BNNT chemical functionalization has received full attention to achieve active functional groups in which modification may generate interest in either N or B sites. Bonding on N sites has mainly been obtained with amine groups via ammonia plasma irradiation (Ikuno et al., 2007). As effective reported methods for solubilizing BNNTs, B sites can be activated by oxidizing BNNTs in $H_2O_2$ under high temperature and pressure (Zhi et al., 2009) or in $HNO_3$ solution under sonicated con- dition (Ciofani et al., 2012), in which hydroxyl groups (—OH) can be co- valently linked to boron atoms. Additionally, the N sites have been suggested to be connected to H, as revealed by theoretical calculations (Sugino et al., 2001). Hydroxylated BNNTs could be a suitable model for drug delivery applications. Platinum-based anticancer drugs, such as cisplatin, carboplatin and oxaliplatin are used to treat a wide range

---

* Corresponding author.
E-mail addresses: hashemianzadeh@iust.ac.ir, hashemianzadeh@gmail.com (S.M. Hashemianzadeh).

http://dx.doi.org/10.1016/j.ejps.2016.04.011
0928-0987/© 2016 Elsevier B.V. All rights reserved.

Please cite this article as: Khatti, Z., Hashemianzadeh, S.M., Boron nitride nanotube as a delivery system for platinum drugs: Drug encapsulation and diffusion coefficient prediction, European Journal of Pharmaceutical Sciences (2016), http://dx.doi.org/10.1016/j.ejps.2016.04.011

of tumors, particularly in genitourinary, colorectal and non-small cell lung cancers, despite their adverse side effects (McWhinney et al., 2009; Wang and Lippard, 2005). The platinum atom of these agents binds to DNA and induces cellular apoptosis (Kelland, 2007; Todd and Lippard, 2009). Hence, many adverse side effects to non-target cells can be greatly mitigated by nanoscale drug delivery. Carboplatin (diammineplatinum(II)-cyclobutane-1,1-dicarboxylate), a second- generation platinum-based anticancer drug, was selected as drug model because it possesses greater water solubility and fewer adverse effects than cisplatin (Arlt et al., 2010; Kelland, 2007; Negureanu and Salsbury, 2013). Molecular modeling is a fast and reliable tool for drug encapsulation inside the nanostructure. On the other hand, boron ni- tride nanotubes are promising alternative nanocarriers offering encap- sulation of more drugs for large inner volume, and generally with open ends to penetrate the drugs if the interaction energy is favorable.

In the present study, our motivation is to characterize the behavior of carboplatin drugs inserted in boron nitride nanotubes as a transporter for use in drug delivery by molecular dynamics simulation. This study focuses on the relationship between diffusivity of water and drug into the pristine and hydroxylated BNNTs. Furthermore, this study investi- gates the capability of loading varying amounts of drugs inside a func- tionalized BNNT. Here, we report the hydrogen bonding associated with the positioning of the drugs along the functionalized BNNT and in- termolecular interactions among the drug molecules and functionalized BNNT cavity surface.

## 2. Simulation details

### 2.1. Molecular models of BNNTs and drug

In this work, the zigzag (18,0) open-ended single-walled BNNT with 14 Å diameter and 40 Å length was considered, and hydrogen atoms for the pristine BNNT model terminated the edges of the tube. In order to construct the functionalized BNNT, 18 hydroxyl groups (—OH) were linked on B sites of one edge, and another edge was saturated with hy- drogen atoms on N sites. Functionalization not only imparts solubility to BNNTs but also avoid dangling bonds at their opened edge, which be- come dramatically active during drug encapsulation (Duverger et al., 2014; Wang et al., 2008).

The initial bond length of HO—B and O—H was 1.48 Å and 0.96 Å, respectively (Chigo Anota and Cocoletzi, 2013). The structures of the pristine and functionalized BNNT were optimized at the B3LYP/3-21G level of theory by GAMESS (Schmidt et al., 1993). Partial charges were derived by fitting the electrostatic potential obtained at the HF/6-31G** level of theory through the restrained electrostatic potential (RESP) method, using the RESP module of the AMBER12 package (Case et al., 2012).

<table><caption>Table 1 Partial charges for FBNNT atoms.</caption>
<thead>
  <tr>
    <th>Atom</th>
    <th>Atomic charge (e)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>B</td>
    <td>0.582134</td>
  </tr>
  <tr>
    <td>N</td>
    <td>−0.513405</td>
  </tr>
  <tr>
    <td>O</td>
    <td>−0.606920</td>
  </tr>
  <tr>
    <td>H of N</td>
    <td>0.256890</td>
  </tr>
  <tr>
    <td>H of O</td>
    <td>0.368378</td>
  </tr>
  <tr>
    <td>H of B</td>
    <td>−0.172224</td>
  </tr>
</tbody>
</table>

Table 1 summarizes the partial charge values used in the MD simu- lations. Parameters involving the boron atoms were taken from the DREIDING force field (Mayo et al., 1990). Other parameters of the pris- tine and functionalized BNNT were modeled using the general AMBER force field (GAFF) (Wang et al., 2004), where the atom types na and oh were chosen to represent the aromatic nitrogen atoms and oxygen atoms in hydroxyl group, respectively. The Lennard-Jones parameters of boron atoms in BNNT were taken from the DREIDING force field ($\varepsilon=0.0950$ kcal·mol⁻¹, $\sigma=4.0200$ Å).

On the basis of our previous work (Khatti and Hashemianzadeh, 2015), the structure of carboplatin was obtained from the protein databank as PDB entry code QPT, and the parameters were identified from the literature and the GAFF (Cundari et al., 1996; Williams et al., 2004; Yao et al., 1994); additionally, the carboplatin's partial charges were calculated using the RESP module of AMBER 12. Fig. 1(a) shows the optimized structure of carboplatin molecule. The conformation of carboplatin inside the pristine and functionalized BNNT is as previously reported.

### 2.2. Systems preparation

The molecular dynamic simulations were considered for six systems. The first system contains a carboplatin at a position along the pristine BNNT z-axis that was placed with a mean distance of 10 Å from the tube edge, drug_BNNT. The other five systems were considered differ- ent uptakes of carboplatin molecules in the functionalized BNNT (FBNNT) cavity by increasing the number of carboplatin molecules

![](./images/814532721404542977_1.jpg)

Fig. 1. Chemical structure of carboplatin with atomic labels (a); Initial structure of the six studied systems containing different number of drug in pristine and functionalized BNNT (b).

Please cite this article as: Khatti, Z., Hashemianzadeh, S.M., Boron nitride nanotube as a delivery system for platinum drugs: Drug encapsulation and diffusion coefficient prediction, European Journal of Pharmaceutical Sciences (2016), http://dx.doi.org/10.1016/j.ejps.2016.04.011

![](./images/814532721404542977_2.jpg)

Fig. 2. Mean square displacement ($\mathring{A}^2$) in the direction of the nanotube axis, MSD, vs. time (ps) for water molecules inside the (a) pristine BNNT and (b) functionalized BNNT.

from one to five; these were labeled as i-Drug, where i = 1–5, respectively, i-drug_FBNNT. In the initial state of all i-drug_FBNNT complexes, one drug molecule was placed in the same position with the first system; the other molecule(s) was/were placed in the middle of the FBNNT with equivalent intermolecular distances between each drug molecule when more than one was present, as shown in Fig. 1(b). Thereafter, all of the model systems were solvated in an aqueous solution with a TIP3P (Jorgensen et al., 1983) octagonal box over $12\ \mathring{A}$ from the system surface. All systems were solvated in about 7544 water molecules in total.

### 2.3. Molecular dynamics (MD) simulations

The AMBER 12 simulation package was employed for the molecular dynamics simulations (Case et al., 2012). All calculations were performed in the isothermal-isobaric ensemble at 1 atm and 300 K using the SANDER module in the AMBER 12 program. Langevin dynamics was used for the temperature and presser regulation (Cerutti et al., 2008). The SHAKE algorithm was applied to constrain the bonds containing hydrogen atoms (Shuichi Miyamoto, 1992). Periodic boundary conditions were applied and the particle mesh Ewald method was used for long-range electrostatics (Essmann et al., 1995); it was set at $12\ \mathring{A}$ for nonbonded interactions. Each simulation included 5000 steps of solvent relaxation and 5000 steps of solute relaxation for energy minimization. All systems were then heated from 0 K to 300 K for 120 ps and equilibrated at 300 K for 200 ps. The production stages were finally run for 10 ns with a time step of 2 fs, and the structural coordinates were stored in trajectory files every 1 ps for analysis. Analysis of the configurations was performed with the ptraj module included in AmberTools14.

## 3. Results and discussion

### 3.1. Diffusion coefficient

One of the most important dynamic properties is diffusion coefficient (D), and molecular dynamics simulation is a straightforward and reliable way for its determination. Furthermore, a theoretical study has reported that OH groups of carrier hydrated surface provide a favorable zone for the adsorption of platinum drugs (Simonetti et al., 2011). Hence, in order to study molecular diffusion of drug and water inside the BNNT, MD simulation was performed for two systems, including drug_BNNT and 1drug_FBNNT. The diffusion coefficient of water in single-walled BNNTs has been shown to have a Fickian-type diffusion mechanism; moreover, Fickian diffusion is widely used in MD simulations to predict the diffusion coefficient (Won and Aluru, 2008a). Therefore, Fickian diffusion in Eq. (1)was employed to predict the diffusion coefficient. Molecular dynamics simulations estimated the water mean-square displacement (MSD). All MD simulations were performed in three dimensions; therefore, n = 3 and one-sixth of the slope of MSD gives D by least squares fitting.

$$
<|r-r^0|^2>=2nDt \tag{1}
$$

The MSD plots for water molecules in pristine and functionalized BNNT are shown in Fig. 2. The results of diffusion coefficients in Table 2 show that water molecules diffuse faster inside the FBNNT than in the BNNT. These results may be related to the electrostatic interaction of hydroxyl groups on the tube edge with water molecules that attract water molecules inside the FBNNT faster than inside the BNNT.

For diffusion coefficient prediction of a molecule in solution using MD simulations, several individual MD simulations using the same initial coordinates must be performed (Wang and Hou, 2011). Then the diffusion coefficient D is calculated by a least-square fitting of mean MSD to simulation time. Here, 10 individual MD simulations have been performed using the same initial coordinates of drug_BNNT and 1drug_FBNNT to achieve mean MSD at the time of drug entry into the nanotube. The MSD plots and the determined values of the drug diffusivity into the pristine and functionalized BNNT are presented in Fig. 3 and Table 2, respectively. Whereas carriers with surface tensions below 100–200 mN/m value are drawn into the nanotube cavity by capillarity forces (Ebbesen, 1996), so due to the relative low surface tension ($\gamma=72$ mN/m) of water as solvent and thus the positive wetting behavior, water acts as a carrier for the drug (Hampel et al., 2008). Therefore, drug diffusivity into the nanotube is related to the diffusive behavior of water molecules inside the tube. Since an increase in the diffusion rate of water molecules in FBNNT was observed according to the diffusion coefficient values of Table 2, the penetration rate of the drug obviously is larger than that in BNNT. As will be described in the next section, the electrostatic interaction between carboplatin and hydroxyl groups on the tube edge enhances the permeation rate of the drugs into the nanotube cavity. The absolute values of the diffusion coefficient also cannot be predicted because the type of the MD sampling and MD settings likely impact the diffusion coefficient calculations (Wang and Hou, 2011).

<table>
<caption>Table 2<br>Prediction of diffusion coefficient of water and carboplatin in the pristine and functionalized boron nitride nanotube.</caption>
<thead>
<tr>
<th>System</th>
<th>D,$\text{cm}^2\text{s}^{-1} \times 10^5$</th>
</tr>
</thead>
<tbody>
<tr>
<td>WAT_BNNT</td>
<td>0.440</td>
</tr>
<tr>
<td>WAT_FBNNT</td>
<td>0.600</td>
</tr>
<tr>
<td>Drug_BNNT</td>
<td>0.560</td>
</tr>
<tr>
<td>Drug_FBNNT</td>
<td>1.890</td>
</tr>
</tbody>
</table>

Please cite this article as: Khatti, Z., Hashemianzadeh, S.M., Boron nitride nanotube as a delivery system for platinum drugs: Drug encapsulation and diffusion coefficient prediction, European Journal of Pharmaceutical Sciences (2016), http://dx.doi.org/10.1016/j.ejps.2016.04.011

![](./images/814532721404542977_3.jpg)

Fig. 3. Mean square displacement $(\text{\AA}^2)$ in the direction of the nanotube axis, MSD, vs. time (ps) for carboplatin molecule inside the pristine BNNT (a) and functionalized BNNT (b).

### 3.2. Hydrogen-bonding analysis

Hydrogen bond analysis was performed using the hydrogen bond analysis tools available in AmberTools14. In this study, strong hydrogen bonding between the boron nitride nanotubes and water molecules was measured on the basis of the two criteria, namely that the distance between proton donor (D) and acceptor (A) atom is $\leq 3.5$ Å, and that the $D$-$H$-$A$ angle is $\geq 120^\circ$ (Laohpongspaisan et al., 2009; Nunthaboot et al., 2010). We observed no hydrogen bonds among water molecules and nitrogen atoms of the sidewall inside the pristine and functionalized nanotubes. Won and Aluru[13] reported that although the partial charges on boron and nitrogen atom forming the boron nitride nanotube improve the wetting behavior, the diffusion coefficient due to the formation of hydrogen bonds between the water and nitrogen atoms slightly decreases for a boron nitride nanotube with a radius of $<5.52$ Å (Won and Aluru, 2008a). However, water structure with a strong hydrogen-bonding network inside the BNNTs with larger radius leads to loss of hydrogen bonds between the water and nitrogen atoms inside them and allows larger water flow rates (Hilder et al., 2009).

The simulations result in formation of numerous hydrogen bonds between OH edge-functionalized FBNNT and water molecules, and a few hydrogen bonds on another edge of FBNNT, on N sites with water molecules as shown in Fig. 4(a). In addition, the low number of hydrogen bonds is presented in Fig. 4(b) between N sites of pristine boron nitride nanotube and water molecules through MD production. The effect of hydroxyl (---OH)-functionalized FBNNT on the formation of hydrogen bonds around the edge is indicative of an electrostatic dipole-dipole interaction between hydrophilic carboplatin and hydroxyl groups on the tube edge. As a result, it could be surmised that the faster entry of the drug molecules occurs inside the pores of functionalized boron nitride nanotube, rather than in the pristine ones. Additionally, hydrogen bonds between water and OH edge-functionalized BNNT play an important role in maintaining stable dispersion of BNNTs and preventing aggregation of FBNNTs in the solutions (Lee et al., 2012). In addition, an experimental study has reported that platinum drugs incorporated into hydroxylated nanostructure stayed in the tumor tissues for as much as 25 days after administration, by adhering the carrier to the cells (Ajima et al., 2008).

### 3.3. Drug localization and interaction

The results from MD simulations of the five systems with different drug amounts demonstrated that all encapsulated drug molecules reside inside the FBNNT cavity throughout the simulation time. For the five systems with one carboplatin molecule outside each FBNNT, after the equilibration stage the drug entered quickly inside the FBNNT cavity and was confined there throughout the simulation time. Since carboplatin-carboplatin interactions are involved in determining drug-loading capacity and releasing processes in BNNT for drug delivery systems, the distance between the center of mass of the drugs and hydrogen bonds formed between adjacent carboplatin molecules was monitored. The distance between the center of mass of the drugs was

![](./images/814532721404542977_4.jpg)

Fig. 4. Hydrogen bond occupancy among (a) hydroxyl groups and water molecules O-H...O (black lines), N sites and water molecules N-H...O (red lines) in functionalized boron nitride nanotube; (b) N sites and water molecules N-H...O in pristine boron nitride nanotube. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

Please cite this article as: Khatti, Z., Hashemianzadeh, S.M., Boron nitride nanotube as a delivery system for platinum drugs: Drug encapsulation and diffusion coefficient prediction, European Journal of Pharmaceutical Sciences (2016), http://dx.doi.org/10.1016/j.ejps.2016.04.011

![](./images/814532721404542977_5.jpg)

Fig. 5. Distance between the center of mass and hydrogen bond occupation between the four carboplatin pairs: drug 1-2, drug 2-3, drug 3-4 and drug 4-5 are colored by black, red, blue and green, respectively. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

plotted in Fig. 5(a-d) for the 2- to 5-carboplatin systems, respectively. Additionally, at the bottom of Fig. 5(a-d), hydrogen bonding between adjacent drug molecules was measured.

Based on the mean distance value of the center of mass of the drugs for the four systems with more than one carboplatin molecule inside each FBNNT, the formation of hydrogen bonds was observed by decreasing distance. The hydrogen bond among carboplatin molecules was compared in Fig. 5 as well. The percentage occupancy of hydrogen bonds in the 5-Drug_BNNT was significantly higher than those of the other systems; Fig. 6, which implies a system with a high drug concentration, shows that hydrogen bond interactions play an important role in the localization of the encapsulated carboplatin molecules in FBNNT. Furthermore, in other systems with low drug loading, hydrogen bonds with an occupation percentage of <50% among drug molecules were detected. By increasing the drug loading per FBNNT, interactions among drugs were influential in the drug displacement within the FBNNT cavity for higher drug-loading capacity. Additionally, localization of drug molecules close to each other through the hydrogen bond interactions among themselves leads to faster diffusion of drugs from the tube in releasing processes for drug delivery systems.

### 3.4. Non-bonding interactions between carboplatin and FBNNT

According to reported results, adsorption of platinum-based drugs onto BNNTs using the density functional theory method indicated that BNNTs have no tendency to adsorb these drugs; moreover, the encapsulation of platinum drugs inside the BNNTs is more favorable than the adsorption of these drugs outside of the nanotubes (Mahdavifar and Moridzadeh, 2013; Shakerzadeh and Noorizadeh, 2014). Therefore, to discern the characteristics of the interaction between carboplatin and the FBNNT inner surface in each system, carboplatin-FBNNT electrostatic and van der Waals non-bonding interaction energies were calculated from the trajectories. The non-bond van der Waals energy (Evdw) is plotted in Fig. 7. In addition, Table 3 shows the Evdw and Eele (the electrostatic energy) values per unit of drug molecule for all i-Drug_FBNNT systems where i is 1-5. From the table, we find that the energy due to electrostatic is almost zero for all cases and vdW interactions play a crucial role in the molecular encapsulation. Furthermore, it is clear that the van der Waals energy decreases as the drug in the FBNNT cavity increases in the 4-Drug_FBNNT system. The presence of another carboplatin molecule per FBNNT in the case of the system containing the highest carboplatin loadings reduces the interaction between the drugs and the BNNT inner surface. These results clearly demonstrate

![](./images/814532721404542977_6.jpg)

Fig. 6. Percent occupations of H-bond formation among carboplatin molecules of the corresponding i-Drug system, where i is 2-5, shown in different colors.

Please cite this article as: Khatti, Z., Hashemianzadeh, S.M., Boron nitride nanotube as a delivery system for platinum drugs: Drug encapsulation and diffusion coefficient prediction, European Journal of Pharmaceutical Sciences (2016), http://dx.doi.org/10.1016/j.ejps.2016.04.011

![](./images/814532721404542977_7.jpg)

Fig. 7. The non-bond van der Waals energy between FBNNT and all drugs in each i-Drug_FBNNT system where i is 1-5, shown with different colors.

that increasing the loading of carboplatin molecules inside each FBNNT decreases the drug binding interaction with its transporter.

## 4. Conclusion

In this study, molecular diffusion of carboplatin and water inside a zigzag (18,0) open-ended single-walled BNNT (14 Å diameter and 40 Å length) and a functionalized BNNT having 18 hydroxyl groups linked to B sites of one tube edge were investigated using classical MD simulations. Because of the faster diffusion rate of water molecules inside the FBNNT, the penetration rate of drug in FBNNT obviously was larger than that in the BNNT. Furthermore, the electrostatic interaction between carboplatin and hydroxyl groups on tube edge due to favorable water-mediated hydrogen bonding enhanced the permeation rate of the drugs into the nanotube cavity. Hence, carboplatin molecules were easily and quickly encapsulated into the functionalized boron nitride nanotube. Additionally, the encapsulation of various carboplatin molecules from one to five molecules inside functionalized BNNT was investigated. In all systems, carboplatin molecules always located inside the FBNNT due to the non-bonded van der Waals interaction between the drugs and the inner surface of the FBNNT, as well as the interaction among carboplatin molecules themselves through the hydrogen bond formation. At high drug concentration (five carboplatin molecules per FBNNT), the formation of hydrogen bonds between carboplatin molecules encapsulated in FBNNT was increased and the interaction energy between the drugs and the FBNNT inner surface was decreased. Consequently, interactions among drugs and the FBNNT surface were influential in the drug displacement within the FBNNT cavity for higher drug-loading capacity.

### Table 3
The non-bond van der Waals energy values per unit of drug molecule for each i-Drug_FBNNT system where i is 1-5.

<table>
  <thead>
    <tr>
      <th>System</th>
      <th>Energy vdw (kcal mol⁻¹) per drug</th>
      <th>Energy ele (kcal mol⁻¹)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1-Drug_FBNNT</td>
      <td>−43.0 ± 0.6</td>
      <td>0.018 ± 0.6</td>
    </tr>
    <tr>
      <td>2-Drug_FBNNT</td>
      <td>−45.2 ± 0.5</td>
      <td>0.032 ± 0.4</td>
    </tr>
    <tr>
      <td>3-Drug_FBNNT</td>
      <td>−46.3 ± 0.9</td>
      <td>0.207 ± 0.5</td>
    </tr>
    <tr>
      <td>4-Drug_FBNNT</td>
      <td>−46.8 ± 0.6</td>
      <td>−0.139 ± 0.6</td>
    </tr>
    <tr>
      <td>5-Drug_FBNNT</td>
      <td>−45.4 ± 0.7</td>
      <td>−0.897 ± 0.5</td>
    </tr>
  </tbody>
</table>

## Acknowledgements

We are grateful to AMBER developers, especially Prof. David Case of Rutgers University and Prof. Ray Luo of the University of California, Irvine, for user support. The authors give special thanks to S. Skies for editing this manuscript.

## References

Adeli, M., Hakimpoor, F., Ashiri, M., Kabiri, R., Bavadi, M., 2011. Anticancer drug delivery systems based on noncovalent interactions between carbon nanotubes and linear-dendritic copolymers. Soft Matter 7, 4062-4070.

Ajima, K., Murakami, T., Mizoguchi, Y., Tsuchida, K., Ichihashi, T., lijima, S., Yudasaka, M., 2008. Enhancement of in vivo anticancer effects of cisplatin by incorporation inside single-wall carbon nanohorns. ACS Nano 2, 2057-2064.

Arlt, M., Haase, D., Hampel, S., Oswald, S., Bachmatiuk, A., Klingeler, R., Schulze, R., Ritschel, M., Leonhardt, A., Fuessel, S., Buchner, B., Kraemer, K., Wirth, M.P., 2010. Delivery of carboplatin by carbon-based nanocontainers mediates increased cancer cell death. Nanotechnology 21, 335101.

Baughman, R.H., Zakhidov, A.A., de Heer, W.A., 2002. Carbon nanotubes-the route toward applications. Science 297, 787-792.

Bottini, M., Bruckner, S., Nika, K., Bottini, N., Bellucci, S., Magrini, A., Bergamaschi, A., Mustelin, T., 2006. Multi-walled carbon nanotubes induce T lymphocyte apoptosis. Toxicol. Lett. 160, 121-126.

Case, D., Darden, T., Cheatham III, T., Simmerling, C., Wang, J., Duke, R., Luo, R., Walker, R., Zhang, W., Merz, K., 2012. AMBER 12. 1. University of California, San Francisco, p. 3.

Cerutti, D.S., Duke, R., Freddolino, P.L., Fan, H., Lybrand, T.P., 2008. Vulnerability in popular molecular dynamics packages concerning Langevin and Andersen dynamics. J. Chem. Theory Comput. 4, 1669-1680.

Chen, X., Wu, P., Rousseas, M., Okawa, D., Gartner, Z., Zettl, A., Bertozzi, C.R., 2009. Boron nitride nanotubes are noncytotoxic and can be functionalized for interaction with proteins and cells. J. Am. Chem. Soc. 131, 890-891.

Chigo Anota, E., Cocoletzi, G.H., 2013. First-principles simulations of the chemical functionalization of (5,5) boron nitride nanotubes. J. Mol. Model. 19, 2335-2341.

Ciofani, G., 2010. Potential applications of boron nitride nanotubes as drug delivery systems. Expert Opin. on Drug Deliv. 7, 889-893.

Ciofani, G., Raffa, V., Menciassi, A., Cuschieri, A., 2008. Cytocompatibility, interactions, and uptake of polyethyleneimine-coated boron nitride nanotubes by living cells: confirmation of their potential for biomedical applications. Biotechnol. Bioeng. 101, 850-858.

Ciofani, G., Genchi, G.G., Liakos, I., Athanassiou, A., Dinucci, D., Chiellini, F., Mattoli, V., 2012. A simple approach to covalent functionalization of boron nitride nanotubes. J. Colloid Interface Sci. 374, 308-314.

Ciofani, G., Danti, S., Nitti, S., Mazzolai, B., Mattoli, V., Giorgi, M., 2013. Biocompatibility of boron nitride nanotubes: an up-date of in vivo toxicological investigation. Int. J. Pharm. 444, 85-88.

Ciofani, G., Del Turco, S., Rocca, A., de Vito, G., Cappello, V., Yamaguchi, M., Li, X., Mazzolai, B., Basta, G., Gemmi, M., Piazza, V., Golberg, D., Mattoli, V., 2014. Cytocompatibility evaluation of gum Arabic-coated ultra-pure boron nitride nanotubes on human cells. Nanomedicine (Lond) 9, 773-788.

Please cite this article as: Khatti, Z., Hashemianzadeh, S.M., Boron nitride nanotube as a delivery system for platinum drugs: Drug encapsulation and diffusion coefficient prediction, European Journal of Pharmaceutical Sciences (2016), http://dx.doi.org/10.1016/j.ejps.2016.04.011

Cohen, M.L., Zettl, A., 2010. The physics of boron nitride nanotubes. Phys. Today 63,
34-38.

Cundari, T.R., Fu, W., Moody, E.W., Slavin, L.L., Snyder, L.A., Sommerer, S.O., Klinckman,
T.R., 1996. Molecular mechanics force field for platinum coordination complexes.
J. Phys. Chem. 100, 18057-18064.

Duverger, E., Gharbi, T., Delabrousse, E., Picaud, F., 2014. Quantum study of boron nitride
nanotubes functionalized with anticancer molecules. Physical chemistry chemical
physics: PCCP 16, 18425-18432.

Ebbesen, T.W., 1996. Wetting, filling and decorating carbon nanotubes. J. Phys. Chem.
Solids 57, 951-955.

Essmann, U., Perera, L., Berkowitz, M.L., Darden, T., Lee, H., Pedersen, L.G., 1995. A smooth
particle mesh Ewald method. J. Chem. Phys. 103, 8577-8593.

Hampel, S., Kunze, D., Haase, D., Krämer, K., Rauschenbach, M., Ritschel, M., Leonhardt, A.,
Thomas, J., Oswald, S., Hoffmann, W., Büchner, B., 2008. Carbon nanotubes filled with a
chemotherapeutic agent: a nanocarrier mediates inhibition of tumor cell growth.
Nanomedicine 3, 175-182.

Hilder, T.A., Gordon, D., Chung, S.-H., 2009. Salt rejection and water transport through
boron nitride nanotubes. Small 5, 2183-2190.

Ikuno, T., Sainsbury, T., Okawa, D., Fréchet, J.M.J., Zettl, A., 2007. Amine-functionalized
boron nitride nanotubes. Solid State Commun. 142, 643-646.

Jorgensen, W.L., Chandrasekhar, J., Madura, J.D., Impey, R.W., Klein, M.L., 1983. Compari-
son of simple potential functions for simulating liquid water. J. Chem. Phys. 79,
926-935.

Kelland, L., 2007. The resurgence of platinum-based cancer chemotherapy. Nat. Rev. Can-
cer 7, 573-584.

Khatti, Z., Hashemianzadeh, S., 2015. Investigation of thermodynamic and structural
properties of drug delivery system based on carbon nanotubes as a carboplatin
drug carrier by molecular dynamics simulations. J. Incl. Phenom. Macrocycl. Chem.
83, 131-140.

Lahiri, D., Rouzaud, F., Richard, T., Keshri, A.K., Bakshi, S.R., Kos, L., Agarwal, A., 2010. Boron
nitride nanotube reinforced polylactide-polycaprolactone copolymer composite:
mechanical properties and cytocompatibility with osteoblasts and macrophages
in vitro. Acta Biomater. 6, 3524-3533.

Laohpongspaisan, C., Rungrotmongkol, T., Intharathep, P., Malaisree, M., Decha, P.,
Aruksakunwong, O., Sompornpisut, P., Hannongbua, S., 2009. Why amantadine
loses its function in influenza M2 mutants: MD simulations. J. Chem. Inf. Model. 49,
847-852.

Lee, C., Drelich, J., Yap, Y., 2009. Superhydrophobicity of boron nitride nanotubes grown
on silicon substrates. Langmuir 25, 4853-4860.

Lee, C.H., Zhang, D., Yap, Y.K., 2012. Functionalization, dispersion, and cutting of boron ni-
tride nanotubes in Water. J. Phys. Chem. C 116, 1798-1804.

Lewinski, N., Colvin, V., Drezek, R., 2008. Cytotoxicity of nanoparticles. Small 4, 26-49.

Li, X., Zhi, C., Hanagata, N., Yamaguchi, M., Bando, Y., Golberg, D., 2013. Boron Nitride
Nanotubes Functionalized with Mesoporous Silica for Intracellular Delivery of Che-
motherapy Drugs. Chemical Communications.

Mahdavifar, Z., Moridzadeh, R., 2013. Theoretical prediction of encapsulation and adsorp-
tion of platinum-anticancer drugs into single walled boron nitride and carbon nano-
tubes. J. Incl. Phenom. Macrocycl. Chem. 79, 443-457.

Mayo, S.L., Olafson, B.D., Goddard, W.A., 1990. DREIDING: a generic force field for molec-
ular simulations. J. Phys. Chem. 94, 8897-8909.

McWhinney, S.R., Goldberg, R.M., McLeod, H.L., 2009. Platinum neurotoxicity pharmaco-
genetics. Mol. Cancer Ther. 8, 10-16.

Negureanu, L., Salsbury, F.R., 2013. Non-specificity and synergy at the binding site of the
carboplatin-induced DNA adduct via molecular dynamics simulations of the MutSα-
DNA recognition complex. J. Biomol. Struct. Dyn. 32, 969-992.

Nunthaboot, N., Rungrotmongkol, T., Malaisree, M., Kaiyawet, N., Decha, P., Sompornpisut,
P., Poovorawan, Y., Hannongbua, S., 2010. Evolution of human receptor binding affin-
ity of H1N1 hemagglutinins from 1918 to 2009 pandemic influenza a virus. J. Chem.
Inf. Model. 50, 1410-1417.

Pal, S., Vivekchand, S.R.C., Govindaraj, A., Rao, C.N.R., 2007. Functionalization and solubili-
zation of BN nanotubes by interaction with Lewis bases. J. Mater. Chem. 17, 450-452.

Saikia, N., Jha, A.N., Deka, R.C., 2013. Interaction of Pyrazinamide Drug Functionalized Car-
bon and Boron Nitride Nanotubes with pncA Protein: A Molecular Dynamics and
Density Functional Approach. RSC Advances.

Salvetti, A., Rossi, L., Iacopetti, P., Li, X., Nitti, S., Pellegrino, T., Mattoli, V., Golberg, D.,
Ciofani, G., 2015. In vivo biocompatibility of boron nitride nanotubes: effects on
stem cell biology and tissue regeneration in planarians. Nanomedicine (Lond) 10,
1911-1922.

Schmidt, M.W., Baldridge, K.K., Boatz, J.A., Elbert, S.T., Gordon, M.S., Jensen, J.H., Koseki, S.,
Matsunaga, N., Nguyen, K.A., Su, S., Windus, T.L., Dupuis, M., Montgomery, J.A., 1993.
General atomic and molecular electronic structure system. J. Comput. Chem. 14,
1347-1363.

Shakerzadeh, E., Noorizadeh, S., 2014. A first principles study of pristines and Al-doped
boron nitride nanotubes interacting with platinum-based anticancer drugs. Physica
E 57, 47-55.

Sharma, A., Jain, N., Sareen, R., 2013. Nanocarriers for diagnosis and targeting of breast
cancer. BioMed research international 2013.

Shiuchi Miyamoto, P.A.K., 1992. Settle: an analytical version of the SHAKE and RATTLE al-
gorithm for rigid water models. J. Comput. Chem. 13, 952-962.

Simonetti, S., Compañy, A.D., Brizuela, G., Juan, A., 2011. Theoretical study of cisplatin ad-
sorption on silica. Appl. Surf. Sci. 258, 1052-1057.

Sugino, T., Tai, T., Etou, Y., 2001. Synthesis of boron nitride film with low dielectric con-
stant for its application to silicon ultralarge scale integrated semiconductors. Diam.
Relat. Mater. 10, 1375-1379.

Todd, R.C., Lippard, S.J., 2009. Inhibition of transcription by platinum antitumor com-
pounds. Metallomics 1, 280-291.

Wang, J., Hou, T., 2011. Application of molecular dynamics simulations in molecular prop-
erty prediction II: diffusion coefficient. J. Comput. Chem. 32, 3505-3519.

Wang, D., Lippard, S.J., 2005. Cellular processing of platinum anticancer drugs. Nat. Rev.
Drug Discov. 4, 307-320.

Wang, J., Wolf, R.M., Caldwell, J.W., Kollman, P.A., Case, D.A., 2004. Development and test-
ing of a general amber force field. J. Comput. Chem. 25, 1157-1174.

Wang, W., Bando, Y., Zhi, C., Fu, W., Wang, E., Golberg, D., 2008. Aqueous noncovalent
functionalization and controlled near-surface carbon doping of multiwalled boron ni-
tride nanotubes. J. Am. Chem. Soc. 130, 8144-8145.

Wang, J., Lee, C.H., Yap, Y.K., 2010. Recent advancements in boron nitride nanotubes.
Nanoscale 2, 2028-2034.

Weng, Q., Wang, B., Wang, X., Hanagata, N., Li, X., Liu, D., Jiang, X., Bando, Y., Golberg, D.,
2014. Highly water-soluble, porous, and biocompatible boron nitrides for anticancer
drug delivery. ACS Nano 8, 6123-6130.

Williams, K.M., Rowan, C., Mitchell, J., 2004. Effect of amine ligand bulk on the interaction
of methionine with platinum(II) diamine complexes. Inorg. Chem. 43, 1190-1196.

Won, C.Y., Aluru, N.R., 2008a. Structure and dynamics of Water confined in a boron nitride
nanotube. J. Phys. Chem. C 112, 1812-1818.

Won, C.Y., Aluru, N.R., 2008b. Water phase transition induced by a Stone-Wales defect in a
boron nitride nanotube. J. Am. Chem. Soc. 130, 13649-13652.

Wong, C.H., Vijayaraghavan, V., 2014. Compressive characteristics of single walled carbon
nanotube with water interactions investigated by using molecular dynamics simula-
tion. Phys. Lett. A 378, 570-576.

Xie, S.Y., Wang, W., Fernando, K.A., Wang, X., Lin, Y., Sun, Y.P., 2005. Solubilization of
boron nitride nanotubes. Chem. Commun. (Camb.) 3670-3672.

Yao, S., Plastaras, J.P., Marzilli, L.G., 1994. A molecular mechanics AMBER-type force field
for modeling platinum complexes of guanine derivatives. Inorg. Chem. 33,
6061-6077.

Zhi, C.Y., Bando, Y., Terao, T., Tang, C.C., Kuwahara, H., Golberg, D., 2009. Chemically acti-
vated boron nitride nanotubes. Chem. Asian J. 4, 1536-1540.

Zhi, C., Hanagata, N., Bando, Y., Golberg, D., 2011. Dispersible shortened boron nitride
nanotubes with improved molecule-loading capacity. Chem. Asian J. 6, 2530-2535.

Please cite this article as: Khatti, Z., Hashemianzadeh, S.M., Boron nitride nanotube as a delivery system for platinum drugs: Drug encapsulation
and diffusion coefficient prediction, European Journal of Pharmaceutical Sciences (2016), http://dx.doi.org/10.1016/j.ejps.2016.04.011