Accepted Manuscript

The glass transition temperature of PMMA: A molecular dynamics study and comparison of various determination methods

Maryam Mohammadi, Hossein fazli, Mehdi karevan, Jamal Davoodi

<table>
<tr><td>PII:</td><td>S0014-3057(16)31237-X</td></tr>
<tr><td>DOI:</td><td>http://dx.doi.org/10.1016/j.eurpolymj.2017.03.056</td></tr>
<tr><td>Reference:</td><td>EPJ 7805</td></tr>
<tr><td>To appear in:</td><td>European Polymer Journal</td></tr>
<tr><td>Received Date:</td><td>13 October 2016</td></tr>
<tr><td>Revised Date:</td><td>9 March 2017</td></tr>
<tr><td>Accepted Date:</td><td>12 March 2017</td></tr>
</table>

![](./images/811042179291021313_1.jpg)

Please cite this article as: Mohammadi, M., fazli, H., karevan, M., Davoodi, J., The glass transition temperature of PMMA: A molecular dynamics study and comparison of various determination methods, European Polymer Journal (2017), doi: http://dx.doi.org/10.1016/j.eurpolymj.2017.03.056

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# The glass transition temperature of PMMA: A molecular dynamics study and comparison of various determination methods

Maryam Mohammadi$^{\text{a}}$, Hossein fazli$^{\text{b}}$, Mehdi karevan$^{\text{c}}$, Jamal Davoodi$^{\text{a}*}$

$^{\text{a}}$Department of Physics, University of Zanjan, Zanjan 45195-313, Iran

$^{\text{b}}$ Institute for Advanced Studies in Basic Sciences (IASBS), P. O. Box 45195-1159, Zanjan 45195, Iran

$^{\text{c}}$Department of Mechanical Engineering, Isfahan University of Technology, 84156-83111, Iran

*Corresponding Author.
E-mail address: jdavoodi@znu.ac.ir

## Abstract
The glass transition temperature ($\text{T}_\text{g}$) governs the mechanical and physical performances of polymeric materials and thus their ultimate applications. Although an extensive body of research has focused on the study and determination of the $\text{T}_\text{g}$, thermal events at and around the $\text{T}_\text{g}$ at the molecular level have not yet been fully understood. It is widely believed that, at and around the $\text{T}_\text{g}$, the intermolecular interactions and the structure of polymer change resulting in dramatic variations of the bulk properties of polymers. Therefore, the $\text{T}_\text{g}$ could be determined by tracing the changes observed in macroscopic (bulk) and microscopic properties as a polymer system cools down. In this study, we attempted to estimate the $\text{T}_\text{g}$ of isotactic Polymethylmethacrylate (is-PMMA) employing the molecular dynamics simulations based on the united atom model. To achieve this, the polymer properties including the thermal conductivity, volume, density, thermal expansion and Young's module were examined. Moreover, microscopic properties such as the

radial distribution function (RDF) and motions of the polymer chains by the mean squared displacement (MSD) function and the non-bonded energy were assessed. It was shown that a unique break appears on the property-temperature curves around 440 K irrespective of the MD simulation method. The $T_g$ values obtained in this work were quite consistent with the experimental results reported in the literature. The study also indicated that the $T_g$ increases with increasing the cooling rate and molecular weight of the polymer.

![](./images/811042179291021313_2.jpg)

### Highlights:
- Eight MD measurements were employed to determine glass transition and were compared with each other.
- Thermal conductivity was calculated using the equilibrium MD simulation according to the Green-Kubo approach.
- Non-bond carbon atom investigate to obtain glass transition temperature through cooling the system.

Keywords: glass transition temperature, polymer chains, molecular dynamics simulation, interaction.

## 1 Introduction

The glass transition temperature, $T_g$, which is considered to be one of the specific properties of polymers, is a temperature observed both in the amorphous and semi-crystalline polymers. It has been broadly shown that the $T_g$ is an important determinant in the application of polymer based products [1-3]. The value of $T_g$ has been well-known to dictate the elastic and viscoelastic response of polymers at a given temperature. Such a correlation between the $T_g$ and viscoelastic behavior of products has made the determination the $T_g$ a key requirement for the optimized processing foods [4], drugs [5] and industrial polymeric products [6]. A growing body of efforts has been consequently directed toward determining the $T_g$ employing a variety of methods. For instance, the $T_g$ and its associated properties have been extensively investigated using theoretical and computational studies. Various techniques have been utilized in order to measure the $T_g$ through experimental observations. For example, thermodilatometry [7], ellipsometry [8], differential scanning calorimetry (DSC) [9, 10], dynamic mechanical analysis (DMA) [11, 12], X-ray diffraction (XRD) [13], fourier transform infrared (FTIR) [14], fourier transform raman (FT-Raman) [15], fluorescence intensity [16], dielectric measurement [17] and positron annihilation lifetime spectroscopy (PALS) [18] can be listed as tools for evaluating the $T_g$, among which, the DSC and DMA are exploited more frequently.

The understanding of the thermal events around the $T_g$ has been appeared to be a continuing issue. In fact a polymeric system can reach an equilibrium state at temperatures above $T_g$, while it is at a frozen non-equilibrium glassy state below the Tg.

Numerous theoretical and modeling techniques have been suggested and developed to describe the glass transition phenomenon [19]. For example, the Fictive temperature concept [20], the

Vol'kenshtein-Ptitsyn relaxation theory [21], the free-volume models [22], the Tool-Narayanaswamy-Moynihan method [23], the Kovacs method [24], the Adam-Gibbs theory [25], the configurational entropy approach to $T_g$ [26] and nonequilibrium thermodynamics [27] have been introduced and developed to study the changes in the physical and structural properties of polymers observed around the $T_g$. Among the current microscopic approaches, the energy landscape model [28, 29], the mode-coupling theory [30] and the Random First-Order Transition (RFOT) theory [31, 32] can be mentioned. More recently, the mean field investigation have been carried out to study the scaling and universality at the $T_g$ [33].

Despite the interest in the evaluation of the $T_g$ using generalizable and well-grounded methods, no perfect theory, as far as we know, has been developed as an explanation to the glass transition phenomenon. This limitation has led to the lack of useful tools to fully understand the $T_g$ and events appearing around this temperature. Therefore, numerous computational studies through molecular dynamics (MD) [34-36] and Monte Carlo [37-39] methods have been employed to obtain a better insight into the $T_g$ of polymers. Specially, the use of the molecular dynamics simulations has been proven to assist in understanding the relationships existing between the bulk properties of polymers and intermolecular forces exiting among the polymer chains.

As considerable attention has been paid to polymethylmethacrylate (PMMA) due to its promising behavior among the commodity polymers and its widespread applications [40, 41]. Soldera et al. investigated the $T_g$ of PMMA in several studies using the MD simulations. They evaluated the energy of the structural analysis in different tacticity of PMMA chains [42, 43], different force fields [44], cooperativity in different tacticity of PMMAs [45] and the local chain dynamics [46]. Subramanian et al. evaluated the chain flexibility of the polypropylene and PMMA using the Monte Carlo simulations [47]. Berrahou et al. determined the $T_g$ and elastic

properties of amorphous polymers such as PMMA, polymethacrylamide (PMAAM) and PMMA co PMAAM copolymers using MD simulations [48].

Although MD simulations of polymers aiming at characterizing the $T_g$ have already been reported, to the best of our knowledge, no comparative study using different MD measurements to specify the $T_g$ of PMMA exists. Thus, the goal of this work is to define the $T_g$ of PMMA using various methods through MD simulations. It is widely accepted that the macro-scale physical properties of polymers such as the volume, density, thermal conductivity, elastic and intermolecular properties are expected to exhibit an abrupt change near the $T_g$ [1-3]. The hypothesis, consequently, is that the $T_g$ could be specified by tracing the changes in characteristics mentioned above. In addition, one objective of this study is to illustrate the links between the intermolecular and bulk properties of PMMA observed at and around the $T_g$. Our findings reveal that the estimated $T_g$ employing different simulation measurements are consistent with the experimental values reported in the literature.

