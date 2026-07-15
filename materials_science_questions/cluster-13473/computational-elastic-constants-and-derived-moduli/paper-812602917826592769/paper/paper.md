Journal Pre-proof

Study of nanoscale deformation mechanisms in bulk hexagonal hydroxyapatite under uniaxial loading using molecular dynamics

Alexander D. Snyder, Iman Salehinia

![](./images/812602917826592769_1.jpg)

PII:
S1751-6161(20)30448-3

DOI:
https://doi.org/10.1016/j.jmbbm.2020.103894

Reference:
JMBBM 103894

To appear in:
*Journal of the Mechanical Behavior of Biomedical Materials*

Received Date: 19 June 2019

Revised Date: 19 December 2019

Accepted Date: 29 May 2020

Please cite this article as: Snyder, A.D., Salehinia, I., Study of nanoscale deformation mechanisms in bulk hexagonal hydroxyapatite under uniaxial loading using molecular dynamics, *Journal of the Mechanical Behavior of Biomedical Materials* (2020), doi: https://doi.org/10.1016/j.jmbbm.2020.103894.

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier Ltd.

Alexander D. Snyder: Methodology, Software, Validation, Writing - Original Draft,
Visualization, Writing - Review & Editing

Iman Salehinia: Conceptualization, Writing - Review & Editing, Visualization, Supervision,
Project administration

# Study of Nanoscale Deformation Mechanisms in Bulk Hexagonal Hydroxyapatite under Uniaxial Loading using Molecular Dynamics

Alexander D. Snyder¹, Iman Salehinia²,*

¹Department of Mechanical and Aerospace Engineering, North Carolina State University, Raleigh, NC, 27695. (asnyder3@ncsu.edu)
²Department of Mechanical Engineering, Northern Illinois University, DeKalb, IL, 60115.
(Corresponding author, isalehinia@niu.edu)

## Abstract
Hydroxyapatite (HAP) is a natural bioceramic which is currently used in scaffolds and coatings for the regrowth of osseous tissue but offers poor load-bearing capacity compared to other biomaterials. The deformation mechanisms responsible for the mechanical behavior of HAP are not well understood, although the advent of multiscale modeling offers the promise of improvements in many materials through computational materials science. This work utilizes molecular dynamics to study the nanoscale deformation mechanisms of HAP in uniaxial tension and compression. It was found that deformation mechanisms vary with loading direction in tension and compression leading to significant compression/tension asymmetry and crystal anisotropy. Bond orientation and geometry relative to the loading direction was found to be an indicator of whether a specific bond was involved in the deformation of HAP in each loading case. Tensile failure mechanisms were attributed to stretching and failure in loading case-specific ionic bond groups. The compressive failure mechanisms were attributed to columbic repulsion in each case, although loading case-specific bond group rotation and displacement were found to affect specific failure modes. The elastic modulus was the highest for both tension and compression along the Z direction (i.e. normal to the basal plane), followed by Y and X.

Keywords: hexagonal hydroxyapatite, nanoscale deformation mechanisms, uniaxial loading, molecular dynamics, interface force field

## 1. Introduction
Hydroxyapatite (HAP) $(Ca_{10}(PO_{4})_{6}(OH)_{2})$ is an inorganic calcium phosphate ceramic which acts as the main load-bearing constituent in osseous tissues. Hydroxyapatite platelets act as a reinforcement in the composite structure of bone as the collagen matrix transfers load to them via shear (Stock, 2015). Hydroxyapatite can be produced synthetically in stoichiometric ratios consistent with its biological counterpart, and is currently used in applications such as bone tissue scaffolding with tunable resorbability and as a bioactive coating for bioinert materials (Gao et al., 2014; Pawłowski, 2018; Szcześ et al., 2017). The use of HAP as a bioactive coating has been shown to improve bone adhesion and mechanical properties at the implant-tissue interface (Harun et al., 2018).

The remarkable properties of natural bone can be attributed to its hierarchical structuring and associated deformation mechanisms (Huang et al., 2019). In hydroxyapatite single crystals alone, those subjected to nanoindentation were found to display more dislocation pile up and plasticity than crystals subjected to microindentation (Viswanath et al., 2007). Further nanoindentation studies with HAP single crystals have shown crystallographic anisotropy with respect to work hardening response, yield stress, fracture toughness, and crack lengths (Saber-Samandari and Gross, 2009; Zamiri and De, 2011). HAP crystals were found to have higher side plane fracture toughness but possess higher hardness and elastic moduli values on the basal planes (Saber-Samandari and Gross, 2009).

The bonding and structural disorder present in both monoclinic and hexagonal HAP has been explored via the use of synchrotron and neutron diffraction (Yashima et al., 2011). Clear covalent bonding between O-H and P-O groups was observed, with Ca-O bonds being confirmed as ionic. In hexagonal hydroxyapatite, O-H group alignment is unidirectional and the electron density around phosphate group oxygen atoms is symmetric. This is not the case in monoclinic HAP, where O-H group orientation is random and non-symmetric electron density distribution exist around phosphate group oxygen atoms. Experimental data has been used to reparametrize bonding coefficients and atomic partial charges in hexagonal HAP, with these values being intended for use in molecular dynamics force field formulation (Lin, 2013).

Molecular dynamics atomistic simulations have been used to study the mechanical behavior of HAP crystals. Confinement behavior was observed in HAP single crystals with respect to fracture toughness (Libonati et al., 2013). The elastic modulus of HAP single crystals was found to increase with crystal thickness up to 2nm, which is in agreement with natural HAP platelet thickness of 1-2nm (Qin et al., 2012). In systems of collagen fibrils with HAP platelets or mineralized collagen fibrils, the presence of platelets or increase of mineralization content was found to greatly increase the load-bearing response of the respective system (Nair et al., 2013; Qin et al., 2012). The mechanical properties of monoclinic HAP crystals with periodic boundary conditions were studied using MD simulations implementing a polymer consistent forcefield (PCFF) interatomic potential (Ou and Han, 2014). The fracture strength and elastic modulus of monoclinic HAP in tension were found to increase with applied strain rate and decreasing temperature, with the Z direction (normal to the basal plane) possessing the lowest fracture toughness and elastic modulus. In compression, the Young's modulus and fracture strength values were highest in the Z direction. Temperature was insignificant in affecting fracture strength or elastic moduli in any case. These values were found to increase with increasing compressive strain rate. However, deformation mechanisms that control the observed behavior were not detailed and discussed. Ching et al. performed ab-initio calculations on a small HAP single crystal (88 atoms) to study the its mechanical behavior under uniaxial and bi-axial tension (Ching et al., 2009). They reported one major underlying mechanism, i.e. rotation of PO4 tetrahedra with accompanying movement of both the columnar and axial Ca ions, for the HAP single crystal under loading. However, they have not discussed the other deformation

