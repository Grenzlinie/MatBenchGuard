RESEARCH NOTE

# Reduction of the general fracture compliance matrix $\boldsymbol{Z}$ to only five independent elements

Eduard Berg, $^{1}$ Julie A. Hood $^{2}$ and Gerard J. Fryer $^{1}$
$^{1}$ School of Ocean \& Earth Science \& Technology, University of Hawaii at Manoa, Honolulu, HI 96822, USA
$^{2}$ Naval Research Laboratory, Code 6380, Washington, DC 20375-5000, USA

Accepted 1991 June 6. Received 1991 June 6; in original form 1990 December 31

## SUMMARY
In a system of plane parallel fractures, it is often assumed that resistance to slip on the fractures is independent of the direction of that slip. The fracture system then is transversely isotropic in its elastic properties and can be characterized by just two numbers: the compliances normal and tangential to the fractures, for example. But any relief on the fracture surfaces will destroy the symmetry and demand additional elastic constants. In general, a system of plane parallel fractures has a $3 \times 3$ matrix $\boldsymbol{Z}$ of fracture compliances which contributes to the overall $6 \times 6$ compliance matrix $\boldsymbol{S}$ of the fractured solid. For transversely isotropic fractures $\boldsymbol{Z}$ has only two independent elements, but for general fractures all that is known is that $\boldsymbol{Z}$ must be symmetric. This implies that six parameters are needed to describe a fracture system with triclinic behaviour. We find, however, that there is always a coordinate rotation which sets a symmetric pair of the off-diagonal terms of $\boldsymbol{Z}$ to zero, so $\boldsymbol{Z}$ has, in fact, only five independent elements. The zeros of the rotated $\boldsymbol{Z}$ show that particle displacements tangential to the fractures and parallel to the new coordinate axes are decoupled from each other. Despite this decoupling, the medium is still fully triclinic because displacement normal to the fractures still couples with all the other displacements.

Key words: anisotropy, fracture compliance, fractures.

## INTRODUCTION
As the resolution of seismic measurements improves, it is becoming increasingly apparent that much of the Earth's crust displays direction-dependent velocities, primarily because of aligned fractures or microcracks. Backus (1962) recognized that thin layers of isotropic materials or oriented microcracks would appear anisotropic when measured with seismic waves long compared to the scale of the structures. The long-wavelength theory evolved based on a stiffness formulation

$$
\boldsymbol{\sigma}=\boldsymbol{C} \boldsymbol{\epsilon} \tag{1}
$$

(Schoenberg 1983; Schoenberg & Douma 1988; Schoenberg & Muir 1989; Hood & Schoenberg 1989), but a method which is mathematically much more concise can be developed for the compliance formulation of Hooke's Law,

$$
\boldsymbol{\epsilon}=\boldsymbol{S} \boldsymbol{\sigma} \tag{2}
$$

(Nichols, Muir & Schoenberg 1989; Hood 1991).

Using this compliance formulation, we consider here anisotropy resulting from a single plane parallel fracture system. The seismically measurable quantity of a fractured rock is the compliance matrix $\boldsymbol{S}$ which has contributions from both the fracture compliance and from the compliance of the unfractured host rock. Fortunately, we can avoid consideration of any intrinsic anisotropy of the host rock, as it is relatively simple to decompose $\boldsymbol{S}$ into its fracture and host-rock components (Hood 1991), so we can concentrate just on the compliance properties of the fracture system.

The most familiar system of plane parallel fractures is the most highly symmetric: the transversely isotropic (= hexagonally symmetric) system which results when the resistance to slip on the fractures is independent of the direction of that slip. The fracture system response is then invariant with respect to rotation about the fracture normal. As is well known, when the host rock for such a fracture system is isotropic, the overall symmetry is itself transversely isotropic. While description of the elastic response of a transversely isotropic medium in general


704  E. Berg, J. A. Hood and G. J. Fryer

requires five elastic parameters, when anisotropy results from such a symmetric fracture system only four of the elastic parameters are independent (Schoenberg & Douma 1988). In this paper we seek to find the number of independent parameters needed to describe fracture systems of arbitrary symmetry.

