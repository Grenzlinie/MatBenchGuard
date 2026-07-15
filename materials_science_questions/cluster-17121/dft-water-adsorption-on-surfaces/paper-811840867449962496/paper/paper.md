RESEARCH PAPER

# Molecular dynamics simulations of the formation for NaCl cluster at the interface between the supersaturated solution and the substrate

Shinya Yamanaka · Atsuko Shimosaka ·
Yoshiyuki Shirakawa · Jusuke Hidaka

Received: 25 October 2008 / Accepted: 7 July 2009 / Published online: 24 July 2009
© Springer Science+Business Media B.V. 2009

## Abstract
Molecular dynamics simulations of super-saturated aqueous NaCl solution including the Pt(100) or NaCl(100) crystal surfaces have been performed at an average temperature of 298 K. The behavior of the NaCl cluster produced in the solution have been studied through the consideration of the water dielectric property near the crystalline surfaces for understanding the role of crystal growth on the surface. The surfaces in the solutions greatly influence heterogeneous nucleation in crystallization process. Density profile of the supersaturated solution and polarization of water molecules was calculated in order to describe the effect of the surfaces on the solution structure at the solid–liquid interfaces. The formation levels of NaCl clusters heavily depended on the water orientation at the interfaces. NaCl clusters were easily formed near the Pt(100) surface compared with the NaCl(100) surface owing to a different construction of water molecules between the platinum and NaCl surface.

## Keywords
Molecular dynamics simulation ·
Sodium chloride · Cluster formation ·
Heterogeneous nucleation · Dielectric property

---

S. Yamanaka (⊗) · A. Shimosaka · Y. Shirakawa (⊗) ·
J. Hidaka

Department of Chemical Engineering and Materials
Science, Doshisha University, 1-3, Tatara Miyakodani,
Kyotanabe, Kyoto 610-0321, Japan
e-mail: eth1503@mail4.doshisha.ac.jp

Y. Shirakawa
e-mail: yshiraka@mail.doshisha.ac.jp

---

## Introduction
Composite technologies have been recognized as providers of innovative product solutions because composite structures or interfaces add new functions to existing materials. Powder processes are frequently used for production of composite materials. Then, composite particles are utilized as a precursor in making the composite structures. The interfacial structure of the composite particles determined the physical and chemical properties of the produced bulk composite materials. Therefore, control of the interfacial structure is closely related to a design of the bulk composite materials (Butt et al. 2003).

Organic–inorganic hybrid particles recently attract attention in photoelectronic and pharmaceutical chemicals. In the hybrid processes, heat operation should be avoided for deterioration of organic materials. Then, liquid phase production like sol–gel and crystallization methods is well used for fabrication of their composite structure. The composites production in liquid phase is one of build up processes, and can control their interfacial or composite structure, precisely. The interfacial structure is obtained in surface crystallization which occurs at seed particle surfaces

![](./images/811840867449962496_1.jpg)

in a solution. The seed particles are covered with precipitated particles in a case. Then, nucleation and crystal growth near the seed particle surface deter- mine the interfacial structure and coating condition of the obtained composite particles (Young et al. 1992; Nývly and Ulrich 1995). The nucleation near the seed particle surface is heterogeneous nucleation. It is a complex phenomenon containing the three phase interactions (the solid substrate, the solvent and the solute crystal) (Mullin 2001) and the phase transition of solute molecules at the interface associated with a dehydration process of solute ions (Kadota et al. 2006). Therefore, what is important in heterogeneous nucleation phenomena is to examine the structure and the dynamics of solute and solvent molecules near crystalline surfaces in solution for controlling the surface crystallization.

