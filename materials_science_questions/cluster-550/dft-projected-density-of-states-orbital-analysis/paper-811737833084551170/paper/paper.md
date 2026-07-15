# Investigation of $H_2$ and $H_2S$ Adsorption on Niobium- and Copper-Doped Palladium Surfaces

Ekin Ozdogan and Jennifer Wilcox*

Department of Energy Resources Engineering, School of Earth Sciences, Stanford University,
Green Earth Sciences 065, 367 Panama Street, Stanford, California 94305

Received: June 14, 2010; Revised Manuscript Received: August 23, 2010

Alloying or doping Pd may be an option for overcoming sulfur poisoning. The current investigation probes the mechanism associated with sulfur binding to determine if Nb and Cu are appropriate doping metals. In this study, the effect of doping Pd with Cu or Nb on the binding strength of $H_2$ and $H_2S$ was investigated using plane-wave density functional theory-based electronic structure calculations to determine mechanisms of adsorption. Results of this work indicate that for pure Pd and Pd-doped surfaces, $H_2$ dissociates with the H atoms most stable on the fcc−fcc site. The overall d-band centers calculated for $H_2$ adsorption at the fcc−fcc site for the pure and doped-Pd surfaces indicate that the $H_2$ adsorption strength trend is Pd > Cu > Nb. Regarding $H_2S$ adsorption on Pd and Pd-doped surfaces, it was found that Cu has a lower affinity for $H_2S$ compared to Pd and Nb. The calculation of the local density of states of the s-, p-, and d-orbitals of the adsorbate−surface complex reveals an increase in the occupation of s-and p-states of the adsorbate and d-states of the dopant metals upon adsorption. In addition, the $H_2S$ binding trend is found to be Cu < Pd < Nb, with the doped-Cu surfaces exhibiting the weakest binding and doped-Nb surfaces the strongest binding. Geometry comparisons of each $H_2S$-adsorbed complex shows that the hydrogen atoms are located closest to the surface in the case of Nb, indicating that the strong H−surface interaction leads to the enhanced adsorption behavior, rather than the S−surface interaction; in fact, the sulfur atom is located furthest from the surface doped with Nb.

## Introduction

Gasification of coal combined with membrane technology offers highly concentrated $CO_2$ streams (30−45% vol) allowing for hydrogen production along with carbon capture. $^{1,2}$ Palladium-based membranes have been intensively investigated as an effective separation technology due to their high hydrogen permeability and surface catalytic activity. Membranes play a significant role in producing clean energy from hydrogen while simultaneously separating carbon dioxide from syngas outlet streams of gasification processes sourced from biomass, coal, or municipal solid waste. Designing a durable and efficient membrane is a challenge and has been a topic of interest spanning multiple scientific disciplines for over 40 years. $^{3−5}$ Palladium (Pd) as a membrane material has been the primary focus because of its high hydrogen permeability and solubility, in addition to its reasonable thermal stability at high temperatures. $^{4−6}$ However, Pd is an expensive material to apply at large scales, and it is highly susceptible to sulfur poisoning by $H_2S$ which is present in the syngas produced by the coal gasification processes. $^{7,8}$ Loss of membrane performance by the presence of sulfur species takes place when sulfur reacts with the surface of the membrane forming a $Pd_4S$ layer inhibiting further $H_2$ adsorption and subsequent permeability. $^{9}$ Alloying Pd with other metals could result in materials with improved performance including enhanced catalytic activity and durability.

In particular, Pd−Cu alloys have received a lot of attention since these materials have demonstrated resistance to $H_2S$ poisoning when the alloy composition is in the face-centered cubic (fcc) region of the Pd−Cu phase diagram compared to pure Pd. $^{10}$ It was suggested that the characteristic fcc structure is responsible for the resistance to poisoning by $H_2S.^{11,12}$ This was validated by density functional theory (DFT) calculations performed to investigate atomic S interactions with the ordered fcc $Pd_3Cu(111)$ and bcc $PdCu(110)$ systems. $^{12}$ Sulfur is found to adsorb stronger on the bcc $PdCu(110)$ surfaces with a binding energy of 4.76 eV compared to adsorption on the fcc $Pd_3Cu(111)$ surface with binding energy of 4.74 eV. $^{12}$ Researchers proposed that when applied on the top layer, the low-permeance property of fcc Pd−Cu alloys can be used to protect the surfaces from $H_2S$ poisoning without greatly reducing the overall permeance since the bulk structure would be comprised of the bcc high-permeance alloy. $^{10}$ Different compositions of Pd−Cu such as 53 wt % Pd−47 wt % Cu (bcc region below 871 K and fcc region over 871 K), 60 wt % Pd−40 wt % Cu (fcc+bcc mixed region below 823 K and fcc region above 823 K), and 80 wt % Pd−20 wt % Cu (fcc region) were studied, and the 53 wt % Pd alloy corresponding to the fcc phase showed the greatest resistance to $H_2S$ at temperatures above 913 K. $^{11}$ However, it was also noted that the highest permeability which is comparable to the permeability values of pure Pd was observed for a composition of 60 wt % Pd−40 wt % Cu at 623 K corresponding to the mixed fcc−bcc phase region. $^{9,11,13}$ Unfortunately, the fcc phases of Pd−Cu alloys are more resistant to sulfur poisoning but exhibit lower permeabilities compared to the bcc phase of the alloys. Au alloyed Pd materials have also been investigated in detail and were observed to yield higher hydrogen permeability (up to 4.8 times higher for 12% Au concentration at 456 K) compared to pure Pd membranes. $^{13}$ As the Au concentration of the alloy was increased to between 25% and 30%, the hydrogen permeability of Pd−Au alloys was shown

