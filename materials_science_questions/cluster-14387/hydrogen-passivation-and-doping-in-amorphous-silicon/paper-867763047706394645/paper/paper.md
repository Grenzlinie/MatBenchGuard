# Number Series of Atoms, Interatomic Bonds and Interface Bonds Defining
Zinc-Blende Nanocrystals as Function of Size, Shape and Surface Orientation:
Analytic Tools to Interpret Solid State Spectroscopy Data

Dirk König*

Integrated Materials Design Centre (IMDC) and School of Photovoltaic and Renewable Energy Engineering (SPREE),
University of New South Wales, Sydney, Australia†

Semiconductor nanocrystals (NCs) experience stress and charge transfer by embedding materials or ligands and impurity atoms. In return, the environment of NCs experiences a NC stress response which may lead to matrix deformation and propagated strain. Up to now, there is no universal gauge to evaluate the stress impact on NCs and their response as a function of NC size $d_{\text{NC}}$. I deduce geometrical number series as analytical tools to obtain the number of NC atoms $N_{\text{NC}}(d_{\text{NC}}[i])$, bonds between NC atoms $N_{\text{bnd}}(d_{\text{NC}}[i])$ and interface bonds $N_{\text{IF}}(d_{\text{NC}}[i])$ for seven high symmetry zinc-blende (zb) NCs with low-index faceting: {001} cubes, {111} octahedra, {110} dodecahedra, {001}-{111} pyramids, {111} tetrahedra, {111}-{001} quatrodecahedra and {001}-{111} quatrodecahedra. The fundamental insights into NC structures revealed here allow for major advancements in data interpretation and understanding of zb- and diamond-lattice based nanomaterials. The analytical number series can serve as a standard procedure for stress evaluation in solid state spectroscopy due to their deterministic nature, easy use and general applicability over a wide range of spectroscopy methods as well as NC sizes, forms and materials.

## I. INTRODUCTION

It is well known that the electronic structure and optical response of NCs is a function of mechanical stress in the form of lattice strain. Mechanical stress is routinely measured by Raman- and Fourier-Transformation InfraRed (FT-IR) spectroscopy which probe the phononic spectra of NCs [1–5]. Such spectra are very sensitive to changes of stress induced by lattice pressure which is a function of the material Young's modulus [6]. Changes in compressive or expansive stress were shown to modify the optical response of NCs by fluorescence [7] or photoluminescence (PL) [8, 9]. Stranski-Krastanov growth [10, 11] of NCs in epitaxial films depends critically on balanced stress to avoid stacking faults which deteriotate electronic NC properties [12–15]. Attempts to place phosphorus atoms as donors onto lattice sites in free-standing Si NCs were shown to fail increasingly with shrinking NC diameter [16, 17], revealing a transition region from low to virtually zero doping of 20 to 10 nm. These findings were confirmed recently in theory and experiment for $\text{SiO}_2$-embedded Si NCs [18, 19]. Several research groups have shown that self-purification, a Si NC-internal build-up of stress counteracting external stress due to dopant incorporation, causes impurity doping to fail [20–23].

With a universal gauge for stress such phenomena could be scaled as a function of NC size $d_{\text{NC}}$. Principal parameters are the number of atoms forming the zb-NC $N_{\text{NC}}(d_{\text{NC}})$, the bonds between such atoms $N_{\text{bnd}}(d_{\text{NC}})$ and the number of bonds $N_{\text{IF}}(d_{\text{NC}})$ terminating the NC interface. The ratio $N_{\text{bnd}}(d_{\text{NC}}[i])/N_{\text{NC}}(d_{\text{NC}}[i])$ yields the bonds per atom within zb-NCs as a gauge for the response to external stress, while the ratio $N_{\text{IF}}(d_{\text{NC}}[i])/N_{\text{bnd}}(d_{\text{NC}}[i])$ describes the ability of embedding materials to exert stress onto NCs. The impact of a highly polar surface termination on the zb-NC electronic structure is assessed by $N_{\text{IF}}(d_{\text{NC}}[i])/N_{\text{NC}}(d_{\text{NC}}[i])$ which provides a gauge to interface charge transfer [24].

While we illustrate our findings on Si NCs (diamond lattice), analytical number series introduced below are also valid for zb-NCs due to straightforward symmetry arguments. Thus, analytical descriptions below cover III-V and II-VI compounds with zb symmetry in addition to Si, SiC, SiGe and Ge. Figure 1 shows the regular NC shapes investigated: cubic ({001} faceting), octahedral ({111} faceting) and dodecahedral ({110} faceting); pyramidal ({001} base, {111} side factes) and tetragonal ({111} faceting); 111-quatrodecahedral (dominant {111} faceting plus {001} faceting) and 001-quatrodecahedral (dominant {001} faceting plus {111} faceting).

Due to the complexity of symmetry arguments, zb-NCs with higher index faceting are beyond the scope of this work. For Si, the {111} ({001}) facets have the lowest (second-lowest) experimental values of surface free energy, *cf.* table I. The occurence of {110} facets on zb-NCs is therefore less likely as compared to those with {001} and in particular {111} orientation. Facetes with {111} orientation have the lowest surface bond density for all facets up to {433} orientation [25]. These findings also hold for other diamond- and zb-NCs due to symmetry arguments.

The number series follow a run index $i$ which relates indirectly to $d_{\text{NC}}[i]$ via $N_{\text{NC}}[i]$. This connection is made by the atomic volume $V_{\text{atom}}$, yielding the NC volume as $V_{\text{NC}} = N_{\text{NC}}[i] \times V_{\text{atom}}$. Since NCs are often described as spherical, we use $d_{\text{NC}}$ for spherical NCs which allows to

---
*dirk.koenig@unsw.edu.au*
† Also at Laboratory of Nanotechnology, Dept. of Microsystems Engineering (IMTEK), University of Freiburg, Germany.

![](./images/867763047706394645_1.jpg)

FIG. 1. Diamond (zinc blende) lattice NCs considered in this work. Cubic NCs with exclusive {001} surfaces (a), octahedral NCs with exclusive {111} surfaces (b), dodecahedral NCs with exclusive {110} surfaces (c), pyramidal NCs with {001} base and {111} side surfaces (d), tetahedral NCs with exclusive {111} surfaces (e), quatrodecahedral NCs featuring {001}- and {111}-surfaces, with dominant {001} (f) and {111} (g) faceting.

<table>
<caption>TABLE I. Bond densities and free energies per square for low index Si facets. Bond density values taken from [25], experimental surface energy values taken from [26].</caption>
<thead>
<tr>
<th>facet orientation</th>
<th>surface bond density [cm⁻²]</th>
<th>surface free energy [Jm⁻²]</th>
</tr>
</thead>
<tbody>
<tr>
<td>{001}</td>
<td>1.36 × 10¹⁵</td>
<td>1.36</td>
</tr>
<tr>
<td>{110}</td>
<td>0.96 × 10¹⁵</td>
<td>1.43</td>
</tr>
<tr>
<td>{111}</td>
<td>0.78 × 10¹⁵</td>
<td>1.23</td>
</tr>
</tbody>
</table>

compare different NC shapes as function of $d_{\text{NC}}$:

$$
d_{\text{NC}}[i] = \sqrt[3]{\frac{6}{\pi}N_{\text{NC}}[i] \times V_{\text{atom}}} \tag{1}
$$

## II. ANALYTICAL NUMBERS SERIES OF NANOCRYSTAL TYPES

The derivation of number series can be lengthy and complex. Therefore, only key equations presenting final results are shown in bold print for all zb-NC types. The general algorithm is briefly explained for {110}-faceted dodecahedral NCs as an example. For brevity, we only list final results for all other NC types.

### A. {001} Cubic Zinc-Blende Nanocrystals

Nearly cubic zb-NCs are mainly encountered in nano- and micro-crystalline thin films as found in Si solar cells or ultra-large scale integration (ULSI) devices. The number of atoms forming the NC is given by the product of the atoms of the face-centered-cubic (fcc) unit cell with the cubic increase per index $i$:

$$
\mathbf{N_{\text{NC}}^{\text{cube}}[i] = 8\,\mathbf{i}^3}, \forall \mathbf{i} \geq \mathbf{1}. \tag{2}
$$

The number of bonds between NC atoms is given by

$$
\mathbf{N_{\text{bnd}}^{\text{cube}}[i] = \mathbf{i}\left[(4\mathbf{i} - 2)(4\mathbf{i} - 1) + 1\right]}, \forall \mathbf{i} \geq \mathbf{1}. \tag{3}
$$

The surface bonds of the NC are described by

$$
\mathbf{N_{\text{IF}}^{\text{cube}}[i] = 6\left[(2\mathbf{i} - 1)^2 + 3\mathbf{i} - 1\right]}, \forall \mathbf{i} \geq \mathbf{1}. \tag{4}
$$

These number series can be verified in figure 2 where atoms are color-coded in accord with their bond configuration.

### B. {111} Octahedral Zinc-Blende Nanocrystals

Exclusively {111}-faceted Si NCs correspond to the minimum Si surface energy in experiment [26] and were proven to exist up to a size of ca. 30 Å [27].

For the number of atoms forming the NC we obtain

$$
\mathbf{N_{\text{NC}}^{\text{octa}}[i] = \frac{1}{3}(\mathbf{i} + 1)\left[4(\mathbf{i} + 1)^2 - 1\right]}, \forall \mathbf{i} \geq \mathbf{0}. \tag{5}
$$

The number of bonds between NC atoms is given by