Molecular dynamics (MD) simulation is a useful tool for an elucidation of structures and dynamics of solutions at molecular level. In fact, over the past few decades, a considerable number of studies have been conducted on the MD simulations of solid-liquid interfaces by using various models. Heinzinger (1996) and Spohr and Heinzinger (1986a, b) reported MD simulations of pure water or an electrolyte solution near a Pt(100) surface. They described the structural and dynamical properties of water and solute ions in adsorbed water layer on the Pt surface. Other researchers also studied physical properties of water or aqueous solution in the vicinity of different metals (Zhu and Philpott 1994), Pt(111) (Raghavan et al. 1991), Ag(111) (Yeh and Berkowitz 1999), TiO₂ (Koeppen and Langel 2006), etc. Moreover, Uchida et al. (2003) investigated local composition of solu- tion near solid-liquid interface and found to be completely different from that of bulk composition. Shinto et al. (1998) studied the characteristics of water molecules near the (001) and (011) faces of NaCl crystals. They concluded that a distinctive change in the interaction between a water molecule and the surface was observed despite a slight difference in the features of the crystal faces. These researches have focused their targets on the dynamics and structure of water or dilute solution near the surface and offered important contributions to an understanding of surface crystallization.

Cluster is widely thought to be an origin of nucleation or birth of a crystal. The presence of the clusters has been identified throughout the exper- imental evidences (Ginde and Myerson 1992; Volmer 1929; Mullin and Leci 1969; Allen et al. 1972). The cluster formations are attributable to fluctuations of solute concentration. Therefore, the slight change of an ionic concentration at the solid-liquid interface is greatly related to the clusters formation in surface crystallization processes. MD simulations have emerged as the most direct means to investigate the cluster behavior and get some information about the onset of surface crystallization. Recently, the MD simulations have also shown evidence of cluster formation. The formation of NaCl cluster have detected in unsaturated (Degreve and da Silva 1999; Chen and Pappu 2007; Hassan 2008) and supersatu- rated NaCl solution (Zahn 2004; Kadota et al. 2006). In order to design interfaces of composite particles, the studies at a molecular level of the solution structure and the behavior of cluster at solid-liquid interfaces are necessary.

In this study, the cluster formation processes of aqueous NaCl solution near the Pt(100) or NaCl(100) crystal surfaces have been performed using MD simulation. We have presented the cluster formation mechanism at solid-liquid interface which was estimated from the radial distribution function and the consideration for the dielectric properties of water at the interface.

## Simulations

The heterogeneous systems considered in this article were constructed of the NaCl solutions with the crystalline sodium chloride or the platinum surface. The rectangular basic box for the MD simulation of supersaturated NaCl solution put between two sur- faces of Pt(100) or NaCl(100) is shown in Fig. 1. Pt metal constructs 256 metal atoms, NaCl crystals layer with $6 \times 6 \times 6$ ions (Na⁺, 108; Cl⁻, 108) on each side. The supersaturated NaCl solution consists of 277 water molecules, $38\ \text{Na}^+$ and $38\ \text{Cl}^-$. At room temperature, the concentration of saturated solution is $35.96\ \text{g/100 mL}\ \text{H}_2\text{O}$ (Lide 1996). Under these con- ditions, the ions or atoms in the first layer of crystal surfaces were located at the distance listed in Table 1.

The saturated solution contains one NaCl and nine water molecules. While, the supersaturated solution

![](./images/811840867449962496_2.jpg)

![](./images/811840867449962496_3.jpg)

Fig. 1 Basic box for MD simulation in which shaded regions represent the crystal phase and the remaining is the supersaturated NaCl solution. The standard coordinates are at the center of the box

<table>
<caption>Table 1 Side lengths for MD simulations of solution between the Pt(100) or the NaCl(100) surfaces</caption>
<thead>
<tr>
<th>
</th>
<th>Solution/Pt(100)</th>
<th>Solution/NaCl(100)</th>
</tr>
</thead>
<tbody>
<tr>
<th>Side length</th>
<td>
</td>
<td>
</td>
</tr>
<tr>
<th>$Lx$/nm</th>
<td>1.570</td>
<td>1.692</td>
</tr>
<tr>
<th>$Ly$/nm</th>
<td>1.570</td>
<td>1.692</td>
</tr>
<tr>
<th>$Lz$/nm</th>
<td>7.391</td>
<td>7.099</td>
</tr>
</tbody>
</table>

here contains 38 NaCl and 277 water molecules. Using the mole fraction definition, the supersaturation $S$ of all solutions in the present simulations is calculated to be 0.21.

$$
S=\frac{c-c_{0}}{c_{0}} \tag{1}
$$

where $c_{0}$ is the concentration of saturated solution, and $c$ is a solution concentration ($c=0.12$ and $c_{0}=0.1$ in the present case).

