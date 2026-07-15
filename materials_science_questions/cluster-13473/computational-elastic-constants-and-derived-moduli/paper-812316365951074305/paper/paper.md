![](./images/812316365951074305_1.jpg)

Available online at www.sciencedirect.com
![](./images/812316365951074305_2.jpg)
Polymer 46 (2005) 553–562

![](./images/812316365951074305_3.jpg)
www.elsevier.com/locate/polymer

# Modeling of the mechanical properties of nanoparticle/polymer composites

G.M. Odegard$^{\text{a},*}$, T.C. Clancy$^{\text{b}}$, T.S. Gates$^{\text{c}}$

$^{\text{a}}$Department of Mechanical Engineering—Engineering Mechanics, Michigan Technological University, Houghton, MI 49931, USA
$^{\text{b}}$National Institute of Aerospace, 144 Research Drive, Hampton, VA 23666, USA
$^{\text{c}}$NASA Langley Research Center, MS 188E, Hampton, VA 23681, USA

Received 23 July 2004; received in revised form 11 November 2004; accepted 11 November 2004
Available online 2 December 2004

## Abstract

A continuum-based elastic micromechanics model is developed for silica nanoparticle/polyimide composites with various nanoparticle/polyimide interfacial treatments. The model incorporates the molecular structures of the nanoparticle, polyimide, and interfacial regions, which are determined using a molecular modeling method that involves coarse-grained and reverse-mapping techniques. The micromechanics model includes an effective interface between the polyimide and nanoparticle with properties and dimensions that are determined using the results of molecular dynamics simulations. It is shown that the model can be used to predict the elastic properties of silica nanoparticle/polyimide composites for a large range of nanoparticle radii, 10–10,000 Å. For silica nanoparticle radii above 1000 Å, the predicted properties are equal to those predicted using the standard Mori–Tanaka micromechanical approach, which does not incorporate the molecular structure. It is also shown that the specific silica nanoparticle/polyimide interface conditions have a significant effect on the composite mechanical properties for nanoparticle radii below 1000 Å.

© 2004 Elsevier Ltd. All rights reserved.

Keywords: Molecular dynamics; Nanoparticles; Nanocomposites

---

## 1. Introduction

In the design and development of Unmanned Aerial Vehicles (UAVs) at the National Aeronautics and Space Administration, the primary requirements are long-duration, high-altitude flights. These requirements necessitate the use of lightweight, durable materials for most of the structural components of these UAVs. Polyimide-based composites are excellent candidates for this purpose due to their resistance to degradation under various environmental conditions. Furthermore, the use of nanostructured reinforcement in polymers has the potential to provide increases in the mechanical properties relative to larger-scale reinforcements that are currently used for aerospace applications, such as carbon fibers [1–3]. To facilitate the development of nanostructured polyimide composite materials for this purpose, constitutive relationships must be developed that predict the bulk mechanical properties of the materials as a function of the molecular structure of the polyimide and reinforcement. These constitutive relationships can be used to influence the design of these materials before they are synthesized.

In the past few years, a considerable amount of research has been conducted to examine the modeling of mechanical properties of polymer composites with nanoscale reinforcement. The majority of this work has focused on carbon nanotube-reinforced polymers [4–9]. Even though it has been shown that these materials have the potential to have excellent mechanical properties, the relatively high costs of development and manufacturing of nanotube/polymer composites has been prohibitive. A lower cost approach is the use of clays and particles in the polymer. Several efforts have focused on the modeling of mechanical properties of nanoclay-reinforced polymer composites [10] and nanoparticle-reinforced polymer composites [11,12]. These modeling efforts have demonstrated the need for the development

* Corresponding author. Tel.: +1 906 487 2329; fax: +1 906 487 2822.
E-mail address: gmodegar@mtu.edu (G.M. Odegard).

0032-3861/$ - see front matter © 2004 Elsevier Ltd. All rights reserved.
doi:10.1016/j.polymer.2004.11.022

of a model that will predict the mechanical properties of nanoparticle/polyimide composites as a function of the nanoparticle size and volume fraction, and the molecular structure of the nanoparticle/polyimide interface.

In the present paper, a continuum-based constitutive model was developed for silica nanoparticle/polyimide composites with four different nanoparticle/polyimide interfacial treatments. The model incorporates the molecular structure of the nanoparticle, polyimide, and interfacial region. The model was used to examine the elastic properties of the composite as a function of nanoparticle radius, ranging from $6\ \text{\AA}$ to $1\ \mu\text{m}$, and particle/matrix interfacial treatments, including untreated nanoparticles, nanoparticles with attached hydroxyl and phenoxybenzene groups, and nanoparticles attached to the polyimide via covalent bonding.