$$
\mathbf{N_{\text{bnd}}^{\text{octa}}[i] = 2\mathbf{i}(\mathbf{i} + 1) + \frac{4}{3}\mathbf{i}(\mathbf{i} + 1)(2\mathbf{i} + 1)}}, \forall \mathbf{i} \geq \mathbf{0}. \tag{6}
$$

The number series yielding the number of NC interface bonds is

$$
\mathbf{N_{\text{IF}}^{\text{octa}}[i] = 4(\mathbf{i} + 1)^2}, \forall \mathbf{i} \geq \mathbf{0}. \tag{7}
$$

The start cases of the number series ($i=0$) describe a single Si atoms with four interface bonds, presenting a silane molecule $\text{SiX}_4$, $\text{X} = \text{H}, \text{F}, \text{OH}, \text{NH}_2, \text{CH}_3$, etc. Octahedral {111}-faceted NCs described by these number series are shown in figure 3 where atoms are color-coded in accord with their bond configuration.

### C. Dodecahedral {110}-Faceted Zinc-Blende Nanocrystals

The interface termination and symmetry constraints of {110}-faceted dodecahedral NCs are significantly more complex as compared to {001}-faceted cubic NCs or {111}-faceted octahedral NCs. Figure 5 shows that there are two different types of regular {110}-dodecahedral NCs which have the same form as the Brillouin zone

![](./images/867763047706394645_2.jpg)

FIG. 2. Cubic NCs with exclusive {001} facets described by equations 2 to 4. Grey atoms have all bonds in NC. Blue atoms have two interface bonds and green atoms have three interface bonds. Graphs (a) to (f) show NCs for $i=1,2,3,4,5$ and 6, respectively, cf. table III.

![](./images/867763047706394645_3.jpg)

FIG. 3. Octahedral NCs with exclusive {111} facets described by equations 5 to 7. Grey atoms have all bonds in NC. Red atoms have one interface bond and blue atoms have two interface bonds. Graphs (a) to (f) show NCs for $i=1,2,3,4,5,6$ and 7, respectively, cf. table III.

of a body-centered cubic (bcc) lattice. These two do- decahedral NC classes will each have their own number series for $N_{\mathrm{NC}}^{\mathrm{dod}}, N_{\mathrm{bnd}}^{\mathrm{dod}}$ and $N_{\mathrm{IF}}^{\mathrm{dod}}$. Due to their alternat- ing occurence we name the class of NCs starting with the smallest NC as odd, and the class of NCs starting with the second-smallest NC as even. While it would be suffi- cient to use one NC class, we derive the number series for both classes which diminishes the size difference between adjacent NCs from 17.0 to $8.5 \mathring{A}$. We will first describe the odd class of NCs in detail and then show solutions for the even class of NCs since latter findings use the same algorithm.

The calculations of $N_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}}$ and $N_{\mathrm{bnd}, \mathrm{odd}}^{\mathrm{dod}}$ require a decomposition of dodecahedral NCs into a trunk and two tops, see figure 4. Each section type – trunk and both tops – can be described with third order differential schemes which can be transformed into $2^{\mathrm{nd}}$ order recur- sive number series with a linear term, scaling $\propto i^{3}$ as expected for a volume variable. Since the start values for $i=1$ and $i=2$ of both series are different (see equations 8, 9 and 11, 12), they cannot be directly summed up into one equation for the respective $N_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}}[i]$ or $N_{\mathrm{bnd}, \mathrm{odd}}^{\mathrm{dod}}[i]$. After we derived these number series in their recursive forms, we transform them into series which are an ex- plicit function of $i$, allowing to merge the trunk and tops sections into one series $N_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}}$ and $N_{\mathrm{bnd}, \mathrm{odd}}^{\mathrm{dod}}$.

The $3^{\mathrm{rd}}$ order differential scheme of NC atoms form- ing the trunk section is shown in table II. This scheme serves to derive equation 8, making use of the lin- ear increase of the $2^{\mathrm{nd}}$ differential quotient which is $d^{2}N_{\mathrm{NC},\mathrm{odd}}^{\mathrm{dod,trnk}}[i]/d i^{2}=16(40[i+1]-27)$. Hence, the num- ber of NC atoms forming the trunk of dodecahedral NCs is

$$
\begin{aligned}
N_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}, \mathrm{trnk}}[i] & =16(40 i-27)+2 N_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}, \mathrm{trnk}}[i-1] \\
& -N_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}, \mathrm{trnk}}[i-2], \forall i \geq 3 ; \\
& N_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}, \mathrm{trnk}}[1]=246, N_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}, \mathrm{trnk}}[2]=1336.
\end{aligned} \tag{8}
$$

Since $d^{2}N_{\mathrm{NC},\mathrm{odd}}^{\mathrm{dod,trnk}}[i]/d i^{2}$ in the differential scheme relates to $N_{\mathrm{NC},\mathrm{odd}}^{\mathrm{dod,trnk}}[i+1]$ (1488 to 3914 for $i=2$, etc.), the term $16(40[i+1]-27)$ translates to $16(40 i-27)$ in equation 8.

![](./images/867763047706394645_4.jpg)

FIG. 4. Decomposition of {110}-faceted dodecahedra. The trunk and top sections are required for deriving $N_{\mathrm{NC}}$ and $N_{\mathrm{bnd}}$ for each section type – $N_{\mathrm{NC}}^{\mathrm{dod,trnk}}, N_{\mathrm{NC}}^{\mathrm{dod,tops}}$ and $N_{\mathrm{bnd}}^{\mathrm{dod,trnk}}, N_{\mathrm{bnd}}^{\mathrm{dod,tops}}$. The sum of the sections provides the total value of $N_{\mathrm{NC}}$ and $N_{\mathrm{bnd}}$, see equations 10 and 13 for the odd index number series.

TABLE II. $3^{\text{rd}}$ order differential scheme, see text for details.

<table>
  <thead>
    <tr>
      <th>$i$</th>
      <th>$N_{\text{NC,odd}}^{\text{dod,trnk}}[i]$</th>
      <th>$\frac{d\ N_{\text{NC,odd}}^{\text{dod,trnk}}[i]}{d\ i}$</th>
      <th>$\frac{d^2\ N_{\text{NC,odd}}^{\text{dod,trnk}}[i]}{d\ i^2}$</th>
      <th>$\frac{d^3\ N_{\text{NC,odd}}^{\text{dod,trnk}}[i]}{d\ i^3}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>246</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>1336</td>
      <td>1090</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>3914</td>
      <td>2578</td>
      <td>1488</td>
      <td>640</td>
    </tr>
    <tr>
      <td>4</td>
      <td>8620</td>
      <td>4706</td>
      <td>2128</td>
      <td>640</td>
    </tr>
    <tr>
      <td>5</td>
      <td>16094</td>
      <td>7474</td>
      <td>2768</td>
      <td>640</td>
    </tr>
    <tr>
      <td>6</td>
      <td>26976</td>
      <td>10882</td>
      <td>3408</td>
      <td>640</td>
    </tr>
    <tr>
      <td>7</td>
      <td>41906</td>
      <td>14930</td>
      <td>4048</td>
      <td>640</td>
    </tr>
    <tr>
      <td>8</td>
      <td>61524</td>
      <td>19618</td>
      <td>4688</td>
      <td>$\cdots$</td>
    </tr>
    <tr>
      <td>$\cdots$</td>
      <td>$\cdots$</td>
      <td>$\cdots$</td>
      <td>$\cdots$</td>
      <td>$=\text{const}.$</td>
    </tr>
  </tbody>
</table>

We obtain the values for the two top sections along the same lines, yielding

$$
\begin{aligned}
N_{\text{NC,odd}}^{\text{dod,tops}}[i] &= 16(8i - 3) + 2N_{\text{NC,odd}}^{\text{dod,tops}}[i - 1] \\
&\quad - N_{\text{NC,odd}}^{\text{dod,tops}}[i - 2], \forall i \geq 3 ; \\
&\quad N_{\text{NC,odd}}^{\text{dod,tops}}[1] = 92,\ N_{\text{NC,odd}}^{\text{dod,tops}}[2] = 386 .
\end{aligned} \tag{9}
$$

We add both series per $i$ to yield the total number of NC atoms:

$$
N_{\text{NC,odd}}^{\text{dod}}[i] = N_{\text{NC,odd}}^{\text{dod,trnk}}[i] + N_{\text{NC,odd}}^{\text{dod,tops}}[i],\ \forall i \geq 1 . \tag{10}
$$

The same approach applies to the number of bonds connecting NC atoms. For the trunk section we get

$$
\begin{aligned}
N_{\text{bnd,odd}}^{\text{dod,trnk}}[i] &= 128(10i - 7) + 2N_{\text{bnd,odd}}^{\text{dod,trnk}}[i - 1] \\
&\quad - N_{\text{bnd,odd}}^{\text{dod,trnk}}[i - 2], \forall i \geq 3 ; \\
&\quad N_{\text{bnd,odd}}^{\text{dod,trnk}}[1] = 472,\ N_{\text{bnd,odd}}^{\text{dod,trnk}}[2] = 2600 .
\end{aligned} \tag{11}
$$

The series for the tops includes the bonds to the trunk, it is

$$
\begin{aligned}
N_{\text{bnd,odd}}^{\text{dod,tops}}[i] &= 32(8i - 5) + 2N_{\text{bnd,odd}}^{\text{dod,tops}}[i - 1] \\
&\quad - N_{\text{bnd,odd}}^{\text{dod,tops}}[i - 2], \forall i \geq 3 ; \\
&\quad N_{\text{bnd,odd}}^{\text{dod,tops}}[1] = 112,\ N_{\text{bnd,odd}}^{\text{dod,tops}}[2] = 572 .
\end{aligned} \tag{12}
$$