mechanisms that govern the changes in both elastic and non-elastic portions of the stress-strain curves. They also did not consider the mechanical behavior of the material under uniaxial compression, which is more applicable for ceramic materials.

To date, the nanoscale deformation mechanisms in bulk hexagonal HAP have not been studied. However, these are believed to play a role in the transition observed from nanoscale to microscale properties in HAP (Huang et al., 2019; Kwon and Clumpner, 2018). Furthermore, hierarchical deformation mechanisms in both collagen and HAP are responsible for the remarkable mechanical properties of bone (Huang et al., 2019; Kwon and Clumpner, 2018; Maghsoudi-Ganjeh et al., 2019). Natural HAP is hexagonal in structure as opposed to monoclinic. Hexagonal HAP is currently synthesized in lab environments to provide osseointegrative and resorbable coatings for metallic implants and scaffolds for bone tissue growth (An et al., 2012; Choudhury and Agrawal, 2011; Costa et al., 2013; Deville et al., 2006; Mygind et al., 2007).

Molecular dynamics simulations using the CVFF-Interface (CVFF-IFF) interatomic potential have been carried out to study the deformation mechanisms in hexagonal HAP under uniaxial tension and compression loading in various directions. More specifically, this work provides novel insights into the bonds and interatomic interactions that govern nanoscale deformation of hydroxyapatite. The proposed framework in this study will allow for the assessment of how these deformation mechanisms change when dopant atoms or defects (vacancies or porosity) are added to hydroxyapatite. This investigation is intended to complement the current knowledge of the governing deformation mechanisms that contribute to ductility of bones and teeth at the atomic scale (Huang et al., 2019; Kwon and Clumpner, 2018). This information further contributes to the multiscale modeling and design of various advanced materials that utilize HAP as a major constituent, such as biocomposites (Ramesh et al., 2018; White et al., 2007) or those with a HAP coating on other materials (Harun et al., 2018; Lacefield, 1988; Ong and Chan, 2000).

## 2. Modeling and Computational Methods

The unit cell for HAP used in this work has the chemical formula $\text{Ca}_{10}(\text{PO}_4)_6(\text{OH})_2$ and has 44 atoms. The unit cell itself is triclinic, with lattice parameters a=9.417 Å, b=9.417 Å, and c=6.875Å. The interior angles are $\alpha=\beta=90^\circ$ and $\gamma=120^\circ$ (Hughes and Rakovan, 2002; Kay et al., 1964; Lin, 2013; Pawłowski, 2018). The space group is P6/3m. The hexagonal HAP unit cell was modeled using Materials Studio 4.0. Using X-ray diffraction and Fourier transform infrared spectroscopy, Viswanath et al. reported phase-pure HAP crystals that were predominantly bounded by prism and basal planes (Viswanath et al., 2007). The Z direction in this work is normal to the basal plane of the HAP single crystal.

![](./images/812602917826592769_2.jpg)

Figure 1: Four HAP unit cells shown in the x-y (transformed a-b) plane. The z (c) axis is into the page. Calcium atoms are in blue, oxygen atoms are in red, phosphorus atoms are in tan, and the yellow atoms represent the hydroxide columns. Oxygens are present below the hydrogen atoms (yellow) into the page and are colored white. Half values of lattice parameters a and b are shown along the respective cell orientations relative to the imposed x-y axes for one unit cell.

The HAP structure is composed of periodically arranged phosphate tetrahedra, Calcium (I) polyhedra, and Calcium (II) polyhedra. These polyhedra and their associated atoms are shown in Figure 2.

![](./images/812602917826592769_3.jpg)

Figure 2: Polyhedra which compose the HAP crystallographic structure. a. Phosphate tetrahedron. b. Calcium (I) polyhedron. c. Calcium (II) polyhedron. Pictured in c are substitution locations for chlorine and fluorine, which are not considered in this work (reproduced from (Hughes and Rakovan, 2002)).

LAMMPS (Plimpton, 1995) as used to perform all MD simulations in this study. The utilized interatomic potential was the CVFF-Interface Force Field, which has the functional form

$$
\begin{aligned}
E_{total} = \sum_{bonds} K_{r,ij} \left(r_{ij} - r_{0, ij}\right)^2 + \sum_{angles} K_{\theta,ijk}(\theta_{ijk} - \theta_{0,ijk})^2 + \sum_{if\ nonbonded} \frac{q_i q_j}{4\pi \varepsilon_0 r_{ij}} + \\
\sum_{if\ nonbonded} \varepsilon_{ij} \left[\left(\frac{\sigma_{ij}}{r_{ij}}\right)^{12} - 2\left(\frac{\sigma_{ij}}{r_{ij}}\right)^6\right]
\end{aligned} \tag{1}
$$

The first summation is a harmonic bond stretching potential, the second summation is a harmonic bond angular potential, the third summation is a nonbonded columbic interaction potential, and the fourth summation is a 12-6 Lennard-Jones nonbonded interaction potential (Lin, 2013). The parameters in Eq. (1) are defined in Table 1.