## 2. Materials
The constitutive models developed in this study are for four variations of silica ($\text{SiO}_2$) nanoparticle-reinforced polyimide composites. The silica had an $\alpha$-quartz crystal structure, and the nanoparticles were nearly spherical in shape, with an approximate radius of $6\ \text{\AA}$. The polymer modeled was based on a polyimide from 3,3',4,4'-biphenyltetracarboxylic dianhydride (BPDA) and 1,3-bis(4-aminophenoxy)benzene (APB) monomers (Fig. 1) [13,14]. The polymer was modeled as having an amorphous molecular structure. The first variation of the composite had a silica nanoparticle without surface treatment that was not bonded to the surrounding polyimide. The second variation had the nanoparticle surface comprised of hydroxyl groups that were bonded to silicon atoms. In this variation, there were no covalent bonds between the polyimide molecules and the nanoparticle. The third variation had phenoxybenzene groups ($-\text{C}_6\text{H}_4-\text{O}-\text{C}_6\text{H}_5$) chemically bonded to the surface of the nanoparticle, and the phenoxybenzene groups were not directly bonded to the polyimide matrix. The fourth variation had a hydroxylated surface (as in the second variation) with the nanoparticle covalently bonded (functionalized) to the surrounding polyimide molecules. In addition to the four composite systems, the pure silica and the pure polyimide materials were examined.

$$
\mathrm{O}=\mathrm{C}_{-\mathrm{N}}^{\mathrm{O}}-\mathrm{C}_{6} \mathrm{H}_{4}-\mathrm{C}_{6} \mathrm{H}_{4}-\mathrm{C}_{-\mathrm{N}}^{\mathrm{O}}=\mathrm{O}-\mathrm{C}_{6} \mathrm{H}_{4}-\mathrm{O}-\mathrm{C}_{6} \mathrm{H}_{4}-\mathrm{O}-\mathrm{C}_{6} \mathrm{H}_{4}-\mathrm{CH}_{3}
$$

Fig. 1. Schematic illustration of BPDA (1,3,4) APB polyimide monomer unit.

## 3. Molecular structure
The first step in establishing structure-property relations of nanostructured materials is the determination of the molecular structure of the nanoparticle, polyimide matrix, and nanoparticle/polyimide interfacial area. The equilibrium molecular structures of representative volume elements (RVEs) of the six material systems were determined using molecular modeling techniques. Atomistic molecular modeling techniques have been in use for several decades to calculate mechanical properties of polymers [15]. Although modern computational limitations restrict the number of atoms in a typical simulated system, and hence the molecular weight of the polymer chains which can be simulated, mechanical properties consistent with experimental results can usually be obtained. The primary challenge in polymer molecular modeling is the generation of suitably equilibrated atomistic polymer molecular structures. To this end, multi-scale modeling techniques are often used to establish the molecular structures. For this study, the molecular structures were prepared with the aid of a reverse-mapping procedure from a coarse-grained model [16]. The methods are similar to those previously employed for multi-scale polymer modeling [17,18]. A brief summary of the method is given here.

For each polyimide molecule, a linked vector model was used to represent the rigid rings that comprise the polyimide backbone (Fig. 2). The linked vectors followed the contour of the molecule. The parameters used for this model consisted of angular distributions between consecutive vectors and long-range forces between beads placed along the midpoint of each vector. These parameters were estimated from molecular dynamics (MD) simulation of the polyimide monomers with the CVFF force field [19]. The centroids of the beads placed at the midpoint of each vector were the centers for interaction forces between non-adjacent beads along the chain of the polymer and between beads on different chains. Additional details on this procedure are presented elsewhere [20].

Once the coarse-grained model for the single polyimide molecule was established, it was subsequently used to assemble the coarse-grained bulk model with multiple polymer molecules and the nanoparticle. The coarse-grained polymers were initially placed as random walk chains inside a simulation box (with periodic boundary conditions) close to their bulk density. In this initial

![](./images/812316365951074305_4.jpg)

Fig. 2. Depiction of the mapping of the atomistic polymer model to the coarse-grained linked vector model.

placement, only the angular distributions between adjacent vectors along the chain were considered. Monte Carlo simulation was used to equilibrate the chains from their initial starting configuration. The nanoparticle was modeled as an effective hard sphere. As the Monte Carlo simulation proceeded, the long-range energy interactions established the excluded volume characteristics of the bulk polymer model. The repulsive interaction of the hard sphere with the polymer excluded the polymer chains from this region. The bulk polymer model consisted of seven chains of polymers each composed of 10 of the repeat units shown in Fig. 1. This chain length is typical for MD simulations of polymers. The simulation box was a cube of side length $42\ \mathring{A}$ with a hard sphere having a diameter of $15\ \mathring{A}$. The periodic box dimensions were chosen to allow the polymer to be close to the equilibrium bulk density. The simulation ran at 650 K until relaxation of the autocorrelation function of the end vectors was achieved and the average centers of mass were displaced a distance greater than the average radii of gyration squared. After sufficient equilibration with the coarse-grained Monte Carlo model, the chains were reverse-mapped by replacing the deleted atoms back into position along the vectors of the coarse-grained model. The nanoparticle was placed in the cavity that resulted from the effective hard sphere in the coarse-grained simulation. The resulting atomistic structures were subsequently minimized by the following procedure. A short energy minimization was applied to the structures. This was followed by constant-pressure MD simulation for 200 ps at 300 K and 1 atm. This constant-pressure MD simulation allowed the atomistic structures to relax to the equilibrium density. The employed algorithm preserved the cubic structure of the simulation box while allowing the box size to change. The final periodic boundary box size varied from 37.6 to $39.9\ \mathring{A}$ on a side depending on the nanoparticle involved. These equilibrated structures were then subjected to a final energy minimization with the criteria of convergence of $0.01\ \text{kcal/(mol}\ \mathring{A}\text{)}$. The functionalized structure was constructed by inserting an oxygen atom covalently bonded to a silicon atom in the nanoparticle and a nearby carbon atom in the polyimide. A total of 10 chemical bonds were inserted between the silica particle and the polymer matrix. The structure was then subjected to a molecular mechanics-based energy minimization [21] using the CVFF force field [19]. The pure polyimide matrix was generated using the same procedure as with the composite materials without the hard sphere particle in the coarse-grained simulation. After the constant pressure MD simulation, the density of the pure polyimide matrix was $1.33\ \text{g/cm}^3$. This density is a reasonable value for polyimides [22].

