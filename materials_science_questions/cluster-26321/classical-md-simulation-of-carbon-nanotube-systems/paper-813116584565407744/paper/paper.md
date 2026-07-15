# Interruption of Hydrogen Bonding Networks of Water in Carbon Nanotubes Due to Strong Hydration Shell Formation

Yoshifumi Oya, $^{\dagger}$ Kenji Hata, $^{\ddagger}$ and Tomonori Ohba*,†

$^{\dagger}$ Graduate School of Science, Chiba University, 1-33 Yayoi, Inage, Chiba 263-8522, Japan
$^{\ddagger}$ Nanotube Research Center, National Institute of Advanced Industrial Science and Technology (AIST), 1-1-1 Higashi Tsukuba, Ibaraki 305-8565, Japan

Supporting Information

**ABSTRACT:** We present the structures of NaCl aqueous solution in carbon nanotubes with diameters of 1, 2, and 3 nm based on an analysis performed using X-ray diffraction and canonical ensemble Monte Carlo simulations. Anomalously longer nearest-neighbor distances were observed in the electrolyte for the 1-nm-diameter carbon nanotubes; in contrast, in the 2 and 3 nm carbon nanotubes, the nearest-neighbor distances were shorter than those in the bulk electrolyte. We also observed similar properties for water in carbon nanotubes, which was expected because the main component of the electrolyte was water. However, the nearest-neighbor distances of the electrolyte were longer than those of water in all of the carbon nanotubes; the difference was especially pronounced in the 2-nm-diameter carbon nanotubes. Thus, small numbers of ions affected the entire structure of the electrolyte in the nanopores of the carbon nanotubes. The formation of strong hydration shells between ions and water molecules considerably interrupted the hydrogen bonding between water molecules in the nanopores of the carbon nanotubes. The hydration shell had a diameter of approximately 1 nm, and hydration shells were thus adopted for the nanopores of the 2-nm-diameter carbon nanotubes, providing an explanation for the large difference in the nearest-neighbor distances between the electrolyte and water in these nanopores.

![](./images/813116584565407744_1.jpg)

## 1. INTRODUCTION

The properties of electrolytes in carbon nanospaces are an important subject of multidisciplinary science, especially in biochemistry, electrochemistry, and separation science. Ion channels in biomembranes, which are composed of hydrophobic carbon nanospaces, control the penetration of ions and subsequent bioactivities. Potassium ions enter potassium channels with a diameter of 1.2 nm and gain access to hydrophobic nanospaces with diameters larger than 0.4 nm with the assistance of inner helix bundles. $^{1,2}$ Transport through a model mimicking an ion channel suggests that the ions form one-dimensional solvation complex structures. $^{3}$ Electric double-layer capacitors provided high power density, fast charge and discharge cycles, and long durability because ions were physically adsorbed in the carbon nanospaces. $^{4}$ Molecular modeling and simulations of electric double-layer capacitors have shed light on the structures and dynamics of electrolytes, contributing to advancements in electric double-layer capacitor technology. $^{5,6}$ Effective charging of electrodes was observed for pore sizes slightly smaller than the hydration diameters of the ions, especially in subnanometer pores. $^{7-11}$ The maximum capacitance performances were also observed for pore sizes close to counterion sizes, preventing the adsorption of counterions in the pores. $^{12,13}$ Small carbon nanotubes (CNTs) also excluded counterions, whereas large CNTs included both ions with a multilayer solvation structure. $^{14}$ Water desalination with high permeability can be achieved using porous graphene. $^{15}$ The hydrophobic graphene pores rejected much more salt than hydrophilic graphene pores. However, the oxygen functional groups on the graphene pores prevented $Cl^{-}$ ions from penetrating the graphene. $^{16}$ Surwade and co-workers experimentally demonstrated water desalination using single-layer graphene, showing nearly 100% purification. $^{17}$ Selecting the appropriate CNT diameter and oxygen functional groups enabled ion species to be distinguished and separated. $^{18,19}$

A molecular-scale understanding of electrolytes in nanospaces is necessary using model structured materials to achieve improved performances for capacitor and desalination applications and to clarify the ion permeation mechanism through ion channels. CNTs, which consist of simple one-

Special Issue: Tribute to Keith Gubbins, Pioneer in the Theory of Liquids