Many interaction models between the water, the ions, and the atoms have been proposed. A simple type model, in which all of the intermolecular interactions are expressed as a sum of Lennard-Jones and/or electrostatic potentials, has been chosen in this article. In MD simulations without complicated molecules and anisotropy of their structures, the simple model gives us clear information of interactions between molecules. The simulation was calculated in the intermolecular potential model for the water, ions, and metal atoms.

$$
u\left(r_{i}, r_{j}\right)=4 \varepsilon_{i j}\left[\left(\frac{\sigma_{i j}}{r_{i j}}\right)^{12}-\left(\frac{\sigma_{i j}}{r_{i j}}\right)^{6}\right]+\frac{q_{i} q_{j}}{r_{i j}} \tag{2}
$$

where $r_{i j}$ is the distance between $i$ and $j$ sites, $\varepsilon_{i j}$ and $\sigma_{i j}$ are the energy parameter and size parameter, respectively, and $q_{i}$ is the charge with ion $i$. The first and second terms in Eq. 2 represent the Lennard-Jones potential. The water–water interaction potential was determined by SPC/E model (Berendensen et al. 1987), which has been represented quite nicely bulk properties of water and aqueous electrolyte solutions (Heinzinger 1985). The potential parameters used are given in Table 2. The Lennard-Jones parameters for the platinum were taken from the published data (Zhu and Philpott 1994). The potential parameters evaluated from a variety of physical properties in crystalline state in a wide range of temperature. The third term represents the Coulomb electrostatic interaction. For the solution of the parameters, $q$, $\sigma$, and $\varepsilon$ given by Koneshan et al. (1998) were used as shown in Table 2. The ions chosen are $\mathrm{Na}^{+}$($q=+1.0$ e, $\sigma_{\mathrm{Na}^{+}, \mathrm{Na}^{+}}=$0.2584 nm and $\varepsilon_{\mathrm{Na}^{+}, \mathrm{Na}^{+}}=0.4184$ kJ/mol) and $\mathrm{Cl}^{-}$($q=-1.0$ e, $\sigma_{\mathrm{Cl}^{+}, \mathrm{Cl}^{+}}=0.4400$ nm and $\varepsilon_{\mathrm{Cl}^{+}, \mathrm{Cl}^{+}}=$0.4184 kJ/mol). The potential parameters for unlike site pairs are expressed by the following Lorents-Berthelot mixing rules.

$$
\sigma_{i j}=\frac{\left(\sigma_{i}+\sigma_{j}\right)}{2} \tag{3}
$$

$$
\varepsilon_{i j}=\sqrt{\varepsilon_{i} \varepsilon_{j}} \tag{4}
$$

The long range electrostatic was treated using the Ewald summation method (Ewald 1921) with infinity of the dielectric constant of surrounding medium and convergence parameter $\alpha=6.4 / L_{X}$. A spherical cut-off with the radius of $L_{X} / 2$ was used for the short range interactions. The equation of transitional motions and rotational motions was integrated by using the velocity Verlet algorithm and the leap-frog method, respectively, with time step of 0.5 fs. The constant temperature and the constant volume (NVT) MD were applied for equilibrium states in our simulation. The temperature was kept at 298 K by velocity scaling. The calculation for property collection was performed for 0.5–1.0 ns.

<table>
<caption>Table 2 Potential Parameters</caption>
<thead>
<tr>
<th>Site</th>
<th>$\sigma$ (nm)</th>
<th>$\varepsilon$ (kJ/mol)</th>
<th>$q$ (e)</th>
</tr>
</thead>
<tbody>
<tr>
<td>O</td>
<td>0.3169</td>
<td>0.6502</td>
<td>$-0.8476$</td>
</tr>
<tr>
<td>H</td>
<td>0</td>
<td>0</td>
<td>$+0.4238$</td>
</tr>
<tr>
<td>$\mathrm{Na}^{+}$</td>
<td>0.2584</td>
<td>0.4184</td>
<td>$+1.0$</td>
</tr>
<tr>
<td>$\mathrm{Cl}^{-}$</td>
<td>0.4400</td>
<td>0.4184</td>
<td>$-1.0$</td>
</tr>
<tr>
<td>Pt</td>
<td>0.2540</td>
<td>65.77</td>
<td>0</td>
</tr>
</tbody>
</table>