## 2 The model and the simulation method

All our simulations were performed using MD simulation package, LAMMPS (large-scale atomic/molecular massively parallel simulator), developed at the Sandia National Laboratories [49]. The system consisted of three linear isotactic PMMA (is-PMMA) chains. Each polymer chain was considered to be built up by 100 monomers (the structure proposed by Shaffer et al. [50]). The PMMA conformations were generated in the Fortran 90 using a random and self-avoiding walk algorithm and then imported into LAMMPS as data input. The obtained monomer and chain structure of PMMA are shown in Figure 1. To perform the simulation, a three-dimensional periodic boundary condition was applied. A united atom model, where the hydrogen

atoms of $CH$, $CH_2$ and $CH_3$ compounds are contained into the connecting carbon atoms and grouping each carbon with its bonded hydrogen atoms, was used to reduce the computation time.

For modeling the atomic interactions, an interatomic force field proposed by Okada et al. was used [51]. Some modifications have been made to the equations of the force field to make them useable in the LAMMPS. In this work, the interaction potential ( U ) is defined as the sum of the bonding and nonbonding interactions and is expressed as the following expression:

![](./images/811042179291021313_3.jpg)

Figure 1. (a) A single monomer of PMMA (all atom), (b) the monomer of PMMA (united atom) and (c) 10-monomer chain of is-PMMA

$$
\begin{aligned}
\mathrm{U}=& \sum_{\text {bonds }} \mathrm{k}_{\mathrm{r}}\left(\mathrm{r}-\mathrm{r}_{0}\right)^{2}+\sum_{\text {angles }} \mathrm{k}_{\theta}\left(\theta-\theta_{0}\right)^{2}+\sum_{\text {torsions }} \sum_{\mathrm{i}=1}\left(\mathrm{~V}_{\mathrm{n}} \cos \mathrm{n} \phi\right) \\
&+\sum_{\substack{\text {improper } \\
\text {torsions }}}\left(\mathrm{K}_{1}\left(\Theta-\Theta_{0}\right)+\mathrm{K}_{2}\left(\Theta-\Theta_{0}\right)^{2}\right)+\sum \frac{\mathrm{A}}{\mathrm{r}^{12}}-\frac{\mathrm{C}}{\mathrm{r}^{6}}
\end{aligned} \tag{1}
$$

in which the first term illustrates the bond stretching energy, r is the bond length and $r_0$ is the equilibrium length of the bond. The second term corresponds to the angular bending energy, $\theta$

is bending angle and $\theta_0$ is the equilibrium angle of the bond. The third and fourth terms represent the dihedral torsion and the improper torsion energy, respectively. The $\phi$ is the dihedral torsion angle and $\Theta$ is the sum of three neighboring bending angles, $\Theta_0$ is the equilibrium sum of three neighboring bending angles. The last term is the Lennard-Jones energy between two non-bonded atoms/molecules.

### 2.1 The energy evaluation of the equilibrium process

The three polymer chains were first built in the simulation box (a cube of 40 Å side length) at the temperature of T=600K. The periodic box dimensions were chosen to allow the polymer density to be less than the equilibrium bulk density. To minimize the total potential energy of the initial system, the conjugate gradient method was applied. This was followed by allowing the polymer chains to equilibrate for 50 ps in order to prevent improper overlaps of the particles to be washed out from the system. Following this energy minimization, the thermal annealing was carried out to remove undesirable interactions and to obtain the lowest energy state. The thermal annealing process was implemented in four NVT simulation stages with the duration of 400 ps. The temperature was decreased from 600 K to 300 K and then back to 600 K, in a similar fashion. The same method was used for raising the temperature from 600 K to 800 K. The stages were followed by satisfying the system equilibrium in 5ns at 600K and zero pressure using the NPT simulation. The NVT simulation for 0.5ns followed by NPT ensembles was used to allow the system to attain the equilibrium state and to prevent the simulated systems from entrapping in a metastable state of the local minima.

When the simulation was run at 600 K by the NPT ensemble, the relaxation of the auto-correlation function (ACF) of the end-to-end vector of PMMA chain was observed as a function

of time due to the macromolecular nature of the system. The ACF is mathematically defined based on the first Legendre polynomial as follows [52]:

$$\mathrm{ACF}=\langle\overrightarrow{\mathrm{u}}(0). \overrightarrow{\mathrm{u}}(\mathrm{t})\rangle \tag{2}$$

where $\overrightarrow{\mathrm{u}}$ denotes the unit vector of the end-to-end separation of the PMMA chain and t is the elapsed time. The ACF shows the time required by the polymer chain to lose memory by a gradual drop from 1 to 0. It is believed that decorrelation of the end-to-end vector is a measure of time required for the system to achieve the equilibrium state.

The time variations of energy and ACF for the end-to-end distance of PMMA chain versus time during the NPT equilibration at 600K are represented in Figure 2. Monitoring the kinetic and potential energies and ACF variations confirmed that a 5ns is sufficient for the system to achieve its minimum energy state. Accordingly, the 5ns time interval was selected for the rest of the simulation studies. The system was then cooled from 600 K to 300 K at a rate of 10K/5ns. The energy of the PMMA during the process of the MD simulation is illustrated in Figure 3.

![](./images/811042179291021313_4.jpg)

Figure 2. (a) The energy/chain during NPT equilibration at 600K and (b) the ACF variations of PMMA chain end-to-end distance vector against production time.

![](./images/811042179291021313_5.jpg)

Figure 3. (a) The energy/chain of the PMMA during the process of MD simulation at a cooling rate of 2K/ns and (b) the potential energy/chain of PMMA at different temperatures during the cooling in each stage.

## 3 Results and discussion

### 3.1 Determination of the $\mathbf{T_g}$ through microscopic properties

#### 3.1.1 The structural property: the radial distribution functions

The radial distribution function (RDF) is a measure of probability to find a given pair of atoms at distance r from each other and is defined as:

$$
g_{AB}(r)=\frac{1}{\rho_{AB} 4 \pi r^{2}} \frac{\sum_{t=1}^{K} \sum_{j=1}^{N_{AB}} \Delta N_{AB}(r \rightarrow r+\delta r)}{N_{AB} \times K} \tag{3}
$$

where $N_{AB}$ is the number of atoms in the system containing A and B atoms, $\Delta N_{AB}$ is the number of neighbor atoms between r and $r+\delta r$ around an atom, $\delta r$ is the distance interval, K is the number of time steps, and $\rho_{AB}$ is the bulk density. It is noteworthy to mention that A and B could be the same type of atoms [53].

The RDF calculated for all atoms, oxygen-oxygen, carbon-oxygen and carbon-carbon of PMMA are shown in Figure 4. As clearly shown, in the range of $\mathrm{r}<6 \mathring{A}$, several peaks are well distinguished. These peaks determine the structure of the PMMA. The first three peaks around 1.21, 1.35, $1.45 \mathring{A}$ are associated with the bond length between the O and C in C=O bonds and two other C-O bonds. The subsequent peak forming around $1.54 \mathring{A}$ is attributed to the distance between the carbon atoms in C-C bonds. The next peaks indicate the separation between neighboring bonded atoms such as the carbon atoms in C-C-C sequences ($2.44 \mathring{A}$). The peaks following this peak appearing around 3.4, 3.7, 4 and $4.7 \mathring{A}$ display the distance between non-bonded carbon atoms. For values of r greater than $6 \mathring{A}$, no sharp peak is detected and the RDF reaches smoothly to 1. As expected, this clearly exhibits the amorphous nature of PMMA [54].

![](./images/811042179291021313_6.jpg)

