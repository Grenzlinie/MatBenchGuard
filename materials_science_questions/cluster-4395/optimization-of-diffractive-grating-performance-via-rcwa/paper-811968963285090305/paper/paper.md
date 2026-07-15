# Deterministic diffractive diffusers for displays

Marko Parikka, Terho Kaikuranta, Pasi Laakkonen, Jari Lautanen, Jani Tervo,
Marko Honkanen, Markku Kuittinen, and Jari Turunen

A LCD backlighting device that uses a diffractive light extractor has been developed for applications in which pointlike light sources are employed. The novel system eliminates the images of light sources, which appear as bright lines emanating from each source in the conventional diffractive approach. In addition, the system illuminates the LCD uniformly: Modulation of the diffractive structure as a function of position is used to control the output field of this extended planar light source. © 2001 Optical Society of America

OCIS codes: 050.1970, 220.4000, 230.7390.

## 1. Introduction
Conventionally, the size of a mobile phone has been defined mainly by the size of the electronics inside it, and major technological efforts have been focused on the miniaturization of electronics as well as on reduc- tion of power consumption. Advancing electronic in- tegration capability has been key to size reduction and also assists in reduction of power consumption. $ ^1 $ Decreasing power consumption allows the use of smaller batteries, which further indirectly reduces both size and weight. The size of mechanical struc- tures has followed the size of electronics: Usually, mechanical structures have simply been scaled down without too much attention to matters such as leaky light-guide performance in the display. This proce- dure has been successful for a long time, but, when the thickness of the light guide approaches the height of the illuminating LEDs, problems arise. Modern mobile phones have already reached this size limit, and improved optical solutions are required.

There are two major issues to consider: visual performance and power efficiency of illumination. Visually, a thin light guide easily becomes nonuni- formly illuminated, featuring bright and dim areas that make the appearance of the display unattractive to the end user. Also, product usability in difficult environments is reduced because of low display con- trast.

Typical mobile-phone displays are illuminated with as many as 4–6 LEDs, even in the case of small single-row displays, mainly because of the low power (optical) efficiency of thin light guides. Illumination can therefore consume 40–60 mA for the display only. The electrical power consump- tion of illumination alone can be considered exceed- ingly high when it is compared with overall power consumption of a device in which a typical battery capacity is 1000 mA h. $ ^2 $

Some attempts to solve these problems have been made, but typically they have focused on illumination efficiency and uniformity only, paying less attention to power consumption. Similar problems have been met also in illumination of laptop displays, for which the relative consumption of illumination is even greater because of the large screen.

As part of the overall development of mobile-phone technology, the leaky light guide must provide better performance. This improved performance is indeed the motivation for the present study. The design path for conventional leaky light guides, which pro- vide output from refractive structures, can be consid- ered to have achieved its end in reducing thickness. A totally new approach must therefore be adopted to overcome these challenges and to permit improved performance requirements to be fulfilled.

So far, diffractive gratings have been used mostly in display systems as transmission-type diffusers $ ^3 $ or to produce color separation. $ ^4 $ In this paper we intro- duce a novel approach to controlled LCD backlighting

M. Parikka and T. Kaikuranta are with Nokia Mobile Phones Ltd., P.O. Box 86, FIN-24101 Salo, Finland. When this research was performed, P. Laakkonen, J. Lautanen, J. Tervo, M. Hon- kanen, M. Kuittinen (e-mail: markku.kuittinen@joensuu.fi), and J. Turunen were with the Department of Physics, University of Joensuu, P.O. Box 111, FIN-80101 Joensuu, Finland. J. Lau- tanen is now with Nanocomp, Ltd., Teollisuuskatu 18, FIN-80100 Joensuu, Finland.

Received 19 July 2000; revised manuscript received 5 February 2001.
0003-6935/01/142239-08$15.00/0
© 2001 Optical Society of America

10 May 2001 / Vol. 40, No. 14 / APPLIED OPTICS 2239

![](./images/811968963285090305_1.jpg)

Fig. 1. Backlighting geometry with discrete, essentially pointlike sources.