![](./images/811840867449962496_4.jpg)

## Results and discussion

### Solution structure at the interface

Figure 2 shows the oxygen-oxygen radial distribution functions (RDF) of the supersaturated NaCl solution on the surfaces of Pt(100) or the NaCl(100) crystal. The water structure near each surface shows pronounced difference. The O-O structure estimated from the RDF clearly resembles the Pt-Pt structure whereas the O-O structure near the NaCl(100) crystal maintains configuration of the NaCl bulk solution. For the solution on Pt(100) crystal, the Pt-Pt distance of 0.277 nm is very close to the O-O distance in the NaCl bulk solution. Moreover, the second peak at 0.39 nm is identical with the lattice constant of Pt-Pt. Therefore, the structure of water near the Pt(100) crystal is affected by the Pt(100) surface structure.

The solution structure near the solution-crystal interface can be conveniently studied by means of density profiles. In order to clarify the interfacial structure of the supersaturated NaCl solution-Pt or NaCl crystal surface, the density profiles for solution on Pt or NaCl were calculated about the water molecules and the each solute ion; they are shown in Fig. 3 in the case of the Pt(100) and the NaCl(100) surface. The density of water molecules profile clearly shows two well separated peaks next to the each surface. The density at the interface is much stronger than the bulk water density. It indicates strong adsorption of water on the each surface. This result was similar to MD simulation results of the water-crystal interface system reported by other workers using different types of water and surface models. (Spohr and Heinzinger 1986a, b; Zhu and Philpott 1994). Moreover, adsorption of hydration layer at interfaces has been already observed in some experiments (Israelachvili 1992; Li et al. 2004). Weak but clear peak of the density profile of both solute ions, $Na^{+}$ and $Cl^{-}$, is obtained near the surfaces in our simulation results. Spohr and Heinzinger studied a system of 8 LiI and 200 water molecules including uncharged flat Lennard-Jones walls and found that the weakly hydrated Li ion was influenced by the weak interactions with the Lennard-Jones walls (Spohr and Heinzinger 1986a, 1986b). In our simulation, the coordination number of water-$Na^{+}$ ion decreased near the surfaces. The number was estimated from O-$Na^{+}$ RDF, and corresponds with their results, as shown in Fig. 4.

![](./images/811840867449962496_5.jpg)

Fig. 2 Oxygen-oxygen radial distribution functions of supersaturated NaCl solution with surfaces of the Pt(100) (solid line) or the NaCl(100) (dashed line) and the supersaturated NaCl solution (dotted line)

![](./images/811840867449962496_6.jpg)

Fig. 3 Density profiles of the water molecules (dashed line), the sodium ion (solid line) and the chloride ion (dotted line) against z axis: a Pt(100), b NaCl(100)

![](./images/811840867449962496_7.jpg)

![](./images/811840867449962496_8.jpg)

Fig. 4 Coordination number of sodium ions in solution including Pt(100) or NaCl(100) against the distance from the crystalline surfaces

The concentration of solute and water molecules against the distance from solution-surface interface was given by the following equation.

$$
C_{\mathrm{A}}(r)=\frac{1}{\rho L^{2} \Delta r} \frac{1}{N_{\text {all }}} \sum_{\mathrm{k}=1}^{N_{\mathrm{A}}} n_{k}(r)
$$

where $C_{\mathrm{A}}$ is the concentration, $\rho$ is bulk density of the solution, $L$ is box length, $\Delta r$ represents the width of each calculation, $N_{\text {all }}, N_{\mathrm{A}}$, and $n_{k}$ are the number of all molecules in each calculation and each ion, respectively. The experimental study was carried out to investigate the concentration of solute ions and solvent molecules near the solution-crystal interface (Matsuoka and Garside 1991). They concluded that the concentration of solvent molecules increased at the interface while the concentration of solute ions decreased. The comparable results are obtained in our simulation as shown in Fig. 5. Additionally, the solute concentration near the Pt(100) surface is significantly higher than that of the NaCl(100) surface. Classical nucleation theory postulates the presence of clusters in supersaturated solutions (Ginde and Myerson 1992). Indirect evidences of the existence of clusters were researched throughout previous works (Volmer 1929; Mullin and Leci 1969; Allen et al. 1972). It is commonly believed that fluctuations of solute concentration cause the cluster formations in the supersaturated solution. Therefore, it is reasonable to suppose that the change in ionic concentration at the interface has much impact on the cluster formation.

