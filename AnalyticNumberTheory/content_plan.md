# Analytic Number Theory — Content Plan

This file lists (1) existing `.tex` files that should be `\input`'d into `AnalyticNumberTheory/content.tex`, and (2) missing definitions/concepts that need to be written for a complete analytic number theory treatment.

---

## Part 1: Files to \input into content.tex

### Section 0 — Prerequisites from other areas (if needed)
```latex
\input{../_definitions/definition_absolute_convergence_of_a_series_in_module_over_a_commutative_ring_with_an_absolute_value_valued_in_an_ordered_semiring}
\input{../_definitions/definition_infinite_series_in_a_topological_abelian_semigroup}
\input{../_concepts/theorem_weierstrass_m_test_for_uniform_convergence_of_function_series}
\input{../_concepts/theorem_comparison_test_for_series_of_nonnegative_real_numbers}
\input{../_concepts/theorem_termwise_differentiation_of_series_under_uniform_convergence_of_derivative_series}
\input{../_definitions/definition_differentiability_classes_Ck_Cinfty_and_Comega_for_real_valued_functions}
\input{../_definitions/definition_natural_logarithm_as_inverse_of_exponential}
```

### Section 1 — Arithmetic functions and Dirichlet convolution
```latex
% --- Definitions ---
\input{../_definitions/definition_arithmetic_function_on_positive_integers_with_values_in_a_ring}
\input{../_definitions/definition_multiplicative_function_on_positive_integers_with_values_in_a_ring}
\input{../_definitions/definition_completely_multiplicative_function_on_positive_integers_with_values_in_a_ring}
\input{../_definitions/definition_dirichlet_convolution_of_arithmetic_functions}

% --- Concepts ---
\input{../_concepts/proposition_mobius_inversion_formula}
```

### Section 2 — Key arithmetic functions
```latex
% --- Definitions ---
\input{../_definitions/definition_mobius_function_on_positive_integers}
\input{../_definitions/definition_euler_totient_function}

% --- Concepts ---
\input{../_concepts/proposition_formula_for_euler_totient_function}
```

### Section 3 — Dirichlet series and convergence theory
```latex
% --- Definitions ---
\input{../_definitions/definition_dirichlet_series_of_a_sequence_of_complex_numbers}
% Note: definition_dirichlet_series.tex exists as a duplicate; review which to keep.

% --- Concepts ---
\input{../_concepts/proposition_uniform_convergence_of_dirichlet_series_on_compact_subsets}
\input{../_concepts/proposition_uniform_convergence_of_termwise_derivatives_of_dirichlet_series}
\input{../_corollary_termwise_differentiation_of_dirichlet_series}  % verify corollary prefix
```

### Section 4 — Zeta functions and L-functions
```latex
% --- Definitions ---
\input{../_definitions/definition_gamma_function}
\input{../_definitions/definition_riemann_zeta_function}
\input{../_definitions/definition_dirichlet_character_modulo_a_nonnegative_integer}
\input{../_definitions/definition_dirichlet_L_function_of_a_dirichlet_character_modulo_a_nonnegative_integer}
\input{../_definitions/definition_dedekind_zeta_function_of_a_number_field}

% --- Concepts ---
\input{../_concepts/theorem_riemann_zeta_function_infinitely_differentiable_on_real_greater_than_one}
```

---

## Part 2: Missing content to write

### A. Foundational definitions (to be placed in `_definitions/`)

| # | Suggested label | Description | Section |
|---|-----------------|-------------|---------|
| 1 | `definition_von_mangoldt_function_on_positive_integers` | $\Lambda(n) = \log p$ if $n=p^k$, else $0$. Fundamental for prime number theorem. | §2 |
| 2 | `definition_chebyshev_functions_theta_and_psi` | $\theta(x)=\sum_{p\le x}\log p$, $\psi(x)=\sum_{n\le x}\Lambda(n)$. Central objects in analytic approach to PNT. | §2 |
| 3 | `definition_prime_counting_function` | $\pi(x)$ = number of primes $\le x$. The main object of study. | §2 |
| 4 | `definition_liouville_lambda_function_on_positive_integers` | $\lambda(n)=(-1)^{\Omega(n)}$ where $\Omega(n)$ is total prime factors with multiplicity. Completely multiplicative. | §2 |
| 5 | `definition_divisor_functions_d_and_sigma_k` | $d(n)=\sigma_0(n)$ = number of divisors; $\sigma_k(n)=\sum_{d|n} d^k$. Multiplicative functions. | §2 |
| 6 | `definition_ramanujan_tau_function` (optional) | Fourier coefficients of the discriminant modular form $\Delta(z)$. | advanced |
| 7 | `definition_natural_density_asymptotic_density_of_a_set_of_primes` | For a set $S$ of primes, density = $\lim_{x\to\infty}\frac{|\{p\in S: p\le x\}|}{\pi(x)}$. Needed to state PNT variants. | §3 |
| 8 | `definition_partial_summation_abel_summation_formula` | The summation-by-parts formula connecting $\sum a_n f(n)$ to integrals of partial sums. The key analytic tool in ANT. Can be a definition or concept. | §1–§4 |

