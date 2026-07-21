![](./images/812767335575191552_1.jpg)

Surface and Coatings Technology 128-129 (2000) 175-180

![](./images/812767335575191552_2.jpg)
www.elsevier.nl/locate/surfcoat

# The role of energetic atoms in the deposition of Au/Au (001) thin films — a computer simulation study

Q.Y. Zhang$^{a,*}$, T.C. Ma$^{a}$, Z.Y. Pan$^{b}$, J.Y. Tang$^{b}$

$^{a}$State Key Laboratory for Materials Modification by Laser, Ion and Electron Beams, Dalian University of Technology, Dalian 116024, PR China
$^{b}$Accelerator-based Atomic and Nuclear Physics Laboratory, Institute of Modern Physics, Fudan University, Shanghai 200433, PR China

## Abstract
The behavior of Au/Au (100) thin film growth with energetic deposition has been investigated by kinetic Monte Carlo simulations with the description of the deposition process of energetic atoms based on molecular dynamics simulation results. We present the simulation results on the morphology, islands distribution, Bragg intensity and roughness of homoepitaxial Au (100)-films growth with energetic deposition at various substrate temperatures. We found the energetic atoms can promote the nucleation and island growth in the early stages of film growth and thus enhance the smoothness of the film surface at the temperatures of film growth in three-dimensional mode and in quasi-two-dimensional mode. The atomistic mechanism that promotes the nucleation and island growth and enhances the smoothness of the film surface is discussed. © 2000 Elsevier Science S.A. All rights reserved.

Keywords: Film growth; Atomistic mechanism; Computer simulation; Gold

---

## 1. Introduction
Thin films are required in many applications, such as in microelectronics, optics, optoelectronics, magnetic materials, etc. To obtain thin films with high quality, a method very often used is to increase the energy of deposition atoms (or ions), such as the negative bias techniques applied in chemical vapor deposition (CVD) and physical vapor deposition (PVD). In the past few years several methods based on energetic atom deposition, e.g. ion beam assisted deposition (IBAD), laser ablation, accelerated molecular beam epitaxial growth and energy-filtered ion beam deposition, etc., have been developed and have become important techniques in the film preparation. Therefore, the atomistic mechanism of energetic deposition has attracted more and more attention both experimentally and theoretically [1–7]. Esch et al. have studied the nucleation and morphology of homoepitaxial Pt (111)-films growth with IBAD by scanning tunneling microscopy and low energy electron diffraction [1]. They found that IBAD increases the island number density and the smoothness of the film in comparison with conventional vapor phase deposition. Kellerman et al. have used kinetic Monte Carlo (MC) simulation to show that a transient ion-induced defect model can explain the experimental observation of surface smoothing in IBAD [2,3]. Gilmore and Sprague have carried out molecular dynamic (MD) simulations of the energetic atom deposition of Ag/Ag (001) film [4,5]. They found that the thin film growth mode can be changed from three-dimensional island growth to layer-by-layer growth by increasing the energy of incident atoms from 0.1 eV to 10.0 eV.

Generally, the film growth consists of two major processes, the deposition process of incident atom and the diffusion process of adatom. These two processes

---
*Corresponding author. Department of Physics, Dalian University of Technology, Dalian 116024, PR China. Tel.: +86-411-4708389; fax: +86-411-4708389.
E-mail address: qyzhang@dlut.edu.cn (Q.Y. Zhang).

0257-8972/00/$ - see front matter © 2000 Elsevier Science S.A. All rights reserved.
PII: S0257-8972(00)00629-0