Again, we add both sub-series to get the total number of bonds between NC atoms:

$$
N_{\text{bnd,odd}}^{\text{dod}}[i] = N_{\text{bnd,odd}}^{\text{dod,trnk}}[i] + N_{\text{bnd,odd}}^{\text{dod,tops}}[i], \forall i \geq 1 . \tag{13}
$$

We now convert the recursive forms of $N_{\text{NC,odd}}^{\text{dod}}[i]$ and $N_{\text{bnd,odd}}^{\text{dod}}[i]$ into number series depending explicitely on $i$. When unfolding $N_{\text{NC,odd}}^{\text{dod,trnk}}[i]$ (equation 8) over $i$-terms, we obtain

$$
\begin{aligned}
N_{\text{NC,odd}}^{\text{dod,trnk}}[i] &= \\
16(40i - 27) &+ 2\left[16(40[i-1]-27)+2\cdot 16(40[i-2]-27)-16(40[i-3]-27)\dots\right] - \\
\left[16(40[i-2]-27)\right. &+ \left.2\cdot 16(40[i-3]-27)+2\cdot 16(40[i-4]-27)-16(40[i-5]-27)\dots\right] \\
&= 16 \sum_{k=1}^{i} \left[(i-k+1)(40k-27)\right] \quad + \ 2(17i+2) \\
&= 16 \left[(40i+13)\frac{i(i+1)}{2}-20\frac{i(i+1)(2i+1)}{3}\right] \quad + \ 2(17i+2) ,
\end{aligned} \tag{14}
$$

whereby the last line used the terms $\sum k^2$ and $\sum k$ to replace the respective partial sum formula [28]. The term $2(17i+2)$ is an offset derived from the intial values of equation 8. Since the start of the recursive series is fixed with $N_{\text{NC,odd}}^{\text{dod,trnk}}[1] = 246$ and $N_{\text{NC,odd}}^{\text{dod,trnk}}[2] = 1336$, we need to solve equation 14 *without the intial offset* for an intial value differential problem. We get $N_{\text{NC,odd}}^{\text{dod,trnk}} = 208, 1264, 3808, 8480 \dots$ for $i = 1, 2, 3, 4, \dots$, respectively. Comparing these values to the ones obtained from equation 8, we get offsets of $38, 72, 106, 140, \dots$ for $i = 1, 2, 3, 4, \dots$, yielding $2(17i+2)$. In the same

![](./images/867763047706394645_5.jpg)

FIG. 5. Dodecahedral NCs with exclusive {110} facets described by equations 16 and 19 to 23. Grey atoms have all bonds in NC. Red atoms have one interface bond, blue atoms have two interface bonds and green atoms have three interface bonds. Graphs (a) to (e) show NCs for $i=1_{\text{odd}}, 1_{\text{even}}, 2_{\text{odd}}, 2_{\text{even}}$, and $3_{\text{odd}}$, respectively. These NCs have to be split into two groups: NCs without atoms having three interface bonds (green) called odd due to first (a), third (c), fifth (e), etc. NC belonging into this group, and an even group (b, d) with four atoms having three interface bonds, cf. table III.

fashion, the explicit form of equation 9 is

$$
\begin{aligned}
N_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}, \mathrm{tops}}[i] &=16 \sum_{k=1}^{i}\left[(i-k+1)(8 k-3)\right] \\
& \quad+6(i+1) \\
&=16\left[(8 i+5) \frac{i(i+1)}{2}-4 \frac{i(i+1)(2 i+1)}{3}\right] \\
& \quad+6(i+1).
\end{aligned}
\label{eq15}
$$

Adding the series of equations 14 and 15 yields the odd number series of atoms forming a dodecahedral {110}-terminated zb-NC:

$$
\begin{aligned}
\mathbf{N}_{\mathrm{NC}, \mathrm{odd}}^{\mathrm{dod}}[\mathbf{i}]=16 \mathbf{i}[&(\mathbf{i}+1)(24 \mathbf{i}+9)-8(\mathbf{i}+1)(2 \mathbf{i}+1)] \\
&+10(4 \mathbf{i}+1).
\end{aligned}
\label{eq16}
$$

The number of bonds between atoms $N_{\mathrm{bnd}, \mathrm{odd}}^{\mathrm{dod}}[i]$ is derived in the same fashion, yielding

$$
\begin{aligned}
N_{\mathrm{bnd}, \mathrm{odd}}^{\mathrm{dod}, \mathrm{trnk}}[i] &=128 \sum_{k=1}^{i}\left[(i-k+1)(10 k-7)\right] \\
& \quad+8(10 i+1) \\
&=128\left[(10 i+3) \frac{i(i+1)}{2}-5 \frac{i(i+1)(2 i+1)}{3}\right] \\
& \quad+8(10 i+1)
\end{aligned}
\label{eq17}
$$

for the trunk and

$$
\begin{aligned}
N_{\mathrm{bnd}, \mathrm{odd}}^{\mathrm{dod}, \mathrm{tops}}[i] &=32 \sum_{k=1}^{i}\left[(i-k+1)(8 k-5)\right] \\
& \quad+4(3 i+1) \\
&=32\left[(8 i+3) \frac{i(i+1)}{2}-4 \frac{i(i+1)(2 i+1)}{3}\right] \\
& \quad+4(3 i+1)
\end{aligned}
\label{eq18}
$$

for the top sections. Adding both series, we get the explicit form

$$
\begin{aligned}
\mathbf{N}_{\mathrm{bnd}, \mathrm{odd}}^{\mathrm{dod}}[\mathbf{i}]=16 \mathbf{i}[&3(16 \mathbf{i}+5)(\mathbf{i}+1)-16(\mathbf{i}+1)(2 \mathbf{i}+1)] \\
&+4(23 \mathbf{i}+3).
\end{aligned}
\label{eq19}
$$

The number series for the bonds of the NCs connecting them to their environment can be solved in its explicit form:

$$
\begin{gathered}
\mathbf{N}_{\mathrm{IF}, \mathrm{odd}}^{\mathrm{dod}}[\mathbf{i}]=128 \mathbf{i}(\mathbf{i}+1)-184 \mathbf{i}+112, \\
\forall \mathbf{i} \geq \mathbf{1}.
\end{gathered}
\label{eq20}
$$

The even class of dodecahedral NCs follow derivations alike to the odd NC class, though coefficients for the number series and start elements are different. We only list the final explicit results:

$$
\begin{aligned}
\mathbf{N}_{\mathrm{NC}, \mathrm{even}}^{\mathrm{dod}}[\mathbf{i}]=16 \mathbf{i}[&(24 \mathbf{i}+21)(\mathbf{i}+1)-8(\mathbf{i}+1)(2 \mathbf{i}+1)] \\
&+88(\mathbf{i}+1)
\end{aligned}
\label{eq21}
$$

$$
\begin{aligned}
\mathbf{N}_{\mathrm{bnd}, \mathrm{even}}^{\mathrm{dod}}[\mathbf{i}]=16 \mathbf{i}[&3(16 \mathbf{i}+13)(\mathbf{i}+1)-16(\mathbf{i}+1)(2 \mathbf{i}+1)] \\
&+140(\mathbf{i}+1).
\end{aligned}
\label{eq22}
$$

Again, the number series of NC interface bonds is explicit:

$$
\mathbf{N}_{\mathrm{IF}, \mathrm{even}}^{\mathrm{dod}}[\mathbf{i}]=128 \mathbf{i}(\mathbf{i}+1)-56 \mathbf{i}+136, \forall \mathbf{i} \geq \mathbf{1}. \quad(23)
$$

**TABLE III.** First members of geometrical series of the number of atoms contained in a NC $N_\text{NC}$, the number of bonds between such atoms $N_\text{bnd}$, the interface bonds of the NC $N_\text{IF}$ for zb-NCs with exclusive {001} facetting (cubes), {111}-facetting (octahedra) and {110}-facetting (dodecahedra), and the equivalent diameter $d_\text{NC}$ when its volume is considered as sphere to allow for comparison between different NC shapes. An atomic volume for Si of $V_\text{atom}=20.024$ $\text{\AA}^3$ was used.

<table>
  <tr>
    <td>$i$</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
  </tr>
</table>

cubic shape, {001} surfaces

<table>
  <tr>
    <td>$N_\text{NC}$</td>
    <td>8</td>
    <td>64</td>
    <td>216</td>
    <td>512</td>
    <td>1000</td>
    <td>1728</td>
    <td>2744</td>
  </tr>
  <tr>
    <td>$N_\text{bnd}$</td>
    <td>7</td>
    <td>86</td>
    <td>333</td>
    <td>844</td>
    <td>1715</td>
    <td>3042</td>
    <td>4921</td>
  </tr>
  <tr>
    <td>$N_\text{IF}$</td>
    <td>18</td>
    <td>84</td>
    <td>198</td>
    <td>360</td>
    <td>570</td>
    <td>828</td>
    <td>1134</td>
  </tr>
  <tr>
    <td>$d_\text{NC}$ [Å]</td>
    <td>6.74</td>
    <td>13.5</td>
    <td>20.2</td>
    <td>27.0</td>
    <td>33.7</td>
    <td>40.4</td>
    <td>47.2</td>
  </tr>
  <tr>
    <td>Figure</td>
    <td>2a</td>
    <td>2b</td>
    <td>2c</td>
    <td>2d</td>
    <td>2e</td>
    <td>2f</td>
    <td></td>
  </tr>
