# Direct imaging of hydrogen-driven dislocation and strain field evolution in a stainless steel grain

David Yang* Mujan Seif Guanze He Kay Song Adrien Morez Benjamin de Jager Ross J. Harder Wonsuk Cha Edmund Tarleton Ian K. Robinson Felix Hofmann*

Dr. D. Yang*, Dr. M. Seif, Dr. G. He†, Dr. K. Song§, Mr. A. Morez, Dr. B. de Jager, Prof. E. Tarleton, Prof. F. Hofmann*
Department of Engineering Science, University of Oxford, Oxford, OX1 3PJ, United Kingdom
Email Address: david.yang@eng.ox.ac.uk, felix.hofmann@eng.ox.ac.uk

Dr. D. Yang*, Prof. I. K. Robinson
Condensed Matter Physics and Materials Science Department, Brookhaven National Laboratory, Upton, NY, 11973, United States

Dr. R. J. Harder, Dr. W. Cha
Advanced Photon Source, Argonne National Laboratory, Lemont, IL, 60439, United States

Prof. I. K. Robinson
London Centre for Nanotechnology, University College London, London, WC1E 6BT, United Kingdom

†Present address: Shanghai Nuclear Engineering Research and Design Institute, Shanghai, 200233, China.

§Present address: School of Aerospace, Mechanical and Mechatronic Engineering, The University of Sydney, Sydney, NSW, 2006, Australia.

Keywords: Hydrogen embrittlement, dislocations, strain field, stainless steel, Bragg coherent x-ray diffraction imaging

Hydrogen embrittlement (HE) poses a significant challenge to the durability of materials used in hydrogen production and utilization. Disentangling the competing nanoscale mechanisms driving HE often relies on simulations and electron-transparent sample techniques, limiting experimental insights into hydrogen-induced dislocation behavior in bulk materials. This study employs *in situ* Bragg coherent X-ray diffraction imaging to track three-dimensional dislocation and strain field evolution during hydrogen charging in a bulk grain of austenitic 316 stainless steel. Tracking a single dislocation reveals hydrogen-enhanced mobility and relaxation, consistent with dislocation dynamics simulations. Subsequent observations reveal dislocation unpinning and climb processes, likely driven by osmotic forces. Additionally, nanoscale strain analysis around the dislocation core directly measures hydrogen-induced elastic shielding. These findings experimentally validate theoretical predictions and offer mechanistic insights into hydrogen-driven dislocation behavior, paving the way for the design of HE-resistant materials.

## 1 Introduction

Hydrogen is an attractive energy carrier that can be produced through water electrolysis using renewable resources [1]. This green hydrogen can be used to decarbonize industries that rely heavily on fossil fuels such as aviation [2], heavy transportation [3], industrial production [4], and power generation [1]. As countries strive to reach their Net Zero 2050 sustainability targets, the global production of green hydrogen is forecast to rise annually, reaching 49 million tons per year by 2030 [5]. This necessitates the design of hydrogen fuel systems to store, transport and distribute hydrogen. A long-standing challenge is hydrogen embrittlement (HE), which occurs when hydrogen atoms diffuse into metals, reducing their ductility and strength, leading to premature failure [6]. Austenitic stainless steels (SS), widely used due to their good corrosion resistance and strength, are not immune to this phenomenon. Understanding the mechanisms behind HE is essential to designing the next generation of HE-resistant materials, and will necessitate the study of hydrogen-SS interactions at different length scales.

HE has been extensively studied at the macro scale through mechanical testing, revealing how cracks initiate and propagate in hydrogen-exposed material [7, 8, 9, 10] and can lead to in-service failure. To explain macroscopic behavior, advances in characterization techniques have enabled the exploration of HE at sub-micron length scales, which has been dominated by electron microscopy (EM) experiments and simulations [11, 12, 13]. This

combination of experimental results and theory has led to multiple proposed degradation mechanisms responsible for HE. Here, we will briefly discuss the two most prominent mechanisms. In hydrogen-enhanced localized plasticity (HELP) [7, 8, 14], hydrogen atoms in the metal lattice accumulate at and near the dislocation cores [15] and reduce the elastic stress field, known as hydrogen elastic shielding [16]. This makes it easier for dislocations to move, leading to a localization of deformation, which drives premature material failure. The second mechanism is hydrogen-enhanced decohesion (HEDE) [17, 9], which states that hydrogen atoms accumulate at locations of high triaxial stress, such as grain boundaries or crack tips. The presence of hydrogen reduces the cohesive forces between atoms, weakening the atomic bonds and causing intergranular fracture. The interplay between HELP and HEDE is multifaceted and possibly synergistic [18, 14, 19], though there are still many different opinions about the mechanisms involved in HE [14, 20, 21]. This is because hydrogen is extremely difficult to probe due to its small size, high diffusion rate and low level of interaction with electron probes.

Consequently, there has been a push towards probing in situ responses to hydrogen diffusion to understand degredation mechanisms. Dislocation movement caused by hydrogen desorption has been reported by Koyama et al. [22], where they visualised micron-scale dislocation movements using electron channel contrast imaging (ECCI) on a Fe-Mn-based alloy. Huang et al. [23] revealed bow-out motions of screw dislocations in $\alpha$-Fe pillars undergoing compression tests in a gaseous hydrogen environment using a transmission electron microscope (TEM). This is an extension to the numerous TEM experiments done by the Robertson group to study hydrogen-induced dislocation movement in foil samples [24, 25, 8, 26]. However, EM techniques only probe the surface of a material, and the question of how hydrogen interacts with a single subsurface defect in situ is still experimentally challenging and primarily addressed using simulations [13]. Furthermore, hydrogen elastic shielding has only been inferred based on the observations of dislocation pileup [27], but the hydrogen-modified strain fields have not been directly measured experimentally. This information would greatly enhance our understanding of dislocation-hydrogen interactions to accelerate the development of HE-resistant alloys.

Here we address these shortcomings by using in situ Bragg coherent X-ray diffraction imaging (BCDI) [28] to probe the evolution of a single dislocation and its associated strain field during hydrogen charging (Figure 1a), using a bespoke electrochemical flow cell (Supporting Text and Figure S1). BCDI is a nondestructive technique that captures three-dimensional (3D) nanoscale images of crystal defects and strain fields [29, 30, 31, 32, 33, 34] by inverting coherent X-ray diffraction patterns [35] from a finite crystalline sample. To produce a sample with grains suitable for BCDI, we use high pressure torsion (HPT) [36] to refine the grain structure of a 316 SS disk (composition shown in Table S1), followed by ex situ annealing to allow some controlled grain growth and defect relaxation (Methods). The 111 Bragg peak from an austentitic, face centered cubic (FCC) grain is measured before and during hydrogen charging at standard ambient temperature and pressure (Methods). Phase retrieval algorithms are used to recover the real space electron density and phase from the diffraction data (Methods), revealing information about the grain morphology, dislocations, and strain fields, $\varepsilon_{111}$, along the [111] direction associated with the scattering vector, $\mathbf{Q}_{111}$.

## 2 Results and Discussion

### 2.1 Bragg peak evolution

