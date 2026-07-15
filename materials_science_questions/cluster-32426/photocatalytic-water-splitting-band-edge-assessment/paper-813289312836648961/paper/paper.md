$Ab$ initio modeling of sulphur doped $TiO_2$ nanotubular photocatalyst for water-splitting hydrogen generation

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2012 IOP Conf. Ser.: Mater. Sci. Eng. 38 012057

(http://iopscience.iop.org/1757-899X/38/1/012057)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 141.161.91.14
This content was downloaded on 08/09/2015 at 15:16

Please note that terms and conditions apply.

International Conference on Functional Materials and Nanotechnologies (FM&NT2012)
IOP Publishing
IOP Conf. Series: Materials Science and Engineering 38 (2012) 012057  doi:10.1088/1757-899X/38/1/012057

# Ab initio modeling of sulphur doped TiO₂ nanotubular photocatalyst for water-splitting hydrogen generation

O Lisovski¹⁵, S Piskunov²³⁴, Y F Zhukovskii⁴ and J Ozolins¹

¹Faculty of Materials Science and Applied Chemistry, Riga Technical University, Latvia
²Faculty of Computing, University of Latvia, Latvia
³Faculty of Physics and Mathematics, University of Latvia, Latvia
⁴Institute for Solid State Physics, University of Latvia, Latvia

E-mail: oleg.lisovski@gmail.com

**Abstract.** In order to construct an efficient visible-light-driven TiO₂ photocatalyst for water splitting applications, one has to perform improvements of its electronic structure. In this theoretical study we consider single-walled anatase TiO₂ nanotubes having following morphologies: (101) 3-layered wall with chirality indexes (n,0) and (n,n), (101) 6-layered wall with (n,0) and (0,n), (001) 6-layered wall with (n,0) and (0,n), and (001) 9-layered wall with (n,0) and (0,n). The latter configuration occurs to be the most energetically stable, due to possessing negative strain energy. In our study the most stable 9-layered anatase (001) (0,n) nanotube has been doped with sulphur. According to obtained results sulphur dopant creates the mid-gap states making the TiO₂ nanotube to be a good candidate for efficient photocatalyst working under day light irradiation.

## 1. Introduction

Issues of alternative energy sources and environment protection belong to the important nowadays topics. Hydrogen is one of the most environment-friendly energy sources; moreover, it is widely used in industry. Currently, hydrogen is generally produced from fossil fuels, and the disadvantage of the method is a presence of CO₂ as a side product. One of the ways how to get rid of this drawback is a hydrogen generation by photocatalytic water splitting [1].

There are several requirements toward the efficiency of photocatalysts. First, it should be a semiconductor, *i.e.*, it should possess a band gap. Second, band gap width should be approximately 2.0 eV, [1] in order to allow the catalyst to use not only UV light (which consists only approximately 4% of total solar radiation [2,3]), but also a significant amount of visible light spectrum. Third, positions of band edges should be adjusted, in order to generate excited electrons and electron holes at appropriate energy levels where hydrogen cations and hydroxyl group anions, respectively, are reduced and oxidized [4]. Fourth, the photocatalyst's structure must be free from impurities, in order to block recombination of excited electrons and electron holes. Such recombination occurs at impurities [4].

TiO₂ samples (band gap ~3.18 eV for the bulk phase of anatase) are one of the most attractive photocatalysts proposed for water-splitting applications [4]. TiO₂ is relatively cheap, chemically stable and non-toxic material. Its top valence band is lower than the energy level which hydroxyl groups are

⁵ To whom any correspondence should be addressed

Published under licence by IOP Publishing Ltd

oxidized at, while its bottom of conduction band is higher than the energy level where $H^+$ are reduced, so energetic requirements are fulfilled.

Nevertheless, the band gap of TiO₂ bulk is too wide, and its crystalline structure normally contains a great number of impurities meaning that it cannot serve as a visible-light-driven photocatalyst. To surmount these disadvantages one can use nanotubes made of titania and dope them with various atoms. Comparing with conventional catalysts, titania nanotubes (NTs) possess larger surface area and, consequently, have better crystallinity, better adsorption capacity, and higher photocatalytic activity. It means that impurity concentration in nanotubes should be lower than in the bulk.

**Table 1.** Lattice constants and band gaps of TiO₂ (bulk phase) as calculated by means of various Eₓc [6].

<table>
  <thead>
    <tr>
      <th>$E_{xc}$</th>
      <th>a, Å</th>
      <th>c, Å</th>
      <th>$\Delta\varepsilon_{\text{g}}$, eV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>B3PW</td>
      <td>3.785</td>
      <td>9.580</td>
      <td>3.667</td>
    </tr>
    <tr>
      <td>PBE0</td>
      <td>3.778</td>
      <td>9.545</td>
      <td>4.109</td>
    </tr>
    <tr>
      <td>B3LYP</td>
      <td>3.800</td>
      <td>9.647</td>
      <td>3.641</td>
    </tr>
    <tr>
      <td>SOGGAXC</td>
      <td>4.449</td>
      <td>9.539</td>
      <td>0.669</td>
    </tr>
    <tr>
      <td>LDA</td>
      <td>3.766</td>
      <td>9.353</td>
      <td>1.999</td>
    </tr>
    <tr>
      <td>PBE</td>
      <td>3.821</td>
      <td>9.597</td>
      <td>2.019</td>
    </tr>
    <tr>
      <td>PWGGA</td>
      <td>3.817</td>
      <td>9.595</td>
      <td>2.023</td>
    </tr>
    <tr>
      <td>HF</td>
      <td>3.777</td>
      <td>9.643</td>
      <td>12.357</td>
    </tr>
    <tr>
      <td>Experiment</td>
      <td>3.784</td>
      <td>9.507</td>
      <td>3.18</td>
    </tr>
  </tbody>
</table>

Thus, it is also easier to introduce dopants in the NT structure. It is known that doping by S shifts the absorption spectrum of titania to a lower energy and effectively leads to visible light photocatalytic activity [5]. Therefore, in the current study we concentrate on titania nanotubes doped with sulphur.

Although pristine nanotubes tend to have larger band gap ($\Delta\varepsilon_{\text{g}}$) as compared to the bulk, low-dimensional structures of TiO₂ with $\Delta\varepsilon_{\text{g}} > 3.2$ eV are better starting point for doping which leads to the formation of the induced mid-gap states diminishing the band gap to the required interval. In this study we consider single-walled titania nanotubes of 8 different morphologies: built of 3-layered anatase (101) nanosheet with chirality indexes $(n,0)$ and $(n,n)$, 6-layered anatase (101) $(n,0)$ and $(0,n)$, 6-layered anatase (001) $(n,0)$ and $(0,n)$, 9-layered anatase (001) $(n,0)$ and $(0,n)$ and define which of them is most stable and prospective for further doping. Then we study effects of S atom (as substitute for O atom) which is being used as a dopant too.

### 2. Computational details
Our *ab initio* calculations have been performed using linear combination of atomic orbitals (LCAO) method with atom-centered Gaussian-type functions (GTF) as basis set (BS), according to implementation in computer code *CRYSTAL* [6]. We have used hybrid exchange-correlation functional B3LYP [6] within the framework of density functional theory (DFT). We have considered two BSs for Ti (ECP-411sp-311d(G) [7] and ECP-5s-6sp-5d [8]). We have figured out that the latter, containing uncontracted GTFs would require irrational amount of computational time for calculations of NTs containing hundreds atoms per unit cell, so we chose the former. The full electron BS for oxygen has been taken in the form $6s$-$311sp$-$1d$. Reciprocal space integration was performed by sampling the Brillouin zone (BZ) with the 4 k-points uniformly distributed along the line segment of the irreducible BZ. The cutoff threshold parameters of *CRYSTAL* for Coulomb and exchange integrals evaluation (ITOL1–ITOL5) have been set to 7, 8, 7, 7, and 14, respectively.

To perform reliable calculations, we have compared three hybrid exchange-correlation functionals ($E_{xc}$), one LDA and three GGA, which allow us to performed Hartree-Fock (HF) calculations too within hybrid functional formalism. We have calculated the band gap and lattice constants of bulk TiO₂ in anatase phase using different $E_{xc}$ too. We have compared the obtained results with experimental data (results are present in the Table 1). According to Table 1, the best agreement with experiment is achieved for hybrid B3LYP $E_{xc}$ (band gap 3.64 *vs.* 3.18 eV). Nevertheless, the result was

not accurate enough for further calculations as far as band gap is the key feature for a photocatalyst, so, we modify an admixture coefficient for non-local HF exchange in B3LYP. The result provided in the Table is obtained with default 20% of HF exchange. Lowering HF exchange contribution down to 14% we have been able to reproduce experimental $\Delta \varepsilon_{\mathrm{g}}$ (3.16 vs. 3.18 eV) while TiO₂ lattice constants remain practically unchanged.

3. Results and discussion

In our study, we have considered four different anatase nanosheets to roll-up NTs (see Fig. 1). These are 3-layered slab cut parallel to (101) anatase face, 6-layered slab parallel to (101), 6- and 9-layered

![](./images/813289312836648961_1.jpg)

Figure 1 (color online). Schematic representation (top view and side view) of nanosheets considered in current study to roll-up NTs: (a) 3-layered anatase (101) nanosheet, (b) 6-layered anatase (101) nanosheet, (c) 6-layered anatase (001) nanosheet and (d) 9-layered anatase (001) nanosheet.

slabs parallel to (001). It is possible to form two types of titania nanotubes from the two-dimensional structure since the nanotube configuration depends on how chirality vector is oriented [7]. For 3- layered anatase (101) of hexagonal morphology [7], any (n,m) chirality indexes are possible, however, in current study, we have considered only achiral structures having (n,n) and (n,0) chirality indexes. For the rest NTs of rectangular morphology, only (n,0) and (0,n) chirality indexes are possible [7].

We have calculated energetics for NTs folded from nanosheets mentioned above and having diameters ranging from 0.6 to 4 nm. The purpose of that was to define the most energetically stable NT. According to our calculations, 9-layered (001) NT with (0,n) chirality indexes possess negative strain energy, *i.e.* it is energetically more favorable to form nanotube rather than to keep original 2D structure. Dependence of calculated strain energy on NT diameters is shown in Figure 2. It is worth mentioning that our prediction is in good agreement with earlier theoretical study performed by Ferrari *et al.* [8]. Based on our strain energy calculations (Figure 2), for further doping with sulphur, we have chosen (0,36) 9-layered anatase (2×2) (001) NT with internal diameter of 3.47 nm, wall thickness of 0.67 nm, and having 648 atoms in the unit cell. Sulphur has replaced oxygen in six possible configurations yielding defect concentration of ~8%. The notation of dopant positions is the following: S1 – dopant placed in the NT's outer wall, S2 and S3 – dopant placed in two irreducible positions of outer subsurface NT layer, S4 and S5 – dopant placed in two irreducible positions of inner subsurface NT layer, and S1 – dopant placed in the NT's inner wall.

Fig. 3 shows band edge positions calculated for TiO₂ nanosheet, pristine and S-doped NTs. For five configurations of S-doped NT, their top valence bands are essentially shifted in a beneficial position,

![](./images/813289312836648961_2.jpg)

Figure 2. Calculated strain energies, $E_{strain}$, vs. NT diameters for (0,n) 9-layered (001) NT.

![](./images/813289312836648961_3.jpg)

Figure 3. Calculated positions of band edges for TiO₂ nanosheet (2D), pristine (0,36) NT and S-doped (0,36) NTs denoted as S1 – S6 (see text). Energy scale shown with respect to standard hydrogen electrode (SHE, -4.44 eV vs. vacuum level). Dash-dotted line corresponds to the oxygen redox potential (-1.23 eV).

while the bottoms of conduction bands are positioned substantially above the standard hydrogen electrode (SHE, -4.44 eV vs. vacuum level). However, there is a single configuration (S1) where bottom of conduction bands lies close to SHE. In this last case dopant is introduced into the outer NT surface layer, and it occurs to be the most energetically favorable position. The band gap of this structure is 2.72 eV (narrower with respect to the bulk TiO₂) which is close to interval required for construction of efficient visible-light-driven photocatalysts.

### 4. Conclusion
In current study, we have defined the most energetically stable nanotube. It can be folded from 9-layered anatase (001) nanosheet with chirality indices (0,n). We have performed calculations for the S-doped (0,36) NT. Doping of nanotubular TiO₂ by sulphur results in narrowing of its band gap with the band edges positions, close to the limits required for efficient H₂O splitting. Therefore, S-doped NT can be predicted as suitable photoanode for day-light photocatalytic applications. The energetically favorable position of S dopant is in the outer surface layer of the NT.

### Acknowledgements.
S.P. is thankful for the financial support through the ESF project No. 2009/0216/1DP/1.1.1.2.0/09/APIA/VIAA/044.

### References
[1] Cook T R, Dogutan D K, Reece S Y, Surendranath Y, Teets T S and Nocera D G 2010 *Chem Rev* **110** 6474-6502
[2] Thimsen E, Biswas S, Lo C S and Biswas P 2009 *J Phys Chem C* **113** 2014-2021
[3] Valdes A 2012 *Phys Chem Chem Phys* **14** 49-70
[4] Kudo A and Miseki Y 2009 *Chem Soc Rev* **38** 253-278

International Conference on Functional Materials and Nanotechnologies (FM&NT2012)
IOP Publishing

IOP Conf. Series: Materials Science and Engineering **38** (2012) 012057
doi:10.1088/1757-899X/38/1/012057

[5] Periyat P, Pillai S C, McCormack D E, Colreavy J and Hinder S J 2008 *J. Phys. Chem. C* **112** 7644–7652.

[6] Dovesi R, Saunders V R, Roetti C, Orlando R, Zicovich-Wilson C M, Pascale F, Civalleri B, Doll K,
Harrison N M, Bush I J, D'Arco Ph and Llunell M. *CRYSTAL-2009 User Manual*: University of Torino:
Turin 2009

[7] Piskunov S, Heifets E, Eglitis R I and G. Borstel 2004 *Comput Mater Sci* **29** 165-178

[8] Evarestov R A, Bandura A V, Losev M V, Piskunov S and Zhukovskii Yu F 2010 *Physica E* **43** 266-278

[9] Ferrari A M, Szieberth D, Zicovich-Wilson C M and Demichelis R 2010 *J Phys Chem Lett* **1** 2854–2857