</table>

octahedral shape, {111} surfaces

<table>
  <tr>
    <td>$N_\text{NC}$</td>
    <td>10</td>
    <td>35</td>
    <td>84</td>
    <td>165</td>
    <td>286</td>
    <td>455</td>
    <td>680</td>
  </tr>
  <tr>
    <td>$N_\text{bnd}$</td>
    <td>12</td>
    <td>52</td>
    <td>136</td>
    <td>280</td>
    <td>500</td>
    <td>812</td>
    <td>1232</td>
  </tr>
  <tr>
    <td>$N_\text{IF}$</td>
    <td>16</td>
    <td>36</td>
    <td>64</td>
    <td>100</td>
    <td>144</td>
    <td>196</td>
    <td>256</td>
  </tr>
  <tr>
    <td>$d_\text{NC}$ [Å]</td>
    <td>7.26</td>
    <td>11.0</td>
    <td>14.8</td>
    <td>18.5</td>
    <td>22.2</td>
    <td>25.9</td>
    <td>29.6</td>
  </tr>
  <tr>
    <td>Figure</td>
    <td>3a</td>
    <td>3b</td>
    <td>3c</td>
    <td>3d</td>
    <td>3e</td>
    <td>3f</td>
    <td>3g</td>
  </tr>
</table>

dodecahedral shape, {110} surfaces

<table>
  <tr>
    <td>$i$</td>
    <td>$1_\text{odd}$</td>
    <td>$1_\text{even}$</td>
    <td>$2_\text{odd}$</td>
    <td>$2_\text{even}$</td>
    <td>$3_\text{odd}$</td>
    <td>$3_\text{even}$</td>
    <td>$4_\text{odd}$</td>
  </tr>
  <tr>
    <td>$N_\text{NC}$</td>
    <td>338</td>
    <td>848</td>
    <td>1722</td>
    <td>3048</td>
    <td>4930</td>
    <td>7456</td>
    <td>10730</td>
  </tr>
  <tr>
    <td>$N_\text{bnd}$</td>
    <td>584</td>
    <td>1528</td>
    <td>3172</td>
    <td>5700</td>
    <td>9312</td>
    <td>14192</td>
    <td>20540</td>
  </tr>
  <tr>
    <td>$N_\text{IF}$</td>
    <td>184</td>
    <td>336</td>
    <td>512</td>
    <td>792</td>
    <td>1096</td>
    <td>1504</td>
    <td>1936</td>
  </tr>
  <tr>
    <td>$d_\text{NC}$ [Å]</td>
    <td>23.5</td>
    <td>31.9</td>
    <td>40.4</td>
    <td>48.9</td>
    <td>57.4</td>
    <td>65.8</td>
    <td>74.3</td>
  </tr>
  <tr>
    <td>Figure</td>
    <td>5a</td>
    <td>5b</td>
    <td>5c</td>
    <td>5d</td>
    <td>5e</td>
    <td></td>
    <td></td>
  </tr>
</table>

Minor oscillations of $N_\text{IF}^\text{dod}[i]$ occur for small NCs due to alternating odd and even terms, *cf.* Figs. 4b and 11. These originate from different interface bond configurations for odd and even NC series, see figure 5. The origin of this irregular behavior is found in the less perfect termination of {110} facets due to the more complex geometry of {110} surfaces in compound with their inter-facet angles being obtuse at all edges. These imperfections are less dominant for small dodecahedra due to the small area of rhomboid {110}-facets since there are less chains of {110}-oriented surface atoms. These chains have an atom with two interface bonds at each end which contributes to $N_\text{IF}^\text{dod}[i]$.

### D. Tetrahedral Zinc-Blende Nanocrystals

With exclusive {111} facetting of zb-NCs, the resulting tetrahedral NCs can also be seen as regular pyramids with three sides. For the number of NC atoms forming the tetrahedral {111} zb-NC we get

$$
\begin{aligned}
\mathbf{N}_\text{NC}^\text{tetra}[\mathbf{i}] &= \frac{\mathbf{1}}{\mathbf{6}} \mathbf{i} (\mathbf{i} + \mathbf{1}) (2\mathbf{i} + \mathbf{1}) + (\mathbf{i} + \mathbf{1})^\mathbf{2}, \\
&\forall \mathbf{i} \geq \mathbf{0},
\end{aligned} \tag{24}
$$

The bonds between such NC atoms are described by

$$
\begin{aligned}
\mathbf{N}_\text{bnd}^\text{tetra}[\mathbf{i}] &= \frac{\mathbf{1}}{\mathbf{3}} \mathbf{i} (\mathbf{i} + \mathbf{1}) (2\mathbf{i} + \mathbf{1}) + \mathbf{i} (\mathbf{i} + \mathbf{1}), \\
&\forall \mathbf{i} \geq \mathbf{0}.
\end{aligned} \tag{25}
$$

The number of interface bonds connecting these NCs to their embedding matrix or attached ligands is given by

$$
\mathbf{N}_\text{IF}^\text{tetra}[\mathbf{i}] = 2(\mathbf{i} + \mathbf{1}) (\mathbf{i} + \mathbf{2}), \ \forall \mathbf{i} \geq \mathbf{0}. \tag{26}
$$

Equation 26 deviates from equations 7 and 29 because base and side areas of a tetragonal zb-NC with {111} facetting are identical.

### E. {111}-{001} Pyramidal Zinc-Blende Nanocrystals

Pyramidal NCs consist of four triangular {111} side facets and a square {001}-oriented base. Such NCs are relevant in particular for epitaxial growth of III-V quantum dots (QDs) [29, 30]. The number of atoms forming the NC are

$$
\begin{aligned}
\mathbf{N}_\text{NC}^\text{pyra}[\mathbf{i}] &= \frac{\mathbf{1}}{\mathbf{6}} \mathbf{i} (\mathbf{i} + \mathbf{1}) \left[ 2(2\mathbf{i} + \mathbf{1}) + \mathbf{9} \right] + \mathbf{i} + \mathbf{1}, \\
&\forall \mathbf{i} \geq \mathbf{0}.
\end{aligned} \tag{27}
$$

The bonds between such NC atoms are described by

$$
\mathbf{N}_\text{bnd}^\text{pyra}[\mathbf{i}] = \frac{\mathbf{2}}{\mathbf{3}} \mathbf{i} (\mathbf{i} + \mathbf{1}) (2\mathbf{i} + \mathbf{1}) + \mathbf{i} (\mathbf{i} + \mathbf{1}), \ \forall \mathbf{i} \geq \mathbf{0}. \tag{28}
$$

The number of NC interface bonds is given by

$$
\mathbf{N}_\text{IF}^\text{pyra}[\mathbf{i}] = 4(\mathbf{i} + \mathbf{1})^\mathbf{2}, \forall \mathbf{i} \geq \mathbf{0}, \tag{29}
$$

The identity of equations 7 and 29 shows the resemblance of symmetry arguments of both series which is underlined by the start term ($i=0$) describing $\text{SiX}_4$ in both cases.

### F. Quatrodecahedral Zinc-Blende Nanocrystals with Dominant {111}-Facetting (Truncated Octahedra)

The {111}-dominated quatrodecahedra are NCs which are limited by eight regular {111}-faceted hexagons and six {001}-faceted squares, see figure 8a to d. Quantities for these NCs can be derived from truncating {111}-faceted octahedra (Section II B) at their six corners, making use of the number series we obtained for the pyramids

![](./images/867763047706394645_6.jpg)

FIG. 6. Tetrahedral NCs with exclusive {111} faceting as described by equations 24 to 26. For atoms colors, see figure 5. Graphs (a) to (g) show tetrahedral NCs for $i=1,2,3,4,5,6$ and 7, respectively, see also table IV.

![](./images/867763047706394645_7.jpg)

FIG. 7. Pyramidal NCs with {001} base surface and {111} side surfaces as described by equations 27 to 29. Graphs (a) to (g) show pyramid-shape NCs for $i=1,2,3,4,5,6$ and 7, respectively, see also table IV.

TABLE IV. First members of geometrical series for tetrahedral zb-NCs with exclusive {111}-faceting and pyramidal zb-NCs with {111}-oriented side areas and {001} base, see table III for further details.

<table>
  <tr>
    <td>$i$</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
  </tr>
</table>

tetragonal shape, {111} surfaces
<table>
  <tr>
    <td>$N_{\text{NC}}$</td>
    <td>5</td>
    <td>14</td>
    <td>30</td>
    <td>55</td>
    <td>91</td>
    <td>140</td>
    <td>204</td>
  </tr>
  <tr>
    <td>$N_{\text{bnd}}$</td>
    <td>4</td>
    <td>16</td>
    <td>40</td>
    <td>80</td>
    <td>140</td>
    <td>224</td>
    <td>336</td>
  </tr>
  <tr>
    <td>$N_{\text{IF}}$</td>
    <td>12</td>
    <td>24</td>
    <td>40</td>
    <td>60</td>
    <td>84</td>
    <td>112</td>
    <td>144</td>
  </tr>
  <tr>
    <td>$d_{\text{NC}}$ [Å]</td>
    <td>5.8</td>
    <td>8.1</td>
    <td>10.5</td>
    <td>12.8</td>
    <td>15.2</td>
    <td>17.5</td>
    <td>19.8</td>
  </tr>
  <tr>
    <td>Figure</td>
    <td>6a</td>
    <td>6b</td>
    <td>6c</td>
    <td>6d</td>
    <td>6e</td>
    <td>6f</td>
    <td>6g</td>
  </tr>
