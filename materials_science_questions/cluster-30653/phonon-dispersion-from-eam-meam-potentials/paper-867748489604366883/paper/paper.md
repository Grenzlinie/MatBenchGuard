# Structures of Cylindrical Ultrathin Copper Nanowires

Ho Jung Hwang and Jeong Won Kang*

Semiconductor Process and Device Laboratory, Department of Electronic Engineering, Chung-Ang University, 221 HukSuk-Dong, DongJak-Ku, Seoul 156-756, Korea

## ABSTRACT

To investigate cylindrical ultrathin copper nanowires, we performed atomistic simulations using the steepest descent method. The stable structures of the cylindrical ultrathin copper nanowires were multi-shell packs composed of coaxial cylindrical shells with {111}-like surfaces. Semiclassical orbits in a circle and circular rolling of a triangular network could explain the structures of the cylindrical ultrathin multi-shell copper nanowires. A calculation of the angular correlation function and the radial distribution function for nanowires showed that the structural properties of nanowires became closer to those of the bulk with increasing nanowire diameter.

KEY WORDS : Cu nanowire, Atomistic simulation, Cylindrical multi-shell nanowires

PACS Numbers:
Email: kok@semilab3.ee.cau.ac.kr
Tel: 82-02-820-5296
Fax: 82-02-825-1584

# INTRODUCTION

Since the fundamental interest in low-dimensional physics and technological applications, such as for molecular electronic devices, has increased during the past decade, ultrathin metallic nanowires have been studied intensively [1-33]. In recent years, long metallic nanowires with well-defined structures having diameters of several nanometers have been fabricated using different methods [5-10]. Novel helical multi-shell structures have been observed in ultrathin gold nanowires [5-8], and these have been investigated using molecular dynamics (MD) simulations [11-16]. Multi-shell nanowires have also been made from several inorganic layered materials, such as $\text{WS}_2$, $\text{MoS}_2$, and $\text{NiCl}_2$ [17-19]. The cylindrical shells obtained in the MD simulation are similar to the geometric shells of clusters. The MD simulations have focused on infinite wires with periodic boundary conditions along the wire axes. For example, MD studies have been carried out on the structure of ultra-thin, infinite Pb and Al nanowires at $T = 0$ K [20, 21], on the pre-melting of infinite Pb nanowires orientated along the (110) direction [22], and on the melting of infinite Pt and Ag (100)-oriented nanowires [23]. The structures of freestanding Ti nanowires have been studied using a genetic algorithm and a tight-binding potential [24]. The strain rate effect induced by amorphizations of pure Ni and NiCu alloy nanowires [25] and the yielding and fracture mechanisms of Au and Cu nanowires [26, 27] have also been investigated using MD simulations. Yanson *et al.* have studied multi-shell structures in Na nanowires [28]. The stability of Na

nanowires was studied by modeling them as infinite uniform jellium cylinders and by solving self-consistently [29]. In addition, the deformation and the breaking of atomic-sized sodium wires has been studied using a density functional simulation [30]. The stability of quasi-one-dimensional Si structures has been investigated using a generalized tight-binding MD scheme [31], and Si nanowires connected to Al electrodes have been studied using large-scale local density functional simulation [32]. Bilalbegović studied the room temperature structure of Al, Cu, and Au infinite nanowires using MD simulations and showed that cylindrical multi-shell and filled metallic nanowires exist for several fcc metals [16].

However, present knowledge of the structures and properties of metallic nanowires is still quite limited. In particular, as far as we know, there is no theoretical work on the atomic structures of cylindrical ultrathin copper nanowires. For cylindrical ultrathin copper nanowires, computer simulations can help in elucidating their properties and in developing new methods for their fabrication and can provide microscopic information on their physical properties. Therefore, in this research, we have investigated the structural properties of cylindrical ultathin copper nanowires.

## SIMULATION METHODS

The interaction between Cu atoms is described by a well-fitted potential function of the second moment approximation of the tight binding (SMA-TB) scheme [34]. The SMA-TB-type potential function has been used in atomistic simulation studies of nanoclusters [35-39] and ultrathin nanowires [24]. This potential is in good agreement with other potentials and with the experiments for bulk [34] and low-dimensional systems [33]. Table 1 shows the physical values for Cu calculated by using the SMA-TB scheme and other theological methods and measured by experiment. The physical values for Cu calculated by the SMA-TB scheme are in agreement with the other results.