Figure 4. (a) The RDF for various pairs of atoms for oxygen atoms, carbon atoms, carbon and oxygen atoms and all atoms and (b) the RDF for all atoms in two temperatures.

The RDF is an effective tool to examine the structural properties of the polymer systems providing a proven approach for the understanding of the atom interactions including the bonding or non-bonding ones [51]. Through this simulation, the intensities of peaks corresponding to the bonded atoms do not noticeably change with temperature over the studied range. The peaks correlated to the non-bonded carbon atoms, in contrast, were found to depend on temperature. We, therefore, considered the RDF calculation for non-bonded carbon atoms as displayed in Figure 5 (left) and the inserted image over an appropriate zone showing distinguishable changes in the peaks (right). It is clearly shown that, g(r=4 Å) is greater at low temperatures as compared to high temperatures. This effect seem to be caused by the changes in the density of polymer system at the $T_g$. As is shown in Figure 6, the slope of lines fitted to g(r) values is sharply altered around 459 K. This temperature is expected to be the $T_g$ of the PMMA.

To find the best fit curve, the piecewise linear function with the "orthogonal distance regression" algorithms in the iterative procedure, has been used [55, 56].

![](./images/811042179291021313_7.jpg)

Figure 5. (a) The radial distribution function at different temperatures for non-bonded carbon atoms and (b) a zoomed-in image over (right)

![](./images/811042179291021313_8.jpg)

Figure 6. g(r=4 Å) against temperature for non-bonded carbon atoms.

### 3.1.2 The mean squared displacement and self-diffusion coefficient

In the statistical mechanics, the mean squared displacement (MSD) is a measure of the deviation over time between the position of a particle and its initial position. It is one of the most common tools for the evaluation of the random mobility of the atoms in a system .The MSD is defined as:

$$
\mathrm{MSD}=\frac{1}{\mathrm{~N}} \sum_{\mathrm{i}=1}^{\mathrm{N}-1}\left|\overrightarrow{\mathrm{R}}_{\mathrm{i}}(\mathrm{t})-\overrightarrow{\mathrm{R}}_{\mathrm{i}}(0)\right|^{2} \tag{4}
$$

In this equation, $\overrightarrow{\mathrm{R}}_{\mathrm{i}}(\mathrm{t})$ denotes the current position of the $\mathrm{i}_{\text {th }}$ atom (at time $\mathrm{t}$ ) and $\mathrm{N}$ is the total number of the atoms of a given type [57]. Analyzing MSD in the PMMA system at various temperatures during the cooling process has been shown to be very useful and informative [58]. In this work, the MSD curves at various temperatures were generated in order to characterize the thermal motion as the temperature changes and goes through the $\mathrm{T}_{\mathrm{g}}$. Figure 7 verifies that the MSD curves more or less remain constant with variation in temperature below 470 K. The values of MSD gradually increased with the lapse of time. However, the MSD values notably increased with temperatures raised above 470 K. The difference observed in the trend of the MSD results in temperatures below 470 K could be attributed to the lower mobility of the polymer chains, so far called immobilization of polymer chains occurring at temperatures below the $\mathrm{T}_{\mathrm{g}}$. According to the Figure 7a, a significant change in the MSD values is noticed when the temperature decreases from 470 to 460 K, which is an indication of the system transition to the glassy state. Figure 7b represents the replotted MSD values as a function of temperature at 2.5 ns. The results clearly depict a noticeable change in the MSD values determined below and above the $\mathrm{T}_{\mathrm{g}}$.

![](./images/811042179291021313_9.jpg)

Figure 7. (a) MSD curves against variation time and temperature and (b) MSD values at 2.5 ns in different temperatures.

The diffusion behavior in the system can be displayed with the diffusion coefficient being related to MSD according to the Einstein's relation [59] as follows:

$$
\mathrm{D}=\frac{1}{6} \lim _{\mathrm{t} \rightarrow \infty} \frac{\mathrm{d}}{\mathrm{dt}}(\mathrm{MSD}) \tag{5}
$$

Figure 8 illustrates the self-diffusion coefficient curve against changes in temperature. According to the Einstein's relation, the self-diffusion coefficient was achieved by calculating the slopes of MSD-time curve at different temperatures. It is well-defined that there is an abrupt change in slope fitted lines around 467 K.

![](./images/811042179291021313_10.jpg)

Figure 8. Self-diffusion coefficient against temperature.

Previous findings in the literature have exhibited the existence of subdiffusive behavior as determined by the MSD for both untangled and entangled linear polymer chains [60, 61]. To understand whether any diffusive displacement exists, we considered the log (MSD) curves against log (time) for 480 K (above $T_g$) and 430 K (below $T_g$). The results shown in Figure 9 indicate that, at high temperatures, the MSD directly crosses over from ballistic motion ( $t^{0.25}$ ) at short times to subdiffusive motion ( $t^{0.5}$ ) at the intermediate times.

![](./images/811042179291021313_11.jpg)

Figure 9. The MSD value versus time for two temperature Line with slopes of 0.25 and 0.5 are shown as a guide for the eye.

### 3.1.3 The internal energy of the system

As reported in previous research, the analysis of the system energy has been proven to be an informative and useful tool for the estimation of the $T_g$. For instance, Soldera et al. specified the $T_g$ of two PMMA chain tacticities by the implementation of an energy approach [62]. Their simulated results revealed that the non-bonded energy plays a significant role in the events associated with the $T_g$ of the PMMA system. To show such a correlation in our study, the variation in the van der Waals energy (E_vdwl) against temperature was assessed. As is illustrated in Figure 10, the energy value linearly increases with the temperature increase. However, it is evident that a sudden change in the slope of the fitted line well specifies a distinct temperature value (429 K) known as the $T_g$.

![](./images/811042179291021313_12.jpg)

Figure 10. Van dar Waals Energy plot versus temperature.

## 3.2 Determination of the $T_g$ through macroscopic properties

### 3.2.1 The volumetric properties

The thermodilatometry technique is an experimental method employed to determine the $T_g$ [63]. Therefore, the concept used to determine the $T_g$ through this technique was employed in the current study to investigate the $T_g$ of PMMA by utilization of the molecular dynamics simulation. To this end, the system was cooled down and the changes in the volume were calculated through a temperature ramp. It is expected that the degree of the motion of the polymer chains alters while the polymer experiences the $T_g$. As commonly accepted, upon the increase in the temperature, the polymers thermally expand. The volume thermal expansion coefficient is defined as:

$$
\alpha_{\mathrm{p}}=\frac{1}{\mathrm{~V}_{0}}\left(\frac{\partial \mathrm{V}}{\partial \mathrm{T}}\right)_{\mathrm{p}} \tag{6}
$$

where V denotes the total volume of the system at temperature $T$, $V_0$ denotes the reference volume at 600K and P is the pressure [64]. The calculated $\alpha_p$ is $2.19 \times 10^{-4} / K$ in the glassy state, and $7.8 \times 10^{-4} / K$ in the rubbery state. Figure 11 depicts the variations in the ratio of $(V-V_0)/V$ against temperature. The slope of the curve represents the volume thermal expansion coefficient. A linear data fitting is used onto the calculated data points. As clearly seen, these lines intersect at 430 K, the temperature value ascribed to the $T_g$.

![](./images/811042179291021313_13.jpg)

Figure 11. The graph of $(V-V_0)/V$ against temperature.

### 3.2.2 The thermal conductivity

In the current study, the equilibrium MD simulation by the utilization of the Green-Kubo approach (Equ. 7) aiming at calculation of the thermal conductivity $\kappa$ of PMMA was employed. The following equation expresses the governing variables in this approach [65]:

$$
\kappa=\frac{\mathrm{V}}{\mathrm{k}_{\mathrm{B}} \mathrm{T}^{2}} \int_{0}^{\infty}\left\langle\mathrm{J}_{\mathrm{z}}(\mathrm{t}) \mathrm{J}_{\mathrm{z}}\left(\mathrm{t}+\mathrm{t}^{\prime}\right)\right\rangle \mathrm{dt}^{\prime} \tag{7}
$$

