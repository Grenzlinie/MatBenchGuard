Accepted Manuscript

Adsorption of $CO_2$ on graphene surface modified with defects

Roxana M. del Castillo, Alipio G. Calles, Raúl Espejel-Morales, Héctor Hernández-
Coronado

![](./images/813021007773171714_1.jpg)

PII:
S2352-2143(18)30146-1

DOI:
10.1016/j.cocom.2018.e00315

Article Number: e00315

Reference:
COCOM 315

To appear in: Computational Condensed Matter

Received Date: 9 May 2018

Revised Date: 8 June 2018

Accepted Date: 12 June 2018

Please cite this article as: R.M. del Castillo, A.G. Calles, Raú. Espejel-Morales, Hé. Hernández-
Coronado, Adsorption of $CO_2$ on graphene surface modified with defects, Computational Condensed
Matter (2018), doi: 10.1016/j.cocom.2018.e00315.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to
our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please
note that during the production process errors may be discovered which could affect the content, and all
legal disclaimers that apply to the journal pertain.

# Adsorption of $CO_2$ on graphene surface modified with defects.

Roxana M. del Castillo$^{a,*}$, Alipio G. Calles$^{a}$, Raúl Espejel-Morales$^{a}$, Héctor Hernández-Coronado$^{a}$

$^{a}$Facultad de Ciencias, Universidad Nacional Autónoma de México,
Circuito Exterior s/n, Ciudad Universitaria,
Coyoacán, 04510, Ciudad de México

## Abstract
Graphene doped with nitrogen acts as a metal-free electrode, it has three times more catalytic activity than graphene and achieves the catalytic activity of the Pt. It has been proposed as an alternative to Pt since it would be cheaper and easier to produce. We report a computational analysis using dispersed corrected DFT calculations and molecular dynamics (MD). Adsorption properties, electronic properties, and stabilities in time of the adsorption of $CO_2$ molecule on defected graphene were studied. The MD was carried out at room temperature and in time of 0.8 ps. The defective graphene chosen has the following defects: Graphitic-N type defect, Pyridinic-N type defect, and a vacancy in graphene layer. The adsorption analysis gives the interaction type existing between the $CO_2$ molecule and the defected graphene, which is in the physisorption range. Also, it is proven here that the type of defect defines the interaction. Graphene with a vacancy and Pyridinic-N systems are p-type doping, indicating that electrons on the surfaces are pulled out and directed to the $CO_2$ molecule. The most stable system at room temperature is the graphitic-N, which present n-type doping, pulling electrons from the $CO_2$ molecule and stimulating the electrocatalytic activity for $CO_2$ conversion.

**Keywords:** Defective graphene, Gas adsorption, $CO_2$, Electronic structure,

---
*Corresponding author*
Email address: roxanadelcastillo@ciencias.unam.mx (Roxana M. del Castillo)

---
Preprint submitted to Journal of $\\LaTeX$ Templates
June 13, 2018

Molecular Dynamics

### 1. Introduction

Since the experimental discovery of graphene in 2004 [1, 2], it has captured an enormous attention of the scientists because it owns uniques physical properties, e.g., high thermal [3], optical [4], and electrical conductivity [5]. This high electrical conductivity makes graphene as an alternative to electro-catalytic applications [6]. Nitrogen impurities have been induced on graphene to simulate metal-free electrodes. These nitrogen impurities were introduced to manipulate electrical and chemical properties of pristine graphene [7, 8, 9]. The advantage of graphene-based nanodevices is that has three times more catalytic activity than pristine graphene [10] and would be cheaper than metal-based nanodevices. Thus, graphene doped with nitrogen is a viable alternative to platinum in catalytic processes at industrial scales [11]. In this work, we focused on the adsorption of $\text{CO}_2$ over defective graphene and nitrogen doped to determine the most stable system in which $\text{CO}_2$ can be transformed into a high-value product for industrial purposes, for instance, ethanol, methanol, etc [12].

According to previous experimental studies made by Kuhl et al. [13], it is highly viable to transform greenhouse gases, like $\text{CO}$ and $\text{CO}_2$, in hydrocarbon products. For this purpose, they used copper surfaces as a reduction electrode and transform $\text{CO}_2$ in ethylene. Also, there is another previous study in which it is made an electrochemical reduction of $\text{CO}_2$ to methanol over carbon nanotubes impregnated with $\text{Cu}_2\text{O}$ [14]. With these studies [13, 14], we hypothesized that defective graphene makes possible to reproduce those findings. The convenience of using graphene against metallic materials stems from the fact that graphene represents a cheaper alternative to recycle $\text{CO}_2$ on an industrial scale [15]. There are other experimental studies done by the group of Song [16], in which they find a high capability of graphene doped with Nitrogen to make an electrochemical conversion from $\text{CO}_2$ to ethanol. However, further theoretical studies are needed to compare with the experiments.

There are previous theoretical studies, in which it is investigating the in-
teractions between graphene and $CO_2$ molecule [17, 18]. They determine, with ab-initio methodology, that there is viable to trap the $CO_2$ over graphene and defective graphene in a very efficient way. Based on these studies it is that we propose the present work, deeping in the adsorption analysis and making new reactive studies and molecular dynamics studies. We focus on the characteriza-
tion of the adsorption mechanism of $CO_2$ over a graphene layer with different types of defects, through a study of their interactions, which are analyzed within the framework of adsorption sites and adsorption energies. It is analyzed the electronic properties and reactive sites. Also, molecular dynamics was carried out to make a complete stability analysis.

