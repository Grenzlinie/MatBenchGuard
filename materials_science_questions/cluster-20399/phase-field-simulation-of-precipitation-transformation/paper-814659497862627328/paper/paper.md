Available online at www.sciencedirect.com

# ScienceDirect
Acta Materialia 87 (2015) 45-55

![](./images/814659497862627328_1.jpg)
www.elsevier.com/locate/actamat

# Effect of variant strain accommodation on the three-dimensional microstructure formation during martensitic transformation: Application to zirconia

Mahmood Mamivand, $^{a,b,}$ Mohsen Asle Zaeem $^{c}$ and Haitham El Kadiri $^{a,b}$

$^{a}$ Center for Advanced Vehicular System, Mississippi State University, Starkville, MS 39762, USA
$^{b}$ Department of Mechanical Engineering, Mississippi State University, Mississippi State, MS 39762, USA
$^{c}$ Department of Materials Science and Engineering, Missouri University of Science and Technology, Rolla, MO 65409, USA

Received 30 June 2014; revised 17 December 2014; accepted 19 December 2014
Available online 23 January 2015

## Abstract—This paper computationally investigates the effect of martensitic variant strain accommodation on the formation of microstructural and topological patterning in zirconia. We used the phase-field technique to capture the temporal and spatial evolution of embryonic formation of the monoclinic phase in tetragonal single crystals. The three-dimensional simulations were able to capture the formation of all the possible monoclinic variants. We used the multivariant single embryo as an initial condition to mitigate the lack of nucleation criteria at the mesoscale. Without a priori constraint, the model can select the transformation path and final microstructure. The phase-field model was benchmarked against experimental studies on surface uplift formation in zirconia reported by Deville et al. (Acta Mater 2004;52:5697, Acta Mater 2004;52:5709). The simulations showed the excellent capabilities of the model in predicting the formation of a surface relief induced by the tetragonal to monoclinic martensitic transformation.
© 2014 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

Keywords: Phase-field modeling; Martensitic transformation; Zirconia; Surface relief

## 1. Introduction

Zirconia-based ceramics are strong, hard, inert and smooth, with low thermal conductivity and good biocompatibility. Such properties make zirconia ceramics an ideal material for a range of applications from thermal barrier coatings (TBCs) to biomedical applications such as femoral implants and dental bridges [3].

Zirconia has three polymorphs: monoclinic, tetragonal and cubic. In pure zirconia, the cubic phase is stable at temperatures higher than 2640 K to the melting point, while the tetragonal phase is stable between 1430 and 2640 K, and monoclinic phase is stable at room temperature up to 1430 K. However, tetragonal zirconia can be stabilized at lower temperatures by suitable addition of alloying elements such as yttrium and cerium [3]. Nonetheless, tetragonal zirconia can still transform to monoclinic phase (stable) under external loadings or due to crack propagation in surrounding regions. In nuclear fuel rod claddings, this tetragonal to monoclinic $(T \to M)$ transformation can lead to crack and porosity formation in the thermally growing oxide layer, with deleterious effects on the structural integrity and durability of the zirconium substrate [4].

Stabilizing the tetragonal phase at the room temperature has revolutionized the application of zirconia in industry [5]. This stabilized zirconia is resistant to crack growth, as the stress field at the crack tip stimulates the $T \to M$ transformation. This transformation results in a $5 \%$ volume expansion, which helps crack closure and toughening [6,7].

$T \to M$ transformation in zirconia is one of the most studied phase transformations in ceramics. In the classical literature, the properties and mechanisms of the $T \to M$ transformation have been addressed using two different approaches. The first approach relies on the thermodynamics of transformation [7-11], while the second approach captures the crystallography and topology of the growing variants [12-17]. The thermodynamics-based approach provides some information, such as the start and finish temperatures of the transformation, and the crystallographic approach provides information on the directions of the habit and twin planes. However, failure of zirconia influenced by the $T \to M$ transformation in, for example, nuclear power plants [4] and biomedical applications [3],

* Corresponding author at: Center for Advanced Vehicular System, Mississippi State University, Starkville, MS 39762, USA. Tel.: +1 608 890 4617.; e-mail: mamivand@wisc.edu

http://dx.doi.org/10.1016/j.actamat.2014.12.036
1359-6462/© 2014 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

has raised several questions that cannot be answered by any
of the two above-mentioned approaches:
1.  What is the transformation path?
2.  What is the stress field of the transformation domains?
3.  How would the final microstructure change with loading
    and boundary conditions?
4.  How would the $\mathrm{T} \rightarrow \mathrm{M}$ transformation evolve in geo-
    metrically complicated specimens?

To redress the current gaps, a more reliable model which
captures these mechanisms is needed.

Recently, the phase-field method has been used for cap-
turing solid-state phase transformations, including recon-
structive and displacive transformations [18,19]. The
phase-field approach combines the thermodynamics, kinet-
ics and crystallographic information of a transformation to
capture the microstructural developments during the phase
transformation [20]. This method has been frequently used
in different moving-boundary applications, such as solidifi-
cation [21-24], solid-state phase transformation [25-28],
grain growth [29] and crack growth [30].

For a martensitic transformation (MT), e.g. $\mathrm{T} \rightarrow \mathrm{M}$
transformation, various types of phase-field models exist,
which mainly differ in terms of order parameters,
thermodynamic potentials, model formulations and
numerical methods. Recently, Mamivand et al. [31]
reviewed and discussed the phase-field models developed
to simulate MT. Three different phase-field approaches
were recognized for simulating MT. For instance, within
the Ginzburg-Landau theory [32], the primary order
parameters may be used to describe either some compo-
nents of the strain tensor or atomic shuffles. In the first
approach, the free energy density is a polynomial in terms
of strain components [33-38], while in the second
approach, the free energy is a Landau polynomial in terms
of atomic shuffles plus a linear or quadratic term which
couples order parameters and the strain tensor [19,39-46].
A third approach may be worth mentioning here, which
uses the same order parameters as in the aforementioned
second approach, but it couples the strain tensor
components to the order parameter(s) through a 2-3-4 or
higher-order polynomial [47-52].

We recently developed a two-dimensional (2-D) phase-
field model for $\mathrm{T} \rightarrow \mathrm{M}$ transformation in both single-crystal
and polycrystal zirconia [53,54]. The model was envisioned
based on the well-known approach of Khachaturyan, Chen
and Wang [25,40,45]. The model was able to capture some
important features observed or measured in zirconia, such
as twin morphology, transformation toughening, shape
memory effect and pseudoelasticity.

In this paper, we present a three dimensional (3-D)
phase-field model for $\mathrm{T} \rightarrow \mathrm{M}$ transformation in zirconia
which is anisotropic and elastically inhomogeneous. The
3-D formulation enables us to capture all the possible
monoclinic variants. Therefore, we can acquire more realis-
tic microstructural patterns from the simulations. The
paper is organized as follows. Section 2 describes the nature
of the $\mathrm{T} \rightarrow \mathrm{M}$ transformation, including the thermody-
namic and crystallography aspects of the transformation;
Section 3 presents the process of developing the governing
equations of the phase-field model for the $\mathrm{T} \rightarrow \mathrm{M}$ transfor-
mation; Section 4 includes model parameters; and Section 5
presents and discusses the simulation results for monoclinic
embryo evolution and compares these to the experimental
results.

## 2. The nature of the $\mathrm{T} \rightarrow \mathrm{M}$ transformation

### 2.1. Thermodynamics

