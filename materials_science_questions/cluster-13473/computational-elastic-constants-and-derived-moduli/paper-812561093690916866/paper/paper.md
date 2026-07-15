**RESEARCH ARTICLE**

# A comparative study on enhancement of mechanical and tribological properties of nitrile rubber composites reinforced by different functionalized graphene sheets: Molecular dynamics simulations

Jianzheng Cui¹ | Jing Zhao¹ | Shijie Wang¹ | Yunlong Li² ![](./images/812561093690916866_1.jpg)

¹School of Mechanical Engineering, Shenyang University of Technology, Shenyang, Liaoning, China
²College of Engineering, Shantou University, Shantou, Guangdong, China

## Correspondence
Yunlong Li, College of Engineering, Shantou University, Shantou, Guangdong 515063, China.
Email: yunlongli@stu.edu.cn

## Funding information
National Natural Science Foundation of China, Grant/Award Number: 51903148; Special Program for Local Science and Technology Development of the Ministry of Science and Technology, China, Grant/Award Number: 2030JH6/10500016; Start-Up Fund of Scientific Research of Shantou University, China, Grant/Award Number: NTF19018

---

## Abstract
Molecular dynamics (MD) simulations were adopted to compare the enhanced mechanical and tribological properties of nitrile rubber composites reinforced by different functionalized graphene sheets. Functional groups such as hydroxyl ($\text{—OH}$), carboxyl ($\text{—COOH}$), and ester ($\text{—COOCH}_3$) were adopted. The constant strain method was applied to measure the mechanical properties of graphene/nitrile rubber composites. Sandwiched molecular models were developed to investigate the tribological properties of graphene/nitrile rubber composites by applying a shear load. The MD simulation results showed that the incorporation of functionalized graphene enhanced the Young's modulus, bulk modulus, and shear modulus of the nitrile rubber matrix. In addition, the coefficient of friction and abrasion rate of the functionalized graphene/nitrile rubber composites decreased. The mechanisms for the interfacial interactions between the functionalized graphene and nitrile rubber matrix were determined by calculating the mean square displacement of rubber chains, binding energy, and the radial distribution function between functional groups and polar atoms in the rubber matrix, respectively. The results of the atomistic simulations indicated that stronger interfacial interactions and better stability and dispersion of graphene in rubber matrices can be obtained by introducing functionalized graphene. Owing to the combination of hydrogen bonding and strong van der Waals interactions, the COOH-functionalized graphene behaves the best effect on the enhancement of mechanical and tribological properties of the nitrile rubber composites.

## KEYWORDS
adhesion, interfaces, mechanical properties, molecular dynamics, Nanocomposites

---

## 1 | 1. INTRODUCTION

Polymer-based composites have been widely used in industries owing to their excellent properties such as oil and abrasion resistance, viscoelasticity, and self-lubrication.${}^{[1-3]}$ Numerous studies have shown that the mechanical and tribological properties of polymer-based nanocomposites can be enhanced by the inherent properties and special structure of nanofillers. For example, because of its high specific surface area, nanosilica has

---
Polymer Composites. 2020;1-15.
wileyonlinelibrary.com/journal/pc
© 2020 Society of Plastics Engineers

been applied as a reinforcement for polymer composites. $^{[4,5]}$ Ma et al $^{[6]}$ investigated the mechanical and tribochemical properties of polyimide (PI)/mesoporous silica (MPS) nanocomposites. They found that the elastic modulus, microhardness, and anti-wear resistance of PI/MPS nanocomposites can be improved by the incorporation of 1.5 wt.% of MPS. Furthermore, carbon nanotubes (CNTs) with a Young's modulus as high as 1 TPa and tensile strength higher than 1 GPa are ideal nanofillers for improving the mechanical and tribological properties of polymer-matrix composites. $^{[7-10]}$ Wang et al $^{[11]}$ studied the mechanical and tribological properties of epoxy composites incorporated with polyvinylidene fluoride (PVDF) and CNTs. The results showed that the mechanical and tribological capabilities of PVDF composites can be efficiently enhanced by adding CNTs as reinforcement, particularly at a concentration of 1.0 wt.%.

Recently, graphene sheets (GNSs) have been regarded as the most promising nanofiller for enhancing the mechanical and tribological properties of polymer-based composites due to their outstanding structural, physical, and mechanical properties. $^{[12-14]}$ Moreover, GNSs play a better role in delaying propagation of cracks compared to CNTs because of their larger specific surface area. $^{[15]}$ However, due to the strong interparticle interaction, agglomeration can be commonly observed in GNS-reinforced polymer composites. To uniformly disperse GNSs within a polymer, functionalization of the GNS was proposed. $^{[16]}$ Ramanathan et al $^{[17]}$ studied the mechanical and thermal properties of polymer composites reinforced by functionalized GNSs. The results indicated that the oxygen-containing functional groups on the functionalized GNSs were suitable for the formation of composites with polar polymers such as polyacrylonitrile. Gudarzi et al $^{[18]}$ studied the enhancement of the dispersion and bonding of amino-functionalized graphene oxide (GO)/epoxy composites. Li et al $^{[19]}$ studied the tribological properties of GO/nitrile rubber (NBR) nanocomposites. The results showed that the hydrophilic groups of GO are capable of forming greater interfacial interactions within the NBR matrix, leading to a significant improvement in the tribological properties. Conducting experimental studies is the most common approach to the study and development of high-performance polymer nanocomposites. Nevertheless, time-consuming and expensive experiments with limited length and time scales impose significant limitations on the qualitative and quantitative studies of nanocomposites at the microscale.

In view of the above issue, computational methods, such as molecular dynamics (MD) simulations, have been extensively developed and applied in simulating interactions occurring in multiscale simulations and cross-scale analysis. $^{[20-25]}$ Arash et al $^{[26]}$ proposed a novel MD simulation method to measure the mechanical properties, such as Young's modulus and yield strength, of the interfacial region between CNTs and a poly (methyl methacrylate) matrix. Wei et al $^{[27]}$ applied MD simulations to investigate the enhanced mechanical and tribological properties of nanosilica-reinforced polyvinyl alcohol (PVA)/polyacrylamide (PAM) composites. Analysis of the binding energies and pair-correlation functions indicated that the incorporation of nanosilica improves the internal binding strength between different components. Li et al $^{[28]}$ studied the improved tribological properties of CNT-reinforced polymer composites using MD simulations by developing a tribological molecular model. The results showed that the decrease of 38% and 60% in the coefficient of friction (COF) and abrasion rate (AR) of the composites, respectively, were obtained by introducing CNTs under different normal loadings. Li et al $^{[29]}$ conducted a MD simulation to study the tribological properties of hydroxyl groups ($-$OH)-functionalized GNS-reinforced polymer composites. The results showed that a higher interfacial interaction energy can be acquired with the addition of OH-functionalized GNS, resulting in a better anti-friction property. Although many MD simulations have been conducted to study the mechanical and tribological properties of nanofiller-reinforced polymer composites, very few MD-based studies have been carried out to investigate the inherent influences on the mechanical and tribological properties of polymer composites reinforced by various functionalized GNSs. To the authors' knowledge, previous works have highlighted the lack of comparative studies on different functional groups.