Upon initiation of charging, hydrogen atoms diffuse into the SS disk, gradually permeating the measured grain and causing localized lattice expansion [37]. This is shown as an increase in the mean lattice parameter of the grain, $a_0$, measured by BCDI throughout hydrogen charging (Figure 1b). We interpret this to cause a homogeneous lattice strain, $e_{111}$, relative to $a_0$ at -3.4 h before charging. Note that $e_{111}$ differs from $\varepsilon_{111}$: the latter is relative to the average lattice parameter at time $t$, $a_{0,t}$ (Methods) [33]. The homogeneous lattice strain results in a volumetric strain due to hydrogen occupying interstitial sites in SS [38]. The volumetric strain is combined with the relaxation volume of hydrogen in austenitic SS to estimate the local hydrogen concentration (Methods), which increases during charging (Figure 1b).

Figure 1b also shows central slices of the Bragg peak at different hydrogen concentrations as insets (see Figure S2 for all Bragg peak slices during charging). To quantify subtle changes, the 3D Pearson correlation coefficient (Methods) is computed between the Bragg peak at different times, shown in Figure 1c. There is negligible change

![](./images/1089059721182183472_1.jpg)
![](./images/1089059721182183472_2.jpg)

Figure 1: In situ hydrogen charging BCDI setup and evolution of the Bragg peak. a), The microcrystalline 316 SS disk is mounted in the electrochemical flow cell (see Supporting Information and Figure S1). An incoming coherent X-ray beam (red) illuminates a grain within the SS disk, and a slice through the reflected 111 Bragg peak is captured on the detector. During in situ charging, a bias is applied to the SS (working electrode). A Pt wire coil (counter electrode) sits inside the flow cell moat. The blue arrows indicate the flow of the hydrogen charging solution. b), The lattice parameter and inferred hydrogen concentration before and during the experiment, with insets showing slices through the center of the Bragg peak corresponding to different times. c), 3D Pearson correlation of the Bragg peaks. Hydrogen charging starts at 0 h.

before 0 h, prior to hydrogen charging. Once hydrogen charging is applied at 0 h, the Bragg peak evolves until 3.2 h, after which it changes little. The evolution of the Bragg peak directly correlates to structural changes in the grain.

### 2.2 Strain at the grain surface
Figure 1b shows a large increase in average $a_0$ with hydrogen, leading to homogeneous strain. Does this homogeneous strain drive an increase in intergranular strain that could drive plasticity, or does hydrogen lead to a predominantly volumetric strain? If there were a substantial increase of intergranular strain, we would expect the surface strain of the grain of interest to increase due to mismatch with its neighbors. Figure 2 shows the time evolution of surface strain. We refer to the surface strain, $\varepsilon_{111,\text{surf.}}$, as the $\varepsilon_{111}$ value of the surface voxel of the reconstruction as determined using an amplitude threshold (Supporting Text). Note the surface strain is limited by our estimate of the 3D spatial resolution of 12 nm, determined using the phase retrieval transfer function (Supporting Text and Figure S3).

The morphology of the grain (Figure 2a) remains stable during the hydrogen charging, however, a softening of the grain edges is noticeable after 1.9 h (Figure S4). Hydrogen is expected to accumulate at grain boundaries [39], recently shown by Chen et al. using cryogenic atom probe tomography [15]. This may explain the apparent rounding of the grain edges in Figure 2, where hydrogen accumulates. We do not observe any grain boundary mobility as noticed in palladium thin film grains undergoing hydrogen adsorption in a previous BCDI study [32].

The distribution of $\varepsilon_{111,\text{ surf.}}$ in Figure 2a is shown in Figure 2b. The mean $\varepsilon_{111,\text{ surf.}}$ is slightly compressive

![](./images/1089059721182183472_3.jpg)

Figure 2: Evolution of the strain field on the grain surface before and during hydrogen charging. a), Different views of the grain surface, colored by $\varepsilon_{111, \text{surf.}}$, the strain relative to the average lattice parameter indicated at the bottom. See Figure S4 and Supporting Video S1 for reconstructions from all time points. b), Histogram distribution of the surface strain for different time points during the hydrogen charging history. c), Evolution of average surface strain. The shaded region corresponds to one standard deviation.

at all times, and the distribution remains largely unchanged during hydrogen charging. This shows that hydrogen has little effect on grain-grain misfit and thus intragranular strains that could drive plasticity. Rather, hydrogen predominantly leads to a large volumetric strain compared to $\varepsilon_{111,\text{surf.}}$. The mean and standard deviation of $\varepsilon_{111,\text{surf.}}$ are plotted in Figure 2c. The reduction in average $\varepsilon_{111,\text{surf.}}$ with increasing charging time suggests a small average compression at grain boundaries. This is consistent with the accumulation of hydrogen at grain boundaries, leading to a slight compression of near-boundary material.

### 2.3 Dislocation dynamics
A phase vortex in a BCDI reconstruction indicates the spatial position of a dislocation core [29], enabling the mapping of the 3D dislocation network (Methods). **Figure 3** shows the dislocation network evolution during hydrogen charging. Initially, the grain shows two small dislocations close to the surface, and one large bow-shaped dislocation that extends across the grain, hereafter to as the "large dislocation." The large dislocation remains unchanged before hydrogen charging and up to 1.9 h after the start of charging. To determine its Burgers vector, we assume that it is a shear loop and lies in the $(\overline{1}11)$ plane, as expected for FCC metals (we confirm the angle between the dislocation glide plane normal and $\mathbf{Q}_{111}$ is $68.9^\circ$, less than $2^\circ$ from the angle between theoretical $\langle 111 \rangle$ directions and within error). Thus, we determine the orientation matrix, $\mathbf{UB}$ (Supporting Text). Glide dislocations in the $(\overline{1}11)$ plane can have three different Burgers vectors $\mathbf{b} = \frac{a_0}{2}[110]$, $\frac{a_0}{2}[101]$ or $\frac{a_0}{2}[0\overline{1}1]$. However, $\mathbf{Q}_{111} \cdot \mathbf{b} \neq 0$ only for $\frac{a_0}{2}[110]$ and $\frac{a_0}{2}[101]$, meaning that only dislocations with these Burgers vectors will be visible in a $\mathbf{Q}_{111}$ crystal reflection [34]. By comparing the measured strain field of the large dislocation to a 3D elastic model and dislocation dynamics simulations, we determine that the large dislocation has Burgers vector $\mathbf{b} = \frac{a_0}{2}[110]$ (Supporting Text, Figs. S5-S6, and Table S2).

After 1.9 h of hydrogen charging, the large dislocation begins to glide (Figure 3). This is remarkable, as Figure 2 shows little change in surface strain, and hence externally-applied stress that could drive plasticity. It suggests that hydrogen either reduces the Peierls barrier for dislocation glide, or unpins the dislocation from obstacles such as alloying elements [40]. Either way, the introduction of hydrogen enables the dislocation to relax, reducing its line length and thus strain energy (Supporting Text and Figure S7) [39]. A discrete dislocation dynamics simulation

![](./images/1089059721182183472_4.jpg)

