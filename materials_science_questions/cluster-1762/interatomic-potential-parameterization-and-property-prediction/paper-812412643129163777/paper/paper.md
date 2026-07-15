![](./images/812412643129163777_1.jpg)

Available online at www.sciencedirect.com

![](./images/812412643129163777_2.jpg)

Nuclear Instruments and Methods in Physics Research B 202 (2003) 93–99

![](./images/812412643129163777_3.jpg)

www.elsevier.com/locate/nimb

# Molecular dynamics study of defect formation in GaN cascades

J. Nord $^{a,*}$, K. Nordlund $^{a}$, J. Keinonen $^{a}$, K. Albe $^{b}$

$^{a}$ Accelerator Laboratory, University of Helsinki, P.O. Box 43, FIN-00014, Helsinki, Finland
$^{b}$ Institut für Materialwissenschaft, TU Darmstadt, D-64287 Darmstadt, Germany

## Abstract
Simulations of irradiation effects in compound semiconductors require interatomic potentials which describe not only the compound phases, but also the pure constituents and defects. We discuss a systematic approach based on the analytic bond-order scheme for constructing such potentials and give an example for GaN. Finally, this potential is employed for simulations of defect formation in GaN by ion irradiation for recoils in the 200 eV to 10 keV energy range. Results on the total damage production are presented and compared with other semiconductors and experiments.

© 2002 Elsevier Science B.V. All rights reserved.

_PACS:_ 61.50.Ah; 61.50.Lt; 61.72.Ji; 81.05.Ea
_Keywords:_ Irradiation; Defects; Semiconductors; GaN

---

## 1. Introduction

In the past decades ion beam methods have played a major role especially in the semiconductor industry and were applied in the modification of material properties as well as manufacturing of miniature components [1]. Therefore, further development of these methods requires the precise knowledge of effects related to ion irradiation.

Although gallium nitride has only been actively studied for about 10 years, components based on this material have already reached the commercial marketplace [2]. Because of its large, direct band gap ($\sim$3 eV), it is especially interesting for opto-electronic applications, as devices emitting any wavelength of visible light can, at least in principle, be manufactured from it.

Ion implantation has many attractive aspects for the processing of GaN [3]. Despite this, not much is known about the microscopic mechanisms of damage production during ion irradiation. There is evidence that damage production in GaN is even more complex in the more traditional semiconductor materials. For instance, the damage level seems to depend strongly on the mass of the irradiating ions (even after normalization with the nuclear deposited energy), which has been interpreted as a sign of dynamic in-cascade defect annealing similar to that in metals [4].

In most other semiconductors, molecular dynamics computer simulations have proved to be an

---

*Corresponding author. Tel.: +358-9-191-50013; fax: +358-9-191-50042.
_E-mail address:_ janne.nord@helsinki.fi (J. Nord).

0168-583X/02/$ - see front matter © 2002 Elsevier Science B.V. All rights reserved.
doi:10.1016/S0168-583X(02)01839-6

invaluable tool for gaining understanding of the atomic level damage production mechanisms [5–8]. Since suitable interatomic potential for GaN were not available, MD simulation studies of irradiation effects have been impossible, so far.

Hence, we have developed a potential for GaN which we aimed to have as wide applicability as possible. With this potential we have simulated collision cascades in GaN, analyzed the produced damage, and compared to other semiconductors in an attempt to understand the large differences between the materials.

In this paper, we first briefly describe the principles we use to develop the potential, and then proceed with discussing our results on damage production in GaN.

## 2. The principles of potential development

When potentials are developed or chosen for the study of far-from-equilibrium effects such as those induced by ion irradiation, one of course first has to consider what physical effects are important.

Ion irradiation can lead to many effects in materials. Some of the more important ones are defect production, inducing phase changes (melting, amorphization and recrystallization), element mixing in multicomponent samples, and segregation in compounds.

