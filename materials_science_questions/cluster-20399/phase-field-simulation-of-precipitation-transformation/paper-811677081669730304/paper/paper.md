# OXYGEN PRECIPITATION IN SILICON: NUMERICAL MODELS

J. P. LAVINE, G. A. HAWKINS, C. N. ANAGNOSTOPOULOS, AND L. RIVAUD
Research Laboratories, Eastman Kodak Company, Rochester, NY 14650

## ABSTRACT
We present a numerical model that simulates the evolution of precipitates and the diffusion of interstitial oxygen in Czochralski silicon. The growth and/or dissolution of each precipitate and the local concentration of interstitial oxygen with which the precipitates interact are followed as a function of time. We treat realistic densities of discrete, interacting precipitates and determine how the precipitate density influences the extent of the precipitation. The model also treats oxygen outdiffusion and the formation of precipitate-free or denuded zones. We apply the model to previous experimental data on the time dependence of precipitate growth and to the development of denuded zones during intrinsic gettering.

## INTRODUCTION
We have developed a numerical model that simulates interstitial oxygen diffusion and precipitation in Czochralski silicon. We use this model to study intrinsic gettering [1-3] and the formation of defect-free regions or denuded zones at the wafer surface. The motivation for the model is threefold: (1) to understand a new intrinsic gettering procedure [4] that is highly effective in suppressing the formation of near-surface defects; (2) to establish a means of estimating the effects of process variations such as ramping [5]; (3) to investigate the extent to which the assumed laws of growth and dissolution can be uniquely determined from experimental data.

Precipitate growth has been described for isolated precipitates [6] and for regular arrays of precipitates [7]. However, the realistic situation of a random distribution of precipitates has not been treated. Our model treats this case with simple assumptions for the forms of the growth and dissolution laws. These laws can be varied to allow a realistic estimate of their ability to predict experimental data. We note that our numerical model treats a set of discrete, interacting precipitates. This removes the restrictions of earlier approaches to oxygen precipitation in silicon that assumed either a continuum [8-10] or noninteracting precipitates [11].

We describe our numerical model and present the results of a study of oxygen outdiffusion and precipitation at $1200^{\circ}C$.

## NUMERICAL MODEL
Our numerical model treats the diffusion of interstitial oxygen $O_i$ by dividing space into cubic cells of edge d and transferring interstitial oxygen between nearest-neighbor cells at each discrete time step. This procedure amounts to solving the diffusion equation

Mat. Res. Soc. Symp. Proc. Vol. 59. ©1986 Materials Research Society

$$
\frac{\partial O_{i}}{\partial t}=D\left(\frac{\partial^{2} O_{i}}{\partial x^{2}}+\frac{\partial^{2} O_{i}}{\partial y^{2}}\right)
\tag{1}
$$

by an explicit scheme. In eq. (1) t is the time, D is the interstitial oxygen diffusion coefficient [12], x is the spatial coordinate parallel to the wafer surface, and y is the spatial coordinate perpendicular to the wafer surface, which is y = 0.0. The diffusion time is divided into discrete time steps of

$$
\Delta t=d^{2} /(4 D).
\tag{2}
$$

This time step provides a stable and well-behaved numerical scheme. Each cell starts out with the same amount of intersti- tial oxygen. If the cell has a precipitate, then some of this initial interstitial oxygen is assigned to the precipitate. We do not consider nucleation, so we start with precipitates of initial radius $R_{0}$ greater than the critical radius for dissolution. Each precipitate takes $4 \pi R_{0}^{3} n / 3$ oxygen atoms with n = $4.2 × 10^{22}/cm^{3}$, the density of oxygen atoms in silicon dioxide.

We assume that the growth and/or dissolution of a precipi- tate depend only on the average interstitial oxygen concentra- tion in the cell and on the precipitate radius R. $O_{i}$ and R change during each time step $\Delta t$. We do not allow for a spatial variation of $O_{i}$ within any single cell. These assumptions allow us to treat realistic densities of interacting precipi- tates. The local interstitial oxygen concentration drops, owing to oxygen outdiffusion at the wafer surface and to oxygen precipitation in the bulk. The precipitate radius R is calcu- lated from the amount of oxygen in the precipitate. R is then compared with a critical radius, which represents the thermody- namic approach to precipitate growth [13]. We use a critical radius (in micrometers) based on the work of Craven [14]

$$
R_{C R}=1.29 × 10^{-4} /\left\{1.0-\left(T / T_{E Q}\right)\right\}.
\tag{3}
$$

Here T is the diffusion temperature in degrees Kelvin and $T_{EQ}$ is the equilibrium temperature for the amount of interstitial oxygen per cubic centimeter in the cell. $T_{EQ}$ is found from the solid solubility relation [14]

$$
O_{i E Q}=\exp \left\{48.7-\left(11800 / T_{E Q}\right)\right\} / \mathrm{cm}^{3}.
\tag{4}
$$

If R is less than $R_{CR}$, then the precipitate is partially dissolved and $\Delta N$ oxygen atoms are added to the interstitial oxygen population of the cell with