We performed a comprehensive and comparative MD simulation study on the mechanical and tribological capabilities of polymer composites by introducing a GNS modified with various functional groups. The NBR material with perfect processability, $^{[30]}$ a kind of polar rubbers extensively used in petroleum industries and mechanical seals owing to its superior oil-resistance, was adopted as the polymer matrix. The functional groups grafted on the surfaces of the GNSs were hydroxyl ($-$OH), carboxyl ($-$COOH), and ester ($-$COOCH$_3$). The Young's modulus, shear modulus, and bulk modulus of these GNS/NBR composites were calculated via the constant strain method. The COF and AR were calculated to predict the tribological properties of the GNS/NBR composites. The interfacial frictional properties of the functionalized GNS-reinforced NBR matrix were studied by analyzing the temperature and relative concentration distributions as well as the total potential energies of the GNS/NBR composites during friction processes. To determine the atomic mechanisms of enhancements in the mechanical

and tribological properties of the GNS/NBR composites, the binding energy, free volume (FV), mean square dis- placement (MSD) of the NBR chains, and radial distribu- tion function (RDF) between hydrogen and nitrogen atoms in the NBR matrix and the attached functional groups were calculated. This study provides theoretical predictions and a scientific basis for the surface-modified GNS/polar polymer composites.

## 2 | MODELING AND METHOD

### 2.1 | Composite construction

To investigate the effects of the GNS-reinforced NBR with different functional groups, four kinds of atomistic models, that is, pristine graphene (PGNS)/NBR, hydroxyl-functionalized graphene (OH-GNS)/NBR, carboxyl-functionalized graphene (COOH-GNS)/NBR, and ester-functionalized graphene (COOCH₃-GNS)/NBR matrices, were constructed as shown in Figure 1. All the four models were constructed using similar protocols; hence, only the COOH-GNS/NBR model is discussed in detail here.

In the modeling, a single-layer COOH-functionalized GNS with a size of $3.92 \times 2.41\ \text{nm}^2$, as shown in Figure 1E, was initially constructed and located at the center of the periodic unit cell with a size of $4.5 \times 3.0 \times 3.0\ \text{nm}^3$. For the COOH-functionalized GNS, 32 carboxyl groups were uniformly distributed on both sides of the GNS. Additionally, to avoid the effects of unsaturated boundary conditions, $^{[31]}$ all the GNS

![](./images/812561093690916866_2.jpg)

FIGURE 1 Molecular models: A, pristine GNS/NBR; B, functionalized GNS/NBR composites; C, pristine GNS; D, OH-functionalized GNS; E, COOH-functionalized GNS; F, COOCH₃-functionalized GNS. In the snapshots, the green color represents the NBR matrix, the nanosheets denote the GNS. The white, gray and red color present elements of hydrogen, carbon and oxygen respectively [Color figure can be viewed at wileyonlinelibrary.com]

reinforcements were edge-grafted by hydrogen atoms. A repeat unit was made from acrylonitrile ($\text{C}_3\text{H}_3\text{N}$) and 1,3 butadiene ($\text{CH}_2{=}\text{CH}{-}\text{CH}{=}\text{CH}_2$) in a 1:1 allocation ratio. A single NBR chain consisting of 20 repeat units was then continuously packed into the simulation cell with a target density of $0.97\ \text{g/cm}^3$. The information of the GNS/NBR composite models is listed in Table 1.

To attain global and local minimum energy configu- rations, an equilibration process, which contains geome- try optimizations followed by MD simulations, was performed. First, geometry optimization was conducted using the conjugate gradient algorithm$^{[32]}$ with an energy convergence of $10^{-5}$ kcal/mol. Then, to eliminate the internal stress of the composites, the system was equili- brated for 1 ns in the NVT (constant volume, constant temperature) ensemble at a temperature of 298 K. Finally, an NPT (constant pressure, constant tempera- ture) simulation was performed at a temperature and pressure of 298 K and 101 KPa, respectively, for 1 ns. Materials Studio (MS) 2018 software was used to con- duct all molecular modelings and MD simulations. The COMPASS force field,$^{[33]}$ which is an ab-initio force field that can accurately predict structural characteristics of a wide range of molecules and polymers,$^{[34]}$ was implemented. The time step for all the simulations was 1 fs, and the temperature and pressure were controlled by the Andersen thermostat$^{[35]}$ and Berendsen barostat,$^{[36]}$ respectively. Electrostatic and van der Waals (vdW) interac- tions were calculated by an Ewald summation method$^{[37]}$ with an accuracy of 0.001 kcal/mol and atom-based sum- mation method with a cutoff distance of 1.25 nm, respectively.

<table><caption>TABLE 1 The information of GNS/NBR composites models</caption>
<thead>
<tr>
<th rowspan="2">Composites</th>
<th>NBR</th>
<th rowspan="2">Number of NBR chains</th>
<th rowspan="2">Number of total atoms</th>
</tr>
<tr>
<th>chain length</th>
</tr>
</thead>
<tbody>
<tr>
<td>PGNS/NBR</td>
<td>20</td>
<td>20</td>
<td>3836</td>
</tr>
<tr>
<td>$\text{COOCH}_3$-GNS/NBR</td>
<td>20</td>
<td>19</td>
<td>3888</td>
</tr>
<tr>
<td>OH-GNS/NBR</td>
<td>20</td>
<td>20</td>
<td>3900</td>
</tr>
<tr>
<td>COOH-GNS/NBR</td>
<td>20</td>
<td>20</td>
<td>3964</td>
</tr>
</tbody>
</table>

## 2.2 | Mechanical properties