where $\mathrm{k}_{\mathrm{B}}$ is the Boltzmann constant, $\boldsymbol{\nabla}$ is the volume and $\mathrm{T}$ is the temperature of the system.

$\overrightarrow{\mathrm{J}}(\mathrm{t})$ denotes the heat flux is given by the following expression [65]:

$$
\overrightarrow{\mathrm{J}}(\mathrm{t})=\frac{1}{\mathrm{~V}}\left\{\sum_{\mathrm{i}} \varepsilon_{\mathrm{i}} \overrightarrow{\mathrm{v}}_{\mathrm{i}}+\frac{1}{2} \sum_{\mathrm{i}, \mathrm{j}, \mathrm{i} \neq \mathrm{j}} \overrightarrow{\mathrm{r}}_{\mathrm{ij}}\left(\overrightarrow{\mathrm{F}}_{\mathrm{ij}} \cdot \overrightarrow{\mathrm{v}}_{\mathrm{ij}}\right)\right\} \tag{8}
$$

where $\overrightarrow{\mathrm{v}}_{\mathrm{i}}$ and $\varepsilon_{\mathrm{i}}$ denote the velocity and energy of the atom i respectively, $\overrightarrow{\mathrm{r}}$ is the distance between the atoms and $\overrightarrow{\mathrm{F}}$ is the two/three-body interactions between the atoms. For calculation of the heat flux and its autocorrelation function the simulation was carried out in the NVT ensemble for 10 ns to attain a converged value of the thermal conductivity. Figure 12 indicates the thermal conductivity of PMMA obtained over a temperature scan.

Previous work conducted elsewhere validates these findings and reports a noticeable peak around the $\mathrm{T}_{\mathrm{g}}$ appears in the curve of thermal conductivity- temperature for amorphous polymers [66].
Based on Figure 12, the glass transition is expected to fall within the range of 430–480 K in which the polymer transforms from the glassy to the rubbery state. It is evident that the thermal conductivity of PMMA increases against temperatures below the $\mathrm{T}_{\mathrm{g}}$ whereas the conductivity decreases at temperatures above $\mathrm{T}_{\mathrm{g}}$. The observed increase in the thermal conductivity with temperature below $\mathrm{T}_{\mathrm{g}}$ could be due to two synergistic effects: first, the increase in the mobility of the polymer chains, and second, the decrease in the thermal conductivity of polymer above $\mathrm{T}_{\mathrm{g}}$ possibly due to a greater free volume produced after the $\mathrm{T}_{\mathrm{g}}$ and the lower thermal conductivity of air. It is noteworthy that the trend of results and thermal conductivity values are consistent with those observed experimentally [66].

![](./images/811042179291021313_14.jpg)

Figure 12. Thermal conductivity of PMMA versus temperature.

### 3.2.3 The mechanical properties

For small deformations, the relationship between the stresses and strains may be expressed in terms of the generalized Hooke's law, and can be written following the Einstein's notation as [67, 68]:

$$
\sigma_{\mathrm{i}}=\mathrm{c}_{\mathrm{ij}} \varepsilon_{\mathrm{j}} \tag{9}
$$

where $\mathbf{i}, \mathbf{j}=1,2,3$. $\sigma_{i}$ and $\varepsilon_{j}$ are the six-dimensional stress and strain tensors, respectively, and $c_{i j}$ is the $\boldsymbol{6} \boldsymbol{\times} \boldsymbol{6}$ stiffness matrix. In this work, to account for the thermal effects on the chains as well as the atomic interaction, the stress field, $\sigma$, is calculated using as follows:

$$
\sigma=-\frac{1}{\mathrm{~V}_{0}}\left[\left(\sum_{\mathrm{i}=1}^{\mathrm{N}} \mathrm{m}_{\mathrm{i}}\left(\mathrm{v}_{\mathrm{i}} \mathrm{v}_{\mathrm{i}}\right)\right)+\left(\sum_{\mathrm{i}<\mathrm{j}} \mathrm{r}_{\mathrm{ij}} \mathrm{f}_{\mathrm{ij}}\right)\right] \tag{10}
$$

where $\mathrm{i}$ is the number of the particle, $\mathrm{m}_{\mathrm{i}}$ is the mass, $\mathrm{v}_{\mathrm{i}}$ is the velocity of the particle and $\mathrm{f}_{\mathrm{i}}$ is the force acting on the particle, $\mathrm{V}_{0}$ is the volume of the system [64]. In Equ. 10, the first term is

the contribution of the thermal motions and the second term corresponds to the atomic interactions. The Young's modulus, E, is calculated from the following equation:

$$
\mathrm{E}=\mu \frac{3 \lambda+2 \mu}{\lambda+\mu} \tag{11}
$$

where $\lambda$ and $\mu$ are the elastic Lame's constants. The Lame constants can be calculated from the following relations [64]:

$$
\lambda=\frac{1}{3}\left(\mathrm{C}_{11}+\mathrm{C}_{22}+\mathrm{C}_{33}\right)-\frac{2}{3}\left(\mathrm{C}_{44}+\mathrm{C}_{55}+\mathrm{C}_{66}\right) \tag{12}
$$

$$
\mu=\frac{1}{3}\left(\mathrm{C}_{44}+\mathrm{C}_{55}+\mathrm{C}_{66}\right) \tag{13}
$$

The Young's modulus of the polymer at different temperatures is given in Figure 13. It is shown that when the polymer chains experience the glass transition, the Young's modulus dramatically decreases in the range of 400–500 K from the glassy to the rubbery state. The findings could be attributed to the greater mobility of the chains as a result of the increased kinetic energy available to the individual atoms at high temperatures.

![](./images/811042179291021313_15.jpg)

Figure 13. The Young's modulus of PMMA against temperature.

### 3.3 Effect of cooling rate and molecular weight on $T_g$

The dependency of the $T_g$ on the cooling rate and the polymer molecular weight were also examined.

Table 1 gives the $T_g$ of the polymer against variation in the cooling rate and degree of polymerization. According to

Table 1, the $T_g$ increases as the degree of polymerization and cooling rate increase consistent with the literature [69].

The $T_g$s reported in the table 1 were obtained by the study of the PMMA density against temperature.

Table 1. $T_g$ values obtained using various cooling rates and the degree of polymerization (the Tg unit is in Kelvin).

<table>
<thead>
<tr>
<th rowspan="2">Degree of polymerization</th>
<th rowspan="2">Resulted Chain numbers</th>
<th colspan="6">Cooling Rate</th>
</tr>
<tr>
<th>20 K/ns</th>
<th>10 K/ns</th>
<th>5 K/ns</th>
<th>3.3 k/ns</th>
<th>2.5 K/ns</th>
<th>2 K/ns</th>
</tr>
</thead>
<tbody>
<tr>
<td>100</td>
<td>3</td>
<td>450</td>
<td>437</td>
<td>433</td>
<td>431</td>
<td>430</td>
<td>430</td>
</tr>
<tr>
<td>60</td>
<td>5</td>
<td>435</td>
<td>428</td>
<td>424</td>
<td>422</td>
<td>421</td>
<td>420</td>
</tr>
<tr>
<td>30</td>
<td>10</td>
<td>422</td>
<td>406</td>
<td>401</td>
<td>398</td>
<td>397</td>
<td>395</td>
</tr>
<tr>
<td>20</td>
<td>15</td>
<td>405</td>
<td>389</td>
<td>381</td>
<td>380</td>
<td>380</td>
<td>379</td>
</tr>
<tr>
<td>15</td>
<td>20</td>
<td>390</td>
<td>383</td>
<td>378</td>
<td>375</td>
<td>373</td>
<td>370</td>
</tr>
<tr>
<td>10</td>
<td>30</td>
<td>381</td>
<td>378</td>
<td>375</td>
<td>372</td>
<td>369</td>
<td>368</td>
</tr>
</tbody>
</table>

