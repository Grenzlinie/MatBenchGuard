# First-principles study on structure and stability of YAP crystal

Qing-Gong Song $^{1,2,a}$, Liwei Liu$^{2,b}$, Yanbo Wang $^{2,c}$, Hui Zhao $^{2,d}$,
Huiyu Yan$^{1,e}$, and Yifei Chen$^{1,f}$

$^{1}$ College of Science, Civil Aviation University of China, Tianjin 300300, China
$^{2}$ College of Science, Hebei University of Technology, Tianjin 300130, China

$^{a}$qgsong@cauc.edu.cn, $^{b}$liuliwei_0086@163.com, $^{c}$wangyanbo1199@163.com,
$^{d}$zhzhao2008@126.com, $^{e}$hyyan@cauc.edu.cn, $^{f}$yifei_chen@163.com

**Keywords:** YAP, First-principles, Lattice parameter, Formation energy, Mulliken population

**Abstract:** The geometry optimization, formation energy, Mulliken populations, and density of states of YAP ($YAlO_3$) crystal are studied by using first-principles method based on density functional theory. The optimal lattice parameters of YAP crystal are in good accordance with experimental results reported. The calculated formation energy (-3.73eV) indicates the excellent structural stability of YAP crystal. The obtained Mulliken charge populations of O, Al and Y atoms and their deviations from the formal ones, as well as overlap populations show YAP crystal is a mixed bond material with stronger ionic and weaker covalent bonds, which is attributed to the hybridization of atomic orbitals. The comprehensive effect of various interactions in the system makes YAP crystal more stable.

## Introduction

Recently, much attention has been paid to yttrium-aluminum oxide, $YAlO_3$ (YAP) and related materials for their admirable comprehensive properties [1-10]. For instance, orthorhombic YAP crystals doped with rare-earth ions are potential candidates of better laser materials than $Y_3Al_5O_{12}$ (YAG) crystal and sparklers for radiation detection, as well as other applications [9-12]; cubic YAP crystals with perovskite structure are used for preparing transparent ceramics thin film with better transparency in a wide spectral range, high heat conductivity and hardness [1,13], also used as electrolyte for solid oxide fuel cells [2]. Many groups reported their research works and presented significant information about electronic structures [8,10,14], electrical conductivity [2,15], absorption spectra [3,16-18], color centers [5,16,17], energy transfer [18,19], luminescence [5,6,19-21], electron paramagnetic resonance [22], thermal diffusivity [7]. etc. However, to our best knowledge, the geometric structure and stability of YAP crystal, which are important factors for advanced technology applications, especially ceramic materials at the nano-scale [23], have not been reported in detail. Methodologically, first-principles calculation based on density functional theory (DFT) has been successfully used to investigate the structures and properties of many crystals [23-26]. Here, we present theoretical investigations about the structure and stability of orthorhombic YAP crystal by using first-principles method.

## Structural model and calculation scheme

**Structural model.** For pure orthorhombic YAP crystal, its structure ( lattice parameters: $a \neq b \neq c$, $\alpha = \beta = \gamma =90^\circ$; space group: Pnma) can be regarded as distorted perovskite structure. The conventional unit cell contains four formula units and can be constructed with tilted $AlO_6$ octahedra, in which each Al ion is located in the center of a regular octahedron, while Y ions insert the holes between these octahedra, as shown in Fig.1. The structural model used for calculation consists of 16 Y, 16 Al and 48 O atoms.

![](./images/813349728115752960_1.jpg)

Fig. 1. Structural model of YAP crystal

Calculation scheme and selected parameters. The first-principles calculations are carried out by using CASTEP code [26]. The calculation scheme includes: the generalized gradient approximation (GGA) with the Perdew-Wang exchange correlation potential; the ultrasoft pseudopotentials, in which the atomic orbital electrons O- $2s^22p^4$, Al- $3s^23p^1$, Y- $4d^15s^2$ are selected as valence electrons. The parameters selected for calculation are cutoff energy, 550.0 eV for all of atoms; Monkhorst-Pack k-point, $5\times3\times5$ for numerical integration of Brillouin zone sampling; and the convergence tolerance, energy- $2.8997\times10^{-5}$ eV/atom; force- $2.7684\times10^{-3}$ eV/Å; stress- 7.3323 $\times10^{-3}$ GPa; displacement- $4.6906\times10^{-4}$ Å; original lattice parameters, $a=5.33$ Å, $b=7.38$ Å, $c=5.18$ Å. Based on the above mentioned scheme and parameters, the calculations continue until convergent results are obtained.