All these effects correspond to a variety of local atomic configurations and therefore realistic simulations are only possible if the chosen interatomic potential goes beyond merely reproducing stable ground state structures. Hence a prerequisite for simulations of far-from-equilibrium effects are potentials which describe many structurally different atomic configurations with sufficient accuracy.

Most potentials for compound semiconductors including the widely used multicomponent potentials of Tersoff [9] are analytic bond-order potentials. Their general idea is to write the total potential energy as sum over individual bond strengths, where the attractive pair potentials $V_{\mathrm{A}}$ is moderated by the environment-dependent bond-order $\overline{b_{i j}}$:

$$
E=\sum_{i>j} f_{i j}\left(r_{i j}\right)\left[V_{\mathrm{R}}^{i j}\left(r_{i j}\right)-\overline{b_{i j}} V_{\mathrm{A}}^{i j}\left(r_{i j}\right)\right]. \tag{1}
$$

Here $r_{i j}$ is the interatomic separation between atoms $i$ and $j, V_{\mathrm{R}}$ the pair-like repulsion and $V_{\mathrm{A}}$ the pair-like attraction, while $f_{i j}$ describes the cutoff function limiting the interaction radius to the first neighbor shell. In principle there is no strict rule how to choose the pair-like term. For the case of a dimer, however, $\overline{b_{i j}}$ equals one and therefore Eq. (1) reduces to $E=V_{\mathrm{A}}-V_{\mathrm{R}}$. Therefore it is convenient to choose a Morse-like form as proposed first by Brenner [10], where $V_{\mathrm{R}}$ and $V_{\mathrm{A}}$ depend on the bond energy $D_{0}$ and distance $r_{0}$ of the diatomic molecule:

$$
\begin{aligned}
& V_{\mathrm{R}}(r)=\frac{D_{0}}{S-1} \exp \left(-\beta \sqrt{2 S}\left(r-r_{0}\right)\right), \\
& V_{\mathrm{A}}(r)=\frac{S D_{0}}{S-1} \exp \left(-\beta \sqrt{2 / S}\left(r-r_{0}\right)\right).
\end{aligned} \tag{2}
$$

In these functions $S$ is an adjustable parameter, while $\beta$ is given by the ground state oscillation frequency.

The bond-order $\overline{b_{i j}}$ contains all information of the atomic neighbourhood. Based on the second-moment tight-binding approximation it depends on the square-root of the coordination number. Details on the analytic form of the bond-order term which is similar to that used by Brenner [10,11] can be found elsewhere [12,13].

One important modification of the potential is required for simulations of ion-irradiation, because the repulsion gets artificially small at short distances. If we assume that $V_{\text {short }}$ describes a pairpotential that is valid at small distances, like the ZBL-potential [14], the total potential $E=\sum \Phi_{i j}$ can simply be constructed with $\Phi_{i j}(r)=[1-F(r)] \times$ $V_{\text {short }}(r)+F(r)\left(V_{\mathrm{R}}(r)-\overline{b_{i j}} V_{\mathrm{A}}(r)\right)$, where $F(r)=1 /$ $\left(1+\exp \left(-b_{f}\left(r-r_{f}\right)\right)\right)$. Note that this method avoids jumps in the total potential curve that occur if only the dimer potential is splined to a repulsive term.

During the construction of the potential, cohesive properties of reference structures with different coordination numbers $Z$ are required, which mostly can be obtained from ab initio calculations. These data include at least cohesive energies and

bonding distances, and for the most important structures also the elastic constants.

Now it is important to note that within the bond-order formalism that the equilibrium bond lengths $r_{\mathrm{b}}$ and energies $E_{\mathrm{b}}$ of all stable structures follow the simple Pauling relationship

$$
E_{\mathrm{b}}=-D_{0} \exp \left(-\beta \sqrt{2 S}\left(r_{\mathrm{b}}-r_{0}\right)\right), \tag{3}
$$