Received: May 22, 2017
Revised: July 1, 2017

dimensional nanopores, are ideal porous materials for examining the structure and dynamic properties of electrolytes. Various studies have been conducted on the fundamental properties of electrolytes in CNTs. Ion permeation through hydrophobic CNTs associated with dehydration is restricted by a high energy barrier. $^{20}$ Ions remain in their hydration forms even in narrow CNTs to maintain stability. $^{21}$ In addition, ions with the same charge avoid being located together in short CNT nanopores when ions penetrate through. $^{22}$ Shao et al. proposed that a weaker hydration shell of $Na^{+}$ was formed in 0.87–1.28-nm-diameter CNTs than in the bulk electrolyte based on MD simulations, whereas CNTs with diameters smaller than 0.87 nm provided strong hydration shells. $^{23}$ However, a strong hydration shell was experimentally observed in NaCl aqueous solution in 2-nm-diameter CNTs. $^{24}$ Electrolyte structures in CNTs have mainly been studied using molecular simulations, and there is a lack of experimental results and connections between experimental and simulated structures.

In this study, we evaluated the structures of NaCl aqueous solution in CNTs with average diameters of 1, 2, and 3 nm using X-ray diffraction (XRD) combined with canonical ensemble Monte Carlo (CEMC) simulations. Our results provide evidence of the CNT-diameter-dependent hydration structures of ions.

## 2. EXPERIMENTAL AND SIMULATION PROCEDURES

2.1. Experiments. Three types of CNTs were synthesized using the high-pressure carbon monoxide method (Unidym Inc., Menlo Park, CA), supergrowth method (provided by the Hata group, AIST, Ibaraki, Japan), $^{25}$ and chemical vapor deposition (NanoLab Inc., Waltham, MA). These CNTs were labeled 1, 2, and 3 nm CNTs, respectively, on the basis of the evaluation of the CNT diameter distributions using transmission electron microscopy (JEM-2100F, JEOL Co., Tokyo, Japan) at 120 kV. The diameters of more than 500 CNTs were considered in determining the distributions. The CNTs were immersed in 0.5 M NaCl aqueous solution for more than 1 week and then were collected by filtration with flushing with deionized water to remove electrolyte from the external surfaces of the CNTs. The CNTs were then rapidly placed in a 0.5-mm-diameter glass capillary tube; the relative humidity was maintained at 85% for 2 days before sealing the tube to remove excess water from the external surfaces of the CNTs. Synchrotron XRD patterns for dried CNTs and CNTs that had adsorbed 0.5 M NaCl aqueous solution were collected for 20 min at 300 K on the BL02B2 beamline at the SPring-8 synchrotron radiation facility. The wavelength was 0.09995 nm. Electron radial distribution functions (ERDFs) were calculated from the XRD patterns using Fourier transforms.

2.2. Monte Carlo Simulations. CEMC simulations of NaCl aqueous solution in single-walled CNTs at 300 K were performed to evaluate the electrolyte structure. In the CEMC simulations, the movement of ions and water molecules were attempted equally. The exchange among ions and water molecules was also attempted to smoothly reach an equilibrium state. In the calculation cycles, the use of $10^{7}$ steps was sufficient to achieve equilibrium in these systems, as evaluated from the total potentials. The CNTs had diameters of 0.8, 1.7, and 2.7 nm, resembling the actual CNTs of 1, 2, and 3 nm, respectively, and lengths of 6.1 nm and were embedded in the holes of two graphene sheets with sizes similar to the CNT diameters to avoid adsorption in the external nanopores of the CNTs, as described later. The CNTs had no partial charges, and image forces were not considered in this study, although a more detailed discussion would be possible if they were considered. $^{26,27}$ The unit cell size was $10.0 \times 5.66 \times 5.54$ nm$^{3}$. The cutoff length of the interaction potentials was set to 2.5 nm for all three directions. Ions and water molecules freely moved between the internal nanopores of the CNTs and reservoirs. As initial configurations, $30$ Na$^{+}$ ions, $30$ Cl$^{-}$ ions, and 3000 water molecules were randomly positioned in the internal nanopores of the CNTs and reservoirs under the condition of a larger distance than the contact distance among ions and water molecules. A CEMC simulation in the bulk electrolyte in a $5.0 \times 5.0 \times 5.0$ nm$^{3}$ unit cell was also performed for comparison. The numbers of $Na^{+}$ ions, $Cl^{-}$ ions, and water molecules in the bulk were 38, 38, and 3800, respectively. The intermolecular interactions were calculated using a combination of Lennard–Jones and Coulomb potentials. The intermolecular interaction of water molecules was calculated using the TIPSP model proposed by Mahoney and Jorgensen with the following parameters: $\varepsilon_{H_{2}O}/k_{B} = 80.5116$ K, $\sigma_{H_{2}O} = 0.312$ nm, $q_{H}/e = +0.241$ C, and $q_{lone\_pair}/e = -0.241$ C.$^{28}$ The potential parameters of ions and carbon atoms of a CNT were $\varepsilon_{Na}/k_{B} = 1.40$ K, $\sigma_{Na} = 0.333$ nm, $q_{Na}/e = +1.0$ C, $\varepsilon_{Cl}/k_{B} = 59.3$ K, $\sigma_{Cl} = 0.442$ nm, $q_{Cl}/e = -1.0$ C, $\varepsilon_{C}/k_{B} = 30.14$ K, $\sigma_{C} = 0.3416$ nm, and $q_{C}/e = 0.0$ C.$^{29,30}$ Lorentz–Berthelot mixing rules and the Ewald summation technique were adopted to determine the intermolecular interactions between different molecular species and the long-range interactions between partial charges, respectively.