Figure 3: Evolution of the dislocation network before and during hydrogen charging. a,b,c), Columns represent a different orthogonal view of the grain and the dislocation network. The top row shows the initial morphology of the grain rendered as a grey isosurface. The subsequent rows have translucent renderings of the same grain morphology (largely unchanged, see Figure 2) along with the dislocation network at different states, with glide and climb events indicated. The dislocation dynamics simulation of glide is indicated in green. Dislocation networks are colored according to the time of observation. The black arrow indicates the Burgers vector. See Supporting Video S2 for the dislocation network at each measurement time.

(Methods) is set up with the large dislocation in the position observed before hydrogen charging. The ends of the dislocation are pinned at the grain boundary, consistent with our experimental observation, and the system was then allowed to relax under self-stress. The subsequent dislocation evolution, shown in Figure 3, agrees very well with that observed experimentally. This confirms that the dislocation glide observed in experiments is relaxation-driven, suggesting hydrogen-enhanced dislocation mobility and/or depinning.

Following the glide motion, after 3.2 h of hydrogen charging, one end of the large dislocation becomes unpinned and climbs out of the glide plane. Subsequently, from 3.9 h onwards, the dislocation remains largely unchanged upon further charging. The climb force on a mixed dislocation is the sum of an elastic interaction force and an osmotic force [40]. Figure 2c shows that the average strain on the grain surface changes little, indicating that the contribution of external stresses to dislocation climb will be small. Furthermore, the unpinned dislocation segment is ~ 200 nm from the nearest observable small dislocation, meaning that any dislocation-dislocation forces will be minor [16]. Thus, the climb force on the large dislocation will be dominated by the osmotic force, $F_{\text{os}}$. $F_{\text{os}}$, per unit length of a dislocation line is [40],

$$
\frac{F_{\mathrm{os}}}{L}=-\frac{k_{b} T b_{e}}{v_{a}} \ln \frac{c}{c^{0}},\qquad(1)
$$

where $v_{a}$ is the atomic volume, $c$ is the vacancy concentration, $c^{0}$ is equilibrium concentration of vacancies, and $b_{e}$ is the edge component of the Burgers vector, given by

$$
b_{e}=|\mathbf{b} \times \xi|,\qquad(2)
$$

where $\xi$ is the unit dislocation line segment direction. Here we observe climb mobility to be much higher than expected for FCC materials [41]. Climb requires diffusion of self-interstitial atoms or vacancies to the dislocation line. Our results suggest hydrogen-facilitated climb, driven by the formation and migration of vacancies due to hydrogen influx [42]. This can be rationalized by the superabundant vacancies (SAV) model proposed by Fukai [43], where hydrogen reduces the formation energy of a vacancy by trapping multiple interstitial hydrogen atoms, forming vacancy–hydrogen (vac-H) clusters that are mobile even at room temperature [44]. Furthermore, hydrogen has been demonstrated to enhance metal atom diffusion [43] and lower the vacancy migration free energy barrier in FCC metals [45], which would also drive hydrogen-facilitated climb.

Our observations suggest that once there is a sufficient hydrogen concentration within the grain, there will be enough vac-H clusters and sufficient reduction in vacancy and metal migration energy such that the osmotic force can facilitate climb. The equilibrium concentration of vacancies along the length of the large dislocation depends on the spatial variation of hydrogen concentration. Based on the magnitudes of $e_{111}$ ($\sim 10^{-3}$) compared to $\varepsilon_{111}$ ($\sim 10^{-4}$), increasing hydrogen concentration dominates homogeneous lattice swelling. Therefore, any variations in hydrogen concentration along the dislocation, and by extension, vacancy concentration, are small by comparison. This suggests that differences in $b_{e}$, i.e. the degree of edge character along the dislocation line, will determine which parts of the dislocation climb. **Figure 4** shows a magnified view of the large dislocation before and after the climb at 3.9 h. Each segment of the dislocation is colored by edge character. The edge character is low at the end of the dislocation that does not climb, making this segment less likely to climb due to a lower $F_{\text{os}}$. Conversely, the segment of the dislocation that climbs also has the greatest edge character. The climb direction (magenta arrow in Figure 4) is nearly perpendicular ($89.5^{\circ}$) to the Burgers vector, as expected. After climb, the climbing segment lies on the $(11\overline{1})$ plane. However, since $\mathbf{b}=\frac{a_{0}}{2}[110]$ is not one of the Burgers vectors in this plane, this segment is sessile, explaining the lack of further evolution beyond 3.9 h.

### 2.4 Dislocation strain field evolution

Based on observations of dislocation pileup evolution upon introduction of hydrogen, it has been previously inferred that hydrogen reduces the interaction between dislocations by changing their stress fields [16, 27]. To quantify the changes in the strain field surrounding the large dislocation, we compare slices though the 3D reconstructed volume where $\mathbf{b}$ and $[\overline{1}11]$ (the normal to the initial glide plane of the large dislocation) are in plane and $\xi$ is normal to the slice (i.e. where the large dislocation has predominantly edge character). These slices are shown in **Figure 5**a and b. A theoretical model, devoid of hydrogen, of an edge dislocation strain field projected along

![](./images/1089059721182183472_5.jpg)

Figure 4: Dislocation unpinning and climb. A translucent isosurface of the grain showing only the large dislocation before (1 - at 3.2 h) and after the climb event (2 - at 3.9 h). The dislocation is colored between two nodes based on the $b_e$ (Equation 2), where $b_e/|{\bf b}| = 1$ represents a pure edge dislocation and $b_e/|{\bf b}| = 0$ represents a pure screw dislocation. The black arrow indicates the Burgers vector direction. The magenta arrow, which is nearly perpendicular to the Burgers vector direction, indicates the direction of climb. a), Orthogonal views based on sample coordinates. b), Crystallographic views based on the dislocation loop plane, with the dislocation initially lying on the $(\bar{1}11)$ plane, and later one end unpinning and climbing onto the $(11\bar{1})$ plane.

[111] is shown in Figure 5c (Methods), and compared to the experimental strain field by considering circular line profiles drawn at a 30 nm radius from the dislocation core (Figure 5d). Agreement between the theoretical model and the experiment is initially good, but worsens as the hydrogen concentration increases.

The evolution of strain along the circular line profiles during charging is shown in Figure 5e and f. Figure 5g shows how the maximum and minimum values, averaged over $\pm\pi/8$ around each maximum/minimum, evolve during charging. We observe a reduction of the elastic strain surrounding the dislocation by up to 35% between the start and end of hydrogen charging. This relative reduction agrees well with the computed reduction of edge dislocation-carbon atom interaction energy in $\alpha$-Fe upon introduction of hydrogen [46]. Our observations reveal hydrogen elastic shielding (Figure 5) which has been predicted by simulations [16], and indirectly inferred from *in situ* TEM observations of dislocation pileup evolution following the introduction of hydrogen [27]. These direct BCDI measurements of subtle changes in dislocation strain field are important, since they provide fundamental validation of hydrogen-induced dislocation stress shielding, which is core to the HELP mechanism.

## 3 Conclusion