* To whom correspondence should be addressed. Tel.: 650-724-9449.
Fax: 650-725-2099. E-mail: wilcoxj@stanford.edu.

10.1021/jp105469c
© 2010 American Chemical Society
Published on Web 09/16/2010

to be lower than that of pure Pd.¹³ Although Pd−Au alloys show enhanced hydrogen permeability at concentrations lower than 12% Au, the high cost of Au (e.g., $950/ounce)¹⁴ makes implementation of these materials to large-scale applications cost-prohibitive. Understanding the mechanism associated with sulfur resistance of the fcc phase motivated the current research to find a material that would exhibit both sulfur resistance and optimal permeability. This was carried out by doping pure Pd with Cu and Nb to specifically investigate the H₂ and H₂S interactions with these doped surfaces to determine the mechanism responsible for surface preference toward sulfur versus hydrogen. Niobium of the group 5 metals (i.e., V, Nb, Ta) with its low material cost (e.g., $1.105/ounce)¹⁵ provides an interesting option for doping since it exhibits exceedingly high H₂ permeabilities compared to pure Pd and other alloying metal options like Au.¹⁶,¹⁷ Among the group 5 metals, Nb exhibits the highest relative permeability of hydrogen.¹⁷ The study of competitive adsorption of H₂ and H₂S on Pd−Nb surfaces is limited in the literature; therefore, this will be the focus of the current work which will assess the feasibility of using such membranes for enhanced H₂ permeability. Although there is wide variety in the studies performed for Nb and Pd in the context of H₂ and H₂S interactions,¹⁷,¹⁸ no computational study has directly investigated Pd−Nb systems for hydrogen separation applications.

The main aim of this study is to show the effect of the addition of a small amount of Nb and Cu to the surface of pure Pd on the adsorption of H₂S and H₂ using plane-wave DFT-based electronic structure calculations. Binding energies, optimized adsorption configurations, and density of states (DOS) analyses of these structures are presented and used for understanding surface reactivity and the related mechanism associated with H₂ and H₂S adsorption.

## Computational Methodology
The calculations were performed using the Vienna ab initio simulation package (VASP) using the generalized gradient approximation (GGA).¹⁹ The Kohn−Sham one-electron valence eigenstates were expanded in terms of plane-wave basis sets with a cutoff energy of 350 eV and Methfessel−Paxton²⁰ smearing width of 0.05 eV. The Pd(111) surface was modeled by a four-layer slab having an in-plane 4 × 4 unit cell with 16 atoms per layer with 1 Nb or Cu atom placed on the uppermost layer resulting in a dopant concentration of 1.6%. This concentration was selected to ensure that the fcc phase of Pd remained the same for the alloy structures. According to the Pd−Nb phase diagram, the Pd−Nb system is fcc up to 30 at % Nb.²¹ To prevent the interaction between periodic images, a 10 Å-thick vacuum region was used to isolate the slabs. During the geometry optimization for the final stable configurations, the atomic coordinates were allowed to relax except for the bottom two layers, which were fixed at their equilibrium values. The k-point sampling of the two-dimensional electronic Brillouin zone of the periodic slabs was performed using the Monkhorst−Pack k-point mesh of 5 × 5 × 1. To compare the stability of the different models, the adsorption energy, $E_{\text{ads}}$, is defined for dissociated H₂ in eq 1 and H₂S in eq 2 as

$$
E_{\text{ads}} = \frac{(E_{\text{surf+H}_2} - E_{\text{surf}} - E_{\text{H}_2})}{2} \tag{1}
$$

$$
E_{\text{ads}} = E_{\text{surf+H}_2\text{S}} - E_{\text{surf}} - E_{\text{H}_2\text{S}} \tag{2}
$$

such that $E_{\text{surf+H}_2}$, $E_{\text{surf+H}_2\text{S}}$ are the total energy of the adsorbate system where $E_{\text{surf}}$, $E_{\text{H}_2}$, and $E_{\text{H}_2\text{S}}$ are the relaxed surface and gas phase H₂ and H₂S energies, respectively. By this definition, the larger the negative value associated with adsorption, the more stable the adsorbed complex is.

## Results and Discussion
### 1. Hydrogen (H₂) Adsorption.
Within this work, the adsorption of two H atoms after the dissociation of H₂ was investigated on pure Pd and Nb- and Cu-doped Pd surfaces, with H atoms placed at three different configurations, i.e., the fcc−fcc, hcp−hcp, and fcc−hcp sites as shown in Figure 1b(i)−(iii). The location of each site was determined so that it would be closest to the surface atom where the effect of the dopant metal would be greatest.