Results and discussion

Lattice parameters and formation energy. Before property calculations, geometry optimization is necessary in order to check the usability of the selected scheme. Table 1 presents the optimized lattice parameters and total energies of orthorhombic YAP, $\text{Y}_2\text{O}_3$ and $a$-$\text{Al}_2\text{O}_3$ crystals, as well as the experimental results reported in the literatures [27-29]. It can be seen that the optimal results are in

<table>
<caption>Table1 Lattice parameters and total energies of YAP, $\text{Y}_2\text{O}_3$ and $a$-$\text{Al}_2\text{O}_3$ crystals</caption>
<thead>
<tr>
<th colspan="2">System</th>
<th colspan="3">$\text{YAlO}_3$</th>
<th>$\text{Y}_2\text{O}_3$</th>
<th colspan="2">$a$-$\text{Al}_2\text{O}_3$</th>
</tr>
</thead>
<tbody>
<tr>
<th rowspan="4">Parameters</th>
<th></th>
<th>$a$</th>
<th>$b$</th>
<th>$c$</th>
<th>$a=b=c$</th>
<th>$a=b$</th>
<th>$c$</th>
</tr>
<tr>
<th>Calculated [Å]</th>
<td>5.3584</td>
<td>7.4170</td>
<td>5.1975</td>
<td>11.4607</td>
<td>4.7837</td>
<td>13.0596</td>
</tr>
<tr>
<th>Experimental [Å]</th>
<td>5.330</td>
<td>7.375</td>
<td>5.180 [27]</td>
<td>10.604 [28]</td>
<td>4.759</td>
<td>12.986 [29]</td>
</tr>
<tr>
<th>Deviation [%]</th>
<td>0.53</td>
<td>0.57</td>
<td>0.34</td>
<td>8.08</td>
<td>0.52</td>
<td>0.57</td>
</tr>
<tr>
<th colspan="2">Total energy [eV]</th>
<td colspan="3">-5015.704</td>
<td>-6860.625</td>
<td colspan="2">-3163.33</td>
</tr>
</tbody>
</table>

good accordance with experimental ones. This means our calculation scheme and selected parameters are reasonable. All the property calculations are carried out on the basis of optimized parameters in stead of experimental data.

The formation energy of an ordered system is defined [30] as

$$\Delta E=E-x\ E_{\mathrm{Y}}-(1-x)E_{\mathrm{Al}},\tag{1}$$

where $E$, $E_{\mathrm{Y}}$ and $E_{\mathrm{Al}}$ are the total energies of YAP, $\mathrm{Y}_{2}\mathrm{O}_{3}$ and $a$-$\mathrm{Al}_{2}\mathrm{O}_{3}$ systems, respectively; $x$ represents the concentration of Y atom, $x = 1$ corresponds to $\mathrm{Y}_{2}\mathrm{O}_{3}$ system, while $x = 0$ corresponds to $\alpha$-$\mathrm{Al}_{2}\mathrm{O}_{3}$ system. According to Eq. (1), we can obtain the formation energy of YAP crystal, *i.e.* -3.73eV. The larger absolute value of formation energy indicates good stability of YAP crystal, especially at high temperature, which is of great importance for high technological applications.

Populations. Mulliken populations include the atomic population and overlap population. The former is accurate for qualitatively describing chemical property of an atom in spite of large deviation for quantitatively describing [31]; and the latter is a parameter that characterizes the strength of covalent bond, of which the positive sign represents covalent bonds and the negative one represents ionic bond [32].