systems by means of a diffractive optical element.⁵
First, in Section 2, several systems based on refrac-
tive optics that were designed previously are pre-
sented, and the problems that emerge as a
consequence of the use of such systems are detailed.
The basic principles of controlled light extraction by
means of diffractive optics are explained, and the
advantages of the diffractive approach are listed. In
Section 3 we consider various methods to control uni-
formity by employing diffraction and identify a prob-
lem with line images caused by the combined use of
pointlike light sources and conventional diffractive
(grating) structures. One solution to the line prob-
lem based on the use of a novel diffractive structure
is shown as well. In Section 4 we describe the
microlithographic fabrication of the diffractive struc-
ture. Finally, the experimental results are pre-
sented in Section 5.

### 2. Geometrical Configuration
Figure 1 shows the typical construction of a LCD
backlighting device for a mobile phone. This kind of
a system usually contains a polymeric light guide
sitting under the LCD, a set of pointlike light sources
placed edge-on to the light guide, and a rear reflector
positioned under the guide. The system should
transform the optical field radiated by the point
sources into an extended upward-propagating light
field that illuminates the LCD uniformly. The ex-
traction of light from the light guide is usually im-
plemented with a scattering coating⁶ or by
roughening the bottom or top surface of the guide to
transform a part of guided light into illumination
light. In some approaches, a scattering light-guide
material is used.⁷ Also, different types of nonscat-
tering extractor, such as lens patterns and prism
rows, are employed.⁸ However, the conventional
techniques are accompanied by serious problems.
With random extractors (coatings or roughening), the
uniformity of illumination is typically poor: Be-
cause the scattering efficiency is position indepen-
dent, the amount of light coupled out of the light
guide (per unit area) decreases with the distance
from the light source. In addition, brighter areas,
known as hot spots, are generated in front of the light
sources. This is a particularly serious problem if the
light-guide structure is thin because light rays hit the
surface of a thinner light guide more frequently, caus-
ing faster outcoupling.

The standard approach to improving uniformity of
illumination is to arrange light sources on two oppo-
site ends on the guide. Naturally, this requires
twice as many light sources and twice as much elec-
tric power to drive them, but it fails to eliminate the
hot spots. Also, the mechanical structure becomes
more complicated. For a scattering material, the
angular spectrum of outcoupled light is undesirable,
and an additional prism sheet is needed to redirect it.

Methods for performing controlled light extraction
based on conventional refractive optics have been in-
vestigated with the goal of achieving a uniform out-
coupled field by density variations of light-extracting
lenses or prisms. Unfortunately, not only do the
lenses cause light to spread in disadvantageous di-
rections but the lens patterns themselves are often
visible. Relatively good angular spectra of out-
coupled radiation may be achieved with prisms, but
even microprism rows tend to cause undesired visual
effects.⁹ To hide such visual defects, or to improve
the angular spectrum, additional diffuser or prism
sheets are needed. When the size of the lenses or
prisms is decreased to make them invisible, their
number must correspondingly be increased to main-
tain the system efficiency. Consequently, the design
becomes more difficult because in many cases it turns
out to be impossible to carry out the required com-
puter simulations because of limited computer capac-
ity. Thus the testing of system functionality would
require a prototype, which means that a remarkably
expensive mold is needed. In practice this means
that a series of molds is needed for an iteration pro-
cess.

The facts described above suggest the use of dif-
fractive optics to control light extraction. The prin-
ciple of using a diffractive structure as a controlled
light extractor is based on modulation of the diffrac-
tive structure’s parameters as a function of position
to control the light output. Explicitly, application of
rigorous diffraction theory permits an exact calcula-
tion of relative light energy that is locally coupled out
of the light guide. There are numerous ways to con-
trol light outcoupling efficiency by means of diffrac-
tive optics. Also, it has been reported that the use of
a diffractive extractor offers a doubling of the relative
brightness in comparison with that from refractive
solutions.¹⁰

The use of a diffractive extractor leads to an ad-
vantageous angular spectrum of outcoupled light,
meaning that no additional redirecting sheets are
needed. In addition, the illumination is definitely
visually structureless owing to the small size of the
diffracting features. Also, the diffractive structure
permits maintenance of the outcoupling efficiency at
a low level without causing any discontinuities, such
as noncoupling but totally internally reflecting areas.
This makes it possible to extend the reach of illumi-
nation easily, i.e., to increase the length of the light

