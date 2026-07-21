# Influence of Trimethylamine $N$-Oxide (TMAO) on the Three-dimensional Distribution and Alignment of Solvent Molecules in Aqueous Solution

Hideo Doi, $^{1,2}$ Yudai Watanabe, $^{1,2}$ and Misako Aida$^{*1,2}$

$^{1}$Center for Quantum Life Sciences (QuLiS), Hiroshima University,
1-3-1 Kagamiyama, Higashi-Hiroshima, Hiroshima 739-8526
$^{2}$Department of Chemistry, Graduate School of Science, Hiroshima University,
1-3-1 Kagamiyama, Higashi-Hiroshima, Hiroshima 739-8526

(E-mail: maida@hiroshima-u.ac.jp)

By means of Monte Carlo simulations together with an ab initio molecular orbital method, we present the influence of trimethylamine $N$-oxide (TMAO), which is a highly polarized spherical-polyhedron, on the distribution and the alignment of surrounding water molecules. The specific alignment of the average dipole moments of solvent water around TMAO is observed in the MC simulation. The number of water molecules in the first hydration shell from MC simulation was in good agreement with the experimental value. A cluster model of TMAO with 12 water molecules was presented as a representative hydration structure of TMAO.

Trimethylamine $N$-oxide (TMAO, Figure 1a) is one of the well-known osmolytes that play an important role in maintaining osmotic equilibria in living cells.$^{1}$ TMAO also plays a prominent in stabilizing protein structure.$^{2}$ Although many experimental and theoretical investigations have been carried out using different techniques to understand the characteristics of TMAO, the molecular mechanism by which TMAO functions is not completely known yet. Hydration structure around TMAO, especially around the methyl groups, has been a point of interest and also of controversy.$^{3-10}$

In this letter, by means of Monte Carlo (MC) simulations together with ab initio molecular orbital (MO) method, we shed light on the influence of TMAO on the distribution of the surrounding water and reveal a specific alignment of average dipole moments of solvent water around TMAO. This is the first report concerning the influence of TMAO on the alignment of solvent water molecules.

The geometry of TMAO was optimized in the gas phase using the ab initio MO method. The MP2/6-31G* level of theory was used for the geometry optimization using the Gaussian09 program package.$^{11}$ By means of the normal mode analysis, we confirmed that it is the local minimum structure. TMAO has $C_{3v}$ symmetry (Figure 1a). For geometrical parameters, see Table S1 in the Supporting Information.$^{12}$ The barrier height of one methyl group rotation is $+5.2\ \text{kcal}\ \text{mol}^{-1}$, indicating that the methyl groups of TMAO are not free to rotate.

With the global minimum geometry, the atomic charges of TMAO using natural population analysis (NPA)$^{13}$ were calculated: they are listed in Figure 1b. We adapted NPA, since it is generally accepted that NPA gives reasonable values for atomic charges.$^{14}$ The top-, side-, and bottom-views of the electrostatic potential map of TMAO are shown in Figure 1c. Based on the isoelectronic density surface, we can estimate the effective size of TMAO, which may correspond to the van der Waals volume. Assuming TMAO to be a sphere, the effective radius of TMAO was roughly estimated to be $\approx 3\ \text{\AA}$ with the nitrogen atom as the center. This is a highly polarized spherical polyhedron. It is divided into two parts: one is the partially negative region (oxide region), and the other is the partially positive region (methyl region). The dipole moment of TMAO was calculated to be $4.67\ \text{D}$. This is large, indicating the ability of TMAO to influence the distribution of the surrounding solvent molecules. Note that TMAO is a highly polarized molecule with $C_{3v}$ symmetry.

For MC simulation, the NPA charges (Figure 1b) were used as the molecular mechanics (MM) parameters of TMAO. The Lennard-Jones parameters determined by Freindorf and Gao$^{15}$ were applied to the atoms of TMAO. The TIP3P water potential function$^{16}$ was employed for solvent molecules to compare the hydration pattern of TMAO with that of adamantane,$^{17}$ for which we had used TIP3P.

Our own MC program was used to create the configurations of water molecules so as to form the NVT ensemble (at constant number $N$, volume $V$, and temperature $T$) using the canonical MC method based on the Metropolis-Hastings algorithm.$^{18}$ 500 water molecules were distributed around TMAO in a solvation sphere with a radius of $15.3\ \text{\AA}$. The density of TMAO with 500 water molecules in this sphere is $1\ \text{g}\ \text{cm}^{-3}$. The temperature was set at $300\ \text{K}$. The nitrogen atom of TMAO is set at the origin of the system, with the oxide bond along the direction of the $z$-axis. The N–C bond of one of the three methyl groups of TMAO is set on the $xz$ plane, which is one of three $\sigma_{v}$ planes.