The resulting RVEs of the molecular structures for the four composite systems are shown in Figs. 3-6. The left-hand side of Figs. 3-6 shows the silica nanoparticle, and the right-hand side shows the particle in the polyimide matrix. The various surface treatments are shown on the nanoparticle in each figure. In Fig. 6 an example of the chemical bonding between the nanoparticle and the matrix is shown. For each of the four composite molecular models, the radial density profiles of the nanoparticle and polymer (including the polyimide and interfacial molecules) were also determined and plotted in Fig. 7 as a function of the radial distance from the center of the nanoparticle. In Fig. 7, the full magnitudes of the nanoparticle densities are not shown since only the nanoparticle density drop-off and the polymer densities are necessary in the micromechanical model development in this paper. The density of the core structure of the nanoparticle for all four materials remained at the value of the quartz structure from which it was derived $(2.65\ \text{g/cm}^3)$.

![](./images/812316365951074305_5.jpg)

Fig. 3. Molecular model of silica nanoparticle/polyimide composite.

## 4. Elastic constants

The mechanical behavior of the molecular systems was described using continuum mechanics. Since the molecular system has a discrete (not continuous) structure, the model is an equivalent-continuum model [23] in which the overall

![](./images/812316365951074305_6.jpg)

Fig. 4. Molecular model of hydroxylated silica nanoparticle/polyimide composite.

![](./images/812316365951074305_7.jpg)

Fig. 5. Molecular model of phenoxybenzene silica nanoparticle/polyimide composite.

mechanical response of a RVE to an applied set of boundary conditions is equivalent to the response of the molecular system RVE subjected to the same set of boundary conditions. The equivalent-continuum constitutive equation for the materials considered herein is devel- oped below.

It was assumed that the equivalent-continuum had a linear-elastic constitutive behavior. The generalized constitutive equation of the equivalent continuum is

$$\sigma_{i j}=C_{i j k l} \varepsilon_{k l} \tag{1}$$

where $\sigma_{i j}$ are the components of the stress tensor $(i, j=$ $1,2,3), C_{i j k l}$ are the components of the linear-elastic stiffness tensor, $\varepsilon_{i j}$ are the components of the strain tensor, and the summation convention associated with repeated subscripted indices is used. It was further assumed that the composite, pure polymer, and pure silica RVEs had isotropic material symmetry. The composite was assumed isotropic because of the presence of spherical reinforcement. Therefore, after

![](./images/812316365951074305_8.jpg)

Fig. 6. Molecular model of functionalized silica nanoparticle/polyimide composite. An example of the bonding to the matrix is illustrated at the top of the nanoparticle.

![](./images/812316365951074305_9.jpg)

Fig. 7. Radial density profiles of nanoparticle and polyimide. For the phenoxybenzene silica/polyimide composite, the density includes the polyimide and phenoxybenzene molecules.

expansion, Eq. (1) can be expressed as:

$$
\begin{aligned}
\sigma_{11} & =C_{11} \varepsilon_{11}+C_{12} \varepsilon_{22}+C_{12} \varepsilon_{33}, \\
\sigma_{22} & =C_{12} \varepsilon_{11}+C_{11} \varepsilon_{22}+C_{12} \varepsilon_{33}, \\
\sigma_{33} & =C_{12} \varepsilon_{11}+C_{12} \varepsilon_{22}+C_{11} \varepsilon_{33}, \\
\sigma_{44} & =1 / 2\left(C_{11}-C_{12}\right) \gamma_{23}, \\
\sigma_{55} & =1 / 2\left(C_{11}-C_{12}\right) \gamma_{13}, \\
\sigma_{66} & =1 / 2\left(C_{11}-C_{12}\right) \gamma_{12}
\end{aligned} \tag{2}
$$

where $\gamma_{i j}=2 \varepsilon_{i j}$, and $C_{k l}$ are the elastic stiffness tensor components written in the usual contracted notation $(k, l=1, \ldots, 6)$. While the shear modulus of the materials, $G$, is simply $1 / 2\left(C_{11}-C_{12}\right)$, the Young's modulus, $E$, is determined by inverting the stiffness tensor components, $C_{k l}$, to determine the components of the compliance tensor, $S_{k l}$, followed by an inversion of $S_{11}$.

The elastic constants in Eq. (2) were determined using the approach outlined by Theodorou and Suter [15], using the Materials Studio 2.2 [19] software package. With this approach, a set of small, static (i.e. no thermal motion) deformations of the RVE was performed from an equili- brated, non-deformed state. The deformed atomic coordi- nates were determined through an additional energy minimization step after the deformation was applied. The energy difference between the deformed and undeformed states was used to calculate one elastic constant for each deformation applied. Further details on this method can be found elsewhere [15].