Table 1: Definitions of the parameters in Eq. 1.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$K_{r,ij}$</td>
      <td>harmonic bond linear stretching stiffness</td>
    </tr>
    <tr>
      <td>$r_{ij}$</td>
      <td>center-to-center distance between two particles i and j</td>
    </tr>
    <tr>
      <td>$r_{0,ij}$</td>
      <td>initial length of a harmonic bond</td>
    </tr>
    <tr>
      <td>$K_{\theta,ijk}$</td>
      <td>harmonic bond angular stretching stiffness</td>
    </tr>
    <tr>
      <td>$\theta_{ijk}$</td>
      <td>angle between three particles i, j, and k</td>
    </tr>
    <tr>
      <td>$\theta_{0,ijk}$</td>
      <td>initial angle between three particles i, j, and k</td>
    </tr>
    <tr>
      <td>$q_i$</td>
      <td>charge of particle i</td>
    </tr>
    <tr>
      <td>$q_j$</td>
      <td>charge of particle j</td>
    </tr>
    <tr>
      <td>$\varepsilon_0$</td>
      <td>permittivity of a vacuum</td>
    </tr>
    <tr>
      <td>$\varepsilon_{ij}$</td>
      <td>Van Der Waals energy well depth</td>
    </tr>
    <tr>
      <td>$\sigma_{ij}$</td>
      <td>Van der Waals radius of two non-bonded atoms i and j</td>
    </tr>
  </tbody>
</table>

In addition to showing excellent agreement between calculated and experimental values for bulk and surface properties across many inorganic compounds such as mica, silicate, and aluminate, the Interface Force Field (IFF) and its variants have also accurately reproduced cleavage energy, bulk modulus, and lattice parameters for hydroxyapatite (Emami et al., 2014; Heinz et al., 2013; Heinz, 2016; Lin and Heinz, 2016; Lin, 2013). IFF enables accurate quantitative computations of adsorption, substitution, and assembly due to the reduction of surface and interfacial energy error to <10%. IFF also provides more accurate computation of lattice parameters by up to an order of error magnitude compared to other forcefields and allows for higher chemical accuracy (~1 kcal/mol) relative to experiments (Heinz et al 2013).

Given that the bonds used in this potential are harmonic in nature, it is implied that the bond between two atoms is represented computationally as a spring with a given stiffness. Using the CVFF Interface force field, the calculated bulk modulus obtained was 81.3 GPa at, which are in good agreement with the other published values in Table 2.

Table 2: Elastic stiffness and bulk modulus values for HAP from experimental data and different computational methods.

<table>
  <thead>
    <tr>
      <th>Method/Potential Used</th>
      <th>C₁₁ (GPa)</th>
      <th>C₃₃ (GPa)</th>
      <th>B (GPa)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>This work</td>
      <td>131</td>
      <td>165</td>
      <td>81.3</td>
    </tr>
    <tr>
      <td>Experimental (Gilmore and Katz, 1982)</td>
      <td>137</td>
      <td>172</td>
      <td>89.0</td>
    </tr>
    <tr>
      <td>Lin 9-6 FF (Heinz, 2016)</td>
      <td>130</td>
      <td>157</td>
      <td>72.9</td>
    </tr>
    <tr>
      <td>Lin 12-6 FF (Heinz, 2016)</td>
      <td>147</td>
      <td>185</td>
      <td>81.3</td>
    </tr>
    <tr>
      <td>Buckingham (Leeuw et al., 2006)</td>
      <td>134.4</td>
      <td>184.7</td>
      <td>90</td>
    </tr>
    <tr>
      <td>PAW-PBE (DFT) (Ching et al., 2009)</td>
      <td>140</td>
      <td>174.8</td>
      <td>84.5</td>
    </tr>
    <tr>
      <td>PBE Functional (DFT) (Menéndez-Proupin et al., 2011)</td>
      <td>145.2</td>
      <td>191.4</td>
      <td>90.7</td>
    </tr>
    <tr>
      <td>VRH Approximation (Snyders et al., 2007)</td>
      <td>117.1</td>
      <td>231.8</td>
      <td>82</td>
    </tr>
  </tbody>
</table>

All mechanical loading simulations were performed by utilizing a model of 44000 atoms obtained via replication of the HAP unit cell 10 times in the X, Y, and Z directions. Periodic boundary conditions were applied in all 3 dimensions. Prior to any loading application, minimization was performed using the conjugate gradient method. The cutoff distance of $9.5\ \mathring{A}$ was used for the Lennard-Jones and the long-range columbic pair potentials. To correctly account for charge screening and to ensure proper convergence of system energy due to contributions from long-range interactions, an Ewald summation with a desired relative error of 1e-4 or less was used (Ewald, 1921). Due to the presence of hydrogen in the system, a timestep of 0.5 fs was used in all simulations.

Loading directions included in this study are X, Y, and Z uniaxial tension and uniaxial compression. The deformation mechanisms were explored at a strain rate of 1e10 /s and the temperature of 10 K for a system of 44000 atoms. The deformation mechanisms were the same for selected cases when a strain rate of 6e8 /s was used. Simulations at 10K were used to clearly visualize the deformation mechanisms under mechanical loading (Salehinia et al., 2013). As HAP is a ceramic, no significant change in the deformation mechanisms is anticipated between 10 K and higher temperatures that are associated with the living systems. The effect of system size was found to be insignificant, with the behavior for systems of 5500 atoms and 44000 atoms being the same.

### 3. Results and Discussion

This section details the mechanical response and associated deformation mechanisms of HAP single crystals under uniaxial tension and compression along the illustrated X, Y, and Z axes.

### 3.1. Uniaxial tension

Uniaxial tension and compression in X, Y, and Z directions were applied to the HAP single crystals to understand the mechanical response and the governing deformation mechanisms under mechanical loading. The model is free of defects and representative of material at the nanoscale, where the presence of defects is less probable (Salehinia et al., 2013).

Fig. 3 shows the stress-strain curves for uniaxial tension at a strain rate of 1e10 /s and temperature of 10 K along the X, Y, and Z axes. The elastic modulus is highest in the Z direction ($E_z = 160$ GPa) and similar for X and Y ($E_x = 116$ GPa, $E_y = 117$ GPa). However, the fracture strength and strain are both highest in the Y direction and lowest in the Z direction. For both the X and Y directions, the peak strain is larger than the strain where the constitutive response is changed, i.e. 6.5%. In contrast, the stress quickly drops for the Z direction at a strain of 8.5%, indicating a very low degree of plasticity in this direction. The observed mechanical behavior of HAP single crystals in this work is in good agreement with the results of an ab-initio study detailing the mechanical behavior of a HAP single crystal under tensile loading (Ching et al., 2009). Ductile behavior was observed when the single crystal was loaded in the X and Y directions, with a yield strain of ~8%. However, the HAP single crystal showed brittle behavior under uniaxial Z tension (normal to the basal plane), as the stress dropped significantly after the following peak stress at a strain of ~10%. Differences between the reported values in this work and the aforementioned study by Ching et al. could be due to different methods of solving (ab-initio vs molecular dynamics) and different model sizes (100s of atoms for ab-initio vs thousands of atoms for MD), with both having significant effect on the calculated strain and stress values.