The initial and final structures of H₂ adsorption on pure Pd, Pd−Nb, and Pd−Cu surfaces are identical and shown in Figures 1 and 2. After the geometric optimizations, the H atoms essentially remain at their initial positions for the fcc−fcc and hcp−hcp configurations as demonstrated in Figure 2a, b. However, for the third case (Figure 1b(iii)), where one H atom was positioned at the hcp site and the other at the fcc site, the H atom at the hcp site moved to the neighboring fcc site located farther from the dopant (Nb or Cu) atom (Figure 2d). This new fcc−fcc site is labeled as fcc−fcc* to show the distinction between the distances of H atom to the dopant atom in the fcc−fcc and fcc−fcc* configurations. This indicated that the binding to the fcc−fcc sites is much more stable for H₂ adsorption further from the alloying atom on these surfaces. The shift of the initial fcc−hcp structure was not observed for H₂ adsorption on the pure Pd surface, and the initial fcc−hcp structure was preserved (Figure 2c). This suggests that the first step in the pathway for subsurface H diffusion will likely be from a site coordinated with Pd rather than a dopant metal. In fact, as can be seen in Table 1, the most stable configurations for H₂ adsorption on the Pd−Nb and Pd−Cu surfaces were obtained from the optimization of initial placement at the fcc−hcp site resulting in the final adsorption at the fcc−fcc* site. Also shown in Table 1 are all of the adsorption energies and geometric properties for H₂ on pure Pd, Pd−Nb, and Pd−Cu surfaces. Comparing the energy values of H₂ adsorption on the Pd−Nb and Pd−Cu surfaces to pure Pd for the initial fcc−hcp binding configuration where the final structures are different showed that alteration of a Pd atom with a dopant metal atom can act to separate the hydrogen atoms on the surface.

Our calculations show that the individual positions of each H atom of the H₂ molecule are very important for adsorption.

![](./images/811737833084551170_1.jpg)

Figure 1. Schematic representation of the (a) side view (dark gray atoms, first layer; light gray, second layer; dashed, third layer; blank, 4th layer; black, alloyed atom) of the clean surface; (b) top view of the initial (i) fcc−fcc, (ii) hcp−hcp, and (iii) fcc−hcp initial positions of two H atoms on the doped surfaces.

![](./images/811737833084551170_2.jpg)

Figure 2. Schematic representation of final top view of two H atoms at the (a) fcc−fcc, (b) hcp−hcp, (c) fcc−hcp, and (d) fcc−fcc* sites.