## 3. RESULTS AND DISCUSSION

Figure 1 presents TEM images of the CNTs and shows the CNT diameter distributions. The CNT diameters were

![](./images/813116584565407744_2.jpg)

Figure 1. TEM images of CNTs and diameter distributions of 1 nm CNTs (blue), 2 nm CNTs (red), and 3 nm CNTs (green) (bottom right).

determined to be $1.0 \pm 0.2$, $2.0 \pm 0.6$, and $2.9 \pm 0.8$ nm for the 1, 2, and 3 nm CNTs, respectively, which agrees with the pore diameters previously determined from $N_{2}$ adsorption isotherms. $^{31}$ We assumed that the NaCl aqueous solution was mainly introduced into the internal nanopores of the CNTs even though some water molecules and ions could be adsorbed in the external nanopores because the water vapor adsorption amounts in the internal nanopores were much larger than those in the external nanopores based on geometrical assumptions. $^{31}$

XRD patterns of the electrolyte adsorbed in the CNTs and the CNTs only are presented in Figure S1. Scattering by the electrolyte increased the intensity, whereas the small-angle scattering was rarely affected. These tendencies support the assumption of the electrolyte mainly being introduced through the internal nanopores. The XRD patterns of the adsorbed

electrolyte were obtained from the difference between the XRD patterns of the electrolyte adsorbed in the CNTs and those of the CNTs only (Figure 2a). The XRD pattern of the bulk electrolyte perfectly corresponds with that of bulk water, with three peaks at 20, 28, and $44\ \text{nm}^{-1}$; the water structure was thus dominant (Figure S2). However, the XRD patterns of the electrolyte in the CNTs differed from that of the bulk, especially for the 1 nm CNTs. The first peaks in the 1, 2, and 3 nm CNTs were located at 21, 19, and $19\ \text{nm}^{-1}$, respectively. The peak positions for the 1 nm CNTs were shifted to higher values compared to those for the bulk electrolyte, whereas those in the 2 and 3 nm CNTs were shifted to lower values. In the 2 and 3 nm CNTs, the two minor peaks at 30 and $52\ \text{nm}^{-1}$ may be associated with remaining CNT scattering and/or the formation of an icelike structure. $^{31}$ These two peaks disappeared in the 1 nm CNTs. Instead, the peak at $30\ \text{nm}^{-1}$ might be a result of excessive subtraction of the CNTs. However, a major broad peak appeared at approximately $42\ \text{nm}^{-1}$ for the 1 nm CNTs. The ERDFs were calculated from the differential XRD patterns in Figure 2a and were used to determine the intermolecular distances in the CNTs (Figure 2b). Distances shorter than 0.15 nm resulted from the intramolecular correlation and are not discussed here. The ERDF peak positions were rarely changed even with the removal of the XRD pattern near $30\ \text{nm}^{-1}$. The ERDF peaks in the bulk electrolyte at 0.30, 0.46, and 0.7 nm were assigned as the nearest, second-nearest, and third-nearest neighbor distances of water molecules, respectively. Another small peak at 0.37 nm was rarely expected from the interwater distance, which was from the ion−water correlation, as discussed later. Three peaks at 0.29, 0.39, and 0.46 nm were clearly observed in the ERDFs for the 2 and 3 nm CNTs. The interwater distances of 0.29 nm were slightly shorter than that in the bulk electrolyte, whereas the third peaks assigned as the second-nearest-neighbor distance between water molecules were unchanged. The intensities of the second peaks increased considerably compared to that for the bulk electrolyte solution. The electrolyte in the 1 nm CNTs showed three peaks at 0.26, 0.33, and 0.42 nm, which clearly differed from the others. The first peak at 0.26 nm was too short to be considered the interwater distance because the interwater distance in bulk ice is 0.28 nm. Therefore, the second peak at 0.33 nm could be the peak associated with the interwater distance. The distance between water molecules was significantly longer than the others as well as the third peak in the 1 nm CNTs. The peak at 0.13−0.18 nm was observed only in the 1 nm CNTs, which might be attributed to the relatively strong interwater OH correlation. $^{32}$ The relatively strong OH correlation contradicted the above longer interwater distance. This finding can be explained by some water molecules forming strong hydrogen bonds, whereas the majority were separated. A detailed discussion of the ERDFs is presented later and compared with the results obtained using simulations.