![](./images/812602917826592769_4.jpg)

Figure 3: The stress-strain curves for the perfect HAP crystal loading in uniaxial tension along the x, y, and z axes at 10K and a strain rate of 1e10/s.

The overall mechanical behavior of monocrystalline HAP subjected to deformation can be viewed as a reflection of the behavior of individual bond types that comprise the crystal, since no defects or surface conditions are present. Given this assertion, the cohesiveness and shape of certain bond groups and overall bond lengths of each bond type were observed during loading. OVITO was used to measure bond lengths and observe discrete particle behavior directly (Stukowski, 2010). Cohesiveness and shape refer to initial polyhedral arrangement and order, including allowances for the effect of bond lengthening under load. The bond length considered the limit above which breakage occurred was equal to the initial bond length multiplied by one plus the failure strain of the crystal for the respective uniaxial loading being simulated. This is viewed as a conservative approximation of bond breakage, since all bond types present contribute to the cumulative failure strain in a crystal.

Given that ionic bonds do not rely on direct electron sharing, ionic interactions can persist beyond the range that covalent bonds can stretch to before failure. Thus, ionic bonds are suspected to contribute to the majority of strain at failure in the HAP crystal. The initial bond lengths in HAP were taken from Posner et al. (Posner et al., 1958), as shown in Table 3. To explain the observed tensile behavior in Figure 3, we intend to investigate the underlying deformation mechanisms for each load case.

Table 3: The bonds present in hexagonal HAP, listed with their length and primary bond type (Posner et al., 1958)

<table>
  <thead>
    <tr>
      <th>Bond</th>
      <th>Equilibrium Length (pm)</th>
      <th>Bond Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O-H</td>
      <td>95.5</td>
      <td>Covalent</td>
    </tr>
    <tr>
      <td>P-O(I)</td>
      <td>153.3</td>
      <td>Covalent</td>
    </tr>
    <tr>
      <td>P-O(II)</td>
      <td>154.4</td>
      <td>Covalent</td>
    </tr>
    <tr>
      <td>P-O(III)</td>
      <td>151.4</td>
      <td>Covalent</td>
    </tr>
    <tr>
      <td>Ca(I)-O(I)</td>
      <td>241.6</td>
      <td>Ionic</td>
    </tr>
    <tr>
      <td>Ca(I)-O(II)</td>
      <td>244.9</td>
      <td>Ionic</td>
    </tr>
    <tr>
      <td>Ca(I)-O(III)</td>
      <td>280.2</td>
      <td>Ionic</td>
    </tr>
    <tr>
      <td>Ca(II)-O(OH)</td>
      <td>235.4</td>
      <td>Ionic</td>
    </tr>
    <tr>
      <td>Ca(II)-O(I)</td>
      <td>271.2</td>
      <td>Ionic</td>
    </tr>
    <tr>
      <td>Ca(II)-O(II)</td>
      <td>235.6</td>
      <td>Ionic</td>
    </tr>
    <tr>
      <td>Ca(II)-O(III)</td>
      <td>236.7</td>
      <td>Ionic</td>
    </tr>
    <tr>
      <td>Ca(II)-O(III)</td>
      <td>251.1</td>
      <td>Ionic</td>
    </tr>
  </tbody>
</table>

Nanoscale deformation mechanisms associated with uniaxial X tension were found to include directionally-dependent bond breakage, where bonds aligned with the loading direction were found to break. Initial fracture was observed to be local to Ca(II) hexahedral arrangements surrounding hydroxide columns. Following the inception of plasticity at 6.5% strain, breakage of ionic Ca(I)-O(III) and Ca(II)-O(I) groups was observed prior to global crystal failure. Bond breakage and group deformation were observed for ionically bonded Ca(I)-O(I), Ca(I)-O(III),

Ca(II)-OH, Ca(II)-O(I), and the shorter of the two Ca(II)-O(III) bond species (see Fig. 2). Fig. 4 shows the breakage observed in these bond groups in a given fracture zone at 15.5% strain, i.e. the strain at the highest stress. Among the involved bond types, Ca(II)-OH contributes the most to the deformation at the fracture zone as shown in Fig. 4.

![](./images/812602917826592769_5.jpg)

Figure 4: Bond breakage observed in uniaxial X tension. Ca(I)-O(I) bonds, Ca(I)-O(III) bonds, Ca(II)-O(I) bonds, longer Ca(II)-O(III) bonds, and Ca(II)-OH bonds are shown at strains of $\varepsilon$=0, $\varepsilon$=0.155, and $\varepsilon$=0.175.

In uniaxial Y tension, bond breakage and group deformation were observed in ionic Ca(I)-O(I), Ca(I)-O(III), Ca(II)-O(I), and Ca(II)-O(II) bonds (see Fig. 2). Figure 5 shows the deformation in these bond groups.

![](./images/812602917826592769_6.jpg)

Figure 5: Bond breakage observed at the crystal failure point of 15.5% strain in uniaxial Y tension. Ca(I)-O(I), Ca(I)-O(III), Ca(II)-O(I), and Ca(II)-O(II) bonds are shown prior to applied strain (ε=0.00), at the inception of failure (ε=0.170), and following fracture (ε=0.190).

The superior mechanical properties compared to uniaxial X tension despite similar deformation mechanisms are postulated to be due to the maintenance of Ca(II)-OH bonds. These allow for the hexagonal arrangement of Ca(II) atoms to maintain position around the hydroxyl columns until large scale planar Ca(II)-O(II) bond fracture occurs. Fig. 6 a-h shows the atomic snapshots of a sample Ca(II)-OH column selected in the shear zone at the peak points and at about 2.5% strain after the peak points for uniaxial tension in X and Y directions, respectively.

![](./images/812602917826592769_7.jpg)

