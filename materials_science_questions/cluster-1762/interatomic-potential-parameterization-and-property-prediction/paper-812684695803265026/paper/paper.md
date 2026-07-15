# Ge segregation at Si-Ge (001) stepped surfaces
M. Karimi,* T. Kaplan, M. Mostoller, and D. E. Jesson
Solid State Division, Oak Ridge National Laboratory, Oak Ridge, Tennessee 37831-6032
(Received 26 October 1992; revised manuscript received 8 December 1992)

Atomistic calculations using the Stillinger-Weber and Tersoff interatomic potentials are used to study the energetics of Si-Ge interchange at Si step edges on (001) Ge surfaces. The calculations indicate that Ge segregation at $S_{B}$ rebonded step edges is energetically favored. This is consistent with the Ge-pump model of Jesson, Pennycook, and Baribeau [Phys. Rev. Lett. 66, 750 (1991)].

The growth of Si-Ge superlattices by molecular-beam epitaxy (MBE) is of considerable current interest. $^{1}$ These superlattices offer the potential of direct band-gap materials for optical electronic devices which could be directly integrated into silicon-based technologies. $^{2,3}$ Recent experiments $^{4,5}$ indicate the presence of interfacial ordering in these superlattices. This ordering could have significant effects on the zone-folding properties of these structures.

The study of interfacial ordering in ultrathin $(Si_{m} Ge_{n})_{p}$  superlattices by $Z$ -contrast scanning transmission electron microscopy (STEM) produced the first atomic- resolution images of the ordered interfaces. $^{5}$ The ordering is confined to the Si layers and many different phase variants can exist at the $Si$ on $Ge$ interfaces.
Si-Ge superlattices are grown at rates sufficiently slow to preclude direct numerical simulations. An alternative numerical approach is to use experimental results as a guide for determining the critical configurations in the growth process. Then atomic simulations can be used to examine the energetics of the proposed process. The Ge- pump model of Jesson, Pennycook, and Baribeau $^{5}$ was developed from $Z$ -contrast STEM experiments to explain the complex structure at $Si-Ge$ interfaces. In the pump model, the interchange of $Ge$ and $Si$ atoms at $S_{B}$ rebonded step edges $^{6}$ is an essential part of the growth process. We have investigated the energetics of this interchange numerically by performing atomistic simulations usingclassical Stillinger-Weber $^{7,8}$ and Tersoff potentials. $^{9}$
While the Tersoff potential has been constructed for pure and mixed systems of $Si$ and $Ge$ , the StillingerWeber potential has been fitted only to pure $Si$ (Ref. 7) and $Ge^{8}$ We have constructed a Stillinger-Weber-type potential for mixed $Si-Ge$ systems using a geometric approximation similar to that used by Tersoff in constructing his mixed system potentials. The Stillinger-Weber potential is composed of two terms: a pair term and a three-body term. The pair and the three-body terms are given by

$$f_{2}\left(r_{i j}\right)= \begin{cases}\varepsilon_{i j} A_{i j}\left[B_{i j}\left(r_{i j} / \sigma_{i j}\right)^{-4}-1\right] \exp \left[\left(r_{i j} / \sigma_{i j}-1.8\right)^{-1}\right] & \text { for } r_{i j} / \sigma_{i j}<1.8 \\ 0 \quad \text { otherwise },\end{cases}$$

$$f_{3}\left(r_{j}, r_{i}, r_{k}\right)= \begin{cases}\lambda_{i j k} \varepsilon_{j i k}\left(\cos \phi_{j i k}+\frac{1}{3}\right)^{2} \exp \left[1.2\left(r_{i j} / \sigma_{i j}-1.8\right)^{-1}+1.2\left(r_{i k} / \sigma_{i k}-1.8\right)^{-1}\right], & \frac{r_{i j}}{\sigma_{i j k}}, \frac{r_{i k}}{\sigma_{i k}}<1.8 \\ 0 \quad \text { otherwise },\end{cases}$$

