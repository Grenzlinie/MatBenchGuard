# APPLICATION OF MOLECULAR DYNAMIC SIMULATION TO NANOCOMPOSITE PROCESSING: INVESTIGATION OF INTERACTIONS BETWEEN NANOTUBE AND POLYMER MOLECULES

Jihua (Jan) Gou, Zhiyong Liang, Chuck Zhang and Ben Wang
Department of Industrial & Manufacturing Engineering
Florida A&M University – Florida State University College of Engineering
Tallahassee, Florida

Leslie Kramer
Lockheed Martin Missiles and Fire Control - Orlando
Orlando, Florida

## ABSTRACT

Carbon nanotubes are considered a promising reinforcement material for the next generation high performance structural and multifunctional composites. However, nanotubes are difficult to properly wet by polymer materials during nanotube composite processing due to the very high chemical stability of the nanotube fullerene structure. Consequently, the resultant materials fail to demonstrate their much-anticipated performance because of the poor wetting and weak interfacial bonding of nanotube-polymer composites. New principles and technologies are required to properly handle and investigate such nano-scale processing phenomena in nanotube-based composites. In this study, molecular interactions between single-walled nanotube (SWNT) and epoxy resin were investigated using molecular dynamics (MD) simulation. The molecular models of (10,10) SWNT, simple porous network structure of SWNT and Epon 862 resin oligomer were established and used to conduct MD simulation of molecular interaction in nanocomposite processing. The results show that (10,10) SWNT can be automatically filled and wrapped by Epon 862 resin molecules through their molecular interactions at room temperature. An external pressure is required to drive resin molecules to flow through a 6x6 nanometer pore structure of SWNTs. These results also show that MD simulation is an effective method for the material selection and processing optimization from molecular level for nanotube nanocomposites development.

Keywords: Carbon nanotube, Nanocomposites,
Molecular dynamic simulation, Epoxy resin

## INTRODUCTION

The discovery of carbon nanotubes by Iijima in 1991 [1] has initiated a number of scientific investigations to explore their unique properties and potential applications. A nanotube resembles a hexagonal arrangement of carbon atoms in a sheet form that has been rolled up to form a tube. The tube can either be open ended or have caps formed from half a $C_{60}$ molecule at either end. Carbon nanotubes have many remarkable characteristics such as novel electronic properties, exceptionally high strength and axial Young's modulus of 1TPa [2]. The composite community considers nanotubes "ultimate reinforcements" for next generation high performance composites.

However, the very high chemically stability of nanotube fullerene structure makes wetting by polymer materials during nanotube composite processing difficult. Several research groups have fabricated nanotube-polymer composites by the solution casting technique. In their studies, epoxy resins and thermoplastic polymers were used as the matrix polymers. Schadler *et al.* [3] observed a 20% increase in both tensile and compressive moduli of an epoxy upon ultrasonically dispersing 5wt.% multi-walled nanotubes (MWNTs) in the EPON 828 epoxy resin. Qian *et al.* [4] studied composite films in which MWNTs were dispersed in a polystyrene matrix. Qian reported a 1wt.% nanotube addition resulted in 36-42% increase in elastic modulus and a 25% increase in break stress. The research results have shown that composite materials made by direct mixing of nanotubes and polymeric resin do not demonstrate the much-anticipated performance. The poor wetting and weak interfacial bonding are considered major reasons for

this shortcoming. New principles and technologies are needed to properly handle and investigate such a nano-scale processing phenomena in nanotube-based composites.

The processing phenomena of nanotube composites strongly depending on the interactions between nanotubes and polymer molecules [5-10] are well known. The main objective of our study was to demonstrate the molecular interactions by examining their dynamic behaviors in the processing environment of nanotube-epoxy composite. Molecular dynamics simulations were used to provide reasonable predictions of their interactions at the nano-scale. (10, 10) SWNT and Epon 862 epoxy resin were used in the study. Molecular dynamics simulations were carried out on a SGI-Octane2 workstation using Materials Studio, a commercial software package developed by Accelrys, Inc.

## MOLECULAR MODEL