![](./images/813157137009082369_1.jpg)

<table>
  <tr>
    <th>atom</th>
    <th>charge</th>
  </tr>
  <tr>
    <td>O</td>
    <td>-0.755</td>
  </tr>
  <tr>
    <td>N</td>
    <td>0.035</td>
  </tr>
  <tr>
    <td>C</td>
    <td>-0.469</td>
  </tr>
  <tr>
    <td>H<sub>eq</sub></td>
    <td>0.248</td>
  </tr>
  <tr>
    <td>H<sub>ax</sub></td>
    <td>0.213</td>
  </tr>
</table>

Figure 1. (a) Global minimum structure ($C_{3v}$ symmetry) of TMAO. Some notations are described. (b) NPA charges of TMAO atoms. (c) Side-, top-, and bottom-views of electrostatic potential map on the isoelectronic density ($0.005\ e/a_{0}^{3}$) surface of TMAO. MP2/6-31G* is used as the theoretical level.

The MC simulation was carried out using the following procedure. First, $10^8$ MC steps simulation was done for the equilibrium. Afterward $2 \times 10^{10}$ MC steps simulations were performed and used for the analysis.

The number densities of O and H atoms of solvent water were calculated in the same way as in the previous work¹⁷ (see Method S1).¹² The average dipole moment of solvent water at the position $(x, y, z)$ was calculated, as follows:
$$
\vec{M}(x, y, z)=\frac{\sum \vec{\mu}(x, \delta x, y, \delta y, z, \delta z)}{|\vec{\mu}|\left\langle N_{\mathrm{O}}(x, \delta x, y, \delta y, z, \delta z)\right\rangle} \tag{1}
$$

$$
M(x, y, z)=|\vec{M}(x, y, z)| \tag{2}
$$

Here, $\vec{\mu}$ denotes the dipole moment of a water molecule, the O atom of which resides in $x \approx x+\delta x$, $y \approx y+\delta y$, and $z \approx z+\delta z$. The length of the dipole moment is denoted by $|\vec{\mu}|$. In this study, we use the TIP3P potential function for water, so that the length of the dipole moment of each water molecule is fixed (2.35 D). $M(x, y, z)$ is the length of the average dipole moment of the solvent at $(x, y, z)$. The dipole moment was sampled every time when all water molecules had moved. The direction of the average dipole moment is defined as
$$
D(x, y, z)=\cos (\theta(x, y, z))=\frac{-\vec{P}(x, y, x) \cdot \vec{M}(x, y, z)}{|-\vec{P}(x, y, z)||\vec{M}(x, y, z)|} \tag{3}
$$

Here, $\vec{P}(x, y, z)$ denotes the position vector at the position $(x, y, z)$. The angle between the inverse position vector and the average dipole moment vector at the position $(x, y, z)$ is denoted as $\theta(x, y, z)$. When the average dipole moment at a position $(x, y, z)$ points to the origin (N atom of TMAO), the angle $\theta$ is $0^\circ$ and $D$ is +1. See Figure 2g for the definition.

The radial distributions of the number densities are shown in Figure S1.¹² Two-dimensional distributions of water molecules on specified planes around TMAO are calculated, and some of them are shown in Figure 2, since TMAO has a $C_3$ axis. Spherical or orientational averagings, which are often done in molecular simulations, led to the loss of intrinsically important local structural information¹⁹ of TMAO.

The number density of water O atoms around TMAO is plotted on the $\sigma_{\mathrm{v}}$ plane (xz plane at $y=0$) in Figure 2a, and also on the $xy$ plane at $z=0$ in Figure 2d. The first hydration shell (yellow-red portion) is clearly recognized. The second hydration shell outside the oxide region is clearly recognized around $z \approx 5 \mathring{\mathrm{A}}$. The second hydration shell (slightly red portion) outside the methyl region is recognized less clearly around the radius of ca. $7.5 \mathring{\mathrm{A}}$.

The distribution of the $M$ value, which is the length of the average dipole moment, is plotted in Figures 2b and 2e. An $M$ value close to 1 means that water molecules in a position tend to align in a similar direction. It is noticeable that $M$ values are large in the first hydration shell, especially in the oxide region.

The distribution of the $D$ value, which is the direction of the average dipole moment of solvent water molecules, is plotted in Figures 2c and 2f. It is noteworthy that the $D$ values are negative (blue-colored) in the methyl region, indicating that the average dipole moment is directed toward the outside of TMAO not only in the first hydration shell but also up to the range around the radius of ca. $7.5 \mathring{\mathrm{A}}$. In the oxide region, the $D$ values are positive, indicating that the average dipole moment is directed toward TMAO.