$$A_{i j}=\left(A_{i} A_{j}\right)^{1 / 2}, \quad B_{i j}=\left(B_{i} B_{j}\right)^{1 / 2}, \quad \varepsilon_{i j}=\left(\varepsilon_{i} \varepsilon_{j}\right)^{1 / 2},$$

$$\lambda_{i j}=\left(\lambda_{i} \lambda_{j}\right)^{1 / 2}, \quad \sigma_{i j}=\left(\sigma_{i}+\sigma_{j}\right) / 2, \quad \varepsilon_{j i k}=\left(\varepsilon_{i j} \varepsilon_{i k}\right)^{1 / 2}, \quad \lambda_{j i k}=\left(\lambda_{i j} \lambda_{i k}\right)^{1 / 2}.$$

Here, $i, j$ , and $k$ label the atoms of the system, $r_{i j}$ is the length of the $i j$ bond, and $\phi_{j i k}$ is the bond angle between $i j$ and $i k$ . The subscripts on the parameters indicate their dependence only on the type of atom. For each triplet, similar terms must be included in the sum for the total energy with $j$ and $k$ at the vertex. We have used the approximation of Grabow and Gilmer $^{10}$ for $\varepsilon_{j i k}$ and $\lambda_{j i k}$ .
We considered a (001) Ge surface with semi-infinite single-layer Si terraces as shown schematically in Fig. 1. The terraces were terminated by $S_{B}$ steps that are either rebonded or nonrebonded. The structures are similar to the ones used by Poon et al., $^{11}$ except that we used Ge for the flat surface. The structures are periodic in the plane of the surface. The basic unit was chosen to be four atomic layers wide $(4 a)$ parallel to the step edge and were varied from $6 a$ to $26 a$ normal to the step edge. $a$ is the surface lattice constant and was set initially to the Ge value of $3.995 \AA$ . The edge separation corresponds to half the periodic length normal to the step. A sufficient number of layers of $Ge$ atoms were included in the computational cell to allow atoms located above the three layers of fixed atoms to have the correct bulk cohesive energy. Four different ledge separations were considered, $3 a$ , $5 a, 9 a$ , and $13 a$ , with the number of atoms in the simulation varying from 1108 to 4268.
The structures were relaxed in constant-volume mode

![](./images/812684695803265026_1.jpg)

FIG. 1. Schematic drawing of the top few layers of the simu- lation cell showing a side view of the steps with a $3a$ separation. (a) and (c) show the $S_{B}$ rebonded step with all the Si on the ter race surface and with the Si and Ge interchanged at the step edge, respectively. Similarly, (b) and (d) show the $S_{B}$ nonre bonded step with all the Si on the terrace surface and with the Si and Ge interchanged at the step edge, respectively. Si is solid black and Ge is white.

through energy minimization by the conjugate gradient method. For each system, rebonded and nonrebonded steps with and without Ge and Si interchange at the step edge were considered. One Si atom at one of the step edges in the cell was interchanged with the adjacent Ge atom. For both Stillinger-Weber and Tersoff potentials, $\Delta E$, the change in energy per ledge atom for Si-Ge inter- change for each structure, was computed. The results are presented in Table I.

In all cases, Si-Ge interchange is energetically favor- able at $S_{B}$ steps. The gain in energy is significantly greater at the $S_{B}$ rebonded steps. These results support the Ge-pump model of Jesson, Pennycook, and Baribeau. In addition, there is virtually no dependence on ledge sep- aration. Overall the agreement between the Tersoff and Stillinger-Weber calculations is very good. Only the magnitude of the energy gain at the nonrebonded step shows any significant difference. From the work of Poon et al. $^{11}$ on pure Si steps it is known that there is a strong dependence of the ledge formation energy per atom on the ledge separation. For example, the Stillinger-Weber potential for Si $S_{B}$ rebonded steps shows a ledge forma tion energy per atom that varies from 60 meV at $3a$ sepa- ration to approximately $-10$ meV at $13a$. The absence of any significant dependence of $\Delta E$ on ledge separation in our calculations indicates that the long-range strain fields associated with the $S_{B}$ step remain approximately the same when Si and Ge are interchanged. All significant contributions to $\Delta E$ are local.