### Molecular Model of Single-Wall Carbon Nanotube (10,10)
A single-wall carbon nanotube can be described as a conformational mapping of a graphene sheet into a cylinder subjected to periodic boundaries both around the cylinder and along its axis, as shown in Figure 3. The geometry of a single-wall carbon nanotube is determined by the chiral vector $C_h$, transnational vector $\mathbf{T}$, and symmetry vector $\mathbf{R}$ . Detailed descriptions of the three vectors can be found in reference [11]. If we introduce the set of primitive lattice vector $\boldsymbol{\alpha}_1$ and $\boldsymbol{\alpha}_2$, then $\mathbf{C}_h$ can be expressed as:

$$
\mathbf{C}_{h}=n \boldsymbol{\alpha}_{1}+m \boldsymbol{\alpha}_{2} \equiv(n, m)
$$

Each nanotube can be labeled by a pair of integers ($n$, $m$). Various helical structures are possible, such as numerous different achiral, "Zigzig" $\mathbf{C}_{h}=(n, 0)$ and "armchair" $\mathbf{C}_{h}=(n, n)$ configurations.

In this study, the molecular model of (10,10) SWNT was established. The main structural parameters are listed in Table 1. The modeled SWNT had a finite length of $9.7 nm$ and its diameter was $1.38 nm$. The computer graphics (CG) picture of the nanotube in the longitudinal view is shown in Figure 1. The unsaturated boundary effect was avoided by adding 20 hydrogen atoms at each end of carbon nanotube. The model had 400 carbon atoms and 40 hydrogen atoms. Each C-C bond length was $1.42 \mathring{A}$ and C-H bond length was $1.10 \mathring{A}$. The hydrogen atoms had charges of $+0.1268e$ and the carbon atoms connecting hydrogen atoms had charges of $-0.1268e$, thus overall the carbon nanotube was neutrally charged.

Table 1. Detailed structural parameters of a (10,10) SWNT

<table>
  <tr>
    <td>Symbol</td>
    <td>Name</td>
    <td>Value</td>
  </tr>
  <tr>
    <td>$a$</td>
    <td>Length of unit vector (Å)</td>
    <td>$a=\sqrt{3}b_{c-c}=2.49$</td>
  </tr>
  <tr>
    <td>$\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2$</td>
    <td>Primitive vector</td>
    <td>$\left(\frac{\sqrt{3}}{2},\frac{1}{2}\right)a,\left(\frac{\sqrt{3}}{2},-\frac{1}{2}\right)a$</td>
  </tr>
  <tr>
    <td>$\mathbf{C}_h$</td>
    <td>Chiral vector</td>
    <td>$\mathbf{C}_{h}=10\boldsymbol{\alpha}_{1}+10\boldsymbol{\alpha}_{2}\equiv(10,10)$</td>
  </tr>
  <tr>
    <td>$R$</td>
    <td>Radius (Å)</td>
    <td>$d_{t}=\frac{a\sqrt{n^{2}+m^{2}+nm}}{2\pi}=6.8$</td>
  </tr>
  <tr>
    <td>$\mathbf{T}$</td>
    <td rowspan="2">Translational vector</td>
    <td>$\mathbf{T}=t_{1}\boldsymbol{\alpha}_{1}+t_{2}\boldsymbol{\alpha}_{2}=\boldsymbol{\alpha}_{1}-\boldsymbol{\alpha}_{2}$</td>
  </tr>
  <tr>
    <td></td>
    <td>$t_{1}=\frac{2m+n}{d_{R}}=1$<br>$t_{2}=--\frac{2n+m}{d_{R}}=-1$</td>
  </tr>
  <tr>
    <td>$T$</td>
    <td>Length of $\mathbf{T}$ (Å)</td>
    <td>$T=|\mathbf{T}|=\frac{\sqrt{3}L}{d_{R}}=2.49$</td>
  </tr>
  <tr>
    <td>$N$</td>
    <td>Number of hexagons in the unit cell</td>
    <td>$N=\frac{2(n^{2}+m^{2}+nm)}{d_{R}}=20$</td>
  </tr>
  <tr>
    <td>$\mathbf{R}$</td>
    <td rowspan="2">Symmetry vector</td>
    <td>$\mathbf{R}=p\boldsymbol{\alpha}_{1}+q\boldsymbol{\alpha}_{2}$<br>$\equiv(p,q)=(1,0)$</td>
  </tr>
  <tr>
    <td></td>
    <td>$t_{1}q-t_{2}p=1$</td>
  </tr>
  <tr>
    <td>$\tau$</td>
    <td>Pitch of $\mathbf{R}$ (Å)</td>
    <td>$\tau=\frac{(mp-nq)T}{N}=\frac{MT}{N}=1.25$</td>
  </tr>
  <tr>
    <td>$\psi$</td>
    <td>Rotation angle of $\mathbf{R}$</td>
    <td>$\psi=\frac{2\pi}{N}=0.314$</td>
  </tr>