### 5. Micromechanics models

With the elastic constants of the equivalent-continuum models in hand, two continuum-based micromechanics techniques were used to predict the bulk elastic properties of composites comprised of the polyimide and silica

nanoparticles for various effective particle sizes and effective interfaces. Both models are described below.

### 5.1. Mori–Tanaka model
The Mori–Tanaka approach [24,25] was used to predict the elastic properties of two-phase composites (matrix and effective particle phases) as a function of the effective particle volume fraction and geometry (Fig. 8). For this method, the overall elastic-stiffness tensor of the composite containing the isotropic constituents is
$$
\mathbf{C}=\left(c^{\mathrm{m}} \mathbf{C}^{\mathrm{m}}+c^{\mathrm{p}} \mathbf{C}^{\mathrm{p}} \mathbf{T}^{\mathrm{p}}\right)\left(c^{\mathrm{m}} \mathbf{I}+c^{\mathrm{p}} \mathbf{T}^{\mathrm{p}}\right)^{-1}
\tag{3}
$$
where the boldface terms indicate tensor quantities, $c^{\mathrm{p}}$ and $c^{\mathrm{m}}$ are the effective particle and matrix volume fractions, respectively, $\mathbf{C}^{\mathrm{p}}$ and $\mathbf{C}^{\mathrm{m}}$ are the stiffness tensors of the effective particle and matrix, respectively, $\mathbf{I}$ is the identity tensor, and $\mathbf{T}^{\mathrm{p}}$ is the dilute strain-concentration tensor of the effective particles, and is given by
$$
\mathbf{T}^{\mathrm{p}}=\left[\mathbf{I}+\mathbf{S}^{\mathrm{p}}\left(\mathbf{C}^{\mathrm{m}}\right)^{-1}\left(\mathbf{C}^{\mathrm{p}}-\mathbf{C}^{\mathrm{m}}\right)\right]^{-1}
\tag{4}
$$
where $\mathbf{S}^{\mathrm{p}}$ is the Eshelby tensor [26]. For spherical effective particle and an isotropic matrix, the components of the Eshelby tensor are [27]
$$
\begin{aligned}
& S_{1111}=S_{2222}=S_{3333}=\frac{7-5 \nu}{15(1-\nu)} \\
& S_{1122}=S_{2233}=S_{3311}=S_{1133}=S_{2211}=S_{3322}=\frac{5 \nu-1}{15(1-\nu)} \\
& S_{1212}=S_{2323}=S_{3131}=\frac{4-5 \nu}{15(1-\nu)}
\end{aligned}
\tag{5}
$$
where $\nu$ is the Poisson's ratio of the matrix. For a composite with spherical particles, it is evident from Eqs. (3)–(5) that the composite stiffness tensor is isotropic. For composites with fibrous reinforcement, which are not considered in this study, Eq. (5) has a different form and the composite stiffness tensor is generally anisotropic.

In the Mori–Tanaka method, it is assumed that only the two phases exist (matrix and reinforcement), and they are perfectly bonded to each other. Through a multitude of publications, the Mori–Tanaka approach has been used to accurately predict overall properties of composites when the reinforcements are on the micrometer-scale level, or higher. At these higher length scales, the assumption of the existence of two phases is apparently acceptable. However, for nanometer-sized reinforcement, it has been shown that the molecular structure of the polymer matrix is significantly perturbed at the reinforcement/polymer interface, and this perturbed region is on a length scale that is the same at that of the nanometer-sized reinforcement [9]. Therefore, at the nanometer level, the reinforcement and adjacent polymer region is not accurately described as consisting of just two phases, thus the Mori–Tanaka model is not expected to perform well for nanostructured reinforcements.

![](./images/812316365951074305_10.jpg)

Fig. 8. Schematic illustration of Mori–Tanaka and effective interface micromechanics approaches.