## 4 Discussion

In the following, we compare the $T_g$ values obtained from various approaches in this study and with the experimental $T_g$ values of PMMA reported in literature and discuss the origins of these discrepancies. The inconsistent $T_g$ values predicted by various approaches used in this work could be explained by the existence of a variety of factors. Table 2 represents the $T_g$ values obtained from the simulation used in this work. As clearly shown, unlike the thermal

conductivity and Young's modulus approaches, the RDF, non-bond energy and the volume method resulted in roughly unique $T_g$ values.

<table>
<caption>Table 2. $T_g$ of PMMA calculated using various methods</caption>
<thead>
  <tr>
    <th>Approach</th>
    <th>$T_g$ (K)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>RDF</td>
    <td>459</td>
  </tr>
  <tr>
    <td>MSD</td>
    <td>470</td>
  </tr>
  <tr>
    <td>Non-bond energy</td>
    <td>430</td>
  </tr>
  <tr>
    <td>Volume thermal expansion</td>
    <td>430</td>
  </tr>
  <tr>
    <td>Thermal conductivity</td>
    <td>glass transition over<br>430-460</td>
  </tr>
  <tr>
    <td>Young's modulus</td>
    <td>glass transition over<br>400-500</td>
  </tr>
  <tr>
    <td>Experimental value</td>
    <td>(315-330) [69-72]</td>
  </tr>
</tbody>
</table>

### 4.1 $T_g$ values against the simulation approaches

The $T_g$ values resulted from various approaches used in this work are in the same order of magnitude and are comparable to the simulation data reported in previous studies (430- 445) [43, 70, 73]. The $T_g$ estimated using the volume, energy, RDF and density methods are quite consistent, which could turn out the increase in the free volume available in the polymer around the $T_g$. Among the methods used in the current work, the $T_g$ obtained from the MSD evaluation is found to be the greatest. This prediction is in perfect agreement with the findings reported in previous studies suggesting that the MSD method estimates a greater $T_g$ with respect to other methods [74, 75]. The higher $T_g$ predicted by the MSD analysis could be explained by the lack of equilibrium for the polymer system in the simulation. This finding appears to be a result of the dynamic equilibrium requiring much more computational time. This work confirms our view that the assessment of $T_g$ using the density and volume approaches can be carried out more easily as compared with the rest of methods employed in this study. The result of the present investigation

also indicates that the thermal conductivity and Young's modulus methods need longer computational time to evaluate the $T_g$ among all other approaches.

Moreover, the utilization of the aforementioned methods leads to the determination of a $T_g$ transition region whereas the methods otherwise just specify a unique $T_g$ value. The gradual release of the immobilized polymer chains so far called the cooperative rearranging regions or CRR is thought to be accounted for a $T_g$ gradient observed over a transition zone [76-78]. The unique $T_g$ estimated being the intersection of the data fitting segments can be however correlated to the change in physical properties of polymer as a result of different mechanisms responsible for the $T_g$. As commonly accepted, such mechanisms are associated with the segmental motion of polymer chains against the vibrational or rotational motion of atoms or side groups each of which dominates the changes in physical properties of a polymer [79-82]. The results also demonstrate that the thermal conductivity and the Young's modulus data points calculated against the variation in temperature follows a non-linear trend consistent with the experimental results reported in earlier studies [48, 66]. However, other methods used for the determination of the $T_g$ result in linear variations in the physical and structural properties against temperature. In such cases, the sudden change in the slope of the curve specifies the value of $T_g$.

The dependency of the $T_g$ on the cooling rate was investigated within the range of 20K/ns – 2K/ns too. A shift of $T_g$ from 450 K to 430 K (almost 5% decrease) is observed over this cooling range. The results additionally show that $T_g$ is governed by the molecular weight. These findings, moreover, reveal that the polymer system consisting of chains with greater molecular weight lead to greater $T_g$ values.

By cooling down a polymer from liquid to glassy state, the density and viscosity of the system increases and the mobility of its chains decreases [83]. Also, the characteristic time of molecular

motions, i.e. structural rearrangements, become greater than the timescale of experimentations
[83]. At the $T_{\mathrm{g}}$, the liquid becomes physically in a non-equilibrium state. The transition from the
equilibrium associated with the liquid state to the solid-like glassy state is called "thermal glass
transition". The thermal glass transition is the temperature at which the slope of the temperature
dependence of characteristic thermodynamic quantities such as the specific volume, density, and
energy changes abruptly but continuously [84]. From a kinetic point of view, the term the
"dynamic glass transition" is associated with the segmental dynamics of polymer. In fact, the
glass transition is regarded as a dynamic phenomenon. At high temperatures, the relaxation time
$\tau$ has a typical value of about $\tau=10^{-13} \mathrm{~s}$. At the $T_{\mathrm{g}}$, the segmental relaxation time increase to
$\tau=10^{2} \mathrm{~s}$ that is comparable to the timescale of the experiments. The study of the viscosity,
modulus, and mean square displacement over a temperature scan could help to determine the
dynamic glass transition [85] .Therefor, the magnitude of the $T_{\mathrm{g}}$ is also governed by the method
employed itself.

### 4.2 The simulation results $\mathbf{T}_{\mathrm{g}}$ versus the experimental results

The results of this study overestimate the $T_{\mathrm{g}}$ of PMMA as compared to the experimental values
[69-72]. This difference seems to be the result of several factors including the modeling
assumptions and the cooling rate employed as follows.

The physical and structural properties of polymers, in general, including PMMA, is highly
influenced by factors such as the molecular weight, tacticity, processing method as well as the
degree of crystallinity and the crystallites sizes in crystalline and semi-crystalline polymers [86,

87]. Consequently, a range of values (i.e. ~315 to 330 K) [69-72] has been reported as the $T_g$ of is-PMMA. This range of values is because of the different cooling rate and different molecular weight of polymer chains. As mentioned earlier, the united atom model in which the presence of hydrogen atoms is not incorporated, was used for the sake of simplicity and improvement in the calculation time. Above such assumptions, the number of repeated units per a chain used in our simulation might be one main cause of deviation from the experimental results. Moreover, a given degree of polymerization and tacticity was also assumed for all chains in our simulations. The discrepancy observed between the simulation and the experimental results can be also attributed to the inconsistency in the simulation cooling rates and what is actually taken place during the processing of polymers. The simulated cooling rate is in the order of 2 K/ns ($1.2×10^{11}$ K/min) that is virtually 10 order of magnitude greater than the cooling rates expected during experimentation [88]. The 50-60 K difference in the $T_g$ found in this work compared with the experimental results may corroborate the dependence of the Tg on the cooling rates and signify that the high cooling rates used in the simulation has led to the greater Tg values [54, 89].

## 5 Conclusions

This study examined various MD-based methods to determine the $T_g$ of PMMA. This was achieved through tracing of the variations in the macroscopic (bulk) and microscopic properties of the polymer during temperature cooling scans. The polymer bulk properties including the thermal conductivity, volume, density, thermal expansion and Young's modulus were calculated against temperature. Microscopic properties such as the structural behavior through the RDF and

the motions of PMMA molecule chains by the MSD function as well as the non-bonded energy were assessed. It is believed that the changes in macroscopic properties of the polymer is controlled by the intermolecular interaction and polymer structure, and, thus, were regarded as a measure to determine the $T_g$.

