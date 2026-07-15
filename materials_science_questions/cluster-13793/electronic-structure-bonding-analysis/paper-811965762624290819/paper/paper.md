![](./images/811965762624290819_1.jpg)

Available online at www.sciencedirect.com
![](./images/811965762624290819_2.jpg)
Superlattices and Microstructures 43 (2008) 559-563

# Superlattices
and Microstructures
www.elsevier.com/locate/superlattices

# Simulation of band structure for CrN lattices by using a 3D array of range-limited circularly symmetric attractive potential

E. Restrepo-Parra$^{a,}$, S. Amaya-Roncancio$^{a}$, C.M. Bedoya-Hincapie$^{a}$, J.C. Riaño-Rojas$^{b}$

$^{a}$ Grupo de Desarrollo de Nuevos Materiales, Departamento de Física y Química, Universidad Nacional de Colombia, Sede Manizales, Colombia
$^{b}$ Departamento de Matemáticas y Estadística, Universidad Nacional de Colombia, Sede Manizales, Colombia

Available online 7 September 2007

## Abstract
The band structure obtention is important for establishing the different electrical and thermal properties of materials. Band structure of CrN was carried out by employing a 3D array range-limited spherical symmetric potential. For this purpose, several tools of Mathematics package were used. Initially, the unit cell is gridded in order to obtain small parts. Each grid point was well-represented by a wavefunction. The finite differences of each grid point is obtained approximately in each direction (x, y and z), establishing the difference between the neighboring points along the axis. The wavefunctions which are described by the Bloch functions, the Laplacian and the derivatives are included into the Schrödinger equation. Then, the equation is solved in order to obtain the eigenvalues (energies), which are plotted to obtain the band structure in (100), (110) and (111) directions.

© 2007 Elsevier Ltd. All rights reserved.

Keywords: Band structure modeling; Eigenvalues; Eigenfunctions; Griding

## 1. Introduction
Transition metal nitrides have attracted growing attention because of their scientific and technological interest. They are extremely hard; they often crystallize in stable rock-salt-like

* Corresponding author.
E-mail address: erestrepopa@unal.edu.co (E. Restrepo-Parra).

0749-6036/$ - see front matter © 2007 Elsevier Ltd. All rights reserved.
doi:10.1016/j.spmi.2007.07.027

(NaCl-like) or CsCl-like structures. Additionally, they are corrosion resistant and have very high melting points [1]. Many authors have studied band structure of different materials. Lévy et al. present a summary of recent relevant results on the structural, mechanical, electronic and optical properties of fcc TiN, VN, CrN, NbN, W2N, hexagonal MoN, and some ternary nitrides in the form of sputtered thin films [2]. The general methods used in theoretical investigations include the augmented plane wave (APW) method, the linear muffin-tin orbitals (LMTO) method and the extended Huckel tight-binding (EHT) method [3]. One of the most used methods is density functional theory (DFT), which reduces the problem of an electron gas to a problem of one particle moving in an effective potential. DFT considers that the total energy is a function only of the electron density, and the potential is unknown, but it can be handled with approximations. This method has been widely employed for calculating band structure of materials like diamond among others [4]. Total energy must be considered as the addition of different parts like electron kinetic, Hartree, interaction ion-ion, ion-electron energies among others. On the contrary, the advantage of the model proposed here is a simple and easy to implement technique, which can give results similar to those reported, with low computational cost. In our method, the cell is divided into smaller parts that conserve the behaviour of the whole lattice, and the potential depends strongly on the Coulomb interaction of the lattice ions. The reason to choose the CrN for the model is because during the last years, the research interest has turned to it, due to the increasing demand for new materials, which have higher resistance to wear and corrosion [5, 6]. It is interesting to note that CrN has a larger lattice parameter than other nitrides, although $r_{\text{Cr}} < r_{\text{V}}$ and $r_{\text{Cr}} < r_{\text{Ti}}$. A higher degree of ionic bonding for CrN can be assumed than for example VN and TiN. Antiferromagnetic order occurs in CrN below 288 K and at low temperatures CrN is an insulator [7]. Ducastelle and Costa Modeled the band structure of CrN and TiN [8].

The aim of this work is to present a technique for modeling band structures of materials, in this case, CrN, employing finite differences and a high symmetrical and periodical potential. The advantage of this method is that it is easy to implement.

## 2. Theoretical fundamentals

As the general theory shows, the eigenfunctions of the wavefunction obtained by solving the Schrödinger equation have the form of the Bloch functions

$$
\psi(x, y, z)=\exp (\mathrm{i} \mathbf{k} \cdot \mathbf{r}) u_{k}(x, y, z). \tag{1}
$$

Replacing Eq. (1) in Schrödinger equation we obtained

$$
\begin{aligned}
& -\frac{\hbar^{2}}{2 m}\left[\left(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}\right)-2 \mathrm{i} \mathbf{k} \cdot \nabla\right] u_{k}(x, y, z)+V(x, y, z) u_{k}(x, y, z) \\
& \quad=E(k) u_{k}(x, y, z),
\end{aligned} \tag{2}
$$

