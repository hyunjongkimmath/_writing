# Analytic Number Theory Checklist

**Purpose:** Track coverage of analytic number theory topics — zeta/L-functions, prime distribution, analytic methods, and connections to arithmetic geometry.
**Source of truth:** `AnalyticNumberTheory/content.tex` (currently empty except `\nocite{*}`) + `_definitions/` + `_concepts/` file existence.
**Cross-ref:** `LFunctions`, `AlgebraicNumberTheory`, `AutomorphicForms`, `GaussSumsAndKloostermanSums`, `Langlands`, `TatesThesis`, `FourierAnalysisOnDerivedCategories`, `RepresentationTheory`, `Probability`, `QuantumFieldTheory`, `RealAndComplexAnalysis` vaults.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ **ACTIVE** | Wired in `content.tex` (not commented), definition file exists |
| 📝 **DEFINED** | Definition file exists in `_definitions/` or `_concepts/`, not yet wired |
| ⏳ **DRAFT** | Draft exists in `_assembly/`, needs review/move |
| ❌ **MISSING** | No file exists, not in content.tex |
| 💬 **COMMENTED** | Referenced in `content.tex` but commented out |
| 🔗 **EXT REF** | Referenced from another vault (definition exists elsewhere) |

---

## Phase 0: Foundations (Complex Analysis & Harmonic Analysis Prerequisites)

**Note:** Many foundational items exist in `RealAndComplexAnalysis` vault — cross-ref them rather than duplicate.

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 0.1 | Complex analysis: holomorphic/meromorphic, residues, Cauchy theory | 🔗 **EXT REF** | `RealAndComplexAnalysis`: `definition_holomorphic_function...`, `definition_meromorphic_function...`, `definition_contour_integral...`, `definition_residue...`, `definition_isolated_singularity...` | `RealAndComplexAnalysis`: `theorem_cauchy_integral_theorem...`, `theorem_cauchy_integral_formula...`, `theorem_the_residue_theorem...`, `theorem_riemanns_theorem_on_removable_singularities.tex` | Cauchy integral theorem/formula, residue theorem, winding number in RealAndComplexAnalysis §7–8 |
| 0.2 | Entire functions, order/growth, Hadamard factorization | ❌ **MISSING** | | | Weierstrass/Hadamard products, genus — needed for $\xi(s)$ |
| 0.3 | Gamma function $\Gamma(s)$, functional equation, Stirling | 📝 **DEFINED** | `definition_gamma_function.tex` (in `_definitions/`, also in RealAndComplexAnalysis) | | Reflection formula, duplication, Stirling need expansion |
| 0.4 | Mellin transform, inverse Mellin, Parseval/Plancherel | ❌ **MISSING** | `definition_mellin_transform_of_a_measurable_function_on_the_positive_real_numbers.tex` exists | | $\int_0^\infty f(x)x^{s-1}dx$ — definition exists but no properties/theorems |
| 0.5 | Fourier analysis on $\mathbb{R}$, $\mathbb{R}/\mathbb{Z}$, $\mathbb{Q}_p$, adèles | 🔗 **EXT REF** | `RealAndComplexAnalysis`: `definition_fourier_transform_of_an_L_1_function_on_R.tex`, `definition_fourier_transform_of_an_L_2_function.tex`, `definition_fourier_transform_of_a_function_on_a_locally_compact_abelian_group.tex` | | Adèlic Fourier in `TatesThesis` |
| 0.6 | Poisson summation formula | ❌ **MISSING** | | | $\sum_{n\in\mathbb{Z}} f(n) = \sum_{n\in\mathbb{Z}} \hat{f}(n)$ — crucial for functional equations |
| 0.7 | Dirichlet series: abscissae of convergence, Landau's theorem | 📝 **DEFINED** | `definition_dirichlet_series.tex`, `definition_dirichlet_series_of_a_sequence_of_complex_numbers.tex` | `proposition_uniform_convergence_of_dirichlet_series_on_compact_subsets.tex`, `proposition_uniform_convergence_of_termwise_derivatives_of_dirichlet_series.tex`, `corollary_termwise_differentiation_of_dirichlet_series.tex` | In `_definitions/` & `_concepts/`; also in RealAndComplexAnalysis §10 |
| 0.8 | Perron's formula, inverse Mellin for Dirichlet series | ❌ **MISSING** | | | $\sum_{n\leq x} a_n = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} D(s)\frac{x^s}{s}ds$ |
| 0.9 | Tauberian theorems (Ikehara, Wiener-Ikehara) | ❌ **MISSING** | | | For prime number theorem |
| 0.10 | Complex Tauberian theorems (Ingham, Korevaar) | ❌ **MISSING** | | | |
| 0.11 | Phragmén-Lindelöf principle, convexity bounds | ❌ **MISSING** | | | For subconvexity, Lindelöf hypothesis |
| 0.12 | Logarithmic integral $\mathrm{Li}(x)$, Chebyshev functions $\psi(x), \vartheta(x)$ | ❌ **MISSING** | | | Core to PNT statements |