<table>
<caption>TABLE I. Energy change per ledge atom for interchange of Si and Ge at the step edge.</caption>
<tbody><tr><td>Ledge separation</td><td>Step structure</td><td>Stillinger-Weber $\Delta E$ (eV)</td><td>Tersoff $\Delta E$ (eV)</td></tr>
<tr><td>$3a$</td><td>rebonded</td><td>$-0.16$</td><td>$-0.20$</td></tr>
<tr><td>$5a$</td><td>rebonded</td><td>$-0.17$</td><td>$-0.23$</td></tr>
<tr><td>$9a$</td><td>rebonded</td><td>$-0.17$</td><td>$-0.23$</td></tr>
<tr><td>$13a$</td><td>rebonded</td><td>$-0.16$</td><td>$-0.23$</td></tr>
<tr><td>$3a$</td><td>nonrebonded</td><td>$-0.026$</td><td>$-0.11$</td></tr>
<tr><td>$5a$</td><td>nonrebonded</td><td>$-0.029$</td><td>$-0.12$</td></tr>
<tr><td>$9a$</td><td>nonrebonded</td><td>$-0.030$</td><td>$-0.12$</td></tr>
<tr><td>$13a$</td><td>nonrebonded</td><td>$-0.030$</td><td>$-0.13$</td></tr>
</tbody></table>

It is worth noting that the Ge potential parameters fit by Ding and Andersen $^{8}$ to the Stillinger-Weber potential form give a stronger three-body interaction than would be predicted by simply scaling the Si Stillinger-Weber po- tential by the Ge lattice constant and cohesive energy. Ding and Andersen chose parameters that gave a good fit for the crystal and amorphous phases. In order to pro- mote tetrahedral bonding in the amorphous phase, the bond angle forces may have been chosen to be too stiff. Despite this, the calculations with Stillinger-Weber po- tentials show reasonably good agreement with those for the Tersoff potentials.

A Monte Carlo study by Kelires and Tersoff $^{12}$ for reconstructed (001) surfaces of Si-Ge alloys shows a gen- eral tendency for surface segregation. Our results show enhanced Ge segregation at $S_{B}$ rebonded step edges demonstrating its potential importance in the growth Si- Ge layer structures.

This research was sponsored by the Division of Materi- als Sciences, U.S. Department of Energy, under Contract No. DE-AC05-84OR21400 with Martin Marietta Energy Systems, Inc. One of the authors (M.K.) was supported in part by Oak Ridge Associated Universities.

*Permanent address: Indiana University of Pennsylvania, India- na, PA.
$^{1}$See, for example, Thin Solid Films $\textbf{183}$ (1989).
$^{2}$S. Froyen, D. M. Wood, and Z. Zunger, Phys. Rev. B $\textbf{36}$, 4547 (1987).
$^{3}$T. P. Pearsall et al., Phys. Rev. Lett. $\textbf{58}$, 729 (1987).
$^{4}$E. Müller, H.-U. Nissan, M. Ospelt, and H. von Känel, Phys. Rev. Lett. $\textbf{63}$, 1819 (1989).
$^{5}$D. E. Jesson, S. J. Pennycook, and J.-M. Baribeau, Phys. Rev. Lett. $\textbf{66}$, 750 (1991).
$^{6}$D. J. Chadi, Phys. Rev. Lett. $\textbf{59}$, 1691 (1987).
$^{7}$F. Stillinger and T. Weber, Phys. Rev. B $\textbf{31}$, 5262 (1985).
$^{8}$K. Ding and C. Andersen, Phys. Rev. B $\textbf{34}$, 6987 (1986).
$^{9}$J. Tersoff, Phys. Rev. B $\textbf{39}$, 5566 (1989).
$^{10}$M. H. Grabow and G. H. Gilmer, Surf. Sci. $\textbf{194}$, 333 (1988).
$^{11}$T. W. Poon, S. Yip, P. S. Ho, and F. F. Abraham, Phys. Rev. Lett. $\textbf{65}$, 2161 (1990).
$^{12}$P. C. Kelires and J. Tersoff, Phys. Rev. Lett. $\textbf{63}$, 1164 (1989).