which holds true regardless of the specific choice for $\overline{b_{i j}}$.

Since the dimer parameters are fixed, the only free parameter is $S$. By plotting the cohesive energy vs. bond length data for the different polytypes for which data are available, one can adjust the parameter $S$ to give the best fit for different coordinations. This is illustrated for the case of nitrogen in Fig. 1.

In the same way parameters for all possible pair-interactions are fitted independently, but not taken from averages as in the multicomponent potential of Tersoff [9].

In addition to fitting the different structures, we emphasize the importance of testing the potential in non-equilibrium situations. There are several ways in which a seemingly good fit can produce artificial structures lower in potential energy than the true ground state. The best test we know of for finding these are simulations of melting. In case a grossly wrong minimum exists, even a simple simulation of slow quenching of a random structure starting from a high temperature is likely to spot the minimum. However, if a minimum exists which is only slightly (of the order of 0.1 eV/atom) lower in energy than the true ground state, such a simulation is not likely to find it. In this case, however, long simulations of a solid and liquid in equilibrium close to the melting point can spot such minima, since the liquid-solid interface can act as a seed for a structural transformation. In our previous tests of GaAs potentials, we have found that several well-motivated potentials indeed had wrong minima [15,16]. In our own potential development we have also discarded several parameter sets on these grounds.

In the final testing of the potential, adjusting the cutoff range can often be used to somewhat improve on non-equilibrium properties such as melting and surface reconstruction energetics.

This approach has previously been used by Albe for BN [17], and recently in our collaborative team for PtC [12] and GaAs [13]. Very recently we have developed a potential for GaN, the main features of which we describe here. Additional details will be given elsewhere.

The Ga part of the potential is from [13], except that the cutoff function region has been shortened to be able to handle GaN structures with relatively short distances between second-nearest Ga-Ga neighbours. It is noteworthy that this potential achieves describing the very complex crystal structure of Ga (with seven nearest neighbours at four different bonding distances) as the ground state.

For the N part the most important consideration are of course the dimer properties, which are easily accounted for using the formalism described above. But there exists extensive literature data for hypothetical high-pressure phases of N [18], and quite recently a polymeric nitrogen phase has been reported [19]. Our potential can describe all of these phases reasonably well.

![](./images/812412643129163777_4.jpg)

Fig. 1. Illustration of fitting the energy-bond relation to DFT data for nitrogen [18]. By choosing the parameter $S$, one can adjust the slope of the fitted line. The plot then allows for easy visual inspection of which coordinations are described well, and which are not. In this particular case, the potential would realistically describe all phases except for fcc.

For the Ga–N fit, we considered of course the tetrahedral wurtzite and zincblende structures, but also the dimer ($Z=1$), B1 ($Z=6$) and B2 ($Z=8$) structures, to obtain a description of a wide range of coordinations in a compound.

For all the three cases, we obtained satisfactory description of all the coordinations. This gives us confidence that we can use the model to examine not only single cascades, but also prolonged irra- diation of GaN where complex phase transitions are known to occur.

The potential parameters are given in Appen- dix A.

### 3. Method

Defect production in bulk GaN was studied by simulating collision cascades using molecular dy- namics methods. The recoil energies varied from 200 eV to 10 keV and the number of atoms was between 8000 and 1,800,000 depending on the re- coil energy. Statistics were collected separately for both recoil atom types and 8–100 simulations were run for all the cases.

Berendsen temperature control [20] was used at the borders of the simulation cell to remove the excess heat produced by the cascades. A variable time step was used to speed up the simulations. Closer details about the simulation method are described elsewhere [7,8].

The defects were recognized by using the Voronoi-polyhedron approach. The positions of the atoms after the recoil event were assigned to belong to some Voronoi polyhedron of the initial lattice configuration. An empty polyhedron was considered as a vacancy. If a multiply filled poly- hedra contained atoms only of the same type as it initially contained, all atoms except the initial one were counted as interstitials. Otherwise one of the atoms was counted as an antisite and the others as interstitials. Also atoms on a singly filled poly- hedron of a wrong type were considered antisites.