![](./images/813116584565407744_3.jpg)

Figure 2. (a) XRD patterns of NaCl aqueous solutions in CNTs with diameters of 1 nm (blue), 2 nm (red), and 3 nm (green). The XRD pattern of the bulk electrolyte is shown for comparison. (b) ERDFs of NaCl aqueous solutions in CNTs and the bulk electrolyte.

The nearest-neighbor distances between water molecules in the electrolyte in the CNTs were compared to assess the intermolecular correlation, as shown in Figure 3. The nearest-neighbor distances in water in the CNTs were obtained from our previous report. $^{31}$ The nearest-neighbor distance of the bulk electrolyte was approximately 0.30 nm, corresponding to that of bulk water. The distances in the electrolyte and water in the 1 nm CNTs were longer than those in the bulk electrolyte and water, respectively, whereas those in the 2 and 3 nm CNTs were shorter than those in the bulk electrolyte. The water structures in the 2 and 3 nm CNTs were icelike, where the intermolecular distance of bulk ice is 0.28 nm. However, the longer intermolecular distance of 0.32 nm in the 1 nm CNTs compared to that in bulk liquid water was between those of liquid and gas phases, suggesting a supercritical gaslike structure. These phases were also expected in the nanopores based on the hydrogen bonding numbers in our previous study. $^{31}$ The intermolecular distances in the electrolyte in the CNTs were longer than those in water in the CNTs. Therefore, the hydrogen bonding between water molecules was somewhat broken instead of consisting of hydration formation with ions. Significant hydration formation was observed in the 2 nm CNTs. $^{24}$ We observed the largest difference of the intermolecular distance between water and the electrolyte in the 2 nm CNTs.

![](./images/813116584565407744_4.jpg)

Figure 3. Interwater distances in the electrolyte (red curve) and water (blue curve) in 1−3 nm CNTs. The bulk electrolyte and water are depicted by the black dashed line.

Snapshots of the electrolyte in the CNTs and the bulk electrolyte are presented in Figure 4. Ions and water molecules

![](./images/813116584565407744_5.jpg)

Figure 4. Snapshots of the electrolyte in 1 nm CNTs (a), 2 nm CNTs (b), and 3 nm CNTs (c) and of the bulk electrolyte (d). The close-up images of the electrolyte in CNTs and bulk were inserted into ellipsoids. $Na^{+}$ ions, $Cl^{-}$ ions, and water molecules are depicted by green spheres, yellow spheres, and blue spheres (O atoms) with two red rods (H atoms), respectively. CNTs sandwiched by two graphenes with holes are depicted by black lines.

![](./images/813116584565407744_6.jpg)

