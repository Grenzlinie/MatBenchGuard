Materials Science-Poland, 29(3), 2011, pp. 223-232
http://www.materialsscience.pwr.wroc.pl/
DOI: 10.2478/s13536-011-0035-3
![](./images/813329434646937600_1.jpg)

# Determination of the electronic band structure of the rutile polymorph of TiO₂: a quantum chemical approach

P.J. BARDZIŃSKI¹,²*

¹ Imperial College London, Thomas Young Centre, Computational Materials Science Group;
South Kensington Campus, Exhibition Road, London SW7 2AZ, Great Britain

² Wroclaw University of Technology, Institute of Materials Science and Technical Mechanics,
B1 building – room 110, Smoluchowskiego 25, 50-370 Wrocław, Poland

The aim of this work is the investigation of the relationship between the electronic band structure of the TiO₂ rutile and the dimensionality of the system. For three dimensional system the bulk form of rutile was considered, while a slab model was chosen in order to represent the titanium (IV) dioxide (110) surface. The influence of changing the number of atomic layers on the bandgap value for the (110) surface was also examined. Density of states referring to the bands from the first valence band up to the bottom of the conduction band was projected on the whole set of atomic orbitals as well as on the significant shells of the titanium and oxygen atoms. Ab initio calculations with a B3LYP functional were carried out. Basis sets used were modified Ti_86-411(d31)G_darco_unpub and O_8-411_muscat_1999. The results are compared with experimental and computational data already available in the literature. Surface termination problem was discussed and the application of the obtained results as a starting point to obtain the first model of the rutile titania nanotube was proposed. The surface formation energies for rutile planes with a different surface terminations were compared and the modification to the equation needed for surface energy calculation was introduced.

Keywords: rutile, band structure, B3LYP, surface termination, surface formation energy

© Wroclaw University of Technology.

## 1. Introduction

In the recent years, titanium (IV) dioxide in its various structural forms was attracting attention of the researchers from many fields. It is due to its many possible applications, such as photocatalysis [1], solar cells [2] or water photocleavage [3], which could be significant for the renewable energy eco- nomy. The focus on this particular compound, TiO₂, results from its unique physico-chemical properties, which distinguishes it among others, rendering it the best material for the mentioned applications [4]. Thus, it becomes obvious that determination of the electronical structure as well as the value of corre- sponding electronic and optical bandgap of the ma- terial is becoming a task of prior importance, both for experimental [5, 6] and theoretical [7] research groups. In this work, the mentioned quantities were calculated from first principles. Due to significant inaccuracy in estimation of the bandgap value in the cases when pure HF (Hartree-Fock) or DFT (Density Functional Theory) functionals were used [7, 8], the hybrid functional was chosen, as in the work of Zhang Yong-fan *et al.* [9] or Nilsing *et al.* [10], which show, that the approach like this could lead to much better results.

## 2. Methodology

In this work, quantum mechanical calculation have been performed. The method adopted to solve the time independent Schrödinger equation is the Density Functional Theory (DFT). The hamilto- nian consists of a kinetic energy part and a part describing potential, which takes into account both the exchange and the Coulomb-type electron cor- relation. The main approximation used is a Born- Oppenheimer approximation, where the total wave- funtion is a product of the electronic and nuclear wavefunctions that are computed separately.

The wave function of a crystal is approximated by means of a linear combination of atomic orbitals

*E-mail: piotr.bardzinski@pwr.wroc.pl
![](./images/813329434646937600_2.jpg)

(LCAO). For a periodic system – like a crystal – each crystalline orbital is expressed by a linear combination of Bloch functions. These Bloch functions start from the atomic orbitals, which are given by a linear combination of Gaussian type functions.

## 3. Calculations
The calculations were carried out using the CRYSTAL06 software [11], except those for the purpose of evaluating the surface formation energy, which were done using Gaussian09 [12]. For visualizations the DLV [13] was utilized. The model of a surface was obtained by cutting out from the optimized bulk crystal structure a two dimensional infinite system, normal to the chosen (110) plane. This is called the slab approach.

It is known that while the bandgap value of a semiconductor is usually overestimated when the HF approach is used, pure DFT methods give the underestimated width of the bandgap. It was the reason of choosing the hybrid, B3LYP (Becke-3 parameter-Lee-Yang-Parr) functional in this work. The form of the functional [14] used is as following:

$$
E_{exch-corr}^{B3LYP} = 0.80(E_{exch}^{LDA} + 90E_{exch}^{Becke}) + 20E_{exch}^{HF} + 0.19E_{corr}^{VWN} + 0.81E_{corr}^{LYP}
$$

where $E_{exch}^{LDA}$ is a local density approximation (LDA) exchange functional of the electron density, $E_{exch}^{Becke}$ is the exchange functional of Becke, $E_{exch}^{HF}$ is the exact Hartree-Fock exchange functional, $E_{corr}^{VWN}$ is the Vosko-Wilk-Nusair, LDA correlation functional and $E_{corr}^{LYP}$ is the Lee-Yang-Parr correlation functional.

In this work, the shrinking factor with the value of 8 was chosen for the Monkhorst net, which corresponds to 75 k points in the Irreducible Brillouin Zone. The restricted closed shell formalism with a Kohn-Sham hamiltonian was applied in the calculations performed.

The basis set chosen for titanium atom was shown in the Appendix, which is available on the website: http://www.immt.pwr.wroc.pl/~bardzinski/MatSciPol/APPENDIX_rutile.pdf.

The core part of the basis set chosen for Ti atom is the same as the Ti_86-411(d31)G_darco_unpub [15, 16]. The exponents in the functions describing two additional sp shells were changed from 0.8099 and 0.3242 to 0.8126 and 0.3297, respectively. For the first titanium d shell, the number of primitives GTF $n_g$ was changed from 3 to 4. All of the exponents as well as their corresponding contraction coefficients were changed from 7.6781 0.1127, 1.8117 0.3927, 0.4630 0.5206, to: 16.2685 0.0675, 4.3719 0.2934, 1.4640 0.5658 and one extra function was added to describe this d shell, with an exponent (which is the most diffuse) set to 0.5485 and contraction coefficient of 0.5450. Note that the formal charge of this d shell was set to 2 instead of 0, as it was in the previous version of the basis set. In the last d shell from the original basis set, the exponent was changed from 0.23 to 0.26. The basis set for oxygen was the O_8-411_muscat_1999 [17, 18] with a minor modification. Namely, the extra d shell was added, described with the function with an exponent of 0.6 and the value of 1.0 of its corresponding coefficient.

For the titanium 3d shell, the fourth exponent, with a value of $5.485*10^{-1}$ is the most diffuse, while for 2 sp and 3 sp Ti shells the most diffuse exponents are the sixth (2.412) and the fourth (1.890), respectively. For the oxygen 2 sp shell, the most diffuse exponent is the fourth one, with a value of 1.217. The use of the modified basis sets led to the minor improvement of the resulting total energy value of the system, which was slightly lowered. The space group of rutile polymorph of TiO₂ is $P4_2/mnm$ – which corresponds to 16 symmetry operators – when the three dimensional system (bulk) is considered. However, in the case of the (110) surface (slab), the number of symmetry operators (there are 8 symmetry operators, instead of 16) is decreased with respect to the bulk and thus, the space group is different.

**Table 1.** Final optimized lattice parameters for 3D and 2D systems. They are given in Angstroms and degrees.

<table>
  <thead>
    <tr>
      <th colspan="3">Dimensionality of the system – 3</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>$\alpha$</th>
      <th>$\beta$</th>
      <th>$\gamma$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>B3LYP</td>
      <td>4.6391</td>
      <td>4.6391</td>
      <td>2.9794</td>
      <td>90</td>
      <td>90</td>
      <td>90</td>
    </tr>
    <tr>
      <td>experimental [19]</td>
      <td>4.5931</td>
      <td>4.5931</td>
      <td>2.9589</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th colspan="3">Dimensionality of the system – 2</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th></th>
      <th>$\gamma$</th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <td>B3LYP</td>
      <td>2.9794</td>
      <td>6.5607</td>
      <td></td>
      <td>90</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 2.** Coordinates of atoms in the primitive cell (given in fractionary units) obtained after the final optimization for the 3D system of bulk rutile and their experimental counterparts from the neutron powder diffraction method [19] obtained at the temperature of 15 K.

