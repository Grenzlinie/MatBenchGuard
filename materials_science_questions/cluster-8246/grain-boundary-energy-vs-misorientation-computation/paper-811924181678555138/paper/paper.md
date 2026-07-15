# THE ENERGY DEPENDENCE OF THE {111} AND {100} TILT GRAIN BOUNDARIES ON DISORIENTATION ANGLE IN Ni₃Al

D. V. Sinyaev,¹ G. M. Poletaev,² M. D. Starostenkov,² and A. I. Potekaev³
UDC 539.2

Dependence of the energy of {111} and {100} boundaries on tilt angle $\theta$ is investigated by the molecular dynamics method using intermetallic Ni₃Al as an example. It is shown that the energy (per single grain dislocation) of grain boundaries in the {111} planes is higher than that of the grains located in the {100} planes.

Despite the large number of works dealing with the problem [1–3], the study of the energy dependence of grain-boundaries (GBs) on their disorientation angle $\gamma = \gamma(\theta)$ is still a challenging issue [4].

This is primarily due to a vague concept of this characteristic as such. Furthermore, there are a variety of GB models, with the dislocation models being most frequently used to estimate GB energy versus disorientation angle $\theta$ [5]. For instance, the Read – Shockley model is useful in describing the low-angle boundary energy, while that by Van der Merve fails to satisfactorily interpret a number of energy dependences characteristic of special-type boundaries [6]. These approximations are, nevertheless, fairly consistent with the results of full-scale experiments.

One of the most acceptable approaches providing investigation of the dependence of GB energy on disorientation angle, $E = E(\theta)$, is that of computer simulation. This approach has been implemented in a quite extensive number of studies on tilt grain boundaries, predominantly of a special type [6].

The purpose of this work is to study the dependence of the {111} and {100} tilt grain boundaries on disorientation angle $\theta$.

The investigation was performed using a computer simulation approach, in particular, the method of molecular diagnostics [11, 12]. Since in this case the focus is primarily on the structure of grain boundaries, it is reasonable to describe the interatomic forces to a pair approximation using the Morse potential functions. In our case, the pair interaction was assumed to cover five coordination spheres of the neighborhood, with the potential parameters taken from [13].

A tilt boundary was constructed in the middle of the computational block by rotating its two parts by angle $\theta$. The block was then cut to rule out interstices and shape it to a parallelepiped. The atoms beyond the grain-boundary line in the region of another grain were removed. Strict boundary conditions were set at the computational block boundaries in the plane perpendicular to the GB, and periodic conditions were prescribed along the axis of tilt [14]. The number of atoms in the computation blocks was from $2 \cdot 10^5$ to $5 \cdot 10^5$. After constructing a certain type GB, we implemented a dynamic relaxation of the structure by heating the system within 50–150 K for 100 ps. The computational cell temperature was prescribed using the initial atom velocities in accordance with the Maxwell distribution. The total kinetic energy in this case corresponded to a certain temperature, and the cumulative momentum of the computation block was equal to zero.

Upon completion of the initial relaxation for the computation block at the prescribed angle $\theta$, we calculated a GB energy per unit area as

$$
E = \frac{U_1 - U_0}{S}.
$$

¹Siberian State Industrial University, ²Altai State Technical University, e-mail: genphys@mail.ru; ³V. D. Kuznetsov Siberian Physical Technical University, e-mail: kanc@spti.tsu.ru. Translated from Izvestiya Vysshikh Uchebnykh Zavedenii, Fizika, No. 11, pp. 33–35, November, 2007.

1064-8887/07/5011-1101 ©2007 Springer Science+Business Media, Inc.

![](./images/811924181678555138_1.jpg)

Fig. 1. Dependence of the GB energy $E$ (curve 1) and GB energy per single dislocation $E_{\mathrm{d}}$ (curve 2) on disorientation angle $\theta$: GB in $\{111\}$ $(a)$ and $\{100\}$ $(b)$ planes.

Here $U_{1}$ is the energy of a crystal with grain boundaries, $U_{0}$ is the energy of a perfect crystal containing the same number of atoms, and $S$ is the grain-boundary area.