Using 316 SS as a model system, our results capture the evolution of a single dislocation undergoing glide relaxation, followed by climb. We propose that this sequence is initiated by the introduction of hydrogen into the lattice, which greatly enhances dislocation mobility via several complementary mechanisms: A hydrogen-induced reduction of lattice friction, or Peierls stress, has been predicted by density functional theory (DFT) studies on pure metals using the Peierls-Nabarro model [47]. However, in 316 SS, this reduction is small compared to the pinning stress from alloying elements, given that 316 SS's yield stress is more than twice that of pure iron. In addition, hydrogen accumulation has been predicted to lower the dislocation core energy [48] and reduce the dislocation strain field [46], as we have directly measured (Figure 5). This reduces the elastic interactions of the dislocation with the surrounding environment, such as other dislocations and point defects, allowing easier dislocation glide. Furthermore, our observation that hydrogen greatly enhances dislocation climb mobility (Figure 4) suggests that

![](./images/1089059721182183472_6.jpg)

Figure 5: Evolution of the internal strain field surrounding the large dislocation. Three time points are presented as rows in a,b,c,d). a), Translucent morphologies of the grain with dislocation networks. Slices through $\varepsilon_{111}$ are in-plane to the Burgers vector and the normal to the $(\overline{1}11)$ plane. The average lattice parameter is listed for each time. b), A $\varepsilon_{111}$ slice capturing a section of the large dislocation with pure edge character. See Supporting Video S3 for $\varepsilon_{111}$ slices through the entire grain. c), Theoretical model devoid of hydrogen, $\varepsilon_{111,model}$, of b) (Methods). d), Circular line profiles, drawn at a 30 nm radius from each dislocation core, compared to the model. The shaded region is the standard deviation of the experimental values in the neighboring 26 pixels. Line profiles start at the Burgers vector (horizontal) and run anticlockwise. e), Circular line profiles drawn for each time point of the experiment, plotted as a surface indicating $\varepsilon_{111}$ values. f), Top-down view of e). g), Maximum and minimum values of the line profiles, averaged over a range of $\pi/4$. The shaded region corresponds to one standard deviation of each value.

also during glide, dislocations will be able to "climb around" obstacles that would otherwise lead to dislocation pinning. Together, these observations suggest that, in the presence of hydrogen, the currently accepted view of glide-dominated dislocation motion [16, 14, 27] may no longer hold.

Our findings showcase the unique capability of in situ BCDI to monitor the evolution of nanoscale deformation and defects in a grain exposed to hydrogen under bulk conditions. This advancement is particularly timely as many third-generation synchrotrons are being upgraded to fourth-generation facilities, offering greater coherent flux for BCDI experiments with enhanced spatial and temporal resolution. Importantly, in situ BCDI is applicable to most alloy systems and perfectly complements higher-resolution electron microscopy techniques, computational models, and atomistic simulations to shed light on HE degradation pathways. Understanding these internal mechanisms is key to engineering alloys with enhanced resistance to hydrogen-induced degradation, which are urgently needed to enable the green hydrogen economy.

## 4 Methods

### 4.1 Sample preparation
The SS sample was produced using high pressure torsion (HPT) to produce sub-micron grain sizes appropriate for BCDI. A sheet of 316 A4 austenitic stainless steel (composition shown in Table S1), 1 mm thick, was obtained from RS Components (stock number 264-7241) and cut into a 5 mm diameter disk. The disk then went through HPT to refine the grain microstructure. HPT was performed in a quasi-constrained set-up [36] on a Zwick Roell Z100 Materials Testing machine. Using 5 mm diameter anvils, a compressive force of 80 kN was applied to the face of the disk and maintained for 30 turns using a rotational speed of $5 \, ^\circ\text{s}^{-1}$. The final disk thickness after HPT was $300 \, \mu\text{m}$. The disk was then annealed in vacuum ($5 \times 10^{-6}$ mbar) at $700 \, ^\circ\text{C}$ for 1 hour. Following annealing, the disk was sequentially ground with 800, 1200, and 2500 grit SiC paper, followed by polishing in $3 \, \mu\text{m}$ and 1 $\mu\text{m}$ diamond suspension.

### 4.2 BCDI measurements
BCDI relies on inverting far-field, oversampled [49], 3D coherent X-ray diffraction patterns (CXDPs) for a particular $hkl$ reflection on a finite crystalline material. This is done using phase retrieval algorithms [35] to obtain the grain morphology and associated phase, $\psi_{hkl}(\mathbf{r})$. Dislocation line positions can be readily identified from the positions of phase vortex loci [29], thus making BCDI a valuable tool to study in situ or in operando defect evolution [29, 30, 31, 32, 50]. The strain fields associated with the dislocations can be obtained from the phase, $\psi_{hkl}(\mathbf{r})$, since $\psi_{hkl}(\mathbf{r})$ is a projection of the lattice displacement field, $\mathbf{u}_{hkl}(\mathbf{r})$, onto the scattering vector, $\mathbf{Q}_{hkl}$ [51].

BCDI was performed at beamline 34-ID-C at the Advanced Photon Source (APS) at Argonne National Laboratory, USA. An in situ confocal microscope was used to position the X-ray beam within the disk. The 111 Bragg peak ($2\theta = 34.7^\circ$) was measured for multiple grains to screen for the best candidate grain. Although each candidate's position perpendicular to the X-ray beam can be easily aligned, the position of the candidate along the beam needs to be determined to ensure the grain is on the axis of rotation. We used an approach presented by Shabalin et al. [52] to accomplish this.

For all BCDI measurements, the grain was illuminated using a 10 keV ($\lambda = 0.124$ nm) coherent X-ray beam, with a bandwidth of $\Delta\lambda/\lambda \approx 10^{-4}$ from a Si(111) monochromator. The X-ray beam was focused to a size of 810 nm $\times$ 860 nm (h $\times$ v, full width at half-maximum) using Kirkpatrick–Baez (KB) mirrors. Beam defining slits were used to select the coherent portion of the beam at the entrance to the KB mirrors. CXDPs were collected on a 256 $\times$ 256 pixel module of a 512 $\times$ 512 pixel Timepix area detector (Amsterdam Scientific Instruments) with a GaAs sensor and pixel size of $55 \, \mu\text{m} \times 55 \, \mu\text{m}$ positioned at 1.4 m from the sample to ensure oversampling. The peak of the CXDP was positioned at the center of the detector module before data collection. CXDPs were recorded by rotating the crystal through an angular range of $0.5^\circ$ about the peak and recording an image every $0.005^\circ$ with 0.5 s exposure time and 10 accumulations at each angle.

### 4.3 Hydrogen charging
The disk was attached to the electrochemical flow cell using chemically resistant insulating tape, with the bottom of the disk in contact with a Pt wire, thereby forming the working electrode (WE). The counter electrode (CE)

was another Pt wire coiled into the well, or moat, of the electrochemical cell. The cell was then sealed using an O-ring and a thin kapton film. The flow cell was fixed to the sample stage using a Thorlabs 1X1 kinematic mount and connected to a Cole-Parmer Masterflex peristaltic pump and a SP-300 Biologic potentiostat. See Supporting Information and Figure S1 for further details about the electrochemical flow cell.

