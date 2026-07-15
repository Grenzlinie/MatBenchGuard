# Controlling Polymorphism during the Crystallization of an Atomic Fluid

Caroline Desgranges and Jerome Delhommelle

Department of Chemical Engineering, University of South Carolina, 301 Main Street South, Columbia, South Carolina 29208, USA
(Received 13 January 2007; published 7 June 2007)

We use molecular dynamics simulations to shed light on polymorphism selection during the crystallization of the Lennard-Jones fluid. By varying pressure at fixed supercooling, we form large crystallites either of the stable face centered cubic form or of the metastable body centered cubic form and even fine-tune the fractions of stable and metastable polymorphs in the crystallite. We demonstrate that the conditions of crystallization, leading to large bcc crystallites, lie within the occurrence domain of the metastable bcc polymorph. We also find that the predominantly fcc crystallites contain a notable amount of the hexagonal close packed form, due to the cross nucleation of the hcp form on the fcc form. By varying temperature at fixed pressure, we prevent cross nucleation and form pure fcc crystallites. Our results reveal that polymorph selection may take place, and be controlled, during the growth step.

DOI: 10.1103/PhysRevLett.98.235502
PACS numbers: 81.10.Aj, 07.05.Tp, 61.50.Ah

Controlling the structure (or polymorph) in which a molecule crystallizes is a long-standing issue [1,2]. Since polymorphs have different physical properties, it is crucial for many applications (e.g., in the making of pharmaceuticals [1] and of materials exhibiting piezoelectricity or nonlinear optical properties [3]) to control which polymorphs form during crystallization. Understanding polymorphism requires determining when and how polymorph selection takes place during the crystallization process. This is particularly challenging, and remains an unsolved problem even for a simple liquid, since polymorph selection is a complex phenomenon resulting from the interplay between thermodynamics and kinetics [4].

In this Letter, we use molecular dynamics (MD) simulations and vary the conditions of crystallization to shed light on polymorph selection during the crystallization of Lennard-Jones (LJ) particles. The phase diagram for the LJ system is well known [5,6]. The stable form for the LJ crystal is the face centered cubic structure. There are also two metastable forms: the hexagonal close packed form, whose free energy is almost equal to that of the fcc form, and the body centered cubic form of higher free energy.

The intricacy of polymorph selection was first prefigured by Ostwald in his "step rule" which states that the phase that nucleates is not necessarily the thermodynamically stable phase [7]. Several approaches were applied to investigate the crystallization of simple liquids and to account for this observation. First, on the basis of Landau theory, it was suggested that bcc crystallites easily form from the supercooled liquid and then undergo a transformation into the stable form [8,9]. This picture was later confirmed by simulations on supercooled liquids of LJ particles [10] and hard spheres [11]. Both simulations showed that nucleation first proceeded through the formation of small bcc clusters. As they grew, the clusters transformed into critical nuclei whose structure was predominantly that of the thermodynamically stable phase. For the LJ system [10], the structure of the critical nuclei was predominantly that of the fcc phase, with a surface layer of bcc particles as predicted by density functional theory [12]. For the hard sphere system [11], the critical nuclei were a random mixture of the stable fcc and of the hcp forms (the free energy difference between the fcc and hcp structures is extremely small [13]). This structure was also identified by microscope imaging during the crystallization of concentrated colloidal suspensions [14]. These results seem to indicate that, in simple liquids, polymorph selection takes place during the nucleation event. However, recent simulation studies on the LJ system reveal a different picture. Moroni et al. found that the critical nucleus may be either small and predominantly of the stable fcc form or large and predominantly of the metastable bcc structure [15]. In previous work [16], we studied the growth of the predominantly fcc critical nuclei. We found that it proceeded through the cross nucleation (or heterogeneous nucleation) of clusters of the metastable hcp form on the structurally compatible (111) planes of the fcc structure. Cross nucleation between polymorphs was also observed experimentally in molecular liquids [17,18]. Both results show that for simple liquids, polymorph selection may take place during the growth step and not necessarily during the nucleation step as previously thought.

In this work, we simulate the entire crystallization process, i.e., both the nucleation and the growth steps. We show how, by modifying the conditions of crystallization, we succeed in controlling polymorphism. By varying pressure at fixed supercooling, we form large crystallites either of the stable fcc form or of the metastable bcc form and even fine-tune the fractions of stable and metastable polymorphs in the crystallite. This is a new observation since no large postcritical bcc crystallite of LJ particles was ever obtained in previous work. We rationalize our results by demonstrating that the conditions of crystallization, leading to large bcc crystallites, lie within the occurrence domain of the metastable bcc polymorph (i.e., the domain where the chemical potential of the metastable form is less than that of the liquid). In agreement with previous work [16], we find that the predominantly fcc crystallites contain