It was found that the density and volume method requires less computational time to determine the $T_g$ than the thermal conductivity and Young's modulus method. Inconsistent slopes of data fitted lines representing the density, volume, energy, and RDF of polymer were adopted to approximate the $T_g$ values. The thermal conductivity and Young's modulus method, however, resulted in a gradient transition around the $T_g$. The $T_g$ values obtained in this study were found to be almost unvarying irrespective of the MD simulations used and comparable to the reported simulation results. It was suggested that the differences between the experimental and simulated findings could be a result of the simulation simplified assumptions in particular the employed cooling rate. The results also corroborated that the $T_g$ dependence on the molecular weight and cooling rate of which both increase the $T_g$. Further study of this investigation would be useful by incorporating other key variables including the cooling rate and polymer molecular weight into simulations to better scrutinize the generalizability and usefulness of the existing MD techniques in determination of the $T_g$.

## 6 Acknowledgements

The authors would like to thank HR. Rezaei and Dr. H. Nedaaie for their valuable comments and suggestions. We gratefully acknowledge the help from the National High Performance

Computing Center of IASBS (Institute for Advanced Studies in Basic Sciences) for providing the cluster.

## 7 References

1.  Samith VD, Ramos-Moore E: **Study of glass transition in functionalized poly(itaconate)s by differential scanning calorimetry, Raman spectroscopy and thermogravimetric analysis.** *Journal of Non-Crystalline Solids* 2015 **408**:37-42.

2.  Huang M, Tunnicliffe LB, Thomas AG, Busfield JJC: **The glass transition, segmental relaxations and viscoelastic behaviour of particulate-reinforced natural rubber.** *European Polymer Journal* 2015, **67** 232-241.

3.  Djemour A, Sanctuary R, Baller J: **Mobility restrictions and glass transition behaviour of an epoxy resin under confinement.** *Soft Matter* 2015, **11** (13):2683-2690.

4.  Balasubramanian S, Devi A, Singh K, Bosco SD, Mohite AM: **Application of Glass Transition in Food Processing.** *Critical reviews in food science and nutrition* 2016, **56**(6):919-936.

5.  Rask MB, Knopp MM, Olesen NE, Holm R, Rades T: **Influence of PVP/VA copolymer composition on drug-polymer solubility.** *European Journal of Pharmaceutical Sciences* 2016, **85**:10-17.

6.  Burroughs MJ, Napolitano S, Cangialosi D, Priestley RD: **Direct Measurement of Glass Transition Temperature in Exposed and Buried Adsorbed Polymer Nanolayers.** *Macromolecules* 2016, **49**(12):4647-4655.

7.  Knapek M, Húlan T, Minárik P, Dobroň P, Štubňa I, Stráská J, Chmelík F: **Study of microcracking in illite-based ceramics during firing.** *Journal of the European Ceramic Society* 2016, **36**(1):221-226.

8.  Jackson C, Lan T, Caporale S, Torkelson J: **Glass Transition of Polystyrene Thin Films on Silicon Wafer Measured by Dynamic Mechanical Analysis and Ellipsometry.** In: *APS Meeting Abstracts: 2016*; 2016.

9.  Simon SL, Koh YP: **The Glass Transition and Structural Recovery Using Flash DSC.** In: *Fast Scanning Calorimetry*. edn.: Springer; 2016: 433-459.

10. Pagacz J, Pielichowski K: **PVC/MMT nanocomposites.** *Journal of Thermal Analysis and Calorimetry* 2012 **111**(2):1571-1575.

11. Wood CD, Ajdari A, Burkhart CW, Putz KW, Brinson LC: **Understanding competing mechanisms for glass transition changes in filled elastomers.** *Composites Science and Technology* 2016, **127**:88-94.

12. Sun W, Vassilopoulos AP, Keller T: **Effect of thermal lag on glass transition temperature of polymers measured by DMA.** *International Journal of Adhesion and Adhesives* 2014, **52** 31-39.

13. Barbour A, Alatas A, Liu Y, Zhu C, Leu B, Zhang X, Sandy A, Pierce M, Wang X, Cheong S-W: **Partial glass isosymmetry transition in multiferroic hexagonal ErMn O 3.** *Physical Review B* 2016, **93**(5):054113.

14. Silalai N, Sirilert T, Roos YH, Potes N, Devahastin S: **Role of solids composition on $\alpha$-relaxation behavior, molecular structure and stability of spray-dried xanthones encapsulation systems around glass transition.** *Journal of Food Engineering* 2016, **174**:85-91.

15. Thirunarayanan S, Arjunan V, Marchewka M, Mohan S, Atalay Y: **Characterisation of 1, 3-diammonium propylselenate monohydrate by XRD, FT-IR, FT-Raman, DSC and DFT studies.** *Journal of Molecular Structure* 2016, **1107**:220-230.

16. Burroughs MJ, Napolitano S, Cangialosi D, Priestley RD: **Direct Measurement of Glass Transition Temperature in Exposed and Buried Adsorbed Polymer Nanolayers.** *Macromolecules* 2016.

17. Tarnacka M, Kaminska E, Kaminski K, Roland CM, Paluch M: **Interplay between Core and Interfacial Mobility and Its Impact on the Measured Glass Transition: Dielectric and Calorimetric Studies.** *The Journal of Physical Chemistry C* 2016, **120(13)**:7373-7380.

18. Hughes D, Tedeschi C, Leuenberger B, Roussenova M, Coveney A, Richardson R, Bönisch GB, Alam MA, Ubbink J: **Amorphous-amorphous phase separation in hydrophobically-modified starch-sucrose blends II. Crystallinity and local free volume investigation using wide-angle X-ray scattering and positron annihilation lifetime spectroscopy.** *Food Hydrocolloids* 2016, **58**:316-323.

19. Tropin TV, Schmelzer J, Aksenov VL: **Modern aspects of the kinetic theory of glass transition.** *Physics-Uspekhi* 2016, **59(1)**:42.

20. Tool AQ: **Viscosity and the extraordinary heat effects in glass.** *J Am Ceram Soc* 1946, **29**:240-253.

21. Vol'kenshtein M, Ptitsyn O: **The relaxation theory of glass transition.** In: *Dokl Akad Nauk SSSR*: 1955; 1955: 795-798.

22. Doolittle AK: **Studies in Newtonian flow. II. The dependence of the viscosity of liquids on free-space.** *Journal of Applied Physics* 1951, **22(12)**:1471-1475.

23. Moynihan C, Macedo P, Montrose C, Gupta P, DeBolt M, Dill J, Dom B, Drake P, Easteal A, Elterman P: **Structural relaxation in vitreous materials.** *Annals of the New York Academy of Sciences* 1976, **279(1)**:15-35.

24. Kovacs AJ, Aklonis JJ, Hutchinson JM, Ramos AR: **Isobaric volume and enthalpy recovery of glasses. II. A transparent multiparameter theory.** *Journal of Polymer Science: Polymer Physics Edition* 1979, **17(7)**:1097-1162.

25. Gibbs JH, DiMarzio EA: **Nature of the glass transition and the glassy state.** *The Journal of Chemical Physics* 1958, **28(3)**:373-383.

26. Gutzow I, Schmelzer J: **The vitreous state**: Springer; 1995.

27. De Donder T, Van Rysselberghe P: **Thermodynamic theory of affinity**, vol. 1: Stanford university press; 1936.

28. Hodge IM: **Strong and fragile liquids—a brief critique.** *Journal of non-crystalline solids* 1996, **202(1)**:164-172.

29. Scott Shell M, Debenedetti PG, Panagiotopoulos AZ: **A conformal solution theory for the energy landscape and glass transition of mixtures.** *Fluid Phase Equilibria* 2006, **241(1-2)**:147-154

30. Leutheusser E: **Dynamical model of the liquid-glass transition.** *Physical Review A* 1984, **29(5)**:2765.

31. Kirkpatrick T, Thirumalai D, Wolynes PG: **Scaling concepts for the dynamics of viscous liquids near an ideal glassy state.** *Physical Review A* 1989, **40(2)**:1045.

32. Chakrabarty S, Das R, Karmakar S, Dasgupta C: **Understanding the Dynamics of Glass-forming Liquids with Random Pinning within the Random First Order Transition Theory.** *arXiv preprint arXiv:160304648* 2016.