</table>

pyramidal shape, {001} base, {111} sides
<table>
  <tr>
    <td>$N_{\text{NC}}$</td>
    <td>7</td>
    <td>22</td>
    <td>50</td>
    <td>95</td>
    <td>161</td>
    <td>252</td>
    <td>372</td>
  </tr>
  <tr>
    <td>$N_{\text{bnd}}$</td>
    <td>6</td>
    <td>26</td>
    <td>68</td>
    <td>140</td>
    <td>250</td>
    <td>406</td>
    <td>616</td>
  </tr>
  <tr>
    <td>$N_{\text{IF}}$</td>
    <td>16</td>
    <td>36</td>
    <td>64</td>
    <td>100</td>
    <td>144</td>
    <td>196</td>
    <td>256</td>
  </tr>
  <tr>
    <td>$d_{\text{NC}}$ [Å]</td>
    <td>6.4</td>
    <td>9.4</td>
    <td>12.4</td>
    <td>15.4</td>
    <td>18.3</td>
    <td>21.3</td>
    <td>24.2</td>
  </tr>
  <tr>
    <td>Figure</td>
    <td>7a</td>
    <td>7b</td>
    <td>7c</td>
    <td>7d</td>
    <td>7e</td>
    <td>7f</td>
    <td>7g</td>
  </tr>
</table>

(Section II E), cf. figure 8e. We start again with the series yielding the number of NC atoms:
$$
\begin{aligned}
\mathbf{N}_{\text{NC}}^{\mathbf{q.111}}[\mathbf{i}] & =9 \mathbf{i}(2 \mathbf{i}+1)^{2}+(2 \mathbf{i}+1) \\
& -\mathbf{i}(4 \mathbf{i}+5)(\mathbf{i}+1), \quad orall \mathbf{i} \geq \mathbf{1}.
\end{aligned} \tag{30}
$$

The bonds between such NC atoms are described by
$$
\begin{aligned}
\mathbf{N}_{\text{bnd}}^{\mathbf{q.111}}[\mathbf{i}] & =2 \mathbf{i}(3 \mathbf{i}+1)(12 \mathbf{i}+5) \\
& -[4 \mathbf{i}(\mathbf{i}+1)(2 \mathbf{i}+1)+6 \mathbf{i}(\mathbf{i}+1)], \quad orall \mathbf{i} \geq \mathbf{1}.
\end{aligned} \tag{31}
$$

The number of interface bonds which connect these NCs to an embedding matrix or attached ligands is given by
$$
\mathbf{N}_{\text{IF}}^{\mathbf{q.111}}[\mathbf{i}]=(6 \mathbf{i}+2)^{2}, \quad orall \mathbf{i} \geq \mathbf{1}. \tag{32}
$$

For facilitating interpretations of electron paramagnetic resonance (EPR) data of SiO₂-embedded Si NCs [31] as discussed in section IV, we decompose $N_{\text{bnd}}^{\text{q.111}}[i]$ into a fraction of bonds originating from the six {001} facets where each atom has two interface bonds (blue atoms in figure 8a to d)
$$
N_{\mathrm{IF},\langle 001\rangle}^{\mathrm{q}.111}[i]=12(i+1)^{2}, \quad orall i \geq 1, \tag{33}
$$

and another fraction originating from {111} facets where each atom has one interface bond (red atoms in figure 8a to d)
$$
N_{\mathrm{IF},\langle 111\rangle}^{\mathrm{q}.111}[i]=8\left(3 i^{2}-1\right), \quad orall i \geq 1. \tag{34}
$$

### G. Quatrodecahedral Zinc-Blende Nanocrystals with Dominant {001}-Faceting (Truncated Cubes)

Here, the situation is more complex. The truncated corners of the cubic NC have a low symmetry as evident from different triangular facets having {001} orientations for side areas with angles of 45, 45 and 90° and a {111}-oriented base with three 60° angles. These truncated corners cannot be decribed by pyramids (Section II E) or tetrahedra (Section II D). As illustrated in section II C for dodecahedral {110}-terminated zb-NCs, these NCs can be described with third order differential schemes which can be transformed into 2ⁿᵈ order recursive number series and eventually into an explicit form of $N_{\text{NC}}^{\text{q.001}}[i]$ and

![](./images/867763047706394645_8.jpg)

FIG. 8. Quatrodecahedral Zinc-Blende Nanocrystals with Dominant {111}-faceting as described by equations 30 to 32 (a, b, c, d). For atoms colors, see figure 5. Graphs (a) to (d) show NCs for $i=1,2,3$ and 4, respectively, see table V. Decomposition of {111}-faceted octahedron into six pyramidal {001}-{111} NCs and a dominantly {111}-faceted quatrodecahedral NC (e). The bottom atom layers of the pyramidal NCs are part of the {111}-dominated quatrodecahedral NC to achieve its symmetry and shape.

$$
\begin{aligned}
\mathrm{N}_{\mathrm{bnd}}^{\mathrm{q}, 001}[\mathrm{i}]=& \\
& 4\left[6(\mathrm{i}+3)^{2}+(\mathrm{i}+1)\left(\mathrm{i}\left\{\frac{10}{3} \mathrm{i}+\frac{11}{3}\right\}+\frac{9}{2} \mathrm{i}+5\right)+7(2 \mathrm{i}+3)(\mathrm{i}+2)\right], \forall \mathrm{i} \geq 1.
\end{aligned}
\tag{36}
$$

The number of interface bonds for these NCs is given by
$$
\mathrm{N}_{\mathrm{IF}}^{\mathrm{q}, 001}[\mathrm{i}]=4(2 \mathrm{i}+7)^{2}, \forall \mathrm{i} \geq 1.
\tag{37}
$$

As for dominantly {001}-faceted quatrodecahedra, we decompose $N_{\mathrm{IF}}^{\mathrm{q}, 001}[i]$ into {001} and {111} partitions to facilitate data interpretation for EPR measurements of $\mathrm{SiO}_{2}$-embedded Si NCs [31], see section IV. The {001} fraction of bonds originates from the six {001} facets where blue atoms have two interface bonds, $c f$. figure 9, and 12 green atoms with three interface bonds, the

$N_{\text {bnd }}^{\mathrm{q}, 001}[i]:$

$$
\begin{aligned}
\mathrm{N}_{\mathrm{NC}}^{\mathrm{q}, 001}[\mathrm{i}]=&(2 \mathrm{i}+7)\left[(\mathrm{i}+4)^{2}+\frac{2}{3}(\mathrm{i}+3)\left(\mathrm{i}+\frac{5}{2}\right)\right] \\
&+2(\mathrm{i}+3)\left[(\mathrm{i}+4)^{2}+\mathrm{i}\right] \\
&+\frac{4}{3}(\mathrm{i}+1)(\mathrm{i}+2)(\mathrm{i}+3), \forall \mathrm{i} \geq 1
\tag{35}
\end{aligned}
$$

and

![](./images/867763047706394645_9.jpg)

FIG. 9. Quatrodecahedral Zinc-Blende Nanocrystals with dominant {001}-faceting as described by equations 35 to 37. For atoms colors, see figure 5. Graphs (a) to (d) show NCs for $i=1,2,3$ and 4, respectively, see table V.

latter accounting for the 36 added in equation 38.

$$
\begin{aligned}
N_{\mathrm{IF},\langle 001\rangle}^{\mathrm{q}, 001}[i] & =12\left[(i+4)^{2}-4\right]+36 \\
& =12\left[(i+4)^{2}-1\right], \forall i \geq 1.
\end{aligned}\qquad(38)
$$

The fraction which originates from {111} facets where each atom has one interface bond (red atoms in figure 9) is described by

$$
N_{\mathrm{IF},\langle 111\rangle}^{\mathrm{q}, 001}[i]=4(i+2)^{2}, \forall i \geq 1.\qquad(39)
$$

## III. RESULTS

The ratio $N_{\mathrm{bnd}}(d_{\mathrm{NC}}[i])/N_{\mathrm{NC}}(d_{\mathrm{NC}}[i])$ provides the number of bonds per atom within the zb-NC, the asymptotic limit $\lim_{i \to \infty}(N_{\mathrm{bnd}}[i]/N_{\mathrm{NC}}[i])=2$ describes the bulk case: The considered atom has four bonds, each shared with a first next neighbour (1-nn) atom. A finite crystal has outermost bonds missing as these connect the NC with its environment which results in $N_{\mathrm{bnd}}/N_{\mathrm{NC}}$ increasingly declining below 2 with shrinking $d_{\mathrm{NC}}[i]$, $cf$. figure 10.

Depending on the NC form and faceting, $N_{\mathrm{bnd}}(d_{\mathrm{NC}}[i])/N_{\mathrm{NC}}(d_{\mathrm{NC}}[i])$ can vary in particular for small NCs.

Exclusively {111}-faceted octahedra have the highest value per NC size $d_{\mathrm{NC}}$ by combining a low volume-to-surface ratio with a minimum surface bond density,

TABLE V. First members of geometrical series for quatrodecahedral zb-NCs with dominant {111}- and {001}-faceting. Partitions $N_{\mathrm{IF},\langle 001\rangle}[i]$ and $N_{\mathrm{IF},\langle 111\rangle}[i]$ are discussed in section IV. For further details see table III.