The charge distribution in YAP crystal is shown in Table 2. It is a well-known fact that the formal charge numbers of O, Al and Y atoms in $\mathrm{YAlO}_{3}$ molecule are -2, + 3 and + 3, respectively; while the

<table>
<caption>Table 2 Charge distribution in YAP crystal</caption>
<thead>
<tr>
<th rowspan="2">Atom</th>
<th colspan="3">Orbital charge</th>
<th rowspan="2">Total charge</th>
<th rowspan="2">Mulliken charge</th>
</tr>
<tr>
<th>s</th>
<th>p</th>
<th>d</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\mathrm{O_{a}}$</td>
<td>1.84</td>
<td>5.09</td>
<td>-</td>
<td>6.93</td>
<td>-0.93</td>
</tr>
<tr>
<td>$\mathrm{O_{b}}$</td>
<td>1.84</td>
<td>5.10</td>
<td>-</td>
<td>6.93</td>
<td>-0.93</td>
</tr>
<tr>
<td>Al</td>
<td>0.55</td>
<td>1.04</td>
<td>-</td>
<td>1.59</td>
<td>1.41</td>
</tr>
<tr>
<td>Y</td>
<td>2.27</td>
<td>5.14</td>
<td>1.20</td>
<td>9.62</td>
<td>1.38</td>
</tr>
</tbody>
</table>

calculated results present Mulliken charge numbers of O, Al and Y atoms are - 0.93, + 1.41 and + 1.38, respectively. These populations exhibit that YAP crystal possesses the character of ionic crystals. However, the deviations of Mulliken charge numbers from the formal ones have shown that the chemical bonds between O and Al (or Y) atom are not perfect electrovalent, instead, partly electrovalent and partly covalent bonds. This fact originates from the hybridization of atomic orbitals in crystal, as can be confirmed by their partial density of states (Fig.2), in which s-orbitals and p-orbitals of the three elements are hybridized distinctly near Fermi surface. Thus, we can conclude that orthorhombic YAP crystal is a mixed bond material with stronger ionic and weaker covalent bonds. This chemical character confirms the stability of YAP crystal further.

The Mulliken overlap populations are list in Table 3. The results obviously show that the O-Al bonds and O-Y bonds possess some covalent character, and the O-O bonds possess some ionic character in YAP crystal. It can be seen that there are two kinds of O-Al bonds and several kinds of O-Y bonds. It is the structural distortion of YAP crystal that causes the breaking of crystal symmetry, resulting in various chemical bond lengths and charge numbers of atoms. The negative population of an O-O bond indicates repulsion between the two O atoms, and these O atoms are in a tendency of moving out of the octahedron. While the O-Al and O-Y bonds with positive overlap population give attractive interaction. All in all, the comprehensive effect of various interactions in the system makes YAP crystal more stable.

![](./images/813349728115752960_2.jpg)

Fig. 2. Density of states and partial density of states of YAP crystal

<table>
  <caption>Table 3 Mulliken overlap populations of chemical bonds in YAP crystal</caption>
  <thead>
    <tr>
      <th>Bond</th>
      <th>Population</th>
      <th>Length[$\mathring{\text{A}}$]</th>
      <th>Bond</th>
      <th>Population</th>
      <th>Length[$\mathring{\text{A}}$]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O-Al</td>
      <td>0.34</td>
      <td>1.91169</td>
      <td>O-Y</td>
      <td>0.12</td>
      <td>2.47577</td>
    </tr>
    <tr>
      <td>O-Al</td>
      <td>0.34</td>
      <td>1.93617</td>
      <td>O-O</td>
      <td>-0.06</td>
      <td>2.67861</td>
    </tr>
    <tr>
      <td>O-Y</td>
      <td>0.22</td>
      <td>2.25704</td>
      <td>O-O</td>
      <td>-0.11</td>
      <td>2.71973</td>
    </tr>
    <tr>
      <td>O-Y</td>
      <td>0.28</td>
      <td>2.28798</td>
      <td>O-O</td>
      <td>-0.12</td>
      <td>2.72667</td>
    </tr>
    <tr>
      <td>O-Y</td>
      <td>0.10</td>
      <td>2.31914</td>
      <td>O-O</td>
      <td>-0.06</td>
      <td>2.73282</td>
    </tr>
  </tbody>