The first hydration shell of TMAO is fairly distinctive. The area where the number density of water in the first hydration shell is large, the average dipole moment is large. In the area where the first hydration shell is clearly formed, the average dipole moment of the second hydration region is rather large, indicating that the outer water molecules tend to align in such an area.

![](./images/813157137009082369_2.jpg)

Figure 2. Two-dimensional number density (atoms$\mathring{\mathrm{A}}^{-3}$) of water O atoms plotted on (a) the $\sigma_{\mathrm{v}}$ plane (xz plane at $y=0$), and (d) the $xy$ plane at $z=0$. Two-dimensional distribution of $M$ value on (b) the $\sigma_{\mathrm{v}}$ plane, and (e) the $xy$ plane at $z=0$. Two-dimensional distribution of $D$ value on (c) the $\sigma_{\mathrm{v}}$ plane, and (f) the $xy$ plane at $z=0$. (g) Schematic description of the definition of the direction of average dipole moment at a point $(x, y, z)$.

In the top- and bottom-regions along the $C_3$ axis of TMAO, water molecules tend to align even in an area rather far away, as seen in Figure 2c. In the bottom region, the O atom of water is directed toward TMAO; in the top region, one of the H atoms of water is directed toward TMAO. The hydrogen-bonding network of water molecules is preserved in those regions, while the direction of the network formation is restricted. Previously, it was demonstrated that TMAO does not disrupt the hydrogen bonding of water.¹⁹ We show here clearly the anisotropy in the effect of TMAO on the surrounding water.

As seen in Figure 2f, $D$ values outside the first hydration shell around the methyl region are more or less 0, indicating that the water molecules are not aligned. The region between neighboring methyl groups has the alignment of the second solvation shell.

In the case of adamantane, which is regarded as a hydrophobic molecule, water molecules in the first solvent shell are

![](./images/813157137009082369_3.jpg)

Figure 3. Three-dimensional side-, top-, and bottom-views of the distribution of O (red) and H (white) number densities of solvent water molecules around TMAO. Threshold to plot is 0.09 atoms $\text{\AA}^{-3}$ for oxygen, and 0.12 atoms $\text{\AA}^{-3}$ for hydrogen.

oriented in such a way that the direction of the average dipole moment of water is tangential to the skeleton surface, and the hydrogen-bonding network is formed among the water mole- cules in the first shell as well as between the first shell and the outer shell. $^{17,20}$ The hydration structure of the methyl region of TMAO is different from that of adamantane.

The first hydration shell around TMAO is highlighted in Figure 3. We plot a red point where the O number density is higher than 0.09 atoms $\text{\AA}^{-3}$, and a white point where the H number density is higher than 0.12 atoms $\text{\AA}^{-3}$. Note that the O number density, $n_{\mathrm{O}}(x, y, z)$, of bulk water $(1\ \mathrm{g\ cm}^{-3})$ is uniform and 0.033 atoms $\text{\AA}^{-3}$. As seen in Figure 3, TMAO has a highly populated hydration region of almost $C_{3}$ symmetry. The hydration region is spread not only around the oxide region but also in the three gorges between the methyl groups.

In the oxide region, one of the H atoms of each water molecule is pointed to the O atom of TMAO. The number of the directly hydrogen-bonded water molecules in the oxide region was calculated to be 3.7 from the MC simulation. In the methyl region, solvent water molecules are populated in the three gorges between the methyl groups. It is noteworthy that the O atoms, not the H atoms, of water molecules are pointed toward TMAO in this region. This is consistent with the $D$ value distribution (Figures 2c and 2f). The number of populated water molecules in the methyl region was calculated to be 9.6 from the MC simulation. In total, 13.3 water molecules reside in a sphere with a radius of approximately $6\ \text{\AA}$ (Figure S1). As indicated above, the effective radius of TMAO is $\approx 3\ \text{\AA}$. That is, there are 13.3 water molecules surrounding TMAO, with a thickness of $\approx 3\ \text{\AA}$ for the first geometric hydration shell. This is in fairly good agreement with the experimentally observed view: using the extended frequency range depolarized light scattering (EDLS) technique, it was demonstrated that the number of retarded water molecules around TMAO was 12-14 in the first geometric hydration shell with a thickness of $\approx 3.1\ \text{\AA}.^{7}$

Taking account of the water distribution (Figure 3) from MC simulation, we constructed several kinds of TMAO-water cluster models. One of those TMAO hydration structures, the cluster of TMAO with 12 water molecules in $C_{3}$ symmetry, is shown in Figure 4. The MP2/aug-cc-pVDZ level of theory was used for the geometry optimization.