a notable amount of the hcp form, due to the cross nucleation of the hcp form on the fcc form. By varying temperature at fixed pressure, we prevent cross nucleation and succeed in forming pure fcc crystallites. Our results show that polymorph selection may take place, and be controlled, during the growth step.

We first study the crystallization of a LJ liquid cooled at fixed supercooling, i.e., at a temperature 25% below the melting point. We carry out simulations of crystal nucleation and growth at fixed pressure $P = 10, 15, 20, 25$, and 50 in reduced units [19]. We use two different types of MD simulations, corresponding to the two mechanistic steps of nucleation and growth. We first induce the formation of a critical nucleus. For a supercooling of 25%, nucleation is an activated process, which can be studied by using a non-Boltzmann sampling scheme in our simulations [10,20]. We therefore perform MD simulations together with an umbrella sampling bias potential on systems of 4000 particles. The bias potential allows the system to overcome the free energy barrier of nucleation. The bias potential is a harmonic function of the global order parameter $Q_6$ [21].

The bias potential does not favor the formation of a specific polymorph since $Q_6$ takes similar values for the fcc, hcp, and bcc polymorphs. By gradually increasing the imposed value for $Q_6$, we are able to grow a crystal nucleus. Using local bond order parameters [16,22], we analyze the structure of the nucleus. As expected from previous studies [8-11,16], our simulations show that nucleation proceeds into the bcc phase. Kinetics dominates the entire nucleation step. Regardless of the value of pressure, the critical nuclei are all predominantly bcc. Once we have formed a critical nucleus, we can simulate the growth step. We proceed as in previous work [16]. The system of 4000 particles, containing a critical nucleus, is embedded in a larger system of liquid to form a system containing 32 000 particles. We then equilibrate the new system of 32 000 particles while still applying the bias potential on the central subsystem of 4000 particles for 10 time units. After the equilibration run, we switch off the bias potential and monitor the free evolution of the crystal nucleus. We repeat this last operation 10 times and check that we have formed a genuine critical nucleus, i.e., that the nucleus grows for half of the MD trajectories and dissolves into the liquid for the other MD trajectories.

Throughout the growth of the nuclei, we monitor the evolution of its size and of the number of fcc, bcc, and hcp particles composing the nuclei [16]. We present in Fig. 1 the averages for the number of fcc and bcc particles, calculated over all the MD trajectories (leading either to the growth or to the dissolution of the critical nuclei), obtained for the 5 conditions of crystallization against the number of particles contained in the crystallites. Our results clearly demonstrate that we succeed in controlling polymorphism. At low pressure $(P = 10)$, we form crystallites predominantly of the stable fcc form and containing the fewest bcc particles. At the end of the MD trajectories, the core of the nucleus is composed of fcc particles (55% of the cluster) and of hcp particles (25%). bcc particles, which only account for 20% of the total, are almost exclusively located on the liquid-solid interface and quickly convert into fcc and hcp particles as the crystallite grows. In agreement with previous simulations [16], we find that the relatively high fraction of hcp particles (25%) results from the cross nucleation of hcp clusters on the (111) fcc planes. As we increase pressure, Fig. 1 shows that the fraction of fcc particles in the crystallite gradually decreases while, in turn, the fraction of bcc particles gradually increases (the rate of cross nucleation of hcp particles is not affected by the change in pressure). Finally, at high pressure $(P = 50)$, we obtain an essentially pure bcc crystallite: 85% of the particles are bcc and there are virtually no fcc particles in the crystallite. In that case, nucleation and growth both proceed through the metastable bcc form. We also present in Fig. 2 snapshots of the crystallites obtained at the beginning (i.e., for a critical nucleus) and at the end of a MD trajectory for $P = 10$ and $P = 50$. The snapshots show that the critical nuclei are very similar for both pressures. A fivefold increase in pressure has little effect on the structure of the critical nucleus, which is in both cases almost exclusively of the metastable bcc form. This confirms that nucleation is governed by kinetics and that a dramatic change in the thermodynamic conditions of crystallization has little effect on the structure of the critical nucleus. However, the snapshots of the configurations of the system obtained at the end of the MD trajectories show that the conditions of crystallization have a significant effect on polymorph selection, even at a very early

![](./images/811987672905023488_1.jpg)

FIG. 1 (color online). Evolution of (a) the number of fcc particles and (b) the number of bcc particles with the total number of particles in the crystallite for the different pressures of crystallization at fixed supercooling.

stage during the growth process. This suggests that it is possible to control polymorphism and to manipulate the growth mechanism of crystallites of a few thousand parti- cles by simply changing the thermodynamic conditions of crystallization.