In our study of the structure of cylindrical Cu nanowires, atomistic simulations were as follows: (1) We defined a cylinder with a diameter; then, an atom was inserted into the bottom of the cylinder. (2) Another atom was inserted into the bottom of the cylinder, and the atomic configuration was relaxed using the steepest descent (SD) scheme. (3) After sufficient relaxation, another atom was inserted into the bottom of the cylinder, and the atomic configuration was again relaxed using the SD scheme. This simulation was repeated until the length of the nanowire reached $40$ $\mathring{A}$. The reflective boundary condition (RBC) and the free boundary condition were then applied to the radial direction of the cylinders and to the axis of the nanowires, respectively. The diameter of the cylinder, $D_{\rm c}$, ranged from $2$ to $16$ $\mathring{A}$, and the positions of the atomic centers were

sited along the radius, $D_c/2$.

# SIMULATION RESULTS AND DISCUSSION

Before discussion of our simulation results, we briefly review regular polygons inside a circle, which are applicable to cylindrical nanowires. A series of semiclassical orbits inside a circle is elementary geometry obtained by using the classical dynamics of a circular billiard ball on a circular billiard table [28, 40, 41]. Due to momentum conservation, only the ball's direction and position [40,41] determine its motion. The periodic orbits for the circular billiard ball are the regular polygons shown in Fig. 1. Each of these orbits can be characterized by a three-integer numbers $\beta(v, \omega, n)$,where $v$ is the number of turning points at the boundary during on period and $\omega$ measures how many times the trajectory encircles the center during the fundamental period. Therefore the winding number is $\omega$, and the number of vertices is $v$. Obviously, we have $v \geq 2\omega$. If there is a maximum common divisor $n$ between $v$ and $\omega$, the orbit is an $n$-fold repetition of a primitive periodic orbit (see (2,1,1), (4,2,2), (6,3,3), and (3,1,1), (6,2,2), and (9,3,3) in Fig. 1). Introducing an angle $\phi_{v\omega} = \pi \omega / v$, the length of a periodic orbit is $L_{v\omega}=2\ v R \sin\phi_{v\omega}$ from simple geometry, where $R$ is the radius. The structures of artificial cylindrical ultrathin Cu nanowires obtained from our simulations can be compared with the closed classical periodic orbits in a circular billiard with reflective walls.

Figure 2 shows some typical cylindrical Cu nanowire structures obtained from our

simulations. In general, the stable structures of the cylindrical copper nanowires are multi-shell packs composed of coaxial cylindrical shells. The copper nanowires in some cases have a single-atom chain at their center. Each shell is formed by rows of atoms wound helically upwards, side by side. The pitch of the helices for the outer and the inner shells are different. The lateral surface of each shell exhibits a near-triangular network. Such helical multi-shell structures have been theoretically predicted for Al, Pb [20, 21], Au [11-16], and Ti nanowires [24] and recently experimentally observed in Au nanowires [5-8]. To characterize the multi-shell structures, Yanson *et al.* [28] used the classical orbits inside a circle and labeled the orbits of nanowires as (M,Q), where M is the number of vertices and Q is the winding number, and Kondo and Takayanagi [7] introduced the notation $n$ - $n'$ - $n''$ - $n'''$ to describe a nanowire consisting of coaxial tubes with $n$, $n'$, $n''$, $n'''$ helical atom rows ($n > n' > n'' > n'''$). Wang *et al* [24] used this notation. Since the thinnest magic nanowire consists of a single tube and a central strand, Tosatti *et al.* [13] used an $(n, h)$ to denote a tube consisting of $n$ closely packed strands forming a maximal angle ranging from $30^\circ$ ($n$ = 0) to $0^\circ$ ($h = n/2$) with respect to the tube axis. Although the index of Kondo and Takyanagi ($KT$ index) is useful and easy to determine for multi-shell nanowire structures, the chirality information on nanowires cannot be characterized. The index of Tosatti *et al.* ($T$ index) provides both chirality information and helical atom rows in the shells. In this work, we use both notations, the $KT$ and the $T$ indices, to denote cylindrical multi-shell nanowire structures.