33. de Candia A, Fierro A, Coniglio A: **Scaling and universality in glass transition.** *Scientific reports* 2016, **6**.

34. Wang Z, Lv Q, Chen S, Li C, Sun S, Hu S: Glass transition investigations on highly crosslinked epoxy resins by molecular dynamics simulations. *Molecular Simulation* 2015 **41** (18):1515-1527.

35. Gupta J, Nunes C, Jonnalagadda S: A molecular dynamics approach for predicting the glass transition temperature and plasticization effect in amorphous pharmaceuticals. *Molecular pharmaceutics* 2013, **10** (11):4136-4145.

36. Soldera A: Comparison Between the Glass Transition Temperatures of the Two PMMA Tacticities: A Molecular Dynamics Simulation Point of View. *Macromolecules* 1998, **133**.

37. Binder K: Monte Carlo and molecular dynamics simulation of the glass transition of polymers. *J Phys: Condens Matter* 1999, **11**:A47–A55.

38. Binder K: The Monte Carlo method for the study of phase transitions: A review of some recent progress. *Journal of Computational Physics* 1985, **59**(1):1-55.

39. Binder K: Monte Carlo and molecular dynamics simulations in polymer science: Oxford University Press; 1995.

40. Accelrys Inc SD: *Amorphous cell and discover modules* [Materials Studio 4.0, Visualizer, QSAR]. 2005.

41. Zhu X, Zhang S, Zhang L, Liu H, Hu J: Interfacial synthesis of magnetic PMMA@ Fe 3 O 4/Cu 3 (BTC) 2 hollow microspheres through one-pot Pickering emulsion and their application as drug delivery. *RSC Advances* 2016, **6**(63):58511-58515.

42. Soldera A, Grohens Y: Molecular modeling of the glass transition of stereoregular PMMAs. *Polymer-Plastics Technology and Engineering* 2002, **41**(3):561-571.

43. Soldera A: Energetic analysis of the two PMMA chain tacticities and PMA through molecular dynamics simulations. *Polymer* 2002, **43**(15):4269-4275.

44. Soldera A, Metatla N: Glass transition phenomena observed in stereoregular PMMAs using molecular modeling. *Composites Part A: Applied Science and Manufacturing* 2005, **36**(4):521-530.

45. Soldera A, Grohens Y: Cooperativity in stereoregular PMMAs observed by molecular simulation. *Polymer* 2004, **45**(4):1307-1311.

46. Soldera A, Grohens Y: Local dynamics of stereoregular PMMAs using molecular simulation. *Macromolecules* 2002, **35**(3):722-726.

47. Subramanian V, Asirvatham PS, Balakrishnan R, Ramasami T: Molecular mechanics studies on polypropylene and polymethylmethacrylate polymers. *Chemical physics letters* 2001, **342**(5):603-609.

48. Berrahou N, Mokaddem A, Doumi B, Hiadsi S, Beldjoudi N, Boutaous A: Investigation by molecular dynamics simulation of the glass transition temperature and elastic properties of amorphous polymers PMMA, PMAAM and PMMA co PMAAM copolymers. *Polymer Bulletin*:1-11.

49. Plimpton S: Fast parallel algorithms for short-range molecular dynamic. *Journal of computational physics* 1995, **117.1**:1-19.

50. Shaffer JS, Chakraborty AK, Tirrell M, Davis HT, Martins JL: The nature of the interactions of poly(methyl methacrylate) oligomers with an aluminum surface. *The Journal of Chemical Physics* 1991 **95**(11):8616.

51. O. Okadaa KO, S. Kuwajimab, S. Toyodac, K. Tanabed: Molecular simulation of an amorphous poly(methyl methacrylate)–poly(tetrafluoroethylene) interface. *Computational and Theoretical Polymer Science* 2000, **10**:371–381.

52. Asadinezhad A, Kelich P: Effects of carbon nanofiller characteristics on PTT chain conformation and dynamics: A computational study. *Applied Surface Science* 2017, 392:981-990.

53. Luo Z, Jiang J: Molecular dynamics and dissipative particle dynamics simulations for the miscibility of poly (ethylene oxide)/poly (vinyl chloride) blends. *Polymer* 2010, 51(1):291-299.

54. Wu C, Xu W: Atomistic molecular simulations of structure and dynamics of crosslinked epoxy resin. *Polymer* 2007, 48(19):5802-5812.

55. Leenaerts D, Van Bokhoven WM: Piecewise linear modeling and analysis: Springer Science & Business Media; 2013.

56. Tronstrum MK, Sethna JP: Improvements to the Levenberg-Marquardt algorithm for nonlinear least-squares minimization. *arXiv preprint arXiv:12015885* 2012.

57. Choi J, Yu S, Yang S, Cho M: The glass transition and thermoelastic behavior of epoxy-based nanocomposites: A molecular dynamics study. *Polymer* 2011, 52 (22):5197-5203.

58. Trady S, Mazroui M, Hasnaoui A, Saadouni K: Molecular dynamics study of atomic-level structure in monatomic metallic glass. *Journal of Non-Crystalline Solids* 2016, 443:136-142.

59. Favro LD: Theory of the rotational Brownian motion of a free rigid body. *Physical Review* 1960, 119(1):53.

60. Wang Z, Larson RG: Constraint release in entangled binary blends of linear polymers: a molecular dynamics study. *Macromolecules* 2008, 41(13):4945-4960.

61. Lyulin AV, Balabaev NK, Michels M: Correlated segmental dynamics in amorphous atactic polystyrene: a molecular dynamics simulation study. *Macromolecules* 2002, 35(25):9595-9604.

62. Soldera A: Energetic analysis of the two PMMA chain tacticities and PMA through molecular dynamics simulation *Polymer* 2002, 43:4269-4275.

63. Venkatanarayanan RI, Krishnan S, Sreeram A, Yuya PA, Patel NG, Tandia A, McLaughlin JB: Simulated Dilatometry and Static Deformation Prediction of Glass Transition and Mechanical Properties of Polyacetylene and Poly (para-phenylene vinylene). *Macromolecular Theory and Simulations* 2016, 25(3):238-253.

64. Fan HB, Yuen MM: Material properties of the cross-linked epoxy resin compound predicted by molecular dynamics simulation. *Polymer* 2007, 48(7):2174-2178.

65. Henry A, Chen G: High thermal conductivity of single polyethylene chains using molecular dynamics simulations. *Physical review letters* 2008, 101(23):235502.

66. Dos Santos W, de Sousa J, Gregorio R: Thermal conductivity behaviour of polymers around glass transition and crystalline melting temperatures. *Polymer Testing* 2013, 32(5):987-994.

67. Nye JF: Physical properties of crystals: their representation by tensors and matrices: Oxford university press; 1985.

68. Giunta G, Koutsawa Y, Belouettar S, Hu H: Static, free vibration and stability analysis of three-dimensional nano-beams by atomistic refined models accounting for surface free energy effect. *International Journal of Solids and Structures* 2013, 50(9):1460-1472.

69. Ute K, Miyatake N, Hatada K: Glass transition temperature and melting temperature of uniform isotactic and syndiotactic poly (methyl methacrylate) s from 13mer to 50mer. *Polymer* 1995, 36(7):1415-1419.

70. Soldera A, Metatla N, Beaudoin A, Said S, Grohens Y: Heat capacities of both PMMA stereomers: Comparison between atomistic simulation and experimental data. *Polymer* 2010, 51(9):2106-2111.

71. Biroš J, Larina T, Trekoval J, Pouchlý J: Dependence of the glass transition temperature of poly (methyl methacrylates) on their tacticity. *Colloid & Polymer Science* 1982, 260(1):27-30.

72. Grohens Y, Brogly M, Labbe C, David M-O, Schultz J: **Glass transition of stereoregular poly (methyl methacrylate) at interfaces.** *Langmuir* 1998, **14**(11):2929-2932.