A 1 L hydrogen charging solution was prepared using 4 g of NaOH (0.1 mol/L) and 5 g thiourea (0.07 mol/L) dissolved in deionized water, yielding a pH of 13. After an appropriate grain was found, the hydrogen charging solution was continuously pumped into the cell at 5 mL/min. Repeated 111 CXDPs from the grain were measured in solution, without charging, over three hours to verify that there was no effect on the sample. Next, hydrogen charging was performed using chronopotentiometry with a two electrode setup, keeping the current fixed at 0.2 mA (0.5 mA/cm²). During the charging, two repeated BCDI measurements for the 111 refiection were measured approximately every 40 minutes, with each scan requiring approximately 10 minutes to complete. We noticed bubbles slowly form during charging.

## 4.4 Phase retrieval
Before phase retrieval, the repeated CXDPs were corrected for dead-time, darkfield, and whitefield before cross-correlation alignment and summation. The minimum data threshold was 2. The resulting CXDP was binned by a factor of two along each direction of the detector plane, resulting in a size of $128 \times 128 \times 101$ voxels.

The reconstructions were processed using a MATLAB phase retrieval package [29]. The reconstructions for each time point were seeded using a reconstruction from eight repeated CXDPs (combined following the same procedure) of the grain before the charging solution was pumped into the flow cell. This seed was reconstructed starting with a random guess. A guided phasing approach [53] with 100 individuals and four generations was used with a geometric average breeding mode and a low to high-resolution scheme [54]. For each generation and population, a block of 20 error reduction (ER) and 180 hybrid input-output (HIO) iterations, with $\beta = 0.9$, was repeated three times. This was followed by 20 ER iterations to return the final object. The shrinkwrap algorithm [55] with a threshold of 0.08 was used to update the real-space support every iteration. The best reconstruction was determined using a sharpness criterion, appropriate for crystals containing defects [56]. The seed reconstruction was then used as the initial guess for the reconstructions at all time points, which followed the same guided phase retrieval procedure as the seed.

## 4.5 BCDI strain calculations
The residual, or heterogeneous strain relative to the average lattice, $\varepsilon_{hkl}$, is calculated by,

$$
\varepsilon_{hkl}(\mathbf{r}) = \frac{\partial \mathbf{u}_{hkl}(\mathbf{r})}{\partial x_{hkl}} = \nabla \psi_{hkl}(\mathbf{r}) \cdot \frac{\mathbf{Q}_{hkl}}{\left| \mathbf{Q}_{hkl} \right|^2}. \tag{3}
$$

This differs from the homogeneous strain, $e_{hkl}$, associated with changes of the average lattice parameter at time $t$, $a_{0,t}$,

$$
e_{hkl} = \frac{a_{0,t} - a_{0,\text{ref.}}}{a_{0,\text{ref.}}}, \tag{4}
$$

where $a_{0,\text{ref.}}$ is the reference lattice parameter, determined at -3.4 h.

## 4.6 Hydrogen concentration
The volumetric strain, $\varepsilon_{\text{vol}}$, associated with the swelling of the grain due to hydrogen uptake can be written as [57],

$$
\varepsilon_{\text{vol}} = \sum_{A} n^{(A)} \Omega^{(A)}, \tag{5}
$$

where $n^{(A)}$ is the defect concentration for defect type $A$, and $\Omega^{(A)}$ is the relaxation volume for the specific defect type. The FCC metal lattice has two interstitial sites available for accommodating hydrogen atoms: octahedral (O) and tetrahedral (T) sites. In transition metals with FCC lattice, dissolved hydrogen atoms preferentially occupy

the O site with larger free space than the T site [38]. We used a relaxation volume of $0.200 \pm 0.005$ for interstitial hydrogen in austenitic stainless steels [37]. For our calculation, we assumed this value is similar for FCC 316 SS, and that all the interstitial hydrogen atoms reside in the O sites.

The volumetric strain relative to the initial volume at -3.4 h was calculated using the homogeneous strain, $e_{hkl}$ (Equation 4),
$$
\varepsilon_{\mathrm{vol}}=\left(1+e_{h k l}\right)^{3}-1. \tag{6}
$$

Thus, the concentration of hydrogen was determined as,
$$
n^{(A)}=\frac{\left(1+e_{h k l}\right)^{3}-1}{\Omega^{(A)}}. \tag{7}
$$

The hydrogen concentrations presented in Figure 1b are reasonable when compared to values obtained from charging hydrogen into 316L SS [58].

### 4.7 Pearson correlation coefficient
The Pearson correlation coefficient, $r$, between two images was computed using Equation 8:
$$
r(x, y)=\frac{\sum_{n}\left(x_{n}-\bar{x}\right)\left(y_{n}-\bar{y}\right)}{\sqrt{\sum_{n}\left(x_{n}-\bar{x}\right)^{2}} \sqrt{\sum_{n}\left(y_{n}-\bar{y}\right)^{2}}} \tag{8}
$$
where $x$ and $y$ were the Bragg peaks being compared, $x_n$ and $y_n$ were the values for a single voxel, and $\bar{x}$ and $\bar{y}$ were the means of each array.

### 4.8 Dislocation position identification
We define the dislocation line as the spatial positions of the locus of the phase vortices, referred to as nodes. Each dislocation is composed of many nodes, joined by edges based on the MATLAB graph object. The nodes were determined automatically by integrating the derivatives of the complex exponential of the phase $(e^{i\psi_{hkl}(\mathbf{r})})$ [59] and then selecting the maximum value as the dislocation node position if the value exceeded $0.75\pi$. The dislocation lines were found not to overlap perfectly in the reconstructions, which we attribute to noise and the limited spatial resolution. To increase overlap, the reconstructions were subpixel-shifted [60], on the order of a few pixels, or up to $\sim30$ nm. The dislocation lines terminated on the surface of the grain.

### 4.9 Dislocation dynamics modeling
#### 4.9.1 Overview
Discrete dislocation dynamics (DDD) was used to simulate the motion of the dislocation structure and compare to the experimental result. The DDD simulations here are nodal, based on discrete straight segments [61, 62] presented by *Yu et al.* [63]. Dislocation motion is calculated by evaluating the velocity $\mathbf{V}_k$ of node $k$ at position $\mathbf{X}_k$ through a mobility law (shown in the following section), which describes mobility in various modes like glide, climb, and cross-slip.

#### 4.9.2 FCC Mobility Law
The nodal force, $\mathbf{F}^k$, of node $k$ at position $\mathbf{X}^k$ is evaluated at each time increment for every node, and the dislocation structure is updated using the nodal velocity $\mathbf{V}^k$, as computed through an FCC mobility law. The nodal force, $\mathbf{F}$, has contributions from the segment-segment interaction force, obtained from the non-singular dislocation stress field, the dislocation core force, and the forces due to the corrective (image) stress field. The total nodal force can therefore be represented as

$$
\begin{aligned}
\boldsymbol{F}^{k} & =\sum_{l} \sum_{i, j} \tilde{\boldsymbol{f}}_{i j}^{k l}\left(\boldsymbol{X}^{k}\right)+\sum_{l} \boldsymbol{f}_{c}^{k l}\left(\boldsymbol{X}^{k}\right)+\sum_{l} \hat{\boldsymbol{f}}^{k l}\left(\boldsymbol{X}^{k}\right) \\
& =\tilde{\boldsymbol{F}}^{k}+\boldsymbol{F}_{c}^{k}+\hat{\boldsymbol{F}}^{k}
\end{aligned}
$$