### 5.2. Effective interface model
Because of the aforementioned drawbacks to the Mori–Tanaka approach, another modeling approach was developed. The effective interface model was used to predict the elastic properties of a composite with effective particles that have an interface of the same spherical shape as the effective particle (Fig. 8). The effective interface has a finite size and models the region immediately surrounding the spherical reinforcement, which is commonly referred to as an interphase or an interaction zone. The micromechanical model used for this was developed for composites with two-phase particles [28]. For this model, the bulk elastic stiffness tensor is
$$
\begin{aligned}
\mathbf{C}= & \mathbf{C}^{\mathrm{m}}+\left[\left(c^{\mathrm{p}}+c^{\mathrm{i}}\right)\left(\mathbf{C}^{\mathrm{i}}-\mathbf{C}^{\mathrm{m}}\right) \mathbf{T}^{\mathrm{pi}}+c^{\mathrm{p}}\left(\mathbf{C}^{\mathrm{p}}-\mathbf{C}^{\mathrm{i}}\right) \mathbf{T}^{\mathrm{p}}\right] \\
& \times\left[c^{\mathrm{m}} \mathbf{I}+\left(c^{\mathrm{p}}+c^{\mathrm{i}}\right) \mathbf{T}^{\mathrm{pi}}\right]^{-1}
\end{aligned}
\tag{6}
$$
where $c^{\mathrm{i}}$ and $\mathbf{C}^{\mathrm{i}}$ are the volume fraction and stiffness tensor for the interface, respectively, and $\mathbf{T}^{\mathrm{p}}$ and $\mathbf{T}^{\mathrm{pi}}$ are the dilute strain-concentration tensors given by
$$
\begin{aligned}
\mathbf{T}^{\mathrm{p}}= & \mathbf{I}-\mathbf{S}^{\mathrm{p}}\left[\mathbf{S}^{\mathrm{p}}+\left(\mathbf{C}^{\mathrm{p}}-\mathbf{C}^{\mathrm{m}}\right)^{-1} \mathbf{C}^{\mathrm{m}}\right]^{-1}, \\
\mathbf{T}^{\mathrm{pi}}= & \mathbf{I}-\mathbf{S}^{\mathrm{p}}\left\{\frac{c^{\mathrm{p}}}{c^{\mathrm{i}}+c^{\mathrm{p}}}\left[\mathbf{S}^{\mathrm{p}}+\left(\mathbf{C}^{\mathrm{p}}-\mathbf{C}^{\mathrm{m}}\right)^{-1} \mathbf{C}^{\mathrm{m}}\right]^{-1}\right. \\
& \left.+\frac{c^{\mathrm{i}}}{c^{\mathrm{i}}+c^{\mathrm{p}}}\left[\mathbf{S}^{\mathrm{p}}+\left(\mathbf{C}^{\mathrm{i}}-\mathbf{C}^{\mathrm{m}}\right)^{-1} \mathbf{C}^{\mathrm{m}}\right]^{-1}\right\}
\end{aligned}
\tag{7}
$$

In Eq. (7), the Eshelby tensor, $\mathbf{S}^{\mathrm{p}}$, is given by Eq. (5). As with the Mori–Tanaka model, it is evident with the effective

interface model the composite stiffness tensor in Eq. (6) is isotropic for spherical particle reinforcement.

Similar to the Mori–Tanaka model, the effective interface model assumes that the phases are perfectly bonded to each other. However, the region that physically exists between the surface of the particle and the polymer matrix that has the bulk polymer molecular structure can be considered as an effective interface. The presence of the effective interface allows the region that consists of the perturbed polyimide and interfacial molecules (e.g. phenoxybenzene) to be modeled as a phase unto itself. Unlike the Mori–Tanaka model, the effective interface model should be applicable to both nanometer-sized and larger-sized reinforcement.

At this point, it is appropriate to discuss some of the assumptions in the effective-interface model. In Figs. 3–7 it is clear that the molecular structure of the interfacial region is neither continuous nor homogeneous. The use of the effective interface model assumes that the equivalent-continuum interfacial region is both continuous and homogeneous. The assumptions of continuity and homogeneity must be made to achieve the objectives of this study. The assumption of material continuity is required in order to develop structure–property relationships within a continuum mechanics-based framework. The assumption of homogeneity within the effective interface is employed here to develop an accurate and efficient equivalent-continuum model for nanostructured composites. As a consequence, the effective interface must be modeled as having a finite size with a discrete transition, even though the actual molecular structure consists of a gradual transition to the bulk molecular structure.

## 6. Results and discussion

The calculated Young's and shear moduli of the six material systems are shown in Tables 1 and 2, respectively, determined using the molecular modeling procedure discussed in Sections 3 and 4. It is clear that the presence of the nanoparticle adversely affected the Young's moduli of all four composite systems and the shear moduli of the three non-functionalized composites systems. Therefore, in these instances, there was no elastic reinforcement of the matrix. For the functionalized composite, the shear modulus was equal to that of the pure polyimide. Furthermore, for the functionalized composite system, the Young's and shear moduli were higher than those of the other three composite systems, indicating that direct functionalization of the silica nanoparticle resulted in improved elastic properties over those obtained with non-functionalized silica nanoparticles. It is noted here that it is assumed that all of the predicted properties correspond to room temperature mechanical properties.

A micromechanics analysis was used to predict the elastic properties of the four composite systems using the Mori–Tanaka approach with the elastic properties of the pure polyimide matrix and silica materials determined with the molecular modeling. The effective nanoparticle volume fraction was chosen to be that of the molecular model RVEs (Figs. 3–6), which was determined to be 1.7%. The resulting predicted Young's and shear moduli are shown in Tables 1 and 2, respectively. Because the Mori–Tanaka approach does not consider the molecular structure of the particle/matrix interface, the properties for each of the four composite systems are the same. In contrast to the properties predicted with the molecular modeling, the properties predicted with the Mori–Tanaka approach have Young's and shear moduli that are equal to or larger than those of the polyimide matrix, as expected. Clear discrepancies exist between the values of Young's and shear moduli predicted by the molecular modeling and Mori–Tanaka approach, as is shown in Tables 1 and 2 with the listed percentage differences. The difference between the two approaches is much smaller for the functionalized silica nanoparticle/polyimide composite.

The data presented in Fig. 7 may explain the discrepancies between the predicted elastic properties of the Mori–Tanaka and molecular modeling approaches. For the non-functionalized composites, that is, the silica nanoparticle/polyimide, hydroxylated silica nanoparticle/polyimide, and phenoxybenzene silica nanoparticle/polyimide systems; a 33–40% increase in the polymer density exists at a radial distance of about 8–10 Å, as measured by the peak density value relative to the density at 18 Å. For the functionalized system, only a 6% increase in density is observed. For radial distances between 10 and 15 Å, the initial rise in polymer densities is followed by a decrease in density. For the non-functionalized composites in this radial distance range, the polymer densities associated with the non-functionalized composites are below that of the bulk polymer density (1.33 g/cm³), before they rise to the bulk density level after a radial distance of at least 15 Å. For the functionalized polymer, the initial rise in density is followed by a gradual