<table>
  <thead>
    <tr>
      <th></th>
      <th>atom</th>
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">this work (optimized)</td>
      <td>Ti</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.306153</td>
      <td>0.306153</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">experimental [19]</td>
      <td>Ti</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.306153</td>
      <td>0.306153</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

Full optimization, involving both cell parameters and atomic coordinates was performed for the bulk. It is worth mentioning, that atoms in the internal part of the slab had the literature-based parameters with respect to their counterparts in the bulk, thus in the case of a slab, only the atomic coordinates were optimized. The parameters obtained after final optimization for the three- and two-dimensional systems are given in Table 1. Note that the C-parameter in 2D system refers to non periodic direction, and thus was formally set to 500 Å. The related neutron powder diffraction data [19] obtained at the temperature of 15 K is also added for comparison.

The finally optimized coordinates of the atoms in the primitive cell (given in fractionary units) and their corresponding experimental [19] values are collected in Table 2. The calculated deviation for the $x$ and $y$ coordinates (where $x=y$) was 0.48 %. The (110) plane was defined and the slab was chosen to describe the surface, with the thickness of 9 atomic layers and surface termination on the layer built up from the oxygen anions.

The volume of the 3D cell was 64.120 Å³ with a density of 4.138 g/cm³ and the area of the 2D cell was 19.547 Å². The number of atoms in the asymmetric unit and in the unit cell, are 2 and 6 for 3D system and 9 and 18 for 2D system, respectively.

The density of states (DOS) was calculated by means of a Fourier-Legendre method. The Legendre polynomial with a degree of 12 was used for DOS expansion in every calculation. The DOS was covering the bands from the first valence band up to the bottom of the conduction band. In the case of 9 layers (110) rutile slab, the energy range in which the DOS was computed, was from $-1.03230$ to $-0.13504\ \text{E}_\text{h}$ (from band 67 to 119) and for the bulk it was from $-0.87736$ to $0.04113\ \text{E}_\text{h}$ (which covers the band range from band 23 to 43).

## 4. Results

The calculations for a bulk rutile have been performed for the cell with 6 atoms, 76 electrons (from which 44 are core electrons), and the number of symmetry operators was 16. Similarly, for the (110) surface slab, there were 18 atoms per cell, 228 electrons per cell (132 core electrons), and 8 symmetry operators. The resulting band structure is presented in Fig. 1. The calculated value for a direct bandgap of the bulk rutile was $3.4063\ \text{eV}\ (0.1252\ \text{E}_\text{h})$. For the (110) surface it was equal to $2.8982\ \text{eV}\ (0.1065\ \text{E}_\text{h})$. The influence of changing the number of atomic layers, while other parametrs of the calculation remained the same, on the bandgap value of the (110) TiO₂ rutile surface was studied and shown in Table 3. The corresponding primitive cells for each system are given in Fig. 2 and Fig. 3, respectively.

### 4.1. Surface termination problem

According to the Tasker's work [20], when a dipole moment is present in the unit that is repeated in the direction perpendicular to the surface, it leads to the situation where the surface energy is tending to infinity and thus such layer is unstable without the addition of certain defects. The author distinguishes three types of surfaces that can be present in a ionic crystal. In the first type, the surface is composed of planes with alternating ions of opposite charges, rendering the whole structure electrostatically neu-

![](./images/813329434646937600_3.jpg)

Fig. 1. The electronic band structure of the rutile TiO₂ from the first valence band up to five unoccupied bands above the total number of occupied bands. Note that figure on the left corresponds to the bulk rutile, while the one on right side is related to its (110) surface with 9 atomic layers.

![](./images/813329434646937600_4.jpg)

Fig. 2. The primitive cell of the bulk rutile TiO₂. Note that large and small spheres are O and Ti, respectively.

![](./images/813329434646937600_5.jpg)

Fig. 3. The primitive cell of the TiO₂ rutile slab (built up from 9 atomic layers), with two lattice vectors perpendicular to [110] direction. Note that large and small spheres are O and Ti, respectively.

![](./images/813329434646937600_6.jpg)

Fig. 4. The slab model of the $TiO_{2}$ rutile (110) surface was constructed from 6 atomic layers in order to show the periodicity. Subsequent figures are representing the surface termination on the first, second and third layer, respectively. The large spheres refer to oxygen, while small ones are the titanium atoms.