where $\tilde{\boldsymbol{f}}_{i j}^{k l}\left(\boldsymbol{X}^{k}\right)$ is the interaction force at node $k$, due to segment $i \rightarrow j$ integrated along segment $k \rightarrow l$. This is summed over all segments $i \rightarrow j$ within the domain, including the self force due to segment $k \rightarrow l$. Finally this is then summed over all nodes $l$ which are connected to node $k$ to give the interaction force on node $k, \tilde{\boldsymbol{F}}^{k}$. The quantity $\boldsymbol{F}_{c}^{k}$ is the dislocation core force and $\hat{\boldsymbol{F}}^{k}$ is the corrective elastic force evaluated with the finite element method using the superposition principle to account for the finite boundary.

For each segment $k l$ with $L^{k l}$, a drag tensor $\boldsymbol{B}^{k l}$ is determined according to the segment character. The nodal velocity $\boldsymbol{V}^{k}$ at node $k$ is then calculated as

$$
\left[\frac{1}{2} \sum_{l} L^{k l} \boldsymbol{B}^{k l}\right]^{-1} \boldsymbol{F}^{k}=\boldsymbol{V}^{k},
$$

where the sum is over all nodes $l$ connected to node $k$, and $\boldsymbol{F}^{k}$ is the nodal force determined by Equation 10.

All dislocation segments are constrained to the $\{111\}$ slip planes in FCC, and their respective drag tensor can be expressed as [64]

$$
\boldsymbol{B}^{k l}\left(\boldsymbol{l}^{k l}\right)=B_{g}\left(\boldsymbol{m}^{k l} \otimes \boldsymbol{m}^{k l}\right)+B_{c}\left(\boldsymbol{n}^{k l} \otimes \boldsymbol{n}^{k l}\right)+B_{l}\left(\boldsymbol{l}^{k l} \otimes \boldsymbol{l}^{k l}\right)
$$

where $B_{g}, B_{c}$, and $B_{l}$ are the drag coefficients for glide, climb, and motion along the line direction, respectively. The unit vectors are the line direction $\boldsymbol{l}^{k l}$, the slip plane normal $\boldsymbol{n}^{k l}$, and glide direction $\boldsymbol{m}^{k l}$.

### 4.9.3 Incorporating finite boundary conditions
To evaluate the corrective force term $\hat{\boldsymbol{F}}^{k}$ in Equation 10, the superposition principle is adopted. As described elsewhere [65, 66], the total stress strain and displacement fields are expressed as

$$
\boldsymbol{\sigma}=\hat{\boldsymbol{\sigma}}+\tilde{\boldsymbol{\sigma}}
$$

$$
\boldsymbol{\varepsilon}=\hat{\boldsymbol{\varepsilon}}+\tilde{\boldsymbol{\varepsilon}}
$$

$$
\boldsymbol{u}=\hat{\boldsymbol{u}}+\tilde{\boldsymbol{u}},
$$

respectively. The infinite-body fields are denoted as $(\tilde{)}$ and the finite-element correction fields as $(\hat{)}$. According to the following procedure [67], the image stress field may be evaluated. First, the elastic stress field due to dislocations in an infinite body, $\tilde{\boldsymbol{\sigma}}$, is obtained. The tractions $\tilde{\boldsymbol{T}}=\tilde{\boldsymbol{\sigma}} \cdot n$ on the traction boundaries due to this stress are then calculated, and subtracted from the desired boundary conditions $\boldsymbol{T}$. These modified boundary values, $\hat{\boldsymbol{T}}=\boldsymbol{T}-\tilde{\boldsymbol{T}}$, in addition to the displacement conditions $\boldsymbol{U}$ on the displacement boundaries are used in an elastic finite element simulation to determine the corrective fields. Finally, the corrective stress field, $\hat{\boldsymbol{\sigma}}$, is used to evaluate the corrective nodal force, $\hat{\boldsymbol{f}}$.

### 4.9.4 Calculation Details
The initial dislocation structure used in the simulation is identical to the initial dislocation structure measured by experiment before the start of hydrogen charging. The following parameters were used to represent $\gamma$-Fe: the lattice parameter, $a_{0}=3.602$ Å, the shear modulus, $G=77$ GPa, Poisson's ratio, $v=0.28$, The dislocation structure was enclosed within a $0.6 \mu \mathrm{m} \times 0.6 \mu \mathrm{m} \times 0.6 \mu \mathrm{m}$ domain representing the experimentally observed grain. The finite element (FE) mesh was $20 \times 20 \times 20$. The drag coefficients for edge and screw dislocations were

both 1.0, essentially making the mobility of each type of dislocation equivalent. In contrast, the drag coefficient for dislocation segments attempting to move in the climb direction was $10^8$, essentially confining the segments to the glide plane. The two end points were fixed for the entire simulation, while the internal nodes were free in all directions (though as discussed, they were restricted in the climb direction). No external mechanical load was applied to the domain.

### 4.10 Dislocation strain field modeling

The $\varepsilon_{111,\text{model}}$ for the large dislocation was created using the dislocation node positions determined from BCDI, the Burgers vector (using the local lattice parameter, $a_{0,t}$), and $v = 0.28$. Each dislocation node was joined by an edge, which was then connected to another point to form a dislocation triangle. The displacement field for this triangular dislocation loop was determined using the solution developed by Barnett [68, 69], which was then numerically differentiated to determine the lattice strain field, $\varepsilon_{\text{model}}$,

$$
\varepsilon_{\text{model}} = \begin{bmatrix}
\varepsilon_{xx,\text{model}} & \varepsilon_{xy,\text{model}} & \varepsilon_{xz,\text{model}} \\
\varepsilon_{yx,\text{model}} & \varepsilon_{yy,\text{model}} & \varepsilon_{yz,\text{model}} \\
\varepsilon_{zx,\text{model}} & \varepsilon_{zy,\text{model}} & \varepsilon_{zz,\text{model}}
\end{bmatrix}. \tag{16}
$$

$\varepsilon_{\text{model}}$ was projected to the [111] direction,

$$
\varepsilon_{111,\text{model}} = \begin{bmatrix}
a & b & c
\end{bmatrix}
\begin{bmatrix}
\varepsilon_{xx,\text{model}} & \varepsilon_{xy,\text{model}} & \varepsilon_{xz,\text{model}} \\
\varepsilon_{yx,\text{model}} & \varepsilon_{yy,\text{model}} & \varepsilon_{yz,\text{model}} \\
\varepsilon_{zx,\text{model}} & \varepsilon_{zy,\text{model}} & \varepsilon_{zz,\text{model}}
\end{bmatrix}
\begin{bmatrix}
a \\
b \\
c
\end{bmatrix}, \tag{17}
$$

where $a$, $b$, $c$, transformed the Cartesian coordinate system for the theoretical edge dislocation, to the experimental sample space. These were determined by,