---

## Phase 1: Zeta and L-Functions — Foundations

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 1.1 | **Riemann zeta function** $\zeta(s)$: definition, Euler product | 📝 **DEFINED** | `definition_riemann_zeta_function.tex` | | In `_definitions/`; has TODOs for continuation, trivial zeros, functional equation |
| 1.2 | **Analytic continuation** of $\zeta(s)$ to $\mathbb{C}\setminus\{1\}$ | ❌ **MISSING** | | | Via $\xi(s)$ or Riemann's functional equation |
| 1.3 | **Functional equation**: $\xi(s) = \xi(1-s)$ with $\xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$ | ❌ **MISSING** | | | Proof via Poisson summation / theta function |
| 1.4 | **Trivial zeros** at $s=-2,-4,\ldots$; pole at $s=1$ with residue 1 | ❌ **MISSING** | | | |
| 1.5 | **Riemann Hypothesis**: all non-trivial zeros on $\Re(s)=1/2$ | ❌ **MISSING** | | | Statement, equivalent forms |
| 1.6 | **Zero-free region**: classical $\Re(s) \geq 1 - c/\log|t|$ | ❌ **MISSING** | | | de la Vallée Poussin, Korobov-Vinogradov |
| 1.7 | **Dirichlet characters** $\chi \pmod{q}$ | 📝 **DEFINED** | `definition_dirichlet_character_modulo_a_nonnegative_integer.tex` | | In `_definitions/` |
| 1.8 | **Dirichlet L-functions** $L(s,\chi)$: definition, Euler product | 📝 **DEFINED** | `definition_dirichlet_L_function_of_a_dirichlet_character_modulo_a_nonnegative_integer.tex` | | In `_definitions/`; has TODOs for continuation, trivial zeros, functional equation |
| 1.9 | Analytic continuation of $L(s,\chi)$; entire if $\chi\neq\chi_0$ | ❌ **MISSING** | | | |
| 1.10 | Functional equation for $L(s,\chi)$ (Gauss sums, root number) | ❌ **MISSING** | | | $\Lambda(s,\chi) = \varepsilon(\chi)\Lambda(1-s,\bar{\chi})$ |
| 1.11 | **Dirichlet's theorem** on primes in arithmetic progressions | ❌ **MISSING** | | | Uses non-vanishing $L(1,\chi)\neq 0$ |
| 1.12 | **Dedekind zeta function** $\zeta_K(s)$ of a number field | 📝 **DEFINED** | `definition_dedekind_zeta_function_of_a_number_field.tex` | | In `_definitions/`; has TODOs for Euler product, continuation, functional equation, trivial zeros |
| 1.13 | Analytic continuation, functional equation of $\zeta_K(s)$ | ❌ **MISSING** | | | |
| 1.14 | **Hecke characters** (Größencharaktere) and **Hecke L-functions** | 📝 **DEFINED** | `definition_hecke_character_of_a_number_field.tex`, `definition_hecke_L_function_of_a_hecke_character_of_a_number_field.tex`, `definition_completed_hecke_L_function_of_a_hecke_character_of_a_number_field.tex` | `theorem_functional_equation_for_a_hecke_L_function_of_a_hecke_character_of_a_number_field.tex` | In `_definitions/` & `_concepts/`; functional equation theorem exists |
| 1.15 | **Artin L-functions** $L(s,\rho)$ for Galois representations | ❌ **MISSING** | | | Induction from 1-dim, Artin conjecture |
| 1.16 | **Weil L-functions** of varieties over finite fields | 📝 **DEFINED** | `definition_L_function_of_a_constructible_complex_on_a_scheme_of_finite_type_over_a_finite_field.tex` | `theorem_grothendieck_L_function_of_a_complex_is_a_determinant_of_the_total_compactly_supported_cohomology_of_the_complex.tex` | In `LFunctions` vault |
| 1.17 | **Hasse-Weil zeta function** of a scheme over a number field | 📝 **DEFINED** | In `LFunctions/content.tex` (Definition) | | In `LFunctions` vault |