Table 3. Electronic bandgap values (given in [eV]), obtained from the calculations for a different number of atomic layers for a (110) plane of $TiO_{2}$ rutile. The experimental data are also shown for a comparison.

<table>
  <thead>
    <tr>
      <th>Number of layers</th>
      <th>Bandgap [eV]</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3</td>
      <td>0.0018</td>
      <td>this work</td>
    </tr>
    <tr>
      <td>6</td>
      <td>4.0616</td>
      <td>this work</td>
    </tr>
    <tr>
      <td>9</td>
      <td>2.8982</td>
      <td>this work</td>
    </tr>
    <tr>
      <td>surface (110)</td>
      <td>3.40</td>
      <td>experimental [23]</td>
    </tr>
    <tr>
      <td>surface (110)</td>
      <td>3.37</td>
      <td>experimental [24]</td>
    </tr>
  </tbody>
</table>

tral. Due to the arrangement of ions in the studied rutile lattice, such surface is not possible to obtain. The second one is built of a symmetrical stack of charged planes with no dipole moment normal to the surface. The last type is a charged surface with a perpendicular dipole moment. It is important to note that each atomic layer can be charged or neutral, but the slab may consist of many atomic layers. This leads to the conclusion that by changing the sequence of them, one can change the type of the resulting surface.

In this work, it was shown in Fig. 4, that the (110) surface termination on the first or third atomic layer (which are the equivalent but rotated variants of rutile surface termination) leads to such charged surface (with the two outer layers of $O^{2-}$). It was the reason of choosing the second atomic layer as a surface termination in the current work. Although such choice also revealed a charged layer, there is no dipole moment in the repeating sequence for the planar charge density. In this case, the neutral plane with ions of both charges lies under the layer built of $O^{2-}$ anions and there are two $O^{2-}$ layers underneath the neutral plane.

### 4.2. Surface formation energy

The formation energy of the rutile (110) surface, was calculated from the modified form of the equation 87 proposed by Lipkowitz *et al.* [21], which looks as following:

$$
E_{surface}^{n-layers} = \frac{E_n - kE_{bulk}}{2A}
$$

where $E_n$ is the energy of the slab, n is a number of layers forming a model of the surface, $E_{bulk}$ is the energy per atomic layer in three-dimensional system and A is the area of the primitive surface unit cell (which was found to be equal to 19,547 $\mathring{A}^2$).

The original equation was modified by substituting k, the number of repetitive units in a direction normal to the surface, for n, which stands for the number of atomic layers the slab was composed of. For the metal oxide surfaces which have only one atomic layer as a repetitive unit – such as MgO (100) – the application of the original equation is leading to the correct values of $E_{surface}^{n-layers}$. However, if the repetitive unit is made of more non-identical atomic planes, what we encounter in the case of $TiO_2$ (110) rutile, the equation yields unphysical values of surface formation energy, of the order of tens of $kJ/m^2$, as we can see in Table 4. It was confirmed for three and six atomic layers chosen to

Table 4. A comparison of the surface formation energies $E_{surface}$ for 3 and 6 layers (110) TiO₂ rutile slab with a surface termination on the second atomic plane, obtained by using the equation suggested in the book of Lipkowitz *et al.* [21] and its modified form. "n" stands for the number of layers in a slab, while "k" is a number of repetitive units in a direction perpendicular to the surface. Take note that the bulk energy was $-1994,39502$ Ha.

<table>
  <thead>
    <tr>
      <th>n</th>
      <th>k</th>
      <th>Slab energy [Ha]</th>
      <th>$E_{surface}[kJ/m^{2}]$ – original equation [21]</th>
      <th>$E_{surface}[J/m^{2}]$ modified equation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3</td>
      <td>1</td>
      <td>$-1994,19514$</td>
      <td>44,49</td>
      <td>2,23</td>
    </tr>
    <tr>
      <td>6</td>
      <td>2</td>
      <td>$-3988,62097$</td>
      <td>88,97</td>
      <td>1,89</td>
    </tr>
  </tbody>
</table>

Table 5. Surface formation energies $E_{surface}$ of a (110) TiO₂ rutile, for different atomic layers chosen for surface termination. The bulk energy was equal to $-1994,39502$ Ha. The energies were calculated from the modified equation, developed in this work.