The mechanical properties of the GNS/NBR composites were characterized by evaluating their Young's modulus, bulk modulus, and shear modulus. An additional simula- tion in the NVT ensemble (298 K) was carried out for 200 ps on each well-relaxed structure obtained in Sec- tion 2.1. We used the last 40 snapshots of the trajectory. The constant strain method was adopted by applying four strains in each Cartesian direction, and the maximum strain amplitude was 0.003, as shown in Figure 2. Every strained configuration was optimized to undergo internal relaxation. The stress in each direction was then calcu- lated according to the virial stress definition.$^{[38]}$ The Young's modulus in each Cartesian direction can be cal- culated by the expression of $E_i=\frac{\sigma_i}{\varepsilon_i}$. To describe the stress-strain behavior, the $6\times6$ stiffness $(C_{ij})$ and compli- ance $(S_{ij})$ matrices can be obtained using the following relations: $\sigma_i=C_{ij}\varepsilon_j$ and $\varepsilon_i=S_{ij}\sigma_j$. To determine the bulk modulus $B$ and shear modulus $G$, Voigt-Reuss-Hill approximations$^{[39]}$ can be used.

The upper limits of $B$ and $G$ are determined by the following Voigt expressions:

![](./images/812561093690916866_3.jpg)

FIGURE 2 Schematic diagram of the constant strain method: A, axial strain; B, plane shear [Color figure can be viewed at wileyonlinelibrary.com]

$$B_{V}=\left[C_{11}+C_{22}+C_{33}+2 C_{12}+2 C_{13}+2 C_{23}\right] / 9 \quad (1)$$

$$G_{V}=\left[C_{11}+C_{12}+C_{33}+3 C_{44}+3 C_{55}+3 C_{66}-C_{12}-C_{13}-C_{23}\right] / 15$$

(2)

The lower limits of $B$ and $G$ are determined by the following Reuss expressions:

$$B_{R}=1 /\left(S_{11}+S_{22}+S_{33}+2 S_{12}+2 S_{13}+2 S_{23}\right) \quad (3)$$

$$G_{R}=15 /\left[4\left(S_{11}+S_{22}+S_{33}-S_{12}-S_{13}-S_{23}\right)+3\left(S_{44}+S_{55}+S_{66}\right)\right]$$

(4)

Finally, the actual values of $B$ and $G$ are determined by the Hill's definition, that is, averaging the corresponding values of $B$ (Equation (1) and (3)) and $G$ (Equation (2) and (4)) obtained from the Voigt's and Reuss' definitions. The corresponding equations are given as follows:

$$B_{H}=\left[B_{V}+B_{R}\right] / 2 \quad (5)$$

$$G_{H}=\left[G_{V}+G_{R}\right] / 2 \quad (6)$$

## 2.3 | Friction process

To investigate the tribological properties of the surface-functionalized GNS-reinforced NBR composites, a three-layer molecular model was proposed, as schematically shown in Figure 3. Fe atom layers (shown in Figure 4) with dimensions $0.28 \times 0.28 \times 1.71 \mathrm{~nm}^{3}$ and $4.58 \times 2.86$ $\times 1.71 \mathrm{~nm}^{3}$ were developed and used as the top and bottom slip planes, respectively. Energy minimization was performed using the conjugate gradient method. A five-cycle annealing simulation with an initial temperature of 150 K and mid-cycle temperature of 350 K in the NVT ensemble was conducted for 200 ps. The friction process on the surface of the GNS/NBR composites were realized by applying a shear load to the top Fe layer at a speed of $0.1 \AA /$ ps for 600 ps under a depth at the nanoindentation of $0.03 \mathrm{~nm} .{ }^{[4,40]}$

The tribological properties were characterized by calculating the COF and AR of the composites. The COF can be determined by the expression $\mu=\frac{F_{f}}{F_{n}}$, where $F_{f}$ and $F_{n}$ are the frictional and normal forces, respectively. According to the friction law proposed by Eder et al, ${ }^{[41]}$ the frictional force $\left(F_{f}\right)$ is calculated as $F_{f}=F_{0}+\tau A_{c}(L)$, where $F_{0}$ and $\tau$ represent the load-independent Derjaguin offset and effective shear strength, respectively, where, $A_{c}(L)$ denotes the contact area under load L. The AR can be calculated by the expression $A R=\frac{N_{\text {leave }}}{N_{\text {total }}}$, where $N_{\text {leave }}$ and $N_{\text {total }}$ represent the number of atoms that leave NBR matrices during the friction process and the total number of atoms in the original NBR matrices, respectively.

## 3 | RESULTS AND DISCUSSIONS

### 3.1 | Mechanical properties

The mechanical properties of all composites are summarized in Table 2 and Figure 5. In general, the Young's modulus $(E)$, shear modulus $\left(G_{H}\right)$, and bulk modulus $\left(B_{H}\right)$ are used to measure the material stiffness, ${ }^{[42]}$ resistance ability to shear deformation, ${ }^{[43]}$ and resistance capacity to volume change, ${ }^{[44]}$ respectively, of a rigid material under diverse stresses.

As illustrated in Table 2 and Figure 5A, the Young's moduli in the X, Y, and Z directions, shear moduli, and bulk moduli of the GNS/NBR composites were all significantly improved with the addition of the functionalized GNSs. The average Young's moduli of the NBR composites reinforced by the GNS modified with $-\mathrm{COOCH}_{3}$, $-\mathrm{OH}$, and $-\mathrm{COOH}$ functional groups were calculated as $5.13,5.68$, and $5.73 \mathrm{GPa}$, respectively. These moduli show an increase of approximately $19.6 \%, 32.4 \%$, and $33.6 \%$, respectively, as compared to that of the PGNS/NBR composite (4.29 GPa). These results are in good agreement with the experimental study. ${ }^{[45]}$ Moreover, from Figure 5B, the shear modulus values of the NBR

![](./images/812561093690916866_4.jpg)

FIGURE 3 Schematic diagram of three-layer molecular friction model [Color figure can be viewed at wileyonlinelibrary.com]

![](./images/812561093690916866_5.jpg)

FIGURE 4 Friction models: A, functionalized-GNS/NBR; B, PGNS/NBR composites. In the snapshots, the purple represents the Fe elements, the green denotes the NBR matrix [Color figure can be viewed at wileyonlinelibrary.com]