Table 1
Young's moduli of the material systems (GPa)

<table>
<thead>
<tr>
<th></th>
<th>Silica</th>
<th>Polyimide</th>
<th>Silica composite</th>
<th>Hydroxylated silica composite</th>
<th>Phenoxybenzene silica composite</th>
<th>Functionalized silica composite</th>
</tr>
</thead>
<tbody>
<tr>
<td>Molecular model</td>
<td>88.7</td>
<td>4.2</td>
<td>3.4</td>
<td>3.3</td>
<td>2.2</td>
<td>4.0</td>
</tr>
<tr>
<td>Mori–Tanaka</td>
<td>–</td>
<td>–</td>
<td>4.3</td>
<td>4.3</td>
<td>4.3</td>
<td>4.3</td>
</tr>
<tr>
<td>% Difference</td>
<td>–</td>
<td>–</td>
<td>26.5</td>
<td>30.3</td>
<td>95.5</td>
<td>7.5</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2 Shear moduli of the material systems (GPa)</caption>
<thead>
<tr>
<th></th>
<th>Silica</th>
<th>Polyimide</th>
<th>Silica composite</th>
<th>Hydroxylated silica composite</th>
<th>Phenoxybenzene silica composite</th>
<th>Functionalized Silica composite</th>
</tr>
</thead>
<tbody>
<tr>
<td>Molecular model</td>
<td>41.0</td>
<td>1.5</td>
<td>1.2</td>
<td>1.2</td>
<td>0.8</td>
<td>1.5</td>
</tr>
<tr>
<td>Mori–Tanaka</td>
<td>–</td>
<td>–</td>
<td>1.5</td>
<td>1.5</td>
<td>1.5</td>
<td>1.5</td>
</tr>
<tr>
<td>% Difference</td>
<td>–</td>
<td>–</td>
<td>25.0</td>
<td>25.0</td>
<td>87.5</td>
<td>0.0</td>
</tr>
</tbody>
</table>

decrease in the density that approaches (but does not consistently drop below) the bulk density level. This decrease in polymer density is most likely a result of the initial increase of the density close to the particle and conservation of mass. The decrease of polymer density below the bulk density level (with an expected decrease in stiffness with a decrease in polymer density) and the nature of the molecular interactions between the particle and polymer molecules could be the causes for the substantial decrease in the predicted properties of the polymer when the non-functionalized particles are added. This behavior at the interface agrees with other results found in the literature [12]. These local changes in molecular structure are not incorporated into the Mori–Tanaka model, where it is assumed that the matrix material has a uniform density up to the surface of the effective particle, to which the matrix is perfectly bonded. Therefore, it is expected that the Mori–Tanaka approach would predict an increase in the elastic properties of the polyimides upon reinforcement, whereas the molecular model predicts a decrease in the elastic properties. Furthermore, the closer agreement between the Mori–Tanaka and molecular models for the functionalized system is expected because of the more uniform density profile of the functionalized system, which is evident in Fig. 7. Because the density of the functionalized system does not consistently drop below the bulk density, a mechanical reinforcement of the polymer matrix is observed.

From the results presented thus far, continuum-based micromechanics do not accurately predict elastic properties of the silica nanoparticle/polyimide composite system when it is assumed that only two uniform phases exist, as is the case with the Mori–Tanaka approach. To improve the micromechanics formulations for nanoparticle-reinforced composite systems, the change in the molecular structure near the particle/polymer interface must be incorporated into the micromechanics model. At the same time, the micromechanics model needs to be able to accurately predict elastic properties for the composite as the effective particle radius is increased from the nanometer level up to the micrometer level.

In the proposed model, it is assumed that an effective interface existed between the surface of the effective particle and the bulk matrix material. This effective interface included the region that contained the denser polymer region and any interfacial molecules, and the scheme in Fig. 9 shows how this effective interface region was defined. For clarity, the graph depicted in Fig. 9 is the same data as in Fig. 7, without the data labels. The effective interface extended from the surface of the effective nanoparticle, at a radial distance of 6 Å, to a radial distance of 18 Å, which corresponded to the edge of the simulation volume in the molecular modeling. The effective interface was spherical and centered at the center of the effective particle, and had a thickness of 12 Å. In Fig. 7 it appears that there is a non-zero polymer density for radii below 6 Å for the phenoxybenzene silica/polyimide composite, thus there are small amounts of polymer in the region that is modeled as an effective particle in the effective interface model. The polymer density in this region is relatively small, and results from the non-perfect spherical shape of the nanoparticle in the molecular model. The radius of the effective particle was chosen to approximate the average radii of the nanoparticles in all of the molecular models. It is expected that for MD simulations of phenoxybenzene silica/polyimide composite with larger simulation box sizes, the densities of the polymer would approach those of the bulk polyimide for large radial distances.