<table>
<thead>
  <tr>
    <th>$i$</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="8">quatrodecahedral shape, {111}-dominant</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{NC}}$</td>
    <td>66</td>
    <td>377</td>
    <td>1126</td>
    <td>2505</td>
    <td>4706</td>
    <td>7921</td>
    <td>12342</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{bnd}}$</td>
    <td>100</td>
    <td>656</td>
    <td>2052</td>
    <td>4672</td>
    <td>8900</td>
    <td>15120</td>
    <td>23716</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{IF}}$</td>
    <td>64</td>
    <td>196</td>
    <td>400</td>
    <td>676</td>
    <td>1024</td>
    <td>1444</td>
    <td>1936</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{IF},\langle 001\rangle}$</td>
    <td>48</td>
    <td>108</td>
    <td>192</td>
    <td>300</td>
    <td>432</td>
    <td>588</td>
    <td>768</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{IF},\langle 111\rangle}$</td>
    <td>12</td>
    <td>88</td>
    <td>208</td>
    <td>376</td>
    <td>592</td>
    <td>856</td>
    <td>1168</td>
  </tr>
  <tr>
    <td>$d_{\mathrm{NC}}$ [Å]</td>
    <td>13.6</td>
    <td>24.3</td>
    <td>35.1</td>
    <td>45.8</td>
    <td>56.5</td>
    <td>67.2</td>
    <td>77.9</td>
  </tr>
  <tr>
    <td>Figure</td>
    <td>8a</td>
    <td>8b</td>
    <td>8c</td>
    <td>8d</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="8">quatrodecahedral shape, {001}-dominant</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{NC}}$</td>
    <td>549</td>
    <td>1021</td>
    <td>1707</td>
    <td>2647</td>
    <td>3881</td>
    <td>5449</td>
    <td>7391</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{bnd}}$</td>
    <td>936</td>
    <td>1800</td>
    <td>3076</td>
    <td>4844</td>
    <td>7184</td>
    <td>10176</td>
    <td>13900</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{IF}}$</td>
    <td>324</td>
    <td>484</td>
    <td>676</td>
    <td>900</td>
    <td>1156</td>
    <td>1444</td>
    <td>1764</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{IF},\langle 001\rangle}$</td>
    <td>288</td>
    <td>420</td>
    <td>576</td>
    <td>756</td>
    <td>960</td>
    <td>1188</td>
    <td>1440</td>
  </tr>
  <tr>
    <td>$N_{\mathrm{IF},\langle 111\rangle}$</td>
    <td>36</td>
    <td>64</td>
    <td>100</td>
    <td>144</td>
    <td>196</td>
    <td>256</td>
    <td>324</td>
  </tr>
  <tr>
    <td>$d_{\mathrm{NC}}$ [Å]</td>
    <td>27.6</td>
    <td>33.9</td>
    <td>40.3</td>
    <td>46.6</td>
    <td>53.0</td>
    <td>59.3</td>
    <td>65.7</td>
  </tr>
  <tr>
    <td>Figure</td>
    <td>9a</td>
    <td>9b</td>
    <td>9c</td>
    <td>9d</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

![](./images/867763047706394645_10.jpg)

FIG. 10. Ratio of bonds per NC atom within NC $\boldsymbol{N_{\mathrm{bnd}}/N_{\mathrm{NC}}}$, shown for cubic (cube), octahedral (octa), dodecahedral (dod), pyramidal (pyra), tetrahedral (tetra), {001}-dominated (quatro-001) and {111}-dominated (quatro-111) quatrodecahedral NCs. For size values at bottom and associated $N_{\mathrm{bnd}}/N_{\mathrm{NC}}$ values as function of NC shape, see Section IV and figure 7 in [17]. Inset zooms up range for 40 to 300 nm NC size to show asymptotic behavior. Lines were used to minimize obstruction.

$cf$. table I. Quatrodecahedra with dominant {111}-

![](./images/867763047706394645_11.jpg)

FIG. 11. Ratio of interface bonds per NC to number of NC atoms $N_{\text{IF}}/N_{\text{NC}}$. The values of $N_{\text{IF}}/N_{\text{NC}}$ shown for cubic and octahedral NCs at 7 nm refer to the minimum size limit below which a strong dielectric embedding or coating the NC will dominate its electronic properties [24]. Cubic high symmetry zb-NCs are dominated by the dielectric up to $d_{\text{NC}}=12$ nm (dashed blue line), lower symmetry NCs like Si cubic fins of fin-FETs are dominated up to even bigger $d_{\text{NC}}$ due to cubicle shape driving up $N_{\text{IF}}/N_{\text{NC}}$. For legend description see figure 10.

facetting and square {001} facets have the next highest ratio $N_{\text{bnd}}(d_{\text{NC}}[i])/N_{\text{NC}}(d_{\text{NC}}[i])$. The latter facets cause an increase of $N_{\text{IF}}[i]$. Both NCs types are closely followed by dodecahedral NCs with exclusive {110}-facetting. Although dodecahedra have a higher volume-to-surface ratio as compared to octahedra, their more complex {110} facetting results in a less perfect surface termination. Thereby, the number of bonds within the NC is decreased, the missing bonds are added to the number of interface bonds $N_{\text{IF}}[i]$. Dodecahedra are followed by {111}-tetrahedra which have less favourable (smaller) volume-to-surface ratios. However, the minimum bond density of {111} surfaces (see table I) yields high $N_{\text{bnd}}(d_{\text{NC}}[i])/N_{\text{NC}}(d_{\text{NC}}[i])$ values. These NCs are followed by pyramids with {001} base and {111} side facets. We obtain the lowest values for $N_{\text{bnd}}(d_{\text{NC}}[i])/N_{\text{NC}}(d_{\text{NC}}[i])$ for {001}-faceted cubic NCs. This is straightforward to show by their unfavourable volume-to-surface ratio combined with the maximum bond density of {001}-facets, $cf.$ table I.

The ratio $N_{\text{IF}}(d_{\text{NC}}[i])/N_{\text{NC}}(d_{\text{NC}}[i])$ yields the number of interface bonds per NC atom, see figure 11. This key parameter quantifies electronic phenomena occurring across NC interfaces, see section IV. It follows the opposite trend as discussed for $N_{\text{bnd}}(d_{\text{NC}}[i])/N_{\text{NC}}(d_{\text{NC}}[i])$: Any bond not available for connecting NC atoms occurs at an interface. The irregular behavior of {110}-faceted dodecahedra also occurs for $N_{\text{IF}}(d_{\text{NC}}[i])/N_{\text{NC}}(d_{\text{NC}}[i])$ for reasons discussed above. Elongated zb-NCs have a higher ratio $N_{\text{IF}}/N_{\text{NC}}$ which results in bigger $d_{\text{NC}}$ values up to which the embedding dielectric dominates electronic and optical NC properties. This finding is crucial for {001}-terminated Si cubicles as encountered in fin-FETs to exploit nanoscopic phenomena such as ultrathin $\text{SiO}_2$ and $\text{Si}_3\text{N}_4$ coatings which can replace conventional doping while maintaining CMOS-compatibility for ULSI devices [24].

The quantity $N_{\text{IF}}(d_{\text{NC}}[i])/N_{\text{bnd}}(d_{\text{NC}}[i])$ provides the number of interface bonds per bond between NC atoms, see figure 12. With increasing $d_{\text{NC}}[i]$, the behaviour of $N_{\text{IF}}/N_{\text{bnd}}$ converges against $\frac{1}{2}N_{\text{IF}}/N_{\text{NC}}$ due to $\lim_{i\rightarrow\infty}(N_{\text{bnd}}[i]/N_{\text{NC}}[i])=2$, $cf.$ figure 10.

![](./images/867763047706394645_12.jpg)

FIG. 12. Ratio of interface bonds per NC to bonds between atoms of NC $N_{\text{IF}}/N_{\text{bnd}}$. Size values refer to smallest observed Si NCs and biggest observed size for octahedral Si NCs, see section IV for further explanation. A linear interpolation between values of the number series for {111}-octahedral and {001}-cubic zb-NCs was used to estimate the size range discussed in the text. For legend description see figure 10.

## IV. APPLICATIONS

The ratio $N_{\text{bnd}}/N_{\text{NC}}$ yields information about the NC response to external stress like NC lattice deformation. As example, $N_{\text{bnd}}/N_{\text{NC}}$ is a gauge for the NC stress response to attempts of dopant formation on Si NC lattice sites, triggering self-purification [17, 22]. Numerical values of $d_{\text{NC}}$ and $N_{\text{bnd}}/N_{\text{NC}}$ in figure 10 refer to figure 7 in [17] where donor formation was shown to decrease from $6\times10^{-3}$ for 20 nm Si NCs via $1.3\times10^{-4}$ for 10 nm Si NCs to $3\times10^{-5}$ for 4.5 nm Si NCs. We can thus derive that self-purification for free-standing Si NCs prevents dopant formation in the NC lattice for $N_{\text{bnd}}/N_{\text{NC}}\leq1.92\pm0.02$. We can narrow down this range further if the preferential shape of the NCs was known. Figure 7 in [17] also shows increased standard deviations of doping efficiencies with shrinking NC size which may originate from an increasing relative size deviation with shrinking NC size. However,

we note that $N_{\rm bnd}/N_{\rm NC}$ values cover a wider range with shrinking $d_{\rm NC}$ which may add to the uncertainty in EPR measurements and NC counter-stress related phenomena in general if the NC shape is not known or NC ensembles have no strong preference in shape and faceting. In a similar fashion, $N_{\rm bnd}/N_{\rm NC}$ can be useful for investigat- ing dopant clustering in ULSI devices [32, 33] as function of Si nanovolume shape, size and interface orientation.