are very different. In the deposition process, the incident atoms impinge on the film surface and induce the transient movement of deposited atoms, the displacement of adatoms, the recombination of vacancies with adatoms and deposited atoms, and the production of new defects. All events in the deposition process occur in a few picoseconds. In other words, the deposition process is a transient dynamic process and cannot be simulated by the kinetic MC method. The diffusion process, however, generally occurs in nanoseconds to seconds depending on the temperature and deposition rate. In the diffusion process, some events are very important to the film growth, such as the motion of adatoms in large scale, the nucleation of adatoms, the growth of islands, and the recombination of adatoms with vacancies. It is impossible to consider the diffusion process with enough simulation time in the MD simulation. Therefore, a reasonable physical model is to consider both the deposition process and diffusion process in the computer simulation of film growth. In kinetic MC simulations of the film growth with conventional vapor phase deposition, the deposition process is generally described by the downward funneling model due to the low incident energy of deposition atom [8,9]. In the film growth with energetic deposition, however, the downward funneling model is no longer suitable because the morphology of film growth is seriously changed and many new defects are produced. In this study, based on the MD simulation results of deposition process of energetic atoms, a method has been devised to describe the change of local morphology in deposition process and then applied to the investigation of the film growth with energetic deposition by kinetic MC simulation. We present the simulation results on the morphology, Bragg intensity and roughness of homoepitaxial Au (100)-films growth with energetic deposition at various substrate temperatures. The role of energetic atoms in the film growth and the atomistic mechanism of film growth with energetic deposition are discussed.

## 2. Physical model and simulation method

### 2.1. Description of deposition process

To study the influence of energetic atoms on the film morphology, the interaction of energetic atoms with various cluster configuration on substrates is carried out by MD simulations. The basic principle and method of MD simulation have been described in detail elsewhere [10,11]. The initial energy of the incident atom is 10 eV and every event of energetic deposition is simulated for 100 runs by changing the incident point in a crystal cell. Statistical results show that the push-out probability of an adatom in clusters is relative to the nearest neighbor coordination number in plane and the distance to the incident point. The push-out probability of an adatom in a cluster can be written as

$$
P_{\text {push }}=1-P_{\mathrm{D}} n_{\mathrm{b}} \rho / a_{u} \tag{1}
$$

where $P_{\mathrm{D}}=0.2$ for 10.0 eV atom, $n_{\mathrm{b}}$ is the coordination number of an atom in plane, $\rho$ is the distance of the atom to the incident point and $\rho=a_{u}$ if $\rho<a_{u}$, $a_{u}=0.5\ a_{0}$, $a_{0}$ is the lattice constant. The push-out probabilities calculated by Eq. (1) are very close to the statistical results of MD simulation with an error less than 15.0%. The new adatoms produced by incident atom are redistributed nearby a circle with radius of $R_{\mathrm{D}}=2.83\ a_{u}$ around the incident point. According to the above results, the deposition process can be represented by placing an adatom at a random site on film surface and by the production of new adatoms and vacancies with a certain distribution around the incident point, where the production of defects is determined by Eq. (1).

### 2.2. Simulation of diffusion process

For the simulation of diffusion process of adatoms we used the kinetic MC method proposed by Voter [12]. In the simulation, the substrate is an fcc lattice of typical size $160×160×4$, on which energetic atoms are deposited onto random sites at a deposition rate of 0.05 monolayer per second (ML/s). A periodic boundary condition is applied in the kinetic MC simulations. The hopping rate of an adatom for a specific move is determined by [12]

$$
h=v \exp \left(-E_{\mathrm{B}} / k T\right) \tag{2}
$$

where $v=0.5×10^{12}$ Hz is the attempt frequency, $E_{\mathrm{B}}$ is the height of the energy barrier that the adatom needs to cross for that specific move, $k$ is Boltzmann's constant, and $T$ is the temperature. The diffusion barrier of an adatom for a specific move is determined by the local environment of the adatom; the model proposed by Breeman et al. [13]. The local environments of an adatom for hopping from an initial site to a vacant nearest-neighbor site in plane diffusion and for jumping off step edges in interlayer diffusion are shown in Fig. 1. Au-Au interaction potential with an embedded-atom method [14] is used to calculate diffusion barriers by using a three-dimensional Newton-Raphson search for the stationary points [15].