<table>
<thead>
<tr>
<th>TABLE 2 The mechanical properties of GNS/NBR composites (GPa)</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<th>Composites</th>
<th>$E_{X}$</th>
<th>$E_{Y}$</th>
<th>$E_{Z}$</th>
<th>$E_{Avg}$</th>
<th>$G_{R}$</th>
<th>$G_{V}$</th>
<th>$G_{H}$</th>
<th>$B_{R}$</th>
<th>$B_{V}$</th>
<th>$B_{H}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>PGNS/NBR</td>
<td>4.15</td>
<td>4.54</td>
<td>4.18</td>
<td>4.29</td>
<td>1.38</td>
<td>1.52</td>
<td>1.45</td>
<td>3.77</td>
<td>3.81</td>
<td>3.79</td>
</tr>
<tr>
<td>$COOCH_{3}$-GNS/NBR</td>
<td>5.10</td>
<td>5.58</td>
<td>4.71</td>
<td>5.13</td>
<td>1.78</td>
<td>1.82</td>
<td>1.80</td>
<td>3.94</td>
<td>3.98</td>
<td>3.96</td>
</tr>
<tr>
<td>OH-GNS/NBR</td>
<td>6.11</td>
<td>6.35</td>
<td>4.58</td>
<td>5.68</td>
<td>1.87</td>
<td>1.95</td>
<td>1.91</td>
<td>3.97</td>
<td>3.99</td>
<td>3.98</td>
</tr>
<tr>
<td>COOH-GNS/NBR</td>
<td>6.53</td>
<td>6.08</td>
<td>4.57</td>
<td>5.73</td>
<td>1.96</td>
<td>2.02</td>
<td>1.99</td>
<td>4.30</td>
<td>4.38</td>
<td>4.34</td>
</tr>
</tbody>
</table>

composites containing the GNS with $-COOCH_{3}$, $-OH$, and $-COOH$ functional groups are 1.80, 1.91, and 1.99 GPa, respectively. These values indicate an increase of 24.1%, 31.7%, and 37.2%, respectively, as compared to the shear modulus of 1.45 GPa of the PGNS/NBR composite (1.65 GPa by Li et al$^{[46]}$). Furthermore, the bulk moduli of the GNS/NBR composites with $-COOCH_{3}$ and $-OH$ functional groups are generally higher than that of the PGNS/NBR composite, as shown in Table 2. Similarly, a significant increase of 14.5% in the bulk modulus of COOH-functionalized GNS/NBR composite (4.34 GPa) was observed as compared to the bulk modulus of PGNS/NBR composite (3.79 GPa), thus demonstrating that the COOH-GNS/NBR composite exhibits the best resistance to volume change among the three functionalized GNS/NBR composites.

In addition, it is interesting to note that the differences in the Young's moduli of the functionalized GNS/NBR composites in the longitudinal (X, Y) and transverse (Z) directions become larger when the functionalized GNSs are introduced into the NBR matrices. This indicates that the anisotropy of the GNS/NBR composites tends to be more distinct with the addition of the functionalized GNSs. By observing the equilibrated structures of the GNS shown in Figure 6, the surface of the PGNS is smooth, curly, and easily agglomerated. In contrast, the carbon atoms connected with the functional groups form slightly distorted tetrahedral structures, thus making the surfaces of the functionalized GNSs rougher than that of the PGNS. This agrees well with experimental observations,$^{[47]}$ and it is attributed to the intermolecular interactions of the functionalized GNSs, which lead to wrinkling and high in-plane stiffness.$^{[48]}$ It, therefore, leads to effective reduction of the curling and agglomeration of the functionalized GNSs. Owing to the combination of better stabilities within the NBR matrices and the adsorption functions of the functionalized GNSs with rougher surfaces, higher resistance performances of the functionalized GNS/NBR composites to external forces can be obtained. Thus, significant increments in the Young's modulus in the X and Y directions as well as the shear and bulk moduli were observed. However, only a slight increase in the Young's modulus in the Z direction is observed in Table 2. This is because only the

![](./images/812561093690916866_6.jpg)

**FIGURE 5** The mechanical properties of GNS/NBR composites: A, Young's modulus; B, shear and bulk modulus [Color figure can be viewed at wileyonlinelibrary.com]

adsorption functions can be achieved efficiently by the functional groups when the composites are subjected to transverse (Z-direction) loading. This indicates that the roughnesses of the functionalized GNSs surfaces play a dominant role compared to the adsorption functions.

Among the functionalized GNSs, the COOH-functionalized GNS behaves the best effect on improving the mechanical properties of the NBR composites. It can be deduced that the improved stability, dispersion, and interfacial interactions of the COOH-functionalized GNS in the NBR matrix are conducive to promoting the transfer efficiency of mechanical loading, leading to significant enhancements of the mechanical properties of NBR composites. $^{[16,49,50]}$ It is generally known that the mechanical properties of polymer materials have a significant influence on their tribological performances. $^{[51]}$ Hence, the inherent mechanisms of the improved mechanical stiffness and strength of the NBR composites are further explored and extended in the next section.

### 3.2 | Tribological properties

The COF and AR of all composites were calculated and are given in Table 3. Obvious reductions in the COF and AR of the functionalized GNS/NBR composites were observed as compared to those of the PGNS/NBR composite. In particular, the COF and AR of the COOH-functionalized GNS/NBR composite decreased by as much as 30.7% and 76.2%, respectively, compared to those of the PGNS/NBR composite. This indicates that the COOH-functionalized GNS has a significant effect on improving the tribological properties of the NBR composites. These comparison results agree well with the findings of the mechanical properties of the GNS/NBR composites discussed in Section 3.1. The snapshots of the friction processes of all composites were recorded and are shown in Figure 7.

To explore the inherent mechanisms of the enhancement of mechanical and tribological properties, the binding energy between the GNS and the NBR matrix during the NVT equilibrium processes (mentioned in Section 2.1) was calculated using the following equation (Equation 7).

$$
U_{bind} = -U_{inter} = -(U_{total} - U_{NBR} - U_{GNS}), \tag{7}
$$

where $U_{total}$ represents the total energy of the composites, $U_{NBR}$ denotes the energy of the NBR matrix, and $U_{GNS}$ is the energy of the GNS.

The average values of the binding energies of the GNS/NBR composites are shown in Figure 8. The average binding energies of the NBR composites reinforced by the $COOCH_3$-, OH-, and COOH-functionalized GNSs are 623.68, 641.60, and 685.14 kcal/mol, respectively. Compared to the binding energy of the PGNS/NBR composite, that is, 5321.08 kcal/mol, the binding energies of the functionalized GNS/NBR composites increased significantly by 17.44%, 20.81%, and 29.01%, respectively. It is indicated that stronger internal binding strengths between the functionalized GNSs and NBR matrices can be achieved as compared to that between the PGNS and the NBR matrix. $^{[52-54]}$ Moreover, the composite reinforced by the COOH-functionalized GNS provides the highest binding energy. To validate the above results

![](./images/812561093690916866_7.jpg)

FIGURE 6 Equilibrated GNS
configurations in NBR composites: A,
PGNS; B, OH-GNS; C, COOH-GNS; D,
COOCH₃-GNS [Color figure can be
viewed at wileyonlinelibrary.com]

