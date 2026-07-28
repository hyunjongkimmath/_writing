# References-Needed Checklist — Final Status

Generated: 2026-07-26
Started with: ~42 `\TODO{AI generated, reference needed}` markers across ~30 files
Remaining: 22 (no vault labels exist for these)
Resolved: 20

---

## Resolved references (replaced TODO with \CrefIfExists or inline explanation)

| # | File | What was needed | Resolution |
|---|------|----------------|------------|
| 1 | `lemma_kernel_cokernel_image_coimage_of_modules_over_rings_are_categorical.tex` | first isomorphism theorem for modules | `\Cref{theorem:first_isomorphism_theorem_for_modules_over_rings}` |
| 2 | `definition_logarithmic_derivative_of_a_holomorphic_function.tex` | order of a zero of holomorphic function | `\CrefIfExists{definition:order_of_a_zero_of_a_holomorphic_function}` |
| 3 | `definition_logarithmic_derivative_of_a_holomorphic_function.tex` | pole of meromorphic function | `\CrefIfExists{definition:isolated_singularity_of_a_holomorphic_function_from_an_open_subset_of_the_complex_plane_to_the_complex_plane_classified_as_removable_pole_or_essential}` |
| 4 | `definition_logarithmic_derivative_of_a_holomorphic_function.tex` | complex derivative of holomorphic function + standalone reference dumps | Removed standalone reference dumps per referencing_spec §11; inline ref already existed |
| 5 | `theorem_witt_decomposition_theorem_for_quadratic_forms_over_fields.tex` | nondegenerate subspace orthogonal complement | `\Cref{proposition:v_decomposes_as_direct_sum_of_subspace_and_its_orthogonal_complement}` |
| 6 | `proposition_witt_cancellation_for_quadratic_forms_over_a_field.tex` (line 25) | same as #5 | Same label |
| 7 | `proposition_witt_cancellation_for_quadratic_forms_over_a_field.tex` (line 30) | symmetric argument — proof guidance, not a reference | Replaced TODO with inline explanation of the reverse argument |
| 8 | `theorem_root_test_for_absolute_convergence_of_series.tex` | limsup of sequence | `\CrefIfExists{definition:limsup_and_liminf_of_a_sequence_in_the_extended_real_line}` |
| 9 | `theorem_root_test_for_absolute_convergence_of_series.tex` | geometric series convergence criterion | `\CrefAndHyperrefIfExist{definition:geometric_progression_and_geometric_series_over_a_commutative_semiring}{geometric series}` + `\Cref{theorem:convergence_of_an_infinite_geometric_series_in_a_topological_ring}` |
| 10 | `proposition_complex_derivative_of_a_branch_of_complex_logarithm_is_reciprocal.tex` | definition of complex logarithm/principal branch | Removed — the proposition itself defines the concept inline as "right inverse of exp" |
| 11 | `definition_modular_form_with_nebentypus.tex` | primitivity for Dirichlet characters | Removed — already references `\CrefAndHyperrefIfExist{definition:primitive_dirichlet_character}` on the same line; TODO was redundant |
| 12 | `theorem_hecke_operators_are_well_defined_linear_operators_on_modular_forms.tex` | Fourier expansion at infinity for modular forms (in commented-out code) | `\CrefIfExists{definition:fourier_expansion_of_a_periodic_holomorphic_function_on_the_upper_half_plane}` |
| 13 | `proposition_eulers_reflection_formula_for_gamma_function.tex` | analytic continuation of meromorphic functions | Replaced with `\CrefAndHyperrefIfExist{definition:meromorphic_continuation_of_a_holomorphic_function_on_an_open_subset_of_the_complex_plane}{meromorphic continuation}` |
| 14 | `proposition_hecke_operators_are_self_adjoint_wrt_petersson_inner_product.tex` | orthonormal basis in inner product space | `\CrefIfExists{definition:orthogonal_and_orthonormal_sets_in_an_inner_product_space}` |
| 15 | `proposition_hecke_operators_are_self_adjoint_wrt_petersson_inner_product.tex` | simultaneous diagonalization of commuting self-adjoint operators | Removed TODO — replaced with inline prose (standard linear algebra result) |
| 16 | `corollary_trivial_zeros_of_dirichlet_L_function.tex` | zeroes and poles of Gamma function | Removed bare `\TODO{reference needed}` — the definition:gamma_function already states the pole locations in its text; no separate label exists for a gamma zero/pole proposition |
| 17 | `definition_gamma_function.tex` | meromorphic continuation of Gamma with functional equation | Replaced TODO with reference to `\CrefIfExists{lemma:mellin_transform_integral_representation_of_gamma_function}` and inline explanation |
| 18 | `corollary_values_of_riemann_zeta_at_even_positive_integers.tex` | Bernoulli numbers explicit values | `\CrefIfExists{definition:bernoulli_numbers}` — the definition already lists B_0..B_8 explicitly |
| 19 | `proposition_commutative_ring_with_absolute_value...tex` (line 20) | only nonnegative square root of 1 is 1 in ordered semiring | Replaced with inline proof sketch: "since in an ordered semiring, if 0 < t < 1_T then t^2 < t < 1_T..." |
| 20 | `proposition_commutative_ring_with_absolute_value...tex` (line 41) | dense at zero property c*delta < eta | Replaced with inline explanation referencing the definition of dense at zero |