The elastic properties of the effective interface were determined using Eqs. (6) and (7) and the elastic properties of the composites, silica, and pure polyimide determined using the molecular modeling. The volume fractions of the effective particle, effective interface, and matrix were determined based on the volumes shown in Fig. 9, and were 1.7, 45.2, and 53.1%, respectively. The only unknown parameter in Eqs. (6) and (7) is the elastic stiffness tensor of the effective interface, $C^{i}$. It was assumed that $C^{i}$ was isotropic, thus two independent elastic constants were required to define $C^{i}$. Even though the molecular structure of the effective interface region (Fig. 7) does not necessarily posses isotropic symmetry, this assumption was made to maintain a reasonable level of simplicity in the modeling. It was also assumed that the Poisson’s ratio of the effective interface was approximately equal to that of the polyimide, 0.4. The resulting elastic properties of the effective interface are given in Table 3. For all four composites, the effective interface elastic properties were lower than those of the polyimide material (Tables 1 and 2), which is self-consistent with the results discussed above. The elastic properties of the effective interface for the functionalized composite were higher than those of the three non-functionalized composites, indicating that the presence of covalent bonds between the silica and polyimide allowed for an improved load transfer over those of the non-functionalized systems. The elastic properties of the phenoxybenzene silica composite

![](./images/812316365951074305_11.jpg)

Fig. 9. Schematic of the process used to determine effective interface (see Fig. 7 for graph legend).

were particularly low, most likely because of the nature of the interactions of the phenoxybenzene groups with the surrounding polyimide.

Young's and shear moduli of the four composite systems were determined as a function of effective particle size (Figs. 10 and 11, respectively) using the effective interface model; the elastic properties of the silica, polyimide, and effective interface materials; an effective particle volume fraction of 5%; and a constant effective interface thickness of $12 \mathring{A}$. From both Figs. 10 and 11, it is clear that as the effective particle radius is increased up to $1000 \mathring{A}$, the Young's and shear moduli increase. Therefore, as the effective particle size increases, and thus the ratio of the volume of the interface to the volume of the effective particle decreases, the effect of the interface on the composite elastic properties diminishes. For further increases in effective particle size beyond $1000 \mathring{A}$, the elastic properties do not increase significantly.

Also included in Figs. 10 and 11 are the predicted elastic properties determined using the Mori-Tanaka method with the elastic properties of the silica and polyimide materials for an effective particle volume fraction of 5%. Since the Mori-Tanaka method does not assume the existence of an effective interface, the predicted properties were independent of effective particle size and the particle/polyimide interfacial molecular structure. Comparing all of the curves determined from the two modeling approaches, it is clear that the moduli predicted from the effective interface model approach those predicted from the Mori-Tanaka model as the effective particle size increases. At effective particle radii of about $1000 \mathring{A}$ and larger, the predicted Young's moduli and shear moduli of the two models agree. Furthermore, at effective particle radii greater than $1000 \mathring{A}$, $c^{\text{i}} \to 0$ and it can be seen that Eqs. (6) and (7) reduce to Eqs. (3) and (4), respectively. Therefore, the two models are nearly the same for relatively large effective particle radii.

### 7. Summary and conclusions

A continuum-based elastic micromechanics model was developed for silica nanoparticle/polyimide composites with various nanoparticle/polyimide interfacial treatments. The model incorporated the molecular structures of the nanoparticle, polyimide, and interfacial regions, which were determined using a molecular modeling method that involved coarse-grained and reverse-mapping techniques. The micromechanics model included an effective interface

Table 3
Effective interface elastic properties (GPa)

<table>
<thead>
<tr>
<th></th>
<th>Silica composite</th>
<th>Hydroxylated silica composite</th>
<th>Phenoxybenzene silica composite</th>
<th>Functionalized silica composite</th>
</tr>
</thead>
<tbody>
<tr>
<td>Young's modulus</td>
<td>2.4</td>
<td>2.2</td>
<td>0.3</td>
<td>3.5</td>
</tr>
<tr>
<td>Shear modulus</td>
<td>0.9</td>
<td>0.8</td>
<td>0.1</td>
<td>1.3</td>
</tr>
</tbody>
</table>

![](./images/812316365951074305_12.jpg)

Fig. 10. Young's modulus of the four composite systems versus effective particle radius.

between the polyimide and effective nanoparticle with properties and dimensions that were determined using the results of MD simulations.

The predicted elastic properties from the effective interface model were compared to those predicted from the Mori–Tanaka method, which does not incorporate the molecular structure of the nanoparticle, polyimide, and interfacial region. The results of the models were deter- mined for four versions of the composite with different nanoparticle/polyimide interface treatments for effective particle radii ranging from 10 to 10,000 Å. It was shown that the composite Young's moduli and shear moduli deter- mined with the effective interface model increased with increasing effective particle size, and asymptotically approached the moduli predicted from the Mori–Tanaka method, which were independent of effective particle size. This increase in mechanical properties relates to the diminishing effect of the effective interface as its relative volume, with respect to the volume of the particle, decreases when the nanoparticle size becomes larger. The predicted moduli of the two models converged at an effective nanoparticle radius around 1000 Å. Therefore, for the silica nanoparticle/polyimide composites studied, while the effec- tive interface model can be used for any effective nanoparticle size, the Mori–Tanaka method will only predict accurate elastic properties for effective particles greater than 1000 Å.