Solid-state phase transformations can be reconstructive
(diffusional) or displacive (diffusionless). In reconstructive
transformations, long-range diffusion is required for the
growth of the new phases. The main characteristic feature
of reconstructive transformations is the necessity of an
atomic bond breaking in the parent phase, and new atomic
bond reconstruction in the product phase. However in dis-
placive transformations, atoms move only short distances
in order to join the new phases. $\mathrm{T} \rightarrow \mathrm{M}$ transformation
takes place by a displacive mechanism [55]. An important
type of displacive phase transformation, which is very com-
mon in both metals and ceramics, is martensitic transfor-
mation. In martensitic transformation atoms have to
move in a coordinated manner, so there is a shape change
in the crystal which is associated with transformation
strains. The nature of the displacive $\mathrm{T} \rightarrow \mathrm{M}$ transformation
has led it to be classified as a martensitic transformation,
which was first suggested by Wolten [56].

Wang et al. [57] calculated the equilibrium temperature
for the $\mathrm{T} \rightarrow \mathrm{M}$ phase transformation for pure zirconia
and adopted it to assess the Gibbs free energy of zirconia
in different phases. According to Ref. [57], the equilibrium
temperature is a temperature at which the Gibbs free
energy of both tetragonal and monoclinic phases are the
same; this temperature for $\mathrm{T} \rightarrow \mathrm{M}$ is $1367 \pm 5 \mathrm{~K}$, and the
Gibbs free energies for monoclinic and tetragonal zirconia
are:
$$
\begin{aligned}
G_{\mathrm{ZrO}_{2}}^{M}= & -1126163.5+424.8908 T-69.38751 T \ln T \\
& -0.0037588 T^{2}+683000 T^{-1},
\end{aligned}
\tag{1}
$$

$$
G_{\mathrm{ZrO}_{2}}^{T}=5468-4 T+G \mathrm{ZrO}_{2} M,
\tag{2}
$$
where the Gibbs free energies are in $\mathrm{J} \mathrm{mol}^{-1}$, and the tem-
perature $(T)$ is in Kelvin.

### 2.2. Crystallography

The $\mathrm{T} \rightarrow \mathrm{M}$ transformation has three correspondences:
$A$, $B$ and $C$ (correspondence determines which atom of
the parent phase becomes which atom of the product
phase). These are named based on which monoclinic axis
is derived from the unique tetragonal $c$ axis $\left(c_{t}\right)$. The tetrag-
onal $c$ axis can become the $a$, $b$ or $c$ axis in the monoclinic
product phase $\left(a_{m}, b_{m}\right.$ or $\left.c_{m}\right)$. When $c_{t}$ becomes $a_{m}\left(b_{m}\right.$ or
$c_{m}$) the correspondence is $A$ ($B$ or $C$). This notation system
was introduced by Kriven et al. [58].

Each correspondence has two variants (variants are
crystallographically equivalent, but rotated with respect
to each other). For example, in correspondence $C$
(Fig. 1), the $c_{t}$ axis becomes the $c_{m}$ axis, but each of the
two other tetragonal axes, which are crystallographically
equivalent, has a chance to become $a_{m}$ or $b_{m}$ axis. To distin-
guish between these correspondence variants, Hayakawa
et al. [59-61] presented another notation system. They
denoted the tetragonal axes by $a_{t}$, $b_{t}$ and $c_{t}$ (even though
the $a_{t}$ and $b_{t}$ are crystallographically equivalent), and used
a three-letter notation for different monoclinic correspon-
dences and variants. In this notation, the first, second,
and third letters indicate which axes would derive from

![](./images/814659497862627328_2.jpg)

Fig. 1. Three-dimensional schematics of possible monoclinic variants of correspondence $C$.

the $a_{t}, b_{t}$ and $c_{t}$ axes in the monoclinic crystal. For instance $B A C$ shows that the $a_{t}$ axis becomes the $b_{m}$ axis, the $b_{t}$ axis becomes the $a_{m}$ axis, and the $c_{t}$ axis becomes the $c_{m}$ axis; and $A B C$ shows that the $a_{t}$ axis becomes the $a_{m}$ axis, the $b_{t}$ axis becomes the $b_{m}$ axis, and the $c_{t}$ axis becomes the $c_{m}$ axis. $B A C$ and $A B C$ are two variants of the correspondence $C$ which are related by a $90^{\circ}$ rotation about $c_{t}(c_{t} \| c_{m})$. These variants are illustrated in Fig. 1 (note that in variants1 and 2, the $a_{m}$ and $b_{m}$ axes switch places).

In a tetragonal crystal all the crystallographic axes are orthogonal, while in monoclinic zirconia the angle between $a_{m}$ and $c_{m}$ is $\sim 99^{\circ}$ [17]. Therefore, in the orientation relationship between two phases all crystallographic axes cannot be parallel. The monoclinic $b_{m}$ axis is perpendicular to both $a_{m}$ and $c_{m}$ , so if we set the orientation relation such that $b_{m}$ remains parallel to one of the tetragonal axes, then one or the other monoclinic axes $(a_{m}$ or $c_{m})$ could be parallel to their parent axis in the tetragonal form. This situation suggests two possible orientations for each variant, $O R 1$ and $O R 2$ . In both orientations the $b_{m}$ is parallel to the tetragonal axis while $a_{m}$ in $O R 1$ and $c_{m}$ in $O R 2$ remains parallel to the tetragonal axes [17]. In other words, for the $O R 1$ case the plane $a_{m} \times b_{m}$ and for the $O R 2$ case the plane $c_{m} \times b_{m}$ remains unrotated. The last column of Fig. 1 shows the possible orientations of correspondence $C$ of a monoclinic crystal. The combination of correspondences, variants and orientations gives 12 possible monoclinic crystals for each tetragonal crystal in the $T \to M$ transformation.

Each variant can be represented by a specific notation representing its plane and direction. For example, in the case of $B C A-O R 1$ , the $O R 1$ indicates that $a_{m}$ is unrotated and because $A$ is in the third place in $B C A$ , it replaces the $c_{t}$ , so $[100]_{m} \sim \|[001]_{t}$ . The $b_{m}$ can always be aligned with the tetragonal axis and since $B$ is in the first place, it replaces the $a_{t}$ , so $[010]_{m} \sim \|[100]_{t}$ . The $a_{m}$ and $b_{m}$ form a plane which is parallel with its tetragonal counterpart plane so their normal vectors are also parallel, therefore(001)m ~ ||(010)1. Combining all directional relations, theBCA - OR1 can be represented as follows:

$$(001)_{m} \sim \|(010)_{t}$$

$$[100]_{m} \sim \|[001]_{t}$$

$$[010]_{m} \sim \|[100]_{t}$$

Table 1 shows the 12 monoclinic variants and their acronyms to identify them based on their planes and directions.

Each monoclinic variant has a self-accommodating variant. Self-accommodating variants (which accommodate the shear strain) are the reflected image of each variant about its unrotated plane. For instance, in the case of $O R 1$ variants, since the $a_{m}$ and $b_{m}$ are parallel to their tetragonal counterpart axes, the unrotated plane is $\vec{a}_{m} \times \vec{b}_{m}$ . With the same logic, in the case of $O R 2$ variants the unrotated plane is $\vec{c}_{m} \times \vec{b}_{m}$ . Fig. 2 shows all 12 possible monoclinic variants for the $T \to M$ transformation and their self-accommodating variants.

The tensorial quantities of self-accommodating variants can be obtained by proper reflections of the tensorial quantities of the original variants (see Fig. 3).

The reflection matrixes about different planes are:

$$
R_{x y}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & -1
\end{array}\right], R_{x z}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right], R_{y z}=\left[\begin{array}{ccc}
-1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right],
\tag{3}
$$

<table>
<caption>Table 1. Acronyms of the 12 monoclinic variants.</caption>
<tbody>
<tr>
<td>(1)</td>
<td>$ABC-OR1$</td>
<td>$(001)_m \sim \|(001)_t$</td>
<td>(2)</td>
<td>$ABC-OR2$</td>
<td>$(100)_m \sim \|(100)_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[100]_m \sim \|[100]_t$</td>
<td></td>
<td></td>
<td>$[010]_m \sim \|[010]_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[010]_m \sim \|[010]_t$</td>
<td></td>
<td></td>
<td>$[001]_m \sim \|[001]_t$</td>
</tr>
<tr>
<td>(3)</td>
<td>$BAC-OR1$</td>
<td>$(001)_m \sim \|(001)_t$</td>
<td>(4)</td>
<td>$BAC-OR2$</td>
<td>$(100)_m \sim \|(010)_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[100]_m \sim \|[010]_t$</td>
<td></td>
<td></td>
<td>$[010]_m \sim \|[100]_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[010]_m \sim \|[100]_t$</td>
<td></td>
<td></td>
<td>$[001]_m \sim \|[001]_t$</td>
</tr>
<tr>
<td>(5)</td>
<td>$ACB-OR1$</td>
<td>$(001)_m \sim \|(010)_t$</td>
<td>(6)</td>
<td>$ACB-OR2$</td>
<td>$(100)_m \sim \|(100)_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[100]_m \sim \|[100]_t$</td>
<td></td>
<td></td>
<td>$[010]_m \sim \|[010]_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[010]_m \sim \|[001]_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$[001]_m \sim \|[010]_t$</td>
</tr>
<tr>
<td>(7)</td>
<td>$CAB-OR1$</td>
<td>$(001)_m \sim \|(100)_t$</td>
<td>(8)</td>
<td>$CAB-OR2$</td>
<td>$(100)_m \sim \|(010)_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[100]_m \sim \|[010]_t$</td>
<td></td>
<td></td>
<td>$[010]_m \sim \|[001]_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[010]_m \sim \|[001]_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$[001]_m \sim \|[100]_t$</td>
</tr>
<tr>
<td>(9)</td>
<td>$BCA-OR1$</td>
<td>$(001)_m \sim \|(010)_t$</td>
<td>(10)</td>
<td>$BCA-OR2$</td>
<td>$(100)_m \sim \|(001)_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[100]_m \sim \|[001]_t$</td>
<td></td>
<td></td>
<td>$[010]_m \sim \|[100]_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[010]_m \sim \|[100]_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$[001]_m \sim \|[010]_t$</td>
</tr>
<tr>
<td>(11)</td>
<td>$CBA-OR1$</td>
<td>$(001)_m \sim \|(100)_t$</td>
<td>(12)</td>
<td>$CBA-OR2$</td>
<td>$(100)_m \sim \|(001)_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[100]_m \sim \|[001]_t$</td>
<td></td>
<td></td>
<td>$[001]_m \sim \|[010]_t$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$[010]_m \sim \|[010]_t$</td>
<td></td>
<td></td>
<td>$[001]_m \sim \|[100]_t$</td>
</tr>
</tbody>
</table>

![](./images/814659497862627328_3.jpg)

Fig. 2. Possible monoclinic variants in the $\text{T} \rightarrow \text{M}$ transformation and their self-accommodating variants.

![](./images/814659497862627328_4.jpg)

Fig. 3. Schematic of the rotation-procedure sequence to get variant $CAB$ from $ABC$.

where $R_{xy}$, $R_{xz}$ and $R_{yz}$ are reflection tensors about the $xy$, $xz$ and $yz$ planes, respectively.

To calculate the tensorial quantities of the self-accommodating variants, a right reflection tensor must be selected. The reflection tensor is calculated based on the tetragonal coordinate system. For example, for variant $CAB-OR1$ the accommodating variant is $\bar{C}AB-OR1$. Therefore in monoclinic coordinates the reflection is about $(001)_{m}$, but since the monoclinic $c_{m}$ is a counterpart of $a_{t}$, the reflection plane is $(100)_{t}$ and its rotation tensor is $R_{yz}$. Similarly for $CAB-OR2$ the accommodating variant is $\bar{C}AB-OR2$ and since the $a_{m}$ is the counterpart of $b_{t}$ the reflection plane is $(010)_{t}$.

### 3. Phase-field model

The phase-field governing equation for martensitic transformations, as the order parameters (monoclinic variants) are not conserved quantities, is the Ginzburg-Landau [32] (or Allen-Cahn [62]) equation. The Ginzburg-Landau equation has a phenomenological character and relates the rate of order parameter to the variational derivative of total free energy to the order parameter:
$$
\frac{\partial \eta_{p}(\vec{r}, t)}{\partial t}=-L \frac{\delta F}{\delta \eta_{p}(\vec{r}, t)} \quad p=1, \ldots, n
\tag{4}
$$
where $\eta_{p}$ represents the $p$ th variant of the monoclinic form, $L$ is the kinetic coefficient, $F$ is the total free energy of system, $\delta F / \delta \eta_{p}(\vec{r}, t)$ is the thermodynamic driving force for spatial and temporal evolution of $\eta_{p}$, and $n$ is the number of possible martensitic variants. The value of $\eta_{p}$ varies approximately from 0 to 1 ; where $\eta_{p} \approx 1$, the monoclinic $p$ th variant exists, and where $\eta_{p} \approx 0$, one of the other variants of the monoclinic phase or the parent phase exists.

In MT the total free energy is a combination of chemical free energy and elastic strain energy:
$$
F=F_{c h}+F_{e l}.
\tag{5}
$$

### 3.1. Chemical free energy

The chemical free energy is the driving force of MT and can be written as [45]:
$$
F_{c h}=\int_{V}\left[f\left(\eta_{1}, \eta_{2}, \ldots, \eta_{n}\right)+\frac{1}{2} \sum_{z=1}^{n} \beta_{i j}(p) \nabla_{i} \eta_{z} \nabla_{j} \eta_{z}\right] d V
$$
$$
n=1, \ldots, p,
\tag{6}
$$
where $\beta_{i j}(p)$ is a positive gradient energy coefficient, $\nabla$ is the gradient operator, and $f(\eta_{1}, \eta_{2}, \ldots, \eta_{n})$ is the local specific free energy density defining the basic bulk thermodynamic properties of the system. $f(\eta_{1}, \eta_{2}, \ldots, \eta_{n})$ can be approximated by the Landau polynomial in terms of long-range order parameters $\eta_{p}$. We selected the fourth-order polynomial form for the local specific free energy [49]:
$$
\begin{aligned}
f\left(\eta_{1}, \eta_{2}, \ldots, \eta_{n}\right)= & A\left(\eta_{1}^{2}+\eta_{2}^{2}+\cdots+\eta_{n}^{2}\right)+(4 \Delta G-2 A) \\
& \times\left(\eta_{1}^{3}+\eta_{2}^{3}+\cdots+\eta_{n}^{3}\right)+(A \\
& -3 \Delta G)\left(\eta_{1}^{2}+\eta_{2}^{2}+\cdots+\eta_{n}^{2}\right)^{2},
\end{aligned}
\tag{7}
$$