Figure 6: a. top view of Ca(II)-OH column in uniaxial x tension at ε=0.155. b. side view of Ca(II)-OH column in uniaxial x tension at ε=0.155. c. top view of Ca(II)-OH column in uniaxial x tension at ε=0.180. d. side view of Ca(II)-OH column in uniaxial x tension at ε=0.180. e. top view of Ca(II)-OH column in uniaxial y tension at ε=0.17. f. side view of Ca(II)-OH column in uniaxial y tension at ε=0.170. g. top view of Ca(II)-OH column in uniaxial y tension at ε=0.195. h. side view of Ca(II)-OH column in uniaxial y tension at ε=0.195.

Figure 7 shows the deformation mechanisms including the breakage and shape loss for various bonds when the model subjected to uniaxial Z strain. Consistent with tensile loading in the X and Y directions, no covalent bond group breakage or loss of shape was observed in uniaxial tension along the Z direction. The inception of failure for Z-direction uniaxial tension is not accompanied by the fracture of any bond groups with X-Y planar character, i.e. Ca(II)-O(I), Ca(II)-O(II), Ca(II)-OH, and Ca(I)-O(III) bonds; instead it is marked by fracture of the Ca(I)-O(II) groups and both variants of the Ca(II)-O(III) group. This is consistent with the directional bond breakage observed for X and Y uniaxial tension, since the named bond groups are highly aligned with Z axis. The bond breakage described in all tensile loading directions was antedated by concomitant rotation of the phosphate groups to which the Ca-O bonds are attached, which agrees with the ab initio findings of Ching et al. (Ching et al., 2009).

![](./images/812602917826592769_8.jpg)

Figure 7: Bond breakage observed at the crystal failure point of 8.0% strain in uniaxial z tension. Ca(I)-O(II), Ca(I)-O(III), longer Ca(II)-O(III), and shorter Ca(II)-O(III) bonds are shown prior to applied strain (ε=0.0), at the inception of failure (ε=0.08), and following fracture (ε=0.10).

### 3.2. Uniaxial compression

Fig. 8 shows the stress-strain curves for the uniaxial compression at a strain rate of 1e10 /s and the temperature of 10 K along the X, Y, and Z axes. Similar to uniaxial tension, the elastic modulus is highest in the Z direction ($E_z = 175$ GPa), while X and Y show similar values ($E_x = 143$ GPa, $E_y = 150$ GPa). The highest strength and strain at failure were observed for the Z direction. The failure strength was higher for Y than X, although the observed failure strains were similar. The stress-strain curves for compression along the X and Z directions show significant change in the slope prior to fracture. In contrast with uniaxial tension, failure in uniaxial compression was characterized by bond shortening and angular reduction (when applicable) between chemical species. Due to the largely ionically bonded nature of HAP,

columbic repulsion is believed to be the main cause of failure in compression. This mechanism is further discussed below.

![](./images/812602917826592769_9.jpg)

Figure 8: The stress-strain curves for the perfect HAP crystal loading in uniaxial compression along the x, y, and z axes at 10K and a strain rate of 1e10/s. An inset of the elastic region is shown to differentiate between the directional stiffnesses prior to 5% linear strain.

In uniaxial X compression, the observed loss in elastic modulus and subsequent re-strengthening of the material prior to the inception of failure was found to be due to angular rotation and re-alignment between the shorter Ca(II)-O(III) bond species positioned along the X axis. It is believed that the temporary loss of bond alignment along the X-axis is responsible for the accompanying decrease in the elastic modulus. This effect was observed to be global. Figs. 9 and 10 show the progression of realignment of these groups prior to the inception of failure.

![](./images/812602917826592769_10.jpg)

Figure 9: The x-z planar view of the progression of angle change and realignment in Ca(II)(blue)-O(III)(red) groups. Note that as deformation increases from left to right, the bonds increase in angle.

![](./images/812602917826592769_11.jpg)

Figure 10: The x-y planar view of the progression of positional change in Ca(II)-O(III) groups. Note that as deformation increases from left to right, the oxygen atoms (red) move about their bonded calcium atoms (blue) while the calcium atoms are stationary.

The inception of failure, at the strain of 0.135, for compression loading in X direction was found to be associated with tensile strain induced in Ca(I)-O(III) bonds as compressive strain caused rotation of neighboring phosphate groups. Phosphate group rotation caused the Ca(I) column between three neighboring phosphates to divide into two sections. This dissociation did not show calcium atoms shifting with the rotating phosphate group in question as they shifted with the other two phosphate groups. As a result, likely fracture of the ionic Ca(I)-O(III) bond with the rotated phosphate was observed, signaling material failure. Figure 11 illustrates this mechanism.

![](./images/812602917826592769_12.jpg)

Figure 11: Bond breakage at an applied compressive strain of (a) 0, (b) 0.075, (c) 0.135 (the peak point), and (d) 0.145. observed in Ca(I)-O(III) groups due to Ca(II)-O(III) motion inducing phosphate group rotation during X compression. The phosphate groups are not shown for the sake of higher clarity.

The inception of failure in the crystal when compressed in Y direction was found to be global. Increased atomic shear strain was observed on the Ca(II)-O(II) bond groups with Y-axis

bond orientation throughout loading. Material failure was attributed to failure of these groups.
The atomic snapshots at the progressive compressive strains in these groups leading to, at, and
after the inception of failure are shown in Figure 12.

![](./images/812602917826592769_13.jpg)

Figure 12: Ortho view of Ca(II)-O(II) groups during Y compression. A. Prior to applied compressive strain. B. At an applied compressive strain of 0.135. C. At an applied compressive strain of 0.145. D. At an applied compressive strain of 0.150

Upon application of compressive strain in the Y direction, the shift of Ca(II) atoms which
have Y-oriented Ca(II)-O(II) bonds is apparent (see Fig. 13). These bonds are driven most
directly in the direction of the compressive load due to their orientation but do not break prior to
global failure. This causes the attached phosphate groups to rotate into the nearest neighbor
phosphate groups, resulting in columbic repulsion between oxygen atoms and sudden global
failure.

![](./images/812602917826592769_14.jpg)

Figure 13:The progression of hexagonal Ca(II) atomic orientation skewing as y compressive deformation proceeds. Note that the largest displacement prior to failure occurs in the Ca(II) atoms with y-oriented Ca(II)-O(II) bonds (circled), indicating that these bonds bear much of the compressive load prior to failure. Note also the rotation of those phosphate groups into one another as deformation progresses, causing columbic repulsion between phosphate oxygens.