The most general fracture system is one in which the fracture compliance is triclinic. While truly triclinic fracture systems (i.e., those that do not collapse to higher symmetry) are probably extremely rare, it is clear that we have to consider lower symmetry systems than hexagonal. For example, if fracture surfaces are striated, tangential fracture compliance will be greater parallel to the striations than perpendicular to them, and the fracture compliance will be orthorhombic. If the striations on one fracture surface are laterally offset from those on the opposite surface, any fracture closure will tend to reduce the offset; displacements normal and parallel to the fractures will be coupled. The fracture system will then display monoclinic symmetry (Schoenberg & Douma 1988). For generality, we consider triclinic systems here.

Parallel fractures of completely general triclinic symmetry can be described by a $3 \times 3$ symmetric compliance matrix, $\boldsymbol{Z}$, implying that six different elements are independent (Schoenberg 1980). The goal of this paper is simple: to show that at most only five of those elements are independent. This appears to be a new result, although we note that Gibson & Ben-Menahem (1990) mention a five-element $\boldsymbol{Z}$ en passant.

# REDUCTION OF THE Z MATRIX

Reduction of the $\boldsymbol{Z}$ matrix can be accomplished by a simple rotation of the coordinate system around the axis normal to the fracture planes. There is always a rotation for which two of the elements in the symmetric matrix $\boldsymbol{Z}$ become zero. To show this we partition the compliance matrix $\boldsymbol{S}$ into submatrices $\boldsymbol{S}_{\mathrm{N}}$ and $\boldsymbol{S}_{\mathrm{T}}$ describing compliances normal and tangential to the fractures, and cross compliances $\boldsymbol{S}_{\mathrm{TN}}$. As shown in the Appendix, fractures make no contribution to either $\boldsymbol{S}_{\mathrm{T}}$ or $\boldsymbol{S}_{\mathrm{TN}}$. This makes it possible to find the compliances of a fractured medium from given properties of the unfractured medium and of the fractures themselves simply by transforming the properties of the elastic background material into the coordinate system oriented by the fractures, adding in the corresponding fracture compliance $\boldsymbol{Z}$ (which contributes only to the $\boldsymbol{S}_{\mathrm{N}}$ submatrix), and transforming the combined compliances back into the original observation coordinates (Nichols *et al.* 1989; Hood & Schoenberg 1989; Hood 1991).

A remarkable property of $\boldsymbol{S}$ is that under a coordinate rotation about the axis normal to the fractures, the submatrix $\boldsymbol{S}_{\mathrm{N}}$ is constrained to the same submatrix space. As we shall show, it is this property which guarantees the existence of a rotation angle for which the symmetric fracture matrix, $\boldsymbol{Z}'$ (the rotated $\boldsymbol{Z}$), has two symmetric zero elements. As a consequence, there are only five independent elements in $\boldsymbol{Z}$.

Without a loss of generality, we choose the $x_3$ axis of a Cartesian system to be normal to the $x_1x_2$ fracture plane, as shown in Fig. 1. The change in the compliance caused by the introduction of fractures is given by the matrix $\boldsymbol{S}_{\mathrm{f}}$ in terms of

![](./images/812004586154885121_1.jpg)

Figure 1. Geometry of the coordinate system. The $x_3$ axis is perpendicular to the fracture planes (shaded) and the coordinate system is rotated about this axis to find the zeros of $\boldsymbol{Z}$. Fracture compliance normal to the fracture planes is $Z_{\mathrm{N}}$, while $Z_1$, $Z_2$ are the tangential fracture compliances parallel to $x_1$ and $x_2$ axes.

the six $\boldsymbol{Z}$ elements,

$$
\boldsymbol{S}_{\mathrm{f}}=\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & Z_{33} & Z_{23} & Z_{13} & 0 \\
0 & 0 & Z_{23} & Z_{22} & Z_{12} & 0 \\
0 & 0 & Z_{13} & Z_{12} & Z_{11} & 0 \\
0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix} \tag{3}
$$

(Nichols *et al.* 1989). Following the established convention, we denote the fracture compliance normal to the fractures by $Z_{\mathrm{N}}$, and the tangential compliances parallel to $x_1$ and $x_2$ axes by $Z_1$ and $Z_2$ (i.e., we choose $Z_{33} \equiv Z_{\mathrm{N}}$, $Z_{22} \equiv Z_2$, $Z_{11} \equiv Z_1$). A coordinate rotation about the $x_3$ axis (normal to the fracture planes) by an angle $\phi$ yields the fracture compliance matrix $\boldsymbol{S}_{\mathrm{f}}'$ in the rotated system $(x_1', x_2', x_3'=x_3)$,