Table 2. Deformation gradient tensor of all monoclinic variants in the $\mathrm{T} \rightarrow \mathrm{M}$ transformation $\left(\beta=98.6^{\circ}\right)$.
| Variant | Deformation gradient | Variant | Deformation gradient |
|---------|----------------------|---------|----------------------|
| $A B C-O R 1$ | $\left[\begin{array}{ccc}\frac{a_{m}}{a_{t}} & 0 & \frac{c_{m} \cos (\beta)}{c_{t}} \\ 0 & \frac{b_{m}}{b_{t}} & 0 \\ 0 & 0 & \frac{c_{m} \sin (\beta)}{c_{t}}\end{array}\right]$ | $A B C-O R 2$ | $\left[\begin{array}{ccc}\frac{a_{m} \sin (\beta)}{a_{t}} & 0 & 0 \\ 0 & \frac{b_{m}}{b_{t}} & 0 \\ \frac{a_{m} \cos (\beta)}{a_{t}} & 0 & \frac{c_{m}}{c_{t}}\end{array}\right]$ |
| $B A C-O R 1$ | $\left[\begin{array}{ccc}\frac{b_{m}}{a_{t}} & 0 & 0 \\ 0 & \frac{a_{m}}{b_{t}} & \frac{c_{m} \cos (\beta)}{c_{t}} \\ 0 & 0 & \frac{c_{m} \sin (\beta)}{c_{t}}\end{array}\right]$ | $B A C-O R 2$ | $\left[\begin{array}{ccc}\frac{b_{m}}{a_{t}} & 0 & 0 \\ 0 & \frac{a_{m} \sin (\beta)}{b_{t}} & 0 \\ 0 & \frac{a_{m} \cos (\beta)}{b_{t}} & \frac{c_{m}}{c_{t}}\end{array}\right]$ |
| $A C B-O R 1$ | $\left[\begin{array}{ccc}\frac{a_{m}}{a_{t}} & \frac{c_{m} \cos (\beta)}{b_{t}} & 0 \\ 0 & \frac{c_{m} \sin (\beta)}{b_{t}} & 0 \\ 0 & 0 & \frac{b_{m}}{c_{t}}\end{array}\right]$ | $A C B-O R 2$ | $\left[\begin{array}{ccc}\frac{a_{m} \sin (\beta)}{a_{t}} & 0 & 0 \\ \frac{a_{m} \cos (\beta)}{a_{t}} & \frac{c_{m}}{b_{t}} & 0 \\ 0 & 0 & \frac{b_{m}}{c_{t}}\end{array}\right]$ |
| $C A B-O R 1$ | $\left[\begin{array}{ccc}\frac{c_{m} \sin (\beta)}{a_{t}} & 0 & 0 \\ \frac{c_{m} \cos (\beta)}{a_{t}} & \frac{a_{m}}{b_{t}} & 0 \\ 0 & 0 & \frac{b_{m}}{c_{t}}\end{array}\right]$ | $C A B-O R 2$ | $\left[\begin{array}{ccc}\frac{c_{m}}{a_{t}} & \frac{a_{m} \cos (\beta)}{b_{t}} & 0 \\ 0 & \frac{a_{m} \sin (\beta)}{b_{t}} & 0 \\ 0 & 0 & \frac{b_{m}}{c_{t}}\end{array}\right]$ |
| $B C A-O R 1$ | $\left[\begin{array}{ccc}\frac{b_{m}}{a_{t}} & 0 & 0 \\ 0 & \frac{c_{m} \sin (\beta)}{b_{t}} & 0 \\ 0 & \frac{c_{m} \cos (\beta)}{b_{t}} & \frac{a_{m}}{c_{t}}\end{array}\right]$ | $B C A-O R 2$ | $\left[\begin{array}{ccc}\frac{b_{m}}{a_{t}} & 0 & 0 \\ 0 & \frac{c_{m}}{b_{t}} & \frac{a_{m} \cos (\beta)}{c_{t}} \\ 0 & 0 & \frac{a_{m} \sin (\beta)}{c_{t}}\end{array}\right]$ |
| $C B A-O R 1$ | $\left[\begin{array}{ccc}\frac{c_{m} \sin (\beta)}{a_{t}} & 0 & 0 \\ 0 & \frac{b_{m}}{b_{t}} & 0 \\ \frac{c_{m} \cos (\beta)}{a_{t}} & 0 & \frac{a_{m}}{c_{t}}\end{array}\right]$ | $C B A-O R 2$ | $\left[\begin{array}{ccc}\frac{c_{m}}{a_{t}} & 0 & \frac{a_{m} \cos (\beta)}{c_{t}} \\ 0 & \frac{b_{m}}{b_{t}} & 0 \\ 0 & 0 & \frac{a_{m} \sin (\beta)}{c_{t}}\end{array}\right]$ |

<table><thead><tr><th>Crystal parameter</th><th>$a$</th><th>$B$</th><th>$c$</th><th>$\beta$</th></tr></thead><tbody><tr><td>Tetragonal</td><td>5.141</td><td>5.141</td><td>5.2609</td><td>$90^{\circ}$</td></tr><tr><td>Monoclinic</td><td>5.184</td><td>5.207</td><td>5.370</td><td>$98.8^{\circ}$</td></tr></tbody></table>

where $\Delta G$ is the difference in the specific chemical free energy between the tetragonal and the monoclinic phase (Eqs. (1) and (2)), and $A$ is a material property. The free energy polynomial must give unstable austenite at temperatures lower than the austenite critical temperature (the temperature at which austenite loses its thermodynamic stability), so $A$ can simply be defined as $A_{0}(T-T_{c}), A_{0}>0$, where $T_{c}$ is a austenite critical temperature. If we assume the equilibrium temperature is the average of the austenite and martensite start temperatures, we simply have $\Delta G=A_{0}(T-T_{e})/3$ [47,49], where $T_{e}$ is the equilibrium temperature between austenite and martensite.

We assume that the positive gradient energy coefficient is isotropic $(\beta_{ij}=\beta\delta_{ij})$; therefore the chemical free energy can be simplified as:

$$
F_{c h}=\int_{V}\left[f\left(\eta_{1}, \eta_{2}, \ldots, \eta_{n}\right)+\frac{1}{2} \sum_{z=1}^{n} \beta\left(\nabla_{i} \eta_{z}\right)^{2}\right] d V.
\tag{8}
$$