<table>
<caption>TABLE 3 The COF and AR of GNS/NBR composites</caption>
<thead>
<tr>
<th>Composites</th>
<th>COF</th>
<th>Decrease percentage (%)</th>
<th>AR (%)</th>
<th>Decrease percentage (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>PGNS/NBR</td>
<td>0.52</td>
<td>0</td>
<td>30.8</td>
<td>0</td>
</tr>
<tr>
<td>COOCH₃-GNS/NBR</td>
<td>0.48</td>
<td>7.7</td>
<td>15.9</td>
<td>48.4</td>
</tr>
<tr>
<td>OH-GNS/NBR</td>
<td>0.44</td>
<td>15.4</td>
<td>9.6</td>
<td>68.8</td>
</tr>
<tr>
<td>COOH-GNS/NBR</td>
<td>0.36</td>
<td>30.8</td>
<td>7.3</td>
<td>76.3</td>
</tr>
</tbody>
</table>

on the binding energies, the FVs of the NBR composites were analyzed based on the equilibrated structures described in Section 2.1, as shown in Figures 9 and 10. The Connolly surface is calculated when the probe molecule with a radius $(R_p)$ of $1.0$ Å rolls over the vdW surface, and the FV is determined as the volume on the side of the Connolly surface without atoms. $^{[55-56]}$

As indicated in Figure 9, the average FVs of the COOCH₃-, OH-, and COOH-functionalized GNS/NBR composites are 5686.39, 5752.74, and $5093.94$ Å³, respectively, which indicates a decrease of about 7.85%, 6.77%, and 17.45% as compared to those of the PGNS/NBR composite $(6170.83$ Å³). Evident reductions in the FV of the functionalized GNS/NBR composites show that a smaller movement space and closer entanglement of the NBR chains can be achieved by the addition of the functionalized GNSs. This indicates that more NBR chains are intended to be adsorbed on the functionalized GNS surface owing to the higher interfacial adsorption function of the functionalized GNS, thus resulting in a denser NBR matrix. It is also noted that the FV of the COOCH₃-GNS/NBR composite is slightly smaller than that of the OH-GNS/NBR composite. This is due to the better flexibility of the methyl group in the $-\text{COOCH}_3$ functional group, which is beneficial to the transmission and extrusion of the FV of the composite in confined spaces. $^{[57]}$ Overall, the COOH-functionalized GNS has the best effect on decreasing the FV of the composite, which agrees with the results on the binding energies discussed earlier.

To further explore the mechanisms of the improved tribological properties of the GNS/NBR composites, the temperature and relative concentration distributions as well as the total potential energies of the GNS/NBR composites during friction processes were determined, and are shown in Figures 11-13, respectively. In general,

**FIGURE 7** Snapshots of friction processes: A, PGNS/NBR; B, $COOCH_3$-GNS/NBR; C, OH-GNS/NBR; D, COOH-GNS/NBR composites [Color figure can be viewed at wileyonlinelibrary.com]

![](./images/812561093690916866_8.jpg)

rubber friction on a rough surface mainly involves two contributions, namely the adhesion and hysteric components.$^{[58]}$ As for the nanoscale rubber friction, adhesion contributes mainly to the friction owing to the significance of the attractive vdW forces between the frictional interface as compared to the normal loadings.$^{[59-60]}$ It can be seen in Figure 11 that under the combination of the relative sliding and shear loadings, shear deformations and adhesive frictions occurred between the NBR composites and the top Fe layers. Furthermore, the temperatures of the frictional interfaces increased to their peak values. The peak temperature values (at ~18.2 Å in the Z direction) of the NBR composites reinforced by the $COOCH_3$-GNS, OH-GNS, and COOH-GNS are 308.02, 306.15, and 282.01 K, separately. These temperatures decreased by approximately 22.14%, 22.61%, and 28.68%, respectively, as compared to the peak temperature of the frictional interface of the PGNS/NBR composite during the shear loading process. Meanwhile, the average temperature values of the $COOCH_3$- and OH-functionalized GNS/NBR composites were slightly lower than that of the PGNS/NBR composite (294.95 K). Similarly, the average temperature value of the COOH-GNS/NBR composite during the friction process was 275.43 K, thus indicating a significant decrease of approximately 6.6% as compared to that of the PGNS/NBR composite. According to the results of the binding energies and FVs, it can be understood that the incorporation of a functionalized GNS enhances the compactness and surface hardness of the NBR matrix by increasing the internal binding strength. The enhancement of the surface hardness of the NBR matrix can effectively improve the resistance capability to the adhesive friction,$^{[61]}$ leading to a lower frictional temperature. Among these

![](./images/812561093690916866_9.jpg)

FIGURE 8 Variations of the binding energy between GNS and NBR matrices during NVT simulations [Color figure can be viewed at wileyonlinelibrary.com]

![](./images/812561093690916866_10.jpg)

FIGURE 9 Free volume of GNS/NBR composites [Color figure can be viewed at wileyonlinelibrary.com]

functionalized GNSs, the introduction of the COOH-functionalized GNS is the most effective way to decrease the temperature of the composite during the friction process, which is consistent with the COF results.

Moreover, as shown in Figure 12, the degree of variation of the relative concentration distributions of the four GNS/NBR composites along the Z direction (beyond 17.75 Å) has the following order: PGNS/NBR > COOCH₃-GNS/NBR > OH-GNS/NBR > COOH-GNS/NBR, indicating that the COOH-functionalized GNS has the greatest effect on the enhancement of the wear resistance of the composite. This can also be attributed to the enhanced internal binding strengths between the functionalized GNSs and NBR matrices, and the adsorption functions provided by the functionalized GNSs. Thus, fewer NBR chains in the functionalized GNS-reinforced composites are worn by the attractive vdW forces provided by the top Fe layers, which agrees well with the AR calculation results discussed earlier. Furthermore, as depicted in Figure 13, the molecular potential energy gradually increases and tends to be stable as the friction time increases from 0 to 600 ps. This is attributed to the disturbance of the random NBR orientation, and the deformation and stretching of the NBR chains along the shear direction. This phenomenon leads to a corresponding increase in the total potential energy of the molecules (a source of the elastic force) during sliding, and it is in good agreement with the results shown in previous study.⁽⁶²⁾ Meanwhile, the average values of the total potential energies of the COOCH₃-, OH-, and COOH-functionalized GNS/NBR composites are 10 094.99, 9790.69, and 8641.28 kcal/mol, separately. These average values of the functionalized GNS/NBR composites indicate a decrease of approximately 34.96%, 36.92%, and 44.33%, respectively, as compared to the average total potential energy of the PGNS/NBR composite, that is, 15 521.69 kcal/mol. Based on discussions on the binding energies and FVs, this result can be explained by the fact that the NBR chains in the functionalized GNS-reinforced composites exhibit smaller deformations and a limited degree of motion as compared to those of the PGNS/NBR composite. This is due to the stronger interfacial interactions between the functionalized GNSs and NBR matrices. Furthermore, the COOH-functionalized GNS has the most significant effect on the stability and resistance against the shear deformation of the NBR matrix during the shear loading process. This is in agreement with the results on the mechanical properties of the GNS/NBR composites discussed earlier.

## 3.3 | Interfacial interactions

To understand the interfacial interaction mechanism, the hydrogen bonding and vdW interactions between the functionalized GNSs and NBR matrices were studied. The RDFs g(r) between the nitrogen and hydrogen atoms in the NBR matrices and functional groups, were determined by analyzing the equilibrated trajectories (NVT) of the GNS/NBR composites (see Section 2.1). The results are shown in Figure 14. Based on the definition of the RDF, the types of intermolecular interactions can be obtained by analyzing the distance, r, to the corresponding peaks. It is noted that the peak values below 3.1 Å indicate chemical and hydrogen bonds. The

**FIGURE 10** Snapshots of the free volume: A, PGNS/NBR; B, OH-GNS/NBR; C, $COOCH_3$-GNS/NBR; D, COOH-GNS/NBR composites [Color figure can be viewed at wileyonlinelibrary.com]

![](./images/812561093690916866_11.jpg)

![](./images/812561093690916866_12.jpg)

![](./images/812561093690916866_13.jpg)

![](./images/812561093690916866_14.jpg)

![](./images/812561093690916866_15.jpg)

**FIGURE 11** Variations of temperature of GNS/NBR composites during the friction process: A, PGNS/NBR; B, $COOCH_3$-GNS/NBR; C, OH-GNS/NBR; D, COOH-GNS/NBR composites [Color figure can be viewed at wileyonlinelibrary.com]

peak values at $3.1 \sim 5.0$ Å and beyond $5.0$ Å represent strong and weak vdW interactions, respectively.$^{[63-65]}$

In Figure 14A, three RDF peaks of N~OH with the peak values 3.24, 1.9, and 0.99 are observed at $\text{r} =$1.85, 2.81, and $6.73$ Å, respectively. This indicates that most of the N atoms interact with the $-$OH functional group through hydrogen bonding, and a small portion of the N atoms interact through weak vdW interactions. Likewise, g(r) of N~COOH shows three peaks at $r =$1.8, 2.8, and $3.4$ Å. The peak values at $r = 1.8$ Å and $r = 2.8$ Å are highest among the three peak values, which indicates that the N atoms interact with the $-$COOH functional group mainly through hydrogen bonding. The third peak at $r = 3.4$ Å indicates that a portion of the N atoms interact with the $-$COOH functional group by strong vdW interactions. In addition, g(r) of N~$COOCH_3$ only reaches an obvious peak value at $\text{r} = 3.5$ Å, thus indicating that the strong vdW interactions can be mainly formed between the N atoms and the $-COOCH_3$ functional group. The $-COOCH_3$ functional group has a weak polarity; hence, hydrogen bonds cannot be formed between the polar N atoms and $-COOCH_3$ functional group. However, due to the presence of the strong polar O—H bonds in the $-$OH and $-$COOH functional groups, hydrogen bonding can be formed between the strong polar O—H bond and the polar N atoms with high electro-negativity.$^{[66]}$ Similarly, as illustrated in Figure 14B, the g(r) values for H~OH and H~COOH demonstrate that some of the H atoms can still interact with the $-$OH and

![](./images/812561093690916866_16.jpg)

FIGURE 12 Variations of relative concentrations of GNS/NBR composites along the Z direction: A, PGNS/NBR; B, $COOCH_3$-GNS/ NBR; C, OH-GNS/NBR; D, COOH-GNS/NBR composites [Color figure can be viewed at wileyonlinelibrary.com]

$—COOH$ functional groups through hydrogen bonding. In contrast, the g(r) values for $H\cdots OOCH_3$ indicate that they interact with each other only by weak vdW interactions.

Finally, the types of intermolecular interactions between the functionalized GNSs and NBR matrices are summarized in Table 4. It is noted that the enhancement of the mechanical and tribological properties can be attributed to the improved interfacial interactions, that is, hydrogen bonding and vdW interactions, between the functionalized GNSs and NBR matrices, which is in good agreement with previous studies. $^{[19,67,68]}$ In addition, compared to the $COOCH_3$-functionalized GNS, the OH- and COOH-functionalized GNSs have a significant effect on improving the interfacial interaction through hydrogen bonding. Meanwhile, the COOH-functionalized GNS is capable of providing both hydrogen bonding and strong vdW interactions, while the OH-functionalized GNS interacts with the NBR matrix through hydrogen bonding and weak vdW interactions. These results agree well with the results on the binding energies discussed earlier. Thus, the COOH-functionalized GNS exhibits the best enhancement effect on the mechanical and tribological properties of the NBR composites.

Furthermore, to verify the above analysis of the interfacial interactions, the MSDs of the polymer chains, which play a vital role in determining the movement of the polymer chains, $^{[69]}$ were calculated from the equilibrated trajectories during the NPT simulations (Figure 15). The average MSD values of the functionalized GNS/NBR are 1.95, 1.83 and $1.8\ \mathring{A}^2$, which shows a decrease of 6.25%, 12.02%, 13.46%, respectively, as compared to that of the PGNS/NBR composite $(2.08\ \mathring{A}^2)$. It can be inferred that the motion of the NBR chains is greatly limited due to the improved interfacial interactions between the surface-functionalized GNS and the NBR matrix. These findings validate the above analysis on the binding energies, FVs, and total potential energies of the composites.

## 4 | CONCLUSIONS

In this research, the effect on the mechanical and tribological properties of various functionalized GNS-reinforced NBR composites was studied using MD simulations. The $—OH$, $—COOH$, and $—COOCH_3$ functional groups were adopted. The findings highlighted below are

conducive to understanding the enhancement mecha- nisms of functionalized GNSs.

Due to a rougher surface, higher in-plane stiffness, less curling and agglomeration of the functionalized GNSs, the stability, dispersion, and interfacial properties between the functionalized GNS and the NBR matrix are evidently improved for enhancing the resistance under tensile and shear loadings as compared to those of the PGNS/NBR composite.

![](./images/812561093690916866_17.jpg)

FIGURE 13 Variations of total potential energy of GNS/NBR composites during the friction process [Color figure can be viewed at wileyonlinelibrary.com]

Furthermore, the anisotropy of the NBR composites is more evident by the incorporation of a functionalized GNS. A superior resistance property of the NBR composites against external forces can be acquired by the combination of better stability within the NBR matrix and the adsorption function of the functionalized GNS with a rougher surface. This leads to a remarkable increase in the Young's modulus in the X and Y directions (as well as shear and bulk mod- uli). In contrast, a small increase in the Young's modulus in the Z direction is observed. This is because only the adsorp- tion function is acquired in the transverse direction.

In summary, among the functionalized GNSs, the COOH-functionalized GNS behaves the best enhance- ment of the mechanical and tribological properties of the NBR composites. This is attributed to the formation of strong interfacial interactions, such as hydrogen bonding

TABLE 4 The intermolecular interactions of functionalized GNS/NBR composites

<table>
<thead>
<tr>
<th>Composites</th>
<th colspan="2">Intermolecular interactions</th>
</tr>
</thead>
<tbody>
<tr>
<td>COOCH₃-GNS/NBR</td>
<td>No hydrogen bonding</td>
<td>Strong vdW interactions</td>
</tr>
<tr>
<td>OH-GNS/NBR</td>
<td>Hydrogen bonding</td>
<td>Weak vdW interactions</td>
</tr>
<tr>
<td>COOH-GNS/ NBR</td>
<td>Hydrogen bonding</td>
<td>Strong vdW interactions</td>
</tr>
</tbody>
</table>

![](./images/812561093690916866_18.jpg)

FIGURE 14 RDF g(r) values between nitrogen, hydrogen atoms of NBR chains and functional groups attached to the surface of GNS: A, N atoms~functional groups; B, H atoms~functional groups. In these composites models, the nitrogen and hydrogen atoms of NBR chains are represented by N(NBR) and H(NBR) separately. The -OH, -COOH and -COOCH₃ functional groups on the GNS surface are labeled as OH(GNS), COOH(GNS) as well as COOCH₃(GNS) respectively [Color figure can be viewed at wileyonlinelibrary.com]

![](./images/812561093690916866_19.jpg)

FIGURE 15 Variations of the MSD of NBR chains during NPT simulations [Color figure can be viewed at wileyonlinelibrary.com]

and strong vdW interactions, between the COOH-functionalized GNS and the NBR matrix. In contrast, hydrogen bonding and weak vdW interactions are formed between the OH-functionalized GNS and the NBR matrix, while the $COOCH_3$-functionalized GNS interacts with the NBR matrix only through strong vdW interactions.

## ACKNOWLEDGMENTS
This research is supported by the National Natural Sci- ence Foundation of China (Grant No. 51903148). This research is also undertaken by the Projects (NTF19008, NTF19011) supported by the Start-Up Fund of Scientific Research of Shantou University, China and the Projects (Grant No. 2030JH6/10500016) supported by the Special Program for Local Science and Technology Development of the Ministry of Science and Technology, China.

## ORCID
Yunlong Li https://orcid.org/0000-0001-8041-653X

## REFERENCES
[1] S. C. Tjong, Mater. Sci. Eng. R 2006, 53, 73.
[2] T. Keller, Prog. Struct. Eng. Mater. 2001, 3, 132.
[3] P. De Baets, S. Glavatskih, W. Ost, J. Sukumaran, Presented at 1st International Conf on Polymer Tribology, University of lju- bljana; 2014.
[4] E. He, S. Wang, Y. Li, Q. Wang, Comput. Mater. Sci. 2017, 134, 93.
[5] X. Zhaohong, L. Zhenhua, L. Jian, F. Y. Fei, J. Thermoplast. Compos. 2014, 27, 287.
[6] J. Ma, X. Qi, Y. Zhao, Y. Dong, L. Song, Q. Zhang, Y. Yang, Mater. Des. 2016, 108, 538.
[7] S. Kanagaraj, F. R. Varanda, T. V. Zhil'tsova, M. S. Oliveira, J. A. Simões, Compos. Sci. Technol. 2007, 67, 3071.
[8] R. A. Gandhi, K. Palanikumar, B. Ragunath, J. P. Davim, Mater. Des. 2013, 48, 52.
[9] J. N. Coleman, U. Khan, W. J. Blau, Y. K. Gun'ko, Carbon 2006, 44, 1624.
[10] T. Singh, A. Patnaik, Polym. Compos. 2017, 38, 1183.
[11] H. Wang, R. Wang, L. Sun, Z. Liu, Y. Zhu, Y. Zhu, RSC Adv. 2016, 6, 45636.
[12] S. Stankovich, D. A. Dikin, G. H. Dommett, K. M. Kohlhaas, E. J. Zimney, E. A. Stach, R. D. Piner, S. T. Nguyen, R. S. Ruoff, Nature 2006, 442, 282.
[13] J.-W. Jiang, J.-S. Wang, B. Li, Phys. Rev. B 2009, 80, 113405.
[14] C. Lee, X. Wei, J. W. Kysar, J. Hone, Science 2008, 321, 385.
[15] Y. Li, S. Wang, Q. Wang, M. Xing, Compos. B 2018, 133, 35.
[16] D. Li, M. B. Müller, S. Gilje, R. B. Kaner, G. G. Wallace, Nat. Nanotechnol. 2008, 3, 101.
[17] T. Ramanathan, A. Abdala, S. Stankovich, D. Dikin, M. Herrera-Alonso, R. D. Piner, D. Adamson, H. Schniepp, X. Chen, R. Ruoff, Nat. Nanotechnol. 2008, 3, 327.
[18] M. M. Gudarzi, F. Sharif, Express Polym. Lett. 2012, 6, 1017.
[19] Y. Li, Q. Wang, T. Wang, G. Pan, J. Mater. Sci. 2012, 47, 730.
[20] S. Frankland, V. Harik, G. Odegard, D. Brenner, T. Gates, Compos. Sci. Technol. 2003, 63, 1655.
[21] Y. Chandra, F. Scarpa, S. Adhikari, J. Zhang, E. S. Flores, H.-X. Peng, Compos. B 2016, 102, 1.
[22] H. Shin, S. Chang, S. Yang, B. D. Youn, M. Cho, Compos. B 2016, 87, 120.
[23] F. Liu, N. Hu, H. Ning, Y. Liu, Y. Li, L. Wu, Comput. Mater. Sci. 2015, 108, 160.
[24] F. Lin, Y. Xiang, H.-S. Shen, Compos. B 2017, 111, 261.
[25] A. N. Rissanou, V. Harmandaris, Soft Matter 2014, 10, 2876.
[26] B. Arash, Q. Wang, V. Varadan, Sci. Rep. 2014, 4, 6479.
[27] Q. Wei, Y. Wang, Y. Rao, A. Jiang, K. Zhang, T. Lu, X. Chen, Polymers 2019, 11, 76.
[28] Y. Li, S. Wang, Q. Wang, M. Xing, Compos. B 2016, 97, 62.
[29] Y. Li, S. Wang, Q. Wang, Compos. B 2017, 120, 83.
[30] A. Vozniakovskii, A. Vozniakovskii, S. Kidalov, J. Otvalko, A. Y. Neverovskaia, J. Compos. Mater. 2020, 54, 0021998320914366.
[31] Q. Zheng, Y. Geng, S. Wang, Z. Li, J.-K. Kim, Carbon 2010, 48, 4315.
[32] B. T. Polyak, Comput. Math. Math. Phys. 1969, 9, 94.
[33] H. Sun, J. Phys. Chem. B 1998, 102, 7338.
[34] D. Rigby, H. Sun, B. Eichinger, Polym. Int. 1997, 44, 311.
[35] H. C. Andersen, J. Chem. Phys. 1980, 72, 2384.
[36] H. J. Berendsen, J.v. Postma, W. F. van Gunsteren, A. DiNola, J. R. Haak, J. Chem. Phys. 1984, 81, 3684.
[37] P. P. Ewald, Ann. Phys. 1921, 369, 253.
[38] A. K. Subramaniyan, C. Sun, Int. J. Solids Struct. 2008, 45, 4340.
[39] R. Hill, Proc. Phys. Soc. 1952, 65, 350.
[40] R. Komanduri, N. Chandrasekaran, L. Raff, Phys. Rev. B 2000, 61, 14007.
[41] S. J. Eder, A. S. Vernes, G. Betz, Langmuir 2013, 29, 13760.
[42] I. N. Frantsevich, F. F. Voronov, S. A. B. Frantsevich, Elastic Constants and Elastic Moduli of Metals and Insulators, Naukova Dumka, Kiev, Ukraine 1983.
[43] M. Pang, Y. Zhan, H. Wang, Curr. Appl. Phys. 2012, 12, 957.
[44] S. Pugh, London Edinburgh Dublin Philos. Mag. J. Sci. 1954, 45, 823.

[45] T.V. Varghese, H.A. Kumar, S. Anitha, S. Ratheesh, R. Rajeev, V.L. Rao, . *Carbon* **2013**, *61*, 476-486.

[46] Y. Li, S. Wang, Q. Wang, *Carbon* **2017**, *111*, 538.

[47] A. Allahbakhsh, F. Sharif, S. Mazinani, *NANO* **2013**, *8*, 1350045.

[48] J. H. Jeon, R. K. Cheedarala, C. D. Kee, I. K. Oh, *Adv. Funct. Mater.* **2013**, *23*, 6007.

[49] W.-F. Ji, K.-C. Chang, M.-C. Lai, C.-W. Li, S.-C. Hsu, T.-L. Chuang, J.-M. Yeh, W.-R. Liu, *Compos. A* **2014**, *65*, 108.

[50] S. Sharma, R. Chandra, P. Kumar, N. Kumar, *J. Compos. Mater.* **2016**, 0021998316628973, 1.

[51] A. D. Moghadam, E. Omrani, P. L. Menezes, P. K. Rohatgi, *Compos. B* **2015**, *77*, 402.

[52] G. Gonçalves, P. A. Marques, A. Barros-Timmons, I. Bdkin, M. K. Singh, N. Emami, J. Grácio, *J. Mater. Chem.* **2010**, *20*, 9927.

[53] B. Shen, W. Zhai, M. Tao, D. Lu, W. Zheng, *Compos. Sci. Technol.* **2013**, *77*, 87.

[54] M. Fang, K. Wang, H. Lu, Y. Yang, S. Nutt, *J. Mater. Chem.* **2009**, *19*, 7098.

[55] F. Peng, Z. Jiang, E. M. Hoek, *J. Membr. Sci.* **2011**, *368*, 26.

[56] A. Talapatra, D. Datta, *Proc. Inst. Mech. Eng. J* **2020**, 1350650120912612. https://journals.sagepub.com/doi/abs/10.1177/1350650120912612.

[57] B. Liao, S.-y. Wu, L. Yang, *AIP Adv.* **2017**, *7*, 105101.

[58] B. N. Persson, O. Albohr, U. Tartaglino, A. Volokitin, E. Tosatti, *J. Phys.* **2004**, *17*, R1.

[59] B. Bhushan, P. L. Ko, *Appl. Mech. Rev.* **2003**, *56*, B6.

[60] M. Mofidi, B. Prakash, *Proc. Inst. Mech. Eng. J.* **2008**, *222*, 667.

[61] G. Yiapanis, D. J. Henry, E. Evans, I. Yarovsky, *J. Phys. Chem. C* **2010**, *114*, 478.

[62] A. Homola, H. Nguyen, G. Hadziioannou, *J. Chem. Phys.* **1991**, *94*, 2346.

[63] Y. Xiang, Y. Liu, B. Mi, Y. Leng, *Langmuir* **2014**, *30*, 9098.

[64] Q. Wei, Y. Wang, Y. Che, M. Yang, X. Li, Y. Zhang, *J. Mech. Behav. Biomed.* **2017**, *65*, 565.

[65] J. Yang, X. Gong, G. Wang, *Comput. Mater. Sci.* **2015**, *102*, 1.

[66] F. Hibbert, J. Emsley, *Adv. Phys. Org. Chem.* **1990**, *26*, 255.

[67] H. Kang, K. Zuo, Z. Wang, L. Zhang, L. Liu, B. Guo, *Compos. Sci. Technol.* **2014**, *92*, 1.

[68] Y.-G. Luan, X.-A. Zhang, S.-L. Jiang, J.-H. Chen, Y.-F. Lyu, *Chin. J. Polym. Sci.* **2018**, *36*, 584.

[69] X. Zhang, K. Takegoshi, K. Hikichi, *Macromolecules* **1991**, *24*, 5756.

How to cite this article: Cui J, Zhao J, Wang S, Li Y. A comparative study on enhancement of mechanical and tribological properties of nitrile rubber composites reinforced by different functionalized graphene sheets: Molecular dynamics simulations. *Polymer Composites*. 2020; 1-15. https://doi.org/10.1002/pc.25819