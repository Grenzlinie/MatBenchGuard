# Formation of amorphous phases in an immiscible Cu-Nb system studied by molecular dynamics simulation and ion beam mixing

T.L. Wang, J.H. Li, K.P. Tai and B.X. Liu*

Advanced Materials Laboratory, Department of Materials Science and Engineering, Tsinghua University, Beijing 100084, China

Received 23 January 2007; revised 2 March 2007; accepted 5 March 2007
Available online 19 April 2007

An $n$-body potential is constructed and applied to investigate the crystal-to-amorphous transition of the immiscible Cu-Nb system by molecular dynamics simulation. It is found that supersaturated solid solutions could turn into disordered states when the composition falls into the range of about 15-72 at.% Nb, suggesting that amorphous alloy could be formed in this range for the Cu-Nb system. Interestingly, amorphous phases are obtained in the $\mathrm{Cu}_{70} \mathrm{Nb}_{30}$ and $\mathrm{Cu}_{30} \mathrm{Nb}_{70}$ multilayered films upon ion beam mixing.

© 2007 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

**Keywords**: Amorphous phase; Molecular dynamics simulations; Ion beam mixing; Cu-Nb alloy; Glass-forming ability

In 1959, Klement et al. obtained the first amorphous alloy (metallic glass) by liquid melt quenching in the Au-Si system [1], and since then a number of techniques have been developed to produce amorphous alloys [2]. In the early 1980s, a powerful glass-producing technique, i.e. ion beam mixing (IBM) of multilayered films, was introduced [3], by which a large number of metallic glasses were produced in both miscible and immiscible systems [4]. Subsequently, several empirical criteria and models have been proposed to predict the composition range in which amorphous alloys could be formed [5]. In past decades, significant progress has been achieved in computational materials science, and, as a powerful tool, molecular dynamics (MD) simulation has been widely used to observe and characterize the amorphous alloys of special systems [6-8]. In recent years, the equilibrium immiscible Cu-Nb system characterized with a positive heat of formation $(+4 \mathrm{~kJ} \mathrm{~mol}^{-1})$ has attracted considerable attention, as its composites exhibit high fatigue endurance, and high thermal and electrical conductivity [9,10]. Its equilibrium phase diagram shows that there are no Cu-Nb compounds over the entire composition range [11]. Nonetheless, under far from equilibrium conditions, some metastable crystalline or amorphous phases could be obtained [12-14]. In the present study, MD simulation and IBM experiment are employed to reveal the amorphization behavior of the Cu-Nb system.

To conduct MD simulations, an $n$-body potential is constructed for the Cu-Nb system based on the second moment approximation of the tight-binding (TB-SMA) scheme. In the original TB-SMA formalism, the total energy of a system is given by

$$
E_{\mathrm{tot}}=\frac{1}{2} \sum_{j \neq i} \phi\left(r_{i j}\right)-\sum_{i} \sqrt{\sum_{j \neq i} \psi\left(r_{i j}\right)}. \tag{1}
$$

The first term in the equation is the repulsive portion derived from Born-Mayer pairwise interaction and the second is the band-structure term, i.e. a many-bodied term, which is a second moment approximation of the tight-binding band energy [15]. Here, we make some modification to both terms. To calculate the interaction between $\mathrm{Cu}-\mathrm{Cu}$ and $\mathrm{Cu}-\mathrm{Nb}$, $\phi(r_{i j})$ and $\psi(r_{i j})$ are expressed as follows:

$$
\phi\left(r_{i j}\right)=
\begin{cases}
A_{1} \exp \left[-P_{1}\left(\frac{r_{i j}}{r_{0}}-1\right)\right] & r_{i j}<r_{\mathrm{ml}}, \\
A_{1 \mathrm{~m}} \exp \left[-P_{1 \mathrm{~m}}\left(\frac{r_{i j}}{r_{0}}-1\right)\right]\left(\frac{r_{\mathrm{cl}}}{r_{0}}-\frac{r_{i j}}{r_{0}}\right)^{n_{1}} & r_{\mathrm{ml}}<r_{i j}<r_{\mathrm{cl}},
\end{cases} \tag{2}
$$

* Corresponding author. Tel.: +86 10 6277 2557; fax: +86 10 6277 1160; e-mail: dmslbx@tsinghua.edu.cn

1359-6462/$ - see front matter © 2007 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.scriptamat.2007.03.006