Figure 5. Simulated radial distribution functions between $Na^{+}$−water (blue curves), $Cl^{-}$−water (red curves), $Na^{+}-Cl^{-}$ (green curves), and water−water (black curves) in the 1 nm (a), 2 nm (b), and 3 nm CNTs (c) and the bulk electrolyte (d). The experimental ERDFs from Figure 2b are shown at the bottom for comparison.

could move in and out of the CNTs in these calculations. The 1 nm CNTs had an effective nanopore diameter of 0.6 nm, which is the carbon surface−surface distance and could contain one or two $Na^{+}$ ions, one $Cl^{-}$ ion, and two water molecules. The snapshot in the 1 nm CNTs shows the presence of single $Na^{+}$ and $Cl^{-}$ ions and double-stranded helical water chains, which was also observed in the water adsorbed in CNTs.³³ The narrow nanopores prevented ions and water molecules from forming enough hydration shells and hydrogen bonds, respectively. However, in the 2 and 3 nm CNTs, ions and water molecules had sufficient space to form hydration shells and hydrogen bonds. Hydration numbers of $Na^{+}$ and $Cl^{-}$ ions evaluated from those snapshots were consistent with our preceding results (Figure S3).²¹ Considerable dehydration of $Na^{+}$ and $Cl^{-}$ ions in the 1 nm CNT was observed, whereas hydration numbers in the 2 nm CNT were similar to those in the bulk. In the 2 nm CNT, the hydration numbers of $Na^{+}$ and $Cl^{-}$ ions were slightly decreased and increased, respectively. The hydration shells of $Na^{+}$ and $Cl^{-}$ ions, which were approximately 1 nm in diameter, fit well in the effective nanopore diameter of 1.6 nm in the 2 nm CNT. Therefore, significant hydration shell formation of $Cl^{-}$ ions and the largest difference of the nearest-neighbor distances in the electrolyte and water were observed in the 2 nm CNTs.

The simulated radial distribution functions in Figure 5 calculated from the snapshots in Figure 4 were compared with the experimental ERDFs to analyze the structures of the electrolyte in the CNTs. The peak intensities were corrected using the molecular scattering factors among $Na^{+}$, $Cl^{-}$, and water molecules. The ERDF in the bulk electrolyte revealed a

peak at 0.30 nm and broad peaks at 0.37 and 0.46 nm, whereas the peak of the simulated interwater distance appeared at 0.29 nm. The nearest-neighbor distances roughly corresponded with the experimental results because the simulated nearest-neighbor peak was distributed to a longer distance. The simulated result indicates slightly stronger hydrogen bonding formation than in the experiment. A more ordered water structures in CNTs was observed in the higher water density region.⁴ The experimental electrolyte densities in CNTs might be smaller than 1.0 mg mL⁻¹, and the simulated densities were nearly 1.0 mg mL⁻¹. This caused stronger hydrogen bonding in the simulations than in the experiments. The experimental peaks of 0.26, 0.33, and 0.42 nm in the 1 nm CNTs were attributed to the Na⁺–water, Cl⁻–water, and water–water second-neighbor distances, respectively. The simulated water–water distance of 0.28 nm was rarely observed experimentally, although some strong hydrogen bonding might be expected in experiments. However, the shoulder peak of 0.33 nm agreed with the experimental result. Thus, the strong hydrogen bonding associated with the 0.28 nm peak was considerably weakened, and the peak at 0.33 nm attributed to weak interwater interaction appeared. The ERDF peaks in the 2 and 3 nm CNTs were located at 0.29 and 0.39–0.46 nm, which are consistent with the simulated nearest-neighbor distances and broad second-neighbor (or higher-neighbor) distance, respectively, suggesting stronger hydrogen bonding formation than in the bulk.

In this study, we evaluated the structures of the electrolyte in CNTs using XRD analyses combined with CEMC simulations. The intermolecular distance in the 1 nm CNTs was longer than those in the 2 and 3 nm CNTs and the bulk because of weakened hydrogen bonding resulting from the restricted nanopores of the CNTs. In the 2 and 3 nm CNTs, hydrogen bonding in the electrolyte was slightly weakened compared to that in water as a result of significant hydration shell formation; however, the hydrogen bonding was still stronger than that in the bulk. Therefore, in CNTs, ions anomalously attracted water molecules and formed strong hydration shells, reducing the hydrogen bonding between water molecules.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.langmuir.7b01712.