<table><tbody><tr><td>Variant</td><td></td><td></td><td>Self-accommodating variant</td><td></td><td></td></tr><tr><td>Order parameter</td><td>Variant</td><td>Stress-free strain</td><td>Order parameter</td><td>Variant</td><td>Stress-free strain</td></tr><tr><td>$\eta_{1}$</td><td>$ABC$</td><td>$\begin{bmatrix}0.0049 & 0 & -0.0760 \\ 0 & 0.0117 & 0 \\ -0.0760 & 0 & 0.0180\end{bmatrix}$</td><td>$\eta_{2}$</td><td>$AB\bar{C}$</td><td>$\begin{bmatrix}0.0049 & 0 & 0.0760 \\ 0 & 0.0117 & 0 \\ 0.0760 & 0 & 0.0180\end{bmatrix}$</td></tr><tr><td>$\eta_{3}$</td><td>$BAC$</td><td>$\begin{bmatrix}0.0117 & 0 & 0 \\ 0 & 0.0049 & -0.0760 \\ 0 & -0.0760 & 0.0180\end{bmatrix}$</td><td>$\eta_{4}$</td><td>$BA\bar{C}$</td><td>$\begin{bmatrix}0.0117 & 0 & 0 \\ 0 & 0.0049 & 0.0760 \\ 0 & 0.0760 & 0.0180\end{bmatrix}$</td></tr><tr><td>$\eta_{5}$</td><td>$ACB$</td><td>$\begin{bmatrix}0.0048 & -0.0769 & 0 \\ -0.0769 & 0.0418 & 0 \\ 0 & 0 & -0.0114\end{bmatrix}$</td><td>$\eta_{6}$</td><td>$A\bar{C}B$</td><td>$\begin{bmatrix}0.0048 & 0.0769 & 0 \\ 0.0769 & 0.0418 & 0 \\ 0 & 0 & -0.0114\end{bmatrix}$</td></tr><tr><td>$\eta_{7}$</td><td>$CAB$</td><td>$\begin{bmatrix}0.0418 & -0.0769 & 0 \\ -0.0769 & 0.0048 & 0 \\ 0 & 0 & -0.0114\end{bmatrix}$</td><td>$\eta_{8}$</td><td>$\bar{C}AB$</td><td>$\begin{bmatrix}0.0418 & 0.0769 & 0 \\ 0.0769 & 0.0048 & 0 \\ 0 & 0 & -0.0114\end{bmatrix}$</td></tr><tr><td>$\eta_{9}$</td><td>$BCA$</td><td>$\begin{bmatrix}0.0117 & 0 & 0 \\ 0 & 0.0419 & -0.0760 \\ 0 & -0.0760 & -0.0181\end{bmatrix}$</td><td>$\eta_{10}$</td><td>$B\bar{C}A$</td><td>$\begin{bmatrix}0.0117 & 0 & 0 \\ 0 & 0.0419 & 0.0760 \\ 0 & 0.0760 & -0.0181\end{bmatrix}$</td></tr><tr><td>$\eta_{11}$</td><td>$CBA$</td><td>$\begin{bmatrix}0.0419 & 0 & -0.0760 \\ 0 & 0.0117 & 0 \\ -0.0760 & 0 & -0.0181\end{bmatrix}$</td><td>$\eta_{12}$</td><td>$\bar{C}BA$</td><td>$\begin{bmatrix}0.0419 & 0 & 0.0760 \\ 0 & 0.0117 & 0 \\ 0.0760 & 0 & -0.0181\end{bmatrix}$</td></tr></tbody></table>

<table><thead><tr><th>$C_{11}$</th><th>$C_{22}$</th><th>$C_{33}$</th><th>$C_{44}$</th><th>$C_{55}$</th><th>$C_{66}$</th><th>$C_{12}$</th><th>$C_{13}$</th><th>$C_{16}$</th><th>$C_{23}$</th><th>$C_{26}$</th><th>$C_{36}$</th><th>$C_{45}$</th></tr></thead><tbody><tr><td>361</td><td>408</td><td>258</td><td>100</td><td>81</td><td>126</td><td>142</td><td>55</td><td>$-21$</td><td>196</td><td>31</td><td>$-18$</td><td>$-23$</td></tr></tbody></table>

### 3.2. Elastic strain energy

In MT, an important contribution to the total free energy comes from the strain energy caused by the lattice mismatch between the product precipitates and the parent matrix. It has been shown by Khachaturyan [63] that the strain energy can be expressed as a function of the transformation-induced stress-free strain $\varepsilon_{i j}^{0}(\vec{r})$. In fact, the degree of lattice mismatch between precipitates and matrix can be characterized by stress-free strain. Because of our diffusive interface description, we need to express the stress-free strain in terms of phase-field variables; therefore, the local stress-free strain is related to order parameters as follows [49]:

$$
\varepsilon_{i j}^{0}(\vec{r})=\sum_{p=1}^{n} \varepsilon_{i j}^{00}(p) \eta_{p}^{2}(\vec{r}),
\tag{9}
$$

where $\varepsilon_{i j}^{00}(p)$ is the transformation strain of the $p$th variant. The elastic strain energy of a system is given by:

$$
F_{e l}=\frac{1}{2} \int_{V} \sigma_{i j} \varepsilon_{i j}^{e l} d V=\frac{1}{2} \int_{V} C_{i j k l} \varepsilon_{k l}^{e l} \varepsilon_{i j}^{e l} d V,
\tag{10}
$$

where the elastic strain $\varepsilon_{i j}^{e l}(\vec{r})$ is the difference between the total strain, $\varepsilon_{i j}^{t o t}(\vec{r})$, and the stress free strain, $\varepsilon_{i j}^{0}(\vec{r})$:

<table><caption>Table 6. Elastic constants for tetragonal zirconia (GPa) [71,72].</caption>
<tbody><tr><td>$C_{11}$</td><td>$C_{33}$</td><td>$C_{44}$</td><td>$C_{66}$</td><td>$C_{12}$</td><td>$C_{13}$</td></tr>
<tr><td>327</td><td>264</td><td>59</td><td>64</td><td>100</td><td>62</td></tr>
</tbody></table>

<table><caption>Table 7. Numerical values used for calculation.</caption>
<tbody><tr><td>Temperature (K)</td><td>1170</td></tr>
<tr><td>A ($\text{N m}^{-2}$)</td><td>$2.5\times10^{6}$</td></tr>
<tr><td>Chemical driving force ($\text{J mol}^{-1}$)</td><td>$-788$</td></tr>
<tr><td>Gradient energy coefficient, $\beta$ ($\text{J m}^{-1}$)</td><td>$2.5\times10^{-9}$</td></tr>
<tr><td>Kinetic coefficient, $L$ ($\text{m}^{3}\text{J}^{-1}\text{s}^{-1}$)</td><td>2</td></tr>
<tr><td>Domain size ($\mu\text{m}\times\mu\text{m}\times\mu\text{m}$)</td><td>$1.0\times1.0\times1.0$</td></tr>
<tr><td>Embryo size ($\mu\text{m}\times\mu\text{m}\times\mu\text{m}$)</td><td>$0.2\times0.2\times0.2$</td></tr>
</tbody></table>

![](./images/814659497862627328_5.jpg)