$$
\psi\left(r_{i j}\right)= \begin{cases}A_{2} \exp \left[-P_{2}\left(\frac{r_{i j}}{r_{0}}-1\right)\right] & r_{i j}<r_{\mathrm{m} 2}, \\ A_{2 \mathrm{~m}} \exp \left[-P_{2 \mathrm{~m}}\left(\frac{r_{i j}}{r_{0}}-1\right)\right]\left(\frac{r_{\mathrm{c} 2}}{r_{0}}-\frac{r_{i j}}{r_{0}}\right)^{n_{2}} & r_{\mathrm{m} 2}<r_{i j}<r_{\mathrm{c} 2} .\end{cases}
$$

In the equations, $r_{\mathrm{c} 1}, r_{\mathrm{c} 2}$ are cutoff radii, $r_{0}$ is the first neighbor distance, and $A_{1}, P_{1}, A_{2}$ and $P_{2}$ are adjustable parameters, i.e. potential parameters. $n_{1}$ and $n_{2}$ are generally adopted integer values and can be adjustable, and should be greater than 3 to ensure that $\phi\left(r_{i j}\right), \psi\left(r_{i j}\right)$ and their first derivatives smoothly go to zero at cutoff radii. $A_{1 \mathrm{~m}}, P_{1 \mathrm{~m}}, A_{2 \mathrm{~m}}, P_{2 \mathrm{~m}}, r_{\mathrm{m} 1}$ and $r_{\mathrm{m} 2}$ are also adjustable, but the two functions and their first derivatives should be kept constant at $r_{\mathrm{m} 1}$ and $r_{\mathrm{m} 2}$. If necessary, all the parameters in the equation could be adjustable. While calculating the interaction between $\mathrm{Nb}-\mathrm{Nb}$, the repulsive portion and the band-structure term are expressed as follows:

$$
\phi\left(r_{i j}\right)=\left(r_{i j}-r_{\mathrm{c} 1}\right)^{m}\left(c_{0}+c_{1} r_{i j}+c_{2} r_{i j}^{2}+c_{3} r_{i j}^{3}+c_{4} r_{i j}^{4}\right) \quad r_{i j} \leqslant r_{\mathrm{c} 1},
$$

$$
\psi\left(r_{i j}\right)=\alpha\left(r_{i j}-r_{\mathrm{c} 2}\right)^{n} \exp \left[-\beta\left(\frac{r_{i j}}{r_{0}}-1\right)\right] \quad r_{i j} \leqslant r_{\mathrm{c} 2} .
$$

Here $r_{\mathrm{c} 1}, r_{\mathrm{c} 2}$ are also cutoff radii, $r_{0}$ is the first neighbor distance, and $c_{0}, c_{1}, c_{2}, c_{3}, \alpha$ and $\beta$ are adjustable parameters. $m$ and $n$ are two integers, often greater than 3.

For pure $\mathrm{Cu}$ and $\mathrm{Nb}$, the potential parameters are determined by fitting the experimental properties, i.e. cohesive energy, lattice constant, elastic constants and bulk modulus. The physical properties reproduced from the derived $\mathrm{Cu}$ and $\mathrm{Nb}$ potentials as well as the corresponding experimental properties used in fitting the potential are listed in Table 1. From Table 1, one can see that the derived $\mathrm{Cu}$ and $\mathrm{Nb}$ potentials work fairly well in reproducing the physical properties of the pure $\mathrm{Cu}$ and $\mathrm{Nb}$, respectively. To prove the relevance of the $\mathrm{Cu}$ and $\mathrm{Nb}$ potentials, we also reproduce the cohesive energies of their metastable structures for pure $\mathrm{Cu}$ and $\mathrm{Nb}$, respectively. The results show that the cohesive energy of face-centered cubic (fcc) $\mathrm{Cu}$ is $3.80 \mathrm{eV}$, greater than that of hexagonal close-packed (hcp) or body-centered cubic (bcc) $\mathrm{Cu}$ (3.77 and $3.78 \mathrm{eV}$ ), and that the cohesive energy of bcc $\mathrm{Nb}$ is $7.56 \mathrm{eV}$, greater than that of the fcc or hcp $\mathrm{Nb}$ (7.27 and $7.22 \mathrm{eV}$ ), matching well the fact that the equilibrium states of pure $\mathrm{Cu}$ and $\mathrm{Nb}$ are fcc and bcc structure, respectively. In addition, we further derive the equations of state from the constructed potentials and they agree well with the corresponding Rose's equations [16].