## 3. Nucleation and morphology of film growth in early stages

Fig. 2 contains the perspective-view images of simu-

![](./images/812767335575191552_3.jpg)

Fig. 1. The local environment for an adatom (a) hopping in plane, (b) jumping off an edge at a kink site, (c) jumping off a straight edge.

lated surfaces at various temperatures. The images represent the surfaces of film growth after 0.2 ML energetic atoms have been deposited on substrates. We can see that the morphology of film growth is domi- nated by the substrate temperature. At the tempera- ture of 100 K, the main morphological entities on the surface are monomers, dimers, trimers, small clusters and monomer strings. The morphology of film growth at low temperatures results from the low mobility of adatoms. The mobility of an adatom can be quantita- tively described by the hopping rate of the adatom in a certain time. We calculated the hopping rate of ad- atoms with some typical local environments as a func- tion of temperature in the time of deposition interval.

Calculation results indicate that the hopping rate of adatom with any local environment is much less than 1.0 when the temperatures are below 200 K. This means the nucleation and island growth at low temper- atures mainly depend on the increase of the adatom number density and the transient move of energetic atom on the substrate. With the increase of substrate temperature, monomers and dimers considerably de- crease and islands obviously grow up. At the tempera- ture of 300 K, monomer strings are the major morpho- logical entities on the surface. At temperatures above 400 K, however, the morphological entities are mainly islands. The shape of islands on the surface at 450 K is more regular than that at 400 K. This phenomenon can be attributed to the increase of diffusion capability of the adatom. Adatom diffusion dominates the nucle- ation, island growth and the change of island shape. The calculation results of hopping rates show that dimer and monomer strings are no longer stable and the interlayer diffusion of adatoms can occur with high probability at the temperatures higher than 400 K. Those are the main reasons causing the morphology change with the increase of temperature.

![](./images/812767335575191552_4.jpg)

Fig. 2. The perspective-view images of simulated film surfaces (gray color represents the surface layer of the substrate, the lighter shade represents vacancies on the substrate surface, and the darker shade represents the higher layer) taken at various temperatures after deposition of 0.2 ML energetic atoms.

In comparison to the simulated surfaces of conventional vapor phase deposition [16], we found that the influence of energetic atom on the morphology of film growth is greater at low temperature than that at high temperature. In Fig. 2, we can see that vacancies (white spots) produced by the energetic atom on the substrate can be observed at low temperatures, but few vacancies can be seen on the substrate at high temperatures. For different temperatures, the difference of the influence of energetic atom on the surface morphology can be explained by the change of diffusion capability of adatoms. At low temperatures, the mobility of adatoms is limited so that they have not enough opportunity to recombine with vacancies. With the increase of temperature, adatoms can move in large scale and the probability of adatoms recombining with vacancies increases. The recombination of adatoms with vacancies erases the influence of energetic atom on the morphology of film growth.

For further investigation of the influence of energetic atom on the nucleation and island growth in the early stages, the coverage of island vs. the island size is shown in Fig. 3. In comparison to the simulated results of conventional vapor phase deposition, we found that the number of monomers in the film growth with energetic deposition is decreased by $3.5\%$ and the number of stable islands is increased at the temperature of 100 K. The change of morphological entities can be attributed to the increase of adatom number in the energetic deposition. The additional adatoms in the energetic deposition come from the production of vacancies on the substrate due to the energetic atom impact. This phenomenon implies that the defects produced by the energetic atom promotes the nucleation and island growth in the early stages of film growth. At high temperature, however, adatom diffusion dominates the nucleation and island growth and the influence of energetic atom on the morphology of film growth is not important anymore. In other words, the influence of energetic atom localizes in a small range around incident point. By changing the local morphology of film growth, energetic atoms increase the adatom number and promote the nucleation and island growth.

## 4. Growth mode and atomistic mechanism