![](./images/811840867449962496_9.jpg)

Fig. 5 Concentration of the water molecules (solid line), and the solute ions (dashed line) against z axis: a Pt(100), b NaCl(100). The bulk concentration of the water and the solute ions was set to 1.0

### Behavior of NaCl cluster

The clusters were determined by a simple distance criterion (Stillinger 1963), in which all ions within less than 0.324 nm distance from each other (the first minimum of the $\mathrm{Na}^{+}-\mathrm{Cl}^{-}$RDF). The clusters in solutions, are continuously formed and destroyed (Kadota et al. 2004) due to thermal fluctuation. Thus, we defined the cluster was aggregated solute ions binding for more than 37.5 ps in 50.0 ps. This definition can derive from binding with probability 75% in an assumption of bound ions in harmonically oscillating motion.

The cluster behavior, the number, and the location of clusters, were investigated in supersaturated NaCl solution near the crystal surfaces based on the definition above mentioned. Figures 6 and 7 show

![](./images/811840867449962496_10.jpg)

![](./images/811840867449962496_11.jpg)

Fig. 6 Time dependence of the number of clusters for solutions with surfaces of the Pt(100) or the NaCl(100)

![](./images/811840867449962496_12.jpg)

Fig. 7 The position formed the clusters along the z axis direction with surfaces of the Pt(100) or the NaCl(100)

time dependence of the number of the clusters and position formed clusters along z direction from the interfaces, respectively. As can be seen from Fig. 6, the clusters are continuously formed and destroyed due to thermal fluctuation. It is noted that most of the clusters formed at the interface in the Pt(100) system while the clusters almost uniformly formed in the solution with NaCl(100) (Fig. 7).

We particularly examined the orientation of water molecules to explore the cause of the difference between solution/Pt and solution/NaCl. The orientational distribution in reconstruction of water structure at the interface in Fig. 8 is instrumental in clarifying interaction between the water and the surface. There is a clear peak in the dipole orientation curves for

![](./images/811840867449962496_13.jpg)

Fig. 8 Distributions of electric dipole as a function of $\cos\theta$. $\theta$ is the angle between the dipole moment and the inward normal to the crystal surfaces

solution/Pt system. This peak results from strongly ordered water molecules on the Pt (100) surface which are approximately parallel to the surface. While, at NaCl(100) interface, there is no specific peak to confirm the dipole orientation. It suggests that water molecules near NaCl(100) are oriented weakly near the surface compared to near Pt(100). These orientational difference leads to the dielectric property variation at the interfaces and a difference of cluster formation between solution/Pt and/NaCl.

A role of surface in the cluster formation

In crystallization, crystals are commonly produced by adding a precipitant to metamorphose the electrostatic interactions between the solvent and the solute molecules (Weber et al. 2008). An accurate representation of the dielectric properties of a solvent is a key to the proper description of electrostatic interactions. In water, dielectric constant is related to the fluctuations in total dipole moment of the water molecules (Kirkwood 1939). For a system with periodic boundaries and the long-range interactions treated by the lattice summation method, the static dielectric constant $E$ of a fluid is given by (Neumann et al. 1984)

$$
E=\frac{4\pi\left\langle M^{2}\right\rangle}{3VT}+1 \tag{6}
$$

where $V$ is system volume, $T$ is temperature in units of the Boltzmann's constant and $M$ is total dipole

![](./images/811840867449962496_14.jpg)

moment of water molecules. Angular bracket denotes an ensemble average replaced by a time average over the system which is usual in MD calculation (Frenkel and Smit 1997). In our simulation, the static dielectric constant of water was $81.8 \pm 1.1$ which was seen to be in quite good agreement with the experimental value of 78.3 at 298 K when we calculated the 277 water molecules.