</table>

![](./images/813200696487706625_1.jpg)

Figure 1. Molecular model of a (10, 10) SWNT

### Molecular Model of EPON 862 Resin
In nanotube-polymer composites, the van der Waals forces between nanotube and matrix polymer molecules are dependent on the type and the conformation of the polymer. Several research groups have reported experimental studies of nanotube-polymer composites, which used epoxy resins [3, 12] and thermoplastic polymers [4, 13] as the matrix polymers. Epon 862, a low-viscosity, liquid epoxy resin manufactured from epichlorohydrin and Bisphenol-F, was selected for this study as the matrix material. The chemical structure of Epon 862 resin oligomer is shown in Figure 2.

Energy-minimization molecular mechanics were performed to find the thermal stable morphology of Epon 862 resin. The chain of Epon 862 resin oligomer was twisted to achieve low potential energy. Figure 3 shows its configuration with minimum potential energy. Under this energy, the molecule of Epon 862 has the dimension of $23 \times 9 \times 6 \mathring{A}$.

### Molecular Model of SWNT Pore Structure
In the produced nanotube powders and nanocomposite processing, nanotubes usually form porous networks as fiber networks in conventional carbon fiber composites. In order to investigate the molecular interaction between nanotubes and polymer molecules within nanoscale pore structure of nanotubes, a nanotube pore was constructed with four $9.7nm$ SWNTs and multiple Epon 862 oligomers, as shown in Figure 4. The pore size was $6nm \times 6nm$ and 6400 carbon atoms made up this molecular model.

$$
\mathrm{O-CH_2-CH-CH_2-O-CH_2-CH-CH_2}
$$

Figure 2. Chemical structure of Epon 862 resin oligomer

![](./images/813200696487706625_2.jpg)

Figure 3. Molecular model of Epon 862 resin with minimum potential energy

![](./images/813200696487706625_3.jpg)

Figure 4. Molecular models of SWNT pore structure and resin

## RESULTS AND DISCUSSION
To investigate the interactions of nanotube and Epon 862 resin molecules in the composite processing environment, several MD simulations were carried out. In each case, the MD simulation was performed long enough to observe several cycles of thermal vibration. The interval of each MD simulation step was typically 2 femto second ($fs$). All calculations were carried out at the initial temperature 300K, using NVT ensembles (constant number of particles, constant volume, and constant temperature) [14]. Pore and pore correlation effects and changes in the initial temperature effects were not considered in this study.

### Filling of Epon 862 Molecule into Carbon Nanotube
The Epon 862 molecule is an asymmetric molecule with a narrow width and deformable conformation, which has the same dimensions of (10,10) SWNT. Producing nanotubes with openings is possible during the nanotube fabrication [15]. The investigation of the filling of the resin molecule into the tube indicates the strong interaction between the molecules. The possibility of the resin molecular into tubes during real-world composite processing could create the desired chemical bonding between nanotubes and polymer resin.

To study the nanoscale filling phenomena, a MD simulation was set up with an Epon 862 resin molecule initially placed near the opening at one end of the nanotube along the direction of the tube axis. The interval of a MD simulation step was $2fs$, and the simulation was performed for $40ps$. The system was then allowed to evolve over time without additional constraints, such as external pressure.