$$
\begin{bmatrix}
a \\
b \\
c
\end{bmatrix} = \begin{bmatrix}
\mathbf{x}' & \mathbf{y}' & \mathbf{z}'
\end{bmatrix}^{-1} \left[ \hat{\mathbf{Q}}_{\text{hkl, sam}} \right], \tag{18}
$$

where $\hat{\mathbf{x}}'$ is $\hat{\mathbf{b}}_{\text{sam}}$, $\hat{\mathbf{y}}'$, is the dislocation loop plane normal vector (normalised) at -3.4 h, and $\hat{\mathbf{z}}' = \hat{\mathbf{x}}' \times \hat{\mathbf{y}}'$. All vectors in Equation 18 are column vectors. The subscript, $\text{sam}$, corresponds to the the sample coordinates relative to the standard unit vectors $\hat{\mathbf{x}}$, $\hat{\mathbf{y}}$, and $\hat{\mathbf{z}}$ axes of a 3D Cartesian coordinate system.

### Acknowledgements

F.H. thanks Thomas D. Swinburne and Max Boleininger for insightful comments. D.Y., G.H., and F.H. acknowledge funding from the European Research Council under the European Union's Horizon 2020 research and innovation programme (grant agreement No 714697). K.S. acknowledges funding from the General Sir John Monash Foundation. A.M. acknowledges funding from EDF (Électricité de France). Work at Brookhaven National Laboratory was supported by the U.S. Department of Energy, Office of Science, Office of Basic Energy Sciences, under Contract No. DESC0012704. Work performed at UCL was supported by EPSRC. The authors acknowledge the use of the Advanced Research Computing (ARC) facility at the University of Oxford [70]. Experiments were performed at the Advanced Photon Source, a US Department of Energy (DOE) Office of Science User Facility operated for the DOE Office of Science by Argonne National Laboratory under Contract No. DE-AC02-06CH11357.

### Conflict of Interest

There are no competing interests to declare.

### Author Contributions

Conceptualisation: D.Y., F.H.; Data Curation: D.Y., M.S.; Formal Analysis: D.Y., M.S., E.T., I.K.R., F.H.; Funding Acquisition: E.T., I.K.R., F.H.; Investigation: D.Y., G.H., K.S., R.J.H, W.C.; Methodology: D.Y., B.D., K.S., R.J.H, W.C.; Project Administration: F.H.; Resources: D.Y., G.H., K.S., A.M, F.H.; Software: D.Y., M.S.,

E.T., F.H.; Supervision: E.T., I.K.R., F.H.; Validation: D.Y., M.S.; Visualisation: D.Y., M.S.; Writing – Original Draft Preparation: D.Y., M.S., F.H.; Writing – Review & Editing: All authors.

### Data Availability Statement
The diffraction patterns, reconstructions, and data analysis scripts for producing the figures will be publicly available at Zenodo: http://doi.org/10.5281/zenodo.14503567 after publication.

## References

[1] F. Dawood, M. Anda, G. M. Shafiullah, *International Journal of Hydrogen Energy* **2020**, 45 3847.

[2] S. Tiwari, M. J. Pekris, J. J. Doherty, *International Journal of Hydrogen Energy* **2024**, 57 1174.

[3] A. M. Oliveira, R. R. Beswick, Y. Yan, *Current Opinion in Chemical Engineering* **2021**, 33 100701.

[4] S. Griffiths, B. K. Sovacool, J. Kim, M. Bazilian, J. M. Uratani, *Energy Research & Social Science* **2021**, 80 102208.

[5] I. E. Agency, Global hydrogen review 2024, **2024**.

[6] W. H. Johnson, *Nature* **1875**, 11 393.

[7] C. D. Beachem, *Metallurgical Transactions* **1972**, 3 441.

[8] D. S. Shih, I. M. Robertson, H. K. Birnbaum, *Acta Metallurgica* **1988**, 36 111.

[9] R. A. Oriani, P. H. Josephic, *Acta Metallurgica* **1974**, 22 1065.

[10] S. P. Lynch, *Acta Metallurgica* **1988**, 36 2639.

[11] M. L. Martin, M. Dadfarnia, A. Nagao, S. Wang, P. Sofronis, *Acta Materialia* **2019**, 165 734.

[12] Y.-S. Chen, C. Huang, P.-Y. Liu, H.-W. Yen, R. Niu, P. Burr, K. L. Moore, E. Martínez-Pañeda, A. Atrens, J. M. Cairney, *International Journal of Hydrogen Energy* **2024**.

[13] L. Dong, S. Wang, G. Wu, J. Gao, X. Zhou, H.-H. Wu, X. Mao, *International Journal of Hydrogen Energy* **2022**, 47 20288.

[14] I. M. Robertson, P. Sofronis, A. Nagao, M. L. Martin, S. Wang, D. W. Gross, K. E. Nygren, *Metallurgical and Materials Transactions B* **2015**, 46 1085.

[15] Y.-S. Chen, H. Lu, J. Liang, A. Rosenthal, H. Liu, G. Sneddon, I. McCarroll, Z. Zhao, W. Li, A. Guo, J. M. Cairney, *Science* **2020**, 367 171.

[16] H. K. Birnbaum, P. Sofronis, *Materials Science and Engineering A* **1994**, 176 191.

[17] L. B. Pfeil, *Proceedings of The Royal Society A: Mathematical, Physical and Engineering Sciences* **1926**, 112 182.

[18] M. B. Djukic, G. M. Bakic, V. S. Zeravcic, A. Sedmak, B. Rajicic, *Engineering Fracture Mechanics* **2019**, 216 106528.

[19] M. Koyama, C. C. Tasan, E. Akiyama, K. Tsuzaki, D. Raabe, *Acta Materialia* **2014**, 70 174.

[20] S. Lynch, *Corrosion Reviews* **2012**, 30 105.

[21] M. Nagumo, *Materials Science and Technology* **2004**, 20 940.

[22] M. Koyama, M. Taheri-Mousavi, H. Yan, J. Kim, B. C. Cameron, S. Moeini-Ardakani, J. Li, C. C. Tasan, *Science Advances* **2020**, 6.

[23] L. Huang, D. Chen, D. Xie, S. Li, Y. Zhang, T. Zhu, D. Raabe, E. Ma, J. Li, Z. Shan, *Nature Materials* **2023**, 22 710.

[24] I. M. Robertson, *Engineering Fracture Mechanics* **2001**, 68 671.

[25] I. M. Robertson, T. Tabata, W. Wei, F. Heubaum, H. K. Birnbaum, *Scripta Metallurgica* **1984**, *18* 841.

[26] S. Wang, M. L. Martin, P. Sofronis, S. Ohnuki, N. Hashimoto, I. M. Robertson, *Acta Materialia* **2014**, 69 275.

[27] P. J. Ferreira, I. M. Robertson, H. K. Birnbaum, *Acta Materialia* **1998**, 46 1749.

[28] M. A. Pfeifer, G. J. Williams, I. A. Vartanyants, R. Harder, I. K. Robinson, *Nature* **2006**, 442 63.

[29] J. N. Clark, J. Ihli, A. S. Schenk, Y. Y. Kim, A. N. Kulak, J. M. Campbell, G. Nisbet, F. C. Meldrum, I. K. Robinson, *Nature Materials* **2015**, *14* 780.