The structures of the thinnest nanowire with $KT$ index 2 ($D_{\mathrm{c}}$ =2.56 $\mathring{\mathrm{A}}$), the nanowire with $KT$ index 4 ($D_{\mathrm{c}} = 2.8$ $\mathring{\mathrm{A}}$ - 3.2 $\mathring{\mathrm{A}}$), the 5 - 1 nanowire ($D_{\mathrm{c}} = 4$ $\mathring{\mathrm{A}}$), and the 6 - 1 nanowire ($D_{\mathrm{c}} = 5$ $\mathring{\mathrm{A}}$) in Fig. 2 are related to (2, 1, 1), (4, 1, 1), (5, 1, 1), and (6, 1, 1) of semiclassical orbits in Fig. 1, respectively. The 6 - 1, 8 - 3 ($D_{\mathrm{c}} = 6$ $\mathring{\mathrm{A}}$), 9 - 4 ($D_{\mathrm{c}} = 7$ $\mathring{\mathrm{A}}$), 11 - 6 - 1 ($D_{\mathrm{c}} = 9$ $\mathring{\mathrm{A}}$), 13 - 8 - 3 ($D_{\mathrm{c}} = 10$ $\mathring{\mathrm{A}}$), and 16 - 11 - 6 - 1 ($D_{\mathrm{c}} = 12$ $\mathring{\mathrm{A}}$) wires constitute a growth pattern with a five-atom difference between the shells. In contrast, the structure of the 20 - 16 - 10 - 5 - 1 ($D_{\mathrm{c}} = 16$ $\mathring{\mathrm{A}}$) wire constitute a growth pattern with a four-, five-, and six-atom difference between the shells, centered on a single atom chain. Helical multi-shell nanowires without a single atom chain in the center are 8 - 3, 9 - 4, and 13 - 8 - 3 wires. Each nanowire has a $\{111\}$-like surface. Previous simulation works on nanowire elongation deformation showed that a rectangular $\{100\}$ nanowire transforms in to a cylindrical nanowire with a $\{111\}$-like surface by stretching [27]. In order to carry out a more detailed study of cylindrical multi-shell nanowire structures, we investigated the spreading sheets of nanowires in Fig. 2. Figure 3 shows the spreading sheets of nanowires, which are generally composed of a triangular network. To investigate the spreading sheets, we explain the $T$ index of the triangular network sheet in Fig. 4. As shown in Fig. 4, the tube unit cell is given by the orthogonal vector $(n, h)$ and the wire axis vector $(p, q)$, in which $p: q=(n - 2h):(2n - h)$, and $h\leq n/2$. All other tubes, except $(n, 0)$ and $(n, h/2)$, are chiral, and $(n, h)$ and $(n, n$-$h)$ are symmetrical with one another. At a constant $n$ value, the wire center-to-center radius is given by $d_{0}$

$(n^{2}+h^{2}-nh)^{1/2}/2\pi$ Å and decreases for increasing $h$, as the strands progressively align with the axis, where $d_{0}$ is the distance from the atomic center to the wire center. The total number of atoms per shell is $N=2\ (n^{2}+h^{2}-nh)$, and the number in the central strand is $q$. In this paper, the central strand is denoted by (1, 1).

The nanowire structure indices of $KT$ and $T$ are shown in Table 2. Using the $KT$ index, we denote nanowires with $D_{\mathrm{c}}=2.8$, 3.0, and $3.2$ Å by 4. However, if the $T$ index is used, nanowires with $D_{\mathrm{c}}=2.8$, 3.0, and $3.2$ Å are denoted by (4, 2), (4, 1), and (4, 0), respectively. As mentioned above, at constant $n$ value, the wire diameter is linearly proportional to $d_{0}\ (n^{2}+h^{2}-nh)^{1/2}/\pi$, and the chirality angle is given by $\tan ^{-1}(\sqrt{3}h/(2n-1))$. In the case of $D_{\mathrm{c}}=16$ Å, the spreading sheet of the first inner shell shows triangular and square networks, and the spreading sheet of the outer shell has one vacancy. Both semiclassical orbits in a circle and circular rolling of the triangular network can explain the structures of cylindrical ultrathin multi-shell copper nanowires.