---

## Phase 2: Prime Number Theorem & Distribution of Primes

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 2.1 | **Chebyshev functions**: $\psi(x)=\sum_{n\leq x}\Lambda(n)$, $\vartheta(x)=\sum_{p\leq x}\log p$ | ❌ **MISSING** | | | von Mangoldt function $\Lambda(n)$ |
| 2.2 | **Prime Number Theorem**: $\pi(x) \sim x/\log x$ | ❌ **MISSING** | | | Equivalent to $\psi(x)\sim x$ |
| 2.3 | **Proof via complex analysis**: $\zeta(s)$ zero-free region $\Rightarrow$ PNT | ❌ **MISSING** | | | Hadamard/de la Vallée Poussin |
| 2.4 | **Error term**: $\pi(x) = \mathrm{Li}(x) + O(x e^{-c\sqrt{\log x}})$ | ❌ **MISSING** | | | Classical zero-free region |
| 2.5 | **Explicit formula**: $\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \frac{\zeta'(0)}{\zeta(0)} - \frac12\log(1-x^{-2})$ | ❌ **MISSING** | | | Sum over non-trivial zeros $\rho$ |
| 2.6 | **Riemann Hypothesis $\Leftrightarrow$** $\psi(x) = x + O(\sqrt{x}\log^2 x)$ | ❌ **MISSING** | | | von Koch (1901) |
| 2.7 | **Chebyshev's bias** / prime races | ❌ **MISSING** | | | $\pi(x;q,a)$ vs $\pi(x;q,b)$ |
| 2.8 | **Mertens theorems**: $\sum_{p\leq x} \frac{\log p}{p} = \log x + O(1)$ etc. | ❌ **MISSING** | | | |
| 2.9 | **Brun's sieve** / **Selberg sieve** — upper bounds for twin primes, etc. | ❌ **MISSING** | | | |
| 2.10 | **Bombieri-Vinogradov theorem**: $\sum_{q\leq Q} \max_{a} |\pi(x;q,a) - \frac{\pi(x)}{\phi(q)}| \ll \frac{x}{(\log x)^A}$ | ❌ **MISSING** | | | $Q = x^{1/2}(\log x)^{-B}$ |
| 2.11 | **Elliott-Halberstam conjecture** | ❌ **MISSING** | | | $Q = x^{1-\varepsilon}$ |
| 2.12 | **GPY / Zhang-Maynard-Tao** bounded gaps between primes | ❌ **MISSING** | | | $p_{n+1}-p_n \leq 246$ (Polymath) |

---

## Phase 3: Primes in Arithmetic Progressions

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 3.1 | **Dirichlet's theorem**: $\pi(x;q,a) \sim \frac{1}{\phi(q)}\frac{x}{\log x}$ for $(a,q)=1$ | ❌ **MISSING** | | | Non-vanishing $L(1,\chi)\neq 0$ |
| 3.2 | **Siegel-Walfisz theorem**: uniform in $q \leq (\log x)^A$ | ❌ **MISSING** | | | Ineffective constant (Siegel zero) |
| 3.3 | **Linnik's theorem**: least prime in AP $\ll q^L$ ($L=5$ current best) | ❌ **MISSING** | | | |
| 3.4 | **Chebotarev density theorem** (analytic proof via Artin L-functions) | 💬 **COMMENTED** | In `AlgebraicNumberTheory/content.tex` (TODO) | `theorem_chebotarev_density_*` (inline) | In `AlgebraicNumberTheory` vault |
| 3.5 | **Effective Chebotarev** (Lagarias-Odlyzko, Serre) | ❌ **MISSING** | | | GRH-dependent and unconditional |
| 3.6 | **Lang-Trotter conjecture** for elliptic curves | ❌ **MISSING** | | | Distribution of $a_p(E)$ |

---

## Phase 4: Zeros of L-Functions & Explicit Formulae

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 4.1 | **Zero-free regions** for $\zeta(s)$ and $L(s,\chi)$ | ❌ **MISSING** | | | Classical, Vinogradov-Korobov, Siegel zero exception |
| 4.2 | **Density theorems**: $N(\sigma,T) \ll T^{c(1-\sigma)}\log^A T$ | ❌ **MISSING** | | | Carlson, Halász, Montgomery |
| 4.3 | **Montgomery's pair correlation conjecture** | ❌ **MISSING** | | | $1-(\frac{\sin\pi u}{\pi u})^2$ |
| 4.4 | **Explicit formula** for $\psi(x)$, $\pi(x)$ in terms of zeros | ❌ **MISSING** | | | Weil's explicit formula (general) |
| 4.5 | **Weil's explicit formula** for general L-functions | 📝 **DEFINED** | In `LFunctions` content? | | Need to check |
| 4.6 | **Guinand-Weil explicit formula** (distributional) | ❌ **MISSING** | | | $\sum_\rho \hat{h}(\rho) = \dots$ |
| 4.7 | **Zero density estimates** for families of L-functions | ❌ **MISSING** | | | |
| 4.8 | **Selberg's zero density theorem** | ❌ **MISSING** | | | |

---

## Phase 5: Additive Number Theory & Circle Method

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 5.1 | **Hardy-Littlewood circle method**: major/minor arcs | ❌ **MISSING** | | | $f(\alpha) = \sum a_n e(n\alpha)$ |
| 5.2 | **Vinogradov's theorem**: every large odd $n$ is sum of 3 primes | ❌ **MISSING** | | | Ternary Goldbach |
| 5.3 | **Goldbach's ternary problem** (Helfgott 2013: all $n\geq 7$) | ❌ **MISSING** | | | |
| 5.4 | **Binary Goldbach** / Chen's theorem (prime + $P_2$) | ❌ **MISSING** | | | |
| 5.5 | **Waring's problem**: $g(k)$, $G(k)$ | ❌ **MISSING** | | | Sums of $k$th powers |
| 5.6 | **Hardy-Littlewood asymptotic formula** for representations | ❌ **MISSING** | | | Singular series / singular integral |
| 5.7 | **Vinogradov's mean value theorem** (Wooley, Bourgain-Demeter-Guth) | ❌ **MISSING** | | | Decoupling / efficient congruencing |

---

## Phase 6: Exponential Sums & Sieve Methods

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 6.1 | **Gauss sums** $g(\chi) = \sum \chi(x)e^{2\pi i x/p}$ | 📝 **DEFINED** | `definition_gauss_sum_of_a_dirichlet_character.tex` (in GaussSumsAndKloostermanSums) | | See `GaussSumsAndKloostermanSums` vault |
| 6.2 | **Kloosterman sums** $S(m,n;c) = \sum_{x\in(\mathbb{Z}/c\mathbb{Z})^\times} e(\frac{mx+n\bar{x}}{c})$ | 📝 **DEFINED** | `definition_kloosterman_sum.tex`, `definition_hyper_kloosterman_sum.tex` | `proposition_bound_on_nonnormalized_hyper_kloosterman_sums.tex` | In `GaussSumsAndKloostermanSums` & `LFunctions` |
| 6.3 | **Weil bounds** for Kloosterman sums: $|S(m,n;c)| \leq \tau(c)\sqrt{c}\gcd(m,n,c)^{1/2}$ | ❌ **MISSING** | | | Weil 1948; Deligne for higher dim |
| 6.4 | **Estermann's bound** / **Kuznetsov trace formula** | ❌ **MISSING** | | | |
| 6.5 | **Selberg sieve** / **Large sieve** / **Bombieri-Vinogradov** | ❌ **MISSING** | | | |
| 6.6 | **Fundamental lemma of sieve theory** | ❌ **MISSING** | | | |
| 6.7 | **GPY sieve** / **Maynard-Tao** / **Polymath8b** | ❌ **MISSING** | | | Bounded gaps |

---

## Phase 7: Automorphic Forms & L-Functions (Analytic Perspective)

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 7.1 | **Modular forms** $f(z)=\sum a_n e^{2\pi i n z}$ for $\mathrm{SL}_2(\mathbb{Z})$ | 📝 **DEFINED** | In `AutomorphicForms`, `EllipticCurves` vaults | | |
| 7.2 | **Hecke operators** $T_n$, $L(s,f) = \sum a_n n^{-s}$ | 📝 **DEFINED** | In `AutomorphicForms`, `LFunctions` | | |
| 7.3 | **Analytic continuation & functional equation** of $L(s,f)$ | 📝 **DEFINED** | `definition_L_function_of_a_modular_form.tex` in `LFunctions` | `theorem_functional_equation_for_hecke_L_function` | |
| 7.4 | **Petersson trace formula** | ❌ **MISSING** | | | |
| 7.5 | **Kuznetsov trace formula** (sums of Kloosterman sums) | ❌ **MISSING** | | | |
| 7.6 | **Maass forms** / continuous spectrum / Eisenstein series | 📝 **DEFINED** | In `AutomorphicForms`, `RepresentationTheory` | | |
| 7.7 | **Langlands program** (analytic side): functoriality, $L$-functions | 📝 **DEFINED** | In `Langlands` vault | | |
| 7.8 | **Rankin-Selberg convolution** $L(s,f\times g)$ | ❌ **MISSING** | | | Integral representation |
| 7.9 | **Triple product L-functions** | ❌ **MISSING** | | | |
| 7.10 | **Symmetric power L-functions** (Newton-Thorne, etc.) | ❌ **MISSING** | | | |
| 7.11 | **Standard L-function of $\mathrm{GL}(n)$** | 📝 **DEFINED** | In `Langlands` / `AutomorphicForms` | | Godement-Jacquet / Shahidi |
| 7.12 | **Local L-factors, $\varepsilon$-factors, $\gamma$-factors** | 📝 **DEFINED** | In `Langlands`, `PAdicHodgeTheory`, `TatesThesis` | | Tate's thesis (archimedean + non-archimedean) |

---

## Phase 8: Analytic Theory of Automorphic L-Functions

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 8.1 | **Converse theorems** (Weil, Jacquet-Piatetski-Shapiro-Shalika) | ❌ **MISSING** | | | Characterizing automorphic forms by L-functions |
| 8.2 | **Analytic properties**: poles, zero-free regions, density theorems | ❌ **MISSING** | | | For $\mathrm{GL}(n)$ L-functions |
| 8.3 | **Subconvexity bounds**: $L(1/2,\pi) \ll C(\pi)^{1/4-\delta}$ | ❌ **MISSING** | | | Burgess, Duke-Friedlander-Iwaniec, Blomer-Harcos, etc. |
| 8.4 | **Lindelöf hypothesis** for L-functions | ❌ **MISSING** | | | $\ll_\varepsilon C(\pi)^\varepsilon$ |
| 8.5 | **Moments of L-functions**: $\int_0^T |L(1/2+it)|^{2k} dt$ | ❌ **MISSING** | | | Conrey-Ghosh, Keating-Snaith, Harper |
| 8.6 | **One-level density** of low-lying zeros (Katz-Sarnak) | ❌ **MISSING** | | | Symmetry types: unitary, symplectic, orthogonal |
| 8.7 | **Quantum unique ergodicity** (QUE) / Arithmetic quantum chaos | ❌ **MISSING** | | | Lindenstrauss, Soundararajan |

---

## Phase 9: $p$-adic Analytic Methods

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 9.1 | **$p$-adic L-functions** (Kubota-Leopoldt, Iwasawa) | ❌ **MISSING** | | | Interpolation of $L(1-n,\chi)$ |
| 9.2 | **Iwasawa theory**: $\Lambda = \mathbb{Z}_p[[\Gamma]]$, characteristic ideals | ❌ **MISSING** | | | Main conjecture (Mazur-Wiles, Kato, etc.) |
| 9.3 | **$p$-adic modular forms** (Serre, Katz, Hida) | ❌ **MISSING** | | | Ordinary / Hida families |
| 9.4 | **Eisenstein measure** / $p$-adic Rankin-Selberg | ❌ **MISSING** | | | |
| 9.5 | **$p$-adic Langlands program** (Colmez, Berger, Breuil, etc.) | 📝 **DEFINED** | In `PAdicRepresentationTheory`, `Langlands` | | |
| 9.6 | **$p$-adic L-functions for automorphic forms** | ❌ **MISSING** | | | |

---

## Phase 10: Analytic Methods in Arithmetic Geometry

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 10.1 | **Weil conjectures** (Dwork, Grothendieck, Deligne) | 📝 **DEFINED** | In `LFunctions` (Weil conjectures cohomological form) | | Rationality, functional equation, Riemann hypothesis |
| 10.2 | **Zeta functions of varieties over finite fields** | 📝 **DEFINED** | `definition_zeta_function_of_a_finite_type_scheme_over_a_finite_field.tex`, `theorem_weil_conjectures_cohomological_form.tex` | | In `LFunctions` |
| 10.3 | **Hasse-Weil L-functions** of varieties over number fields | 📝 **DEFINED** | In `LFunctions` | | |
| 10.4 | **Birch and Swinnerton-Dyer conjecture** (analytic rank = algebraic rank) | ❌ **MISSING** | | | |
| 10.5 | **Tate's thesis**: harmonic analysis on adèles, functional equation | 📝 **DEFINED** | In `TatesThesis` vault | | Self-duality of adèles, $\int_{\mathbb{A}_K} f(x)\chi(x)dx$ |
| 10.6 | **Weil representation** / **theta correspondence** | 📝 **DEFINED** | In `RepresentationTheory`, `AutomorphicForms` | | |
| 10.7 | **Relative trace formula** (Jacquet, Zhang, etc.) | ❌ **MISSING** | | | |
| 10.8 | **Period integrals** and L-values (Gross-Zagier, Waldspurger) | ❌ **MISSING** | | | |

---

## Phase 11: Probabilistic Number Theory & Random Matrix Theory

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 11.1 | **Erdős-Kac theorem**: $\omega(n)$ is Gaussian | ❌ **MISSING** | | | Additive number theory |
| 11.2 | **Selberg's central limit theorem** for $\log|\zeta(1/2+it)|$ | ❌ **MISSING** | | | |
| 11.3 | **Random matrix theory**: eigenvalues of $U(N)$, $SO(2N)$, $USp(2N)$ | 📝 **DEFINED** | In `Probability`, `QuantumFieldTheory` | | Keating-Snaith moments conjecture |
| 11.4 | **Katz-Sarnak philosophy**: zeros of L-functions $\sim$ eigenvalues | ❌ **MISSING** | | | Symmetry types |
| 11.5 | **One-level density** / **n-level correlations** of zeros | ❌ **MISSING** | | | |
| 11.6 | **Möbius randomness** / **Sarnak's conjecture** | ❌ **MISSING** | | | $\sum \mu(n)f(n) = o(N)$ for deterministic $f$ |
| 11.7 | **Chowla conjecture** / **Elliott conjecture** | ❌ **MISSING** | | | Correlations of $\mu$, $\lambda$ |

---

## Phase 12: Computational / Algorithmic Analytic Number Theory

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 12.1 | **Computing $\zeta(s)$ zeros** (Odlyzko-Schönhage, Turing method) | ❌ **MISSING** | | | |
| 12.2 | **Computing L-functions** (Rubinstein's lcalc, PARI/GP, LMFDB) | ❌ **MISSING** | | | |
| 12.3 | **Explicit bounds** for zeros, primes, character sums | ❌ **MISSING** | | | Explicit formulae with constants |
| 12.4 | **Verified computation** (interval arithmetic, rigorous numerics) | ❌ **MISSING** | | | |

---

## Cross-Reference with Other Vaults

| Vault | Relevant Content | Status |
|-------|-----------------|--------|
| **LFunctions** | General L-function definitions, Grothendieck L-functions, Hasse-Weil zeta, Weil conjectures | 📝 **DEFINED** (many) |
| **AlgebraicNumberTheory** | Number fields, class field theory, Chebotarev, Dedekind zeta, Hecke L-functions | 📝 **DEFINED** (many) |
| **AutomorphicForms** | Modular forms, Maass forms, Hecke operators, Langlands | 📝 **DEFINED** |
| **GaussSumsAndKloostermanSums** | Gauss sums, Kloosterman sums, hyper-Kloosterman, bounds | 📝 **DEFINED** |
| **TatesThesis** | Adèles, idèles, Fourier analysis, local functional equations | 📝 **DEFINED** |
| **PAdicHodgeTheory** | $p$-adic periods, Fontaine's rings, $p$-adic L-functions | 📝 **DEFINED** |
| **Langlands** | Global Langlands, functoriality, trace formula | 📝 **DEFINED** |
| **RepresentationTheory** | Local Langlands, $\mathrm{GL}(n)$, Whittaker models | 📝 **DEFINED** |
| **FourierAnalysisOnDerivedCategories** | Fourier-Mukai, derived categories | 📝 **DEFINED** |
| **RealAndComplexAnalysis** | Foundational analysis (holomorphic functions, contour integration, residue theorem, gamma function, Dirichlet series, Fourier on LCA groups) | 🔗 **EXT REF** |

---

## Immediate Next Steps (Priority Order)

### 📝 **Input Existing Definitions into `content.tex`** (High Priority)
These files exist in vault but are NOT in `content.tex`:

| File | Suggested Section |
|------|-------------------|
| `definition_riemann_zeta_function.tex` | Phase 1.1 |
| `definition_dirichlet_character_modulo_a_nonnegative_integer.tex` | Phase 1.7 |
| `definition_dirichlet_L_function_of_a_dirichlet_character_modulo_a_nonnegative_integer.tex` | Phase 1.8 |
| `definition_dedekind_zeta_function_of_a_number_field.tex` | Phase 1.12 |
| `definition_hecke_character_of_a_number_field.tex` | Phase 1.14 |
| `definition_hecke_L_function_of_a_hecke_character_of_a_number_field.tex` | Phase 1.14 |
| `definition_completed_hecke_L_function_of_a_hecke_character_of_a_number_field.tex` | Phase 1.14 |
| `theorem_functional_equation_for_a_hecke_L_function_of_a_hecke_character_of_a_number_field.tex` | Phase 1.14 |
| `definition_gamma_function.tex` | Phase 0.3 |
| `definition_dirichlet_series.tex`, `definition_dirichlet_series_of_a_sequence_of_complex_numbers.tex` | Phase 0.7 |
| `definition_absolute_value_on_a_ring_valued_in_an_ordered_semiring.tex` | Phase 0 |
| `definition_absolute_convergence_of_a_series_in_module_over_a_commutative_ring_with_an_absolute_value_valued_in_an_ordered_semiring.tex` | Phase 0 |

### ❌ **Create Missing Core Theorems** (High Priority)
No vault files exist for these fundamental results:

1. **Analytic continuation & functional equation of $\zeta(s)$** (Riemann's $\xi(s)$)
2. **Prime Number Theorem** (with error term)
3. **Dirichlet's theorem on primes in AP** (non-vanishing $L(1,\chi)\neq 0$)
4. **Explicit formula** for $\psi(x)$ (Riemann-von Mangoldt)
5. **Weil bounds for Kloosterman sums** (or reference Deligne)
6. **Bombieri-Vinogradov theorem**
7. **Functional equation for Dirichlet $L(s,\chi)$** (Gauss sums, root number)
8. **Siegel-Walfisz theorem**
9. **Chebotarev density theorem** (complete statement with definitions)
10. **Tate's thesis** summary (adèlic Fourier analysis, local/global functional equations)

### 📝 **Complete TODOs in Existing Files**
- `definition_riemann_zeta_function.tex` has `\TODO` for meromorphic continuation, trivial zeros, functional equation
- `definition_dirichlet_L_function_of_a_dirichlet_character_modulo_a_nonnegative_integer.tex` has similar TODOs
- `definition_dedekind_zeta_function_of_a_number_field.tex` has TODOs for Euler product, meromorphic continuation, functional equation, trivial zeros
- `LFunctions/content.tex` has incomplete Galois representation definition, Fourier L-functions, Grothendieck-Weil L-function definition

---

## Proposed `content.tex` Structure (Target)

```latex
\part{Foundations}
\chapter{Complex Analysis and Harmonic Analysis Prerequisites}
\section{Dirichlet Series and Mellin Transforms}
\section{Gamma Function and Functional Equations}
\section{Fourier Analysis on Adèles} (ref: TatesThesis, FourierAnalysisOnDerivedCategories)

\part{Zeta and L-Functions}
\chapter{The Riemann Zeta Function}
\section{Definition, Euler Product, Convergence}
\section{Analytic Continuation and Functional Equation}
\section{Zeros: Trivial, Non-Trivial, Riemann Hypothesis}
\section{Zero-Free Regions and Density Theorems}

\chapter{Dirichlet L-Functions}
\section{Dirichlet Characters}
\section{Definition and Analytic Properties}
\section{Functional Equation (Gauss Sums)}
\section{Non-Vanishing at $s=1$ and Dirichlet's Theorem}

\chapter{L-Functions of Number Fields}
\section{Dedekind Zeta Functions}
\section{Hecke Characters and Hecke L-Functions}
\section{Artin L-Functions (statement of Artin conjecture)}

\chapter{Automorphic L-Functions} (ref: AutomorphicForms, Langlands)
\section{Modular Forms and Hecke L-Functions}
\section{GL(n) L-Functions}
\section{Local Factors and $\varepsilon$-Factors} (ref: TatesThesis)

\part{Distribution of Primes}
\chapter{Prime Number Theorem}
\section{Chebyshev Functions and Equivalences}
\section{Proof via Zero-Free Region}
\section{Error Terms and Explicit Formula}
\section{RH $\Leftrightarrow$ Optimal Error Term}

\chapter{Primes in Arithmetic Progressions}
\section{Siegel-Walfisz Theorem}
\section{Bombieri-Vinogradov Theorem}
\section{Chebotarev Density Theorem} (ref: AlgebraicNumberTheory)
\section{Bounded Gaps Between Primes}

\chapter{Sieve Methods}
\section{Selberg Sieve}
\section{Large Sieve}
\section{GPY/Maynard-Tao Sieve}

\part{Exponential Sums and Additive Problems}
\chapter{Gauss and Kloosterman Sums} (ref: GaussSumsAndKloostermanSums)
\chapter{Hardy-Littlewood Circle Method}
\section{Vinogradov's Theorem (Ternary Goldbach)}
\section{Waring's Problem}
\chapter{Trace Formulae} (ref: AutomorphicForms, Langlands)
\section{Petersson Trace Formula}
\section{Kuznetsov Trace Formula}

\part{Advanced Topics}
\chapter{$p$-adic Analytic Methods} (ref: PAdicHodgeTheory, PAdicRepresentationTheory)
\chapter{Analytic Methods in Arithmetic Geometry} (ref: LFunctions, AutomorphicForms)
\chapter{Probabilistic Number Theory and Random Matrix Theory} (ref: Probability, QuantumFieldTheory)
\chapter{Computational Analytic Number Theory}
```

---

## Notes for Writing

- **Tate's thesis** is the bridge between classical analytic number theory and modern automorphic forms — self-duality of adèles, local functional equations, global functional equation via Poisson summation.
- **L-functions** are the central organizing principle: every major result connects to analytic properties of some L-function.
- **Explicit formulae** are the key tool linking zeros to primes — the "spectral" side (zeros) vs "geometric" side (primes).
- **Trace formulae** (Petersson, Kuznetsov, Selberg, Arthur) are the main machinery for moments, subconvexity, equidistribution.
- **Random matrix theory** (Katz-Sarnak) provides precise conjectures for zero statistics and moments.
- **$p$-adic L-functions** interpolate special values; Iwasawa theory relates them to Selmer groups (main conjecture).
- **All comparison isomorphisms** (Betti, de Rham, étale, crystalline) for varieties over number fields are ultimately about special values of L-functions (Deligne's conjecture, Beilinson's conjectures, BSD).