For alloyed $\mathrm{Ni}_{3} \mathrm{Al}$, the dependence of a $\{111\}$ tilt GB on $\theta$ was found to be of the same character as that obtained for a 2D model [15]. The principal difference consisted in that in the vicinity of angles $\theta>16^{\circ}$ the GB energy did not fluctuate but continued to increase only slightly. It acquired a steady-state character only when approaching $\theta=30^{\circ}$. The point is that overlapping of the fields of elastic stresses caused by dislocations becomes significant at $\theta>16^{\circ}$. Note that the GB energy per one dislocation, $E_{\mathrm{d}}=E / N_{\mathrm{d}}(\theta)$ (Fig. $1 a$), in the low-angle part is quickly decreasing and then tends to a constant value [13] up to the maximum disorientation angle value.

Similar characteristics for GBs oriented in the $\{100\}$ planes are given in Fig. $1 b$. Comparing the dependences for the $\{111\}$ and $\{100\}$ grain boundaries, we would like to underline that the energy characteristics for GBs oriented in the former planes are found to be higher compared to the latter. In the case of pure metals [15], the dependences were found to be inverse. Apparently, the presence of anti-phase boundaries in the $\{111\}$ family of planes does affect the energy ratio of these types of boundaries in pure metals, $\mathrm{Ni}$ and $\mathrm{Al}$, and in intermetallic $\mathrm{Ni}_{3} \mathrm{Al}$ material [16].

It should be noted that the dependences $E=E(\theta)$ exhibit certain oscillations, which were not found in the case of pure metals [15]. This seems to depend on the presence of a large number of parameters that influence the GB energy in the case of an intermetallic material or an ordered alloy [16, 17]. In the latter situation, a certain number of point substitution defects appear in a random fashion, which result in disorder regions and APB interlayers. It is these factors that cause oscillations in the curves of specific GB energy dependence on disorientation angle.

REFERENCES

1. R. Z. Valiev, R. R. Mulukov, V. V. Ovchinnikov, et al., Metallofizika, 12, No. 5, 124-126 (1990).
2. T. Sakuma, Mater. Sci. Forum, 294-296, 59-66 (1999).
3. O. A. Kaibyshev, and R. Z. Valiev, Grain Boundaries and Properties of Metals [in Russian], Moscow, Metallurgiya (1987).
4. M. D. Starostenkov, in: Abst. III Eurasian Sci.-Pract. Conf. Strength of Inhomogeneous Structures, Moscow, MISiS (2006).
5. J. H. Van der Merve, Proc. of the Phys. Soc. A, 63, 616-637 (1950).
6. A. I. Potekaev, M. D. Starostenkov, V. N. Udodov, et al., Structure and Properties of Promising Metallic Materials (Ed. A. I. Potekaev) [in Russian], Tomsk, NTL (2007).
7. D. V. Heerman, Methods of a Coputer Experiment in Experimental Physics [in Russian], Moscow, Nauka (1990).
8. Yu. M. Plishkin, Crystal Defects and their Computer Simulation [in Russian], Leningrad, Nauka (1980).

9.  A. I. Potekaev, I. I. Naumov, V. V. Kulagina, *et al.*, Natural Long-period Nanostructures (Ed. A. I. Potekaev) [in Russian], Tomsk, NTL (2002).

10. A. I. Potekaev, T. A. Kovalevskaya, B. A. Grinberg, *et al.*, (Ed. A. I. Potekaev) [in Russian], Structure Evolution and Properties of Metallic Materials (Ed. A. I. Potekaev) [in Russian], Tomsk, NTL (2007).

11. V. V. Kulagina, S. V. Eremeev, and A. I. Potekaev, Rus. Phys. J., No. 2, 122–130 (2005).

12. S. V. Eremeev and A. I. Potekaev, Rus. Phys. J., No. 6, 646–656 (2005).

13. A. I. Tsaregorodtsev, N. V. Gorlov, B. F. Demyanov, and M. D. Starostenkov, Fiz. Met. Metalloved., **58**, No. 2, 336–343 (1984).

14. R. Yu. Rakitin, G. M. Poletaev, M. S. Aksenov, and M. D. Starostenkov, Fundamental Problems of Modern Materials Science [in Rusiian], No. 2, 124–129 (2005).

15. R. Yu. Rakitin, Investigation of mechanisms of Tilt Grain Boundary Diffusion in fcc –Metals, Thesis of Cand. Phys.-Math. Sci. Dissert., Barnaul (2006).

16. M. D. Starostenkov, G. V. Popova, G. M. Poletaev, and D. V. Sinyaev, Izv. VUZov. Chernaya Metallurgiya, No. 6, 24–27 (2006).

17. M. D. Starostenkov, R. Yu. Rakitin, and D. V. Sinyaev, Deformation and Fractur of Materials [in Russian], No. 11, 7–11 (2007).