Fig. 4. Formation of variants of correspondence $C$ as surface uplift on (001)$_r$. (Green is tetragonal phase.) (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

$$
\begin{aligned}
\varepsilon_{i j}^{e l}(\vec{r}) & =\varepsilon_{i j}^{t o t}(\vec{r})-\varepsilon_{i j}^{0}(\vec{r})=\varepsilon_{i j}^{t o t}(\vec{r})-\sum_{p=1}^{n} \varepsilon_{i j}^{00}(p) \eta_{p}^{2}(\vec{r}) \\
& =\frac{1}{2}\left(\frac{\partial u_{i}(\vec{r})}{\partial r_{j}}+\frac{\partial u_{j}(\vec{r})}{\partial r_{i}}\right)-\sum_{p=1}^{n} \varepsilon_{i j}^{00}(p) \eta_{p}^{2}(\vec{r}).
\end{aligned}\qquad(11)
$$

The transformation strain [64], eigenstrain [65] or Bain strain [66] are all names for the stress-free strain, which is the strain that occurs inside the material during phase transformation in the absence of external constraints. In martensitic transformations, each variant has its own stress-free strain which can be calculated from lattice parameters of parent and product. For small strains the transformation strain is [64]:
$$
\varepsilon_{i j}^{00}(p)=U_{i j}(p)-\delta_{i j},\qquad(12)
$$
where $U_{i j}(p)$ is the symmetric right stretch tensor of deformation gradient which maps the parent crystal to the $p$th variant of the product.

To calculate the transformation strain for all monoclinic variants and their self-accommodating variants, we need to calculate the deformation gradient tensors for all variants. Table 2 shows the deformation gradient tensors for all monoclinic variants.

### 3.3. Governing equations

The Ginzburg-Landau equation for the $\mathrm{T} \rightarrow \mathrm{M}$ transformation with the given energy functional in the previous section is:
$$
\begin{aligned}
& \frac{\partial \eta_{p}(\vec{r}, t)}{\partial t}=-L\left(-\beta \nabla^{2} \eta_{p}(\vec{r}, t)+\frac{\partial f}{\partial \eta_{p}(\vec{r}, t)}+\frac{\delta F_{e l}}{\delta \eta_{p}(\vec{r}, t)}\right) \\
& p=1, \ldots, n
\end{aligned}\qquad(13)
$$
where $f$ was defined in Eq. (7), and:
$$
\begin{aligned}
\frac{\delta F_{e l}}{\delta \eta_{p}(\vec{r}, t)}= & -\frac{1}{2} C_{i j k l} \varepsilon_{k l}^{00}(p) \eta_{p}(\vec{r}, t)\left(u_{i, j}(\vec{r})+u_{j, i}(\vec{r})\right) \\
& +C_{i j k l} \varepsilon_{k l}^{00}(p) \eta_{p}(\vec{r}, t) \sum_{z=1}^{n} \varepsilon_{i j}^{00}(z) \eta_{z}^{2}(\vec{r}, t) \\
& -\frac{1}{2} C_{i j k l} \varepsilon_{i j}^{00}(p) \eta_{p}(\vec{r}, t)\left(u_{k, l}(\vec{r})+u_{l, k}(\vec{r})\right) \\
& +C_{i j k l} \varepsilon_{i j}^{00}(p) \eta_{p}(\vec{r}, t) \sum_{z=1}^{n} \varepsilon_{k l}^{00}(z) \eta_{z}^{2}(\vec{r}, t).
\end{aligned}\qquad(14)
$$

The Ginzburg-Landau equations are coupled to the mechanical equilibrium equations to find the displacement of domain:
$$
\frac{\partial \sigma_{i j}}{\partial r_{j}}=0 \Rightarrow C_{i j k l}\left[\frac{1}{2}\left(u_{k, l j}(\vec{r})+u_{l, k j}(\vec{r})\right)-\sum_{z=1}^{n} \varepsilon_{k l}^{00}(z) \frac{\partial}{\partial r_{j}}\left(\eta_{z}^{2}(\vec{r})\right)\right]=0. \quad(15)
$$

### 4. Model parameters

In this work, we study the $\mathrm{T} \rightarrow \mathrm{M}$ transformation in a 3D single crystal. The domain size is $1 \mu m \times 1 \mu m \times 1 \mu m$. We assume that the tetragonal crystal is embedded in an untransformable matrix except on the top surface, which is free. The initial condition for the order parameters is a multivariant monoclinic single embryo, and the boundary condition for the $i$th-order parameter is:
$$
n \cdot \nabla \eta_{i}=0, \quad i=1, \ldots, p,\qquad(16)
$$
where the $n$ is the surface normal and $p$ is the number of order parameters.

We consider inhomogeneous elasticity and define a linear transition from tetragonal to monoclinic elastic constants through the following equation:
$$
\tilde{C}=\tilde{C}^{T}\left[1-\left(\eta_{1}+\eta_{2}+\cdots+\eta_{p}\right)\right]+\tilde{C}^{M},\qquad(17)
$$
where $\tilde{C}^{M}$ and $\tilde{C}^{T}$ are monoclinic and tetragonal elastic constants tensors, respectively, and $p$ is the number of order parameters.

To cover elastic inhomogeneity between different monoclinic variants, the monoclinic elastic constant tensor must be customized for each variant. The monoclinic elastic constants given in Table 5 are for variant $A B C$ and must be changed by proper rotations to fit the other variants. For example, to obtain the elastic constants tensor for $C A B$,

![](./images/814659497862627328_6.jpg)

Fig. 5. The evolution of monoclinic embryo on tetragonal single crystal in volume (first column) and isosurface ($\eta=0.5$). (Green is tetragonal, orange is variant $ABC$, light blue (cyan in isosurface) is variant $AB\bar{C}$, red is variant $BAC$, and dark blue is variant $BA\bar{C}$.) (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

we must rotate the $ABC$ tensor $90^{\circ}$ about $b_{m}$ and then $90^{\circ}$ about the new $c_{m}$.

Since the rotation sequence for each variant is specific, we must find the final rotation matrix of each variant by proper combination of individual axis rotations. If $\varphi$, $\theta$ and $\psi$ are rotation angles about $x$, $y$ and $z$ respectively, their rotation matrixes would be:
$$
R x=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & \cos (\varphi) & -\sin (\varphi) \\
0 & \sin (\varphi) & \cos (\varphi)
\end{array}\right], R y=\left[\begin{array}{ccc}
\cos (\theta) & 0 & \sin (\theta) \\
0 & 1 & 0 \\
-\sin (\theta) & 0 & \cos (\theta)
\end{array}\right],
$$

$$
R z=\left[\begin{array}{ccc}
\cos (\psi) & -\sin (\psi) & 0 \\
\sin (\psi) & \cos (\psi) & 0 \\
0 & 0 & 1
\end{array}\right]. \tag{18}
$$

The inhomogeneous monoclinic elastic constants tensor considering the effect of variant rotation would be:
$$
\begin{aligned}
\tilde{C}^{M}= & \eta_{1} \tilde{C}_{A B C}^{M}+\eta_{2} \tilde{C}_{A B \bar{C}}^{M}+\eta_{3} \tilde{C}_{B A C}^{M}+\eta_{4} \tilde{C}_{B A \bar{C}}^{M}+\eta_{5} \tilde{C}_{A C B}^{M} \\
& +\eta_{6} \tilde{C}_{A C \bar{B}}^{M}+\eta_{7} \tilde{C}_{C A B}^{M}+\eta_{8} \tilde{C}_{\bar{C} A B}^{M} \eta_{9} \tilde{C}_{B C A}^{M}+\eta_{10} \tilde{C}_{B \bar{C} A}^{M} \\
& +\eta_{11} \tilde{C}_{C B A}^{M}+\eta_{12} \tilde{C}_{\bar{C} B A}^{M},
\end{aligned} \tag{19}
$$
where the $\tilde{C}^{M}$ is the inhomogeneous monoclinic elastic constants tensor and $\tilde{C}_{X Y Z}^{M}$ represents the $X Y Z$ variant elastic constants tensor.

Table 3 gives the crystal lattice parameters for both monoclinic and tetragonal phases of zirconia. Using the lattice parameters and deformation gradient tensors in Table 2, we can calculate the stress-free strain of all monoclinic variants (Table 4).

We used COMSOL Multiphysics to solve the partial differential equations [67]. The input parameters of the model are given in Tables 5-7.

## 5. Results and discussion

We studied the evolution of a monoclinic embryo in a tetragonal single crystal. It was assumed that the tetragonal crystal was embedded in an untransformable matrix, except on the top surface, which was considered to be a free surface. Since the strain accommodation is much easier on free surfaces, the monoclinic embryo was placed on the free surface (Fig. 5).

![](./images/814659497862627328_7.jpg)

Fig. 6. Surface uplift on (001), (free surface) due to tetragonal to monoclinic transformation in zirconia. A comparison between phase-field simulation (left) and AFM micrograph (right) [1] (Simulation size is $1\ \mathrm{\mu m} \times 0.5\ \mathrm{\mu m}$).

![](./images/814659497862627328_8.jpg)

Fig. 7. Arrangement of four monoclinic variants outside (left) and inside (right) of tetragonal crystal, when the free surface is (001)$_t$.

Fig. 5 shows the evolution of a monoclinic embryo in a tetragonal crystal when (001)$_t$ is the free surface. We define the initial embryo as a multivariant embryo which contains all 12 monoclinic variants with the same chance of formation and evolution; however, the dominant variants will be selected based on the inherent minimum formation energy criteria. In our case study, where (001)$_t$ is the free surface, the results show that system lets the variants of correspondence $C$, including $ABC$, $AB\overline{C}$, $BAC$, and $BA\overline{C}$ grow, and the other variants are dissipated.

Deville et al. [1,2,73] studied the surface relief resulting from $\mathrm{T} \rightarrow \mathrm{M}$ transformation in zirconia by atomic force microscopy (AFM). They discussed a particular case where $[001]_l$ was perpendicular to the free surface. They showed that for a surface uplift on (001)$_t$, only possible correspondences were $C$ and $A$. These variants have shape strain directions with a common large component along the $c_t$ axis and a common free surface. Deville's et al. [1] phenomenological crystallographic calculations and energetic reasoning make correspondence $A$ energetically unfavorable and unlikely to happen, which was validated experimentally by AFM observations. Our phase-field simulation results also show that when (001)$_t$ is the free surface, only variants of the correspondence $C$ would form on the free surface (Fig. 4). Variants of the correspondence $C$ are the ones that reject the most volume change toward the surface, and therefore there will be a large decrease in transformation-induced elastic stress within the volume.

Fig. 5 shows the evolution of a multivariant monoclinic embryo in a tetragonal crystal. At the beginning, all the monoclinic variants are available and they have the same chance to grow. However, the system only selects the favorable variants based on the minimum formation energy, and suppresses the unfavorable variants. When the favorable variants are selected at the initial stages of monoclinic growth, the system arranges the variants in a way that provides the maximum strain accommodation. Phase-field simulation and experimental studies [1,2,73] show that surface uplifts are locally constituted by a set of four variants which have $\{100\}_t$ and $\{110\}_t$ junction planes. The junction planes of these variants are all perpendicular to the free surface, so that the overall long-range lateral stress is almost totally suppressed. Fig. 6 shows a comparison between a phase-field simulation result and an AFM micrograph of surface relief resulting from the martensitic $\mathrm{T} \rightarrow \mathrm{M}$ transformation in zirconia [1]. The cross-section of the experimental picture is not perfectly rectangular because $c_t$ is a slightly tilted with respect to the surface normal.

Fig. 7 shows the arrangement of monoclinic variants both in the inside and on the outside of the tetragonal crystal. Habit planes, interfaces between the matrix and the martensite, remain unchanged during the transformation. The other interfaces which form between different martensite variants are junction planes. These junction planes are of the kind $\{100\}_t$ or $\{110\}_t$ and their triple junction line is along $[100]_l$. The same results have been shown in experimental works [74-76].

Another common phenomenon in the $\mathrm{T} \rightarrow \mathrm{M}$ transformation in zirconia is variant impingement. Variant impingement can happen when the translation along one axis, e.g. $a_t$ in our case, is large enough. The cause of variant impingement formation is the autocatalytic nature of

![](./images/814659497862627328_9.jpg)

Fig. 8. Variants impingement in $T \to M$ transformation. Phase-field model (left) and AFM micrograph (right) [1].

martensitic transformations. When a monoclinic lath forms, it imposes a very large shear strain (16%) and vol- ume increase (4%) on the surrounding zone of transformed material. This back-stress may pile up and stop the phase transformation or may trigger another transformation in neighboring matrix. The formation of new martensite laths due to the imposed internal stresses of neighboring growing martensite is called autocatalytic transformation. It is worth noting that the formation of self-accommodating variant pairs reduces the long-range overall shear strain, because the shear strains of the variant pairs are opposite and equal. A comparison between phase-field simulation and an AFM micrograph of the formation of variant impingement is shown in Fig. 8.

## 6. Conclusion
We presented a 3-D phase-field model to capture the effect of variant strain accommodation on the formation of complex microstructures during the $T \to M$ transformation in zirconia. We assigned 12 order parameters to 12 possible monoclinic variants. Linear elastic incompatibility was considered between the two allotropic variants, tetragonal and monoclinic, as well as between the different variants of the monoclinic phase. By considering all the possible monoclinic variants in the formulation, the phase-field model reproduced the experimentally observed microstructural patterns, including all the main crystallographic, kinetic and morphological features.

For the case that the $(001)_{t}$ lattice plane coincides with the free surface, the results showed that only variants of correspondence $C$ could grow, resulting in a surface uplift constituted of four monoclinic variants. The results also demonstrate the formation of junction planes from the families of $\{100\}_{t},\{110\}_{t}$. During phase transformation, all the habit planes and the junction planes remained unchanged. The model was also able to predict the formation of variant impingement phenomena, which are commonly observed in the $T \to M$ transformation in zirconia.

## Acknowledgements
The authors appreciate the sponsorship of the Institute for Nuclear Energy Science and Technology Laboratory Directed Research and Development (INEST LDRD) and the Center for Advanced Vehicular Systems at Mississippi State University.

## References
[1] S. Deville, G. Guénin, J. Chevalier, Acta Mater. 52 (2004) 5697.

[2] S. Deville, G. Guénin, J. Chevalier, Acta Mater. 52 (2004) 5709.

[3] J. Chevalier, L. Gremillard, A.V. Virkar, D.R. Clarke, J. Am. Ceram. Soc. 92 (2009) 1901.

[4] H. Weidinger, Raman spectroscopy study of the tetragonal-to-monoclinic transition in zirconium oxide scales and determination of overall oxygen diffusion by nuclear microanalysis of O18, Zircon. Nucl. Ind. Proc. Int. Conf., vol. 9, ASTM, 1991.

[5] R.H.J. Hannink, P.M. Kelly, B.C. Muddle, J. Am. Ceram. Soc. 83 (2000) 461.

[6] M. Mamivand, M. Asle Zaeem, H. El Kadiri, Acta Mater. 64 (2014) 208.

[7] W.Z. Zhu, Ceram. Int. 22 (1996) 389.

[8] R.C. Garvie, M.V. Swain, J. Mater. Sci. 20 (1985) 1193.

[9] R.C. Garvie, J. Mater. Sci. 20 (1985) 3479.

[10] A. Suresh, M.J. Mayo, W.D. Porter, J. Mater. Res. 18 (2003) 2912.

[11] W. Qin, C. Nam, H. Li, J. Szpunar, Acta Mater. 55 (2007) 1695.

[12] G.K. Bansal, A.H. Heuer, Acta Metall. 22 (1974) 409.

[13] W.M. Kriven, W.L. Fraser, S.W. Kennedy, The martensite crystallography of tetragonal zirconia, in: Sci. Technol. Zirconia Proc. 1st Int. Conf., Cleveland, OH, 1980, Adv. Ceram., vol. 3, 1980.

[14] P.M. Kelly, C.J. Ball, J. Am. Ceram. Soc. 69 (1986) 259.

[15] B.C. Muddle, R.H. Hannink, J. Am. Ceram. Soc. 69 (1986) 547.

[16] N. Navruz, Phys. Met. Metallogr. 105 (2008) 580.

[17] P.M. Kelly, L. Francis Rose, Prog. Mater. Sci. 47 (2002) 463.

[18] I. Loginova, J. Odqvist, G. Amberg, J. Ågren, Acta Mater. 51 (2003) 1327.

[19] Y. Jin, A. Artemev, A. Khachaturyan, Acta Mater. 49 (2001) 2309.

[20] N. Moelans, B. Blanpain, P. Wollants, Calphad 32 (2008) 268.

[21] W.J. Boettinger, J.A. Warren, C. Beckermann, A. Karma, Annu. Rev. Mater. Res. 32 (2002) 163.

[22] M. Asle Zaeem, H. Yin, S.D. Felicelli, Appl. Math. Model. 37 (2013) 3495.

[23] S. Wang, M.A. Zaeem, M.F. Horstemeyer, P.T. Wang, Mater. Technol. 27 (2012) 355.

[24] M.A. Zaeem, H. Yin, S.D. Felicelli, J. Mater. Sci. Technol. 28 (2012) 137.

[25] L.Q. Chen, Annu. Rev. Mater. Res. 32 (2002) 113.

[26] M.A. Zaeem, S.D. Mesarovic, J. Comput. Phys. 229 (2010) 9135.

[27] M.A. Zaeem, H.E. Kadiri, S.D. Mesarovic, M.F. Horstemeyer, P.T. Wang, J. Phase Equilibria Diffus. 32 (2011) 302.

[28] M.A. Zaeem, S.D. Mesarovic, Comput. Mater. Sci. 50 (2011) 1030.

[29] M. Asle Zaeem, H. El Kadiri, P.T. Wang, M.F. Horstemeyer, Comput. Mater. Sci. 50 (2011) 2488.

[30] R. Spatschek, M. Hartmann, E. Brener, H. Müller-Krumbhaar, K. Kassner, Phys. Rev. Lett. 96 (2006) 015502.

[31] M. Mamivand, M.A. Zaeem, H. El Kadiri, Comput. Mater. Sci. 77 (2013) 304.

[32] L.D. Landau, Collected Papers of L.D. Landau, Pergamon Press, Oxford, 1965.

[33] R. Ahluwalia, T. Lookman, A. Saxena, R.C. Albers, Acta Mater. 52 (2004) 209.

[34] R. Ahluwalia, T. Lookman, A. Saxena, Phys. Rev. Lett. 91 (2003) 55501.

[35] G.R. Barsch, J.A. Krumhansl, Phys. Rev. Lett. 53 (1984) 1069.

[36] Y.W. Cui, T. Koyama, I. Ohnuma, K. Oikawa, R. Kainuma, K. Ishida, Acta Mater. 55 (2007) 233.

[37] R.P. Dhote, R.V.N. Melnik, J. Zu, Comput. Mater. Sci. 63 (2012) 105.

[38] O. Shchyglo, U. Salman, A. Finel, Acta Mater. 60 (2012) 6784.

[39] A. Artemev, Y. Jin, A. Khachaturyan, Acta Mater. 49 (2001) 1165.

[40] A. Artemev, Y. Wang, A. Khachaturyan, Acta Mater. 48 (2000) 2503.

[41] A. Malik, G. Amberg, A. Borgenstam, J. Ågren, Acta Mater. 61 (2013) 7868.

[42] A. Malik, H.K. Yeddu, G. Amberg, A. Borgenstam, J. Ågren, Mater. Sci. Eng. A, Struct. Mater. 556 (2012) 221.

[43] J. Man, J. Zhang, Y. Rong, N. Zhou, Metall. Mater. Trans. A 42 (2011) 1154.

[44] H. She, Y. Liu, B. Wang, Int. J. Solids Struct. 50 (2013) 1187.

[45] Y. Wang, A. Khachaturyan, Acta Mater. 45 (1997) 759.

[46] H.K. Yeddu, T. Lookman, A. Saxena, Acta Mater. 61 (2013) 6972.

[47] J.Y. Cho, A.V. Idesman, V.I. Levitas, T. Park, Int. J. Solids Struct. (2012)

[48] A.V. Idesman, J.Y. Cho, V.I. Levitas, Appl. Phys. Lett. 93 (2008) 043102.

[49] V.I. Levitas, D.L. Preston, Phys. Rev. B 66 (2002) 134206.

[50] V.I. Levitas, D.L. Preston, Phys. Rev. B 66 (2002) 134207.

[51] V.I. Levitas, D.W. Lee, D.L. Preston, Int. J. Plast. 26 (2010) 395.

[52] V.I. Levitas, Int. J. Plast. 49 (2013) 85.

[53] M. Mamivand, M. Asle Zaeem, H. El Kadiri, Int. J. Plast. 60 (2014) 71.

[54] M. Mamivand, M. Asle Zaeem, H. El Kadiri, L.-Q. Chen, Acta Mater. 61 (2013) 5223.

[55] T. Sakuma, Trans. Jpn. Inst. Met. 29 (1988) 879.

[56] G. Wolten, J. Am. Ceram. Soc. 46 (1963) 418.

[57] C. Wang, M. Zinkevich, F. Aldinger, J. Am. Ceram. Soc. 89 (2006) 3751.

[58] W.M. Kriven, W.L. Fraser, S.W. Kennedy, in: A.H. Heuer, L.W. Hobbs (Eds.), Sci. Technol. Zirconia, American Ceramic Society, Columbus, OH, 1981, p. 82.

[59] M. Hayakawa, K. Adachi, M. Oka, Acta Metall. Mater. 38 (1990) 1753.

[60] M. Hayakawa, N. Kuntani, M. Oka, Acta Metall. 37 (1989) 2223.

[61] M. Hayakawa, M. Oka, Acta Metall. 37 (1989) 2229.

[62] S.M. Allen, J.W. Cahn, Acta Metall. 27 (1979) 1085.

[63] A. Khachaturyan, Theory of Structural Transformations in Solids, John Wiley, New York, 1983.

[64] V.I. Levitas, Int. J. Plast. 16 (2000) 805.

[65] T. Mura, Micromechanics of Defects in Solids, vol. 3, Springer Verlag, Berlin, 1987.

[66] N.K. Simha, J. Mech. Phys. Solids 45 (1997) 261.

[67] COMSOL Multiphysics Users' Guide, COMSOL Inc., 2012.

[68] E.C. Subbarao, H.S. Maiti, K.K. Srivastava, Phys. Status Solidi A 21 (1974) 9.

[69] X.-S. Zhao, S.-L. Shang, Z.-K. Liu, J.-Y. Shen, J. Nucl. Mater. 415 (2011) 13.

[70] S.K. Chan, Y. Fang, M. Grimsditch, Z. Li, M.V. Nevitt, W.M. Robertson, E.S. Zouboulis, J. Am. Ceram. Soc. 74 (1991) 1742.

[71] X.S. Zhao, S.L. Shang, Z.K. Liu, J.Y. Shen, J. Nucl. Mater. (2011)

[72] E.H. Kisi, C.J. Howard, J. Am. Ceram. Soc. 81 (1998) 1682.

[73] S. Deville, J. Chevalier, H. El Attaoui, J. Am. Ceram. Soc. 88 (2005) 1261.

[74] J.E. Bailey, R. Proc, Soc. Lond. Ser. Math. Phys. Sci. 279 (1964) 395.

[75] J.M. Fernandez, M.J. Melendo, A.D. Rodriguez, A.H. Heuer, M. Hayakawa, J. Am. Ceram. Soc. 77 (1994) 57.

[76] G.K. Bansal, A.H. Heuer, Acta Metall. 20 (1972) 1281.