</table>

## Conclusions
We obtained optimal lattice parameters of YAP crystal through first-principles calculation, and the results are in good accordance with experimental results reported confirming the validity of the calculation scheme. The derived formation energy indicates the excellent structural stability of YAP crystal. The obtained Mulliken charge populations of O, Al and Y atoms and their deviations from the formal ones, as well as Mulliken overlap populations show YAP crystal is a mixed bond material with stronger ionic and weaker covalent bonds, which can be attributed to the hybridization of atomic orbitals. The comprehensive effect of various interactions in the system makes YAP crystal more stable.

## Acknowledgment
The authors appreciate the financial support from the National Natural Science Foundation of China (Grant No. 60979008).

### References

[1] J.F. Carvalho, F.S. de Vicente and S. Pairis: J. Eur. Ceram. Soc. Vol. 29 (2009), p. 2511.

[2] R. Hariharan and P. Gopalan: J. Alloy Compd. Vol. 496 (2010), p. 528.

[3] Q. Dong, G.J. Zhao, D.H. Cao, J.Y. Chen and Y.C. Ding: J. Alloy Compd. Vol. 493 (2010), p. 661.

[4] Z.S. Liu, J.F. Ma, Y. Sun, Z.W. Song, J.R. Fang, Y. Liu, C. Gao and J.G. Zhao: Ceram. Int. Vol. 36 (2010), p. 2003.

[5] V. Babin, V. Gorbenko, A. Krasnikov, A. Makhov, M. Nikl, S. Zazubovich and Y. Zorenko: Radiation Mearurements. Vol. 45 (2010), p. 415.

[6] L. Grigorjeva, A. Krasnikov, V.V. Laguta, M. Nikl and S. Zazubovich: J. Appl. Phys. Vol. 108 (2010), p. 053509.

[7] A.M. Hofmeister: J. Appl. Phys. Vol. 107 (2010), p. 103532.

[8] W.Y. Ching and Y.N. Xu: Phys. Rev. B Vol. 59(1999), p. 12815.

[9] C.K. Duan, P.A. Tanner, V.N. Makhov and M. Kirm: Phys. Rev. B Vol. 75 (2007), p. 195130.

[10] J.Y. Chen, G.J. Zhao, Y.Y. Sun and T.Y. Liu: Solid State Commun. Vol. 150 (2010), p. 897.

[11] M. Nikl, A. Yoshikawa, A. Vedda and T. Fukuda: J. Cryst. Growth. Vol. 292 (2006), p. 416.

[12] M. Zhuravleva, A. Novoselov, M. Nikl, J. Pejchal, H. Ogino and A. Yoshikawa: J. Cryst. Growth. Vol. 311 (2009), p. 537.

[13] S. Mathur, H. Shen, R. Rapalaviciute, A. Kareiva and N. Donia: J. Mater. Chem. 14 (2004), p. 3259.

[14] D. J. Singh: Phys. Rev. B. Vol. 76 (2007), p. 214115.

[15] R. Hariharan, A. Venkatasubramanian and P. Gopalan: J. Solid State Electr. Vol. 14 (2010), p. 1657.

[16] J.Y. Chen, G.J. Zhao, Q. Dong and Y.C. Ding: J. Alloys Compd. Vol. 506 (2010), p. 500.

[17] J.Y. Chen, G.J. Zhao, D.H. Cao and S.M. Zhou: Curr. Appl. Phys. Vol. 10 (2010), p. 468.

[18] D. H. Cao, G. J. Zhao, Q. Dong, J.Y. Chen, Y. Cheng, and Y.C. Ding: Chinese. Opt. Lett. Vol. 8 (2010), p. 303.

[19] M. Nikl, V.V. Laguta and A. Vedda: Phys. Status Solidi A. Vol. 204 (2007), p. 683.