<table>
  <thead>
    <tr>
      <th>Termination layer</th>
      <th>$E_{surface}[J/m^{2}]$</th>
      <th>Slab energy [Ha]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3,96</td>
      <td>$-1994,04024$</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2,23</td>
      <td>$-1994,19514$</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3,96</td>
      <td>$-1994,04024$</td>
    </tr>
  </tbody>
</table>

build a model of the examined surface. If one use k instead of n in the equation, the obtained values of energy will be of the order of a few $J/m^{2}$, similar to those obtained by Kiejna *et al.* [22].

The results given in Table 5 confirm my previous assumption about the stability of the chosen model of the rutile plane. The surface termination on the second atomic layer leads to the most stable (in the terms of surface formation energy) TiO₂ rutile (110) surface.

## 5. Discussion and conclusions

It was clearly shown in Fig. 5 that the conduction band in both bulk and 9-layer (110) surface of rutile is primarily composed of titanium 3d shells, while the main contribution to the upper valence band is from the oxygen 2p shells with a minor participation of the titanium 3d shells. The oxygen 2s shells have the major contribution to the lower valence band. In Fig. 6 we can see the dominant contribution for the conduction band of titanium atomic orbitals, while the valence band is mainly composed of the oxygen orbitals.

The obtained bandgap value for the bulk rutile, namely 3.41 eV, was the same as obtained by J. Muscat *et al.* [25], but higher than the one presented by M. Nilsing *et al.* [10], who also used B3LYP functional to estimate the rutile TiO₂ bandgap. The obtained value, although still not perfect in comparison with experimental data which is 3.02–3.16 eV [24, 26, 27], is far much more accurate than the corresponding values obtained by LDA (Local Density Approximation) or GGA (Generalized Gradient Approximation) DFT calculations [7, 8], collected in Table 6.

However, the value of $E_{g}$ for the (110) surface of rutile TiO₂, was approximately 2.90 eV, and was suprisingly much lower than the value of around 3.40 eV (obtained by S. Fujiyoshi *et al.* [23]).

The similar calculations, also carried out with a B3LYP functional – undertaken by M. Nilsing *et al.* [10] – returned the value of 3.70 eV for the rutile (110) surface, which overestimates the experimental one. The discrepancies might be due to the use of different basis sets in each case.

According to the results given in Table 3, there is a strong, nonlinear dependence of the bandgap value with respect to the given number of atomic layers. It could indicate, that quantization of states can vary in the direction perpendicular to the TiO₂ surface, when additional atomic layers are inserted to the slab model. Introduction of such extra layers may lead to the formation of the new discrete states, that will be more energetically preferred by the valence electrons in the system. The combination of constant electronic band structure related to

![](./images/813329434646937600_7.jpg)

Fig. 5. The density of states projected on the s and p subsets of atomic orbitals of Oxygen and d subset of atomic orbitals for Titanium. The figure on the left corresponds to the bulk rutile, while the one on the right to the 9 layers (110) rutile TiO₂ surface. Note that only valence bands and five unoccupied bands above the total number of occupied bands are considered.

![](./images/813329434646937600_8.jpg)

Fig. 6. The density of states projected on the whole set of atomic orbitals of all of the Oxygen and Titanium atoms in the unit cell. The figure on left side shows the DOS of bulk rutile and the second one is related to 9 layers (110) rutile TiO₂ surface. Only the valence bands and first five conduction bands are taken into account.

infinite TiO₂ plane and the distribution of energy levels in the direction normal to the surface, which is a function of a number of layers, might lead to the observed oscillations of the bandgap value. In different cases, the $E_g$ was overestimated (6 layers) or slightly underestimated (9 layers) but for 3 layers the underestimation was three fold in comparison with a corresponding experimental value for the (110) surface. However, the last mentioned case might be analogical to the graphene-like structure [28].

Anyway, the above calculations clearly show that the utilization of the hybrid functional leads to better results than the HF or DFT functional alone. The approach needs modifications to improve the accuracy in the bandgap determination, mainly by making it independent from the chosen basis set.

### 5.1. Future work

Recently, many groups have been focusing their research on the titania nanotubes, because of their wide spectrum of possible applications [31, 32]. According to the literature, both anatase and rutile phases in this nanoscale tubular structures of TiO₂ are possible to occur [33]. While it was an exten-

