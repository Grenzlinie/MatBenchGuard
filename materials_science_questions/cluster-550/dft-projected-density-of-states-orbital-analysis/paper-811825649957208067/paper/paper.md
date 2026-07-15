First-principles study of the electronic and optical properties of $CuXS_2$ (X = Al, Ga, In) and $AgGaS_2$ ternary compounds

This article has been downloaded from IOPscience. Please scroll down to see the full text article.

2009 J. Phys.: Condens. Matter 21 485502

(http://iopscience.iop.org/0953-8984/21/48/485502)

View the table of contents for this issue, or go to the journal homepage for more

Download details:
IP Address: 138.73.1.36
The article was downloaded on 30/04/2013 at 23:36

Please note that terms and conditions apply.

# First-principles study of the electronic and optical properties of $\boldsymbol{CuXS_2}$ ($\boldsymbol{X = Al, Ga, In}$) and $\boldsymbol{AgGaS_2}$ ternary compounds

M G Brik

Institute of Physics, University of Tartu, Riia 142, Tartu 51014, Estonia

E-mail: brik@fi.tartu.ee

Received 7 July 2009, in final form 9 September 2009
Published 6 November 2009
Online at stacks.iop.org/JPhysCM/21/485502

## Abstract
First-principles calculations (using the CASTEP code, as implemented in the Materials Studio package) of electronic and optical properties of several representative ternary semiconductors ($CuXS_2$, $X = Al, Ga, In$, and $AgGaS_2$) were performed. After geometry optimization of the crystal structures, the band structures and partial and total densities of states were calculated and analyzed for all compounds considered. A scissor operator value of about 1.5 eV was introduced systematically to overcome the intrinsic drawback of the calculation technique—underestimation of the calculated band gaps. From the dielectric functions calculated with this correction, Sellmeyer’s approximations for the dependence of the refractive index on the wavelength were obtained for all crystals studied. The values of the refractive indices calculated are in reasonable agreement with the experimental data.

(Some figures in this article are in colour only in the electronic version)

## 1. Introduction
The ternary semiconductors with the general formula $\mathrm{A^I B^{III} C_2^{VI}}$ are widely studied due to their applications in non-linear optics, solar cells, optoelectronic devices etc [1–5]. Detailed experimental information on their optical properties can already be found in the literature. For example, the polarized absorption spectra of $AgGaSe_2$, $AgGaS_2$, $CuGaS_2$, $CuInS_2$ were reported in [6]; the energy band structure of $CuGaS_2$ and that of $CuInS_2$ were studied in [7]; tunable mid-infrared down-conversion in $AgGaS_2$ was achieved in [8]; $CuInS_2$ thin films were investigated in [9]; exciton spectra and the energy band structure of $CuGaSe_2$ crystals can be found in [10]; synthesis of $CuAlS_2$ nanorods was reported in [11]. Several research groups have also reported the results of first-principles calculations for some members of the $\mathrm{A^I B^{III} C^{VI}}$ family; in particular, the $CuAlS_2$ band structure was calculated in [12] using the potential-variation mixed-basis approach; the $CuGaS_2$ and $AgGaS_2$ band structures were calculated in [13] using the WIEN2K code. The same WIEN2K code was used in [14] to calculate the electronic properties of $CuAlX_2$ ($X = S, Se, Te$). Analysis of substitutional Mn ions in several $\mathrm{A^I B^{III} C^{VI}}$ compounds was published in [15].

Despite considerable efforts in both experimental and theoretical studies, it should be pointed out that the previously reported results for the energy gaps and optical characteristics for these crystals are somewhat different (the comparison between the previous and present calculations will be given below). Besides, the previously reported first-principles calculations [13, 14] were performed in the local density approximation (LDA), whereas the generalized gradient approximation (GGA) goes beyond the LDA and is better for predicting the lattice constants and chemical bond lengths [16, 17] and phase transitions [18]. That is why in the present work the GGA approximation is employed to calculate the band structure, total and partial density of states (DOS) and optical properties for four representative ternary semiconductors: $CuXS_2$ ($X = Al, Ga, In$) and $AgGaS_2$. The Materials Studio 4.0 package with its CASTEP module [18] has been used in all calculations.

The paper is organized as follows. In section 2 the crystal structure of the crystals considered will be described briefly, then the computational details will be outlined and the calculated results will be presented and compared with available experimental data and results from other calculations. The paper will be concluded with a short summary.

<table>
<caption>Table 1. Crystal lattice constants $a$, $c$ and the unit cell volume $V$ for $\text{CuXS}_2$ ($\text{X} = \text{Al}, \text{Ga}, \text{In}$) and $\text{AgGaS}_2$ crystals.</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">$\text{CuAlS}_2$</th>
<th colspan="3">$\text{CuGaS}_2$</th>
<th colspan="2">$\text{CuInS}_2$</th>
<th colspan="2">$\text{AgGaS}_2$</th>
</tr>
<tr>
<th>Exp.$^\text{a}$</th>
<th>Calc.$^\text{b}$</th>
<th>Exp.$^\text{a}$</th>
<th>Calc.$^\text{b}$</th>
<th>Calc.$^\text{c}$</th>
<th>Exp.$^\text{a}$</th>
<th>Calc.$^\text{b}$</th>
<th>Exp.$^\text{a}$</th>
<th>Calc.$^\text{b}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a$ (Å)</td>
<td>5.3336</td>
<td>5.2816</td>
<td>5.351</td>
<td>5.356</td>
<td>5.263</td>
<td>5.523</td>
<td>5.5775</td>
<td>5.754</td>
<td>5.7219</td>
</tr>
<tr>
<td>$c$ (Å)</td>
<td>10.4440</td>
<td>10.4429</td>
<td>10.480</td>
<td>10.629</td>
<td>10.379</td>
<td>11.12</td>
<td>11.2379</td>
<td>10.295</td>
<td>10.6275</td>
</tr>
<tr>
<td>$V$ (Å$^3$)</td>
<td>297.103</td>
<td>291.308</td>
<td>300.076</td>
<td>304.911</td>
<td>287.490</td>
<td>339.199</td>
<td>349.594</td>
<td>340.852</td>
<td>347.946</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="10">
$^\text{a}$ Reference [20]. $^\text{b}$ This work. $^\text{c}$ Reference [13].
</td>
</tr>
</tfoot>
</table>

![](./images/811825649957208067_1.jpg)

Figure 1. One unit cell of $\text{CuAlS}_2$. The Cu ions are shown by white spheres, the Al ions by gray spheres, and the S ions by black spheres.

## 2. Crystal structure

The crystals considered in the present study crystallize in the chalcopyrite structure, space group $I\bar{4}2d$, with four formula units in a unit cell. Each atom in this structure is fourfold coordinated, like in the zinc-blende or diamond crystal structures (figure 1; only the $\text{CuAlS}_2$ structure is shown and described, since other hosts are isostructural). Each sulfur ion is coordinated with two aluminum and two copper ions; each copper ion and each aluminum ion are coordinated with four sulfur ions. The crystal lattice parameters for the compounds studied (both experimental and calculated) are shown in table 1.

As seen from table 1, the lattice constants increase with increasing atomic number of the trivalent metal ion $\text{Al} \rightarrow \text{Ga} \rightarrow \text{In}$ for the $\text{CuXS}_2$ series. The $c$ constant is almost two times greater than the $a$ constant for all compounds.

The experimental crystal structural data were used as an initial input for optimizing the crystal structure and calculations of the optical properties, as described below.

## 3. Computational details

All calculations presented were performed in the density functional theory framework. The CASTEP module [18] of the Materials Studio 4.0 was employed in the calculations. The total plane-wave pseudopotential method forms the basis of the CASTEP calculations. The exchange–correlation effects were treated within the generalized gradient approximation (GGA) with the Perdew–Burke–Ernzerhof functional [19]. The Monkhorst–Pack scheme $k$-point grid sampling was set at $5 \times 5 \times 2$ for the Brillouin zone. The plane-wave basis set energy cutoff was set at 290 eV for $\text{CuAlS}_2$, 295 eV for $\text{CuGaS}_2$, 310 eV for $\text{CuInS}_2$ and 330 eV for $\text{AgGaS}_2$; ultrasoft pseudopotentials were used for all chemical elements. The convergence parameters were as follows: total energy tolerance $1 \times 10^{-5}$ eV/atom, maximum force tolerance $0.3$ eV nm$^{-1}$, and maximum stress component 0.05 GPa.

The optimized lattice constants are shown in table 1, in comparison with experimental findings and results from other calculations (using the LDA) for $\text{CuGaS}_2$ [13]. As seen from this table, agreement between the results of the present calculations and experimental data is very good. It can be also pointed out that for $\text{CuGaS}_2$ the GGA results are closer to the experimental ones than the LDA results.

After having optimized the crystal structures, the band structures, DOS and optical properties of all crystals considered were calculated.

## 4. Electronic and optical properties

### 4.1. $\text{CuAlS}_2$

All these materials are direct band gap semiconductors, as has been confirmed by the results of the calculations performed. The experimental band gaps for $\text{CuAlS}_2$ are about 3.49 eV [21] and 3.50 eV [22], and the calculated value was 1.94 eV. Such an underestimation of the calculated band gaps is an intrinsic feature of the *ab initio* method (the calculated result can be compared with the results from other band gap calculations for this compound: 2.05 eV [12], 2.44 eV [23], 2.7 eV [14], all of which are also underestimated) and is related to the DFT limitations, namely not taking into account the discontinuity in the exchange–correlation potential [24]. To overcome such a discrepancy, the so called scissor operator [25] is introduced, which effectively eliminates the difference between the theoretical and experimental gap values by means of a simple rigid shift of the unoccupied conduction band with respect to the valence band. In our case the value of the scissor operator was 1.55 eV. The calculated band structure of $\text{CuAlS}_2$ is shown in figure 2.

The composition and origin of the calculated bands can be understood by analyzing the partial DOS diagrams, shown in figure 3. The conduction band between about 3.5 and 10.5 eV

![](./images/811825649957208067_2.jpg)

Figure 2. Calculated band structure of CuAlS₂. The zero of energy is taken as the top of the valence band.

![](./images/811825649957208067_3.jpg)

Figure 3. DOS of CuAlS₂. From top to bottom: sulfur; aluminum; copper; total DOS.

![](./images/811825649957208067_4.jpg)

Figure 4. Dielectric function $\varepsilon$ for CuAlS₂.

is formed by Cu 4s, 4p states and Al 3s, 3p states, all of which are hybridized. The upper valence band is split into two sub-bands. The highest of them is between $-2$ and 0 eV, and the lowest between about $-3$ and $-7$ eV. These bands are formed by the S, Al, and Cu states; all of them are strongly overlapping. The Cu 3d DOS clearly show two peaks, which correspond to the splitting of the 3d orbitals in the tetrahedral crystal field into the e (lower) and t₂ (higher) states (in the Td group irreducible representation notation).

One of the main optical characteristics of a solid is its dielectric function $\varepsilon(\omega)$, which has a complex character: $\varepsilon(\omega) = \varepsilon_1 + \mathrm{i}\varepsilon_2$. The imaginary part $\varepsilon_2$ of the dielectric function is calculated in CASTEP numerically by evaluating the matrix elements connecting the occupied and unoccupied electronic states. The real part $\varepsilon_1$ of $\varepsilon(\omega)$ is calculated then using the Kramers-Kronig transform.

The calculated dielectric function of CuAlS₂ is shown in figure 4. In this and all cases below the instrumental smearing of 0.25 eV was used to model the broadening effects. The imaginary part can be related to the absorption spectrum (which, in this case, will be due to the electronic transitions from the valence band to the conduction band). The real part of $\varepsilon(\omega)$ in the limit of zero energy (or infinite wavelength) is equal to the square of the refractive index $n$. Then from figure 4 it is possible to estimate the value of $n$ to be 2.26, which is close to the experimental value 2.4 and the calculated value 2.6 reported in [26]. Additional useful information, which can be extracted from the calculated dielectric function, is the dependence of the refractive index on the wavelength $\lambda$. The Sellmeyer equation

![](./images/811825649957208067_5.jpg)

Figure 5. Calculated values of $n$ (symbols) and the Sellmeyer approximation (solid line) for CuAlS₂.

with the infrared correction in the following form [27]:

$$
n = A + \frac{B}{1 - \left(\frac{C}{\lambda}\right)^2} - D\lambda^2 \tag{1}
$$

was used to fit the calculated value of $n$ (figure 5). The values of the parameters of this fit are: $A = 1.479\,25 \pm 0.020\,61$; $B = 0.771\,43 \pm 0.018\,98$; $C = 202.836\,14 \pm 1.100\,14$ nm; and $D = (-4.0606 \pm 2.0382) \times 10^{-10}$ nm$^{-2}$.

### 4.2. $CuGaS_2$

The experimental value of the band gap for CuGaS₂ is 2.43 eV [1], whereas the present calculations gave the value as about 0.9 eV. This value is in good agreement with other calculated results for this host: 0.903 eV [13] and 0.92 eV [28].

Again, to avoid underestimation of the calculated band gap, a 1.5 eV scissor operator was applied. Figure 6 shows the calculated band structure of CuGaS₂.

The valence band consists of three sub-bands in this case, as is clearly revealed in the total DOS diagram. The highest of these is between $-2.5$ and 0 eV, the middle one between about $-3.5$ and $-6$ eV, and the lowest one between $-7.5$ and $-6$ eV. These bands are formed by the S s, p and Cu s, p, d (mainly) states, with a very small admixture of the Ga s, p states. The partial DOS for each of these elements (along with the total DOS) are given in figure 7.

The conduction band is formed mainly by a superposition of the Cu and Ga p and s states. The lower valence band at about $-15$ eV mainly consists of Ga 3d states. The S s and p states also contribute (although slightly) to the valence bands. It is interesting to note that the Ga 3d states are not split, like the Cu 3d states (which are located considerably higher in energy), into two sub-states due to the action of the surrounding crystal field. A similar result was also obtained in [13].

Figure 8 shows the real $\text{Re}(\varepsilon)$ and imaginary $\text{Im}(\varepsilon)$ parts of the dielectric function for CuGaS₂. Estimation of the refractive index $n$ from the low energy limit of $\text{Re}(\varepsilon)$ yields the value of $n$ as 2.46, which is close to the value of 2.3999 reported in [29]. Several peaks of the $\text{Im}(\varepsilon)$ function are due to the absorption transition between the valence and conduction bands.

Figure 9 shows the dependence of the calculated refractive index on the wavelength. Equation (1) was used for fitting the calculated data (the fit is shown by a solid line). The following fitting parameters were obtained: $A = 1.539\,56 \pm 0.049\,95$; $B = 0.8999 \pm 0.0448$; $C = 265.009\,37 \pm 3.086\,13$ nm; and $D = (-1.308 \pm 0.272) \times 10^{-8}$ nm$^{-2}$.

![](./images/811825649957208067_6.jpg)

Figure 6. Calculated band structure of CuGaS₂. The zero of energy is taken as the top of the valence band.

![](./images/811825649957208067_7.jpg)

Figure 7. DOS for CuGaS₂. From top to bottom: sulfur; gallium; copper; total DOS.

![](./images/811825649957208067_8.jpg)

Figure 8. Dielectric function $\varepsilon$ for CuGaS₂.

### 4.3. CuInS₂
The experimental value of the band gap for CuInS₂ is 1.55 eV [30]. The calculations performed gave practically a zero value of the band gap (which is consistent with the above-mentioned underestimation of the band gap), so again the scissor operator of 1.5 eV was applied. The calculated band structure is shown in figure 10. The partial DOS (figure 11) show that the conduction band mainly consists of Cu and In s and p states. The upper valence band consists of the S p states with Cu d states (the latter are split into two groups again—the e and t₂ states—because of the crystal field influence). Finally, the In d states give the main contribution to the deeply located band, at about $-15$ eV.

The calculated dielectric function for CuInS₂ is shown in figure 12. The estimation of the refractive index as a square root of $\mathrm{Re}(\varepsilon)$ at the zeroth energy gives the value of 2.57, which can be compared with the value of 2.755 reported for this material in [31]. The dependence of the refractive index on the wavelength, which is shown in figure 13, was fitted using the Sellmeyer law (equation (1)) with the following constants: $A=-0.391\pm0.393$; $B=2.861\pm0.383$; $C=228.877\pm10.994$ nm; and $D=(-2.867\pm0.375)\times10^{-8}$ nm⁻².

![](./images/811825649957208067_9.jpg)

Figure 9. Calculated values of $n$ (symbols) and the Sellmeyer approximation (solid line) for CuGaS₂.

### 4.4. AgGaS₂
The experimental data on the band gap for AgGaS₂ give the value of 2.51 eV for [21], whereas the calculated result was 1 eV. To overcome this usual underestimation, a 1.5 eV scissor operator was applied. The calculated band structure of AgGaS₂ is shown in figure 14.

The conduction band, as the DOS diagrams (figure 15) tell us, is made of the Ag and Ga s and p states, with a small admixture of the sulfur s and p states. In contrast to the case for the previous three crystals, the upper valence band is not split into sub-bands, but itself represents a wide band stretching from about $-7$ to about 0 eV. The main contribution to this band comes from the Ag 3d states, followed by the sulfur 3s and 3p states. Finally, the band at about $-15$ eV predominantly consists of the Ga 3d states with admixture of S 3s states.

The results of the optical properties calculations are shown in figures 15 and 16. The dielectric function (figure 15) allows us to estimate the value of the refractive index at infinite wavelength as about 2.3, comparable with the experimental value (2.44) of the refractive index at $1.24\ \mu$m [32].

The best fit to the Sellmeyer equation (figure 17) was obtained with the following values of the fitting parameters: $A=-1.26\pm0.51$; $B=3.49\pm0.51$; $C=132.62\pm8.03$ nm; and $D=(-6.49\pm0.10)\times10^{-9}$ nm⁻².

## 5. Conclusion
First-principles calculations of the band structure, density of states and optical properties of the CuXS₂ (X = Al, Ga, In) and AgGaS₂ ternary semiconductors have been performed using the CASTEP module of the Materials Studio package.

The band gaps calculated (either with the scissor operator, or without it) decrease in the CuXS₂ group (X = Al, Ga, In) with increasing 'X' element atomic number, whereas the value of the calculated refractive index $n$ increases in the same direction ($2.26\rightarrow2.46\rightarrow2.57$) in the $\mathrm{Al}\rightarrow\mathrm{Ga}\rightarrow\mathrm{In}$ series. The optimized lattice constants also increase in the same way. The general features of the band structure of these four crystals considered (represented generally as AᵢBᵢᵢᵢS₂) are as follows:

![](./images/811825649957208067_10.jpg)

Figure 10. Calculated band structure of CuInS₂. The zero of energy is taken as the top of the valence band.

![](./images/811825649957208067_11.jpg)

Figure 11. Total DOS for CuInS₂. From top to bottom: sulfur; indium; copper; total DOS.

![](./images/811825649957208067_12.jpg)

Figure 12. Dielectric function for CuInS₂.

the conduction band consists mainly of the A and B element s and p states, with a small admixture of the sulfur s and p states. The valence band mainly is composed of the A element d states (which are split into two subgroups, like the d orbitals in a tetrahedral crystal field) with a small contribution of the s and p states coming from other elements. Finally, the lowest calculated band (which for all compounds is at about $-15$ eV) is mainly due to the B element d states, which do not show any crystal field splitting.

Although a complete and precise description of band structure and optical properties implies taking the spin-orbit interaction into account, in the present calculations it was neglected. In making such an approximation, we follow [33], where the spin-orbit coupling was also omitted. Such a

![](./images/811825649957208067_13.jpg)

Figure 13. Calculated values of $n$ (symbols) and the Sellmeyer approximation (solid line) for CuInS₂.

![](./images/811825649957208067_14.jpg)

Figure 14. Calculated band structure for $AgGaS_2$. The zero of energy is taken as the top of the valence band.

![](./images/811825649957208067_15.jpg)

Figure 15. DOS for $AgGaS_2$. From top to bottom: S, Ga, Ag, total DOS.

![](./images/811825649957208067_16.jpg)

Figure 16. Dielectric function for $AgGaS_2$.

step can be justified by the fact that in sulfides—due to the high covalency and strong p–d hybridization—the spin–orbit interaction is reduced significantly [1].

The real and imaginary parts of the dielectric functions for all crystals considered were calculated and plotted against the energy. The imaginary parts of the calculated functions are related to the absorption spectra (band-to-band transitions) and show several peaks. The lowest peak (between the absorption edge and 4–5 eV) can be attributed to the transitions of the d electrons of Cu (or Ag) from the higher $t_2$ states to the conduction bands. The peaks at about 7 eV are due to the transitions of the Cu (or Ag) d electrons from the lower e states to the conduction bands. After making calculations of the dielectric function, the Sellmeyer equation with infrared correction was used to model the dependence of the refractive

![](./images/811825649957208067_17.jpg)

Figure 17. Calculated values of $n$ (symbols) and the Sellmeyer approximation (solid line) for $AgGaS_2$.

index on the wavelength; the parameters of the Sellmeyer fit were obtained for each compound considered. The main calculated results (optimized crystal lattice constants, band gaps with the corresponding scissor operators, values of the refractive index in the limit of infinite wavelength) are in good agreement with available experimental data.

Acknowledgments

Professor Ü Lille (Tallinn University of Technology) is thanked for allowing us to use the computational facilities and Materials Studio package. Financial support from Estonian Science Foundation (grants No. 7456, JD69, 6999 and 6660) is acknowledged.

References

[1] Shay J L and Wernick J H 1975 *Ternary Chalcopyrite Semiconductors: Growth, Electronic Properties, and Applications* (Oxford: Pergamon)

[2] Birkmire R W and Eser E 1997 *Annu. Rev. Mater. Sci.* **27** 625

[3] Wagner S, Shay J L, Migliorato P and Kasper H M 1974 *Appl. Phys. Lett.* **25** 234

[4] Deb S K and Zunger A (ed) 1987 *Ternary and Multinary Compounds* (Pittsburgh, PA: Materials Research Society)

[5] Klenk R, Klaer J, Scheer R, Lux-Steiner M Ch, Luck I, Meyer N and Rühle U 2005 *Thin Solid Films* **480/481** 509

[6] Choi I-H, Han S-D, Eom S-H, Lee W-H and Lee H C 1996 *J. Korean Phys. Soc.* **29** 377

[7] Levcenko S, Syrbu N N, Tezlevan V E, Arushanov E, Doka-Yamingo S, Schedel-Niedrig Th and Lux-Steiner M Ch 2007 *J. Phys.: Condens. Matter* **19** 456222

[8] Okorogu A O, Mirov S B, Lee W, Crouthamel D I, Jenkins N, Dergachev A Y, Vodopyanov K L and Badikov V V 1998 *Opt. Commun.* **155** 307

[9] González-Hernández J, Gorley P M, Horley P P, Vartsabyuk O M and Vorobiev Yu V 2002 *Thin Solid Films* **403/404** 471

[10] Syrbu N N, Bogdanash M, Tezlevan V E and Stamov I G 1997 *J. Phys.: Condens. Matter* **9** 1217–23

[11] Harichandran G and Lalla N P 2008 *Mater. Lett.* **62** 1267

[12] Jaffe J E and Zunger A 1983 *Phys. Rev. B* **28** 5822

[13] Laksari S, Chahed A, Abbouni N, Benhelal O and Abbar B 2006 *Comput. Mater. Sci.* **38** 223

[14] Reshak A H and Auluck S 2008 *Solid State Commun.* **145** 571

[15] Zhao Y-J and Zunger A 2004 *Phys. Rev. B* **69** 104422

[16] Perdew J P and Wang Y 1992 *Phys. Rev. B* **45** 13244

[17] Asahi R, Taga Y, Mannstadt W and Freeman A J 2000 *Phys. Rev. B* **61** 7459

[18] Segall M D, Lindan P J D, Probert M J, Pickard C J, Hasnip P J, Clark S J and Payne M C 2002 *J. Phys.: Condens. Matter* **14** 2717

[19] Perdew J P, Burke K and Ernzerhof M 1996 *Phys. Rev. Lett.* **77** 3865

[20] Brandt G, Rauber A and Schneider J 1973 *Solid State Commun.* **12** 481

[21] Shay J L, Tell B, Kasper H M and Schiavone L M 1972 *Phys. Rev. B* **5** 5003

[22] Yoodee K, Woolley J C and Sa-yakanit V 1984 *Phys. Rev. B* **30** 5904

[23] Yamasaki T, Suzuki N and Motizuki K 1987 *J. Phys. C: Solid State Phys.* **20** 395

[24] Perdew J P and Levy M 1983 *Phys. Rev. Lett.* **51** 1884

[25] Levine Z H and Allane D C 1991 *Phys. Rev. B* **43** 4187

[26] Chemla D S 1971 *Phys. Rev. Lett.* **26** 1441

[27] Pujol M C, Rico M, Zaldo C, Sole R, Nikolov V, Solans X, Aguilo M and Diaz F 1999 *Appl. Phys. B* **68** 187

[28] Rashkeev S N and Lambrecht W R L 2001 *Phys. Rev. B* **63** 165212

[29] Madelung O, Rössler U and Schulz M 2000 *Ternary Compounds, Organic Semiconductors* vol 41E (Berlin: Springer) pp 1–9

[30] Guillen C, Herrero J, Gutierrez M T and Briones F 2005 *Thin Solid Films* **480/481** 19

[31] Zribi M, Kanzari M and Rezig B 2006 *Mater. Lett.* **60** 98

[32] *Handbook of Optics* 1994 2nd edn, vol 2 (New York: McGraw-Hill)

[33] Alonso M I, Wakita K, Pascual J, Carriga M and Yamamoto N 2001 *Phys. Rev. B* **63** 075203