[30] K. W. Orr, J. Diao, M. N. Lintangpradipto, D. J. Batey, A. N. Iqbal, S. Kahmann, K. Frohna, M. Dubajic, S. J. Zelewski, A. E. Dearle, T. A. Selby, P. Li, T. A. Doherty, S. Hofmann, O. M. Bakr, I. K. Robinson, S. D. Stranks, *Advanced Materials* **2023**, 35 2305549.

[31] A. Singer, M. Zhang, S. Hy, D. Cela, C. Fang, T. A. Wynn, B. Qiu, Y. Xia, Z. Liu, A. Ulvestad, N. Hua, J. Wingert, H. Liu, M. Sprung, A. V. Zozulya, E. Maxey, R. Harder, Y. S. Meng, O. G. Shpyrko, *Nature Energy* **2018**, 3 641.

[32] A. Yau, R. J. Harder, M. W. Kanan, A. Ulvestad, *ACS Nano* **2017**, *11* 10945.

[33] C. Atlan, C. Chatelier, I. Martens, M. Dupraz, A. Viola, N. Li, L. Gao, S. J. Leake, T. U. Schülli, J. Eymery, F. Maillard, M. I. Richard, *Nature Materials* **2023**, 1–8.

[34] F. Hofmann, N. W. Phillips, S. Das, P. Karamched, G. M. Hughes, J. O. Douglas, W. Cha, W. Liu, *Physical Review Materials* **2020**, 4 013801.

[35] J. R. Fienup, *Applied Optics* **1982**, *21* 2758.

[36] A. P. Zhilyaev, T. G. Langdon, *Progress in Materials Science* **2008**, 53 893.

[37] D. G. Ulmer, C. J. Altstetter, *Acta Metallurgica et Materialia* **1993**, *41* 2235.

[38] Y. Fukai, *The Metal-Hydrogen System: Basic Bulk Properties*, Springer-Verlag, second, revised a... edition, **2005**.

[39] R. Kirchheim, *Acta Materialia* **2007**, 55 5129.

[40] P. M. Anderson, J. P. Hirth, J. Lothe, *Theory of Dislocations*, Cambridge University Press, 3 edition, **2017**.

[41] A. Abu-Odeh, M. Cottura, M. Asta, *Acta Materialia* **2020**, 193 172.

[42] M. Nagumo, *ISIJ International* **2001**, *41* 590.

[43] Y. Fukai, *Journal of Alloys and Compounds* **2003**, 356-357 263.

[44] H. Sugimoto, Y. Fukai, *Acta Materialia* **2014**, 67 418.

[45] J.-P. Du, W. T. Geng, K. Arakawa, J. Li, S. Ogata, *The Journal of Physical Chemistry Letters* **2020**, *11* 7015, doi: 10.1021/acs.jpclett.0c01798.

[46] P. Sofronis, H. K. Birnbaum, *Journal of the Mechanics and Physics of Solids* **1995**, 43 49.

[47] P. Kumar, P. Garg, K. N. Solanki, I. Adlakha, *International Journal of Hydrogen Energy* **2021**, 46 25726.

[48] H. Yu, I. H. Katzarov, A. T. Paxton, A. C. Cocks, E. Tarleton, *Physical Review Materials* **2020**, 4.

[49] D. Sayre, *Acta Crystallographica* **1952**, 5 843.

[50] O. Y. Gorobtsov, H. Hirsh, M. Zhang, D. Sheyfer, L. H. B. Nguyen, S. D. Matson, D. Weinstock, R. Bouck, Z. Wang, W. Cha, J. Maser, R. Harder, Y. S. Meng, A. Singer, *Advanced Energy Materials* **2023**.

[51] I. Robinson, R. Harder, *Nature Materials* **2009**, 8 291.

[52] A. G. Shabalin, M. Zhang, W. Yao, R. Rysov, Z. Ren, D. Lapkin, Y.-Y. Kim, D. Assalauova, N. Mukharamova, M. Sprung, I. A. Vartanyants, Y. S. Meng, O. G. Shpyrko, *Journal of Synchrotron Radiation* **2023**, 30 445.

[53] C. C. Chen, J. Miao, C. W. Wang, T. K. Lee, *Physical Review B - Condensed Matter and Materials Physics* **2007**, 76 064113.

[54] B. C. McCallum, R. H. Bates, *Journal of Modern Optics* **1989**, 36 619.

[55] S. Marchesini, H. He, N. Chapman, P. Hau-Riege, A. Noy, R. Howells, U. Weierstall, H. Spence, *Physical Review B - Condensed Matter and Materials Physics* **2003**, 68 140101(R).

[56] A. Ulvestad, Y. Nashed, G. Beutier, M. Verdier, S. O. Hruszkewycz, M. Dupraz, *Scientific Reports* **2017**, 7 9920.

[57] F. Hofmann, D. Nguyen-Manh, M. R. Gilbert, C. E. Beck, J. K. Eliason, A. A. Maznev, W. Liu, D. E. Armstrong, K. A. Nelson, S. L. Dudarev, *Acta Materialia* **2015**, 89 352.

[58] A. M. Brass, J. Chêne, *Corrosion Science* **2006**, 48 3222.

[59] D. Yang, M. T. Lapington, G. He, K. Song, M. Zhang, C. Barker, R. J. Harder, W. Cha, W. Liu, N. W. Phillips, F. Hofmann, *Journal of Applied Crystallography* **2022**, 55 1184.

[60] M. Guizar-Sicairos, S. T. Thurman, J. R. Fienup, *Optics Letters* **2008**, 33 156.

[61] A. Arsenlis, W. Cai, M. Tang, M. Rhee, T. Oppelstrup, G. Hommes, T. G. Pierce, V. V. Bulatov, *Modelling Simul. Mater. Sci. Eng.* **2007**, 15, 6 553.

[62] W. Cai, V. Bulatov, *Materials Science and Engineering: A* **2004**, 387–389 277.

[63] H. Yu, A. Cocks, E. Tarleton, *Journal of the Mechanics and Physics of Solids* **2019**, 123 41.

[64] V. Bulatov, W. Cai, *Computer Simulations of Dislocations*, OUP Oxford, **2006**.

[65] E. V. der Giessen, A. Needleman, *Modelling Simul. Mater. Sci. Eng.* **1995**, 3, 5 689.

[66] D. Weygand, L. H. Friedman, E. V. der Giessen, A. Needleman, *Modelling Simul. Mater. Sci. Eng.* **2002**, 10, 4 437.

[67] J. A. El-Awady, S. Bulent Biner, N. M. Ghoniem, *Journal of the Mechanics and Physics of Solids* **2008**, 56, 5 2019.

[68] D. M. Barnett, *Philosophical Magazine A* **1985**, 51 383, doi: 10.1080/01418618508237562.

[69] D. M. Barnett, R. W. Balluffi, *Philosophical Magazine Letters* **2007**, 87 943, doi: 10.1080/09500830701601748.

[70] A. Richards, University of oxford advanced research computing, **2015**, URL https://zenodo.org/record/22558.