Table 6. Comparison of results obtained both in experimental and computational determina- tions of pure rutile TiO₂ bandgap.

<table>
  <thead>
    <tr>
      <th>System</th>
      <th>$E_g$ [eV]</th>
      <th>Method</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bulk</td>
      <td>3.20</td>
      <td>B3LYP</td>
      <td>[10]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>3.40</td>
      <td>B3LYP</td>
      <td>[25]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>1.90</td>
      <td>EV-GGA, $E_g$ from DOS calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>2.14</td>
      <td>EV-GGA, $E_g$ from optical calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>3.03</td>
      <td>experimental</td>
      <td>[24]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>3.02</td>
      <td>experimental</td>
      <td>[26]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>3.16</td>
      <td>experimental</td>
      <td>[27]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>1.84</td>
      <td>GGA</td>
      <td>[8]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>1.85</td>
      <td>GGA-PBE</td>
      <td>[29]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>1.39</td>
      <td>GGA: WIEN2K (FP-LAPW), $E_g$ from DOS calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>2.01</td>
      <td>GGA: WIEN2K (FP-LAPW), $E_g$ from optical calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>1.56</td>
      <td>GGA+SOC , $E_g$ from DOS calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>2.00</td>
      <td>GGA+SOC , $E_g$ from optical calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>3.25</td>
      <td>LCMTO</td>
      <td>[30]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>2.99</td>
      <td>LDA with 13 % HF exchange</td>
      <td>[9]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>1.44</td>
      <td>LDA+SOC, $E_g$ from DOS calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>1.30</td>
      <td>LDA+SOC, $E_g$ from DOS calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>1.91</td>
      <td>LDA+SOC, $E_g$ from optical calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>bulk</td>
      <td>1.93</td>
      <td>LDA+SOC, $E_g$ from optical calculations</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>surface (110)</td>
      <td>3.70</td>
      <td>B3LYP</td>
      <td>[10]</td>
    </tr>
    <tr>
      <td>surface (110)</td>
      <td>3.40</td>
      <td>experimental</td>
      <td>[23]</td>
    </tr>
    <tr>
      <td>surface</td>
      <td>3.37</td>
      <td>experimental</td>
      <td>[24]</td>
    </tr>
    <tr>
      <td>surface (110)</td>
      <td>3.50</td>
      <td>GGA+U (U = 2.0)</td>
      <td>[8]</td>
    </tr>
  </tbody>
</table>

sive experimental investigation of these structures [34–40], there are only a few papers [33, 41, 42] related to theoretical models thereof, and most probably all of them are devoted to only the anatase phase.

The present work thus could serve as a starting point to obtain the first model of the rutile titania nanotube, however, some additional computational effort should be done in order to verify the stability of such thin TiO₂ (110) sheets and their tendency to self-reconstruction must be also investigated. The way to move from the rutile (110) surface to the respective nanotube is to wrap the (110) rutile slab longwise the [001] direction [41]. The other option is to replace some of the surface oxygen ions with the OH ones, what could lead to the torsion of the surface and subsequent nanotube formation. Such behavior could be observed after the treatment of the titanium (IV) oxide with a solution of NaOH [43, 44]. This opens a wide field of research, because many variables could be taken into account, such as the relationship between the bandgap and the internal diameter of the nanotube, number of atomic layers of which it is composed or the dependence of light absorption versus the curvature and length.

### Acknowledgements
The project was realized under the terms of the Lifelong Learning Programme – Erasmus Student Work Placement grant of the European Community and the Undergraduate Research Opportunities Programme (UROP) of the Imperial College of Science, Technology and Medicine in London. Author wanted to acknowledge Mr Prof. Nicholas M. Harrison for the overall supervision and Mr Dr Giuseppe Mallia, as well as Mr Dr Leandro Liborio (ICL) and Mr Dr Pawel Scharoch (WUT) for the useful discussions. Special thanks must be given to the Wroclaw Centre for Networking and Supercomputing where a Gaussian09 part of the calculations was realized.

## References

[1] ZHAO L., HAN M., LIAN J., *Thin Solid Films*, 516(10) (2008), 3394–3398.