where $\mathbf{k}=(k_{x}, k_{y}, k_{z})$ is a parameter in the first Brillouin zone of reciprocal space. Physically $k$ is the crystal momentum, that shows the behaviour of the wavefunction between real lattice cells, and $u_{k}$ has the lattice periodicity and shows the probability density in every cell. Since CrN has a FCC lattice, a model for this structure is present, with lattice parameters described by

$$
a_{1}=\frac{a}{2}(\hat{y}+\hat{z}) ; \quad a_{2}=\frac{a}{2}(\hat{x}+\hat{z}) ; \quad a_{3}=\frac{a}{2}(\hat{x}+\hat{y}). \tag{3}
$$

![](./images/811965762624290819_3.jpg)

Fig. 1. (a) Griding of the unit cell, (b) griding of xy plane of the cell, (c) quasi-spherical potential.

## 3. Methodology

Fig. 1(b) shows the parallelepiped of the unitary cell in a 3D griding, and Fig. 1(c) shows xy plane of the same cell gridded and numbered. It is possible to approximate the derivative with respect to x, y, z by the difference between neighboring points along the x, y and z axes. Thus, the derivative with respect to x at any point in the grid, for example point 2 is approximately the difference between the values of 3 and 1 divided into 2d and the derivative with respect to y and z are calculated by the same way.

$$
\partial_{x} u_{2}=\frac{u_{3}-u_{1}}{2 d} ; \quad \partial_{y} u_{2}=\frac{\frac{1}{2}\left(u_{5}+u_{6}\right)-\frac{1}{2}\left(u_{14}+u_{15}\right)}{\sqrt{3} d} ; \quad \partial_{z} u_{2}=\frac{u_{18}-u_{15}}{2 d}. \tag{4}
$$

The Laplacian at point 2, is a bit tricky. Recall that the Laplacian indicates how much the function differs from its average value on surrounding points. With a little bit of work it is possible to show that:

$$
\nabla^{2} u_{2}=\frac{u_{4}-u_{2}}{2 d^{2}}+\frac{u_{9}+u_{10}+u_{11}+u_{12}-u_{1}-2 u_{2}-u_{3}}{6 d^{2}}+\frac{u_{3}-u_{2}}{2 d^{2}}. \tag{5}
$$

Moreover, if it is considered that

$$
u_{i}=\exp \left(\mathbf{G} \cdot \mathbf{r}_{i}\right)=\exp \left(\mathbf{G} \cdot\left(\mathbf{r}_{2 i}+\mathbf{r}_{2}\right)\right). \tag{6}
$$

Being $r_{i}$ the distance from point $i$ to the origin, $r_{2}$, the distance from the point 2 to the origin, and $r_{2 i}$, the distance between the points $i$ and 2. Replacing Eqs. (5) and (6) in (2), for $\mathbf{G}=G_{x}+G_{y}+G_{z}$, in the case of $u_{2}$, and simplifying with respect to $\exp (\mathbf{G} \cdot \mathbf{r}_{2})$, it is obtained:

$$
\begin{aligned}
&(\mathbf{k}+\mathbf{G})^{2}+\frac{1}{d^{2}}-\frac{1+\cos \left(G_{x} d\right)}{3 d^{2}}+\left(k_{x}+G_{x}\right) \frac{2 \sin \left(G_{x} d\right)}{d} \\
& \quad+\left(k_{y}+G_{y}\right) \frac{4}{\sqrt{3} d} \cos \left(\frac{G_{x} d}{2}\right) \sin \left(\frac{\sqrt{3} G_{y} d}{2}\right)+\left(k_{z}+G_{z}\right) \frac{2 \sin \left(G_{z} d\right)}{d}-V=E. \quad (7)
\end{aligned}
$$

Here the potential $V(x, y, z)$ is defined as:

$$
\begin{aligned}
V(x, y, z) & =V_{0}\left(\left(x-\frac{3}{4} a\right)^{2} \sin \left(G_{x} d\right)^{2}+\left(y-\frac{\sqrt{3}}{4} a\right)^{2} \sin \left(G_{y} d\right)^{2}\right) \\
& \quad+\frac{5}{3}\left(z-\frac{1}{2} a\right)^{2} \sin \left(G_{z} d\right)^{2}
\end{aligned}
$$

![](./images/811965762624290819_4.jpg)

Fig. 2. (a) 2D diagram of the potential, presenting 2 possible trajectories of the particle, (b) diagram of total energy and potential for the trajectory 1-2, (c) diagram of total energy and potential for the trajectory 3-4.

$$
+\frac{2 \sqrt{3}}{3}\left(x-\frac{3}{4} a\right)\left(y-\frac{\sqrt{3}}{4} a\right) \sin \left(G_{x} d\right)^{2} \sin \left(G_{z} d\right)^{2}. \tag{8}
$$