Figure 9 shows the static dielectric constant of water against the distance from the surfaces for Pt(100) or NaCl(100). The both of them are marked maximum value at the first layer and decay to the value of bulk water with distance from the each surface. The number of water molecules was reached that the density in the centre of the box was almost the same of bulk water. An important point is the fact that a large difference is obtained for Pt(100) in which the dielectric constant changes from the range of 50.9–156.4 while 75.3–90.1 for NaCl(100). This result can be interpreted as the dielectric properties are obviously reflected in the water molecular orientations. We should look more carefully into what impact the electrostatic properties would have discussion on the cluster formation from electric interaction between the solute ions in the solution.

![](./images/811840867449962496_15.jpg)

Fig. 9 The value of the dielectric constant $E$ against the distance from the crystalline surfaces for the Pt(100) or the NaCl(100). $E$ is calculated by using Eq. 6

A schematic description of the cluster formation model is illustrated in Fig. 10. On the Pt(100) surface, water molecules are attracted to the surface and form a structured layer (c). There is a lower dielectric region (b) on the structured water due to the screened electric interaction from the surface. It is known that the electrical energy is overly emphasized in a lower dielectric region (Parsegian 1969). This fact indicates that strong electric field enhances a dehydration of the hydrated solutes. Consequently, the decrease of the dielectric property from the solute ions is easier to destroy their hydration structure and more stable if the ions form the cluster, especially near the Pt(100) surface. That is, the water structure on surface has an enormous effect on the cluster behavior. It is concluded that this fact will be a helpful clue to the elucidation of nucleation or crystallization near the crystalline surface.

![](./images/811840867449962496_16.jpg)

## Conclusion

Molecular dynamics simulations of aqueous NaCl solution including the Pt(100) or NaCl(100) crystal surfaces have been performed in order to consider the solution structure and the behavior of NaCl cluster formation. First, the solution structure at the interface between the crystal surface and the solution was studied by means of density profile. There is a clear difference in comparison with the Pt(100) and the NaCl(100) crystal, and it relates to a profound influence on the formation behavior of NaCl clusters. Much of the cluster forms at the Pt(100) interface while the cluster uniformly forms in the solution with NaCl(100). The cluster behavior is dominated by the difference of the dielectric properties of water at the solution-crystal interface, which is attributable to the water orientations at the interface. For Pt(100) interface, there is a specific peak to confirm the dipole orientation which suggests that water molecules are oriented strongly near the surface compared to NaCl(100).

Acknowledgments This work was supported by the Hosokawa Powder Technology Foundation, and the Core-to-Core Program promoted by Japan Society for the Promotion of Science (Project No.18004), and Research Center of Fine Particle Science and Technology in Doshisha University.

## References

Allen AT, McDonald MP, Nicol WM, Wood RM (1972) A thermal concentration gradients in supersaturated solutions of sucrose. Nature 235(53-61):36-37

Berendensen HJC, Grigera JR, Straatsma TP (1987) The missing term in effective pair potentials. J Phys Chem 91(24):6269-6271

Butt HJ, Graf K, Kappl M (2003) Physics and chemistry of interfaces. Wiley-VCH, Weinheim

Chen AA, Pappu RV (2007) Quantitative characterization of ion pairing and cluster formation in strong 1:1 electrolytes. J Phys Chem B 111(23):6469-6478

Degreve L, da Silva FLB (1999) Large ionic clusters in concentrated aqueous NaCl solution. J Chem Phys 111(11):5150-5156

Ewald PP (1921) Die Berechnung optischer und electrostatischer Gitterpotentiale. Ann Phys 64:253-287

Frenkel D, Smit B (1997) Understanding molecular simulation from algorithms to applications. Academic Press, Boston

Ginde RM, Myerson AS (1992) Cluster size estimation in binary supersaturated solutions. J Cryst Growth 116(1/2):41-47

Hassan SA (2008) Computer simulation of ion cluster speciation in concentrated aqueous solutions at ambient conditions. J Phys Chem B 112(34):10573-10584

Heinzinger K (1985) Computer simulations of aqueous electrolyte solutions. Physica BC 131(1/3):196-216

Heinzinger K (1996) Molecular dynamics studies of electrolyte solution/metal interfaces. Mol Simul 16(1/3):19-30

Israelachvili JN (1992) Intermolecular and surfaces forces, 2nd edn. Academic Press, London