Since, we are dealing with the equilibrium immiscible $\mathrm{Cu}-\mathrm{Nb}$ system, there are few available experimental data related to the $\mathrm{Cu}-\mathrm{Nb}$ compounds. In this respect, the ab initio calculation based on quantum mechanics is known to be a reliable way to acquire some physical properties of the compounds of interest [17]. In the present study, it was carried out by using the well-established Vienna ab initio simulation package (VASP) [18]. Employing the program, we have calculated the lattice constants, cohesive energies, elastic constants and bulk modulus for three hypothetical $\mathrm{Cu}-\mathrm{Nb}$ compounds: $\mathrm{L1}_{2} \mathrm{Cu}_{3} \mathrm{Nb}, \mathrm{B} 2 \mathrm{CuNb}$ and $\mathrm{L1}_{2} \mathrm{CuNb}_{3}$. With the calculated data, the cross potential of the $\mathrm{Cu}-\mathrm{Nb}$ system was fitted. The data of properties obtained from the ab initio calculation and derived from the potential are also listed in Table 1, and one can see that the calculated properties from the constructed cross potential are in good agreement with those obtained from ab initio calculations, qualitatively or semi-quantitatively.

Applying the derived potential, MD simulation is conducted with a Parrinello-Rahman constant pressure scheme and the equations of motion are solved through a fourth-order predictor-corrector algorithm of Gear with a time step $t=5 \times 10^{-15} \mathrm{~s}$ [19]. In the simulations, we use the fcc $\mathrm{Cu}$-based and bcc $\mathrm{Nb}$-based solid solutions models [20], respectively. The solid solution models consist of $8 \times 8 \times 8=512$ unit cells (2048 atoms) for the fcc $\mathrm{Cu}$-based solid solution and $10 \times 10 \times 10=1000$ unit cells (2000 atoms) for the bcc $\mathrm{Nb}$-based solid solutions, respectively. For all solid solution models, the [100], [010] and [001] crystalline directions are parallel to the $x, y$ and $z$ axes, respectively, and in these three axes, the periodic boundary conditions are adopted. In setting the solid solution models, the solute atoms are added into the model by randomly substituting the desired number of solvent atoms to obtain the initial state of the solid solution models. Simulations are conducted under the pressure of $0 \mathrm{~Pa}$ and the temperature of $300 \mathrm{~K}$ for 50,000 MD time steps to reach a relatively stable state, when all the related dynamic variables show no secular variation. The structural phase transitions in the solid solutions are monitored by the projections of atomic positions and the pair-correlation function $g(r)$ [21].

Table 1. The lattice constants $(a)$, cohesive energy $\left(E_{\mathrm{c}}\right)$, elastic constants $\left(C_{i j}\right)$ and bulk modulus $\left(B_{0}\right)$ reproduced from the present potential, together with their experimental values of $\mathrm{Cu}$ and $\mathrm{Nb}$ and ab initio calculations of $\mathrm{L1}_{2} \mathrm{Cu}_{3} \mathrm{Nb}, \mathrm{B} 2 \mathrm{CuNb}$ and $\mathrm{L1}_{2} \mathrm{CuNb}_{3}$