Eq. (8) is replaced in Eq. (7), for having the final equation of the energy. $V_{0}$, is calculated as the Coulomb potential between $\mathrm{Cr}^{3+}$ and $\mathrm{N}^{3-}$ ions. Limited spherical symmetric potential is calculated as an ellipsoid contained into the unit cell, and it can be produced by ions of a unitary cell of Fig. 1(d). It is assumed that into the ellipsoid, the potential is quadratic. Thus if the particle moves along the centered axis of the unit cell (line 1-2 in Fig. 2(a)), the potential would look like Fig. 2(b), and in this case the total energy of the particle is greater than zero; the particle has no turning points it is free to roam the entire plane. The trajectory of the particle through the plane will depend critically on the initial position and velocity, as the particle is continually knocked around by the potential wells. On the other hand, if the particle moves along the diagonals of the unit cell as it is shown in Fig. 2(c), a particle with less than zero energy has been displayed. It is confined to one well; classically, the particle would rattle around inside the well and would never tunnel through the region where it would have to have negative kinetic energy. Moreover, The potential has high dependence with respect to periodic function of $G_{x}, G_{y}$ and $G_{z}$, giving the lattice periodicity to the potential. Calculations are carried out with the Mathematics 4.0 package. Band structure is obtained employing Eqs. (7) and (8).

## 4. Results and analysis

Fig. 3 shows the graphic of band structure for fcc CrN $(\delta-\mathrm{CrN})$. This graphic is obtained by plotting Eq. (7) after replacing the potential (Eq. (8)). In this equation $\mathbf{K}$, which takes values (100) for direction $\Delta$, (110) for $\Sigma$ and (111) for $\Lambda$, and $\mathbf{G}=\mathbf{h} \cdot \mathbf{a}$, being $\mathbf{a}=\left(a_{1}, a_{2}, a_{3}\right)$, as it is shown in Eq. (3) and $\mathbf{h}$ depends on the Brillouin zone $((0,0,0),(1,0,0),(2,0,0)$, etc.). It is alike to the band structure reported for materials similar to CrN, from groups V, IV and VII (materials with d-electrons), like MoN, ZrN, and NbN, which have small or any band gap, due to their metallic behaviour since these nitrides usually have a combination of metallic, ionic and covalent bonds [9]. Because of CrN has higher nitrogen-metallic atomic radii ratio (0.584), than TiN (0.504) and ZrN (0.463) the metallic bond that normally appears in these materials is less notorious for CrN. Furthermore, $\sigma$, and $\pi$ covalent bonds between $\mathrm{Cr}$ atoms could be stronger, because their d orbital are a little more complete. Moreover, CrN does not have hybridization between pd orbitals like TiN, characteristic that provides CrN with high metallic behaviour to this

![](./images/811965762624290819_5.jpg)

Fig. 3. Band structures of CrN. The Fermi level is the zero in the energy scale.

material. As is reported, CrN has excellent mechanical properties, being it used in hard coatings and multilayers [10,11]. The increase in the covalent bonds of CrN results in high hardness.

### 5. Conclusions

Band structure of CrN using finite differences and a 3D spherical symmetric attractive potential was made here. The unitary cell was gridded and the Schrödinger equation of one point into the lattice was obtained by finite differences. The spherical potential showed the symmetry of the unit cell and the lattice. The band structure was plotted for (100), (110) and (111) directions was observed. Probably, CrN has lower percentage of metallic bonds than other similar structure nitrides like TiN and ZrN, because its lattice parameter is higher.

### Acknowledgement

The authors wish to acknowledge the Universidad Nacional de Colombia Sede Manizales for its financial support through la División para el Apoyo a la Investigación, DIMA.

### References

[1] Tanmoy Das, Sudipta Deb, Abhijit Mookerjee, Physica B 367 (2005) 6-18.
[2] F. Lévy, P. Hones, P.E. Schmid, R. Sanjinés, M. Diserens, C. Wiemer, Surf. Coat. Technol. 120-121 (1999) 284-290.
[3] S. Logothetidis, P. Patsalas, K. Sarakinos, C. Charitidis, C. Metaza, Surf. Coat. Technol. 180-181 (2004) 637-641.
[4] M.Y. Suárez. V, Jairo Arbey Rodríguez Martínez, F. Fajardo, Rev. Col. Fis. 38 (2) (2006) 501-504.
[5] A. Dasgupta, P.A. Premkumar, F. Lawrence, L. Houben, P. Kuppusami, M. Luysberg, K.S. Nagaraja, V.S. Raghunathan, Surf. Coat. Technol. 201 (2006) 1401-1408.
[6] P. Cai, W. Zhang, L. Chen, Y. Qian, J. Alloys Compounds 414 (2006) 221-223.
[7] K. Inumaru, H. Okamoto, S. Yamanaka, J. Crystal Growth 237-239 (2002) 2050-2054.
[8] F. Ducastelle, P. Costa, Phys. Lett A 33 (1970) 447-448.
[9] H.O. Pierson, Handbook of Refractory Carbides and Nitrides, Ed. Noyes Publications, USA, 1996.
[10] A.P. Ehiasarian, P.Eh. Hovsepian, L. Hultman, U. Helmersson, Thin Solid Films 457 (2004) 270-277.
[11] S. Logothetidis, N. Kalfagiannis, K. Sarakinos, P. Patsalas, Surf. Coat. Technol. 200 (2006) 6176-6180.