$$
\Delta N=4 \pi D\left(O_{P R}-O_{i}\right) R\left\{1-\left(R_{C R} / R\right)\right\} \Delta t.
\tag{5}
$$

In this equation, $O_{PR}$ is the interstitial oxygen concentration that is in equilibrium with a precipitate of radius R. $O_{PR}$ is found by setting the critical radius in eq. (3) to R and eliminating $T_{EQ}$ with eq. (4). If $R>R_{CR}$, then the precipitate grows and $\Delta N$ interstitial oxygen atoms are added to the precip- itate with

$$\Delta N=4\pi D(O_{i}-O_{PR})R\{ 1-(R_{CR}/R)\} \alpha \Delta t.\qquad(6)$$

A sticking coefficient $\alpha$ is introduced as the simplest possible method of altering the diffusion-limited growth law. This allows for the possibility that the precipitate does not incorporate all the allowed oxygen atoms. Our numerical algorithms conserve the total number of oxygen atoms and take less computer time than the Monte Carlo method we used earlier [4,15].

## RESULTS AND DISCUSSION

We compare the predictions of our model with the experi- mental data of Patrick et al. [16] to show that the model produces reasonable results. The calculations are for diffu- sions at $1000^{\circ} C$ and use parameters appropriate to slug $E$ of Patrick et al. The model space is $20.2 \times 20.2 \mu m$ , each cell is $0.2 \times 0.2 \mu m$ , and the sticking coefficient $\alpha$ is set to 1.0. $O_{i}$  starts at $8.4 \times 10^{17} / cm^{3}$ , and the precipitate radius starts at8 Å. Periodic boundary conditions are applied because the model space is assumed to be in the middle of the wafer.
Figure 1 shows how the number of precipitated oxygen atoms perprecipitate varies with time. The curve labeled 20 has 20precipitates in the model space and corresponds to $5.2 \times 10^{10}$  precipitates $/ cm^{3}$ . This curve drops farther below the single precipitate result as time passes. This is due to the competi- tion between the precipitates and the lowered driving force that occurs when the amount of interstitial oxygen is decreased through precipitation. Only 12 times as much interstitial oxygen is finally precipitated in 12 h when the precipitate density is increased by 20. Figure 2 compares our calculations for the indicated precipitate densities with the experimental results for slug E of Patrick et al. [16]. The amount of precipitated interstitial oxygen per precipitate is determined, multiplied by the precipitate density, and converted to theoxygen scale Patrick et al. [16] used. They found $5.2 \times 10^{10}$  precipitates $/ cm^{3}$ for slug $E$ . Our results favor a slightly larger precipitate density. It is clear that with our simple model, the precipitate density can be established to within a factor of 2.

We next consider $13-h$ anneals at $1200^{\circ} C$ because this is a key step in an intrinsic gettering procedure [4]. The model space is enlarged to $101 \times 250 \mu m$ with a $1-\mu m$ cell edge.
Periodic boundary conditions are applied along the edges perpendicular to the wafer surface, and a reflecting or zero normal flux condition is applied at a depth of $250 \mu m$ , which is the center of the wafer. Oxygen is allowed to evaporate or outdiffuse from the top surface by forcing $O_{i}$ in the surface cells to approach the value given by eq. (4) for $1200^{\circ} C$ . This model space allows us to watch both the formation of the denuded or defect-free zone near the wafer surface and the growth of oxide precipitates in the bulk of the wafer. The calculations start with $O_{i}=9.0 \times 10^{17} / cm^{3}$ , a value used in ref. 4, and $R_{O}=18 \AA$ , which exceeds the critical radius for the initial $O_{i}$ .

![](./images/811677081669730304_1.jpg)

Fig. 1. Precipitated oxygen atoms per precipi- tate versus time. The number of precipitates in the model space label each curve.

![](./images/811677081669730304_2.jpg)

Fig. 2. Precipitated oxygen versus time. The curves are labeled with the precipitate density. The triangles are the experi- mental data for slug E of Patrick et al. [16].

Figure 3 compares the time dependence of the total amount of precipitated oxygen for two sticking coefficients and two precipitate densities. The latter differ by a factor of ~100. The sticking coefficient of 1 leads to a saturation of the amount precipitated, although the lower precipitate density does require a few more hours to reach this level. Experimen- tal results [4] show less precipitation than the curves for a sticking coefficient of 1, so we introduce smaller sticking coefficients. The small sticking coefficient curves differ by the ratio of the precipitate densities for most times. At long times the curves come closer together as the lowered driving force for precipitation reduces the amount per precipitate for the higher precipitate density case.

We investigate the effect of the sticking coefficient on experimental quantities in Figs. 4-6, which present the amount of precipitated oxygen, the denuded-zone depth, and the final average precipitate radius, respectively, for a fixed process. The denuded-zone depth depends sensitively on the sticking coefficient when it is below $3 \times 10^{-2}$, while the amount precipi- tated is always sensitive to the sticking coefficient. The precipitate density plays a strong role in determining the average precipitate radius for $\alpha>3 \times 10^{-2}$. Figure 4 shows that the amount precipitated starts to scale linearly with the number of precipitates for sticking coefficients less than 0.1. In fact, the smaller the sticking coefficient is, the larger the range of precipitate density over which the linear scaling