<table>
<thead>
<tr>
<th></th>
<th></th>
<th>Cu</th>
<th>Nb</th>
<th>L1₂ Cu₃Nb</th>
<th>B2 CuNb</th>
<th>L1₂ CuNb₃</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a$ (Å)</td>
<td>This work</td>
<td>3.62</td>
<td>3.30</td>
<td>3.77</td>
<td>3.16</td>
<td>3.96</td>
</tr>
<tr>
<td></td>
<td>Exp./ab initio</td>
<td>3.62</td>
<td>3.30</td>
<td>3.81</td>
<td>3.12</td>
<td>4.05</td>
</tr>
<tr>
<td>$E_{\mathrm{c}}$ (eV)</td>
<td>This work</td>
<td>3.80</td>
<td>7.56</td>
<td>3.75</td>
<td>4.40</td>
<td>5.77</td>
</tr>
<tr>
<td></td>
<td>Exp./ab initio</td>
<td>3.49</td>
<td>7.57</td>
<td>4.18</td>
<td>5.35</td>
<td>6.40</td>
</tr>
<tr>
<td>$C_{11}$ (Mbar)</td>
<td>This work</td>
<td>1.65</td>
<td>2.51</td>
<td>1.50</td>
<td>0.89</td>
<td>0.98</td>
</tr>
<tr>
<td></td>
<td>Exp./ab initio</td>
<td>1.68</td>
<td>2.47</td>
<td>1.49</td>
<td>1.69</td>
<td>0.94</td>
</tr>
<tr>
<td>$C_{12}$ (Mbar)</td>
<td>This work</td>
<td>1.24</td>
<td>1.33</td>
<td>1.28</td>
<td>1.32</td>
<td>1.77</td>
</tr>
<tr>
<td></td>
<td>Exp./ab initio</td>
<td>1.22</td>
<td>1.35</td>
<td>1.54</td>
<td>1.70</td>
<td>1.92</td>
</tr>
<tr>
<td>$C_{44}$ (Mbar)</td>
<td>This work</td>
<td>0.79</td>
<td>0.29</td>
<td>0.66</td>
<td>0.56</td>
<td>0.81</td>
</tr>
<tr>
<td></td>
<td>Exp./ab initio</td>
<td>0.76</td>
<td>0.29</td>
<td>0.48</td>
<td>0.48</td>
<td>0.44</td>
</tr>
<tr>
<td>$B_{0}$ (Mbar)</td>
<td>This work</td>
<td>1.38</td>
<td>1.72</td>
<td>1.36</td>
<td>1.17</td>
<td>1.51</td>
</tr>
<tr>
<td></td>
<td>Exp./ab initio</td>
<td>1.37</td>
<td>1.70</td>
<td>1.48</td>
<td>1.68</td>
<td>1.59</td>
</tr>
</tbody>
</table>

We now present the results of the simulation. Figure
1 shows the projections of the atomic positions along
[001] for the (a) $\text{Cu}_{90}\text{Nb}_{10}$, (b) $\text{Cu}_{85}\text{Nb}_{15}$ and (c)
$\text{Cu}_{60}\text{Nb}_{40}$ fcc Cu-based solid solutions and the (d)
$\text{Cu}_{25}\text{Nb}_{75}$, (e) $\text{Cu}_{28}\text{Nb}_{72}$ and (f) $\text{Cu}_{50}\text{Nb}_{50}$ bcc Nb-based
solid solutions after annealing at 300 K for 50,000 MD
time steps. From Figure 1, it can clearly be seen that
for the solid solution with 10% Nb, the fcc crystalline
structure remains. However, for the solid solution with
more than 15% Nb, the crystalline lattice has apparently
collapsed and turned into a disordered state, i.e. a crys-
tal-to-amorphous transition has occurred. To further
confirm the phase transition, Figure 2a–c shows the
total and partial pair-correlation functions $g(r)$ for fcc
Cu-based solid solutions. In the figure, as the $g(r)$ curve
of the $\text{Cu}_{90}\text{Nb}_{10}$ simulation model shows apparent sharp
peaks even at a large distance, the $\text{Cu}_{90}\text{Nb}_{10}$ simulation
model is considered to still have a crystalline structure.
For comparison, in the $\text{Cu}_{85}\text{Nb}_{15}$ and $\text{Cu}_{60}\text{Nb}_{40}$ simula-
tion models, although the first and the second peaks of
the $g(r)$ curves are still clear, there are no discernible
peaks beyond the third-nearest neighbors. Judging by
Zallen’s criterion [21], one can conclude from the calcu-
lated total and partial pair-correlation functions that a
crystal-to-amorphous transition has indeed taken place
in both the $\text{Cu}_{85}\text{Nb}_{15}$ and $\text{Cu}_{60}\text{Nb}_{40}$ simulation models.

![](./images/811999286626615298_1.jpg)

Figure 1. The projections of the atomic positions along [001] for the
$\text{Cu}_{90}\text{Nb}_{10}$ (a), $\text{Cu}_{85}\text{Nb}_{15}$ (b) and $\text{Cu}_{60}\text{Nb}_{40}$ (c) fcc Cu-based solid
solutions, and $\text{Cu}_{25}\text{Nb}_{75}$ (d), $\text{Cu}_{28}\text{Nb}_{72}$ (e) and $\text{Cu}_{50}\text{Nb}_{50}$ (f) bcc Nb-
based solid solutions after annealing at 300 K for 50,000 MD time
steps.

![](./images/811999286626615298_2.jpg)