![](./images/811968963285090305_2.jpg)

Fig. 2. Backlighting setup with a diffractive light extractor.

guide such that uniformity is maintained and no opposite-end light sources are needed.

Also, the prototyping possibilities of diffractive sys- tems offer an advantage over conventional solutions. Use of electron-beam (e-beam) lithography combined with plastic-replication processes permits fast itera- tion toward the desired result if appropriate facilities are available on site. One can speed up the process further by making diffractive stripe elements whose lengths but not widths are equal to those of the dis- play to be illuminated and by hot embossing these stripes onto the surface of the polished plastic [poly(methyl methacrylate) (PMMA)] light guide. These test stripes permit evaluation of the uniformity of the light output in the direction from the light source to the opposite end of the guide, which in the case of acceptable uniformity is the desired result. For example, e-beam writing of a stripe with a length of 25 mm and a width of 4 mm takes only a few hours, even with relatively slow Gaussian-beam nanopat- terning devices (Leica LION LV1 was available to us). So it can be stated that the test of uniformity of certain grating parameters can be completed within a few days, whereas for the mold-based prototype it takes weeks.

The desired backlighting geometry is shown in Fig. 2. In this setup the light sources are placed on one of the light-guide edges. The geometry of the guide may be wedge shaped to increase the system effi- ciency by reducing end-face loss. Alternatively, the end face of a uniform-thickness light guide could be shaped as a retroreflector.

### 3. Design of Diffractive Diffusers
The purpose of the diffractive structure is to couple light out of the light guide in such a way that uniform illumination of the LCD is achieved. This means that the outcoupling efficiency has to be controlled in some way. In what follows, we present two ideas for accomplishing this with minimum loss of light.

#### A. Modulation of Grating Profile
The directions of forward-propagating diffraction or- ders are given, in the geometry of Fig. 3, by the grat- ing equation

$$
n_{3} \sin \theta_{m}=n_{1} \sin \theta_{\text {in }}+m \lambda / d, \tag{1}
$$

where $n_{3}$ is the refractive index of the material that contains these diffraction orders, $n_{1}$ is the refractive index of the material in which the incident beam and reflected diffraction orders propagate, $\theta_{m}$ is the direc tion of the $m$ th diffraction order (measured from the normal of the grating surface), $\theta_{\text {in }}$ is the angle of incidence, $\lambda$ is the wavelength, and $d$ is the grating period. In numerical calculations we use rigorous diffraction theory, in particular, an implementation of the so-called Fourier expansion method.¹¹

![](./images/811968963285090305_3.jpg)

Fig. 3. Side view of the grating outcoupler and the propagation directions of various diffraction orders.

In the geometry that is used, the rays from the LEDs propagate in the light guide at angles $60^{\circ}-90^{\circ}$. The grating should couple an increasing amount of light out of the light guide from the rays propagating between these angles. Based on numerical simula- tions of the output coupling efficiency, the grating period was selected to be $d=2.5$ µm, and the value $h=0.55$ µm was selected for the height of the grating profile. Some examples of the coupling efficiencies of this type of grating for TE-polarized light are listed in Table 1.

Now only the fill factor $f=c/d$ (see Fig. 3) is a free parameter available for control of coupling efficiency. We aim for an almost linear increase of the outcou- pling efficiency. With the selected grating parame- ters we find that the best performance is reached if fill factor $f$ increases linearly from 0.2 to 0.5. The total outcoupled power is presented in Fig. 4. In Fig. 4(a), only those reflected orders are taken into account for which the reflection angle is smaller than the angle of total internal reflection (reflected orders $-2$ to $-11$ in Fig. 3, where $\theta_{\text {in }}$ is assumed to be positive).

It appears possible to reach the required uniform illumination of the LCD element with this kind of outcoupling structure. In the fabricated element the brightness over the length of the light guide de- creased slightly with distance from the LEDs, but adjusting the change of fill factor from linear to a suitable power $x^{p}$ will compensate for this effect.