The ratio $N_{\rm IF}(d_{\rm NC})/N_{\rm NC}(d_{\rm NC})$ presents a gauge for the impact of interface charge transfer [24, 34] and in- terface dipoles [35-37] onto NCs. Both phenomena have a major influence on NC electronic and optical proper- ties. Interface charge transfer dominates electronic struc- tures of Si NCs for $d_{\rm NC} \geq 70$ Å [24, 38], correspond- ing values of $N_{\rm IF}(d_{\rm NC})/N_{\rm NC}(d_{\rm NC})$ are shown in figure 11 for {001}-faceted cubic and {111}-faceted octahedral Si NCs, presenting maxium and minimum values, respec- tively. Figure 11 shows that cubic high symmetry zb- NCs are dominated by the dielectric for $d_{\rm NC} \leq 12$ nm (dashed blue line). For lower symmetry NCs like Si cubi- cles of fin-FETs, the size limit of $d_{\rm NC}$ where the impact of the embedding dielectric dominates the electronic struc- ture of the NC increases further due to an increased ratio $N_{\rm IF}/N_{\rm NC}$ [24].

Partitions of $N_{\rm IF}(d_{\rm NC}[i])$ as function of surface orientation can be a cornerstone to quantify EPR-active Si dangling bonds (DBs) at ${\rm NC/SiO_2}$ interfaces [31]. Specific interface defect densities of Si DBs, $P_{b(0)}$ and $P_{b1}$, were assigned to {001} and {111} planes [39, 40]. Si NC shapes were estimated by $P_{b(0)}/P_{b1}$ EPR signal ratios, leading to the postulation of Si NCs [41] alike to {001}-dominated octahedra (section II G). Partitions of {001} and {111} planes $N_{\rm IF,\langle 001\rangle}(d_{\rm NC}[i])$ and $N_{\rm IF,\langle 111\rangle}(d_{\rm NC}[i])$ for {001}- and {111}-dominated quatrodecahedral Si NCs (equations 38, 39 and 33, 34, respectively) can be used to interprete EPR data to obtain the dominant NC shape or - if the dominant NC shape is known - an estimate for the average NC size. The terms $N_{\rm IF,\langle 001\rangle}^{q.001}(d_{\rm NC}[i])/N_{\rm IF,\langle 111\rangle}^{q.001}(d_{\rm NC}[i])$ and $N_{\rm IF,\langle 001\rangle}^{q.111}(d_{\rm NC}[i])/N_{\rm IF,\langle 111\rangle}^{q.111}(d_{\rm NC}[i])$ yield ratios of {001}- to {111}-oriented interface bonds for which the density of $P_{b(0)}$ and $P_{b1}$ defects are well known from {001}- and {111}-oriented ${\rm Si/thermal\ SiO_2}$ interfaces [39, 40]. Figure 13 shows these terms as function of $d_{\rm NC}[i]$. Asymptotic values for infinite NC size are $\lim_{i \to \infty} \left[ N_{\rm IF,\langle 001\rangle}^{q.111}(d_{\rm NC}[i])/N_{\rm IF,\langle 111\rangle}^{q.111}(d_{\rm NC}[i]) \right] = 1/2$ for {111}-dominated quatrodecahedra and $\lim_{i \to \infty} \left[ N_{\rm IF,\langle 001\rangle}^{q.001}(d_{\rm NC}[i])/N_{\rm IF,\langle 111\rangle}^{q.001}(d_{\rm NC}[i]) \right] = 3$ for {001}-dominated quatrodecahedra. No overlap exists between both ratios for finite NC size which allows for a clear assignment of either dominant shape or size of NCs, depending on what parameter is already known.

The quantity $N_{\rm IF}/N_{\rm bnd}$ serves as gauge for the stress balance between NCs and an embedding matrix interact- ing via interface bonds such as Si NCs in ${\rm SiO_2}$ or strain- balanced growth of InAs QDs in GaNAs [13-15]. High resolution transmission Electron Microscopy (HR-TEM) was used to determine the size of Si NCs grown by seg- regation from Si-rich dielectrics. Smallest Si NC exten- sions were found to be 15 Å, and {111}-faceted octahedra dominated the shape of Si NCs up to ca. 30 Å [27]. Dis- integration of porous Si by etching and subsequent self- limiting oxidation of Si NCs obtained this way resulted in minimum NC sizes of 12 to 17 Å [42], the smallest range reported to date for Si NCs obtained by solid-state synthesis. Minimum values of $d_{\rm NC}=15$ Å were obtained from gas phase synthesis [17]. The minimum diameter of embedded Si NCs should depend on the external stress exerted onto the Si atomic cluster which appears to yield an amorphous structure below $d_{\rm NC}=15 \pm 2$ Å. The pre- dominant existence of embedded Si NCs as {111}-faceted octahedra can be explained by their minimum ratio of $N_{\rm IF}/N_{\rm bnd}$ which reduces stress exertion. Moreover, Si NC shapes get increasingly polymorphous for sizes be- yond 30 Å where $N_{\rm IF}/N_{\rm bnd}$ of all other Si NC shapes drops below $N_{\rm IF}^{octa}/N_{\rm bnd}^{octa}$ at $d_{\rm NC}^{octa}=15$ Å, see figure 12. We can therefore derive an upper limit of the bond ratio $N_{\rm IF}/N_{\rm bnd} = \frac{1}{476}(197 \pm 27) \approx 0.414 \pm 0.057$ below which Si NCs form out of Si-rich ${\rm SiO_2}$ or amorphous clusters. For the latter, surface tension appears to be the limit- ing factor of minimum NC size [43]. Such empirical val- ues of $N_{\rm IF}/N_{\rm bnd}$ are a function of the zb solid and its embedding environment and can be derived for any zb NCs with appropriate experimental input. Using mate- rial data such as Young's modulus and diffusion coeffi- cients during the NC formation process, we can extrap- olate the findings for Si to arrive at estimates for other group IV NCs such as Ge, SiGe and SiC. As an example, the limit of $N_{\rm IF}/N_{\rm bnd}$ for Si NCs formed by segregation

![](./images/867763047706394645_13.jpg)

FIG. 13. Ratio of {001} to {111} interface bonds for {111}- and {001}-dominant quatrodecahedral zb- NCs. Lines show asymptotic values for $d_{\rm NC}[i] \to \infty$ of {111}-dominated (blue) and {001}-dominated quatrodecahe- dra (red). No overlap exists between both ratios for finite NC size. For legend description see figure 10.

from Si-rich $Si_3N_4$ should be considerably smaller due to the higher Young's modulus and higher packing fraction (hampering diffusion) of $Si_3N_4$ as compared to $SiO_2$. As a result, the minimum size of Si NCs formed in Si-rich $Si_3N_4$ should be notably bigger as compared to Si NCs formed in Si-rich $SiO_2$.

Stress can be further deconvoluted into NC counter- stress and stress originating from the embedding ma- trix, with $N_{bnd}/N_{NC}$ allowing to quantitatively interpret and deconvolute Raman- and Infrared (IR) spectra. A deconvolution of phonon modes is useful to distinguish between internal (NC) and exteral (embedding matrix) stress as function of NC size, shape and interface orien- tation [44]. In analogy to Raman- and IR spectroscopy, stress-dependent photoluminescence (PL) spectra of Si NCs [45] can be interpreted and deconvoluted. Here, PL or electroluminescence (EL) on single Si NCs are particu- lar useful [46, 47] as individual NCs minimize statistical uncertainties due to shape, size and interface termina- tion. Using $N_{bnd}/N_{NC}$ and $N_{IF}/N_{bnd}$ for interpreting NC PL spectra as function of applied stress [48] is an- other method to gain insight into NC properties.

Ensembles of zb-NCs will not necessarily have exactly one of the high-symmetry shapes treated in this work, but a rather spherical shape with a mix of different low-index lattice facets defining the NC surface. In particular for NCs grown by segregation processes [49] it is not possible to describe the exact NC shape on a per-NC base due to significant statistical deviations in size and shape [9]. However, with the symmetry argu- ments derived above, it becomes clear that $N_{NC}(d_{NC})$, $N_{bnd}(d_{NC})$ and $N_{IF}(d_{NC})$ of such NCs are located between values of cubic and octahedral NCs.

## V. CONCLUSION

I deduced analytical number series for zb-NCs as a function of size, shape and surface faceting: the num- ber of NC atoms $N_{NC}[i]$, the number of bonds ex- isting between such atoms $N_{bnd}[i]$ and the number of NC interface bonds $N_{IF}[i]$ for. All expressions are linked to NC sizes $d_{NC}[i]$ via their run index $i$. As regular shapes with distinct faceting I investigated{001} cubes, {111} octahedra, {110} dodecahedra, {001}(base)/{111} (sides) pyramids, {111} tetrahedra, {111}(dominant)/{001} quatrodecahedra, and {001} (domi- nant)/{111} quatrodecahedra, see figure 1.