$$
\boldsymbol{S}_{\mathrm{f}}'=\boldsymbol{N} \boldsymbol{S}_{\mathrm{f}} \boldsymbol{N}^{\mathrm{T}}=\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & Z_{\mathrm{N}}' & Z_{23}' & Z_{13}' & 0 \\
0 & 0 & Z_{23}' & Z_{2}' & Z_{12}' & 0 \\
0 & 0 & Z_{13}' & Z_{12}' & Z_{1}' & 0 \\
0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}, \tag{4}
$$

where the elements of $\boldsymbol{Z}'$ are (with $c = \cos \phi$, $s = \sin \phi$),

$$
Z_{\mathrm{N}}'=Z_{\mathrm{N}}, \tag{5a}
$$

$$
Z_{2}'=c^{2} Z_{2}+s^{2} Z_{1}-2 c s Z_{12}, \tag{5b}
$$

$$
Z_{1}'=s^{2} Z_{2}+c^{2} Z_{1}+2 c s Z_{12}, \tag{5c}
$$

$$
Z_{23}'=c Z_{23}-s Z_{13}, \tag{5d}
$$

$$
Z_{13}'=s Z_{23}+c Z_{13}, \tag{5e}
$$

$$
Z_{12}'=c s\left(Z_{2}-Z_{1}\right)+\left(c^{2}-s^{2}\right) Z_{12}. \tag{5f}
$$

Since this discussion began by assuming that all $Z_{ij} \neq 0$, a rotation angle $-\pi / 2 < \phi < \pi / 2$ around the $x_3$ axis can always be determined such that one of the three off-diagonal $Z_{ij}'$ becomes zero in equations (5). The angle $\phi$ can therefore be found by setting $Z_{23}'$, $Z_{13}'$, or $Z_{12}'$ to zero.

If
$$
Z_{23}^{\prime}=0, \quad \frac{Z_{23}}{Z_{13}}=\frac{s}{c} ; \tag{6a}
$$
if
$$
Z_{13}^{\prime}=0, \quad \frac{Z_{23}}{Z_{13}}=\frac{-c}{s} ; \tag{6b}
$$
and if
$$
Z_{12}^{\prime}=0, \quad \frac{Z_{2}-Z_{1}}{Z_{12}}=\frac{s}{c}-\frac{c}{s}. \tag{6c}
$$

Obviously (6a) and (6b) are interdependent and define the two perpendicular solutions $\phi_{\mathrm{a}}$ for (6a) and $\phi_{\mathrm{b}}$ for (6b) such that $\phi_{\mathrm{b}}=\phi_{\mathrm{a}} \pm \pi / 2$. Either will reduce the six different elements in $\boldsymbol{Z}$ to five independent $\boldsymbol{Z}^{\prime}$ elements. It is more aesthetic, however, to seek the more symmetric solution for $Z_{12}^{\prime}=0$, from (6c).

Two rotations about $x_{3}, \phi_{1}$ and $\phi_{2}$, will satisfy (6c). We find
$$
\tan \phi_{2}<0<\tan \phi_{1}, \quad -\frac{\pi}{2}<\phi_{2}<0<\phi_{1}<\frac{\pi}{2}, \tag{7}
$$
with
$$
\phi_{2}=\phi_{1}-\frac{\pi}{2}.
$$

For
$$
\frac{Z_{2}-Z_{1}}{Z_{12}}<0, \quad 0<\phi_{1}<\frac{\pi}{4} ; \tag{8}
$$
$$
\frac{Z_{2}-Z_{1}}{Z_{12}}>0, \quad \frac{\pi}{4}<\phi_{1}<\frac{\pi}{2}. \tag{9}
$$

Note that for $Z_{2}=Z_{1}, \phi_{1}=\pi / 4$. When $Z_{12}^{\prime} \equiv 0$, the diagonal $\boldsymbol{Z}^{\prime}$ elements are
$$
Z_{\mathrm{N}}^{\prime}=Z_{\mathrm{N}}, \tag{10a}
$$
$$
Z_{2}^{\prime}=Z_{2}-Z_{12} \frac{s}{c}=Z_{1}-Z_{12} \frac{c}{s}, \tag{10b}
$$
and
$$
Z_{1}^{\prime}=Z_{1}+Z_{12} \frac{s}{c}=Z_{2}+Z_{12} \frac{c}{s}. \tag{10c}
$$