Under applied uniaxial Z compressive loading, monocrystalline HAP exhibits relatively
uniform atomic shear strain globally. The small decrease in the stiffness after a strain of 0.06 was
observed to be followed by a slow stiffening prior to the inception of failure. Since no significant
Poisson effect resulting in planar X-Y bond deformation was observed, the deformation behavior

of the crystal can be attributed only to bonds with significant Z orientation in this case. The change in stiffness is attributed to a significant change in angle of the shorter Ca(II)-O(III) bond species from the strain of 6.5% up to the strain at the peak point of 0.22 (see Fig. 14). These are the species that are most aligned with the Z orientation, so increasing misalignment along Z-orientation was believed to soften the global response to applied strain. Furthermore, large reduction in the bond angle was also observed globally in Ca(I)-O(I) and Ca(I)-O(II) bond species (see Figs. 15-16). The stiffening just before the inception of the failure is due to slowly increasing columbic repulsion as bond species end groups of similar charge, i.e. O and Ca ions, are forced closer together. Worth noting is that the end-to-end distance of the longer Ca(II)-O(III) bond groups did not change appreciably before failure, although the observed change in vector azimuthal angle throughout deformation seems to indicate some end group twisting during deformation (see Fig. 17). This twisting behavior as opposed to outright angle closure and end group distance reduction may be due to the fact that the longer Ca(II)-O(III) bonds have the least direct z orientation at equilibrium among the studied groups.

![](./images/812602917826592769_15.jpg)

Figure 14: Shorter Ca(II)-O(III) bonds with their respective end group separations and perspective azimuthal angles shown for A. $\varepsilon$=0.0. B. $\varepsilon$=0.055. C. $\varepsilon$=0.22.

![](./images/812602917826592769_16.jpg)

Figure 15: Ca(I)-O(I) bonds with their respective end group separations and perspective azimuthal angles shown for A. $\varepsilon$=0.0. B. $\varepsilon$=0.055. C. $\varepsilon$=0.22.

![](./images/812602917826592769_17.jpg)

Figure 16: Ca(I)-O(II) bonds with their respective end group separations and perspective azimuthal angles shown for A. $\varepsilon$=0.0. B. $\varepsilon$=0.055. C. $\varepsilon$=0.22.

![](./images/812602917826592769_18.jpg)

Figure 17: Longer Ca(II)-O(III) bonds with their respective end group separations and perspective azimuthal angles shown for A. $\varepsilon$=0.0. B. $\varepsilon$=0.055. C. $\varepsilon$=0.22.

When viewed as a bulk crystal, the continued flattening of oxygen groups between planes of phosphorus atoms is visible until delocalized fracture occurs throughout the crystal. These oxygen groups appear to flatten as the polyhedra undergo angular changes at their vertices due to the applied Z compressive strain. Figure 18 a-c show the YZ views of the HAP crystal at zero strain, right before the inception of failure, and after the failure, respectively.

![](./images/812602917826592769_19.jpg)

Figure 14: The crystallographic YZ plane (a) prior to applied Z compressive strain; $\varepsilon$=0.00, (b) just before the inception of failure; $\varepsilon$=0.22, and (c) right after failure; $\varepsilon$=0.225. Oxygen atoms which sit between planar atom arrays due to polyhedral shape are shown in red.

Both Fig. 3 and Fig. 8 show significant anisotropy with regards to stiffness, fracture (failure) strain, and fracture (failure) strength of a HAP single crystal between the basal (normal to Z direction) and side planes. This trend is in a good agreement with the ab-initio calculations of tensile loading (Ching et al., 2009) and the nanoindentation experiments (Saber-Samandari and Gross, 2009; Viswanath et al., 2007; Zamiri and De, 2011) on HAP single crystals. Comparing Fig. 3 and 8, one can also observe a significant compression/tension asymmetry in all loading directions. In both tension and compression, the elastic modulus is highest in the Z direction, i.e. normal to the basal plane. However, the lowest fracture strength and strain values for the crystal in tension are in the Z direction, with the opposite being true for compression. This asymmetry can be best explained by considering that a large number of bonds throughout the crystal are oriented at least partially along the Z axis. Therefore, a large number of bonds participate in the constitutive behavior of the crystal when it is loaded in the Z direction. This gives the Z direction a higher stiffness than X or Y for either tensile or compression loadings. Because bond stretching and breakage is the cause of tensile failure and columbic repulsion is the cause of compressive failure, the large number of bonds with Z orientation contribute heavily in both cases. Bonds that are significantly oriented with the Z axis stretch the most quickly under tensile loading, but do not have like-charged species getting close to each other in compression until the bond is reduced sufficiently from the initial angle. This results in much larger fracture strain in Z direction when the model is under compression, i.e. 0.22 in comparison against 0.08 in tension. Experimental data for uniaxial loading on HAP single crystal are lacking. However, this trend is in good agreement with the common behavior of ceramics, i.e. lower fracture strains under tension.

## 4. Conclusions
Nanoscale deformation mechanisms in bulk stoichiometric hexagonal hydroxyapatite were studied using molecular dynamics simulation in LAMMPS. Both uniaxial tension and compression were considered.

Different behavior in HAP single crystals between tension and compression is directly attributable to directionally dependent nanoscale deformation mechanisms. In tension, failure of ionic bonds groups due to applied strain caused crystal failure in each loading case. Primary X direction tensile failure was associated with breakage of ionic Ca(I)-O(I), Ca(I)-O(III), Ca(II)-OH, Ca(II)-O(I), and the shorter of the two Ca(II)-O(III) bond species. Y tensile failure was associated with bond breakage in ionic Ca(I)-O(I), Ca(I)-O(III), Ca(II)-O(I), and Ca(II)-O(II) bonds. Z tensile failure was marked by fracture of the Ca(I)-O(II) groups and both variants of the Ca(II)-O(III) group. The elastic tensile modulus for Z was highest, followed by Y and X.

In compression, columbic repulsion between ionic groups of similar charge ultimately caused crystal failure in every loading case, although preceding bond behavior varied by loading case. In X uniaxial compression, failure was caused by the tensile strain induced in Ca(I)-O(III) bonds as compressive strain caused rotation of neighboring phosphate groups. Failure in Y