The ratio $N_{bnd}/N_{NC}$ is useful to gauge internal stress of zb-NCs which is key to evaluate NC self-purification and dopant segregation as encountered in impurity dop- ing, and the general stress response of NCs to an external force. Both, $N_{IF}/N_{bnd}$ and $N_{bnd}/N_{NC}$, can be applied to optical spectroscopy methods such as FT-IR, Raman, PL or EL to interprete and deconvolute spectra into NC- immanent (internal) and matrix (external) components. The ratio $N_{IF}(d_{NC})/N_{NC}(d_{NC})$ describes the electronic interaction of NCs with the embedding matrix or lig- ands to gauge the impact of interface dipoles or interface charge transfer onto the NC electronic structure. Par- titions of $N_{IF}(d_{NC}[i])$ as function of surface orientation allow to quantify facet-specific interface ratios of EPR- active Si DBs to estimate NC shapes, whereby the postu- lated existence of {001}-dominated quatrodecahedral Si NCs in $SiO_2$ can be verified. Decomposing $N_{IF}^{q,001}$ into $N_{IF,\langle 001\rangle}^{q,001}$ and $N_{IF,\langle 111\rangle}^{q,001}$, specific {001} and {111} EPR signal ratios of Si DBs are obtained to arrive at much improved assessments of Si NC size and shape.

The insights into zb-NC structures revealed here allow for major advancements in experimental data interpre- tation and understanding of III-V, II-VI and diamond- lattice based NCs. For the first time, a general ana- lytical tool exists to quickly assess stress- and interface- related effects in zb-NCs which allows for a deconvolution of experimental data into environment-exerted, interface- related and NC-internal phenomena.

## ACKNOWLEDGMENTS

D.K. acknowledges DAAD-Go8 joint research coop- eration schemes in 2012, 2014 and 2016 with IMTEK, Freiburg University, Germany. This work was carried out with financial aid from the UNSW Blue Sky research grant 2015.

[1] R. J. Jaccodine and W. A. Schlegel, J. Appl. Phys. 37,2429 (1966).
[2] E. Anastassakis, A. Pinczuk, E. Burstein, F. H. Pollack, and M. Cardona, Sol. Stat. Comm. 8, 133 (1970).
[3] S. Nakashima, S. Oima, A. Mitsuishi, T. Nishimura, T. Fukumoto, and Y. Akasaka, Sol. Stat. Comm. 40,765 (1981).
[4] I. W. Boyd and J. I. B. Wilson, J. Appl. Phys. 53, 4166(1982).
[5] I. W. Boyd and J. I. B. Wilson, J. Appl. Phys. 62, 3195(1987).

[6] S. R. Elliot, The Physics and Chemistry of Solids (Wiley,1998).
[7] A. M. Smith, A. M. Mohs, and S. Nie, Nature Nanotech.4, 56 (2009).
[8] E. Klimešová, K. Kůsová, J. Vacík, V. Holý, and I. Pelant, J. Appl. Phys. 112, 064322 (2012).
[9] J. Laube, S. Gutsch, D. Hiller, M. Bruns, C. Kübel, C. Weiss, and M. Zacharias, J. Appl. Phys. 116, 223501(2014).
[10] I. N. Stranski and L. Krastanow, Abhandlungen der Mathematisch-Naturwissenschaftlichen Klasse IIb.

Akademie der Wissenschaften Wien (in German) 146,
797 (1938).

[11] E. Bauer, Zeitschrift für Kristallographie (in German)
110, 372 (1958).

[12] R. Oshima, T. Hashimoto, H. Shigekawa, and Y. Okada,
J. Appl. Phys. 100, 083110 (2006).

[13] R. Oshima, A. Takata, and Y. Okada, Appl. Phys. Lett.
93, 083111 (2008).

[14] V. Popescu, G. Bester, M. C. Hanna, A. G. Norman, and
A. Zunger, Phys. Rev. B 78, 205321 (2008).

[15] C. G. Bailey, S. M. Hubbard, D. V. Forbes, and R. P.
Rafaelle, Appl. Phys. Lett. 95, 203110 (2009).

[16] A. R. Stegner, R. N. Pereira, K. Klein, R. Lechner, R. Di-
etmueller, M. S. Brandt, M. Stutzmann, and H. Wiggers,
Phys. Rev. Lett. 100, 026803 (2008).

[17] A. R. Stegner, R. N. Pereira, R. Lechner, K. Klein,
H. Wiggers, M. Stutzmann, and M. S. Brandt, Phys.
Rev. B 80, 165326 (2009).

[18] D. König, S. Gutsch, H. Gnaser, M. Kopnarski,
J. Göttlicher, R. Steininger, M. Zacharias, and D. Hiller,
Sci. Rep. 5, 9702 (2015).

[19] H. Gnaser, S. Gutsch, M. Wahl, R. Schiller, M. Kop-
narski, D. Hiller, and M. Zacharias, J. Appl. Phys. 115,
034304 (2014).

[20] G. M. Dalpian and J. R. Chelikowsky, Phys. Rev. Lett.
96, 226802 (2006).

[21] G. M. Dalpian and J. R. Chelikowsky, Phys. Rev. Lett.
100, 179703 (2008).

[22] T. L. Chan, M. L. Tiago, E. Kaxiras, and J. R. Che-
likowsky, Nano Lett. 8, 596 (2008).

[23] S. Ossicini, E. Degoli, F. Iori, E. Luppi, R. Magri,
G. Cantele, F. Trani, and D. Ninno, Appl. Phys. Lett.
87, 173120 (2005).

[24] D. König, D. Hiller, S. Gutsch, and M. Zacharias, Appl.
Mater. Interfaces 1, 1400359 (2014).

[25] P. J. Hesketh, C. Ju, S. Gowda, E. Zanoria, and S. Dany-
luk, J. Electrochem. Soc. 140, 1080 (1993).

[26] D. J. Eaglesham, A. E. White, L. C. Feldman, N. Moriya,
and D. C. Jacobson, Phys. Rev. Lett. 70, 1643 (1993).

[27] S. Godefroo, M. Hayne, M. Jivanescu, A. Stesmans,
M. Zacharias, O. I. Lebedev, G. V. Tendeloo, and V. V.
Moshchalkov, Nature Nanotech. 3, 174 (2008).

[28] E. Zeidler, ed., *Oxford Users' Guide to Mathematics
(translated from German by B. Hunt)* (Oxford Univer-
sity Press, 2004).

[29] M. Grundmann, O. Stier, and D. Bimberg, Phys. Rev.
B 52, 11969 (1995).

[30] M. H. Baier, E. Pelucchi, E. Kapon, S. Varoutsis, M. Gal-
lart, I. Robert-Philip, and I. Abram, Appl. Phys. Lett.
84, 648 (2004).

[31] A. Stesmans, M. Jivanescu, S. Godefroo, and
M. Zacharias, Appl. Phys. Lett. 93, 023123 (2008).

[32] A. K. Kambham, A. Kumar, A. Florakis, and W. Van-
dervorst, Nanotechnology 24, 275705 (2013).

[33] S. Koelling, O. Richard, H. Bender, M. Uematsu,
A. Schulze, G. Zschaetzsch, M. Gilbert, and W. Van-
dervorst, Nano Lett. 13, 2458 (2013).

[34] D. König, J. Rudd, M. A. Green, and G. Conibeer, Phys.
Rev. B 78, 035339 (2008).

[35] V. Heine, Phys. Rev. 138, A1689 (1965).

[36] J. Tersoff, Phys. Rev. B 30, 4874 (1984).

[37] Y. Nishi, T. Yamauchi, T. Marukame, A. Kinoshita,
J. Koga, and K. Kato, Phys. Rev. B 84, 115323 (2011).

[38] F. Ehrhardt, G. Ferblantier, D. Muller, C. Ulhaq-
Bouillet, H. Rinnert, and A. Slaoui, J. Appl. Phys. 114,
033528 (2013).

[39] C. R. Helms and E. H. Poindexter, Rep. Progr. Phys. 57,
791 (1994).

[40] K. Keunen, A. S. A, and V. V. Afanasév, Appl. Phys.
Lett. 98, 213503 (2011).

[41] M. Jivanescu, A. Stesmans, and M. Zacharias, J. Appl.
Phys. 104, 103518 (2008).

[42] S. Schuppler, S. L. Friedman, M. A. Marcus, D. L. Adler,
Y. H. Xie, F. M. Ross, T. D. Harris, W. L. Brown, Y. J.
Chabal, L. E. Brus, and P. H. Citrin, Phys. Rev. Lett.
72, 2648 (1994).

[43] D. König, M. A. Green, and G. Conibeer, in *Proc. of $21^\text{st}$
European Photovoltaics Science and Engineering Confer-
ence* (WIP Munich, Dresden, Germany, 2006), presenta-
tion 1CO.6.4, CD-ROM.

[44] T. Okada, T. Iwaki, K. Yamamoto, H. Kasahara, and
K. Abe, Sol. Stat. Comm. 49, 809 (1984).

[45] K. Kůsovà, L. Ondič, E. Klimešovà, K. Herynkovà,
I. Pelant, S. Daniš, J. Valenta, M. Gallart, M. Ziegler,
B. Hönerlage, and P. Gilliot, Appl. Phys. Lett. 101,
143101 (2012).

[46] J. Valenta, R. Juhasz, and J. Linnros, Appl. Phys. Lett.
80, 1070 (2002).

[47] J. Valenta, N. Lalic, and J. Linnros, Appl. Phys. Lett.
84, 1459 (2004).

[48] J. Ibanez, S. Hernandez, J. Lopez-Vidrier, D. Hiller,
S. Gutsch, M. Zacharias, A. Segura, J. Valenta, and
B. Garrido, Phys. Rev. B 92, 035432 (2015).

[49] J. Heitmann, F. Müller, M. Zacharias, and U. Gösele,
Adv. Mater. 17, 795 (2005).