We rationalize our findings by determining the occur- rence domain of the bcc form (i.e., the domain where the chemical potential of the metastable form is smaller than that of the liquid). Using thermodynamic integration [23], we determine the melting lines for the fcc and the bcc forms and plot the results in Fig. 3 (our results for the fcc melting line are in excellent agreement with previous work [5,6]). We also report in Fig. 3 the conditions of crystal- lization used in this work. We interpret this diagram as follows. As shown in Fig. 2, nucleation begins with the formation of a critical nucleus of the kinetically favored metastable bcc form. Let us first consider the case $P=10$. These conditions of crystallization lie outside the occur- rence domain of the metastable bcc form. Hence, a large crystallite composed entirely of bcc particles will be less stable not only than a fcc crystallite but also than the liquid. Therefore, during the growth of the crystallite, the structure gradually evolves from a predominantly bcc structure to- wards a predominantly fcc structure as shown in Fig. 1. As pressure increases, we get closer and closer to the occur- rence domain of bcc and the ratio of the fraction of bcc particles to the fraction of fcc particles increases. Eventually, when the conditions of crystallization are chosen to lie within the occurrence domain of the meta- stable bcc form, large bcc crystallites are able to grow since bcc is more stable than the surrounding liquid. This is exactly what we observe for $P=50$ for which we obtain a crystallite almost entirely composed of particles of the metastable bcc polymorph.

The large fcc crystallites we obtain always contain a significant amount of hcp particles. In previous work [16], we attributed this result to the cross nucleation of layers of the hcp form on the structurally compatible (111) planes of the fcc form. In the first part of this Letter, we showed that varying pressure at fixed supercooling had no noticeable effect on the rate of cross nucleation. Therefore, we vary the temperature of crystallization at fixed pressure and study the effect of the degree of supercooling on cross nucleation.

We then simulate the nucleation and growth process at $P=5.68$ and at temperatures $22\%$, $15\%$, and $10\%$ below the melting temperature $(T_m=1.1$ [6]). We find that nu- cleation first proceeds with the formation of small bcc clusters and that the average structure of the critical nu- cleus is dominated by the fcc form for all supercoolings. This finding is in agreement with the results from previous works [10,16]. It is also consistent with the results de- scribed in this Letter for higher pressures since we showed that a decrease in pressure leads to an increase in the fraction of the fcc in the crystallite at the expense of bcc.

We now examine the results obtained for the growth step. We present in Fig. 4 the averages for the number of hcp particles, calculated over all the MD trajectories, ob- tained for the highest and lowest degrees of supercooling, i.e., $22\%$ and $10\%$, against the number of particles con- tained in the crystallites. Our results demonstrate that we succeed in controlling cross nucleation. Figure 4 clearly shows that, by increasing the temperature, we manage to reduce by a factor of 2 the increase in the number of hcp particles with the size of the nucleus, which suggests that cross nucleation has been prevented for a supercooling of $10\%$. This is confirmed by the snapshots presented in Fig. 5. For the highest supercooling $(22\%)$, we observe the formation of layers of hcp particles and thus of large

![](./images/811987672905023488_2.jpg)

FIG. 2 (color). Outside view of (a) the critical nucleus at $P=10$ (i.e., at the beginning of one of the MD trajectories), (b) the crystallite obtained at the end of one of the MD trajectories at $P=10$, (c) the critical nucleus at $P=50$, and (d) the crystallite obtained at the end of one of the MD trajectories at $P=50$ (gray: fcc; yellow: hcp; and red: bcc).

![](./images/811987672905023488_3.jpg)

FIG. 3 (color online). Phase diagram and conditions of crys- tallization (filled circles) studied in this work for the Lennard- Jones system. The solid line corresponds the solid-liquid tran- sition (the stable solid form is the fcc form). The dotted line corresponds to the bcc-liquid transition and delimits the occur- rence domain for the bcc polymorph.

235502-3

![](./images/811987672905023488_4.jpg)

FIG. 4 (color online). $P=5.68$. Evolution of the number of hcp particles with the total number of particles in the cluster at supercoolings of $10\%$ and $22\%$.

hcp domains within the crystallite. This corresponds to the cross nucleation of the hcp form on the fcc form. For the lowest supercooling ($10\%$), we do not observe the formation of such large hcp domains. hcp particles form on the surface of the fcc core of the crystallite and their number increases with the surface of the nucleus. Therefore, at low supercooling, we do not observe any cross nucleation and obtain an essentially pure fcc crystallite. We interpret this result as follows. The cross nucleation of the hcp form on the fcc form is a kinetic phenomenon, which, like any other heterogeneous nucleation process [24], is associated with a free energy barrier of activation. As for homogeneous nucleation, increasing the temperature (or decreasing the supercooling) results in an increase in the height of the free energy barrier. This, in turn, prevents cross nucleation and allows us to form pure fcc crystallites at low supercooling.