## 2. Computational Methodology

A supercell of 6×6 of defective graphene was fully relaxed. A $CO_2$ molecule was placed on defective graphene at a distance of 2.5 Å, in several places of the surface and different orientations. The sites chosen over the surface were; Top-site (over a C atom); in Bridge-site (over a C-C bond); and right in the middle of a carbon hexagonal ring. The $CO_2$ orientations were; horizontal orientation (parallel to the surface); and a vertical direction (with the $CO_2$ molecule perpendicular to the surface). Systematic searches have done, using all possible combinations of places and orientations. Here, only it is commented the most interesting ones.

The computational study is based on the energetic analyses; ground state structures; adsorption sites; adsorption energies; density of states; Löwdin charge analysis; and fukui reactivity analysis. Also, it was performed Verlet molecular dynamics simulations (MD). All theoretical characterizations were carried out with Quantum Espresso computational package [19]. Dispersion-corrected Den-
sity Functional Theory (DFT-D) calculations [20] were performed with the generalized gradient approximation (GGA), using Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional [21]. The empirical dispersion correction was

introduced through the framework proposed by Grimme (D3) [22, 23]. The methodology PBE+D3 is used to consider the van der Waals interaction, be-

cause it has proven to give accurate results and close to the experiments [24, 25]. The geometry optimization was carried out with a criterion of $10^{-8}$ Ry for energy, a kinetic energy cut-off for wavefunction of 40 Ry, and kinetic energy cut-off for charge density of 160 Ry. The integrations of the Brillouin-zone were made with the Methfessel-Paxton technique (0.05 Ry). The Monkhorst-pack

k-point grid (4×4×1) was used. Atoms C, N, and O were approached with Vanderbilt ultrasoft pseudopotentials [26] chosen from the Quantum Espresso website¹. The ab initio molecular dynamics were performed with Verlet algorithm [27], incorporated in Quantum Espresso computational package. These calculations were done with a no controlled in temperature and a microcanonical ensemble, the time step is of 0.05fs, producing a trajectory of 0.8ps, with a starting temperature of 300 K.

The thermodynamic stability was considered with the adsorption energies, given by

$$
E_{\text{ads}} = E_{\text{graphene+CO}_2} - \left[E_{\text{graphene}} + E_{\text{CO}_2}\right]. \tag{1}
$$

$E_{\text{graphene+mol}}$ is the energy of the whole system with the molecule adsorbed

on the defective graphene, $E_{\text{graphene}}$ is the energy of the defective graphene, and $E_{\text{mol}}$ is the energy of the $\text{CO}_2$ molecule in gas phase. These energies were obtained with the same methodology, previously mentioned.

On the other hand, to study the reactivity of the surfaces, the dual Fukui descriptor was used [28]. This descriptor is defined in terms of the difference between the nucleophilic $(f_A^+)$ and electrophilic $(f_A^-)$ Fukui functions as follows:

$$
\Delta f_A = f_A^+ - f_A^- = (Q_N^A - Q_{N+1}^A) - (Q_{N-1}^A - Q_N^A) = 2Q_N^A - Q_{N+1}^A - Q_{N-1}^A. \tag{2}
$$

---
¹Ultrasoft pseudopotentials for C, N, O were taken from the Pwscf PseudoPotential Download Page http://www.quantum-espresso.org (Files: `C.pbe-van_ak.UP`, `N.pbe-van_ak.UPF`, and `O.pbe-van_ak.UPF`).

## 3. Results and discussion

### 3.1. Adsorption analysis: Ground state structures, density of states, and fukui analysis

#### 3.1.1. Defective graphene before the adsorption

![](./images/813021007773171714_2.jpg)

Figure 1: Defective graphene supercell of 6×6.

The main advantage of introducing defects on the graphene is that they modify the electronic properties and the electrocatalytic activity is enhanced [31]. These defects introduced on pristine graphene are; graphitic-N, in which an N atom substitutes one C atom; a vacancy on the surface, it is removed one C atom; and a pyridinic N defect, one C atom is removed and other C atom is replaced by an N atom. The defects considered in the present paper are shown in **Figure 1**. The defective graphene chosen are compared with pristine graphene.

![](./images/813021007773171714_3.jpg)

Figure 2: LDOS of pristine graphene is shown in grey and is compared with graphene with defects; graphitic-N system (blue curve); graphene with a vacancy (green curve); and pyridinic-N system (pink curve).

To study the adsorption of $CO_2$ over graphene with defects, first, we compared the local electronic density of states (LDOS) of pristine graphene with defective graphene, see **Figure 2**. The LDOS are plotted to show the comparison between the majority states (spin-up) and the minority states (spin-down). For graphitic-N and pyridinic-N systems, there is not perceptible difference between the majority (spin-up) and the minority states (spin-down), indicating no magnetization in the system. Meanwhile, the graphene with a vacancy presents a slight difference between the spin-up and spin-down, giving a total magnetization of $1.12\ \mu B/cell$.