We also analyze the angular correlation function (ACF) and the radial distribution function (RDF) relating to the structural properties of cylindrical ultrathin copper nanoiwres. Figure 5 shows the ACFs of cylindrical ultrathin copper nanowires. The dashed line, the case of $D_{\mathrm{c}}=16$ Å, indicates the ACF of the bulk at 300 K. As the nanowire diameter is increased, the ACFs of the nanowires become similar to the ACF of the bulk. Since nanowires with $2.5$ Å $\leq D_{\mathrm{c}}\leq 3.5$ Å have a rectangular structure, the peaks of the ACFs are different from the other ACFs at angle

about $90^\circ$. In the 5 – 1 nanowire, main peaks at about $60^\circ$ and $108^\circ$ and a small peak at about $72^\circ$ are observable, and the $108^\circ$ and$72^\circ$ peaks are related to the pentagonal structure. Since the shells of nanowires are composed of the triangular networks, the ACFs of most of the multi-shell structure nanowires have their main peaks at about $60^\circ$. Figure 6 shows the RDFs of cylindrical ultrathin Cu nanowires for different value of $D_\text{c}$. The dashed line in the case of $D_\text{c}=16$ Å indicates the RDF of the bulk at 300 K. As the nanowire diameter is increased, the RDFs of the nanowires become similar to the RDF of the bulk. In all nanowire cases, it is shown that the first nearest-neighbor atom distances are slightly closer than those in the bulk. Therefore, we also calculate the radii of cylindrical ultrathin Cu nanowires. Table III shows the radii of cylindrical ultrathin copper nanowires in Å. In Table III, A and B indicate nanowires obtained by our simulation and by rolling of a triangular network sheet, respectively. The nanowires obtained by rolling of a triangular network sheet are relaxed by using the steepest descent method. The values in brackets are radii calculated by using $d_0\ (n^2 + h^2 - nh)^{1/2}/\ 2\pi$. The radius of each shell is the distance from the nanowire center. The values in the parentheses at the right of the $KT$ index are the orthogonal vectors of the outer-shell for the nanowires. In the case of the 5-1 nanowire, the radius obtained from simulation and relaxation slightly increases more than the values in the brackets. However, in the other cases, the radii obtained from the simulation and relaxation are slightly less than those obtained by calculation. We think that is reason that, in the cross-sectional pentagon of the 5-1

nanowire, angles between the central strand and the outer-shell deviate from the angle of a normal triangle, as shown in Figs. 1 and 5.

# SUMMARY

We investigated the structure of cylindrical ultrathin copper nanowires by using a cylinder and the steepest descent method. The stable structures of the cylindrical ultrathin copper nanowires are multi-shell packs composed of coaxial cylindrical shells. The theory of semiclassical orbits in a circle partially explained the properties of the structures of cylindrical ultrathin copper nanowires. An investigation of the spreading sheets of the nanowires obtained from our simulations showed that a coaxial cylindrical shell could be obtained by circular rolling of a triangular network sheet with an orthogonal vector. When the cylinder diameters are below $3.2$ Å, the angular correlation functions show a main peak at about $90^\circ$. However, as the diameter of the nanowire is increased, the angular correlation and the radial distribution functions of the nanowires approach those of the bulk.

The structures of cylindrical ultrathin gold nanowires have been made clear by atomistic simulations and experiments; however, for the structures of cylindrical ultrathin copper nanowires, this work partially showed their properties by using atomistic simulations. Therefore, we are now preparing more specific theoretical and experimental works on such subjects as thermal effects, electronic properties, nanowire fabrication using STM and TEM images, thus overcoming our confined simulation work on copper nanowires.

## REFERENCES

[1] N. Agrait, J. G. Rodrigo, and S. Vieira, Phys. Rev. B 47, 12345 (1993); N. Agrait , G. Rubio, and S. Bieira, Phys. Rev. Lett. 74, 3995 (1995); G. Rubio, N. Agrait, and S. Vieira, Phys. Rev. Lett. 76, 2302 (1996).