We shall next show that if we choose $\phi$ such that $Z_{12}^{\prime}=0$, shear waves in the $x_{1}^{\prime} x_{3}^{\prime}$ plane do not involve the shear stress $\sigma_{23}^{\prime}$, while shear waves in the $x_{2}^{\prime} x_{3}^{\prime}$ plane are independent of $\sigma_{13}^{\prime}$. The primed coordinate system is therefore a principal axis system for the oriented fractures. We call this coordinate system the eigensystem.

## S-WAVE DECOUPLING IN THE EIGENCOORDINATES OF $\boldsymbol{Z}$
In any coordinate system, the global compliance matrix is the sum of both background material compliances $\mathbf{S}_{\mathrm{b}}$ and fracture compliances $\mathbf{S}_{\mathrm{f}}$. In particular, in the fracture eigensystem (the primed system), we can write
$$
\mathbf{S}^{\prime}=\mathbf{S}_{\mathrm{b}}^{\prime}+\mathbf{S}_{\mathrm{f}}^{\prime}. \tag{11}
$$

We are here specifically interested in the effects of the fracture compliances, so for simplicity, we now restrict ourselves to the eigensystem and drop the primes.

The fracture-generated contribution to the total strains are
$$
\boldsymbol{\epsilon}_{\mathrm{f}}=\mathbf{S}_{\mathrm{f}} \boldsymbol{\sigma}, \tag{12}
$$
where $\mathbf{S}_{\mathrm{f}}$ has the structure of equation (3). The 3 -vector of non-zero strains in $\boldsymbol{\epsilon}_{\mathrm{f}}$ is
$$
\boldsymbol{\epsilon}_{\mathrm{N}}=\mathbf{Z} \boldsymbol{\sigma}_{\mathrm{N}}, \tag{13}
$$
where
$$
\mathbf{Z}=\left(\begin{array}{ccc}
Z_{\mathrm{N}} & Z_{23} & Z_{13} \\
Z_{23} & Z_{2} & 0 \\
Z_{13} & 0 & Z_{1}
\end{array}\right). \tag{14}
$$

Using the notation $u_{i, j} \equiv \partial u_{i} / \partial x_{j}$, where $\mathbf{u}$ is displacement, equation (13) becomes
$$
\begin{aligned}
\epsilon_{33} & =u_{3,3}=Z_{\mathrm{N}} \sigma_{33}+Z_{23} \sigma_{23}+Z_{13} \sigma_{13}, \\
2 \epsilon_{23} & =u_{2,3}+u_{3,2}=Z_{23} \sigma_{33}+Z_{2} \sigma_{23}, \\
2 \epsilon_{13} & =u_{1,3}+u_{3,1}=Z_{13} \sigma_{33}+Z_{1} \sigma_{13}.
\end{aligned} \tag{15}
$$

It is important to note here that $\mathbf{u}$ is not the total displacement but the additional displacement imparted by the fractures.

In equations (15) the $u_{i, j}$ correspond to displacements in the $i$ direction which change along the $j$ coordinate, i.e., $u_{3,3}$ is a compressional wave propagating in the $x_{3}$ direction. The $u_{i, j}$ for $i \neq j$ are the shear waves polarized in the $i$ direction which propagate in the $j$ direction. Equations (15) therefore show that the fracture system contributes the following additional motions.

(a) A $P$-wave, $u_{3,3}$, which propagates perpendicular to the fracture planes in the $x_{3}$ direction. This $P$-wave has contributions from all three stresses, $\sigma_{i 3}$, which act on the fracture planes.

(b) A shear wave, $u_{2,3}+u_{3,2}$, with motion in the $x_{2} x_{3}$ plane and which propagates in that same plane. It is independent of the stress $\sigma_{13}$ perpendicular to its polarization-propagation plane.

(c) A shear wave, $u_{1,3}+u_{3,1}$, with motion in the $x_{1} x_{3}$ plane which propagates in that same plane [i.e., perpendicular to the shear wave plane described in (b)]. It is independent of $\sigma_{23}$, the stress in the plane perpendicular to its propagation-polarization plane.