[2] MOSADDEQ-UR-RAHMAN MD., MURALI KRISHNA K., MIKI T., SOGA T., IGARASHI K., TANEMURA S., UMENO M., *Solar Energy Mat. Solar Cells*, 48(1-4) (1997), 123–130.

[3] BRUDNIK A., GORZKOWSKA-SOBAS A., PAMULA E., RADECKA M., ZAKRZEWSKA K., *J. Power Sources – X Pol. Conf. on Syst. with Fast Ion. Trans.*, 173(2) (2007), 774–780.

[4] NOZIK A.J., *Nature*, 257 (1975), 383–386.

[5] PARK Y.R., KIM K.J., *Thin Solid Films*, 484(1-2) (2005), 34–38.

[6] TIAN G.-L., HE H.-B., SHAO J.-D., *Chin. Phys. Lett.*, 22(7) (2005), 1787–1789.

[7] BAIZAEE S.M., MOUSAVI N., *Phys. B: Cond. Matt.*, 404(16) (2009), 2111–2116.

[8] MORGAN B.J., WATSON G.W., *Surf. Sci.*, 601(21) (2007), 5034–5041.

[9] ZHANG Y.-F., LIN W., LI Y., DING K.-N., LI J.-Q., *J. Phys. Chem. B*, 109 (2005), 19270–19277.

[10] NILSING M., PERSSON P., LUNELL S., OJAMAE L., *J. Phys. Chem. C*, 111 (2007), 12116–12123.

[11] DOVESI R., SAUNDERS V.R., ROETTI R., ORLANDO R., ZICOVICH-WILSON C.M., PASCALE F., CIVAL- LERI B., DOLL K., HARRISON N.M., BUSH I.J., DARCO P., LLUNELL M., *CRYSTAL06, Release: 1.0; V1.0.2 fix-sequential executable; CRYSTAL06 User's Manual*, University of Torino, Torino, 2006.

[12] FRISCH M.J., TRUCKS G.W., SCHLEGEL H.B., SCUSE- RIA G.E., ROBB M.A., CHEESEMAN J.R., SCALMANI G., BARONE V., MENNUCCI B., PETERSSON G.A., NAKATSUJI H., CARICATO M., LI X., HRATCHIAN H.P., IZMAYLOV A.F., BLOINO J., ZHENG G., SON- NENBERG J.L., HADA M., EHARA M., TOYOTA K., FUKUDA R., HASEGAWA J., ISHIDA M., NAKAJIMA T., HONDA Y., KITAO O., NAKAI H., VREVEN T., MONTGOMERY JR. J.A., PERALTA J.E., OGLIARO F., BEARPARK M., HEYD J.J., BROTHERS E., KUDIN K.N., STAROVEROV V.N., KOBAYASHI R., NORMAND J., RAGHAVACHARI K., RENDELL A., BURANT J.C., IYENGAR S.S., TOMASI J., COSSI M., REGA N., MILLAM J.M., KLENE M., KNOX J.E., CROSS J.B., BAKKEN V., ADAMO C., JARAMILLO J., GOMPERTS R., STRATMANN R.E., YAZYEV O., AUSTIN A.J., CAMMI R., POMELLI C., OCHTERSKI J.W., MAR- TIN R.L., MOROKUMA K., ZAKRZEWSKI V.G., VOTH G.A., SALVADOR P., DANNEN-BERG J.J., DAPPRICH S., DANIELS A.D., FARKAS O., FORESMAN J.B., OR- TIZ J.V., CIOSLOWSKI J., FOX D.J., *Gaussian 09. Revi- sion A.02*, Gaussian, Inc., Wallingford CT, 2009.

[13] SEARLE B.G., *Comp. Phys. Commun.*, 137 (2001), 25.

[14] VOSKO S.H., WILK L., NUSAIR M., *Can. J. Phys.*, 58(8) (1980), 1200.

[15] BREDOW T., HEITJANS P., WILKENING M., *Phys. Rev. B*, 70 (2004), 115111.

[16] CORA F., *Mol. Phys.*, 103 (2005), 2483–2496.

[17] MUSCAT J., *PhD Thesis*, University of Manchester, Manchester, 1999.

[18] SCARANTO J., GIORGIANNI S., *J. Mol. Struct. THEOCHEM*, 858 (2008), 72–76.