[2] J. I. Pascual , J. Mendez, J. Gomez-Herrero, A. M. Baro, N. Garcia, and V. T. Binh, Phys. Rev. Lett. 71, 1852 (1993).

[3] L. Olesen, E. Laegsgaard, I. Stensgaard, F. Besenbacher, J. Schiotz, P. Stoltze, K. W. Hacobsen, and J. K. Norskov, Phys. Rev. Lett. 72, 2251 (1994).

[4] J. M. Kran, J. M. van Ruitenbeek, V. V. Fisun, J. K. Yan, and L. J. de Jongh, Nature 375, 767 (1995).

[5] Y. Kondo and K. Takayanagi, Phys. Rev. Lett. 79, 3455 (1997).

[6] H. Ohnishi, Y. Kondo, and K. Takayanagi, Nature 395, 780 (1998).

[7] Y. Kondo and K. Takayanagi, Science 289, 606 (2000).

[8] V. Rodrigues, T. Fuhrer, and D. Ugarte, Phys. Rev. Lett. 85, 4124 (2000).

[9] I. Lisiecki, A. Filankembo, H. Sack-Kongehl, K. Weiss, M.-P. Pileni, and J. Urban, Phys. Rev. B 61, 4968 (2000).

[10] W. S. Yun, J. Kim, K. H. Park, J. S. Ha, Y. J, Ko, K. Park, S. K. Kim, Y. J. Doh, H. J. Lee, J. P. Salvetat, and László Forró, J. Vac. Sci. Tehcnol. A 18, 1329 (2000).

[11] B. Wang, S. Yin, G. Wang, A. Buldum, and J. Zhao, Phys. Rev. Lett. 86, 2046 (2001).

[12] G. Bilalbegović, Phys. Rev. B 58, 15412 (1998).

[13] E. Tosatti, S. Prestipino, S. Kostlmeier, A. Dal Corso, and F. D. Di Tolla, Science 291, 288 (2001).

[14] G. Bilalbegović, Solid State Communication 115, 73 (2000).

[15] J. A. Torres, E. Tosatti, A. Dal Corso, F. Ercolessi, J. J. Kohanoff, F. D. Di Tolla, and J. M.

Soler, Surf. Sci. 426, L441 (1999).

[16] G. Bilalbegović, Computational Materials Science 18, 333 (2000).

[17] R. Tenne, L. Margulis, M. Genut, and G. Hodes, Nature 360, 444 (1992).

[18] L. Margulis, G. Salitra, R. Tenne, and M. Tallenker, Nature 365, 113 (1993).

[19] Y. R. Hacohen, E. Grunbaum, R. Tenne, and M. Tallenker, Nature 395, 336 (1998).

[20] O. Gülseren, F. Erolessi, and E. Tosatti, Phys. Rev. Lett. 80, 3775 (1998).

[21] F. Di Tolla, A. Dal Corse, J. A. Torres, and E. Tosatti, Surf. Sci. 456, 947 (2000).

[22] O. Gülseren, F. Erolessi, and E. Tosatti, Phys. Rev. B 51, 7377 (1995).

[23] G. M. Finbow, R. M. Lynden-Bell, and I. R. McDonald, Mol. Phys. 92, 705 (1997).

[24] B. Wang, S. Yin, G. Wang, and J. Zhao, J. Phys.: Condens. Matter 13, L403 (2001).

[25] H. Ikeda, Y. Qi, T. Cagin, K. Samwer, W. L. Johnson, and W. A. Goddard, Phys. Rev. Lett. 82,
2900 (1999).

[26] H. Mehrez and S. Ciraci, Phys. Rev. B 56, 12632 (1997).

[27] J. W. Kang and H. J. Hwang, J. Korean Phys. Soc. 38 July (2001).

[28] A. I. Yanson, I. K. Yanson, and J. M. van Ruitenbeek, Phys. Rev. Lett. 84, 5832 (2000).

[29] M. J. Puska, E. Ogando, and N. Zabala, Phys. Rev. B 64, (033401temp), June (2001).