uniaxial compression was attributed to breaking of Ca(II)-O(II) bond groups with Y direction bond orientation. Z uniaxial compressive failure was linked to columbic repulsion as Ca(I)-O(I), Ca(I)-O(II), and shorter Ca(II)-O(III) groups experienced high bond angle reduction and decreasing distance between like-charge end groups. The elastic modulus in compression was highest for Z, followed by Y and X.

The asymmetries seen between uniaxial tension and compression were most disparate for the applied strain in the Z direction as opposed to X and Y. This is largely due to the aforementioned failure mechanisms in each case. Bonds with high Z orientation at equilibrium were found to undergo low strain to failure in tension, but significant strain in compression due to the opportunity for large bond angle reduction prior to repulsive failure.

## Acknowledgements
We would like to thank the GAEA high performance computing staff at NIU for their support of this project. The authors also greatly acknowledge Dr. Sahar Vahabzadeh from the Department of Mechanical Engineering, Northern Illinois University for her valuable insights.

## References
An, S.-H., Matsumoto, T., Miyajima, H., Nakahira, A., Kim, K.-H., Imazato, S., 2012. Porous zirconia/hydroxyapatite scaffolds for bone reconstruction. Dent. Mater. 28, 1221-1231. https://doi.org/10.1016/j.dental.2012.09.001

Ching, W.Y., Rulis, P., Misra, A., 2009. Ab initio elastic properties and tensile strength of crystalline hydroxyapatite. Acta Biomater. 5, 3067-3075. https://doi.org/10.1016/j.actbio.2009.04.030

Choudhury, P., Agrawal, D.C., 2011. Sol-gel derived hydroxyapatite coatings on titanium substrates. Surf. Coat. Technol. 206, 360-365. https://doi.org/10.1016/j.surfcoat.2011.07.031

Costa, D.O., Prowse, P.D.H., Chrones, T., Sims, S.M., Hamilton, D.W., Rizkalla, A.S., Dixon, S.J., 2013. The differential regulation of osteoblast and osteoclast activity by surface topography of hydroxyapatite coatings. Biomaterials 34, 7215-7226. https://doi.org/10.1016/j.biomaterials.2013.06.014

Deville, S., Saiz, E., Tomsia, A.P., 2006. Freeze casting of hydroxyapatite scaffolds for bone tissue engineering. Biomaterials 27, 5480-5489. https://doi.org/10.1016/j.biomaterials.2006.06.028

Emami, F.S., Puddu, V., Berry, R.J., Varshney, V., Patwardhan, S.V., Perry, C.C., Heinz, H., 2014. Force Field and a Surface Model Database for Silica to Simulate Interfacial Properties in Atomic Resolution. Chem. Mater. 26, 2647-2658. https://doi.org/10.1021/cm500365c

Ewald, P.P., 1921. Die Berechnung optischer und elektrostatischer Gitterpotentiale. Ann. Phys. 369, 253-287. https://doi.org/10.1002/andp.19213690304

Gao, C., Deng, Y., Feng, P., Mao, Z., Li, P., Yang, B., Deng, J., Cao, Y., Shuai, C., Peng, S., 2014. Current progress in bioactive ceramic scaffolds for bone repair and regeneration. Int. J. Mol. Sci. 15, 4714-4732. https://doi.org/10.3390/ijms15034714

Gilmore, R.S., Katz, J.L., 1982. Elastic properties of apatites. J. Mater. Sci. 17, 1131-1141. https://doi.org/10.1007/BF00543533

Harun, W.S.W., Asri, R.I.M., Alias, J., Zulkifli, F.H., Kadirgama, K., Ghani, S.A.C., Shariffuddin, J.H.M., 2018. A comprehensive review of hydroxyapatite-based coatings adhesion on metallic biomaterials. Ceram. Int. 44, 1250-1268. https://doi.org/10.1016/j.ceramint.2017.10.162

Heinz, H., 2016. Adsorption of biomolecules and polymers on silicates, glasses, and oxides: mechanisms, predictions, and opportunities by molecular simulation. Curr. Opin. Chem. Eng. 11, 34-41.
https://doi.org/10.1016/j.coche.2015.12.003

Heinz, H., Lin, T.-J., Kishore Mishra, R., Emami, F.S., 2013. Thermodynamically Consistent Force Fields for the Assembly of Inorganic, Organic, and Biological Nanostructures: The INTERFACEForce Field. Langmuir 29, 1754-1765. https://doi.org/10.1021/la3038846

Huang, W., Restrepo, D., Jung, J.-Y., Su, F.Y., Liu, Z., Ritchie, R.O., McKittrick, J., Zavattieri, P., Kisailus, D., 2019. Multiscale Toughening Mechanisms in Biological Materials and BioinspiredDesigns. Adv. Mater. 0, 1901561. https://doi.org/10.1002/adma.201901561

Hughes, J.M., Rakovan, J., 2002. The Crystal Structure of Apatite, Ca5(PO4)3(F,OH,Cl). Rev. Mineral.Geochem. 48, 1-12. https://doi.org/10.2138/rmg.2002.48.1

Kay, M.I., Young, R.A., Posner, A.S., 1964. Crystal Structure of Hydroxyapatite. Nature 204, 1050.
https://doi.org/10.1038/2041050a0

Kwon, Y.W., Clumpner, B.R., 2018. Multiscale modeling of human bone. Multiscale Multidiscip. Model.Exp. Des. 1, 133-143. https://doi.org/10.1007/s41939-018-0013-0

Lacefield, W.R., 1988. Hydroxyapatite Coatings. Ann. N. Y. Acad. Sci. 523, 72-80.
https://doi.org/10.1111/j.1749-6632.1988.tb38501.x

Leeuw, N.H. de, Bowe, J.R., Rabone, J.A.L., 2006. A computational investigation of stoichiometric and calcium-deficient oxy- and hydroxy-apatites. Faraday Discuss. 134, 195-214.
https://doi.org/10.1039/B602012G

Libonati, F., Nair, A.K., Vergani, L., Buehler, M.J., 2013. Fracture mechanics of hydroxyapatite single crystals under geometric confinement. J. Mech. Behav. Biomed. Mater. 20, 184-191.
https://doi.org/10.1016/j.jmbbm.2012.12.005