Figure 2. The calculated $g(r)$ curves for the three fcc Cu-based solid
solutions with overall compositions of $\text{Cu}_{90}\text{Nb}_{10}$ (a), $\text{Cu}_{85}\text{Nb}_{15}$ (b) and
$\text{Cu}_{60}\text{Nb}_{40}$ (c) and three Nb-based bcc solid solutions with overall
compositions of $\text{Cu}_{25}\text{Nb}_{75}$ (d), $\text{Cu}_{28}\text{Nb}_{72}$ (e) and $\text{Cu}_{50}\text{Nb}_{50}$ (f).

These results clearly indicate that in the Cu–Nb system,
when the Nb concentration is equals to or exceeds
15 at.%, the fcc Cu-based solid solution becomes unsta-
ble and turns into amorphous phase. Similarly, for the
bcc Nb based solid solution, Figures 1d–f and 2d–f
shows that the critical solid solubility is 28 at.% Cu.

Figure 3 shows the molar enthalpy and volume as
functions of composition calculated from MD simula-
tion. For Cu-rich solid solutions, one can see a sudden
drop in the molar enthalpy curve and a kink in the vol-
ume curve at 15 at.% Nb, respectively. For Nb-rich solid
solutions, similar behaviors are also observed in molar
enthalpy and volume curves at 28 at.% Cu. These abrupt
changes indicate that crystal–amorphous transition in-
deed takes place at the two critical points and that amor-
phous alloys could be formed within the composition

![](./images/811999286626615298_3.jpg)

Figure 3. The molar enthalpy and volume as a function of alloy
composition in Cu-rich solid solutions (0–50 at.% Nb) and Nb-rich
solid solutions (0–50 at.% Cu) after simulation performed at 300 K for
50,000 MD time steps. The dashed line is the molar enthalpy of
unstable solid solution extrapolated from the values of terminal solid
solutions, and the solid circles represent for the molar enthalpies of the
hypothetic $\text{L1}_2$ $\text{Cu}_3\text{Nb}$, B2 CuNb and $\text{L1}_2$ $\text{CuNb}_3$ compounds.

range bounded by the two critical points. Figure 3 also exhibits the molar enthalpies of unstable solid solution extrapolated from the values of terminal solid solutions, as well as the molar enthalpies of the hypothetical L1₂ Cu₃Nb, B2 CuNb and L1₂ CuNb₃ compounds. One can see that, within the composition range of 15–72 at.% Nb, the molar enthalpy of amorphous phase is lower than that of solid solution and compound, suggesting that amorphous phase is formed by preference.

To confirm the results of the MD simulation, two Cu–Nb multilayered films with compositions of Cu₇₀Nb₃₀ and Cu₃₀Nb₇₀ are designed and irradiated by 200 keV xenon ions. To match the irradiating ion range, the total thickness of the films is calculated to be around 42 nm, according to the TRIM program [22]. The films are designed to consist of 15 and 13 layers, respectively. The Cu–Nb multilayered films are prepared by depositing alternatively pure Cu and Nb at a rate of 0.2 Å s⁻¹ onto NaCl single crystals as substrates in an e-gun evaporation system with a vacuum level better than 10⁻⁶ Pa and irradiated by xenon ions in an implanter with a vacuum level better than 5 × 10⁻⁴ Pa. The irradiation dose is in a range from 8 × 10¹⁴ to 9 × 10¹⁵ Xe⁺ cm⁻². During irradiation, the sample holder is cooled by liquid nitrogen (77 K) and the current density is confined to be about 2 μA cm⁻² to minimize any overheating effect.

After irradiation, energy-disperse spectrum and X-ray fluorescence examinations were employed to ascertain the real compositions of the Cu–Nb films. For structural characterization, the samples are examined by transmission electron microscopy and amorphous phases are observed in both samples after various irradiation. Figure 4a and b shows the selected area diffraction (SAD) patterns of the Cu₇₀Nb₃₀ multilayered films upon irradiation doses of 8 × 10¹⁴ and 2 × 10¹⁵ Xe⁺ cm⁻², respectively. One can see from Figure 4a that the sharp diffraction lines of Cu and Nb remain, while in Figure 4b only diffused halos exist, indicating that an amorphous phase is formed. Similarly, Figure 4c and d shows the SAD patterns of the Cu₃₀Nb₇₀ multilayered films upon irradiation doses of 8 × 10¹⁴ and 9 × 10¹⁵ Xe⁺ cm⁻², respectively. The diffused halo shown in Figure 4d indicates that an amorphous phase is also formed in Cu₃₀Nb₇₀ multilayered films. In short, the experiment supports the results obtained from the MD simulations. In addition, Michaelsen et al. have also obtained amorphous alloys within the composition range of 23–68 at.% Nb by triode-magnetron sputtering [23].