[20] T.B. de Queiroz, C.R. Ferrari, D. Ulbrich, R. Doylev and A.S.S. de Camargo: Opt. Mater. Vol. 32 (2010), p. 1480.

[21] H. Gao and Y.H. Wang: Mater. Res. Bull. Vol. 42 (2007), p. 921.

[22] I. Stefaniuk, A. Matkovskii, C. Rudowicz, A. Suchocki, Z. Wilamowski, T. Lukasiewicz and Z. Galazka: J. Phys. Condens. Matter. Vol. 18 (2006), p. 4751.

[23] H.Z. Yao, L.Z. Ouyang and W.Y. Ching: J. Am. Ceram. Soc. Vol. 90 (2007), p. 319423204.

[24] F.M. Gao, J.L. He, E.D. Wu, S.M. Liu, D.L. Yu, D.C. Li , S.Y. Zhang and Y.J. Tian: Phys. Rev. Lett. Vol. 91 (2003), p. 015502.

[25] B.X. Liu, W.S. Lai and Z.J. Zhang: Adv. Phys. Vol. 50 (2001), p. 367.

[26] M.D. Segall, P.J.D. Lindan, M.J. Probert, C.J. Pickard, P.J. Hasnip, S.J. Clark and M.C. Payne: J. Phys. Condens. Matter. Vol. 14 (2002), p. 2717.

[27] R. Diehl and G. Brandt: Mat. Res. Bull. Vol. 10 (1975), p. 85.

[28] F. Jollet, C. Nogurea, N. Thromat, M. Gautier, and J.P. Duraud: Phys. Rev. B Vol. 42 (1990), p. 7587.

[29] M. Ishida, K. Takeshita, K. Suzuki and T. Ohba: Energ. Fuel. Vol. 109 (2005), p. 18226.

[30] M. Sanati, G.L.W. Hart and A. Zunger: Phys. Rev. B Vol. 68 (2003), p. 155210.

[31] Y.S. Kim, H. Kanoh, R. Chitrakar, T. Hirotsu and K. Ooi: Chem. Lett. Vol. 10 (2000), p. 1224.

[32] R. Hoffmann: Rev. Mod. Phys. Vol. 60 (1988), p. 6017.

New Materials, Applications and Processes
10.4028/www.scientific.net/AMR.399-401

First-Principles Study on Structure and Stability of YAP Crystal
10.4028/www.scientific.net/AMR.399-401.2144

DOI References

[2] R. Hariharan and P. Gopalan: J. Alloy Compd. Vol. 496 (2010), p.528.
http://dx.doi.org/10.1016/j.jallcom.2010.02.095

[3] Q. Dong, G.J. Zhao, D.H. Cao, J.Y. Chen and Y.C. Ding: J. Alloy Compd. Vol. 493 (2010), p.661.
http://dx.doi.org/10.1016/j.jallcom.2009.12.182

[5] V. Babin, V. Gorbenko, A. Krasnikov, A. Makhov, M. Nikl, S. Zazubovich and Y. Zorenko: Radiation Mearurements. Vol. 45 (2010), p.415.
http://dx.doi.org/10.1016/j.radmeas.2009.09.007

[6] L. Grigorjeva, A. Krasnikov, V.V. Laguta, M. Nikl and S. Zazubovich: J. Appl. Phys. Vol. 108 (2010), p.053509.
http://dx.doi.org/10.1063/1.3459881

[7] A.M. Hofmeister: J. Appl. Phys. Vol. 107 (2010), p.103532.
http://dx.doi.org/10.1063/1.3371815

[8] W.Y. Ching and Y.N. Xu: Phys. Rev. B Vol. 59(1999), p.12815.
http://dx.doi.org/10.1103/PhysRevB.59.12815

[9] C.K. Duan, P.A. Tanner, V.N. Makhov and M. Kirm: Phys. Rev. B Vol. 75 (2007), p.195130.
http://dx.doi.org/10.1103/PhysRevB.75.195130

[10] J.Y. Chen, G.J. Zhao, Y.Y. Sun and T.Y. Liu: Solid State Commun. Vol. 150 (2010), p.897.
http://dx.doi.org/10.1016/j.ssc.2010.01.035