### B. Missing concepts/theorems (to be placed in `_concepts/`)

| # | Suggested label | Description | Section |
|---|-----------------|-------------|---------|
| 1 | `theorem_von_mangoldt_sum_identity` | $\sum_{d|n}\Lambda(d)=\log n$. Fundamental identity connecting primes to Dirichlet convolution. | §2 |
| 2 | `proposition_properties_of_chebyshev_functions` | Asymptotic bounds $\psi(x)\asymp x$, $\theta(x)\asymp x$; relation $\sum_{n\le x}\frac{\Lambda(n)}{n}=\log x+O(1)$. | §2 |
| 3 | `proposition_euler_product_for_dirichlet_series_of_multiplicative_functions` | If $f$ is multiplicative, $\sum f(n)n^{-s} = \prod_p (1-f(p)p^{-s})^{-1}$ in region of absolute convergence. | §3 |
| 4 | `corollary_euler_products_for_zeta_and_L_functions` | $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ and $L(s,\chi)=\prod_p(1-\chi(p)p^{-s})^{-1}$ for Re$(s)>1$. | §4 |
| 5 | `theorem_orthogonality_relations_for_dirichlet_characters` | $\sum_{a\bmod k}\chi(a)\overline{\psi}(a) = \phi(k)$ if $\chi=\psi$, else $0$; and the dual relation over characters. Essential for primes in APs. | §4 |
| 6 | `corollary_prime_counting_function_in_terms_of_psi_and_theta` | $\pi(x)=\frac{\theta(x)}{\log x}+\int_2^x\frac{\theta(t)}{t(\log t)^2}\,dt$; PNT in terms of $\psi$ and in terms of $\pi$ are equivalent. | §3 |
| 7 | `theorem_prime_number_theorem` | $\pi(x)\sim x/\log x$, equivalently $\psi(x)\sim x$. The central theorem of ANT. | §5 |
| 8 | `theorem_zero_free_region_for_riemann_zeta_function` | There exists an absolute constant $c>0$ such that $\zeta(s)$ has no zeros in the region Re$(s)\ge 1-c/\log(|t|+2)$. Foundation of PNT proof. | §5 |
| 9 | `theorem_zero_free_region_for_dirichlet_L_functions` | Analogous zero-free region for $L(s,\chi)$; no exceptional real zero unless $\chi$ is real quadratic (Siegel zero). | §5 |
| 10 | `theorem_prime_number_theorem_in_arithmetic_progressions` | If $\gcd(a,q)=1$, then $\pi(x;q,a)\sim\frac{1}{\phi(q)}\frac{x}{\log x}$. Follows from zero-free regions for $L(s,\chi)$. | §5 |
| 11 | `theorem_error_term_in_pnt_and_zeros_of_zeta` | The error term $\pi(x)-\li(x)=O(x^{\theta})$ is equivalent to the location of zeros of $\zeta(s)$; explicit formula relating primes to zeta zeros. | §5 |
| 12 | `theorem_sieve_of_eratosthenes_and_sieve_bounds` (optional) | Basic sieve method, Brun's sieve, upper/lower bounds for sifted sets. | advanced |
| 13 | `theorem_selberg_sieve_upper_bound` (optional) | Modern sieve with Selberg weights; gives non-trivial bounds for twin primes and other additive problems. | advanced |
| 14 | `proposition_bernays_formula_for_d_n` (optional) | $d(n)=O_\varepsilon(n^\varepsilon)$; divisor function growth bound used throughout ANT estimates. | §2 |

### C. Advanced topics (for later chapters, not in immediate core)

- Hardy–Littlewood circle method and Waring's problem
- Exponential sum estimates (Weyl differencing, van der Corput, Vinogradov mean value theorem)
- Goldbach's conjecture results (Vinogradov: every large odd number is a sum of three primes; Chen: $p+p_2$ where $p_2$ has at most 2 prime factors)
- Distribution of primes in short intervals
- Zero-density estimates for $\zeta(s)$
- Siegel–Walfisz theorem (stronger form of PNT in APs)

---

## Implementation notes

1. **Check cross-references before writing**: Use `find_backlinks` or glob to verify that any label referenced by a new file actually exists.
2. **Verify duplicate removal**: `definition_dirichlet_series.tex` and `definition_dirichlet_series_of_a_sequence_of_complex_numbers.tex` overlap; decide which is more complete and remove the other before building content.tex.
3. **TODO items in existing files**: The Riemann zeta and Dirichlet L-function definitions have TODOs for meromorphic continuation, trivial zeros, and functional equation — these should be addressed as new concept files when you build that section.
4. **Follow the protocol specs** in `/_protocols/` for labeling conventions (`_definitions/`, `_concepts/`), referencing (`\CrefAndHyperrefIfExist{}`), and highlighting (`\hldef{}`).