Figure 5 shows the configuration of Epon 862 resin molecule and carbon nanotube observed at several time steps of the MD simulation. The entry and diffusion of the resin molecule into the nanotube occurred through specific orientation. During the initial $8ps$, the molecule was lingering around the opening, constantly changing its orientation. The resin molecule always entered the nanotube with its narrowest end going first, which obviously facilitates the entry of the molecule into the nanotube. When the molecule obtained the correct orientation, it intercalated into the nanotube and moved into the tube. However, the resin molecule remained inside of the nanotube and stayed near the opening, instead of going out the other end. The nanotube diameter widened during the filling, indicating that the nanotube itself is very flexible.

The filling of nanotube with Epon 862 resin molecule can be illustrated by tracking the energy of the "nanotube-Epon 862 resin" system as shown in Figure 6. The total potential energy of the system decreased slightly as the time evolved and a favorable potential energy was obtained when the resin molecule was inside the nanotube. Since the nanotube has a stable structure and the potential energy of the resin molecule is small, most of the energy difference resulted from the change of the interaction energy between nanotube and resin molecule. The filling of the resin molecule in the nanotube was driven by the van der Waals forces, which produced a decrease of interaction energy with 80 kcal/mol.

![](./images/813200696487706625_4.jpg)

![](./images/813200696487706625_5.jpg)

Figure 5. MD simulation of filling nanotube with an Epon 862 resin molecule

![](./images/813200696487706625_6.jpg)

Figure 6. Energy change during the filling of the nanotube: (a) potential energy and (b) interaction energy between nanotube and Epon 862 resin molecule

### Wrapping of Epon 862 Resin Molecule on Carbon Nanotube
Determining the wetting properties of carbon nanotubes is extremely important in nanotube-polymer composite applications. Actually, the analytic methods for the wetting behavior investigation at nanoscale or atomic scale are not yet well defined and developed [16].

Intensive attractive interactions between carbon nanotube and polymer molecules are essential for good wetting of nanotube composites. To simulate the interactions of carbon nanotubes and Epon 862 molecules, a MD simulation model was established with an Epon 862 resin molecule initially placed at the side of a (10,10) SWNT.

Snapshots of MD simulations are shown in Figure 7. Initially, the chain of Epon 862 resin molecule was twisted severely. One end of the chain was put near the nanotube's wall, while the other end was placed away from the nanotube. The simulation shows that during the initial $16ps$, the resin molecule was expanding the chain around the nanotube axis. The atoms in the resin molecule away from the nanotube moved towards the wall of the nanotube. After a long equilibration period of $100ps$, the chain of the resin molecule eventually tended to spirally wrap on the surface of the helix of the nanotube. The nanotube could maintain its overall shape and only a slight distortion of its cross section occurred during the interaction.

![](./images/813200696487706625_7.jpg)

Figure 7. MD simulations of Epon resin molecule wrapping SWNT

Similarly, the wrapping of the nanotube by the Epon 862 resin molecule can be illustrated by tracking the energy of the “nanotube-Epon 862 resin” system, as shown in Figure 8. The system has a smaller potential energy when the Epon 862 resin molecule well wrapped the nanotube. During this interaction, formation of chemical bonding did not occur. Nanotube and resin molecules were only subjected to the van der Waals forces. Consequently, the interaction energy between the carbon nanotube and the Epon 862 resin molecule was decreased by 40 kcal/mol.

![](./images/813200696487706625_8.jpg)

Figure 8. Variations of the energy during resin molecule wrapping nanotube: (a) potential energy and (b) interaction energy between the nanotube and the Epon 862 resin molecule

### Molecular Interactions Within Nanoscale Pore Structure
Within the modeled nanoscale pore structure exists a complicated molecular interaction. Snapshots of MD simulations are shown in Figure 9. Initially, the EPON 862 resin molecules were placed near the opening of the pore (some slightly inside the pore, some well outside the pore). The simulation shows that during the initial $10ps$, the resin molecules were changing their orientations and moving towards the nanotubes. After a long equilibration period of $80ps$, the resin molecules close to a nanotube eventually moved closer and