XRD patterns of CNTs, electrolyte adsorbed in CNTs, bulk electrolyte, and bulk water (PDF)

## AUTHOR INFORMATION

### Corresponding Author
*E-mail: ohba@chiba-u.jp.

### ORCID
Tomonori Ohba: 0000-0001-8207-3630

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
The XRD data at SPring-8 were corrected with help from Dr. S. Kawaguchi. This research was supported by the Japan Society for the Promotion of Science KAKENHI (grant numbers 26706001 and 15K12261) and the Futaba Electronics Memorial Foundation.

## REFERENCES
(1) Jiang, Y.; Lee, A.; Chen, J.; Cadene, M.; Chait, B. T.; MacKinnon, R. The Open Pore Conformation of Potassium Channels. Nature 2002, 417, 523−526.
(2) MacKinnon, R. Potassium Channels. FEBS Lett. 2003, 555, 62−65.
(3) Skerra, A.; Brickmann, J. Structure and Dynamics of One-Dimensional Ionic Solutions in Biological Transmembrane Channels. Biophys. J. 1987, 51, 969−976.
(4) Simon, P.; Gogotsi, Y. Capacitive Energy Storage in Nanostructured Carbon-Electrolyte Systems. Acc. Chem. Res. 2013, 46, 1094−1103.
(5) Burt, R.; Birkett, G.; Zhao, X. S. A Review of Molecular Modelling of Electric Double Layer Capacitors. Phys. Chem. Chem. Phys. 2014, 16, 6519−6538.
(6) Ohba, T. Fast Ion Transportation Associated with Recovering Hydration Shells in a Nanoelectrolyte between Conical Carbon Nanopores During Charging Cycles. J. Phys. Chem. C 2017, 121, 10439−10444.
(7) Bo, Z.; Yang, H.; Zhang, S.; Yang, J.; Yan, J. Molecular Insights into Aqueous Nacl Electrolytes Confined within Vertically-Oriented Graphenes. Sci. Rep. 2015, 5, 14652.
(8) Chmiola, J.; Largeot, C.; Taberna, P. L.; Simon, P.; Gogotsi, Y. Desolvation of Ions in Subnanometer Pores and Its Effect on Capacitance and Double-Layer Theory. Angew. Chem., Int. Ed. 2008, 47, 3392−3395.
(9) Chmiola, J.; Yushin, G.; Gogotsi, Y.; Portet, C.; Simon, P.; Taberna, P. L. Anomalous Increase in Carbon Capacitance at Pore Sizes Less Than 1 Nanometer. Science 2006, 313, 1760−1763.
(10) Largeot, C.; Portet, C.; Chmiola, J.; Taberna, P.-L.; Gogotsi, Y.; Simon, P. Relation between the Ion Size and Pore Size for an Electric Double-Layer Capacitor. J. Am. Chem. Soc. 2008, 130, 2730−2731.
(11) Frackowiak, E. Carbon Materials for Supercapacitor Application. Phys. Chem. Chem. Phys. 2007, 9, 1774−1785.
(12) Varanasi, S. R.; Bhatia, S. K. Capacitance Optimization in Nanoscale Electrochemical Supercapacitors. J. Phys. Chem. C 2015, 119, 17573−17584.
(13) Qiu, Y.; Chen, Y. Capacitance Performance of Sub-2 Nm Graphene Nanochannels in Aqueous Electrolyte. J. Phys. Chem. C 2015, 119, 23813−23819.
(14) Shim, Y.; Kim, H. J. Nanoporous Carbon Supercapacitors in an Ionic Liquid: A Computer Simulation Study. ACS Nano 2010, 4, 2345−2355.
(15) Cohen-Tanugi, D.; Grossman, J. C. Water Desalination across Nanoporous Graphene. Nano Lett. 2012, 12, 3602−3608.
(16) Konatham, D.; Yu, J.; Ho, T. A.; Striolo, A. Simulation Insights for Graphene-Based Water Desalination Membranes. Langmuir 2013, 29, 11884−11897.
(17) Surwade, S. P.; Smirnov, S. N.; Vlassiouk, I. V.; Unocic, R. R.; Veith, G. M.; Dai, S.; Mahurin, S. M. Water Desalination Using Nanoporous Single-Layer Graphene. Nat. Nanotechnol. 2015, 10, 459−464.
(18) Park, J. H.; Sinnott, S. B.; Aluru, N. R. Ion Separation Using a Y-Junction Carbon Nanotube. Nanotechnology 2006, 17, 895−900.
(19) Gong, X.; Li, J.; Xu, K.; Wang, J.; Yang, H. A Controllable Molecular Sieve for Na+ and K+ Ions. J. Am. Chem. Soc. 2010, 132, 1873−1877.
(20) Beckstein, O.; Tai, K.; Sansom, M. S. Not Ions Alone: Barriers to Ion Permeation in Nanopores and Channels. J. Am. Chem. Soc. 2004, 126, 14694−14695.
(21) Ohba, T.; Kanoh, H. Energetic Contribution to Hydration Shells in One-Dimensional Aqueous Electrolyte Solution by Anomalous Hydrogen Bonds. Phys. Chem. Chem. Phys. 2013, 15, 5658−5663.
(22) Liu, H.; Murad, S.; Jameson, C. J. Ion Permeation Dynamics in Carbon Nanotubes. J. Chem. Phys. 2006, 125, 084713.