In previous works, the pristine graphene layers LDOS was compared against graphene with metallic atoms to describe the type of variation occurs in the material [8, 32]. In these studies, a methodology was used to determine the nature of doping induced in the defective graphene layer. In few words, this methodology indicates if the Fermi energy $(E_F)$ of defective graphene moves to the right of the Dirac point ($E_F$ of pristine graphene), there is $n$-type doping or if $E_F$ moves to left is p-type doping. In the graphitic-N system is observed that the defect induced by the N atom over the surface produces that $E_F$ shift to the right of the Dirac point. It is known that moving the $E_F$ to the right induces a $n$-type doping on the material, the charge is transferred from the adsorbate to the adsorbent [32]. Meanwhile, for graphene with a vacancy and the pyridinic-N system the charge transfer mechanism is $p$-type doping, the $E_F$ is on the left of the Dirac point, indicating the tendency of the surfaces to donate electrons to the adsorbates [32]. Also, the LDOS show us that the introduction of defects into the graphene surface increases the number of electronic states available at the $E_F$ as a function of the defect type. A consequence of the existence of more available states is that the electronic transport, conductivity, and catalytic activity can be modified and can have an improvement.

Table 1 shows the shift between the Dirac point and the $E_F$ of the defective graphene system graphene with a vacancy and pyridinic-N system is $p$-type doping.

Table 1: The shift between the Dirac point $(D)$ and the Fermi energy $(E_F)$ of the defective graphene. The sign reflects the type of Doping of each system.