---

## Remaining unresolved references (no vault labels exist)

These cannot be resolved without **creating new definitions/theorems** in the vault. The TODOs have been cleaned up for consistent formatting and more precise descriptions, but remain as `\TODO{AI generated, reference needed: ...}`.

| # | File | Missing concept |
|---|------|----------------|
| 1 | `corollary_dirichlet_L_function_at_positive_integers_even_odd_character.tex` | analytic class number formula for Dirichlet L-functions |
| 2 | `corollary_values_of_riemann_zeta_at_even_positive_integers.tex` | proposition: $e^{2\pi i z} - 1 = 2i e^{\pi i z} \sin(\pi z)$ via Euler's formula |
| 3 | `lemma_zorns_lemma_is_equivalent_to_axiom_of_choice_under_ZF.tex` | transfinite recursion theorem |
| 4 | `lemma_zorns_lemma_is_equivalent_to_axiom_of_choice_under_ZF.tex` | Burali-Forti paradox formal statement (ordinals form proper class) |
| 5 | `proposition_adjugate_formula_for_determinant_over_a_commutative_ring.tex` | definition of classical adjugate matrix (transpose of cofactor matrix) |
| 6 | `definition_determinant_of_a_matrix_over_a_ring.tex` | definition of sign of a permutation as (-1)^transpositions |
| 7 | `proposition_eulers_reflection_formula_for_gamma_function.tex` | ML-estimate lemma for contour integrals (integral bounded by max|integrand| times arc length) |
| 8 | `proposition_eulers_reflection_formula_for_gamma_function.tex` | Beta function identity $B(x,y) = \Gamma(x)\Gamma(y)/\Gamma(x+y)$ |
| 9 | `proposition_legendres_duplication_formula_for_gamma_function.tex` | same Beta function identity as #8 |
| 10 | `proposition_legendres_duplication_formula_for_gamma_function.tex` | integral representation of Beta function $B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1} dt$ |
| 11 | `theorem_poisson_summation_formula_for_schwartz_functions_on_real_numbers.tex` | Fourier series convergence theorem for smooth periodic functions |
| 12 | `proposition_value_of_gamma_function_at_one_half.tex` | substitution rule extension to improper integrals on [0,infty) |
| 13 | `proposition_weierstrass_factorization_sine_function.tex` | Weierstrass factorization theorem for entire functions of finite order |
| 14 | `proposition_witt_cancellation_for_quadratic_forms_over_a_field.tex` | orthogonal direct sum of quadratic modules (q_{M⊕N} = q_M + q_N, polarization splits) |
| 15 | `theorem_eisenstein_series_for_SL_2_Z_is_a_modular_form_with_fourier_expansion.tex` | divisor sum function $\sigma_k(n) = \sum_{d|n} d^k$ |
| 16 | `theorem_hecke_operators_are_well_defined_linear_operators_on_modular_forms.tex` | holomorphic at cusps for modular forms (commented-out code) |
| 17 | `proposition_convergence_of_series_implies_cauchy_tails_condition...tex` | order-complete ordered abelian group definition |
| 18 | `definition_logarithmic_derivative_of_a_holomorphic_function.tex` | branch of the complex logarithm (local inverse of exp) |
| 19 | `proposition_reverse_triangle_inequality_in_extended_metric_space.tex` | Grothendieck group construction embedding ordered semiring T into ordered ring R |
| 20 | `proposition_uniform_convergence_of_termwise_derivatives_of_dirichlet_series.tex` | $(\ln n)^k = o(n^\epsilon)$ as $n \to \infty$ for any k >= 0, epsilon > 0 |
| 21 | `definition_polar_coordinates_on_R2.tex` | diffeomorphism between open subsets of $\mathbb{R}^n$ |
| 22 | `proposition_hecke_operators_commute_and_satisfy_recurrence_relations.tex` | Hecke algebra (associative algebra over C generated by T_n on M_k) |

---

## Summary

- **Resolved: 20** — Replaced with `\CrefIfExists{label}` or inline explanation where the concept was already self-evident
- **Unresolved: 22** — No corresponding definitions exist in vault; TODOs properly formatted with precise descriptions for future writing
- **Standalone reference dumps cleaned**: Removed from `definition_logarithmic_derivative_of_a_holomorphic_function.tex` (per referencing_spec §11)
- **Non-standard TODO format fixed**: `definition_polar_coordinates_on_R2.tex` had bare `TODO{...}` without backslash — corrected to `\TODO{AI generated, reference needed: ...}`

### Categories of missing vault definitions (for future writing):
1. **Beta function** (3 references across Euler reflection + Legendre duplication) — most impactful to write first
2. **Set theory foundations** (transfinite recursion, Burali-Forti paradox)
3. **Complex analysis tools** (ML-estimates, branch of log, Weierstrass factorization theorem)
4. **Linear algebra basics** (adjugate matrix, sign of permutation)
5. **Number theory functions** (divisor sum sigma_k(n))
6. **Analysis utilities** (log growth vs polynomial, Fourier series convergence for smooth functions)