The Bragg intensity calculated with a kinematic approach and roughness of film surface vs. deposited coverage at various temperatures are shown in Fig. 4. In the figures we can see that the Bragg intensity oscillates in the form of similar amplitude at the temperatures higher than 410 K. This implies the film growth proceeds in the form of an almost perfect layer-by-layer mode at these temperatures. For temperatures of 400 K to 300 K, Bragg intensity considerably decreases in the form of damping oscillations with the increase of coverage. In these cases, film growth is a typical three-dimensional island growth mode. At temperatures below 250 K, the damping of the oscillations decreases and the amplitudes of Bragg intensity oscillations increase. When the temperature decreases down to 100 K, the Bragg intensity oscillates in the form of almost the same amplitude again although the amplitude of Bragg intensity oscillations is much lower than

![](./images/812767335575191552_5.jpg)

Fig. 3. The coverage of island vs. the island size taken at various temperatures after deposition of 0.2 ML energetic atoms.

![](./images/812767335575191552_6.jpg)

Fig. 4. The roughness (a) and Bragg intensity (b) of film surface vs. coverage taken at various temperatures after deposition of 5.0 ML energetic atoms.

that at high temperatures. A similar phenomenon of film growth was first discovered by Kunkel et al. in the experiment of homoepitaxial Pt (111)-films growth and was named as 're-entrant layer-by-layer growth' or quasi-two-dimensional layer-by-layer growth [17]. The behavior of film growth with energetic deposition is similar to the simulation result with conventional vapor phase deposition. In other words, the film growth mode is mainly dominated by the temperature of film growth.

Although the behavior of Bragg intensity oscillation at low temperatures is similar to that at high temperatures, the nature of film growth for the two cases is very different. From the change of roughness of film surface at various temperatures as shown in Fig. 4, we can see that the roughness of film growth changes in the form of oscillation with the increase of coverage at high temperatures. This oscillation of roughness is a feature of real layer-by-layer growth. At low temperatures, however, the change of roughness is the linear increase with the increase of coverage after 0.5 ML atoms are deposited. With regard to roughness, the film growth at low temperatures is the same as three-dimensional island growth. The enhancement of Bragg intensity oscillation is the downward funneling effect caused by numerous small islands. At low temperatures, islands grow up very slowly because of the low mobility of adatoms. The morphological entities of film growth are monomers and small islands. These small islands induce the efficient interlayer mass transport.

This also means that the morphology of film growth is rough on an atomic scale at low temperatures.

To reveal the role of energetic atom in the film growth, we compared the simulated results with those obtained in the simulation of conventional vapor phase deposition with the downward funneling model [16]. At the temperatures of 100 K to 200 K, the Bragg intensity of film growth with energetic deposition increases by approximately 40%. For temperatures of 250 K to 400 K, the increase of Bragg intensity is approximately 20%. At the temperatures higher than 410 K, the increase of Bragg intensity sharply drops down to 0 when increasing the temperature up to 450 K. In comparison with conventional vapor phase deposition, the roughness of film growth with energetic deposition decreases approximately 15% in the temperature range 100-400 K. For temperatures above 410 K, the roughness of energetic deposition is almost the same as that of conventional vapor phase deposition. These results imply that the role of energetic atoms in film growth is to enhance the smoothness of morphology at temperatures below 400 K. At temperatures higher than 410 K, the influence of energetic atoms can not dominate the behavior of film growth due to the increase of diffusion capability of adatoms.

The evolution of the roughness ratio of energetic deposition to conventional vapor phase deposition with the increase of coverage at various temperatures is shown in Fig. 5. We can clearly see that the roughness

![](./images/812767335575191552_7.jpg)

Fig. 5. The evolution of roughness ratio of energetic deposition to conventional vapor phase deposition with the increase of coverage at various temperatures, where $R_0$ is the roughness of the conventional vapor phase deposition and $R_1$ is the roughness of energetic deposition.