<table>
  <thead>
    <tr>
      <th>SYSTEMS</th>
      <th>$D-E_F$ (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Graphene with a vacancy</td>
      <td>0.39</td>
    </tr>
    <tr>
      <td>Graphitic-N</td>
      <td>-0.89</td>
    </tr>
    <tr>
      <td>Pyridinic-N</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>

The reactivity study is made using the dual Fukui descriptor defined by Morell et al [28]. This descriptor is used for the characterization of nucleophilic-

ity and electrophilicity, at the same time, in terms of the variation of hardness with respect to the change of the external potential, given by equation 2. The main advantage of the dual descriptor is the immediately visualization of the nucleophilic and the electrophilic centers. Figure 3 shows the Dual Descriptor ($\Delta f_A$) evaluated in the defective graphene layers. The highest positive and negative indices denote a nucleophilic center (green) and an electrophilic center (orange), respectively.

Pristine graphene shows very low reactivity, an average of a dual descriptor of $\Delta f_A \approx 0.001$e is presented. The introduction of an N atom on pristine graphene (graphitic-N) increases the reactivity of the material with a dual descriptor in the N atom is $\Delta f_A \approx -0.016$e. This value of the $\Delta f_A$ indicates that the N atom stimulates the electrophilic attack, which corresponds with the N-doping character of the graphitic-N surface mentioned in a previous work [29]. The pyridinic-N layer shows an intense reactivity activity and there is an evident charge polarization on the surface and an increasing in the nucleophilic activity. The highest nucleophilic center has a $\Delta f_A$ of $\approx 0.032$e and the highest electrophilic center is $\Delta f_A \approx -0.022$e. Patently, the predominant behaviour is the nucleophilic activity, which is consistent with the $p$-type doping.

The vacancy graphene surfaces presents an increase in reactive activity than graphene, but not a reactive activity as significant as the surfaces doped with N. The main nucleophilic site is $\Delta f_A \approx 0.017$e and the main electrophilic site is $\Delta f_A \approx -0.048$e; indicating that the vacancy is not enough to promote the reactive activity on the surface.

![](./images/813021007773171714_4.jpg)

Figure 3: The Dual Fukui descriptor ($\Delta f_A$) evaluated in the pristine graphene layers. The nucleophilic centers and the electrophilic centers are shown in green and orange, respectively.

### 3.1.2. $CO_2$ adsorption over defective graphene

The initial site of the $CO_2$ molecule was chosen in based on the reactive activity presents in **Figure 3**, according to the previous methodology. The ground-state structures were found and are shown in **Figure 4**.

![](./images/813021007773171714_5.jpg)

Figure 4: The ground-state geometry of defective graphene layers with the adsorption of a CO₂ molecule.

Also, it is considered the binding energies. To make a clear difference between the $E_{ads}$ and $E_{bin}$ it is crucial to understand the concept of these two quantities. The adsorption energy can be disjointed in two parts; the binding energy ($E_{bin}$), which is the characterization of the interaction of the adsorbate molecule with the defective graphene; and the difference of the energy of an atomic array in the adsorption geometry (without the defective graphene) and the energy of the total number of isolated atoms ($E_{inter-ad}=E_{CO_2}-E_C-2E_O$) [30]. With these definitions, the binding energy is calculated with the following

equation:

$$E_{bin} = E_{inter-ad} - E_{ads}$$

Table 2: Adsorption energies of the ground-states systems, Binding energies and the distance of the $C$ of $CO_2$ and one middle $C$ of the defective graphene.

<table>
<thead>
<tr>
<th>SYSTEMS</th>
<th>$E_{ads}$ (kcal/mol)</th>
<th>$E_{bin}$ (kcal/mol)</th>
<th>Distance (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pristine graphene</td>
<td>-2.17</td>
<td>-5.32</td>
<td>4.04 (C-C)</td>
</tr>
<tr>
<td>Graphitic-N</td>
<td>-26.06</td>
<td>-5.00</td>
<td>3.37 (N-C)</td>
</tr>
<tr>
<td>Pyridinic-N</td>
<td>-2.77</td>
<td>-5.31</td>
<td>4.01 (N-C)</td>
</tr>
<tr>
<td>Graphene with a vacancy</td>
<td>-2.67</td>
<td>-5.31</td>
<td>3.57 (C-C)</td>
</tr>
</tbody>
</table>

Comparing our results with a previous work made by Ghosh et al. [17], they reported an$E_{bin}$ of -5.07 kcal/mol with a level theory of PBE and a DZP basis set. The difference between the result of Ghosh et al. and this work is that our system is periodical and we include the dispersion correction. A more recent work made by Takeuchi et al. [34] reported a $E_{bin}$ of -5.6 kcal/mol, with a more expensive level of theory (optB86b-vdW) and a smaller supercell (2x2), which makes that the interaction between $CO_2$-$CO_2$ molecules vital fact to account.

After optimizing the geometry, the ground-state structure for pristine graphene system is a horizontal line, in which the $CO_2$ molecule accommodates itself in a parallel position to the layer, in agreement with previous studies [35, 36]. According to a study made by Cabrera-Sanfelix [37], the adsorption energy of graphene-$CO_2$ is about 2.6 kcal/mol with a level theory of PW91. Taking into account these results and the dispersion correction, the $CO_2$ molecule has weak interactions with pristine graphene and the adsorption energy calculated is $E_{ads} = -0.094$ eV (-2.17 kcal/mol). The final distance between the $CO_2$ molecule and the graphene layer is 4.04 Å; this indicates that the $CO_2$ moves away from the graphene (the initial distance was 2.5 Å).

For graphitic-N surface, the ground-state configuration is the perpendicular position. All the configuration mentioned in the computational methodology

were used to found the ground state. In this systematic search, it was observed
that all systems with horizontal orientation of the $CO_2$ molecule were trans-
formed to systems in which the $CO_2$ molecules is in vertical position. The $CO_2$
is precisely above the atom the N atom, in Top-site position (T-site) wih an
adsorption energy of -1.13 eV (-26.06 kcal/mol) and a distance between C-N of
3.37 Å. Although the N-O interaction is stronger than the C-C ones, it is, still,
in the physisorption range.

In the case of the pyridinic-system, the systematic search of the ground state
gives that $CO_2$ molecule in vertical position turns down to be coupled in the
horizontal orientation. The vacancy of the pyridinic defects produces that the
$CO_2$ molecule attempt to fit in it, but this molecule is not small enough to
fit. The effective interactions are C-C, which makes possible this effect. The
adsorption energy of this system is -0.12 eV (-2.77 kcal/mol) with a bond length
of 4.01 Å, from the carbon atom of the $CO_2$ molecule to the N atom of the
pyridinic surface, the $CO_2$ aligned to the surface in a Top-site configuration.
In this case, the van der Waals interactions are predominant, as the adsorption
energies show. For graphene with a vacancy, the systematic search for the
ground states gives the same result as the pyridinic- N system, in which it
is observed that the vertical molecule turns down to place in it, with parallel
position, over the defective graphene. The system has an adsorption energy of
-0.116 eV (-2.67 kcal/mol), which is in physisorption regimen. The distance
between the N-C is 3.57 Å.

The adsorption energies of pyridinic-N-$CO_2$ and vacancy-$CO_2$ systems in-
crease of 0.6kcal/mol and 0.5 kcal/mol concerning pristine graphene, which
indicates that these defects stimulate the adsorption phenomenon. But, the
graphitic-N system presents a substantial increment, of 23.89 kcal/mol, in com-
parison with pristine. This fact also is seen in a shorter distance between the
$CO_2$ molecule-graphitic-N sheet and proves that the N atom and the vertical
position of the $CO_2$ promote the adsorption. Also the bonding phenomenom
makes that the bond lenght of the $CO_2$ molecules (1.17 Å) get a little more
longer than the gas phase (1.16 Å).

![](./images/813021007773171714_6.jpg)

Figure 5: LDOS for the adsorption of $CO_2$ molecule over defective graphene layers.

The LDOS of the ground-state structures are shown in **Figure 5**. The LDOS for pure graphene is shadowed in grey and the LDOS for graphene-$CO_2$ is shadowed in red. Comparing the LDOS of pristine graphene with graphene-$CO_2$ is possible to observe no difference between them. The main reason is that the $CO_2$ interacts very weakly with the graphene, making a little difference between the LDOS. The shift between the $E_F$ of graphene-$CO_2$ and the Dirac point is $D-E_F=-0.092$ eV. The charge is transferred from the $CO_2$ molecule to the graphene. Even though, the charge is going from $CO_2$ to the graphene layer, the LDOS in the $E_F$ is not populated, inclusive there is an energy gap

between the occupied and the virtual states, inhibiting the electronic transport.

The LDOS for graphitic-N system is shadowed in blue and the LDOS of the graphitic-N system with the adsorption of $CO_2$ is in color red. For the graphitic-N system with the adsorption of $CO_2$ molecule, the LDOS is hardly displaced to the right, including the $E_F$. This fact points that the charge is transferred from the molecule to the graphitic-N layer. As it can see, the shift between the $E_F$ of the graphitic-N system alone and the graphitic-N with the adsorption of the $CO_2$ molecule is very weak ($E_F^{\text{graphitic-N}} - E_F^{\text{graphitic-N-CO}_2} = -0.124$ eV); without a notable change in the electronic structure.

The LDOS for pyridinic-N system is overasted in purple and the LDOS of the pyridinic-N system with the adsorption of $CO_2$ is drawn in red. The charge is transferred from the $CO_2$ to the pyridinic-N system ($E_F^{\text{pyridinic-N}} - E_F^{\text{pyridinic-N-CO}_2} = -0.089$ eV). From the LDOS, it can be observed that there is not a significant variation between them, besides the slight shift of the $E_F$ to the right and a little more available states can be occupied by electrons.

The LDOS for graphene with a vacancy is shadowed in green and the LDOS for this system with the adsorption of $CO_2$ is marked in red. It is noticeable that $CO_2$ does not greatly distort the DOS, only produces a slight shift of $E_F$ to the right, indicating that the charge is transferred from the $CO_2$ to the defective graphene layer ($E_F^{\text{graphene vacancy}} - E_F^{\text{graphene vacancy - CO}_2} = -0.089$ eV). From the LDOS, it can be observed that there is no variation between the LDOS. The magnetization, which is presented in the defective graphene layer (graphene with a vacancy), does not longer holds in the adsorption of the $CO_2$.

The charge transfer goes from the $CO_2$ molecule to the defective graphene (see Table 3), as it is indicated in the type of doping observed in the LDOS, which is n-type doping. The highest electron transfer takes places in the pyridinic-N system, with a charge transfer around of $(-0.008e)$ due to the adsorption geometry is the horizontal line. The lowest electron transfer system is the graphitic-N $(-0.001e)$, which has the vertical line as the adsorption geometry.

<table>
<caption>Table 3: Charge if the $CO_2$ molecule ($Q_{CO_2}$) for defective graphene.</caption>
<thead>
<tr>
<th>SYSTEMS</th>
<th>$Q_{CO_2}$ (e)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Isolated</td>
<td>–</td>
</tr>
<tr>
<td>Pristine graphene</td>
<td>-0.002</td>
</tr>
<tr>
<td>Graphitic-N</td>
<td>-0.001</td>
</tr>
<tr>
<td>Pyridinic-N</td>
<td>-0.008</td>
</tr>
<tr>
<td>Graphene with a vacancy</td>
<td>-0.006</td>
</tr>
</tbody>
</table>

Figure 6 shows the dual descriptor of the adsorption of $CO_2$ on defective graphene layers ($\Delta f_A$). The effect of the $CO_2$ molecule on pristine graphene is polarize the surface, inducing a nucleophilic center with value of $\Delta f_A \approx 0.0285$e and two electrophilic centers of $\Delta f_A \approx -0.041\text{e}, -0.036\text{e}$, over the graphene. The $CO_2$ molecule presents $\Delta f_A$ values of C= -0.059e (an electrophilic center) and O= 0.021e, 0.016e (a nucleophilic centers), this indicate that the predominant interactions are C-C, over the C-O interactions, which made that the ground-state configuration is the horizontal one.

For graphitic-N system, the effect of the $CO_2$ molecule induced an imperceptible reactivity in the surface. The greatest nucleophilic center has a value of $\Delta f_A \approx 0.003\text{e}$, which is much more smaller that the value of the greatest electrophilic center $\Delta f_A \approx -0.024\text{e}$. The $CO_2$ molecule presents $\Delta f_A$ values of C= 0.013e (a nucleophilic center) and O= -0.015e, -0.016e (electrophilic centers), with a predominant interaction of N-O over the C-C interaction. Another interesting fact is that the O converts in electrophilic center, in comparison with the pristine graphene case.

For pyridinic-N system, there are two main nucleophilic centers over the surface, with value of $\Delta f_A \approx 0.0431\text{e}, 0.039\text{e}$. In the pyridinic defect, there is an electrophilic center with a value $\Delta f_A \approx -0.029\text{e}$. The $CO_2$ molecule presents $\Delta f_A$ values of C= 0.046e (as a nucleophilic center) and for the O atoms, $\Delta f_A = -0.020\text{e}, -0.012\text{e}$ (electrophilic centers). This reactivity analysis reflects how the charge is transfered, indicating that $CO_2$ molecule negative

doped the defective graphene layer.

For graphene with a vacancy, the effect of the $CO_2$ molecule on graphene induced nucleophilic activity on the surface. The main nucleophilic center has a value of $\Delta f_A \approx 0.026$e and the greater electrophilic value ($\Delta f_A \approx -0.020$e). The $CO_2$ molecule presents $\Delta f_A$ values of C= 0.048e (a nucleophilic center) and O= -0.022e, -0.016e (electrophilic centers).

From the dual descriptor, it is evident that the defects in the graphene promote the reactivity activity, making a significant improvement in the adsorption phenomenon. The graphitic-N system is the best system to adsorb the $CO_2$ molecule, and it is the best choice for a catalytic purpose due to the physisorption nature the fact that the geometry of the $CO_2$ molecule remains unchanged in comparison with the gas phase.

![](./images/813021007773171714_7.jpg)

Figure 6: The Dual Fukui descriptor ($\Delta f_A$) for the adsorption of $CO_2$ molecule over the defective graphene layers. The nucleophilic centers and the electrophilic centers are shown in green and orange, respectively.

### 3.2. Molecular Dynamics

From the optimized geometries and adsorption analysis, it is possible to see that the most stable system for $CO_2$ adsorption is the graphitic-N system.
275 Nevertheless, adsorption occurs with weak bonds, i.e. in physisorption regimens.
To explain these stabilities, we applied Verlet Molecular Dynamics (MD) to the ground-states geometries previously obtain to obseve how these structures change in time. **Figure 7** displays the final structures obtained by the MD at a time of 0.8 ps. These calculations were carried out with a no controlled
280 in temperature, a starting temperature of 300 K, a time step of 0.05fs, and a

microcanonical ensemble. Also, **Figure 7** shows how defective graphene bends due the effects of adsorption of the $CO_2$ molecule. The graphene and graphitic- N system arc just a little due the adsorption of the $CO_2$. The pyridinic-N and graphene with a vacancy have a more significant distortion in this lapse course.

From these results is possible to achieve the best temperature resisting system, which is the graphitic-N system. This system shows a less lattice deforma- tion and preserves the natural bidimensionality. The less stable system is pure graphene with one vacancy, which exhibits a significant lattice deformation on the surface.

![](./images/813021007773171714_8.jpg)

Figure 7: Final structures after Molecular Dynamics of defective graphene.

It is presented the Root mean square deviation (RMSD) in all the steps of the MD. In figure 8, it is shown the RMSD plots for the defective graphene systems. As indicated, there is an increase in the structural change of all the

systems. The most stable system is a graphitic-N system with the adsorption of $CO_2$, and the most unstable system is the graphene with a vacancy.

![](./images/813021007773171714_9.jpg)

Figure 8: Root mean square deviation (RMSD) for all the geometry systems in every step of the MD.

To quantify the distortion of the layer networks in terms of the time and the molecular stability, we considered the displacement of the defect around the equilibrium point and its evolution in time $D(t) = |z(t = 0) - z(t)|$ and the modification of the length C-O of the $CO_2$ molecule. These displacements are display in Figure 9 and Figure 10. As the geometries evolve over time, the surfaces show deformation in their network. An important fact is that displacement of defect depends, fundamentally, on the type of defect.

![](./images/813021007773171714_10.jpg)

Figure 9: Displacement over time of the defect around the equilibrium point ($D(t) = |z(t = 0) - z(t)|$).

![](./images/813021007773171714_11.jpg)

Figure 10: The length of the O-C bond of the CO₂ molecule versus time.

The graphitic-N-CO₂ system is the structure with less displacement of its defect (N) along to the equilibrium point. The displacement of this system is almost negligible ($\sim0.06$ $\mathring{A}$), in addition to staying constant with respect to time. The oscillations of the displacements remain fixed with respect to time, indicating that the N atom holds in its initial position and denoting high stability. Exactly like graphitic-N-CO₂ system, the pristine graphene system with the adsorption of CO₂ molecule has a neglible displacement of the defect. For this system, we considered the displacement of a central carbon atom of the surface, which is the closest to the CO₂ molecule. For the pyridinic-N-CO₂ system, a greater displacements are observed ($\sim0.09$ $\mathring{A}$). In fact, it is seen that larger amplitude oscilations exists, indicating a dimished in the stability over time. The graphene with a vacancy is the system which presents the greatest displacement of its defect with respect time, with a fairly considerable displacement of 0.097 $\mathring{A}$ to 0.115 $\mathring{A}$. In addition of the large displacement presented, this system displays greater oscillations of displacements, with a maximum amplitud of 0.017 $\mathring{A}$, which implies the well-known experimental instability of this system.

The bond length O-C of the CO₂ along time is shown in Figure 10. According to the MD dynamics, the bond length of the CO₂ molecule adsorbed in pristine graphene varies between 1.176 $\mathring{A}$ and 1.183 $\mathring{A}$. The bond length in the gas phase of the CO₂ molecule is around $1.177\mathring{A}$, implying that the molecule remains unchanged, which agrees with the horizontal orientation and the physisorption phenomenon previously observed. The graphitic-N-CO₂ system presents a shortening of the bond length ($1.173\mathring{A}$ to $1.183\mathring{A}$), which seems reasonable because the CO₂ molecule is in a perpendicular orientation. The pyridinic-N system presents a bond length around of $1.176\mathring{A}$ to $1.82\mathring{A}$; meanwhile, the vacancy has a bond length of $1.177\mathring{A}$ to $1.182\mathring{A}$, presenting a slight elongation.

The potential energy along time obtained by the MD is shown in Figure 11. The total potential energy of the system reached a steady standard trajectory value after the initial decline at around 200-250 ps. Simulation was done for a time period of 0.8 ps; the system was equilibrated well using the micocanonical

ensemble.

![](./images/813021007773171714_12.jpg)

Figure 11: Potential energy versus time.

Previous works have found a direct relationship between electronic transport
and the deformation of the surface, specially the breaking of the bidimensional-
ity of the network [32, 8]. It is known that by breaking of the bidimensionality
surface creates new scattering centres, so the electrons will suffer a decrease
in their mean free path and the electronic transport will be less efficient. For
catalytic purpose, it is essential that electrons are delocalized, allowing them to
be permissive for a possible electrocatalytic reaction. After the time course and
the changes in temperature, the graphitic-N system preserve the bidimensional-
ity of the material. This conservation of bidimensionality results in a diminish
of scattering centers that can affect the electronic transport. Also, graphitic-N
system presents $n$-type doping, pulling electrons from the adsorbed molecules,
accordingly with experimental studies [38, 39, 40]

## 4. Conclusions

It is known that when graphene is doped with nitrogen, there are induced different types of defects; graphitic-N; pyridinic-N; and graphene with a vacancy. In this work, we observe that these defects promote a reactive activity different
350 to graphene without defects. It can be seen that graphene-based systems have a weak interaction with $CO_2$ molecule. These weak interactions are marked by the type of defect that the system has, although the defects studied are not strong enough to induce more significant attraction to the molecules. For the graphitic-N system, this defect produces n-type doping in the layer, so there are many
355 electrophilic sites on the surface. For the pyridinic and graphene with a vacancy system, there is p-type doping, producing nucleophilic locations on the surface. The central fact of all this is that the adsorption of $CO_2$ is sufficient, even if it is in physisorption range, to modify the electronic behaviour of the material. For pyridinic -N and graphene with a vacancy system, it is observed a sharp
360 polarisation, inducing electrophilic and nucleophilic sites. In the present work, The most stable systems determined in this work are graphitic-N based systems, which present $n$-type doping, pulling electrons from the adsorbed molecules, accordingly with experimental studies.

From the LDOS, it was observed that the systems with a more definite ten-
365 dency to have a high electronic transport are the graphitic-N based system with the adsorption of $CO_2$, inducing a substantial increase of available states in the Fermi energy and in the DOS virtual zone. This result fits with the experimental results obtained by Song et al., in which they proposed that graphene doped with nitrogen enhanced the electrocatalytic activity.

370 At room temperature, also, the most stable system is the graphitic-N system, which presents a less network deformation, preserving the bidimensionality and having less scattering centres.


### 5. Acknowledgements

This research has been supported by DGTIC-UNAM, with the access to the Miztli-UNAM supercomputer, with the project LANCAD-UNAM-DGTIC-055. Also, authors would like to thank UNAM-DGAPA for the Postdoctoral grant of Roxana M. del Castillo. This work was supported by UNAM-PAPIIT projects IN114318.

### References

[1] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I.V. Grigorieva, A. A. Firsov, Electric Field Effect in Atomically Thin Carbon Films, Science. 306 (2004), 666-669.

[2] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, M. I Katsnelson., I. V. Grigorieva, S. V. Dubonos, A. A. Firsov, Two-dimensional gas of massless Dirac fermions in graphene, Nature. 438 (2005), 197-200.

[3] X. Xu, L.F.C. Pereira, Y. Wang, J. Wu, K. Zhang, X. Zhao, S. Bae, C.T. Bui, R. Xie, J.T.L. Thong, B.H. Hong, K.P. Loh, D. Donadio, B. Li, B. Özyilmaz. Length-dependent thermal conductivity in suspended single-layer graphene. Nature Communications 5 (2014).

[4] B.G. Ghamsari, J. Tosado, M. Yamamoto, M.S. Fuhrer, S.M. Anlage. Measuring the Complex Optical Conductivity of Graphene by Fabry-Pérot Reflectance Spectroscopy. Scientific Reports. 6 (2016), 34166.

[5] R. Raccichini, A. Varzi, S. Passerini, B. Scrosati. The role of graphene for electrochemical energy storage. Nature Materials. 14 (2015), 271–279

[6] A.J. Patil, J.L. Vickery, T.B. Scott, S. Mann, Aqueous Stabilization and Self-Assembly of Graphene Sheets into Layered Bio-Nanocomposites using DNA, Advanced Materials, 21 (2009), 3159-3164.

[7] L. Zhang, Q. Xu, J. Niua, Z. Xia, Role of lattice defects in catalytic activities of graphene clusters for fuel cells, Phys.Chem. Chem.Phys, 17 (2015), 16733-16743.

[8] R.M. Del Castillo, L.E Sansores, Study of the electronic structure of Ag, Au, Pt and Pd clusters, The European Physical Journal B, 88 (2015).

[9] Z. Hou, X. Wang, T. Ikeda, K. Terakura, M. Oshima, M. Kakimoto, S. Miy- ata, Interplay between nitrogen dopants and native point defects in graphene, Physical Review B, 85 (2012), 165439.

[10] L.Qu, Y. Liu, J.B Baek, L. Dai, Nitrogen-Doped Graphene as Efficient Metal-Free Electrocatalyst for Oxygen Reduction in Fuel Cells, ACS Nano, 4 (2010), 1321-1326.

[11] K.R. Paton, E. Varrla, C. Backes, R.J. Smith, U. Khan, A. O'Neill, C. Boland, M. Lotya, O.M. Istrate, P. King et al., Scalable production of large quantities of defect-free few-layer graphene by shear exfoliation in liquids, Nature Materials, 13 (2014), 624-630.

[12] F. Li, D MacFarlane, J. Zhang. Recent Advances in Nanoengineering of Electrocatalysts for $CO_2$ Reduction. Nanoscale (2018).

[13] K.P Kuhl, E.R Cave, D.N. Abram, T.F. Jaramillo, New insights into the electrochemical reduction of carbon dioxide on metallic copper surfaces, En- ergy Environ. Sci, 5 (2012), 7050-7059.

[14] M. Irfan Malik, Z.O Malaibari, M. Atieh, B. Abussaud, Electrochemical re- duction of $CO_2$ to methanol over MWCNTs impregnated with $CU_2O$. Chem- ical Engineering Science, 152 (2016), 468-477.

[15] K.R. Paton, E. Varrla, C. Backes, R.J. Smith, U. Khan, A. O'Neill, C. Boland, M. Lotya, O.M. Istrate, P. King, T. Higgins, S. Barwich, P. May, et al., Scalable production of large quantities of defect-free few-layer graphene by shear exfoliation in liquids. Nature Materials, 13 (2014), 624-630 .

[16] Y. Song, R. Peng, D.K. Hensley, P.V. Bonnesen, L. Liang, Z. Wu, H.M. Meyer III, M. Chi, C. Ma, B. Sumper, A.J. Rondinone, High-Selectivity Elec- trochemical Conversion of $CO_{2}$ to Ethanol using a Copper Nanoparticle/N Doped Graphene Electrode, ChemistrySelect, 1 (2016), 6055-6061.

[17] A. Ghosh, K.S. Subrahmanyam, K.S. Krishna, S. Datta, A. Govin- daraj,S.K. Pati, C.N.R. Rao, Uptake of $H_{2}$ and $CO_{2}$ by Graphene. J. Phys. Chem C 112 (2008), 15704-15707.

[18] J. Li, M. Hou, Y. Chen, W. Cen, Y. Chu, S. Yin. Enhanced $CO_{2}$ capture on graphene via N, S dual-doping. Applied Surface Science (2017) 399, 420-425.

[19] P. Giannozzi et al., QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials, J. Phys.: Condens. Matter, 21, 395502 (2009).

[20] R.G. Parr, Density Functional Theory, Ann. Rev. Phys. Chem, 34, 631-656 (1983).

[21] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett., 77 (1996), 3865,.

[22] S. Grimme, J. Antony, S. Ehrlich, H. Krieg, A consistent and accurate ab initio parametrization of density functional dispersion, The Journal of Chemical Physics, 132 (2010), 154104.

[23] S. Grimme, Semiempirical GGA-type density functional constructed with a long-range dispersion correction, Journal of Computational Chemistry, 27 (2006), 1787-1799.

[24] X. Fan, K. Elgammal, A.D. Smith, M. Östling, A. Delin, M.C. Lemme, F. Niklaus, Humidity and $CO_{2}$ gas sensing properties of double-layer graphene. Carbon, 127 (2018), 567-587.

[25] I.A. Pasti, A. Jovanovic, A.S Dobrota, S.V. Mentus, B. Johansson, N.V. Skorodumova, Atomic adsorption on graphene with a single vacancy: system-

atic DFT study through the periodic table of elements. Phys. Chem. Chem. Phys. 20 (2018), 858-865.

[26] D. Vanderbilt, Soft self-consistent pseudopotentiales in a generalized eigen- value formalism, Phys. Rev. B, 41, 7892-7895 (1990).

[27] L. Verlet, Computer "Experiments" on Classical Fluids. I. Thermodynam- ical Properties of Lennard-Jones Molecules. Physical Review, 159-1 (1967).

[28] C. Morell, A. Grand, A. Toro-Labbé, New Dual Descriptor for Chemical Reactivity. J. Phys. Chem. A. 109 (2005), 205-212.

[29] D. Cortés-Arrigada, Global and local reactivity indexes applied to under- stand the chemistry of graphene oxide and doped graphene. J. Mol. Model. 19 (2013) 919-930.

[30] M.L. Bocquet, A.M. Rappe, H.I. Dai,, A density functional theory study of adsorbate-induced work function change and binding energy: Olefins on Ag(111). Molecular Physcics, 103 (2005), 6-8, 883-890.

[31] Y. Ito, et al., Correlation between Chemical Dopants and Topological De- fects in Catalytically Active Nanoporous Graphene, Advanced Materials, 28 (2016), 10644-10651.

[32] R.M. Del Castillo, L.E. Sansores, Adsorption of Metal Clusters on Graphene and Their Effect on the Electrical Conductivity, Graphene Materi- als, Advanced Applications, 123-142 (2017), George Kyzas (Ed.)- INTECH, Lundon-UK.

[33] T. Schiros, D. Nordlund, L. Pálova, D. Prezzi, L. Zhao, K.S. Kim, U. Wurstbauer,C. Gutiérrez, D. Delongchamp, Ch. Jaye, D. Fischer, U. Oga- sawara, L.G.M. Pettersson, D.R. Reichman, P. Kim, M.S. Hybertsen, A.N. Pasupathy, Connecting Dopant Bond Type with Electronic Structure in N- Doped Graphene, Nano. Lett., 12 (2012), 4025-4031.


[34] K. Takeuchi, S. Yamamoto, Y. Hamamoto, Y. Shiozawa, Y. Tashima, K. Tashima, H. Fukidome, T. Koitaya, K. Mukai, S. Yoshimoto, M. Suemitsu, Y. Morikawa, Y Jun, J. Yoshinobu, I. Matsuda, Adsorption of $CO_2$ on Graphene: A Combined TPD, XPS, and vdW-DF Study. J. Phys. Chem. C. 121 (2017), 2807-2814,.

[35] K.J.Lee, S.J. Kim, Theoretical Investigation of $CO_2$ Adsorption on Graphene, Bull. Korean Chem. Soc., 34 (2013).

[36] D. Cortés-Arrigada, N. Villegas-Escobar, D. Ortega, Fe-doped graphene nanosheet as an adsorption platform of harmful gas molecule ($CO$, $CO_2$, $SO_2$ and $H_2S$), and the co-adsorption in $O_2$ enviroments. Applied Surface Science, 427 (2018), 227-236.

[37] P.Cabrera-Sanfelix, Adsorption and Reactivity of $CO_2$ on Defective Graphene Sheets. J. Phys. Chem. A, 113 (2009), 493-498.

[38] M. Fan, Ch. Zhu, Z. Feng, J. Yang, L., Liu, D. Sun, Preparation of N-doped graphene by reduction of graphene oxide with mixed microbial system and its haemocompatibility, Nanoscale, 9 (2014).

[39] Z. Wang, B. Li, Y. Xin, J. Liu, Y. Yao, Z. Zou Rapid synthesis of nitrogen-doped graphene by microwave heating for oxygen reduction reactions in al- kaline electrolyte, Chinese Journal of Catalysis, 35 (2014), 509-5134.

[40] T. Kondo, et al., Atomic-scale characterization of nitrogen-doped graphitic: Effects of dopant nitrogen on the local electronic structure of the surrounding carbon atoms, Physical Review B, 86 (2012), 035436.