![](./images/811999286626615298_4.jpg)

Figure 4. The SAD patterns of the Cu₇₀Nb₃₀ multilayered films after irradiation doses of 8 × 10¹⁴ Xe⁺ cm⁻² (a) and 2 × 10¹⁵ Xe⁺ cm⁻² (b), and the Cu₃₀Nb₇₀ multilayered film after irradiation doses of 8 × 10¹⁴ Xe⁺ cm⁻² (c) and 9 × 10¹⁵ Xe⁺ cm⁻² (d).

In summary, based on the TB-SMA formalism, an n-body potential is constructed for the immiscible Cu–Nb system and proven to work fairly well in reproducing some physical properties. MD simulations and IBM experiments are carried out and the results suggest that Cu–Nb amorphous phases may be formed in the range of about 15–72 at.% Nb.

The authors are grateful for the financial support from the National Natural Science Foundation of China (50531040), The Ministry of Science and Technology of China (2006CB605201) and the Administration of Tsinghua University.

Supplementary data associated with this article can be found, in the online version, at doi:10.1016/j.scriptamat.2007.03.006.

[1] W. Klement, R.H. Willens, P. Duwez, Nature 187 (1960) 869.
[2] A. Lindsay Greer, Science 267 (1995) 1947.
[3] B.X. Liu, W.L. Johnson, M.A. Nicolet, S.S. Lau, Appl. Phys. Lett. 42 (1983) 45.
[4] B.X. Liu, W.S. Lai, Q. Zhang, Mater. Sci. Eng. 244 (2000) 1.
[5] B.X. Liu, Mater. Lett. 5 (1987) 322.
[6] J.H. He, E. Ma, Phys. Rev. B 64 (2001) 144206.
[7] J.H. He, H.W. Sheng, P.J. Schilling, C.-L. Chien, E. Ma, Phys. Rev. Lett. 86 (2001) 2826.
[8] J.H. Li, S.H. Liang, B.X. Liu, J. Phys. Chem. B 109 (2005) 16463.
[9] Y.C. Wang, A. Misra, R.G. Hoagland, Scripta Mater. 54 (2005) 1593.
[10] E. Botcharova, J. Freudenberger, L. Schultz, Acta Mater. 54 (2006) 3333.
[11] F.R. de Boer, R. Boom, W.C.M. Mattens, A.R. Miedema, A.K. Niessen, Cohesion in Metals: Transition Metal Alloy, North Holland, Amsterdam, 1989.
[12] X. Sauvage, L. Renaud, B. Deconihout, D. Blavette, D.H. Ping, K. Hono, Acta Mater. 49 (2001) 389.
[13] F. Pan, Z.F. Ling, K.Y. Gao, B.X. Liu, Mater. Res. Soc. Symp. Proc. 398 (1996) 337.
[14] S. Yamamoto, H. Naramoto, B. Tuchiya, K. Narumi, Y. Aoki, Thin Solid Films 335 (1998) 85.
[15] C. Massobrio, V. Pontikis, G. Martin, Phys. Rev. B 41 (1990) 10486.
[16] J.H. Rose, J.R. Smith, F. Guinea, J. Ferrante, Phys. Rev. B 29 (1984) 2963.
[17] R. Siegl, M. Yan, V. Vitek, Model. Simul. Mater. Sci. Eng. 5 (1997) 105.
[18] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169.
[19] M. Parrinello, A. Rahman, J. Appl. Phys. 52 (1981) 7182.
[20] B.X. Liu, W.S. Lai, Z.J. Zhang, Adv. Phys. 50 (2001) 367.
[21] Z. Zallen, The Physics of Amorphous Solid, Wiley InterScience, New York, 1983.
[22] J.F. Ziegler, J.P. Biersack, U. Littmark, The Stopping and Range of Ions in Solids, Pergamon Press, New York, 1992.
[23] C. Michaelsen, C. Gente, R. Bormann, J. Appl. Phys. 81 (1997) 6024.