[11] M. Nikl, A. Yoshikawa, A. Vedda and T. Fukuda: J. Cryst. Growth. Vol. 292 (2006), p.416.
http://dx.doi.org/10.1016/j.jcrysgro.2006.04.048

[12] M. Zhuravleva, A. Novoselov, M. Nikl, J. Pejchal, H. Ogino and A. Yoshikawa: J. Cryst. Growth. Vol. 311 (2009), p.537.
http://dx.doi.org/10.1016/j.jcrysgro.2008.09.055

[14] D. J. Singh: Phys. Rev. B. Vol. 76 (2007), p.214115.
http://dx.doi.org/10.1103/PhysRevB.76.214115

[16] J.Y. Chen, G.J. Zhao, Q. Dong and Y.C. Ding: J. Alloys Compd. Vol. 506 (2010), p.500.
http://dx.doi.org/10.1016/j.jallcom.2010.07.063

[17] J.Y. Chen, G.J. Zhao, D.H. Cao and S.M. Zhou: Curr. Appl. Phys. Vol. 10 (2010), p.468.
http://dx.doi.org/10.1016/j.cap.2009.07.006

[19] M. Nikl, V.V. Laguta and A. Vedda: Phys. Status Solidi A. Vol. 204 (2007), p.683.
http://dx.doi.org/10.1002/pssa.200673866

[20] T.B. de Queiroz, C.R. Ferrari, D. Ulbrich, R. Doylev and A.S.S. de Camargo: Opt. Mater. Vol. 32 (2010), p.1480.
http://dx.doi.org/10.1016/j.optmat.2010.06.004

[21] H. Gao and Y.H. Wang: Mater. Res. Bull. Vol. 42 (2007), p.921.
http://dx.doi.org/10.1016/j.materresbull.2006.08.010

[22] I. Stefaniuk, A. Matkovskii, C. Rudowicz, A. Suchocki, Z. Wilamowski, T. Lukasiewicz and Z. Galazka: J. Phys. Condens. Matter. Vol. 18 (2006), p.4751.

http://dx.doi.org/10.1088/0953-8984/18/19/026

[24] F.M. Gao, J.L. He, E.D. Wu, S.M. Liu, D.L. Yu, D.C. Li , S.Y. Zhang and Y.J. Tian: Phys. Rev. Lett. Vol. 91 (2003), p.015502.
http://dx.doi.org/10.1103/PhysRevLett.91.015502

[25] B.X. Liu, W.S. Lai and Z.J. Zhang: Adv. Phys. Vol. 50 (2001), p.367.
http://dx.doi.org/10.1080/00018730110096112

[26] M.D. Segall, P.J.D. Lindan, M.J. Probert, C.J. Pickard, P.J. Hasnip, S.J. Clark and M.C. Payne: J. Phys. Condens. Matter. Vol. 14 (2002), p.2717.
http://dx.doi.org/10.1088/0953-8984/14/11/301

[27] R. Diehl and G. Brandt: Mat. Res. Bull. Vol. 10 (1975), p.85.
http://dx.doi.org/10.1016/0025-5408(75)90125-7

[28] F. Jollet, C. Nogurea, N. Thromat, M. Gautier, and J.P. Duraud: Phys. Rev. B Vol. 42 (1990), p.7587.
http://dx.doi.org/10.1103/PhysRevB.42.7587

[30] M. Sanati, G.L.W. Hart and A. Zunger: Phys. Rev. B Vol. 68 (2003), p.155210.
http://dx.doi.org/10.1103/PhysRevB.68.155210

[31] Y.S. Kim, H. Kanoh, R. Chitrakar, T. Hirotsu and K. Ooi: Chem. Lett. Vol. 10 (2000), p.1224.
http://dx.doi.org/10.1246/cl.2000.1224

[32] R. Hoffmann: Rev. Mod. Phys. Vol. 60 (1988), p.6017.
http://dx.doi.org/10.1103/RevModPhys.60.601