## CONCLUSIONS
Only five of the elements in the fracture compliance matrix $\boldsymbol{Z}$ are independent for triclinic fracture systems, as can be shown by rotating coordinates so that any of the $Z_{i j}$ with $i \neq$ $j$ is zero. The most elegant choice is the eigensystem defined by $Z_{i j}=0$ for which the $x_{i}$ and $x_{j}$ directions are both in the fracture planes. For fracture planes perpendicular to $x_{3}$ this choice gives $Z_{12}=0$. In this system the additional motion resulting from the fracture compliances is conveniently summarized:

(a) compressional motion propagating in the $x_{3}$ direction (perpendicular to the fracture planes);

(b) shear motion polarized and propagating in the $x_{1} x_{3}$ plane; and
(c) shear motion polarized and propagating in the $x_{2} x_{3}$ plane.

The additional compressional motion depends on all three stress components, $\sigma_{i 3}$, acting on the fracture plane. The additional shear wave motions are independent of shear stresses in the planes normal to their respective polarization-propagation planes (i.e., the $x_{1} x_{3} S$ motion is independent of $\sigma_{23} ; x_{2} x_{3} S$ motion is independent of $\sigma_{13}$).

It is worth considering the overall symmetry of a rock with embedded triclinic fractures. If the background is isotropic (two elastic constants) it is simple to show, using equation (11), that the resulting fractured rock has seven independent elastic constants. Despite this small number of parameters, the elastic response does not collapse to any higher symmetry system; the fractured rock is, in general, triclinic.

## ACKNOWLEDGMENTS
This work was supported partially by the National Science Foundation under grant OCE-8711646. We thank both Stuart Crampin and an unknown reviewer for pointing out that, as originally written, this paper appeared to promote a trivial result. Julie Hood is supported as a Research Associate by the US National Research Council. SOEST contribution no. 2609.

## REFERENCES
Auld, B. A., 1973. *Acoustic Fields and Waves in Solids*, vol. 1, Wiley, New York.
Backus, G. E., 1962. Long-wave anisotropy produced by horizontal layering, *J. geophys. Res.*, **66**, 4427-4440.
Gibson, R. L. & Ben-Menahem, A., 1990. Elastic wave scattering by anisotropic obstacles: applications to fractured volumes, *EOS, Trans. Am. geophys. Un.*, **71**, 559.
Hood, J. A., 1991. A simple method for decomposing fracture-induced anisotropy, *Geophysics*, **56**, 1275-1279.
Hood, J. A. & Schoenberg, M., 1989. Estimation of vertical fracturing from measured elastic moduli, *J. geophys. Res.*, **94**, 15611-15618.
Nichols, D., Muir, F. & Schoenberg, M., 1989. Elastic properties of rocks with multiple sets of fractures, *59th Ann. Int. Meeting, Soc. Exploration Geophysicists, Expanded Abstracts*, pp. 471-474.
Schoenberg, M., 1980. Elastic wave behavior across linear slip interfaces, *J. acoust. Soc. Am.*, **68**, 1516-1521.
Schoenberg, M., 1983. Reflection of elastic waves from periodically stratified media with interfacial slip, *Geophys. Prosp.*, **31**, 265-292.
Schoenberg, M. & Douma, J., 1988. Elastic wave propagation in media with parallel fractures and aligned cracks, *Geophys. Prosp.*, **36**, 571-590.
Schoenberg, M. & Muir, F., 1989. A calculus for finely layered anisotropic media, *Geophysics*, **54**, 581-589.

## APPENDIX
### Compliance formulation of the Schoenberg & Muir calculus
We give here a brief outline of the compliance formulation for long-wavelength behaviour of a layered/fractured medium. To obtain Hooke's Law in the matrix form (2) we use the standard abbreviated subscripts for strain and stress, so that in abbreviated and normal notation
$$
\begin{aligned}
& \boldsymbol{\epsilon}=\left(\epsilon_{1}, \epsilon_{2}, \epsilon_{3}, \epsilon_{4}, \epsilon_{5}, \epsilon_{6}\right)^{\mathrm{T}} \equiv\left(\epsilon_{11}, \epsilon_{22}, \epsilon_{33}, 2 \epsilon_{23}, 2 \epsilon_{13}, 2 \epsilon_{12}\right)^{\mathrm{T}}, \\
& \boldsymbol{\sigma}=\left(\sigma_{1}, \sigma_{2}, \sigma_{3}, \sigma_{4}, \sigma_{5}, \sigma_{6}\right)^{\mathrm{T}} \equiv\left(\sigma_{11}, \sigma_{22}, \sigma_{33}, \sigma_{23}, \sigma_{13}, \sigma_{12}\right)^{\mathrm{T}}
\end{aligned}
$$
(Auld 1973).