![](./images/811677081669730304_3.jpg)

Fig. 3. Precipitated
oxygen as a percentage of
the total initial oxygen
versus time. The curves
are labeled by the sticking
coefficient, and the
initial precipitate densi-
ties are (---) $5.78 \times 10^{9}$
and (----) $5.83 \times 10^{11}/cm^{3}$.

![](./images/811677081669730304_4.jpg)

Fig. 4. Precipitated
oxygen as a percentage of
the total initial oxygen
versus the sticking coeffi-
cient. Initial precipi-
tates$/cm^{3}$: $(\nabla)$ $5.94 \times 10^{8}$;
(O) $5.78 \times 10^{9}$; $(\Delta)$ $5.74 \times$
$10^{10}$; $(\square)$ $5.83 \times 10^{11}$.

is valid. The amount precipitated saturates for larger stick-
ing coefficients, since nearly all of the interstitial oxygen
above the equilibrium concentration has precipitated or outdif-
fused. The dependence of the denuded-zone depth on the stick-
ing coefficient (Fig. 5) occurs because a larger sticking
coefficient leads to faster precipitate growth. This means
that precipitates near the wafer surface can more quickly
exceed the critical size.

![](./images/811677081669730304_5.jpg)

Fig. 5. Denuded-zone depth
versus the sticking coeffi-
cient. . Precipitate densi-
ties as in Fig. 4.

![](./images/811677081669730304_6.jpg)

Fig. 6. Final average
precipitate radius versus
the sticking coefficient.
Precipitate densities as in
Fig. 4.

## CONCLUSIONS

We have presented selected results from a numerical simu- lation of interstitial oxygen diffusion and precipitation. Our model takes account of the interaction between precipitates in a simple fashion. The calculations predict physically measur- able quantities such as the amounts of precipitated and outdif- fused oxygen, denuded-zone depths, and precipitate sizes as functions of the precipitate density and the sticking coeffi- cient. The model is capable of predicting these quantities for arbitrary processing conditions.

## REFERENCES

1. W.K. Tice and T.Y. Tan, in Defects in Semiconductors, edited by J. Narayan and T.Y. Tan (North-Holland, Amster- dam, 1981), p. 367.

2. S.M. Hu, J. Appl. Phys. 52, 3974 (1981).

3. R.A. Craven, in Impurity Diffusion and Gettering in Silicon, edited by R.B. Fair, C.W. Pearce, and J. Washburn (Materials Research Society, Pittsburgh, PA, 1985), p. 159.

4. C.N. Anagnostopoulos, L. Rivaud, J.P. Lavine, K.Y. Wong, G.A. Hawkins, J. Kyan, and G.R. Erikson, Electrochemical Society Spring 1985 Meeting, late news paper.

5. R.F. Pinizzotto, H.F. Schaake, R.G. Massey, and D.W. Heidt, in Impurity Diffusion and Gettering in Silicon, edited by R.B. Fair, C.W. Pearce, and J. Washburn (Materi- als Research Society, Pittsburgh, PA, 1985), p. 275.

6. H.S. Carslaw and J.C. Jaeger, Conduction of Heat in Solids (Oxford University Press, Oxford, 1959), Ch. 9 and 10.

7. F.S. Ham, J. Phys. Chem. Solids 6, 335 (1958).

8. C. Weigel, J. Reffle, and D. Huber, in Electronic Devices and Materials 1984, edited by L.J. Chen (National Tsing Hua University, Hsinchu, Taiwan, 1984), p. 537.

9. S. Takasu, M. Watanabe, Y. Matsushita, T. Usami, and M. Ogino, in VSLI Science and Technology 1982, edited by C.J. Dell'Oca and W.M. Bullis (Electrochemical Society, Penning- ton, NJ, 1982), p. 33.

10. B. Rogers, R.B. Fair, W. Dyson, and G.A. Rozgonyi, in VSLI Science and Technology 1984, edited by K.E. Bean and G.A. Rozgonyi (Electrochemical Society, Pennington, NJ, 1984), p. 74.

11. N. Inoue, J. Osaka, and K. Wada, J. Electrochem. Soc. 129, 2780 (1982).

12. G.D. Watkins, J.W. Corbett, and R.S. McDonald, J. Appl. Phys. 53, 7097 (1982).

13. J.W. Martin, Micromechanisms in Particle-Hardened Alloys (Cambridge University Press, Cambridge, 1980), pp. 1-26.

14. R.A. Craven, in *Semiconductor Silicon 1981*, edited by H.R. Huff, R.J. Kriegler, and Y. Takeishi (Electrochemical Society, Pennington, NJ, 1981), p. 254.

15. J.P. Lavine, W.-C. Chang, C.N. Anagnostopoulos, B.C. Burkey, and E.T. Nelson, presented at the 2nd Conference on Numerical Simulation of VLSI Devices, Boston, Nov. 1984.

16. W. Patrick, E. Hearn, W. Westdorp, and A. Bohg, J. Appl. Phys. 50, 7156 (1979).