<table>
<caption>TABLE 1: Adsorption Energies and Optimized Geometric Parameters for the Adsorption of H₂ on Different Surfaces</caption>
<thead>
<tr>
<th>initial (H−H)</th>
<th>final (H−H)</th>
<th>E<sub>ads</sub>(eV)</th>
<th>d<sub>H−surface</sub>(Å)</th>
<th>d<sub>(H−H)</sub>(Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5">Pd</td>
</tr>
<tr>
<td>fcc−fcc</td>
<td>fcc−fcc</td>
<td>−0.5927 (−0.6)<sup>a</sup></td>
<td>0.75/0.73</td>
<td>2.89</td>
</tr>
<tr>
<td>hcp−hcp</td>
<td>hcp−hcp</td>
<td>−0.5485 (−0.56)<sup>a</sup></td>
<td>0.80/0.88</td>
<td>2.89</td>
</tr>
<tr>
<td>fcc−hcp</td>
<td>fcc−hcp</td>
<td>−0.4889</td>
<td>0.78/0.83</td>
<td>1.96</td>
</tr>
<tr>
<td colspan="5">Pd−Nb</td>
</tr>
<tr>
<td>fcc−fcc</td>
<td>fcc−fcc</td>
<td>−0.4740</td>
<td>0.86/1.06</td>
<td>3.18</td>
</tr>
<tr>
<td>hcp−hcp</td>
<td>hcp−hcp</td>
<td>−0.4259</td>
<td>0.81/0.84</td>
<td>3.14</td>
</tr>
<tr>
<td>fcc−hcp</td>
<td>fcc−fcc*</td>
<td>−0.5230</td>
<td>0.83/0.96</td>
<td>2.92</td>
</tr>
<tr>
<td colspan="5">Pd−Cu</td>
</tr>
<tr>
<td>fcc−fcc</td>
<td>fcc−fcc</td>
<td>−0.5357</td>
<td>0.92/0.91</td>
<td>2.86</td>
</tr>
<tr>
<td>hcp−hcp</td>
<td>hcp−hcp</td>
<td>−0.4946</td>
<td>0.93/0.91</td>
<td>2.89</td>
</tr>
<tr>
<td>fcc−hcp</td>
<td>fcc−fcc*</td>
<td>−0.5699</td>
<td>0.82/1.10</td>
<td>2.88</td>
</tr>
<tr>
<td colspan="5"><sup>a</sup> Reference 29.</td>
</tr>
</tbody>
</table>

For example, on the pure Pd(111) surface, H₂ preferably binds to the fcc−fcc site with an adsorption energy of −0.5927 eV and the energy decreases to −0.5485 eV for adsorption at the hcp−hcp site and has the highest value of −0.4889 eV at the fcc−hcp site. Binding energies for the two H atoms initially located at the fcc−fcc and hcp−hcp sites decrease when a Pd atom is replaced by a Nb or Cu atom. The strongest adsorption for dissociated H₂ on the Pd−Nb surface is −0.5230 eV and −0.5699 eV on the Pd−Cu surface. From Table 1, the distances of each H atom to the Pd surface were found to be 0.75 Å/0.73 Å, 0.80 Å /0.88 Å, and 0.78 Å /0.83 Å for the fcc−fcc, hcp−hcp, and fcc−hcp configurations, respectively. Comparing the distances of the H atoms to the surface and adsorption energies, it can be concluded that as the H binding becomes stronger, the final H atom distance to the surface become shorter due to the higher attraction of the surface.

Analyzing how doping modifies the electronic structure of the atoms of the surface and adsorbate−surface complex helps in understanding the mechanism associated with adsorption. Local density of states (LDOS) analyses have been carried out and are plotted for H₂ adsorption at the fcc−fcc site of the pure and doped Pd surfaces as shown in Figure 3a, 3b, and 3c. In each of the subfigures, the initial and final states are given for each H atom positioned at the dopant location and the surface metal atom having the greatest interaction. To make a complete comparison of the adsorption effect of doping Pd with Nb and Cu, the Pd atom on the pure Pd surface at the dopant location was labeled as Pd*. It can be understood from Figure 3a−c that half of the occupied s-states of hydrogen in the gas phase represented by the peak centered at the Fermi level become fully occupied after adsorption. The downshift and subsequent splitting of the initial s-orbital peak from the Fermi level to energy values ranging between −6 and −7.5 eV are also depicted in these figures. For all the three surfaces, the decreasing population of the metal d-states close to the Fermi level and the broadening and shift of the main d-peak to lower energy levels illustrate the increased occupation of the d-states of the metal found at the dopant location. A more detailed analysis was performed through the investigation of the Nb-doped Pd surface LDOS after adsorption, as pictured in Figures 4 and 5.

Similar LDOS trends were observed for pure Pd and doped-Pd surfaces for the case of H₂ adsorption, and the LDOS of Nb-doped surface are given in Figures 4 and 5 to show the overall changes in the density of states before and after adsorption. The first observation that can be drawn from Figure 4 is that the level of bonding between the s-orbitals of the two dissociated H atoms has decreased in energy due to the interaction with the s-, p-, and d-states of Nb, which can be seen by the double peaks lying below −6 eV. The strongest interactions appear to occur between the s-orbital of H and the s-, d<sub>z²</sub>-, d<sub>xy</sub>-, and d<sub>xz</sub>-orbitals of the Nb atom. Also, the

![](./images/811737833084551170_3.jpg)

Figure 3. LDOS of metal d-states and H₂ s-states before and after the adsorption.

![](./images/811737833084551170_4.jpg)

Figure 4. LDOS of s- and p-orbitals of Nb after adsorption.

![](./images/811737833084551170_5.jpg)

Figure 5. LDOS of s-orbital of H and d-orbitals of Nb after the adsorption.

interactions between the s-orbital of H and the pₓ-, dₓᵧ-, and dₓz-orbitals of Nb lie at a higher energy value around −6 eV compared with the s-, pᵧ-, pz-, dᵧz-, dₓ₂-, and dᵧ₂-orbitals of Nb lying around an energy value of −6.4 eV. (Figures 4 and 5)

Other important conclusions that can be drawn from the LDOS analysis are the locations of the d-band centers ($\varepsilon_{\text{d}}$) relative to Fermi level for the surface atoms, which provides an indication of the ability of the surface d-electrons to form bonds with the adsorbate. Methods of modifying and potentially enhancing surface reactivity include overlayer deposition and alloying or doping with a metal into the surface layer.²²,²³ According to Ruban et al.,²⁴ doping with a metal atom of a smaller lattice constant within the surface layer of another metal atom type with larger lattice constant will cause the $\varepsilon_{\text{d}}$ of the dopant metal to shift up toward the Fermi level. There are three components that drive the stability of an adsorbate−sorbent complex, which include the $\varepsilon_{\text{d}}$ of the surface atoms, the degree of filling of the d-bands, and the coupling matrix element between the adsorbate states and the metal d-states. Filling of the adsorbate's antibonding orbitals results in a weakening of the intramolecular bonds of the adsorbate. Depending upon the level of filling of the bonding orbitals, an upshift of the surface $\varepsilon_{\text{d}}$ could result in an increased interaction with the metal d-states

**Adsorption on Nb- and Cu-Doped Pd Surfaces**
*J. Phys. Chem. B, Vol. 114, No. 40, 2010* **12855**

<table>
<caption>TABLE 2: Surface d-Band Centers and Adsorption Energies for H₂ at the Initial fcc−fcc Configuration</caption>
<thead>
<tr>
<th></th>
<th>ε<sub>d</sub> (eV)</th>
<th>Wigner−Seitz radius r<sub>s</sub> (au)<sup>a,b</sup></th>
<th>ε<sub>davg</sub><sup>d,e</sup> (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Pd*</td>
<td colspan="3">Pd(111)</td>
</tr>
<tr>
<td>−1.79 (−1.81)<sup>a,b</sup></td>
<td>2.87</td>
<td>−1.79</td>
</tr>
<tr>
<td rowspan="2">Cu<br>Pd (first layer)</td>
<td colspan="3">Pd−Cu(111)</td>
</tr>
<tr>
<td>−1.53 (−2.36)<sup>a,b</sup><br>−2.27</td>
<td>2.67</td>
<td>−2.16</td>
</tr>
<tr>
<td rowspan="2">Nb<br>Pd(first layer)</td>
<td colspan="3">Pd−Nb(111)</td>
</tr>
<tr>
<td>−2.76 (1.41)<sup>a,c</sup><br>−1.91</td>
<td>3.07</td>
<td>−2.40</td>
</tr>
</tbody>
</table>

<sup>a</sup> Values are given for the properties of pure metals having (111) indexed surface. <sup>b</sup> Reference 12. <sup>c</sup> Reference 26. <sup>d</sup> Calculated by ε<sub>davg</sub> = (Σ<sub>M</sub>V<sub>M</sub><sup>2</sup>ε<sub>d</sub><sup>M</sup>N<sup>M</sup>)/(Σ<sub>M</sub>V<sub>M</sub><sup>2</sup>N<sup>M</sup>), where V<sub>M</sub><sup>2</sup> is the d-band coupling matrix element for the surface metal (M = Pd, Cu, Nb), ε<sub>d</sub><sup>M</sup> is the d-band center of the individual surface atom, and N<sup>M</sup> is the number of M−H bonds.<sup>25</sup> <sup>e</sup> V<sub>Pd</sub><sup>2</sup> = 2.78, V<sub>Cu</sub><sup>2</sup> = 1, V<sub>Nb</sub><sup>2</sup> = 7.73.<sup>24</sup>

and the antibonding orbitals of the adsorbate, thereby increasing the chemisorption energy. The d-band centers of each surface metal located at the dopant position of the model surface and their bulk experimental ε<sub>d</sub> values are provided in Table 2. In order to make the size and adsorption strength comparison of these metals, their Wigner−Seitz radius (r<sub>s</sub>) and the H₂ adsorption energies for the fcc−fcc configuration are also included in Table 2. As can be examined from Table 2, the addition of Cu (r<sub>s</sub> = 2.67) to the Pd (r<sub>s</sub> = 2.87) surface resulted in an upshift of ε<sub>d</sub> from −2.36 to −1.53 eV. On the other hand, doping with Nb (r<sub>s</sub>= 3.07), which has a larger Wigner−Seitz radius than Pd, resulted in a downshift of ε<sub>d</sub> from 1.41 to −2.76 eV. The downshift of the Nb d-band center and the subsequent location of the metal d-states increase the difficulty of filling of the antibonding states of the hydrogen dimer. From Table 2 it can be observed that the Pd d-band center of the Pd−Cu surface is located at a lower energy level (ε<sub>d</sub> = −2.27 eV) than in pure Pd (ε<sub>d</sub> = −1.79 eV), which is consistent with the previous study of Alfonso et al.<sup>12</sup> Previous investigations showed that the d-band shifts in the Pd−Cu alloys are strong enough to reverse the ordering of the d-band centers of the two metals with respect to the pure metal surfaces.<sup>12</sup> Our findings indicate that the shifts in the d-band center of Pd−Nb surfaces are also large enough to reverse the d-band ordering seen for the pure Pd system from −1.79 to −1.91 eV. The effect of doping a Pd surface with Cu or Nb on the chemisorption energy of H₂ on these surfaces was determined by investigating the overall d-band center average (ε<sub>davg</sub>) of these systems obtained by using the method of Pallasana and co-workers (Table 2).<sup>25</sup> From Table 2, it was observed that the fcc−fcc configuration of H₂ on pure Pd resulted in the strongest interaction with ε<sub>davg</sub> (−1.79 eV) located closest to the Fermi level compared to the Cu- or Nb-doped Pd surfaces. In the case of the doped surfaces, as ε<sub>davg</sub> shifts further from the Fermi level (−2.16 eV for Pd−Cu and −2.40 eV for Pd−Nb), the adsorption energy weakens, which is consistent with the d-band model of Hammer and Nørskov.<sup>26</sup>

### 2. Hydrogen Sulfide (H₂S) Adsorption.
Understanding the adsorption of H₂S on pure Pd and Nb- and Cu-doped Pd surfaces provides insight into the design and synthesis of H₂S-tolerant surfaces for H₂ production applications. To consider the interactions of H₂S with these surfaces, one S and two H atoms were placed at different configurations on each of the surfaces investigated. Some of the initial and final structures for the Pd−Nb surface are given in Figure 6. By inspection of Figure 6, one can notice that all of the initial configurations, except the one given in Figure 6a, have changed upon adsorption to a more stable configuration. These observations are supported by considering the adsorption energies and optimized geometric properties of the systems investigated as shown in Table 3.

For the case of H₂S adsorption, pure Pd and Nb-doped Pd surfaces were compared first with different adsorption configurations, and then only the most stable system from the Pd−Nb case was tested for the Cu-doped Pd surface to determine the effect of doping with Cu versus Nb. Adsorption energies are given in Table 3. Our calculations indicate that the most stable configuration for H₂S on the Pd surface occurs with each of the H atoms located at bridge sites and the S atom at the top site with an adsorption energy of −0.707 eV, which was obtained from the initial fcc−fcc−top configuration. The results obtained for the bridge−hcp−top (H−H−S) adsorption configuration on the pure Pd surface are found to be consistent with the previous study by Alfonso et al.<sup>27</sup>

It is also interesting to note that the H atoms located at both fcc and hcp sites in most of the cases moved through the bridge sites (i.e., initial H−H−S configurations of fcc−fcc−topNb and hcp−hcp−topNb) to arrive at their stable configurations. There is only one initial configuration where the final structure is unique; therefore, we have defined this new site as the “off-center hollow” (oc hollow) site as shown in Figure 5b. The initial configuration for this defined final structure is such that the two H atoms are at the fcc sites with the S atom located at the hcp site. When the Nb atom is replaced by Pd, an increase in adsorption energy is observed for the configuration in which the H atoms are each located at the fcc and bridge sites with the S atom located at the top-site of Nb. The adsorption energy for this configuration is −0.803 eV, representing the most stable configuration of all those tested for H₂S adsorption. Thus, it can be concluded that the Nb-doped surface has a higher affinity toward H₂S compared to Pd. Another aspect that is significant to mention is the difference between the adsorption strengths of H₂S on Nb- and Cu-doped surfaces for the bridge−fcc−top configuration. The absolute H₂S adsorption energy on Cu-doped surfaces (−0.429 eV) is nearly half that of Nb-doped or pure Pd surfaces. This shows that Cu has a lower attraction to H₂S compared to Pd and Nb at the bridge−fcc−top (H−H−S) configuration. Comparing the adsorption energies of H₂ versus H₂S on both the pure Pd and Nb-doped Pd surfaces, both surfaces favor H₂S adsorption. However, this is not the case for the Cu-doped Pd surface (the bridge−fcc−top configuration) of which the adsorption energy for H₂ is remarkably lower than that of H₂S. Comparison of the sulfur atom distance and each of the hydrogen atom distances to these surfaces provides information about the affinities of the investigated surfaces toward the adsorbate atoms. The side views of the final configurations obtained after the H₂S adsorption for the bridge−fcc−top (H−H−S) case are given in Figure 7. The distance of the S atom to the Nb-doped Pd surface (2.65 Å) is shown to be larger compared to the case of pure Pd (2.34 Å) and Cu-doped Pd (2.33 Å) surfaces. Considering the case in which the adsorption energy is the strongest, i.e., H₂S on the Nb-doped surface, the sulfur atom is located furthest from the surface and the two hydrogen atoms are positioned closest to the surface compared to pure Pd or the Cu-doped surfaces. This indicates that the overall low energy (strong binding) of H₂S on the Nb-doped surface may have to do with the high affinity hydrogen has to the surface relative to sulfur. In fact, these investigations indicate that this surface may be promising for diffusion of surface-bound hydrogen into the bulk due to this strong H-surface interaction; however, this is the case only if

![](./images/811737833084551170_6.jpg)

Figure 6. Schematic representation of $H_2S$ adsorption on the Pd−Nb surface at the sites (a) bridge−fcc−topNb, (b) fcc−fcc−hcp, (c) hcp−hcp−fcc, and (d) hcp−hcp−topPd and (e) side view of the system.

<table>
<thead>
<tr>
<th colspan="2">TABLE 3: Adsorption Energies of the Pd and Nb- and Cu-Doped Surfaces</th>
<th> </th>
<th> </th>
<th> </th>
<th> </th>
</tr>
<tr>
<th>initial H−H−S</th>
<th>final H−H−S</th>
<th>$E_{ads}$(eV)</th>
<th>$d_{S-surface}$(Å)</th>
<th>$d_{H-S}$(Å)</th>
<th>$d_{H-surface}$(Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td> </td>
<td> </td>
<td>Pd</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>fcc−fcc−topPd*</td>
<td>bridge−bridge−topPd*</td>
<td>−0.707</td>
<td>2.33</td>
<td>1.352/1.354</td>
<td>2.70/2.69</td>
</tr>
<tr>
<td>hcp−hcp−topPd*</td>
<td>bridge−bridge−topPd*</td>
<td>−0.701</td>
<td>2.32</td>
<td>1.352/1.353</td>
<td>2.60/2.60</td>
</tr>
<tr>
<td>bridge−fcc−topPd*</td>
<td>bridge−fcc−topPd*</td>
<td>−0.700</td>
<td>2.34</td>
<td>1.355/1.352</td>
<td>2.64/2.60</td>
</tr>
<tr>
<td>bridge−hcp−topPd*</td>
<td>bridge−hcp−topPd*</td>
<td>−0.688</td>
<td>2.299</td>
<td>1.362/1.364</td>
<td>2.49/2.39</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>$(−0.71)^a$</td>
<td>$(2.37)^a$</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>fcc−hcp−topPd*</td>
<td>fcc−hcp−topPd*</td>
<td>−0.692</td>
<td>2.34</td>
<td>1.359/1.357</td>
<td>2.56/2.58</td>
</tr>
<tr>
<td>fcc−fcc−hcp</td>
<td>ochollow−ochollow−ochcp</td>
<td>−0.593</td>
<td>2.35</td>
<td>1.356/1.359</td>
<td>2.81/2.82</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>Pd−Nb</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>bridge−fcc−topNb</td>
<td>bridge−fcc−topNb</td>
<td>−0.803</td>
<td>2.65</td>
<td>1.362/1.260</td>
<td>2.33/2.31</td>
</tr>
<tr>
<td>hcp−hcp−fcc</td>
<td>bridge−bridge−topNb</td>
<td>−0.704</td>
<td>2.59</td>
<td>1.359/1.539</td>
<td>2.60/1.60</td>
</tr>
<tr>
<td>bridge−hcp−topNb</td>
<td>bridge−hcp−topNb</td>
<td>−0.735</td>
<td>2.59</td>
<td>1.437/1.361</td>
<td>1.88/2.32</td>
</tr>
<tr>
<td>hcp−hcp−topNb</td>
<td>bridge−bridge−topNb</td>
<td>−0.702</td>
<td>2.64</td>
<td>1.357/1.358</td>
<td>2.55/2.55</td>
</tr>
<tr>
<td>fcc−fcc−topNb</td>
<td>bridge−bridge−top</td>
<td>−0.696</td>
<td>2.63</td>
<td>1.355/1.358</td>
<td>2.58/2.55</td>
</tr>
<tr>
<td>fcc−hcp−topNb</td>
<td>fcc−hcp−topNb</td>
<td>−0.682</td>
<td>2.66</td>
<td>1.364/1.356</td>
<td>2.40/2.44</td>
</tr>
<tr>
<td>fcc−fcc−hcp</td>
<td>ochollow−ochollow−ochcp</td>
<td>−0.651</td>
<td>2.59</td>
<td>1.362/1.367</td>
<td>2.91/2.90</td>
</tr>
<tr>
<td>hcp−hcp−topPd</td>
<td>hcp−bridge−topPd</td>
<td>−0.602</td>
<td>2.36</td>
<td>1.354/1.354</td>
<td>2.96/2.75</td>
</tr>
<tr>
<td>fcc−hcp−topPd</td>
<td>fcc−hcp−topPd</td>
<td>−0.585</td>
<td>2.37</td>
<td>1.357/1.356</td>
<td>2.77/2.79</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>Pd−Cu</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>bridge−fcc−topCu</td>
<td>bridge−fcc−topCu</td>
<td>−0.429</td>
<td>2.33</td>
<td>1.356/1.354</td>
<td>2.37/2.33</td>
</tr>
<tr>
<td>bridge−hcp−topCu</td>
<td>bridge−hcp−topCu</td>
<td>−0.431</td>
<td>2.33</td>
<td>1.367/1.362</td>
<td>2.24/2.37</td>
</tr>
</tbody>
</table>

$^{a}$ Reference 27.

the atomic sulfur is not left behind to potentially occupy and poison sites preventing additional hydrogen adsorption. The changes in electronic structure of the atoms in the bridge−fcc−top (H−H−S) configuration for the pure Pd and doped-Pd surfaces are investigated through a LDOS analysis as illustrated in the plots in Figure 8. It was observed that for all three surfaces the

d-orbital states of the metals downshift in energy and most importantly split to form three distinct peaks overlapping the sulfur p-states after adsorption. The interaction of the metal with the sulfur atom has also resulted in the downshift of sulfur p-states further from the Fermi level (Figure 8). This indicates that the occupancies of the metal d-states and sulfur p-states

![](./images/811737833084551170_7.jpg)

Figure 7. Side view of the final structures after $H_2S$ adsorption to the bridge−fcc−top (H−H−S) site on (a) pure Pd, (b) Pd−Nb, and (c) Pd−Cu surfaces.

have redistributed to an increased occupancy at lower energies as a result of the interaction. These findings also indicate that since the d-states of the metal are located further from the Fermi level it will be more difficult for electrons to fill the antibonding states of the adsorbate.

After considering the above investigations, it can be con- cluded that doping changes both adsorption preferences and binding strength. This result is also consistent with the previous findings of $H_2^{28}$ and atomic $S^{12}$ adsorption on Pd−Cu alloys. According to Ling et al.,$^{28}$ the difference between pure Pd and the $Pd_{75}Cu_{25}$ alloy comes from the latter surface having a spatially heterogeneous set of binding sites. They stated that the binding sites on the alloy surface are geometrically similar but have varying local atomic compositions. The adsorption energy results for the geometrically similar fcc−fcc and fcc−fcc* configurations showed consistency with the previous investigation$^{28}$ through yielding unique energies corresponding to the local atomic composition resulting from doping. For S adsorption on Pd and alloy surfaces, Alfonso et al.$^{12}$ stated that Pd interacts more strongly than Cu. The atomic S binding energy decreases on alloy surfaces, and S prefers to adsorb at the highest coordination sites on the alloy surfaces as investigated in their work.$^{12}$ As a conclusion of the current study, it was observed that the addition of Nb increased the $H_2S$ affinity of the Pd surface where as the opposite occurred with the addition of Cu for a similar adsorption configuration.

The d-band center model of Hammer and Nørskov$^{26}$ also gives insight into determining the affinity of the metal surfaces for a given adsorbate species, provided the adsorbate is in atomic form or a simple diatomic molecule. In the case of S binding at the top site of the dopant metal atom, the position of $\varepsilon_d$ of the dopant atom (Table 2, experimental $\varepsilon_d$) with respect to the Fermi level is helpful for understanding the adsorption strengths of the dopant metal for atomic sulfur only. In fact, for the molecular species, $H_2S$, the binding trend is (Cu < Pd < Nb) due to the enhanced interaction of hydrogen atoms with the surface in the case of the Nb-doped system. In the case of $H_2S$ the d-band center model could be used only if the local interactions of sulfur and each of the hydrogen atoms with the surface were examined.

![](./images/811737833084551170_8.jpg)

Figure 8. LDOS of metal d-states and sulfur (S) p-states before and after adsorption.

## Conclusions

In the present work, the effects of doping, or more specifi- cally, replacing a surface Pd atom with a Nb or Cu atom, were examined for different $H_2$ and $H_2S$ adsorbed states. Results of this work indicate that the placement of dissociated $H_2$ at the fcc−fcc site is energetically favorable compared to placement at the hcp−hcp and fcc−hcp sites. Especially for the Nb- and Cu-doped surfaces, the subsequent movement of the H atom from the hcp site to the fcc site shows that the fcc site is the most stable adsorption site. Another significant finding was the stronger binding exhibited for the same kind of adsorption configuration (fcc−fcc) but at different initial placements. The more stable adsorption configuration was obtained when the H atom moves away from the Nb or Cu dopant atom, indicating that Pd is more attracted to H than to Nb and Cu. Among the three different alloy surfaces and configurations investigated, it can be concluded that $H_2$ adsorption is more likely to occur at the fcc−fcc site on a pure Pd surface. The LDOS are analyzed to determine the mechanism of adsorption, and it can be concluded that the s-, $d_{xy^{-}}$, and $d_{xz}$-orbitals played the most significant role in the adsorption mechanism. The downshift of

the d-band center of Pd by the addition of Nb and the upshift resulting from doping with Cu illustrates the improved perfor- mance in terms of $H_2$ binding of Cu-doped Pd surfaces compared to Nb-doped surfaces. The obtained adsorption energy trend for these surfaces is also found to be consistent by investigating the overall d-band centers. Regarding the $H_2S$ adsorption on Pd and Pd-doped surfaces, it can be concluded that Nb has a higher affinity for $H_2S$ compared to Pd. It has also been found that Cu has a lower attraction to $H_2S$ compared to Pd and Nb for the initial bridge-fcc-top $(H-H-S)$ configuration. LDOS analyses of these systems show that the interaction of the metal with the sulfur atom also results in the depletion of p-states of sulfur near the Fermi level. Also, the metal d-states and sulfur p-states have redistributed toward increased occupancy at lower energies as a result of interaction. The trend of increasing $H_2S$ binding strength of the dopants $(Cu < Pd < Nb)$ is obtained as a result of the given study. Geometry comparisons of each $H_2S$- adsorbed complex show that the hydrogen atoms are located closest to the surface in the case of Nb, indicating that the strong $H$-surface interaction leads to the enhanced adsorption behav- ior, rather than the $S$-surface interaction; in fact, the sulfur atom is located furthest from the surface doped with Nb.

Acknowledgment. Financial support has been provided by the U.S. Army Research Young Investigator Program. We thank Dr. Shela Aboud for her insight and helpful discussions on this work. The computations were carried out on the Center for Computational Earth & Environmental Science (CEES) cluster at Stanford University.

### References and Notes

(1) Han, C.; Harrison, D. P. *Chem. Eng. Sci.* **1994**, 49 (24B), 5875-5883.

(2) Cormos, C. C.; Starr, F.; Tzimas, E.; Peteves, S. *Int. J. Hydrogen Energy* **2008**, 33, 1286-1294.

(3) Jewett, D. N.; Makrides, A. C. *Trans. Faraday Soc.* **1965**, 61, 932-939.

(4) Løvvik, O. M.; Olsen, R. A. *Phys. Rev. B* **1998**, 58 (16), 10890-10898.

(5) Ozawa, N.; Arboleda, N. B., Jr.; Roman, T. A.; Nakanishi, H.; Diño, W. A.; Kasai, H. *J. Phys.: Condens. Matter.* **2007**, 19, 365214-365225.

(6) Conrad, H.; Ertl, G.; Latta, E. E. *Surf. Sci.* **1974**, 41, 435-446.

(7) Alptekin, G.; DeVoss, S.; Dubovik, M.; Monroe, J.; Amalfitano, R.; Israelson, G. *J. Mater. Eng. Perform.* **2006**, 15 (4), 433-438.

(8) Criscuoli, A.; Basile, A.; Drioli, E.; Loiacono, O. *J. Membr. Sci.* **2001**, 181 (1), 21-27.

(9) Morreale, B. D.; Howard, B. H.; Iyoha, O.; Enick, R. M.; Ling, C.; Sholl, D. S. *Ind. Eng. Chem. Res.* **2007**, 46 (19), 6313-6319.

(10) Pomerantz, N.; Ma, Y. H. *Ind. Eng. Chem. Res.* **2009**, 48 (8), 4030-4039.

(11) Morreale, B. D.; Ciocco, M. V.; Howard, B. H.; Killmeyer, R. P.; Cugini, A. V.; Enick, R. M. *J. Membr. Sci.* **2004**, 241, 219-224.

(12) Alfonso, D. R.; Cugini, A. V.; Sholl, D. S. *Surf. Sci.* **2003**, 546 (1), 12-26.

(13) Sonwane, C. G.; Wilcox, J.; Ma, Y. H. *J. Chem. Phys.* **2006**, 125 (184714), 1-10.

(14) U.S. Geological survey, http://minerals.usgs.gov/minerals/pubs/commodity/gold/mcs2010-gold.pdf, August 2010.

(15) U.S. Geological survey, http://minerals.usgs.gov/minerals/pubs/commodity/niobium/mcs-2010-niobi.pdf, August 2010.

(16) Phair, J. W.; Donelson, R. *Ind. Eng. Chem. Res.* **2006**, 45 (16), 5657-5674.

(17) Buxbaum, R. E.; Marker, T. L. *J. Membr. Sci.* **1993**, 85 (1), 29-38.

(18) Komiya, K.; Shinzato, Y.; Yukawa, H.; Morinaga, M.; Yasuda, I. *J. Alloys Compd.* **2005**, 404-406, 257-260.

(19) Kresse, G.; Hafner, J. *Phys. Rev. B* **1994**, 49, 14251-14269.

(20) Methfessel, M.; Paxton, A. T. *Phys. Rev. B* **1989**, 40 (6), 3616-3621.

(21) Chandrasekharaiah, M. S. *Bull. Alloy Phase Diagr.* **1988**, 9, 4-449.

(22) Rodriguez, J. A.; Goodman, D. W. *Science* **1992**, 257 (5072), 897-903.

(23) Holmblad, P. M.; Hvolbæk Larsen, J.; Chorkendorff, I.; Pleth Nielsen, L.; Besenbacher, F.; Stensgaard, I; Lægsgaard, E.; Kratzer, P.; Hammer, B.; Nørskov, J. K. *Catal. Lett.* **1996**, 40, 131-135.

(24) Ruban, A.; Hammer, B.; Stoltze, P.; Skriver, H. L.; Nørskov, J. K. *J. Mol. Catal. A: Chem.* **1997**, 3 (115), 421-429.

(25) Pallasana, V.; Neurock, M.; Hansen, L. B.; Nørskov, J. K. *J. Chem. Phys.* **2000**, 112, 5435-5440.

(26) Hammer, B.; Nørskov, J. K. *Adv. Catal.* **2000**, 45, 71-129.

(27) Alfonso, D. R.; Cugini, A. V.; Sorescu, D. R. *Catal. Today* **2005**, 99 (3-4), 315-322.

(28) Ling, C.; Sholl, D. S. *J. Membr. Sci.* **2007**, 303 (1-2), 162-172.

(29) Dong, W.; Hafner, J. *Phys. Rev. B* **1997**, 56 (23), 15396-15402.

JP105469C