The cluster model of TMAO with 12 water molecules (Figure 4) represents well the characteristics of the water distribution around TMAO (Figure 3). One of the H atoms of the water molecules in the oxide region points to the O atom of TMAO. Three arrays, each of which is composed of three water molecules, are set in three gorges between the neighboring methyl groups. The interaction energy (with BSSE corrected)

![](./images/813157137009082369_4.jpg)

Figure 4. A cluster model ($C_{3}$ symmetry) of hydration structure of TMAO with 12 water molecules, optimized with MP2/aug-cc-pVDZ.

between TMAO and the cluster of 12 water molecules was calculated to be $-64.38\ \text{kcal}\ \text{mol}^{-1}$, which is fairly large, considering that the interaction energy between 2 water molecules is around $-4\ \text{kcal}\ \text{mol}^{-1}$ (Table S2). $^{12}$

In the current work, we performed MC simulations with an all-MM model. The calculated distribution of water O molecules around TMAO is consistent with the spatial density function of water around TMAO from X-ray and neutron scattering studies $^{21}$ although the experimentally derived distribution did not show the H distribution of water molecules. Ab initio MO calculations of TMAO with 12 water molecules show characteristics for the water distribution around TMAO similar to that in aqueous solution from MC simulations with MM. Thus, we consider that the current MM calculation is good enough to represent the qualitative character of the hydration structure of TMAO.

TMAO has a great influence on the distribution and the alignment of water. Not only the oxide region, but also the gorge region between the methyl groups is strongly hydrated. The methyl groups in TMAO are not "hydrophobic."

### References and Notes
1 B. A. Seibel, P. J. Walsh, *J. Exp. Biol.* **2002**, *205*, 297.
2 P. H. Yancey, M. E. Clark, S. C. Hand, R. D. Bowlus, G. N. Somero, *Science* **1982**, *217*, 1214.
3 Y. L. A. Rezus, H. J. Bakker, *Phys. Rev. Lett.* **2007**, *99*, 148301.
4 A. Panuszko, P. Brużdziak, J. Zielkiewicz, D. Wyrzykowski, J. Stangret, *J. Phys. Chem. B* **2009**, *113*, 14797.
5 K. L. Munroe, D. H. Magers, N. I. Hammer, *J. Phys. Chem. B* **2011**, *115*, 7699.
6 J. Hunger, K.-J. Tielrooij, R. Buchner, M. Bonn, H. J. Bakker, *J. Phys. Chem. B* **2012**, *116*, 4783.
7 L. Comez, L. Lupi, A. Morresi, M. Paolantoni, P. Sassi, D. Fioretto, *J. Phys. Chem. Lett.* **2013**, *4*, 1188.
8 K. A. Sharp, B. Madan, E. Manas, J. M. Vanderkooi, *J. Chem. Phys.* **2001**, *114*, 1791.
9 A. Fornili, M. Civera, M. Sironi, S. L. Fornili, *Phys. Chem. Chem. Phys.* **2003**, *5*, 4905.
10 D. Laage, G. Stirnemann, J. T. Hynes, *J. Phys. Chem. B* **2009**, *113*, 2428.
11 M. J. Frisch, et al., *Gaussian 09 (Revision C.01)*, Gaussian, Inc., Wallingford CT, **2009**.
12 Supporting Information is available electronically on the CSJ-Journal Web site, http://www.csj.jp/journals/chem-lett/index.html.
13 A. E. Reed, R. B. Weinstock, F. Weinhold, *J. Chem. Phys.* **1985**, *83*, 735.
14 L. F. Pacios, P. C. Gómez, *THEOCHEM* **2001**, *544*, 237.
15 M. Freindorf, J. Gao, *J. Comput. Chem.* **1996**, *17*, 386.
16 W. L. Jorgensen, J. Chandrasekhar, J. D. Madura, R. W. Impey, M. L. Klein, *J. Chem. Phys.* **1983**, *79*, 926.
17 H. Doi, M. Aida, *Chem. Lett.* **2013**, *42*, 292.
18 N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, E. Teller, *J. Chem. Phys.* **1953**, *21*, 1087.
19 Q. Zou, B. J. Bennion, V. Daggett, K. P. Murphy, *J. Am. Chem. Soc.* **2002**, *124*, 1192.
20 M. Ohisa, M. Aida, *Chem. Phys. Lett.* **2011**, *511*, 62.
21 F. Meersman, D. Bowron, A. K. Soper, M. H. J. Koch, *Phys. Chem. Chem. Phys.* **2011**, *13*, 13765.