[30] A. Nakamura, M. Brandbyge, L. B. Hansen, and K. W. Jacobsen, Phys. Rev. Lett. 82, 1538
(1999).

[31] M. Menon and E. Richter, Phys. Rev. Lett. 83, 792 (1999).

[32] U. Landman, R. N. Barnett, A. G. Scherbakov, and P. Avouris, Phys. Rev. Lett. 85, 1958
(2000).

[33] J. W. Kang and H. J. Hwang, Nanotechnology (in submitted).

[34] F. Cleri and V. Rosato, Phys. Rev. B 48, 22 (1993).

[35] K. Michaclian, N. Rendon, and I. L. Garzon, Phys. Rev. B 60, 2000 (1999).

[36] F. J. Palacios, M. P. Iniguez, M. J. Lopez, and J. A. Alonso, Phys. Rev. B **60**, 2908 (1999).

[37] L. Rongwu, P. Ahengying, and H. Yukun, Phys. Rev. B **53**, 4156 (1996).

[38] T. X. Li, S. Y. Yin, Y. L. Ji, B. L. Wang, G. H. Wang, and J. J. Zhao, Phys. Lett. A **267**, 403 (2000).

[39] H. Lei, J. Phys.: Condens. Matter **13**, 3023 (2001).

[40] S. M. Reimann, M. Brack, A. G. Magner, J. Blaschke, and M. V. N. Murthy, Phys. Rev. A 53, 39 (1996).

[41] C. Hoppler and W. Zwerger, Phys. Rev. B 59, R7849 (1999).

[42] R. A. Johnson, Phys. Rev. B **39**, 12554 (1989).

[43] M. A. Baskes, Phys. Rev. B **46**, 2727 (1992).

[44] F. Montalenti and R. Ferrando, Phys. Rev. B **59**, 5881 (1999).

[45] J. Merikoski, I. Vattulainen, J. Heinonen, and T. Ala-Nissila, Surf. Sci. **387**, 167 (1997); J. Merikoski and R. Ala-Nissila, Phys. Rev. B **52**, 8715 (1995).

[46] P. Stolze, J. Phys.: Condens. Matter **6**, 9495 (1994).

[47] L. S. Perkins and A. E. DePristo, Surf. Sci. **294**, 67 (1993).

[48] L. S. Perkins and A. E. DePristo, Surf. Sci. **317**, L1152 (1994).

[49] C. J. Lui, J. M. Cohen. J. B. Adams, and A. F. Voter, Surf. Sci. **253**, 334 (1991)

[50] G. Boisvert and L. J. Lewis, Phys. Rev. B **56**, 15569 (1997).

[51] M. Breeman and D. O. Boerma, Surf. Sci. **269-170**, 224 (1992).

### Table Caption

Table I. SMA-TB results are compared to results of a simple analytic nearest-neighbor embedded-atom model developed by Johnson [42] and Baskes [43]. The SMA-TB results for a surface diffusion barrier are compared to other results, such as effective medium (EM)[45, 46], corrected effective medium (CEM) [47], embedded-atom models in the Voter-Chen parameterization (EA(VC)) [48] and in the Adams-Foiles-Wolfer parameterization (EA(AFW)) [49], *ab-initio* density-functional calculations in the local-density approximation (LDA) [50], *ab-initio* density-functional results with gradient corrections (GGA) [50], and experimental results [51]. $E_{\rm c}$ and $a_0$ are the cohesive energy of the atom and the lattice constant, respectively.

Table II. Structure index of the cylindrical ultrathin copper nanowires obtained by our simulations. $D_{\rm c}$ is the diameter of the cylinder, the *KT* index is the index of Kondo and Takyanagi [7], and the *T* index is the index of Tosatti *et al.* [13].

Table III. Radii of the cylindrical ultrathin copper nanowires; A and B are for nanowires obtained by our simulation and for relaxed nanowires of structures obtained by rolling of triangular networks sheet, respectively. The values in brackets [ ] are the radii calculated by using $d_0\ (n^2+h^2-nh)^{1/2}/2\pi$, where $d_0$ is the atomic distance in the bulk at T = 0 K and $(n,h)$ is the orthogonal vector of the nanowire. The unit of the radii is Å.

