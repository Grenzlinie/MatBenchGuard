# Thermo-mechanical properties of a piezoelectric polyimide carbon nanotube composite: Assessment of composite theories

Arnab Chakrabarty $^{a}$, Tahir Çağın $^{a,b,*}$

$^{a}$ Department of Chemical Engineering, Texas A\&M University, College Station, TX 77843, USA
$^{b}$ Materials Science and Engineering, Texas A\&M University, College Station, TX 77843, USA

---

## ARTICLE INFO

**Article history:**
Received 15 January 2014
Received in revised form 13 May 2014
Accepted 21 May 2014

**Keywords:**
Polymer nanocomposite
Molecular dynamics
Micromechanics
Carbon nanotube
Halpin–Tsai
Mori–Tanaka
Piezoelectric

---

## ABSTRACT

In this work, we have characterized the thermomechanical properties of carbon nanotube based piezoelectric polymer nanocomposite using a hybrid force field for all atomistic molecular dynamic simulations. In addition, applicability of some of the well-known micromechanics composite theory in estimating carbon nanotube based polymer nanocomposite properties were assessed. We found that the primary reason for the strengthening effect of a nanocomposite with incorporation of a nanotube is the carbon–carbon bond and angle strength. The orientation of the nanotube in the polymer matrix is key to its reinforcement effect on a nanocomposite. We also observed that a perfect axial orientation does result in improving the axial modulus, but in the radial direction any strengthening for such a unidirectional composite does not seem possible without any bonding at the interface between the filler and the matrix material. The self-consistent field theory was found to be the closest with the atomistic simulation results for predicting mechanical properties of a polymer nanocomposite. The Halpin–Tsai model also demonstrated reasonable capability in predicting the strengthening effect. Mori–Tanaka model, however, underestimated the strengthening effect of carbon nanotube on the polymer matrix. It was also found that the existing composite theories are better at estimating low weight percentage nanotube strengthening effect.

© 2014 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Engineering polymer nanocomposite materials at the atomistic level, suited for different advanced applications has made them lucrative to both researchers and industry [1–5]. However, the lack of understanding of the physics at nanoscale, have limited our ability to optimally exploit the possibilities and understand the limitations of nano-reinforced materials. Models capable of capturing composite properties with reasonable accuracy can significantly help successful implementation of engineering applications using nanocomposites and its optimal design. As we illustrated below, in various studies, existing composite theories have been extended and applied to understand their effectiveness in establishing structure–property relationship for characterizing polymer nanocomposites.

Mechanical properties of carbon nanotube and its polymer nanocomposites have been investigated using finite element analysis [6–10], micromechanics model with emphasis on failure [10] and reinforcement mechanism [11], models based on continuum mechanics [8,12], cohesive zone model with incorporation of details related to the interface of the nanocomposite [9], shear lag model to understand effect of electro-thermo-mechanical loadings [13], finite difference model [14], neural network model to estimate transverse elastic modulus of unidirectional composite [15], progressive fracture model [16], Krenchel model [17,40], rule of mixture model [17] and Kelly–Tyson model [39]. Among the micromechanics models, Halpin–Tsai [17,18,35] and Mori Tanaka model [19,29] are two of the well known models. Other models [20] include implementing a combination of 3D voxel based model representation of material structures and Voigt–Reuss method of material property estimation. Quaresimin et al. [21] classified various approaches for assessment of nanocomposite mechanical properties into molecular models, nanostructured models and micromechanics models. However no model till date has emerged as a widely accepted approach in designing nanocomposite materials. Through their review Quaresimin et al. [21] assessed that molecular modeling method is the most effective way of reasonably predicting mechanical properties of nanocomposites. Rahmat et al. [22] also noted the effectiveness and accuracy of

---

* Corresponding author at: Department of Materials Science and Engineering, Texas A&M University, College Station, TX 77843, USA. Tel.: +1 9798622416; fax: +1 9798626835.
E-mail address: tcagin@neo.tamu.edu (T. Çağın.)