Consider a stack of plane, parallel, homogeneous, isotropic layers, with layer $i$ of thickness $h_{i}$, where $h_{i}$ is small compared to a seismic wavelength. The propagation of elastic waves across an interface between two layers in welded contact requires continuity of all displacement and stress components. Under the long-wavelength assumption the boundary conditions require that all interface stress components normal to the layers, $\boldsymbol{\sigma}_{\mathrm{N}}$, be identical, while all tangential interface stress components, $\boldsymbol{\sigma}_{\mathrm{T}_{i}}$, be continuous (Schoenberg & Douma 1988). The long-wavelength assumption further means that the layers move together. Therefore the tangential strains, $\boldsymbol{\epsilon}_{\mathrm{T}}$, are the same in all layers (Schoenberg & Douma 1988) and normal displacement is continuous across the interfaces.

These long-wavelength boundary conditions make it convenient to rewrite Hooke's law, equation (2), in the form
$$
\boldsymbol{\epsilon}_{\mathrm{T}}=\mathbf{S}_{\mathrm{T}} \boldsymbol{\sigma}_{\mathrm{T}}+\mathbf{S}_{\mathrm{TN}} \boldsymbol{\sigma}_{\mathrm{N}}, \quad \text { (A2a) }
$$

$$
\boldsymbol{\epsilon}_{\mathrm{N}}=\mathbf{S}_{\mathrm{TN}}^{\mathrm{T}} \boldsymbol{\sigma}_{\mathrm{T}}+\mathbf{S}_{\mathrm{N}} \boldsymbol{\sigma}_{\mathrm{N}} \quad \text { (A2b) }
$$
(Nichols *et al.* 1989; Hood 1991), where
$$
\boldsymbol{\epsilon}_{\mathrm{T}}=\left(\begin{array}{l}
\epsilon_{1} \\
\epsilon_{2} \\
\epsilon_{6}
\end{array}\right), \quad \boldsymbol{\epsilon}_{\mathrm{N}}=\left(\begin{array}{l}
\epsilon_{3} \\
\epsilon_{4} \\
\epsilon_{5}
\end{array}\right), \quad \boldsymbol{\sigma}_{\mathrm{T}}=\left(\begin{array}{l}
\sigma_{1} \\
\sigma_{2} \\
\sigma_{6}
\end{array}\right), \quad \boldsymbol{\sigma}_{\mathrm{N}}=\left(\begin{array}{l}
\sigma_{3} \\
\sigma_{4} \\
\sigma_{5}
\end{array}\right).
$$

Each $\mathbf{S}_{\mathrm{T}}, \mathbf{S}_{\mathrm{N}}, \mathbf{S}_{\mathrm{TN}}$ is a $3 \times 3$ submatrix of $\mathbf{S}$; each submatrix is constant in a particular layer $i$.

We now expand the stack of layers to a periodic structure of period $H=\sum h_{i}$, where $H$ is small compared to a seismic wavelength so we are still in the long-wavelength realm. Our goal now is to determine bulk elastic properties for the periodic structure. We attempt this by seeking the relationship between the long-wavelength average tangential stress $\overline{\boldsymbol{\sigma}}_{\mathrm{T}}$ and normal strain $\overline{\boldsymbol{\epsilon}}_{\mathrm{N}}$ in terms of the constants $\boldsymbol{\epsilon}_{\mathrm{T}}$ and $\boldsymbol{\sigma}_{\mathrm{N}}$.