Kadota K, Takase K, Shimosaka A, Shirakawa Y, Hidaka J (2004) The influence of habit modifiers on particle shape in a crystallization process. J Soc Powder Technol, Jpn 41(6):431-439

Kadota K, Shimosaka A, Shirakawa Y, Hidaka J (2006) Dehydration process in NaCl solutions under various external electric fields. J Nanopart Res 9(3):377-387

Kirkwood JG (1939) The dielectric polarization of polar liquids. J Chem Phys 7(10):911-919

Koeppen S, Langel M (2006) Simulation of the interface of (100) rutile with aqueous ionic solution. Surf Sci 600(10):2040-2050

Koneshan S, Rasaiah JC, Lynden-Bell RM, Lee SH (1998) Solvent structure, dynamics, and ion mobility in aqueous solutions at 25 °C. J Phys Chem B 102(21):4193-4204

Li Y, Kanda Y, Higashitani K (2004) Interaction forces between hydrophilic surfaces in electrolyte dimethyl sulfoxide solutions measured by atomic force microscopy. Adv Powder Technol 15(2):165-180

Lide DR (1996) CRC handbook of chemistry and physics, 77th edn. CRC Boca Raton, Florida

Matsuoka M, Garside J (1991) Non-isothermal effectiveness factors and the role of heat transfer in crystal growth from solutions and melts. Chem Eng Sci 46(1):183-192

Mullin JW (2001) Crystallization, 4th edn. Butterworths-Heinemann, Oxford

Mullin JW, Leci CL (1969) Evidence of molecular cluster formation in supersaturated solutions of citric acid. Philos Mag 19(161):1075-1077

Neumann M, Steinhauser O, Pawley GS (1984) Consistent calculation of the static and frequency-dependent dielectric constant in computer simulations. Mol Phys 52(1):97-113

Nývly J, Ulrich J (1995) Admixtures in crystallization. VCH, Weinheim

Parsegian A (1969) Energy of an ion crossing a low dielectric membrane: solutions to four relevant electrostatic problems. Nature 221:844-846

Raghavan K, Foster K, Motakabbir K, Berkowitz M (1991) Structure and dynamics of water at the Pt(111) interface: molecular dynamics study. J Chem Phys 94(3):2110-2117

Shinto H, Sakakibara T, Higashitani K (1998) Molecular dynamics simulations of water at NaCl(001) and NaCl(011) surfaces. J Phys Chem B 102(11):1974-1981

Spohr E, Heinzinger K (1986a) Molecular dynamics simulation of a water/metal interface. Chem Phys Lett 123(3):218-221

Spohr E, Heinzinger K (1986b) A molecular dynamics study of an aqueous LiL solution between Lennard-Jones walls. J Chem Phys 84(4):2304-2309

![](./images/811840867449962496_17.jpg)

Stillinger FH (1963) Rigorous basis of the Frenkel-band theory of association equilibrium. J Chem Phys 38(7):1486–1494

Uchida H, Takiyama H, Matsuoka M (2003) Molecular dynamics simulation of the solution structure near the solid–liquid interface between the NaCl(100) and NaCl–KCl–H₂O solutions. Cryst Growth Des 3(2):209–213

Volmer M (1929) Über keimbildung und keimwirkung als spezialfiille der heterogenen katalyse. Z Electrochem 35:555–561

Weber M, Jones MJ, Ulrich J (2008) Crystallization as a purification method for jack bean urease: on the suitability of poly (ethylene glycol), Li₂SO₄, and NaCl as precipitants. Cryst Growth Des 8(2):711–716

Yeh IC, Berkowitz M (1999) Aqueous solution near charged Ag(111) surfaces: comparison between a computer simulation and experiment. Chem Phys Lett 301(1/2):81–86

Young JR, Didymus JM, Mann S, Bown PR, Prins B (1992) Crystal assembly and phylogenetic evolution in heterococcoliths. Nature 356(6369):516–518

Zahn D (2004) Atomistic mechanism of NaCl nucleation from an aqueous solution. Phys Rev Lett 92(4):040801.1–040801.4

Zhu SB, Philpott MR (1994) Interaction of water with metal surfaces. J Chem Phys 100(9):6961–6968

![](./images/811840867449962496_18.jpg)