http://dx.doi.org/10.1016/j.commatsci.2014.05.045
0927-0256/© 2014 Elsevier B.V. All rights reserved.

$$
\left[
\mathrm{
\begin{matrix}
\mathrm{O-}
\mathrm{
\begin{matrix}
\mathrm{CH_3} \\
\mathrm{\bigcirc}
\end{matrix}
}
\mathrm{-O-}
\mathrm{
\begin{matrix}
\mathrm{CN} \\
\mathrm{\bigcirc} \\
\mathrm{O}
\end{matrix}
}
\mathrm{-O-}
\mathrm{
\begin{matrix}
\mathrm{\bigcirc} \\
\mathrm{CH_3}
\end{matrix}
}
\mathrm{-N-}
\mathrm{
\begin{matrix}
\mathrm{O} \\
\mathrm{\bigcirc} \\
\mathrm{\bigcirc} \\
\mathrm{O}
\end{matrix}
}
\mathrm{-O-}
\mathrm{
\begin{matrix}
\mathrm{\bigcirc} \\
\mathrm{\bigcirc} \\
\mathrm{O} \\
\mathrm{N-} \\
\mathrm{O}
\end{matrix}
}
\end{matrix}
}
\right]_n
$$

Fig. 1. (β−CN)APB/ODPA monomer.

using molecular dynamics in capturing the interaction between the polymer matrix and its nanofiller. Hence, experimental studies and simulation of nanocomposite materials at an atomistic level are still the best way for estimating its properties through capturing the behavior at the interface and explain different structure property relationships observed for nanocomposites.

By comparing results to a fully atomistic model, this study attempts to assess the degree of effectiveness of three well received micromechanics models in characterizing a single walled carbon nanotube polymer nanocomposite of a piezoelectric polyimide matrix. Specifically, we have compared our results against rule of mixture, Mori Tanaka, Halpin Tsai and Self Consistent theory. In addition the study looks into thermal softening of nanocomposites, effect of implementing stress perpendicular to nanotube axial direction in a nanocomposite and change in glass transition behavior of nanocomposite owing to the presence of nanotube through atomistic simulation.

## 2. Material and methods

### 2.1. System

The nanocomposite system studied in this work consists of infinitely long single walled (10, 10) carbon nanotube with unidirectional alignment (z direction), inside an amorphous piezoelectric polymer matrix. The matrix is a piezoelectric polyimide substituted with nitrile dipole known as $\beta-CN$)APB/ODPA polyimide (Fig. 1).

### 2.2. Model building

A modified approach of building amorphous polymer samples [23,24] was used to build the nanocomposite samples. An amorphous polymer sample with a very low density was built with Cerius$^{2.0}$ or Materials Studio with sufficient space in the unit cell to incorporate the infinitely long nanotube along the desired axial direction. The carbon nanotubes were then placed and bonded across the periodic boundaries of the unit cell [25]. For efficient use of resources, the nanotube was treated as a rigid rod, ignoring energies resulting from bond and angle vibration in the equilibration stage. Owing to the infinite length of the nanotube, the unit cells were only compressed in two directions. Subsequent to unit cell compression, the charges at the interface were updated through implementation of charge equilibration technique [26]. The built sample then went through temperature annealing within each compression cycle and was followed by isothermal-isobaric (NPT) molecular dynamics simulation to attain an equilibrated state. Fig. 2 illustrates such a sample nanocomposite as viewed in a molecular dynamics simulation environment.

A representative volume element, that is, a zoomed out version of Fig. 2, the polymer nanocomposite sample in its unit cell is shown in Fig. 3.

To overcome the structural biasness in sample distribution resulting from exploration of limited phase space by a single nanocomposite sample, in this work we have built eight different nanocomposite samples with varying weight percentage of nanotube ranging from 2.18% to 18.7%. For convenience, the eight samples constructed are defined below, which are referred throughout the article with the names as given below in Table 1. The corresponding pristine polyimide is prefixed by the word 'pristine'.