### 4. Results

#### 4.1. Threshold and average displacement energy

We first determined the threshold displacement energy for both atom types. The minimum values were below $22\pm1$ eV for Ga and $25\pm1$ eV for N. We also determined the spatial average of the threshold displacement energy by finding the threshold value for 1000 randomly chosen direc- tions. An average value of $45\pm1$ eV for Ga and $109\pm2$ eV for N was obtained.

#### 4.2. Defect production

The average production of each type of point defect is listed in Table 1. For all the tested recoil

<table>
<caption>Table 1 Average production of point defects in 200 eV to 10 keV cascades in GaN for N and Ga recoils</caption>
<thead>
<tr>
<th>$E$/eV</th>
<th>$V_{\text{N}}$</th>
<th>$V_{\text{Ga}}$</th>
<th>$I_{\text{N}}$</th>
<th>$I_{\text{Ga}}$</th>
<th>$\text{N}_{\text{Ga}}$</th>
<th>$\text{Ga}_{\text{N}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7">$N$ recoil</td>
</tr>
<tr>
<td>200</td>
<td>$1.00\pm0.09$</td>
<td>$0.12\pm0.05$</td>
<td>$0.80\pm0.09$</td>
<td>$0.32\pm0.07$</td>
<td>$0.22\pm0.06$</td>
<td>$0.02\pm0.02$</td>
</tr>
<tr>
<td>400</td>
<td>$1.33\pm0.15$</td>
<td>$1.37\pm0.18$</td>
<td>$1.27\pm0.17$</td>
<td>$1.43\pm0.14$</td>
<td>$0.43\pm0.09$</td>
<td>$0.33\pm0.09$</td>
</tr>
<tr>
<td>1000</td>
<td>$3.29\pm0.25$</td>
<td>$2.14\pm0.35$</td>
<td>$2.67\pm0.32$</td>
<td>$2.76\pm0.29$</td>
<td>$1.33\pm0.21$</td>
<td>$0.71\pm0.20$</td>
</tr>
<tr>
<td>2000</td>
<td>$3.87\pm0.85$</td>
<td>$5.3\pm0.9$</td>
<td>$3.13\pm0.58$</td>
<td>$6.0\pm0.7$</td>
<td>$1.50\pm0.60$</td>
<td>$0.75\pm0.25$</td>
</tr>
<tr>
<td>5000</td>
<td>$11.2\pm1.0$</td>
<td>$11.3\pm1.0$</td>
<td>$9.9\pm0.8$</td>
<td>$12.6\pm1.1$</td>
<td>$4.2\pm0.6$</td>
<td>$2.92\pm0.45$</td>
</tr>
<tr>
<td>10,000</td>
<td>$29.5\pm2.7$</td>
<td>$21.4\pm0.9$</td>
<td>$24.9\pm1.9$</td>
<td>$26.0\pm1.1$</td>
<td>$12.4\pm1.2$</td>
<td>$7.8\pm0.9$</td>
</tr>
<tr>
<td colspan="7">Ga recoil</td>
</tr>
<tr>
<td>200</td>
<td>$0.32\pm0.051$</td>
<td>$1.28\pm0.05$</td>
<td>$0.41\pm0.06$</td>
<td>$1.19\pm0.05$</td>
<td>$0.02\pm0.014$</td>
<td>$0.12\pm0.03$</td>
</tr>
<tr>
<td>400</td>
<td>$1.24\pm0.17$</td>
<td>$1.80\pm0.10$</td>
<td>$1.2\pm0.14$</td>
<td>$1.84\pm0.09$</td>
<td>$0.30\pm0.07$</td>
<td>$0.26\pm0.06$</td>
</tr>
<tr>
<td>1000</td>
<td>$4.05\pm0.42$</td>
<td>$3.05\pm0.28$</td>
<td>$3.6\pm0.39$</td>
<td>$3.50\pm0.26$</td>
<td>$1.25\pm0.24$</td>
<td>$0.80\pm0.21$</td>
</tr>
<tr>
<td>2000</td>
<td>$6.1\pm0.5$</td>
<td>$4.8\pm0.5$</td>
<td>$4.9\pm0.4$</td>
<td>$6.0\pm0.6$</td>
<td>$1.18\pm0.23$</td>
<td>$2.36\pm0.39$</td>
</tr>
<tr>
<td>5000</td>
<td>$13.1\pm1.0$</td>
<td>$11.3\pm0.6$</td>
<td>$11.3\pm0.4$</td>
<td>$13.1\pm1.0$</td>
<td>$4.6\pm0.7$</td>
<td>$2.75\pm0.53$</td>
</tr>
<tr>
<td>10,000</td>
<td>$24.6\pm2.2$</td>
<td>$22.1\pm1.4$</td>
<td>$21.8\pm2.2$</td>
<td>$25.0\pm1.4$</td>
<td>$8.8\pm1.5$</td>
<td>$5.9\pm1.4$</td>
</tr>
</tbody>
</table>

![](./images/812412643129163777_5.jpg)

Fig. 2. Number of Voronoi defects produced by Ga and N recoils in GaN and linear fits to data. For comparison the damage production in GaAs is also shown. The GaAs data is from [21].

energies there are fewer vacancies, interstitials and antisites than for GaAs, Si or Ge [7,21]. This is illustrated in Fig. 2.

This is in agreement with the experimental fact that GaN is more difficult to amorphize than the other listed materials (compare e.g. the amorph- ization doses in [4,22]). At energies higher than 2 keV both gallium and nitrogen recoils have sepa- rated into subcascades. This explains the linear behavior of the damage production for recoils with higher initial energies.

The subcascade structure is illustrated in Fig. 3 for a 5 keV recoil. Note the clear difference to GaAs, where it is known from both simulation and experiment that even cascades induced by 10 keV recoils often produce a single amorphous zone [21,23].

## 5. Discussion and outlook

In experimental studies of damage production in GaN, it has been reported that significant dy- namic annealing of defects can occur even at liquid nitrogen temperatures [4]. This effect would be akin to that in metals, where it is well understood both from experiment and MD simulations [24]. A signature of this effect is that the damage pro- duction falls dramatically (by up to an order of

![](./images/812412643129163777_6.jpg)

Fig. 3. Illustration of the damage produced in a sample 5 keV recoil. The size of the atoms reflects the differences in the potential energy, so that damaged areas can be seen as larger atoms. The darker atoms are Gallium and lighter ones Nitrogen.

![](./images/812412643129163777_7.jpg)

Fig. 4. Damage production in GaN by Ga and N recoils, compared with the prediction of the Kinchin–Pease equations.

magnitude) below that predicted by the Kinchin–Pease equation [24]. To test whether the same ef- fect could explain why we have less damage in our simulations, we compare our results with the Kinchin–Pease equation, evaluated with the aver- age displacement energies reported above. This is illustrated in Fig. 4.

As we see from the figure, although there is some deviation from the Kinchin–Pease predic- tions, this is not nearly enough to explain the large difference of about a factor of 5 from GaAs. Since our model also does not have explicit ionic inter- actions, or account for thermal defect migration, we can conclude that the reason to the low damage production must be simply the larger mechanical strength of GaN compared to GaAs (the former has a bulk modulus of 200 GPa, and the latter only 75).

But this simple effect is unlikely to fully explain the large experimental radiation hardness of GaN. Quantitative comparison of amorphization doses is complicated by the observation that different ions amorphize GaN at quite different deposited energy levels, in contrast to the much simpler be- haviour in common semiconductors such as Si [25]. But comparison of the amorphization doses (e.g. in [4,22]) by normalizing with the maximum nuclear deposited energy, indicates that the dose between GaAs and GaN may differ by as much as 2–3 orders of magnitude, much more than the factor of 5 which we observe. There are several possible reasons to this. One is that cascade over- lap has a damage-reducing effect, an effect known in metals [26], another that the long-range ionic interactions make possible recombination of close damage at low temperatures, which is much more efficient than that observed in other semiconduc- tors [27–29].

The potential model we have used in this work contains only short range interactions. However, the model does reproduce many important prop- erties of GaN, such as crystal structure and melt- ing properties. The effect of the long range ionic interaction to these properties is implicitly cap- tured in the short range parametrization. It is not clear how important the long range interactions are to the problems discussed in this work. Hence further simulations and possibly additional model development are clearly needed to understand the intriguing behaviour of GaN during ion irradia- tion.

## Acknowledgements

The research was supported by the Academy of Finland under project Nos. 44215 and 73722. Additional travel fundings of the DAAD and the Academy of Finland as well as Grants for computer time from the Center for Scientific Computing in Espoo, Finland are gratefully acknowledged.

## Appendix A. Potential function

The GaN potential we have used in this work is described in greater detail elsewhere [30]. It has the same functional form as the Pt–C potential model by Albe et al. [12]. Many important properties, such as melting, point defect formation energies and elastic constants, energetics and bond lengths of several Ga, N and GaN phases, are correctly reproduced.

The parameter values are given in Table 2.

<table>
<caption>Table 2
Full parameter set for the interactions</caption>
<thead>
<tr>
<th>ij</th>
<th>Ga–Ga</th>
<th>Ga–N</th>
<th>N–N</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\gamma$</td>
<td>0.007874</td>
<td>0.001632</td>
<td>0.76612</td>
</tr>
<tr>
<td>$S$</td>
<td>1.11</td>
<td>1.1122</td>
<td>1.4922</td>
</tr>
<tr>
<td>$\beta$ (Å$^{-1}$)</td>
<td>1.08</td>
<td>1.968</td>
<td>2.05945</td>
</tr>
<tr>
<td>$D_e$ (eV)</td>
<td>1.40</td>
<td>2.45</td>
<td>9.91</td>
</tr>
<tr>
<td>$R_e$ (Å)</td>
<td>2.3235</td>
<td>1.921</td>
<td>1.11</td>
</tr>
<tr>
<td>$c$</td>
<td>1.918</td>
<td>65.207</td>
<td>0.178493</td>
</tr>
<tr>
<td>$d$</td>
<td>0.750</td>
<td>2.821</td>
<td>0.20172</td>
</tr>
<tr>
<td>$h = \cos(\theta_0)$</td>
<td>0.3013</td>
<td>0.518</td>
<td>0.045238</td>
</tr>
<tr>
<td>$\mu$ (Å$^{-1}$)</td>
<td>1.846</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td>$R_{\text{cut}}$ (Å)</td>
<td>2.87</td>
<td>2.9</td>
<td>2.2</td>
</tr>
<tr>
<td>$D_{\text{cut}}$ (Å)</td>
<td>0.15</td>
<td>0.2</td>
<td>0.2</td>
</tr>
<tr>
<td>$r_f$ (Å)</td>
<td>1.2</td>
<td>0.6</td>
<td>0.5</td>
</tr>
<tr>
<td>$b_f$ (Å$^{-1}$)</td>
<td>12.0</td>
<td>12.0</td>
<td>12.0</td>
</tr>
</tbody>
</table>

## References

[1] J.W. Mayer, S.S. Lau, Electronic Materials Science For Integrated Circuits in Si and GaAs, MacMillan, New York, 1990.

[2] See for example http://www.nichia.co.jp/.

[3] J.C. Zolper, R.J. Schul, MRS Bull. 22 (1997) 36.

[4] S.O. Kucheyev, J.S. Williams, C. Jagadish, J. Zou, G. Li, A.I. Titov, Phys. Rev. B 64 (2001) 035202.

[5] T. Diaz de la Rubia, G.H. Gilmer, Phys. Rev. Lett. 74 (1995) 2507.

[6] M.-J. Caturla, L.A.M.T. Diaz de la Rubia, G.H. Gilmer, Phys. Rev. B 54 (1996) 16683.

[7] K. Nordlund, M. Ghaly, R.S. Averback, M. Caturla, T. Diaz de la Rubia, J. Tarus, Phys. Rev. B 57 (1998) 7556.

[8] J. Nord, K. Nordlund, J. Keinonen, Phys. Rev. B 65 (2002) 165329.

[9] J. Tersoff, Phys. Rev. B 39 (1989) 5566;
J. Tersoff, Phys. Rev. B 41 (1990) 3248.

[10] D.W. Brenner, Phys. Rev. B 42 (1990) 9458;
D.W. Brenner, Phys. Rev. B 46 (1992) 1948.

[11] D.W. Brenner, O.A. Shenderova, J.A. Harrison, S.J. Stuart, S.B. Sinnott, J. Phys.: Condens. Matter 14 (2002) 783.

[12] K. Albe, K. Nordlund, R.S. Averback, Phys. Rev. B 65 (2002) 195124.

[13] K. Albe, K. Nordlund, J. Nord, A. Kuronen, Phys. Rev. B 66 (2002) 035205.

[14] J.F. Ziegler, J.P. Biersack, U. Littmark, The Stopping and Range of Ions in Matter, Pergamon Press, New York, 1985.

[15] K. Nordlund, A. Kuronen, Nucl. Instr. and Meth. B 159 (1999) 183.

[16] K. Nordlund, J. Nord, J. Frantz, J. Keinonen, Comput. Mater. Sci. 18 (2000) 283.

[17] K. Albe, Phys. Rev. B 55 (1997) 6203.

[18] C. Mailhiot, L.H. Yang, A.K. McMahan, Phys. Rev. B 46 (1992) 14419.

[19] M.I. Eremets, R.J. Hemley, H. Mao, E. Gregoryanz, Nature 411 (2001) 173.

[20] H.J.C. Berendsen, J.P.M. Postma, W.F. van Gunsteren, A. DiNola, J.R. Haak, J. Chem. Phys. 81 (1984) 3684.

[21] K. Nordlund, J. Peltola, J. Nord, J. Keinonen, R.S. Averback, J. Appl. Phys. 90 (2001) 1710.

[22] A. Turos, A. Stonert, B. Breeger, E. Wendler, W. Wesch, R. Fromknecht, Nucl. Instr. and Meth. 148 (1999) 401.

[23] M.W. Bench, I.M. Robertson, M.A. Kirk, I. Jenčič, J. Appl. Phys. 87 (2000) 49.

[24] R.S. Averback, T. Diaz de la Rubia, in: H. Ehrenfest, F. Spaepen (Eds.), Solid State Physics, Vol. 51, Academic Press, New York, 1998, p. 281.

[25] J.R. Dennis, E.B. Hale, J. Appl. Phys. 49 (1978) 1119.

[26] K. Nordlund, R.S. Averback, Phys. Rev. B 56 (1997) 2421.

[27] H. Zillgen, P. Ehrhart, Nucl. Instr. and Meth. B 127–128 (1996) 27.

[28] H. Hausmann, A. Pillukat, P. Ehrhart, Phys. Rev. B 54 (1996) 8527.

[29] P. Partyka, Y. Zhong, K. Nordlund, R.S. Averback, I.K. Robinson, P. Ehrhart, Phys. Rev. B 64 (2002) 235207.

[30] J. Nord, K. Albe, K. Nordlund, to be published.