<table>
<caption>Table 1. Diffraction Efficiencies of Reflected ($\eta_{r}$) and Transmitted ($\eta_{t}$) Orders $m$ with Their Propagation Directions $\theta_{r,m}$ and $\theta_{t,m}^{a}$</caption>
<thead>
<tr>
<th>$m$</th>
<th>$\eta_{r}$ (%)</th>
<th>$\theta_{r}$ ($^{\circ}$)</th>
<th>$\eta_{t}$ (%)</th>
<th>$\theta_{t}$ ($^{\circ}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$-5$</td>
<td>0.4</td>
<td>8.4</td>
<td>1.2</td>
<td>12.7</td>
</tr>
<tr>
<td>$-4$</td>
<td>0.4</td>
<td>17.4</td>
<td>1.1</td>
<td>26.6</td>
</tr>
<tr>
<td>$-3$</td>
<td>1.1</td>
<td>26.8</td>
<td>5.9</td>
<td>42.5</td>
</tr>
<tr>
<td>$-2$</td>
<td>0.7</td>
<td>37.0</td>
<td>15.4</td>
<td>64.6</td>
</tr>
<tr>
<td>$-1$</td>
<td>12.3</td>
<td>50.0</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>$0$</td>
<td>55.8</td>
<td>65.0</td>
<td>–</td>
<td>–</td>
</tr>
</tbody>
</table>

$^{a}$The angle of incidence is $\theta_{\text {in }}=65^{\circ}$, the grating period is $d=2.5$ µm, the profile height is $h=0.5$ µm, the wavelength is $\lambda=0.57$ µm, the fill factor is $f=0.5$, and the refractive indices are $n_{1}=1.5$ and $n_{3}=1$. A minus means a nonpropagating, or evanescent, order.

10 May 2001 / Vol. 40, No. 14 / APPLIED OPTICS 2241

![](./images/811968963285090305_4.jpg)

Fig. 4. Total outcoupling efficiencies as functions of fill factor $f$:
(a) reflected and (b) transmitted orders. Solid curves, $\theta_{\text{in}} = 60^\circ$;
dashed curves, $\theta_{\text{in}} = 70^\circ$; dotted curves, $\theta_{\text{in}} = 80^\circ$.

### B. Waveguide Approach
Only a part of the reflected diffraction order is cou-
pled out from the lower surface of the light guide, and
consequently the Fresnel coefficients for all orders
must be determined. Because a large grating period
implies several reflected orders for one incoming ray,
some kind of iterative calculation is needed if one
wants to determine the total outcoupled energy.

Another approach is to make use of waveguide the-
ory. $^{12}$ Even though a light guide is much thicker
than the usual waveguide, one can use this kind of
approach to determine the amount of the outcoupled
energy. Because the thickness of a light guide is $\sim 1$
mm, the number of propagating modes is $\sim 1000$.
When a grating is present, a certain amount of energy
per a unit length is coupled out from the light guide.
Because of this loss the total energy $E$ of a propagat-
ing mode $m$ is a function of a propagation distance $z$,

$$
E_{m}(z) = E_{m}(0)\exp(-2\alpha_{m}z), \tag{2}
$$

where $E_{m}(0)$ is the initial energy and $\alpha_{m}$ is an out-
coupling coefficient. In the usual sense, $\alpha_{m}$ is the
complex part of the propagation factor of a mode.

![](./images/811968963285090305_5.jpg)

Fig. 5. Formation of the LED image pattern. The images are
seen by the eye at a distance proportional to the path length
traveled by the ray. The phenomenon is the same whether the
diffractive structure is on the bottom or on the top surface of the
light guide. However, which geometry produces stronger lines
depends on the structure's transmission and reflection properties.

Determination of the value of $\alpha_{m}$ can be made rigor-
ously by use of the Fourier expansion method for
waveguides. $^{13}$ This method is, however, quite slow,
even with modern PCs, so the use of approximative
methods is justifiable.

Probably the best approximative method is the so-
called improved perturbation analysis introduced by
Tamir and Peng. $^{14}$ The determination of outcou-
pling coefficients, even for thousands of modes, can be
made in a relatively short time with this technique.
However, the validity of results must always be
checked by rigorous theory.

### C. Problem with Lines
In the backlighting mode, when LEDs (or essentially
any other pointlike light sources) are used as light
sources, bright lines formed by the diffracting images
of the LEDs are generated in front of them. This
makes it inconvenient to use the conventional diffrac-
tive technique for illumination of LCDs in mobile-
phone displays if no special treatment (additional
diffusers, special light sources, etc.) is used. The
formation of the lines is illustrated in Fig. 5. Figure
6 shows the resultant performance as seen from the
top of the light guide.

### D. Pixellated Structure with a Uniform Grating
To remove the lines (LED images), one must also
couple light sideways. This can be done in a light
guide if the grating orientation is such that light rays
reach the grating in so-called conical incidence; see
Fig. 7. In this case no light is coupled out: The
side-coupling efficiency depends on the angle of inci-
dence and on the grating parameters. Some diffrac-
tion efficiencies for a grating with $d = 2.5\ \mu\text{m}$ and $h =$
$0.5\ \mu\text{m}$ in a pure conical mount are listed in Table 2.


![](./images/811968963285090305_6.jpg)

Fig. 6. CCD picture of the light output from the light guide operated with three LEDs with the conventional diffractive structure.

In the case of conical incidence the reflection angle (the angle with respect to the normal of the grating surface) is also different for different orders, except for the zeroth order, for which the reflection angle is naturally equal to the incidence angle. For example, when the incidence angle $\theta_{\text{in}} = 60^\circ$, the first, second, and third diffraction orders are reflected in angles $61.6^\circ$, $66.6^\circ$, and $78.2^\circ$, respectively.

![](./images/811968963285090305_7.jpg)

Fig. 7. Top view of the directions of diffraction orders for conical incidence.

<table>
<caption>Table 2. Diffraction Efficiencies of Orders $\pm m$ and Deflection Angles $\varphi_m$ for Several Incidence Angles $\theta_{\text{in}}$$^a$</caption>
<thead>
<tr>
<th rowspan="2">$m$</th>
<th colspan="2">Angle $\theta_{\text{in}}$</th>
<th colspan="2"></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2">$60^\circ$</th>
<th colspan="2">$70^\circ$</th>
<th colspan="2">$80^\circ$</th>
</tr>
<tr>
<th></th>
<th>$\eta_r$ (%)</th>
<th>$\varphi$ ($^\circ$)</th>
<th>$\eta_t$ (%)</th>
<th>$\varphi$ ($^\circ$)</th>
<th>$\eta_r$ (%)</th>
<th>$\varphi$ ($^\circ$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>30.5</td>
<td>0</td>
<td>63.0</td>
<td>0</td>
<td>50.8</td>
<td>0</td>
</tr>
<tr>
<td>$\pm 1$</td>
<td>24.0</td>
<td>10.0</td>
<td>14.4</td>
<td>9.2</td>
<td>24.6</td>
<td>8.7</td>
</tr>
<tr>
<td>$\pm 2$</td>
<td>6.6</td>
<td>19.3</td>
<td>4.1</td>
<td>17.0</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>$\pm 3$</td>
<td>4.1</td>
<td>27.8</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="7">$^a$Grating parameters are period $d = 2.5$ $\mu$m, relief height $h = 0.5$ $\mu$m, and refractive indices $n_1 = 1.5$ and $n_3 = 1$. A minus means a nonpropagating order.</td>
</tr>
</tfoot>
</table>

![](./images/811968963285090305_8.jpg)

Fig. 8. Placement of outcoupling, nonconical (orientation A) and of deflecting, conical (orientation B) gratings.

We may now reach uniform illumination for the LCD by varying the amount of outcoupling pixels; see Fig. 8. In the front end of the light guide (on the side of the LEDs) we first place a strongly deflecting grating with a period $d = 1.25$ $\mu$m; then the light guide's surface is filled with two types of grating. Orientation A gratings are mostly outcoupling gratings (nonconical), and orientation B gratings are mostly deflecting gratings (conical). We can reach uniform outcoupling by varying the area proportions of type A and type B gratings.

In practice, one pixel consists of one working field of the Leica LION LV-1 e-beam machine; see Fig. 9. Gratings with lines in the $y$ direction are considered type A gratings. Using Eq. (2) and the fact that the intensity of the outcoupled field must be constant for every pixel, we obtain a recurrence relation for the area $s_j = w_j^2 - (d_{1,j}d_{2,j} + d_{3,j}d_{4,j})$,

$$
s_j = -\log[2 - \exp(2\alpha_m s_{j-1})], \tag{3}
$$

where the subscript $j$ is related to the $j$th pixel in the direction of light propagation.

![](./images/811968963285090305_9.jpg)

Fig. 9. Structure of a pixellated grating. Dimension $w$ is the width of one working field of the Leica LION LV-1 e-beam machine.

10 May 2001 / Vol. 40, No. 14 / APPLIED OPTICS 2243

![](./images/811968963285090305_10.jpg)

Fig. 10. Designed proportion of type A gratings (nonconical) for an element consisting of 180 × 410 working fields. The LEDs are in positions (50, 0) and (130, 0).

Of course, in our system, rays propagate in al- most all directions, which means that type A grat- ings also deflect reflected rays and type B gratings couple light out. For that reason the percentage of type A gratings must be optimized for different ar- eas of the element. The total outcoupling effi- ciency of a linear grating is undoubtedly a function of the conical angle; hence the total energy coupled out by a pixel consisting of a type A or a type B grating depends critically on the pixel's position in the element. Thus, to optimize the proportion of type A gratings in different areas of the element, we must calculate the outcoupling efficiency as a func- tion of the conical angle. Moreover, because the efficiency depends also on the incident angle, we must make an integration over the incident angle for every single value of the conical angle. Of course, every incident angle must be weighted by the actual radiation pattern of the LED used. For- tunately, in many cases the efficiency as a function of the conical angle $\psi$ follows approximately the function $\cos^{2}\psi$; hence our optimization procedure can be simplified significantly. However, the accu- racy of this approximation must always be checked by use of a rigorous diffraction theory.

Moreover, Eq. (3) is valid only in one-dimensional geometry. In two-dimensional geometry the radia- tion intensity at any given point is proportional to $1/r$, where $r$ is the distance from the LED. Thus the proportion of type A gratings must also be appropri- ately weighted by that distance.

After making the weightings described above, we obtain the final proportion of type A gratings, as shown in Fig. 10 for an element consisting of $180 \times$ 410 working fields of size $100\ \mu\text{m} \times 100\ \mu\text{m}$.

### 4. Fabrication with Electron-Beam Lithography
In this section we describe the fabrication of a dif- fractive structure combined with a plastic light guide. The first step is to fabricate the diffractive structure with conventional lithography methods in the resist. For this purpose the 4-in. (10.16-cm) silicon wafer was spin coated with positive resist (AR-P 619, Allresist, Berlin) to a thickness of 550 nm and then baked in a forced-air convention oven at a temperature of $210\ ^{\circ}\text{C}$ for 60 min. The baked resist layer was coated with a 20-nm aluminum layer.

Exposures were carried out with the Leica LION LV1 e-beam machine with an acceleration voltage of 20 kV and a beam step size of 100 nm. The nominal dose used was $45\ \mu\text{C/cm}^{2}$. With these parameters the exposure rate is $\sim 20\ \text{mm}^{2}/\text{h}$.

After exposure, the aluminum layer was dissolved in a 1:9 solution of hydrochloric acid and deionized water for 60 min. The exposed areas were developed in a solution of methyl isobutyle ketone and isopro- panol (1:2) for 60 s. The development is stopped by holding the sample in isopropanol for 15 s. Finally, the development residual materials were removed by introduction of oxygen plasma.

In the first step of nickel-shim growth the master element (in this case the patterned resist layer) has to be coated with a 40-nm-thick nickel conductivity layer. The master element is then placed in a stan- dard nickel electroplating bath to produce a durable nickel copy. The typical thickness of fabricated shims was $\sim 300\ \mu\text{m}$.

Replication was made by hot embossing. In hot embossing a piece of PMMA plastic and the nickel shim are placed between two polished metal plates and heated above the glass-transition temperature $T_{g}$ of the plastic under pressure (the $T_{g}$ of PMMA is $\sim 90\ ^{\circ}\text{C}$). After pressure release and cooling, the shim and the replicated plastic piece can be sepa- rated easily. We stress that this replication tech- nique is appropriate only for prototyping. For large-scale production, plastic injection molding is the only feasible technique.

![](./images/811968963285090305_11.jpg)

Fig. 11. Atomic-force microscopy picture of the hot embossed structure.

### 5. Experimental Demonstrations
We designed a set of various-sized test elements and varied the proportion of type A gratings in those elements. We achieved these designs by fabricating nickel shims as described in Section 4 and preparing several copies of each sample in a 1-mm-thick sheet of PMMA plastic by hot embossing. An atomic-force microscopy picture of a hot embossed structure is shown in Fig. 11. The shape of the ridges is almost rectangular, and the filling factor is $f \approx 0.5$, as desired. The borders of working fields may be observed in the picture as narrow ridges, but they are so narrow that their influence on the outcoupling may be assumed to be negligible.

Figure 12 illustrates light output from a pixellated light guide imaged through the LCD element. The element in Fig. 12 corresponds to the design shown in Fig. 10: The size of the element is 1.8 cm $\times$ 4.1 cm, and it is illuminated with two LEDs. The LEDs still cause hot spots in front of the element (white areas in the picture), but otherwise the uniformity of the illumination is satisfactory: In the longitudinal direction the intensity drops only 20% from its maximum value (hot spots are neglected), and in the transverse direction the uniformity is almost perfect. The slightly brighter area at the right in the element is caused by a reflection from the polished edge. In Fig. 13 the output of an element of size 1.2 cm $\times$ 9 cm is shown. Again, the uniformity is satisfactory: The drop in intensity is even smaller than that shown in Fig. 12.

![](./images/811968963285090305_12.jpg)

Fig. 12. CCD picture of the light output from a 1-mm-thick pixellated light guide replicated in plastic. The dimensions of the element are 18 mm $\times$ 41 mm.

![](./images/811968963285090305_13.jpg)

Fig. 13. CCD picture of the light output from a 1-mm-thick pixellated light guide replicated in plastic. The dimensions of the element are 10 mm $\times$ 100 mm.

In both Figs. 12 and 13 the lines that are caused by LEDs are spread considerably but are still visible in front of the LEDs. Thus, if the light guide is made even thinner, the lines may still be visible. (Visually the nonuniformity is not quite so large as in the CCD picture because the human eye sees intensity variations on a logarithmic scale).

### 6. Conclusions
We have shown that it is possible to couple light out of a light guide uniformly with diffraction gratings. In designing the grating surface of the light guide we first estimated the performance of the gratings by using rigorous diffraction theory and then applied an approximate waveguide model to find the appropriate distribution of conical and nonconical gratings. However, because of the complexity of the problem, the light guide cannot be modeled completely. Instead, the structure has to be iterated by fabrication of a series of test samples. Our tests showed that good uniformity in the longitudinal direction can be achieved by variations of the filling factors of linear gratings with grating lines perpendicular to the light sources. In this case, however, the pointlike light sources form a series of light source images in a thin light guide, which are observed as disturbing lines aligned toward the light sources.

To avoid the line problem we introduced a solution in which the grating structure is pixellated into two types of grating. The grating lines of nonconical gratings are perpendicular to the rays emanating from the light sources, whereas the lines of the conical gratings are parallel to the rays. The purpose of the nonconical gratings is to couple light out of the light guide, whereas the conical gratings should distribute light sideways. Of course, because we have rays propagating in all directions inside the waveguide, the conical gratings also couple some light out. The CCD pictures taken from the fabricated samples show that this pixellated structure fades out the lines in a satisfactory way, and when the LCD element was placed above the light guide the lines could not be observed at all in a visual inspection. Brighter spots in front of the light sources are still observable, but otherwise the illumination is uniform: The minimum value is $\sim$80% of the maximum value. Even with this approach it seems to be rather

10 May 2001 / Vol. 40, No. 14 / APPLIED OPTICS 2245

difficult to fade out completely the bright spots that reside in the front of the light sources. This may not be considered a serious problem in real display ap- plications because the spots can be usually hidden behind the screen frame.

The overall efficiency of the system depends criti- cally on the size of the element: If the viewing area of the element is short, a large amount of energy is not coupled out, especially when the light guide is thick. This result follows from the fact that the rays that propagate at small propagation angles do not actually meet the diffracting surface at all. This is, of course, a property not of the diffractive surface but of the light guide. However, the efficiency of the small displays can be increased by use of reflecting surfaces, for example, retroreflectors, at the end of the light guide. When the viewing area becomes larger, more light is coupled out from the light guide, and the efficiency of the system becomes superior to that of conventional systems. Naturally the abso- lute efficiency of the system also depends critically on the type of LED used and on the input-coupling effi- ciency.

Another matter that has to be considered is the chromatic dispersion caused by the diffracting grat- ings. It does not, of course, present a problem when one uses LEDs that are emitting only one narrow- frequency band. However, when white LEDs with two or more spectral peaks are used, the chromatic dispersion becomes clearly visible. Fortunately, this problem is diminished in displays by LCD panels that act as diffusers.

We have succeeded in fabricating test structures in 1-mm-thick plastic sheets by hot embossing. There- fore injection molding of such structures should be a feasible method of producing light guides in quantity.

We acknowledge fruitful collaboration with V.-P. Leppänen and T. Jääskeläinen (Nanocomp, Ltd., Joensuu, Finland) and M. T. Gale and M. Rossi (Cen- tre Suisse d'Electronique et de Microtechnique, Zü- rich).

## References and Notes
1. Semiconductor Industry Association, *The National Technology Roadmap for Semiconductors*, 1997 ed. (Semiconductor Indus- try Association, San Jose, California). For recent informa- tion, see http://public.itrs.net.
2. See product information on batteries, for example at http:// www.nokia.com.
3. D. J. Schertler and N. George, “Uniform scattering patterns from grating-diffuser cascades for display applications,” *Appl. Opt.* **38**, 291–303 (1999).
4. B. Layet, I. G. Cormack, and M. R. Taghizadeh, “Stripe color separation with diffractive optics,” *App. Opt.* **38**, 7193–7201 (1999).
5. J. Turunen and F. Wyrowski, eds., *Diffractive Optics for In- dustrial and Commercial Applications* (Wiley, Berlin, 1997).
6. J. M. Teijido, H. P. Herzig, and R. Dändliger, “Design of a non-conventional illumination system using a scattering light pipe,” in *Design and Engineering of Optical Systems*, J. J. Braat, ed., Proc. SPIE **2774**, 747–756 (1996).
7. A. Horibe, M. Baba, E. Nihei, and Y. Koike, “High-efficiency and high-visual-quality LCD backlighting system,” SID Symp. **29**, 153–156 (1998).
8. J. M. Teijido, H. P. Herzig, and R. Dändliger, “Illumination light pipe using micro-optics as diffuser,” in *Holographic and Diffractive Techniques*, G. J. Dansmann, ed., Proc. SPIE **2951**, 146–155 (1996).
9. C.-Y. Tai, “A small-area backlight employing divergent-angle beam rotator and unique double-layer micro-prisms,” SID Symp. **29**, 556–559 (1998).
10. S.-I. Ochiai, “Light guide plates and light guide plate assembly utilizing diffraction grating,” U.S. patent 5,703,667 (30 Decem- ber 1997).
11. J. Turunen, “Diffraction theory of microrelief gratings,” in *Mi- cro-Optics: Elements, Systems and Applications*, H. P. Her- zig, ed. (Taylor & Francis, London, 1997), chap. 2.
12. T. Tamir, ed., *Integrated Optics*, 2nd ed. (Springer-Verlag, Ber- lin, 1979).
13. S. T. Peng, T. Tamir, and H. L. Bertoni, “Theory of periodic dielectric waveguides,” IEEE Trans. Microwave Theory Tech. **MTT-23**, 123–133 (1975).
14. T. Tamir and S. T. Peng, “Analysis and design of grating couplers,” *Appl. Opt.* **14**, 235–254 (1977).