### 2.3. Force field

The interfacial interaction between the polymer and the nanotube was incorporated through van der Waals and coulombic interaction. A force field consisting of hybrid potentials for various energy components was defined to describe the components of the Hamiltonian for the heterogeneous nanocomposite system. A specially developed force field for nanotube, derived from first principle energy calculation of graphite [27], as implemented in another work by the authors [25], was used to describe the energetic of the carbon nanotube. The total energy of the carbon nanotube was defined as:

$$E = E_B + E_A + E_I + E_{VDW} + E_C$$

where $E$ is the total energy of the system; $E_B$ the energy due to bond stretching (two body); $E_A$ the energy due to angle bending (three body); $E_I$ the energy due to out of plane configuration or dihedral (two body); $E_{VDW}$ the energy due to van der Waals interaction; $E_C$ is the energy due to Coulomb interaction.

The energetic due to torsion was assumed to be insignificant and was neglected. The contribution of different components of the total energy were calculated as follows:

van der Waals interaction:
$$E_{vdw} = D_{vdw}(\rho^{-12} - \rho^{-6}) \quad \text{where}: \rho = r/r_v$$

where $r_v$ is the separation energy at minimum energy between the two atoms.

Bond stretch energy:
$$E_{bond} = D_b(\mu - 1)^2 \quad \text{where} \ \mu = e^{-[r-r_b]}$$

![](./images/814748359087620097_1.jpg)

Fig. 2. A cartoon of polymer nanocomposite.

<bbbox>91 88 472 257</>

Fig.. 3. Satic of Sys8 structure file showing nanotube aligned in ' z' direction.

Table 1
Nan composite system naming convention.

| System name | CNT wt.% | Mon monomers per chain | Number of chains
|---|---|---|---
 Syss1 |18.4 |6|6
Sys2 |9..77 |12|110
Sys3 |9.42 |25 |5
Sys4 |9.77 |30 |10
 Sys5 |5.62 |30 |220
Sys6 |5.62 |40 |115
 Sys7 |2.89 |40 |330
Sys8 |2.118 |40 |40

where $r_b is the equilibrium bond length. 

Angle bending energy:

$$
{aligned 
E_{angle== \rac{1}{2k_\0(\cos\ theta-\cos \theta_a)^2+k_{10(r1-r_10)\(\cos\ theta-\ cos theta_a)+ k_{20(r_2-r_20)\(\ cos\ theta-cos \ theta_a)+k_{12(r_1-r_10(r_2-r_20)
\end{aligned
$$

 where $ k_0, k_{10, k_{20 and $k_12 are the bond stretch and stretch-bend force constants.

Di hedral energy:

$$E_{dihedral= V_0 + V_1 \cos\ phi + V_2 \ \cos(2\ phi)$$

 where $ V_0, V_1 and $ V_2 are expansion coefficients for the truncated Fourier expansion up to second order.

The interaction potentials of the polyimide atoms were depicted by CVFF force field and are not described here Table 2.

##3. Results and discussions
###3.1. Mechanical properties

Each nan composite sample was subjected under tension and compression and energy of the deformed composite sample was expanded in Taylor series around its equilibrbrated structure. The second order coefficient of the series was calculated and the mechanical strength of a sample was estimated. Since this method does not take temperature effect into account, the values typically represent the material strength at absolute zero. Details of this approach, also known as molecular mechanics, can be found elsewhere [25]. Table 3 illustrates the reinforcement of the matrix owing to presence of the nanot.

Table2
Force field parameters for carbon nanot.

|Parameters | rv |Dvdw|rb |Db| θ_a |k0 |k10 |k20 |k112 |V0 |V1|V2|
|---|---|---|---|---|---|---|---|---|---|---|---|
||3.805 |0.069 |1.41 |720 |120 |1196.1 |-72.4 |-772.4 |68 |10.6 |0 |-10.6|<bbbbox>559 83900 907295></>

 Fig..4.Reforcement of nan composite with unirectionctionally dispersed CNT.

Translation of Table 3 generates Fig. 4. The results agree well with the expectation of reinforcement of the composite in the axial direction and are directly proportional to the weight percentage of the nanot present in the system. It must be borne in mind that owing to infinite length of the nanot and periodic placement, the study does not look into effect of nanot dispersion, agglom-eration ( proportional to nanot weight percentage), wwiness or defects in nanot, any one or combination of which is expected to reduce the reinforcement effect [10]. Researchers have looked into [28 modifying micromechanchanics equation to account for non-idealalities like these..

 The effect of temperature on mechanical strength of various composite system was assessed by performing all-atomistic molecular dynamic simulation of samples up to ~10% by weight of nanot, namely Sys2-Sys8. Fig.. 5 illustrates the effect of presence of nanot on axial modulus of the polymer nan composite.We observe the nanot reinforcement effect through a shift in the stress-strain slope for various degrees of reinforcement.

 Anallyzing Fig..5 we find:

1. The presence of nanot reinforces the polymer nan composite. The strengthening effect is proportional to the weight percentage of the nanot.
2. The presence of nanot also affects the plastic property of the polymer. We have observed in our polymer simulation study [24, that the polymer enters the viscous region with a stress level <200 MPa. However on applying stress along the axial direction of nanot we do not observe any such response here. We have later showed that any stress applied in the per-ppendicular direction to the nanot axis does result in response similar to that of a pristine polymer.
3. Estimation of Young modulus from Fig.. 5 and results from molecular mechanics calculation generates Table 4. Typically thermal softening effect is more dominant in less stiff materials.

 Fig..6, the visual representation of Table 4, also also shows the softening effect. However, it must be noted that the percentage change in axial modulus values, as shown in Table 4, demonstrates the


<table><caption>Table 3 Effect of carbon nanotube on axial modulus at 0 K.</caption>
<thead>
<tr>
<th>System</th>
<th>Pristine polymer $C_{33}$ (GPa)</th>
<th colspan="2">Nanocomposite</th>
</tr>
<tr>
<th></th>
<th></th>
<th>wt% of nanotube</th>
<th>(GPa)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sys1</td>
<td>13.14</td>
<td>18.4</td>
<td>135</td>
</tr>
<tr>
<td>Sys2</td>
<td>13.14</td>
<td>9.77</td>
<td>101</td>
</tr>
<tr>
<td>Sys3</td>
<td>13.66</td>
<td>9.42</td>
<td>94.5</td>
</tr>
<tr>
<td>Sys4</td>
<td>13.64</td>
<td>9.77</td>
<td>96.3</td>
</tr>
<tr>
<td>Sys5</td>
<td>13.38</td>
<td>5.62</td>
<td>65.7</td>
</tr>
<tr>
<td>Sys6</td>
<td>12.24</td>
<td>5.62</td>
<td>60.3</td>
</tr>
<tr>
<td>Sys7</td>
<td>11.04</td>
<td>2.89</td>
<td>37.5</td>
</tr>
<tr>
<td>Sys8</td>
<td>13.65</td>
<td>2.18</td>
<td>40.3</td>
</tr>
</tbody>
</table>

![](./images/814748359087620097_2.jpg)

reduction in softening in stiffer nanocomposites which may not be apparent in the widening disparity in axial modulus with increased presence of carbon nanotube by weight percentage.

### 3.2. Comparison with micromechanics models

To capture properties of materials reasonably well at all length scales through a unified model, bridging of molecular level studies with continuum mechanics is of significant importance. Several micromechanical models have attempted to estimate mechanical properties of composites as pointed out before in this article. In here we attempt to compare our atomistic simulation results with some of the well known existing composite theories.

In the mean field approach, the effective property of the composite is determined by calculating the stress or strain concentration tensor. Mori-Tanaka [29] theory and self-consistent method [30] are examples of methods which takes advantage of the Eshelby solution [31] of ellipsoidal inclusion with a stress free transformation strain (or Kroner's polarization strain [32] and Mura's eigenstrain [33,34]) in determining the concentration tensor.

Mori-Tanaka and self-consistent field approach uses the following equation in evaluating the modulus of the composite consisting of a matrix and a filler material:

$$E_{C}=E_{M}+c_{C N T}\left(E_{C N T}-E_{M}\right) A_{C N T}\tag{1}$$

where $E_{C}$ is the elastic modulus of the composite; $E_{M}$ the elastic modulus of the matrix (Polymer in our study); $c_{C N T}$ the volume fraction of carbon nanotube; $A_{C N T}$ the concentration tensor of carbon nanotube.

The difference in estimation of the concentration tensor of the filler material makes the difference in approaches of Mori-Tanaka and self-consistent field theory.

For Mori-Tanaka approach the concentration tensor is calculated as follows:

$$A_{C N T}=A_{C N T}^{d i l}\left[c_{C N T} I+c_{C N T} A_{C N T}^{d i l}\right]\tag{2}$$

where the dilute concentration tensor is calculated by:

$$A_{C N T}^{d i l}=\left[I+S_{C N T} E_{M}^{-1}\left(E_{C N T}-E_{M}\right)\right]^{-1}\tag{3}$$

where $S_{C N T}$ stands for the Eshelby tensor for the carbon nanotube. Details of this method can be found elsewhere [29,31].

In self-consistent field approach the concentration tensor used in Eq. (1)is estimated as follows:

$$A_{C N T}=\left[I+S_{C N T} E_{C O M P}^{-1}\left(E_{C N T}-E_{C O M P}\right)\right]^{-1}\tag{4}$$

Comparing Eqs. (4) and (1) we observe that the equations are coupled through the appearance of the unknown modulus of the composite in the right hand side of Eq. (4), which is solved through an iterative scheme.

Halpin-Tsai [35] is another widely used method that uses a different approach in determining composite properties. The theoretical framework of this approach is more suited for predicting properties of unidirectional composites as a function of a given aspect ratio. Using this route, the axial modulus can be predicted by:

$$E_{C O M P}=E_{C N T} v_{C N T}+E_{M} v_{M}\tag{5}$$

where $E_{i}$ is the axial modulus of ' $i$ ' ( $i$ stands for composite, nanotube and polymer matrix); $v_{i}$ is the Volume fraction of component ' $i$ ' ( $i$ stands for carbon nanotube and Polymer matrix).

While Halpin-Tsai model also gives prediction separately for transverse modulus, the model is only valid where the matrix and the filler is firmly bonded [35], unlike the cases studied here.

We have utilized the properties estimated for the pristine polymer [24,36] and nanotube [25] as input to the micromechanics model for predicting nanocomposite properties and compare the same with out atomistic simulation results for the nanocomposite samples. In using these composite theories, the volume fraction values were proportionately replaced by weight fraction of the nanotube. Fig. 7 illustrates the comparison in graphical terms.

Analyzing Fig. 7 we find that:

1. The atomistic results agree best with self-consistent field theory. It also does agree reasonably with Halpin-Tsai theory than Mori-Tanaka. It is expected that the average of Mori Tanaka and self-consistent prediction (methods are only differed by concentration tensor) will predict the mechanical strengthening effect more accurately.
2. Applications of the assessed micromechanics models are better suited with low weight percentage nanotube composite, namely up to 2 wt.% nanotube. The deviation between the models and simulation results widens with higher nanotube weight percentage.

The comparisons of the micromechanics theories through stress-strain diagrams are illustrated in Fig. 8.

<table><caption>Table 4 Reduction of softening with higher % filler.</caption>
<thead>
<tr>
<th>CNT (%)</th>
<th>T</th>
<th></th>
<th></th>
</tr>
<tr>
<th></th>
<th>300 K (MD)</th>
<th>0 K (MM)</th>
<th>Change in axial modulus (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$0^{a}$</td>
<td>4</td>
<td>13</td>
<td>69</td>
</tr>
<tr>
<td>2.18</td>
<td>15.56</td>
<td>40.3</td>
<td>61</td>
</tr>
<tr>
<td>2.89</td>
<td>21.12</td>
<td>37.5</td>
<td>44</td>
</tr>
<tr>
<td>5.62</td>
<td>34.4</td>
<td>63.0</td>
<td>45</td>
</tr>
<tr>
<td>9.77</td>
<td>54.94</td>
<td>96.3</td>
<td>43</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="4">$^{a}$ Note that the values with 0% CNT or that of pristine polyimide is an average value over the examined polyimide systems.</td>
</tr>
</tfoot>
</table>

![](./images/814748359087620097_3.jpg)

Fig. 6. Reduction of softening in axial direction with higher % CNT.

![](./images/814748359087620097_4.jpg)

Fig. 7. Comparison of atomistic simulation results of nanocomposite axial modulus to those predicted by few micromechanics model for composites.

### 3.3. Radial stretch

In the earlier section, we have observed reinforcement of the polymer matrix in the axial direction due to the presence of the nanotube. This is expected as majority of the applied stress is dis- sipated in stretching the stiff carbon-carbon bonds of the nano- tube. However as there is no interfacial bonding, the stress applied orthogonally to the nanotube axial direction is majorly countered by stretching of the polymer system. Fig. 9 represents the system response of composite systems to application of stress in radial direction to various nanocomposite systems. We observe that the polymer enters to plastic region as stress value is increased. The orthogonal orientation of the applied stress with respect to the nanotube axis is the primary reason for the polymer response to be similar to the pristine polymer response [24,36].

Apparently few cases show strengthening effect, careful obser- vation reveals the absence of the strengthening effect in the other radial direction and hence the fact can be attributed to modeling anisotropy than presence of the nanotube itself. Instead of illustrating transverse modulus separately in 'X' and 'Y' direction, the average response as depicted in Fig. 10, shows similar stress-strain behavior of different systems, independent of the weight percentage of the carbon nanotube in each system. The stress-strain response of the pristine polymer has also been

![](./images/814748359087620097_5.jpg)

Fig. 8. Comparison of stress-strain response estimation using various micromechanics theories. From top left clockwise: Sys4, Sys6, Sys8 and Sys7.

![](./images/814748359087620097_6.jpg)

Fig. 9. Transverse modulus in X and Y direction.

![](./images/814748359087620097_7.jpg)

Fig. 10. Average transverse modulus.

plotted along side to emphasize the insignificant effect of presence of carbon nanotube.

The similarity in transverse modulus of a unidirectional nano- composite with the axial modulus of its pristine polymer counter- part has also been noted by the work of Frankland et al. [37] at the atomistic level and Shokrieh et al. [38] at the finite element level analysis. This observation emphasizes that the primary reason for a composite strength is the carbon-carbon bond strength and structural arrangement of nanotube, especially in absence of any

![](./images/814748359087620097_8.jpg)

Fig. 11. Moment of inertia analysis for Sys8.

![](./images/814748359087620097_9.jpg)

Fig. 12. Thermal expansion behavior of nanocomposite samples.

![](./images/814748359087620097_10.jpg)

Fig. 13. Density variation of pristine polymer systems with temperature.

![](./images/814748359087620097_11.jpg)

Fig. 14. Density variation with temperature for nanocomposite samples.

interface bonding between the matrix and the filler. As a conse- quence, the nanotube is not expected to help nullify any effect of force-applied orthogonal to its axial direction unless it is chemi- cally bonded to any polymer chain at the interface. In this study, the interaction of polymer chains with the nanotube is incorpo- rated through van der Waals and coulombic forces at the interface.

To inspect the effect of radial stress at the chain level, normalized principal moment of inertia of all the chains was calculated. We observe, as shown in Fig. 11, that chains get stretched and aligned in the direction of the applied stress ('y' in this case) and as a consequence the value of the moment of inertia reduces for that direction. However to facilitate such process in presence of the entangled network of the polymer chains and presence of nanotube, few chains act otherwise as demonstrated in Fig. 11. On the contrary, the values of $I_{xx}$ and $I_{zz}$ increases at a rapid rate as the polymer enter the plastic region indicating the loss of orientation along those directions.

### 3.4. Thermal expansion and glass transition temperature

To assess thermal effects, various nanocomposites built were subjected to heating from 300 K to 700 K with increments of 100 K. We have observed [36] the presence of glass transition behavior around 490 K for the pristine polymer sample by atomistic simulation. The presence of nanotube is expected to resist and delay the glass transition like behavior of the nanocomposite. Fig. 12 illustrates such effect for Pristine Sys8. Unlike our observation in the pristine polymer study [36] glass transition like behavior was nonexistent within the domain of study for the nanocomposite. Fig. 13, depicts the second order change in density for the pristine polymer samples, whereas Fig. 14, as noted, does not show any change in the degree of softening with temperature for the nanocomposite samples. Two nanocomposite samples, Sys7 and Sys8, samples with the lowest weight % SWNT, were examined for identifying glass transition temperatures. Given that, Sys1 through Sys6, with increased SWNT content and stiffness, are not expected to show glass transition behavior within the examined temperature range.

Fig. 13 clearly demonstrates the presence of glass transition behavior of the pristine polyimide system with a $T_g$ in between 450 and 500 K. While intersection of the two different slopes can provide us a rough estimate, a better estimate can be obtained by examining more temperature points between 450 and 500 K.

## 4. Conclusions

In this work, we have studied thermomechanical characteristics of carbon nanotube based polymer nanocomposite by implementing all-atomistic molecular dynamics simulation by using a hybrid force field. A combination of CVFF force field and a carbon nanotube force field derived from first principle calculations of graphite were utilized to depict the system dynamics. We have also assessed some of the well-known micromechanics composite theory in estimating nanocomposite properties. We found that the primary reason for the strengthening effect of a nanocomposite with incorporation of a nanotube is the carbon-carbon bond and angle strength. The orientation of the nanotube in the polymer matrix is key to its reinforcement effect on a nanocomposite. We also observed that a perfect axial orientation does result in improving the axial modulus, but in the radial direction any strengthening for such a unidirectional composite does not seem possible without any bonding at the interface between the filler and the matrix material. We observe that, self-consistent field theory best agrees with the atomistic simulation results in predicting mechanical properties of a unidirectionally aligned carbon nanotube polymer nanocomposite. The Halpin-Tsai model also demonstrated reasonable capability in predicting the strengthening effect. Mori-Tanaka model however underestimated strengthening effect of carbon nanotube on the polymer matrix. It was also found that the existing composite theories are better at estimating low weight percentage nanotube strengthening effect.

## References

[1] Z. Spitalsky, D. Tasis, K. Papagelis, C. Galiotis, Prog. Polym. Sci. (2010).
[2] Q.H. Zeng, A.B. Yu, G.Q. Lu, Prog. Polym. Sci. (2008).
[3] E.T. Thostenson, C. Li, T.W. Chou, Compos. Sci. Technol. (2005).
[4] P.M. Ajayan, L.S. Schadler, P.V. Braun, Nanocompos. Sci. Technol. (2006).
[5] J.W. Gilman, T. Kashiwagi, J.D. Lichtenhan, SAMPE J. (USA) (1997).
[6] B. Ashrafi, P. Hubert, Compos. Sci. Technol. (2006).
[7] S.K. Georgantzinos, G.I. Giannopoulos, N.K. Anifantis, Theor. Appl. 52 (2009) 158-164.
[8] F. Karimzadeh, S. Ziaei-Rad, S. Adibi, Metall. Mater. Trans. B 38 (2007) 695-705.
[9] M. Kulkarni, D. Carnahan, K. Kulkarni, D. Qian, J.L. Abot, Compos. Part B - Eng. 41 (2010) 414-421.
[10] C. Li, T.-W. Chou, Compos. Part A - Appl. S. 40 (2009) 1580-1586.
[11] A. Eitan, F.T. Fisher, R. Andrews, L.C. Brinson, L.S. Schadler, Compos. Sci. Technol. 66 (2006) 1162-1173.
[12] J. Jancar, J. Mater. Sci. 43 (2008) 6747-6757.
[13] A. Salehi-Khojin, N. Jalili, Compos. Part B - Eng. 39 (2008) 986-998.
[14] Y. Termonia, Polymer 48 (2007) 6948-6954.
[15] E.C. Bezerra Camara, R.C.J. Silverio Freire, Compos. Part B - Eng. 42 (2011) 2024-2029.
[16] K.I. Tserpes, P. Papanikos, G. Labeas, S.G. Pantelakis, Theor. Appl. Fract. Mech. 49 (2008) 51-60.
[17] C. McClory, T. McNally, G.P. Brennan, J. Erskine, J. Appl. Polym. Sci. 105 (2007) 1003-1011.
[18] V. Mittal, J. Thermoplast. Compos. Mater. 22 (2009) 453-474.
[19] X. Zheng, M.G. Forest, R. Lipton, R. Zhou, Continuum Mech. Therm. 18 (2007) 377-394.
[20] L. Mishnaevsky, Compos. Sci. Technol. (2012).
[21] M. Quaresimin, M. Salviato, M. Zappalorto, Compos. Part B - Eng. (2012).
[22] M. Rahmat, P. Hubert, Compos. Sci. Technol. (2011).
[23] S.B. Sane, T. Çağın, W.G. Knauss, J. Comput. Aided 5 (2001) 5-50.
[24] A. Chakrabarty, T. Cagin, Polymer 51 (2010) 2786-2794.
[25] A. Chakrabarty, T. Cagin, CMC: Comput. Mater. Con. 7 (2008) 167-189.
[26] A.K. Rappe, W.A. Goddard III, J. Phys. Chem. (1991).
[27] T. Cagin, G. Gao, W.A.I. Goddard, Turk J. Phys. 30 (2006) 221-229.
[28] R. Arasteh, M. Omidi, A.H.A. Rousta, H. Kazerooni, J. Macromol. Sci. B 50 (2011) 2464-2480.
[29] T. Mori, K. Tanaka, Acta Metall. Mater. 21 (1973) 571-574.
[30] R. Hill, J. Mech. Phys. Solids 13 (1965) 213-222.
[31] J.D. Eshelby, Proc. Roy. Soc. Lond. Ser. A 241 (1957) 376-396.
[32] E. Kroner, Z. Phys. 151 (1958) 504-518.
[33] T. Mura, Micromechanics of Defects in Solids, Kluwer Academic Publishers, 1987.
[34] G.J. Weng, Int. J. Eng. Sci. 28 (1990) 1111-1120.
[35] J.C. Halpin, J.L. Kardos, Polym. Eng. Sci. 16 (1976) 344-352.
[36] A. Chakrabarty, Carbon Nanotube Polymer Nanocomposites for Electromechanical System Applications, Thesis, Texas A&M University, 2008.
[37] S.J.V. Frankland, V.M. Harik, G.M. Odegard, D.W. Brenner, T.S. Gates, Compos. Sci. Technol. 63 (2003) 1655-1661.
[38] M.M. Shokrieh, R. Rafiee, Mech. Res. Commun. 37 (2010) 235-240.
[39] A. Kelly, W.R. Tyson, J. Mech. Phys. Solids 13 (1965) 329-350.
[40] H. Krenchel, Fibre Reinforcement, Akademisk Forlag, Copenhagen, 1964.