### Figure Captions

Figure 1. Series of semiclassical inscribed inside a circular cross section, which are applicable to spheres (clusters) and cylinders (nanowires) alike.

Figure 2. Morphologies of cylindrical ultrathin Cu nanowires with diameters form 2 Å to 16 Å. In each case, a top view (left) and a side view (right) are presented.

Figure 3. Spreading sheets of each cylindrical Cu nanowire case in Fig. 2

Figure 4. Triangular network sheet. An $(n, h)$ shell is made by cylindrically rolling a triangular lattice. A $(p, q)$ is the axis vector of the $(n, h)$ shell. $p: q=(n$-$2h):(2n$-$h)$, and $h \leq n/2$.

Figure 5. Angular correlation functions for nanowires.

Figure 6. Radial distribution functions for nanowires.

**TABLES**

Table I.

<table>
  <tbody>
    <tr>
      <th>
      </th>
      <th>
      </th>
      <th>
      </th>
      <td colspan="3">
        Energy/atom on surface (eV)
      </td>
      <td colspan="3">
        Energy/atom of nanowire (eV)
      </td>
    </tr>
    <tr>
      <th>
      </th>
      <th>
        $E_{c}$(eV)
      </th>
      <th>
        $a_{0}$($Å$)
      </th>
      <td>
        (100)
      </td>
      <td>
        (110)
      </td>
      <td>
        (111)
      </td>
      <td>
        Surface
      </td>
      <td>
        edge
      </td>
      <td>
        inside
      </td>
    </tr>
    <tr>
      <th>
        SMA-TB
      </th>
      <th>
        -3.544
      </th>
      <th>
        3.615
      </th>
      <td>
        -2.999
      </td>
      <td>
        -2.913
      </td>
      <td>
        -3.127
      </td>
      <td>
        -2.999
      </td>
      <td>
        -2.547
      </td>
      <td>
        -3.548
      </td>
    </tr>
    <tr>
      <th>
        EAM-I
      </th>
      <th>
        -3.540
      </th>
      <th>
        3.620
      </th>
      <td>
        -2.989
      </td>
      <td>
        -2.848
      </td>
      <td>
        -3.064
      </td>
      <td>
        -2.989
      </td>
      <td>
        -2.499
      </td>
      <td>
        -3.451
      </td>
    </tr>
    <tr>
      <th>
        EAM-II
      </th>
      <th>
        -3.540
      </th>
      <th>
        3.620
      </th>
      <td>
        -2.360
      </td>
      <td>
        -2.065
      </td>
      <td>
        -2.655
      </td>
      <td>
        -2.360
      </td>
      <td>
        -1.475
      </td>
      <td>
        -3.540
      </td>
    </tr>
    <tr>
      <th>
      </th>
      <th>
        SMA-TB
      </th>
      <th>
        EM
      </th>
      <th>
        CEM
      </th>
      <th>
        EA(VC)
      </th>
      <th>
        EA(AFW)
      </th>
      <th>
        LDA
      </th>
      <th>
        GGA
      </th>
      <th>
        Experiment
      </th>
    </tr>
    <tr>
      <th colspan="9">
        Diffusion Barriers on (100) surface (eV)
      </th>
    </tr>
    <tr>
      <th>
        Jump
      </th>
      <td>
        0.41
      </td>
      <td>
        0.40b
      </td>
      <td>
        0.47d
      </td>
      <td>
        0.53f
      </td>
      <td>
        0.38f
      </td>
      <td>
        0.65-0.75g
      </td>
      <td>
        0.51-0.55g
      </td>
      <td>
        0.39$\pm$0.06h
      </td>
    </tr>
    <tr>
      <th>
        Exchange
      </th>
      <td>
        0.79
      </td>
      <td>
        -
      </td>
      <td>
        0.43d
      </td>
      <td>
        0.79f
      </td>
      <td>
        0.72f
      </td>
      <td>
        1.03-1.23g
      </td>
      <td>
        0.82-0.96g
      </td>
      <td>
        -
      </td>
    </tr>
    <tr>
      <th colspan="9">
        Diffusion Barriers on (110) surface (eV)
      </th>
    </tr>
    <tr>
      <th>
        In channel
      </th>
      <td>
        0.23a
      </td>
      <td>
        0.29c
      </td>
      <td>
        0.26e
      </td>
      <td>
        0.53f
      </td>
      <td>
        0.24f
      </td>
      <td>
        -
      </td>
      <td>
        -
      </td>
      <td>
        -
      </td>
    </tr>
    <tr>
      <th>
        Cross channel
      </th>
      <td>
        0.29a
      </td>
      <td>
        0.56c
      </td>
      <td>
        0.49e
      </td>
      <td>
        0.31f
      </td>
      <td>
        0.30f
      </td>
      <td>
        -
      </td>
      <td>
        -
      </td>
      <td>
        -
      </td>
    </tr>
  </tbody>