Lin, T.-J., 2013. Force Field Parameters and Atomistic Surface Models for Hydroxyapatite and Analysis of Biomolecular Adsorption at Aqueous Interfaces. University of Akron.

Lin, T.-J., Heinz, H., 2016. Accurate Force Field Parameters and pH Resolved Surface Models for Hydroxyapatite to Understand Structure, Mechanics, Hydration, and Biological Interfaces. J.Phys. Chem. C 120, 4975-4992. https://doi.org/10.1021/acs.jpcc.5b12504

Maghsoudi-Ganjeh, M., Lin, L., Wang, X., Zeng, X., 2019. Computational investigation of ultrastructural behavior of bone using a cohesive finite element approach. Biomech. Model. Mechanobiol. 18,463-478. https://doi.org/10.1007/s10237-018-1096-6

Menéndez-Proupin, E., Cervantes-Rodríguez, S., Osorio-Pulgar, R., Franco-Cisterna, M., Camacho- Montes, H., Fuentes, M.E., 2011. Computer simulation of elastic constants of hydroxyapatite and fluorapatite. J. Mech. Behav. Biomed. Mater. 4, 1011-1020.
https://doi.org/10.1016/j.jmbbm.2011.03.001

Mygind, T., Stiehler, M., Baatrup, A., Li, H., Zou, X., Flyvbjerg, A., Kassem, M., Bünger, C., 2007. Mesenchymal stem cell ingrowth and differentiation on coralline hydroxyapatite scaffolds.Biomaterials 28, 1036-1047. https://doi.org/10.1016/j.biomaterials.2006.10.003

Nair, A.K., Gautieri, A., Chang, S.-W., Buehler, M.J., 2013. Molecular mechanics of mineralized collagen fibrils in bone. Nat. Commun. 4, ncomms2720. https://doi.org/10.1038/ncomms2720

Ong, J.L., Chan, D.C., 2000. Hydroxyapatite and their use as coatings in dental implants: a review. Crit.Rev. Biomed. Eng. 28, 667-707.

Ou, X., Han, Q., 2014. Molecular dynamics simulations of the mechanical properties of monoclinic hydroxyapatite. J. Mol. Model. 20, 2505. https://doi.org/10.1007/s00894-014-2505-0

Pawłowski, L., 2018. Synthesis, Properties and Applications of Hydroxyapatite, in: Industrial Chemistry of Oxides for Emerging Applications. John Wiley & Sons, Ltd, pp. 311-352.
https://doi.org/10.1002/9781119424079.ch7

Plimpton, S., 1995. Fast Parallel Algorithms for Short-Range Molecular Dynamics. J. Comput. Phys. 117,1-19. https://doi.org/10.1006/jcph.1995.1039

Posner, A.S., Perloff, A., Diorio, A.F., 1958. Refinement of the hydroxyapatite structure. Acta Crystallogr. 11, 308-309. https://doi.org/10.1107/S0365110X58000815

Qin, Z., Gautieri, A., Nair, A.K., Inbar, H., Buehler, M.J., 2012. Thickness of Hydroxyapatite Nanocrystal Controls Mechanical Properties of the Collagen-Hydroxyapatite Interface. Langmuir 28, 1982-1992. https://doi.org/10.1021/la204052a

Ramesh, N., Moratti, S.C., Dias, G.J., 2018. Hydroxyapatite-polymer biocomposites for bone regeneration: A review of current trends. J. Biomed. Mater. Res. B Appl. Biomater. 106, 2046-2057. https://doi.org/10.1002/jbm.b.33950

Saber-Samandari, S., Gross, K.A., 2009. Micromechanical properties of single crystal hydroxyapatite by nanoindentation. Acta Biomater. 5, 2206-2212. https://doi.org/10.1016/j.actbio.2009.02.009

Salehinia, I., Lawrence, S.K., Bahr, D.F., 2013. The effect of crystal orientation on the stochastic behavior of dislocation nucleation and multiplication during nanoindentation. Acta Mater. 61, 1421-1431. https://doi.org/10.1016/j.actamat.2012.11.019

Snyders, R., Music, D., Sigumonrong, D., Schelnberger, B., Jensen, J., Schneider, J.M., 2007. Experimental and ab initio study of the mechanical properties of hydroxyapatite. Appl. Phys. Lett. 90, 193902. https://doi.org/10.1063/1.2738386

Stock, S.R., 2015. The Mineral-Collagen Interface in Bone. Calcif. Tissue Int. 97, 262-280. https://doi.org/10.1007/s00223-015-9984-6

Stukowski, A., 2010. Visualization and analysis of atomistic simulation data with OVITO-the Open Visualization Tool. Model. Simul. Mater. Sci. Eng. 18, 015012. https://doi.org/10.1088/0965-0393/18/1/015012

Szczes, A., Hołysz, L., Chibowski, E., 2017. Synthesis of hydroxyapatite for biomedical applications. Adv. Colloid Interface Sci., Recent nanotechnology and colloid science development for biomedical applications 249, 321-330. https://doi.org/10.1016/j.cis.2017.04.007

Viswanath, B., Raghavan, R., Ramamurty, U., Ravishankar, N., 2007. Mechanical properties and anisotropy in hydroxyapatite single crystals. Scr. Mater. 57, 361-364. https://doi.org/10.1016/j.scriptamat.2007.04.027

White, A.A., Best, S.M., Kinloch, I.A., 2007. Hydroxyapatite-Carbon Nanotube Composites for Biomedical Applications: A Review. Int. J. Appl. Ceram. Technol. 4, 1-13. https://doi.org/10.1111/j.1744-7402.2007.02113.x

Yashima, M., Yonehara, Y., Fujimori, H., 2011. Experimental Visualization of Chemical Bonding and Structural Disorder in Hydroxyapatite through Charge and Nuclear-Density Analysis. J. Phys. Chem. C 115, 25077-25087. https://doi.org/10.1021/jp208746y

Zamiri, A., De, S., 2011. Mechanical properties of hydroxyapatite single crystals from nanoindentation data. J. Mech. Behav. Biomed. Mater. 4, 146-152. https://doi.org/10.1016/j.jmbbm.2010.11.001

<br>

### Declaration of interests

☒ The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

☐The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:

<table><tbody><tr><td></td></tr></tbody></table>