wrapped the nanotube due to their molecular interactions. However, the resin molecules in the middle of the pore remained in the same place and tended to aggregate together due to their relatively large distances from nanotubes and thus the weak interactions with the nanotubes. This finding suggests that an external pressure is required to drive the resin molecules to properly go through such nanoscale pore structure during the nanocomposite processing.

![](./images/813200696487706625_9.jpg)

Figure 9. MD simulation of molecular interactions within a nanoscale pore structure

## CONCLUSIONS

The molecular dynamic simulations show that (10,10) SWNT can be automatically filled and wrapped by Epon 862 resin molecules through their molecular interactions at room temperature, implying that (10,10) SWNT and Epon 862 resin molecules have the ability to create the desired wetting in nanocomposites due to their molecular properties. Our research also shows that an external pressure is required to drive resin molecules to flow through a $6nm \times 6nm$ pore structure of SWNTs during nanocomposite processing. Based on the properly established molecular models and MD simulations, the quantitative results for molecular interactions can be obtained for material selection and process optimization in nanotube reinforced nanocomposites development.

## ACKNOWLEDGEMENTS

The authors would like to acknowledge the support received from the Air Force Research Laboratory and FSU Research Foundation

## REFERENCES

1. Iijima S, Helical microtubules of graphitic carbon, Nature, 1991; 354: 56-58.
2. Cooper CA, Young RJ, and Halsall M, Investigation into the deformation of carbon nanotubes and their composites through the use of Raman spectroscopy, Composites Part A: Applied Science and Manufacturing, 2001; 32: 401-411.
3. Schadler LS, Giannaris SC and Ajayan PM, Load transfer in carbon nanotube epoxy composites, Applied Physics Letter, 1998; 73(26): 3842-3844.
4. Qian DL and Dickey EC, Load transfer and deformation mechanics in carbon nanotube-polystyrene composites. Applied Physics Letters, 2000; 76(20): 2868-2870.
5. Ajayan, PM, Carbon nanotube: novel architecture in nanometer space, Progress Crystal Growth and Characterization, 1997; 34: 37-51.
6. Dujardin E, Ebbesen TW, Hiura H, and Tanigaki K, Capillarity and wetting of carbon nanotubes, Science, 1994; 265: 1850-1852.
7. Thostenson ET, Ren ZF, and Chou TW, Advances in the science and technology of carbon nanotubes and their composites: a review, Composites Science and Technology, 2001; 61: 1899-1912.
8. Ajayan PM, Schadler LS, and Giannaris C, and Rubio A, Single-walled carbon nanotube-polymer composites: strength and weakness, Advanced Materials, 2000; 12(10): 750-753.
9. Jin ZX, Pramoda KP, Xu GQ, and Goh SH, Dynamic mechanical behavior of melt-processed multi-walled carbon nanotube/Poly (Methyl Methacrylate) composites, Chemical Physics Letters, 2001; 337: 43-47.
10. Lozano K, Rios J, and Barrera EV, A study of nanofiber-reinforced thermoplastic Composites (II): Investigation of mixing rheology and conduction Properties, Journal of Applied Polymer Science, 2001; 80: 1162-1172.

11. Saito R, Dresselhaus G & Ms Dresselhaus.
Physical properties of carbon nanotubes. 1st ed.
London: Imperial College Press, 1999.

12. Lourie O, Cox DM, Wagner HD. Buckling and
collapse of embedded carbon nanotubes. Physical
Review Letters 1998; 81(8): 1638-1641.

13. Bower C. Rosen, and Jin L. Deformation of carbon
nanotubes-polymer composites. Applied Physics
Letters 1999; 74(22): 3317-3319.

14. Materials Studio, User's Manual, Version 1.2,
Accelrys, Inc., San Diego, CA, 2001.

15. Ajayyan PM and Ijima S. Capillarity-induced
filling of carbon nanotubes, Nature, 1993; 361:
333-334.

16. Fan CF and Cagin T, Wetting of crystalline
polymer surfaces: A molecular dynamics
simulation. Journal of Chemical Physics, 1995; 103
(20): 9053-9061.