(23) Shao, Q.; Zhou, J.; Lu, L.; Lu, X.; Zhu, Y.; Jiang, S. Anomalous Hydration Shell Order of $Na^{+}$ and $K^{+}$ inside Carbon Nanotubes. *Nano Lett.* **2009**, 9, 989−994.

(24) Ohba, T.; Hata, K.; Kanoh, H. Significant Hydration Shell Formation Instead of Hydrogen Bonds in Nanoconfined Aqueous Electrolyte Solutions. *J. Am. Chem. Soc.* **2012**, 134, 17850−17853.

(25) Hata, K.; Futaba, D. N.; Mizuno, K.; Namai, T.; Yumura, M.; Iijima, S. Water-Assisted Highly Efficient Synthesis of Impurity-Free Single-Walled Carbon Nanotubes. *Science* **2004**, 306, 1362−1364.

(26) Kondrat, S.; Georgi, N.; Fedorov, M. V.; Kornyshev, A. A. A Superionic State in Nano-Porous Double-Layer Capacitors: Insights from Monte Carlo Simulations. *Phys. Chem. Chem. Phys.* **2011**, 13, 11359−11366.

(27) Ohba, T. Significant Curvature Effects of Partially Charged Carbon Nanotubes on Electrolyte Behavior Using Monte Carlo Simulations. *Phys. Chem. Chem. Phys.* **2016**, 18, 14543−14548.

(28) Mahoney, M. W.; Jorgensen, W. L. A Five-Site Model for Liquid Water and the Reproduction of the Density Anomaly by Rigid, Nonpolarizable Potential Functions. *J. Chem. Phys.* **2000**, 112, 8910−8922.

(29) Shao, Q.; Huang, L.; Zhou, J.; Lu, L.; Zhang, L.; Lu, X.; Jiang, S.; Gubbins, K. E.; Shen, W. Molecular Simulation Study of Temperature Effect on Ionic Hydration in Carbon Nanotubes. *Phys. Chem. Chem. Phys.* **2008**, 10, 1896−1906.

(30) Ohba, T.; Takase, A.; Ohyama, Y.; Kanoh, H. Grand Canonical Monte Carlo Simulations of Nitrogen Adsorption on Graphene Materials with Varying Layer Number. *Carbon* **2013**, 61, 40−46.

(31) Ohba, T. Size-Dependent Water Structures in Carbon Nanotubes. *Angew. Chem.* **2014**, 126, 8170−8174.

(32) Soper, A. K.; Ricci, M. A. Structures of High-Density and Low-Density Water. *Phys. Rev. Lett.* **2000**, 84, 2881−2884.

(33) Perez-Hernandez, G.; Schmidt, B. Anisotropy of the Water-Carbon Interaction: Molecular Simulations of Water in Low-Diameter Carbon Nanotubes. *Phys. Chem. Chem. Phys.* **2013**, 15, 4995−5006.

(34) Sadeghi, M.; Parsafar, G. A. Density-Induced Molecular Arrangements of Water inside Carbon Nanotubes. *Phys. Chem. Chem. Phys.* **2013**, 15, 7379−7388.