In conclusion, we have used molecular dynamics simulations to simulate crystal nucleation and growth in supercooled liquids of LJ particles. We demonstrate that polymorphism selection may take place during the growth step. At fixed supercooling ($25\%$) and for pressures ranging from 10 to 50, we control the formation of crystallites of either the stable fcc form or of the metastable bcc form despite having strikingly similar (and almost entirely bcc) critical nuclei for all pressures. We are able to rationalize the polymorphism selection process in terms of the location of the state point chosen to carry out the crystallization with respect to the occurrence domain for the metastable form. These results show that we are able to exert a thermodynamic control of polymorphism during the growth step. Similarly, at fixed pressure (5.68), we prevent the cross nucleation of the hcp form on the fcc form by increasing the temperature of crystallization. In this case, we have managed to exert a kinetic control of polymorphism during the growth step. Our simulations demonstrate, on the example of the LJ system, that we can manipulate the mechanisms of crystal growth, e.g., fine-tune the fraction of particles of the stable form in the crystallite and even obtain a pure metastable crystallite. These results suggest that atomistic simulations could be a useful tool to understand and predict polymorphism selection in more complex systems.

![](./images/811987672905023488_5.jpg)

FIG. 5 (color). $P=5.68$. Cross section of clusters of 5000 particles for supercoolings of (a) $10\%$ and (b) $22\%$ (gray: fcc; yellow: hcp; and red: bcc).

[1] J. Bernstein, *Polymorphism in Molecular Crystals* (Oxford University Press, Oxford, 2002).

[2] J. Bernstein, R. J. Davey, and J.-O. Henck, Angew. Chem., Int. Ed. **38**, 3440 (1999).

[3] M. D. Hollingsworth, *Science* **295**, 2410 (2002).

[4] N. Blagden and R. J. Davey, *Crystal Growth and Design* **3**, 873 (2003).

[5] R. Agrawal and D. A. Kofke, *Mol. Phys.* **85**, 43 (1995).

[6] M. A. van der Hoef, *J. Chem. Phys.* **113**, 8142 (2000).

[7] W. Ostwald, *Z. Phys. Chem.* **22**, 289 (1897).

[8] S. Alexander and J. P. McTague, *Phys. Rev. Lett.* **41**, 702 (1978).

[9] W. Klein and F. Leyvraz, *Phys. Rev. Lett.* **57**, 2845 (1986).

[10] P. R. ten Wolde, M. J. Ruiz-Montero, and D. Frenkel, *Phys. Rev. Lett.* **75**, 2714 (1995).

[11] S. Auer and D. Frenkel, *Nature (London)* **409**, 1020 (2001).

[12] Y. C. Shen and D. W. Oxtoby, *Phys. Rev. Lett.* **77**, 3585 (1996).

[13] P. G. Bolhuis, D. Frenkel, S. C. Mau, and D. A. Huse, *Nature (London)* **388**, 235 (1997).

[14] U. Gasser, E. R. Weeks, A. Schofield, P. N. Pusey, and D. A. Weitz, *Science* **292**, 258 (2001).

[15] D. Moroni, P. R. ten Wolde, and P. G. Bolhuis, *Phys. Rev. Lett.* **94**, 235703 (2005).

[16] C. Desgranges and J. Delhommelle, *J. Am. Chem. Soc.* **128**, 10 368 (2006).

[17] L. Yu, *J. Am. Chem. Soc.* **125**, 6380 (2003).

[18] S. Chen, H. Xi, and L. Yu, *J. Am. Chem. Soc.* **127**, 17 439 (2005).

[19] M. P. Allen and D. J. Tildesley, *Computer Simulations of Molecular Liquids* (Oxford University Press, Oxford, 1987).

[20] F. Trudu, D. Donadio, and M. Parrinello, *Phys. Rev. Lett.* **97**, 105701 (2006).

[21] P. J. Steinhardt, D. R. Nelson, and M. Ronchetti, *Phys. Rev. B* **28**, 784 (1983).

[22] P. R. ten Wolde, M. J. Ruiz-Montero, and D. Frenkel, *J. Chem. Phys.* **104**, 9932 (1996).

[23] D. Frenkel and A. J. C. Ladd, *J. Chem. Phys.* **81**, 3188 (1984).

[24] A. Caciutto, S. Auer, and D. Frenkel, *Nature (London)* **428**, 404 (2004).

235502-4