73. Dixit M, Gupta S, Mathur V, Rathore KS, Sharma K, Saxena N: **Study of glass transition temperature of PMMA and CdS-PMMA composite.** *Chalcogenide Letters* 2009, **6**(3):131-136.

74. Baljon A, Williams S, Balabaev N, Paans F, Hudzinskyy D, Lyulin A: **Simulated glass transition in free-standing thin polystyrene films.** *Journal of Polymer Science Part B: Polymer Physics* 2010, **48**(11):1160-1167.

75. Wu C: **Simulated glass transition of poly (ethylene oxide) bulk and film: a comparative study.** *The Journal of Physical Chemistry B* 2011, **115**(38):11044-11052.

76. Priestley RD: **Effects of nanoscale confinement and interfaces on the structural relaxation of amorphous polymers monitored at the molecular scale by fluorescence and dielectric spectroscopy:** ProQuest; 2008.

77. Sargsyan A, Tonoyan A, Davtyan S, Schick C: **The amount of immobilized polymer in PMMA SiO<sub>2</sub> nanocomposites determined from calorimetric data.** *European polymer journal* 2007, **43**(8):3113-3127.

78. Donth E: **Characteristic length of the glass transition.** *Journal of Polymer Science Part B: Polymer Physics* 1996, **34**(17):2881-2892.

79. Cicerone MT, Blackburn F, Ediger M: **How do molecules move near Tg? Molecular rotation of six probes in o-terphenyl across 14 decades in time.** *The Journal of chemical physics* 1995, **102**(1):471-479.

80. Fujara F, Geil B, Sillescu H, Fleischer G: **Translational and rotational diffusion in supercooled orthoterphenyl close to the glass transition.** *Zeitschrift für Physik B Condensed Matter* 1992, **88**(2):195-204.

81. Lu H, Nutt S: **Restricted relaxation in polymer nanocomposites near the glass transition.** *Macromolecules* 2003, **36**(11):4010-4016.

82. Zhang X, Loo LS: **Study of glass transition and reinforcement mechanism in polymer/layered silicate nanocomposites.** *Macromolecules* 2009, **42**(14):5196-5207.

83. Schönhals A: **Molecular dynamics in polymer model systems.** In: *Broadband dielectric spectroscopy.* edn.: Springer; 2003: 225-293.

84. Donth E-J: **The glass transition: relaxation dynamics in liquids and disordered materials**, vol. 48: Springer Science & Business Media; 2013.

85. Mijovic J, Lee H, Kenny J, Mays J: **Dynamics in polymer-silicate nanocomposites as studied by dielectric relaxation spectroscopy and dynamic mechanical spectroscopy.** *Macromolecules* 2006, **39**(6):2172-2182.

86. Christofferson AJ, Yiapanis G, Ren JM, Qiao GG, Satoh K, Kamigaito M, Yarovsky I: **Molecular mapping of poly (methyl methacrylate) super-helix stereocomplexes.** *Chemical Science* 2015, **6**(2):1370-1378.

87. Arai F, Shinohara K, Nagasawa N, Takeshita H, Takenaka K, Miya M, Shiomi T: **Crystallization behavior and higher-order structure in miscible crystalline/crystalline polymer blends.** *Polymer journal* 2013, **45**(9):921-928.

88. Nishi T, Wang T: **Melting point depression and kinetic effects of cooling on crystallization in poly (vinylidene fluoride)-poly (methyl methacrylate) mixtures.** *Macromolecules* 1975, **8**(6):909-915.

89. Wu C: **Cooperative behavior of poly (vinyl alcohol) and water as revealed by molecular dynamics simulations.** *Polymer* 2010, **51**(19):4452-4460.

## 8 Figure Captions

Figure 1. (a) A single monomer of PMMA (all atom), ( (b) the monomer of PM PMMA ( united atom) and (c)
10-m chain of is-P -PM

Figure 2. (a) The energy/ chain during NPT equilib at 6600K and ( (b) the AC changes of PM MMA
chain end-to-end distance vector against production time.

Figure 3. ( (a) The energy/ chain of the PMMA during the process of MD simulation at a cooling rate of
2K//ns and ((b) the potential energy/ chain of PMMA at different temperatures during the cooling in each
stage.

Figure 4. ( (a) The RDF for various pairs of atoms for oxygen atoms, carbon atoms, carbon and oxygen
 atoms and all atoms and (b) the RDF for all atoms in two temperatures.

Figure 5. ( (a) The radial distribution function at different temperatures for non-bbonded carbon atoms
and ( (b) a zoomed-in image over ( right)

Figure 6. $g(r=4\\mathring{{A$ against temperature for non-bded carbon atoms.

Figure 7. ((a) MSD curves against variation time and temperature and (b) M values at 255 ns in
 different temperatures.

 Figure 8. Self-d diffusion coefficient against temperature.

 Figure 9. The MSD value versus time for two temperature Line with slopes of 00.225 and 0.5 are shown as
 a guide for the eye.

Figure 10. Van dar Waals Energy plot versus temperature.

 Figure  11. The graph of $(V-V__ //V against temperature.

 Figure  1 2. Thermal conductivity of PMMA versus temperature.

Figure  13. The Young’s modulus of PMMA against temperature.

## 9 Tables

Table 1. $T_g$ values obtained using various cooling rates and the degree of polymerization (the Tg unit is in Kelvin).

<table>
  <thead>
    <tr>
      <th rowspan="2">Degree of polymerization</th>
      <th rowspan="2">Resulted Chain numbers</th>
      <th colspan="6">Cooling Rate</th>
    </tr>
    <tr>
      <th>20 K/ns</th>
      <th>10 K/ns</th>
      <th>5 K/ns</th>
      <th>3.3 k/ns</th>
      <th>2.5 K/ns</th>
      <th>2 K/ns</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>100</td>
      <td>3</td>
      <td>450</td>
      <td>437</td>
      <td>433</td>
      <td>431</td>
      <td>430</td>
      <td>430</td>
    </tr>
    <tr>
      <td>60</td>
      <td>5</td>
      <td>435</td>
      <td>428</td>
      <td>424</td>
      <td>422</td>
      <td>421</td>
      <td>420</td>
    </tr>
    <tr>
      <td>30</td>
      <td>10</td>
      <td>422</td>
      <td>406</td>
      <td>401</td>
      <td>398</td>
      <td>397</td>
      <td>395</td>
    </tr>
    <tr>
      <td>20</td>
      <td>15</td>
      <td>405</td>
      <td>389</td>
      <td>381</td>
      <td>380</td>
      <td>380</td>
      <td>379</td>
    </tr>
    <tr>
      <td>15</td>
      <td>20</td>
      <td>390</td>
      <td>383</td>
      <td>378</td>
      <td>375</td>
      <td>373</td>
      <td>370</td>
    </tr>
    <tr>
      <td>10</td>
      <td>30</td>
      <td>381</td>
      <td>378</td>
      <td>375</td>
      <td>372</td>
      <td>369</td>
      <td>368</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th colspan="2">Table 3. $T_g$ of PMMA calculated using various methods</th>
    </tr>
    <tr>
      <th>Approach</th>
      <th>$T_g$ (K)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RDF</td>
      <td>459</td>
    </tr>
    <tr>
      <td>MSD</td>
      <td>470</td>
    </tr>
    <tr>
      <td>Non-bond energy</td>
      <td>429</td>
    </tr>
    <tr>
      <td>Volume thermal expansion</td>
      <td>430</td>
    </tr>
    <tr>
      <td>Thermal conductivity</td>
      <td>glass transition over 430-460</td>
    </tr>
    <tr>
      <td>Young's modulus</td>
      <td>glass transition over 400-500</td>
    </tr>
    <tr>
      <td>Experimental value</td>
      <td>(315-330) [69-72]</td>
    </tr>
  </tbody>
</table>