In addition to the observations on the limits to the micromechanics model, other conclusions can be drawn regarding the material performance. For all four composite systems studied, the elastic properties were lower than those of the polyimide matrix alone when the effective nanopar- ticle radii were on the order of 10 Å. Based on the predicted density profiles, this loss of properties with the addition of nanoparticles is because of the decrease in the polymer density below the bulk polymer density level and the nature of the nanoparticle/polymer molecular interactions. The loss in the elastic stiffness of the composite was significantly reduced by the introduction of chemical functionalization between the silica nanoparticle and the surrounding polyimide molecules. Clearly, for the material considered in this study, the chemical functionalization strengthened

![](./images/812316365951074305_13.jpg)

Fig. 11. Shear modulus of the four composite systems versus effective particle radius.

the bonding between matrix and reinforcement. As the effective particle size increased, and the size of the zone of perturbed polymer remained the same, the influence of the perturbed polymer densities diminished, and became insignificant at an effective particle diameter around $1000\ \mathring{A}$. Therefore, for the specific materials investigated in this study, nanometer-sized reinforcement does not offer advantages over larger-scale reinforcement in terms of elastic properties of the composite. Due to the sensitivity of the macro-scale elastic properties to changes in molecular structure of the material, the benefits of nano-scale reinforcement must be considered on a case-by-case basis for each combination of nanostructured reinforcement and matrix materials.

## References

[1] Gomoll AH, Bellare A, Fitz W, Thornhill TS, Scott RD, Jemian PR, Long GG. A nano-composite poly(methyl-methacrylate) bone cement. In: Komarneni S, Parker JC, Hahn H, editors. Nanophase and Nanocomposite Materials III: Materials Research Society Proceedings, vol. 581. Warrendale, PA: Materials Research Society; 2000. p. 399-404.

[2] Thostenson ET, Ren Z, Chou TW. Compos Sci Technol 2001;61(13): 1899-912.

[3] Vaia RA, Giannelis EP. MRS Bull 2001;26(5):394-401.

[4] Frankland SJV, Caglar A, Brenner DW, Griebel M. J Phys Chem B 2002;106(12):3046-8.

[5] Bradshaw RD, Fisher FT, Brinson LC. Compos Sci Technol 2003; 63(11):1705-22.

[6] Fisher FT, Bradshaw RD, Brinson LC. Compos Sci Technol 2003; 63(11):1689-703.

[7] Frankland SJV, Harik VM, Odegard GM, Brenner DW, Gates TS. Compos Sci Technol 2003;63(11):1655-61.

[8] Odegard, GM, Frankland, SJV, Gates, TS. The effect of chemical functionalization on mechanical properties of nanotube/polymer composites. 44th AIAA/ASME/ASCE/AHS Structures, Structural Dynamics, and Materials Conference, Norfolk, VA; 2003.

[9] Odegard GM, Gates TS, Wise KE, Park C, Siochi E. Compos Sci Technol 2003;63(11):1671-87.

[10] Sheng N, Boyce MC, Parks DM, Rutledge GC, Abes JI, Cohen RE. Polymer 2004;45(2):487-506.

[11] Smith GD, Bedrov D, Li L, Byutner O. J Chem Phys 2002;117(20): 9478-89.

[12] Brown D, Mele P, Marceau S, Alberola ND. Macromolecules 2003; 36(4):1395-406.

[13] Srinivas S, Caputo FE, Graham M, Gardner S, Davis RM, McGrath JE, Wilkes GL. Macromolecules 1997;30(4):1012-22.

[14] Hergenrother PM, Watson KA, Smith JG, Connell JW, Yokota R. Polymer 2002;43(19):5077-93.

[15] Theodorou DN, Suter UW. Macromolecules 1986;19(1):139-54.

[16] Baschnagel J, Binder K, Doruker P, Gusev AA, Hahn O, Kremer K, Mattice WL, Muller-Plathe F, Murat M, Paul W, Santos S, Suter UW, Tries V. Adv Polym Sci 2000;152:41-156.

[17] Tschop W, Kremer K, Batoulis J, Burger T, Hahn O. Acta Polym 1998;49(2-3):61-74.

[18] Doruker P, Mattice WL. Macromol Theory Simul 1999;8(5):463-78.

[19] Materials Studio, Ver. 2.2. Accelrys Inc., San Diego; 2002.

[20] Clancy, TC, Hinkley, J., NASA/TM-2004-213030, 2004.

[21] Rappe AK, Casewit CJ. Molecular mechanics across chemistry. Sausalito, CA: University Science Books; 1997.

[22] Ashby MF, Jones DRH. Engineering materials 1: an introduction to their properties and applications. Oxford, UK: Butterworth-Heine- mann; 1996.

[23] Odegard GM, Gates TS, Nicholson LM, Wise KE. Compos Sci Technol 2002;62(14):1869-80.

[24] Mori T, Tanaka K. Acta Metall 1973;21(5):571-4.

[25] Benveniste Y. Mech Mater 1987;6(2):147-57.

[26] Eshelby JD. Proc Royal Soc Lond, Ser A 1957;241:376-96.

[27] Mura T. Micromechanics of defects in solids. The Hague: Martinus Nijhoff; 1982.

[28] Dunn ML, Ledbetter H. J Appl Mech 1995;62(4):1023-8.