</table>

a Ref. [44].

b Ref. [45].

c Ref. [46].

d Ref. [47].

e Ref. [48].

f Ref. [49].

g Ref. [50].

h Ref. [51].

<table>
<thead>
<tr>
<th rowspan="2">$D_\text{c}$ (Å)</th>
<th colspan="2">Structure indexes</th>
</tr>
<tr>
<th>$KT$ index<br>n - n' - n'' - n'''-n''''</th>
<th>$T$ index<br>orthogonal vectors</th>
</tr>
</thead>
<tbody>
<tr>
<td>2.5</td>
<td>2</td>
<td>(2,0)</td>
</tr>
<tr>
<td>2.8</td>
<td>4</td>
<td>(4,2)</td>
</tr>
<tr>
<td>3.0</td>
<td>4</td>
<td>(4,1)</td>
</tr>
<tr>
<td>3.2</td>
<td>4</td>
<td>(4,0)</td>
</tr>
<tr>
<td>4.0</td>
<td>5 - 1</td>
<td>(5,0)(1,1)</td>
</tr>
<tr>
<td>5.0</td>
<td>6 - 1</td>
<td>(6,0)(1,1)</td>
</tr>
<tr>
<td>6.0</td>
<td>8 - 3</td>
<td>(8,1)(3,1)</td>
</tr>
<tr>
<td>7.0</td>
<td>9 - 4</td>
<td>(9,1)(4,2)</td>
</tr>
<tr>
<td>9.0</td>
<td>11 - 6 - 1</td>
<td>(11,0)(6,0)(1,1)</td>
</tr>
<tr>
<td>10.0</td>
<td>13 - 8 - 3</td>
<td>(13,1)(8,1)(3,1)</td>
</tr>
<tr>
<td>12.0</td>
<td>16 - 11 - 6 - 1</td>
<td>(16,0)(11,0)(6,0)(1,1)</td>
</tr>
<tr>
<td>16.0</td>
<td>20 - 16 - 10 - 5 - 1</td>
<td>(20,0)(16,0)(10,0)(5,0)(1,1)</td>
</tr>
</tbody>
</table>
Table II.

Table III.

<table>
  <thead>
    <tr>
      <th colspan="2">5-1 (5,0)</th>
      <th colspan="2">6-1 (6,0)</th>
      <th colspan="2">16-11-6-1 (16,0)</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>A</th>
      <th>B</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">[0 - 2.037]</td>
      <td colspan="2">[0 - 2.445]</td>
      <td colspan="2">[0 - 2.445 - 4.482 - 6.519]</td>
    </tr>
    <tr>
      <td>0 - 2.09</td>
      <td>0 - 2.10</td>
      <td>0 - 2.40</td>
      <td>0 - 2.42</td>
      <td>0 - 2.36 - 4.40 - 6.47</td>
      <td>0 - 2.36 - 4.39 - 6.46</td>
    </tr>
  </tbody>
</table>

![](./images/867748489604366883_1.jpg)

Figure 1.

![](./images/867748489604366883_2.jpg)

Figure 2.

![](./images/867748489604366883_3.jpg)

Figure 3.

![](./images/867748489604366883_4.jpg)

Figure 4.

![](./images/867748489604366883_5.jpg)

Figure 5.

![](./images/867748489604366883_6.jpg)

Figure 6.