Since $\boldsymbol{\epsilon}_{\mathrm{T}}$ and $\boldsymbol{\sigma}_{\mathrm{N}}$ are constant in all layers, equation (A2a) results in
$$
\boldsymbol{\sigma}_{\mathrm{T}_{i}}=\mathbf{S}_{\mathrm{T}_{i}}^{-1} \boldsymbol{\epsilon}_{\mathrm{T}}-\mathbf{S}_{\mathrm{T}_{i}}^{-1} \mathbf{S}_{\mathrm{TN}_{i}} \boldsymbol{\sigma}_{\mathrm{N}}, \quad \text { (A4a) }
$$
which, on substituting into (A2b) gives
$$
\boldsymbol{\epsilon}_{\mathrm{N}_{i}}=\mathbf{S}_{\mathrm{TN}_{i}}^{\mathrm{T}} \mathbf{S}_{\mathrm{T}_{i}}^{-1} \boldsymbol{\epsilon}_{\mathrm{T}}+\left(\mathbf{S}_{\mathrm{N}_{i}}-\mathbf{S}_{\mathrm{TN}_{i}}^{\mathrm{T}} \mathbf{S}_{\mathrm{T}_{i}}^{-1} \mathbf{S}_{\mathrm{TN}_{i}}\right) \boldsymbol{\sigma}_{\mathrm{N}}. \quad \text { (A4b) }
$$

Since $\boldsymbol{\epsilon}_{\mathrm{T}}$ and $\boldsymbol{\sigma}_{\mathrm{N}}$ are constants, continuity of $\boldsymbol{\sigma}_{\mathrm{T}_{i}}$ and displacements across the interfaces is assured when the contribution of each layer to the average $\overline{\boldsymbol{\sigma}}_{\mathrm{T}}$ and $\overline{\boldsymbol{\epsilon}}_{\mathrm{N}}$ over the thickness $H$ is in proportion to the thicknesses $h_{i}$. Taking such weighted averages of (A4), we obtain
$$
\overline{\boldsymbol{\sigma}}_{\mathrm{T}}=\sum \frac{h_{i}}{H} \mathbf{S}_{\mathrm{T}_{i}}^{-1} \boldsymbol{\epsilon}_{\mathrm{T}}-\sum \frac{h_{i}}{H} \mathbf{S}_{\mathrm{T}_{i}}^{-1} \mathbf{S}_{\mathrm{TN}_{i}} \boldsymbol{\sigma}_{\mathrm{N}}, \quad \text { (A5a) }
$$
and
$$
\overline{\boldsymbol{\epsilon}}_{\mathrm{N}}=\sum \frac{h_{i}}{H} \mathbf{S}_{\mathrm{TN}_{i}}^{\mathrm{T}} \mathbf{S}_{\mathrm{T}_{i}}^{-1} \boldsymbol{\epsilon}_{\mathrm{T}}+\sum \frac{h_{i}}{H}\left(\mathbf{S}_{\mathrm{N}_{i}}-\mathbf{S}_{\mathrm{TN}_{i}}^{\mathrm{T}} \mathbf{S}_{\mathrm{T}_{i}}^{-1} \mathbf{S}_{\mathrm{TN}_{i}}\right) \boldsymbol{\sigma}_{\mathrm{N}} \text {. (A5b) }
$$

Solving (A5a) for $\boldsymbol{\epsilon}_{\mathrm{T}}$ and substituting this into equation (A5b) allows us to express the long-wavelength Hooke's law over the thickness $H$ in the form

$$
\left(\begin{array}{c}
\boldsymbol{\epsilon}_{\mathrm{T}} \\
\bar{\boldsymbol{\epsilon}}_{\mathrm{N}}
\end{array}\right)=\left(\begin{array}{cc}
\overline{\mathbf{S}}_{\mathrm{T}} & \overline{\mathbf{S}}_{\mathrm{TN}} \\
\overline{\mathbf{S}}_{\mathrm{TN}}^{\mathrm{T}} & \overline{\mathbf{S}}_{\mathrm{N}}
\end{array}\right)\left(\begin{array}{c}
\tilde{\boldsymbol{\sigma}}_{\mathrm{T}} \\
\boldsymbol{\sigma}_{\mathrm{N}}
\end{array}\right).\qquad(\mathrm{A}6)
$$

If we define the coefficient of $\boldsymbol{\sigma}_{\mathrm{N}}$ in (A5a) as $\mathbf{B}$, from (A5) and (A6)