[19] BURDETT J.K., HUGBANKS T., MILLER G.J., RICHARDSON JR. J.W., SMITH J.V., *J. Am. Chem. Soc.*, 109 (1987), 3639–3646.

[20] TASKER P.W., *J. Phys. C: Solid State Phys.*, 12 (1979), 4977–4984.

[21] LIPKOWITZ K.B., BOYD B.D., LARTER R., CUNDARI T.R., *Rev. Comput. Chem.*, 21 (2005), 70.

[22] KIEJNA A., PABISIAK T., GAO S.W., *J. Phys.: Cond. Matt.*, 18(17) (2006), 4209.

[23] SATORU F., TAKA-AKI I., HIROSHI O., *J. Phys. Chem. B*, 109 (2005), 8557–8561.

[24] TANEMURA S., MIAO L., JIN P., KANEKO K., TERAI A., NABATOVA-GABAIN N., *App. Surf. Sci. – 11ᵗʰ Intern. Conf. on Solid Films and Surf.*, 212–213 (2003), 654–660.

[25] MUSCAT J., WANDER A., HARRISON N.M., *Chem. Phys. Lett.*, 342(3-4) (2001), 397–401.

[26] PASCUAL J., CAMASSEL J., MATHIEU H., *Phys. Rev. B*, 18(10) (1978), 5606–5614.

[27] NOWOTNY J., BAK T., BURG T., NOWOTNY M.K., SHEPPARD L.R., *J. Phys. Chem. C*, 111 (2007), 9769–9778.

[28] ZHANG Y., TANG T.-T., GIRIT C., HAO Z., MAR- TIN M.C., ZETTL A., CROMMIE M.F., RON SHEN Y., WANG F., *Nature*, 459 (2009), 820–823.

[29] VON OERTZEN G.U., GERSON A.R., *Int. J. Quant. Chem.*, 106(9) (2006), 2054–2064.

[30] KASOWSKI R.V., TAIT R.H., *Phys. Rev. B*, 20(12) (1979), 5168–5177.

[31] MOR G.K., VARGHESE O.K., PAULOSE M., GRIMES C.A., *Adv. Funct. Mater.*, (2005), 1291–1296.

[32] YU J., XIANG Q., ZHOU M., *Appl. Catal. B: Envir.*, 90(3-4) (2009), 595–602.

[33] LIN F., ZHOU G., LI Z., LI J., WU J., DUAN W., *Chem. Phys. Lett.*, 475(1-3) (2009), 82–85.

[34] WU X., JIANG Q.-Z., MA Z.-F., FU M., SHANGGUAN W.-F., *Solid State Commun.*, 136(9-10) (2005), 513–517.

[35] MACAK J.M., TSUCHIYA H., GHICOV A., YASUDA K., HAHN R., BAUER S., SCHMUKI P., *Curr. Opinion in Solid State and Mater. Sci.*, 11(1-2) (2007), 3–18.

[36] TSAI CH.-CH., NIAN J.-N., TENG H., *App. Surf. Sci.*, 253(4) (2006), 1898–1902.

[37] ZLAMAL M., MACAK J.M., SCHMUKI P., KRYSA J., *Electrochem. Commun.*, 9(12) (2007), 2822–2826.

[38] LAI Y., ZHUANG H., SUN L., CHEN Z., LIN CH., *Elec- trochim. Acta*, 54(26) (2009), 6536–6542.

[39] YANG Y., WANG X., LI L., *Mat. Sci. Eng.: B*, 149(1) (2008), 58–62.

[40] CHEN X., SCHRIVER M., SUEN T., MAO S.S., *Thin Solid Films*, 515(24) (2007), 8511–8514.

[41] BANDURA A.V. EVARESTOV R.A., *Surf. Sci.*, 603(18) (2009), L117–L120.

[42] LIU Z., ZHANG Q., QIN L.-C., *Solid State Commun.*, 141(3) (2007), 168–171.

[43] DU G.H., CHEN Q., CHE R.C., YUAN Z.Y., PENG L.M., *App. Phys. Lett.*, 79(22) (2001), 3702–3704.

[44] WANG Y.Q., HU G.Q., DUAN X.F., SUN H.L., XUE Q.K., *Chem. Phys. Lett.*, 365(5-6) (2002), 427–431.

Received 05.11.2010
Accepted 16.12.2011