of film growth with energetic deposition is increased in the early stages of film growth (the coverage below 0.5 MLs) at low temperatures. The increase of roughness can be interpreted by the sputtering effect of energetic atoms on substrates. The impact of energetic atoms with substrate increases the defects on substrate. However, the increase of adatom number density induced by sputtering effect promotes the nucleation of film growth in the early stages. After the energetic atoms are deposited to more than 1 ML, the roughness of film growth is much lower than that in conventional vapor phase deposition at temperatures of 100-400 K. The decrease of roughness can be attributed to the contribution of sputtering effect of energetic atoms and the results of transient mobility of deposited atoms. On the one hand, the energetic atoms suppress growth of three-dimensional islands by a sputtering effect, on the another hand, the transient mobility of energetic atom induces the efficient interlayer mass transport.

## 5. Conclusions

(1) In the early stages of film growth, the morphology of film growth with energetic deposition is mainly dominated by the substrate temperature. The role of the energetic atom is to influence the local morphology of film growth. The influence of energetic atoms on the morphology of film growth is greater at low temperature than that at high temperature.

(2) Energetic atoms can promote the nucleation and island growth in the early stages at low temperatures. The promotion of the nucleation and island growth can be attributed to the increase of adatom number density and the low diffusion capability of adatom.

(3) The mode of film growth with energetic deposition is mainly dominated by the temperature. The morphology of film growth with energetic deposition is smoother than that with conventional vapor phase deposition at temperatures of 100-400 K. The role of energetic atom in the film growth is to suppress the growth of three-dimensional islands and to increase the interlayer mass transport.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China under grant no. 19835030.

## References

[1] S. Esch, M. Breeman, M. Morgenstern, T. Michely, G. Comsa, Surface Sci. 365 (1995) 187.
[2] B.K. Kellerman, E. Chason, J.A. Floro, S.T. Picraux, J.M. White, Appl. Phys. Lett. 67 (1995) 1703.
[3] E. Chason, B.K. Kellerman, Nucl. Instrum. Methods 127/128 (1997) 225.
[4] C.M. Gilmore, J.A. Sprague, Phys. Rev. B 44 (1991) 8950.
[5] J.A. Sprague, C.M. Gilmore, Thin Solid Films 272 (1996) 244.
[6] A. Robbemond, B.J. Thijsse, Nucl. Instrum. Methods 127/128 (1997) 273.
[7] M. Villarba, H. Jónsson, Surface Sci. 324 (1995) 35.
[8] J.W. Evans, D.E. Sanders, P.A. Thiel, A.E. Depristo, Phys. Rev. B 41 (1990) 5410.
[9] J. Jacobsen, K.W. Jacobsen, P. Stoltze, J.K. Nørskov, Phys. Rev. Lett. 74 (1995) 2295.
[10] Q.Y. Zhang, Z.Y. Pan, J.Y. Tang, Acta Phys. Sinica 8 (1999) 296.
[11] Q.Y. Zhang, J.Y. Tang, G.Q. Zhao, Nucl. Instrum. Methods B 135 (1998) 289.
[12] A.F. Voter, Phys. Rev. B 34 (1986) 6819.
[13] M. Breeman, G.T. Barkema, M.H. Langelaar, D.O. Berma, Thin Solid Films 272 (1996) 195.
[14] S.M. Foiles, M.I. Baskes, M.S. Daw, Phys. Rev. B 33 (1986) 7983.
[15] C.L. Liu, J.M. Cohen, J.B. Adams, A.F. Voter, Surface Sci. 253 (1991) 334.
[16] Q.Y. Zhang, T.C. Ma, Z.Y. Pan, J.Y. Tang, Acta Phys. Sinica, in press.
[17] R. Kunkel, B. Poelsema, L.K. Verheij, F. Comsa, Phys. Rev. Lett. 65 (1990) 733.