$$
\overline{\mathbf{S}}_{\mathrm{T}}=\left(\sum \frac{h_{i}}{H} \mathbf{S}_{\mathrm{T}_{i}}^{-1}\right)^{-1},\qquad(\mathrm{A}7a)
$$

$$
\mathbf{B}=\sum \frac{h_{i}}{H} \mathbf{S}_{\mathrm{T}_{i}}^{-1} \mathbf{S}_{\mathrm{TN}_{i}},\qquad(\mathrm{A}7b)
$$

$$
\overline{\mathbf{S}}_{\mathrm{TN}}=\overline{\mathbf{S}}_{\mathrm{T}} \mathbf{B},\qquad(\mathrm{A}7c)
$$

$$
\overline{\mathbf{S}}_{\mathrm{N}}=\sum \frac{h_{i}}{H} \mathbf{S}_{\mathrm{N}_{i}}-\sum \frac{h_{i}}{H} \mathbf{S}_{\mathrm{TN}_{i}}^{\mathrm{T}} \mathbf{S}_{\mathrm{T}_{i}}^{-1} \mathbf{S}_{\mathrm{TN}_{i}}+\mathbf{B}^{\mathrm{T}} \overline{\mathbf{S}}_{\mathrm{T}} \mathbf{B}.\qquad(\mathrm{A}7d)
$$

The equation for the average density $\bar{\rho}$ is

$$
\bar{\rho}=\sum \frac{h_{i}}{H} \rho_{i}.\qquad(\mathrm{A}7e)
$$

Equations (A7) show that the boundary conditions, using Hooke's law in the compliance form of (2), simply yield the additive group elements $\mathbf{g}_{i}(j)$ of the Schoenberg & Muir calculus (Schoenberg & Muir 1989):

$$
\overline{\mathbf{S}}_{\mathrm{T}}^{-1}=\overline{\mathbf{g}}_{5}=\sum \mathbf{g}_{i}(5);\quad \mathbf{g}_{i}(5)=\frac{h_{i}}{H} \mathbf{S}_{\mathrm{T}_{i}}^{-1},
$$

$$
\mathbf{B}=\overline{\mathbf{g}}_{4}=\sum \mathbf{g}_{i}(4);\quad \mathbf{g}_{i}(4)=\frac{h_{i}}{H} \mathbf{S}_{\mathrm{T}_{i}}^{-1} \mathbf{S}_{\mathrm{TN}_{i}},
$$

$$
\overline{\mathbf{S}}_{\mathrm{N}}-\mathbf{B}^{\mathrm{T}} \overline{\mathbf{S}}_{\mathrm{T}} \mathbf{B}=\overline{\mathbf{g}}_{3}=\sum \mathbf{g}_{i}(3);\qquad(\mathrm{A}8)
$$

$$
\mathbf{g}_{i}(3)=\frac{h_{i}}{H}\left(\mathbf{S}_{\mathrm{N}_{i}}-\mathbf{S}_{\mathrm{TN}_{i}}^{\mathrm{T}} \mathbf{S}_{\mathrm{T}_{i}}^{\mathrm{T}} \mathbf{S}_{\mathrm{TN}_{i}}\right)
$$

$$
\bar{\rho}=\bar{g}_{2}=\sum g_{i}(2);\quad g_{i}(2)=\frac{h_{i}}{H} \rho_{i}.
$$

Equations (A6) and (A7) show that all elastic properties, $\mathbf{S}_{\mathrm{N}_{i}}$, are weighted-summed into $\overline{\mathbf{S}}_{\mathrm{N}}$ and are not coupled into any of the other compliance matrix terms $\overline{\mathbf{S}}_{\mathrm{T}}$ or $\overline{\mathbf{S}}_{\mathrm{TN}}$. The $\mathbf{S}_{\mathrm{N}_{i}}$ determine the strain response $\overline{\boldsymbol{\epsilon}}_{\mathrm{N}}$, normal to an applied stress on a plane perpendicular to the normal, $\boldsymbol{\sigma}_{\mathrm{N}}$. This simple additive form of $\overline{\mathbf{S}}_{\mathrm{N}}$ is what allows a fracture set to be described by such an $\mathbf{S}_{\mathrm{N}}$ submatrix, denoted $\mathbf{Z}$, with a fracture plane perpendicular to the normal.

Although the theory here has been developed for thin layers, fractures are completely analogous (Schoenberg 1980).

<br>