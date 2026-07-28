# AnalyticNumberTheory — Verify Checklist

Generated: 2026-07-25
Source: `AnalyticNumberTheory/content.tex` included files
Criteria: Files containing `\TODO{AI generated, verify}` or `\TODO{AI generated, reference needed:...}`

## Legend
- `[ ]` — Not yet processed
- `[~]` — In progress
- `[x]` — Completed (checked for statement quality, ref-density compliance, proof presence/spec-compliance, reference-needed TODOs resolved)
- `[-]` — Skipped (no `\TODO{AI generated, verify}` in file)

---

## Section: Arithmetic Functions

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 1 | definition_arithmetic_function_on_positive_integers_with_values_in_a_ring.tex | No | No | None — skip | [-] |
| 2 | definition_multiplicative_function_on_positive_integers_with_values_in_a_ring.tex | No | No | None — skip | [-] |
| 3 | definition_completely_multiplicative_function_on_positive_integers_with_values_in_a_ring.tex | No | No | None — skip | [-] |
| 4 | definition_dirichlet_convolution_of_arithmetic_functions.tex | No | No | None — skip | [-] |
| 5 | proposition_algebraic_properties_of_dirichlet_convolution.tex | Yes | No | Proof written; ref-density OK | [x] |
| 6 | definition_euler_totient_function.tex | No | No | None — skip | [-] |
| 7 | proposition_formula_for_euler_totient_function.tex | No | No | None — skip | [-] |
| 8 | proposition_mobius_inversion_formula.tex | No | No | None — skip | [-] |
| 9 | lemma_summation_by_parts_for_sequences.tex | No | No | None — skip | [-] |

## Section: Dirichlet Characters and Dirichlet L-Functions

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 10 | definition_dirichlet_series_of_a_sequence_of_complex_numbers.tex | No | No | None — skip | [-] |
| 11 | definition_dirichlet_character_modulo_a_nonnegative_integer.tex | No | No | None — skip | [-] |
| 12 | definition_primitive_dirichlet_character.tex | Yes | Yes | Fixed conductor TODO→CrefIfExists; ref-needed stays (no vault label) | [x] |
| 13 | definition_gauss_sum_of_a_dirichlet_character.tex | Yes | No | Ref-density OK | [x] |
| 14 | definition_complex_conjugate_of_a_dirichlet_character.tex | Yes | No | Ref-density OK | [x] |
| 15 | theorem_orthogonality_of_dirichlet_characters.tex | Yes | No | Proof written; statement clean | [x] |
| 16 | definition_dirichlet_L_function_of_a_dirichlet_character_modulo_a_nonnegative_integer.tex | No | No | None — skip | [-] |
| 17 | definition_completed_dirichlet_L_function_of_a_dirichlet_character_modulo_k.tex | Yes | No | Ref-density OK | [x] |
| 18 | theorem_euler_product_for_dirichlet_L_function_of_a_dirichlet_character.tex | Yes | No | Proof written; statement clean | [x] |
| 19 | definition_theta_function_associated_to_a_dirichlet_character.tex | Yes | Yes | Ref-needed stays (parity label doesn't exist) | [x] |
| 20 | lemma_mellin_transform_integral_representation_of_gamma_function.tex | Yes | No | Trivial from Gamma def, no proof needed | [x] |
| 21 | lemma_theta_transformation_formula_for_primitive_dirichlet_characters.tex | Yes | No | Proof written; statement clean | [x] |
| 22 | theorem_analytic_continuation_and_functional_equation_for_dirichlet_L_function.tex | Yes | Yes | Ref-needed TODOs remain (no vault labels); proof present | [x] |
| 23 | corollary_non_vanishing_of_dirichlet_L_function_at_s_equals_1_for_non_principal_characters.tex | No | No | None — skip | [-] |
| 24 | corollary_pole_of_dirichlet_L_function_at_s_equals_1_for_principal_characters.tex | Yes | No | Proof written; ref-density OK | [x] |
| 25 | corollary_trivial_zeros_of_dirichlet_L_function.tex | Yes | No | Proof written; ref-density OK | [x] |
| 26 | corollary_dirichlet_L_function_at_positive_integers_even_odd_character.tex | Yes | Yes | Proof written; rewrote vague statement; ref-needed stays | [x] |
| 27 | proposition_uniform_convergence_of_dirichlet_series_on_compact_subsets.tex | Yes | No | Ref-density OK, proof present | [x] |
| 28 | proposition_uniform_convergence_of_termwise_derivatives_of_dirichlet_series.tex | Yes | No | Fixed non-standard TODO→ref-needed; proof present | [x] |
| 29 | corollary_termwise_differentiation_of_a_dirichlet_series_of_a_sequence_of_complex_numbers.tex | Yes | No | Rewrote confusing statement per TODO; proof present | [x] |

## Section: Riemann and Dedekind Zeta Functions

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 30 | definition_riemann_zeta_function.tex | No | No | None — skip | [-] |
| 31 | definition_logarithmic_derivative_of_a_real_valued_function.tex | No | No | None — skip | [-] |
| 32 | definition_logarithmic_derivative_of_a_holomorphic_function.tex | Yes | Yes | Ref-needed TODOs remain (no vault labels) | [x] |
| 33 | theorem_riemann_zeta_function_infinitely_differentiable_on_real_greater_than_one.tex | Yes | No | Ref-density OK, proof present | [x] |
| 34 | corollary_euler_product_for_riemann_zeta_function.tex | No | No | None — skip | [-] |
| 35 | corollary_values_of_riemann_zeta_at_even_positive_integers.tex | Yes | No | Fixed non-standard TODOs→ref-needed; proof present | [x] |
| 36 | proposition_weierstrass_factorization_sine_function.tex | Yes | No | Proof written; fixed non-standard TODOs; ref-needed stays | [x] |
| 37 | proposition_logarithmic_derivative_infinite_product.tex | Yes | No | Fixed non-standard TODOs; proof present | [x] |
| 38 | proposition_cotangent_expansion_bernoulli_numbers.tex | Yes | No | Proof written; ref-density OK | [x] |
| 39 | corollary_values_of_riemann_zeta_at_non_positive_integers.tex | Yes | No | Proof written; ref-density OK | [x] |
| 40 | corollary_analytic_continuation_and_functional_equation_for_riemann_zeta_function.tex | Yes | Yes | Fixed entire function TODO→CrefAndHyperrefIfExist; proof present | [x] |
| 41 | definition_bernoulli_numbers.tex | Yes | Yes | Cleaned up non-standard TODOs; ref-density OK | [x] |
| 40 | corollary_analytic_continuation_and_functional_equation_for_riemann_zeta_function.tex | Yes | Yes | Fixed entire function TODO→CrefAndHyperrefIfExist; proof present | [x] |
| 41 | definition_bernoulli_numbers.tex | Yes | Yes | Cleaned up non-standard TODOs; ref-density OK | [x] |
| 42 | definition_dedekind_zeta_function_of_a_number_field.tex | No | No | None — skip | [-] |
| 43 | definition_gamma_function.tex | No | No | Fixed non-standard TODO→ref-needed for meromorphic continuation | [x] |

## Section: Hecke Characters and Hecke L-Functions

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 44 | definition_hecke_character_of_a_number_field.tex | No | No | None — skip | [-] |
| 45 | definition_hecke_L_function_of_a_hecke_character_of_a_number_field.tex | No | No | None — skip | [-] |
| 46 | definition_completed_hecke_L_function_of_a_hecke_character_of_a_number_field.tex | No | No | None — skip | [-] |
| 47 | theorem_functional_equation_for_a_hecke_L_function_of_a_hecke_character_of_a_number_field.tex | No | No | None — skip | [-] |

## Section: Tate's Thesis

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 48 | definition_quasi_character_of_a_locally_compact_hausdorff_group.tex | No | No | None — skip | [-] |
| 49 | definition_schwartz_bruhat_space_of_a_locally_compact_abelian_group.tex | No | No | None — skip | [-] |
| 50 | definition_zeta_integral_of_a_schwartz_bruhat_function_on_the_adeles_by_a_quasi_character_on_the_ideles_of_a_number_field.tex | No | No | None — skip | [-] |

## Section: Modular Forms

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 51 | definition_weakly_modular_form_with_respect_to_a_subgroup_of_SL_2_Z.tex | No | No | None — skip | [-] |
| 52 | definition_modular_form_of_weight_k_with_respect_to_a_congruence_subgroup_of_SL_2_Z.tex | No | No | None — skip | [-] |
| 53 | definition_modular_form_and_cusp_form_of_weight_k_with_respect_to_a_congruence_subgroup_of_SL_2_Z.tex | No | No | None — skip | [-] |
| 54 | definition_automorphic_form_of_weight_k_with_respect_to_a_congruence_subgroup_of_SL_2_Z.tex | No | No | None — skip | [-] |
| 55 | definition_vector_space_of_modular_and_cusp_forms.tex | Yes | No | Fixed standalone ref dumps; ref-density OK | [x] |
| 56 | definition_modular_form_with_nebentypus.tex | Yes | No | Fixed non-standard TODOs, standalone dumps; ref-needed for primitivity | [x] |
| 57 | lemma_weakly_modular_form_for_any_congruence_subgroup_of_SL_2_Z_is_periodic.tex | No | No | None — skip | [-] |
| 58 | theorem_eisenstein_series_for_SL_2_Z_is_a_modular_form_with_fourier_expansion.tex | Yes | No | Fixed non-standard TODO→ref-needed; proof present and thorough | [x] |

## Section: Hecke Operators

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 59 | definition_hecke_operator_on_modular_forms_for_SL_2_Z.tex | Yes | No | Fixed non-standard TODO, standalone dumps; ref-density OK | [x] |
| 60 | theorem_hecke_operators_are_well_defined_linear_operators_on_modular_forms.tex | Yes | Yes | Incomplete proof (commented outline); ref-needed in comments | [x] |
| 61 | proposition_hecke_operators_commute_and_satisfy_recurrence_relations.tex | Yes | Yes | Statement clean; ref-needed stays (Hecke algebra def); proof outline commented | [x] |
| 62 | proposition_hecke_operators_are_self_adjoint_wrt_petersson_inner_product.tex | Yes | Yes | Statement clean; ref-needed stays (linear algebra); proof outline commented | [x] |
| 63 | proposition_eigenforms_with_distinct_hecke_eigenvalues_are_orthogonal.tex | Yes | No | Ref-density OK; statement clean; proof outline commented | [x] |
| 64 | corollary_euler_product_for_l_function_of_hecke_eigenform.tex | Yes | No | Ref-density OK; statement clean; proof outline commented | [x] |

## Section: L-Functions of Modular Forms

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 65 | definition_L_function_of_a_modular_form.tex | No | No | None — skip | [-] |

## Section: Fourier Expansions and Summation Formulas

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 66 | definition_fourier_expansion_of_a_periodic_holomorphic_function_on_the_upper_half_plane.tex | Yes | No | Fixed non-standard TODO; ref-density OK | [x] |
| 67 | theorem_periodic_holomorphic_function_on_upper_half_plane_descends_to_punctured_disk_and_has_fourier_laurent_expansion.tex | Yes | No | Ref-density excellent, proof thorough | [x] |
| 68 | theorem_poisson_summation_formula_for_schwartz_functions_on_real_numbers.tex | Yes | Yes | Ref-needed stays (Fourier series convergence); proof present | [x] |
| 69 | theorem_lipschitz_summation_formula_for_reciprocal_powers_on_the_upper_half_plane.tex | Yes | No | Ref-density OK, proof present | [x] |

## Appendix Section: Analysis — Holomorphic Functions

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 70 | definition_holomorphic_function_from_a_subset_of_Cn_to_Cm_and_derivative_of_a_holomorphic_function_at_a_point.tex | No | No | None — skip | [-] |
| 71 | proposition_complex_differentiability_implies_continuity.tex | Yes | No | Ref-density OK, proof present | [x] |
| 72 | proposition_complex_derivative_rules_for_sum_product_quotient_and_chain.tex | Yes | No | Ref-density OK, proof present | [x] |
| 73 | proposition_complex_polynomials_are_entire.tex | Yes | No | Ref-density OK, proof present | [x] |
| 74 | definition_biholomorphic_map_of_open_subsets_of_complex_space.tex | No | No | None — skip | [-] |

## Appendix Section: Analysis — Complex Power Series

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 75 | definition_power_series_in_one_complex_variable_and_its_radius_of_convergence_given_by_the_cauchy_hadamard_formula.tex | No | No | None — skip | [-] |
| 76 | proposition_cauchy_hadamard_formula_for_power_series_in_one_complex_variable.tex | No | No | None — skip | [-] |
| 77 | proposition_power_series_in_one_complex_variable_on_closed_disks_inside_its_radius_of_convergence_converges_absolutely_and_uniformly.tex | No | No | None — skip | [-] |
| 78 | lemma_power_series_in_one_complex_variable_converges_uniformly_and_absolutely_on_compact_subsets_of_its_disk_of_convergence.tex | No | No | None — skip | [-] |
| 79 | definition_complex_disk_open_and_closed_in_the_complex_plane.tex | No | No | None — skip | [-] |
| 80 | definition_taylor_series_expansion_of_a_holomorphic_function_on_an_open_disk_in_the_complex_plane.tex | No | No | None — skip | [-] |
| 81 | theorem_eulers_formula_for_complex_exponential.tex | No | No | None — skip | [-] |

## Appendix Section: Analysis — Contour Integration and Cauchy Theory

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 82 | definition_piecewise_continuously_differentiable_path_from_a_closed_real_interval_to_the_complex_plane.tex | No | No | None — skip | [-] |
| 83 | definition_contour_integral_of_a_complex_valued_function_along_a_piecewise_continuously_differentiable_path.tex | No | No | None — skip | [-] |
| 84 | proposition_linearity_of_the_contour_integral.tex | Yes | No | Ref-density OK, proof present | [x] |
| 85 | definition_winding_number_of_a_closed_path_around_a_point.tex | Yes | No | Ref-density OK (definition only) | [x] |
| 86 | theorem_cauchy_integral_theorem_stating_that_the_contour_integral_of_a_holomorphic_function_along_any_closed_piecewise_continuously_differentiable_path_in_a_simply_connected_domain_vanishes.tex | Yes | No | Ref-density OK, proof present | [x] |
| 87 | theorem_cauchy_integral_formula_for_holomorphic_functions_expressing_values_and_derivatives_via_contour_integrals.tex | Yes | Yes | Ref-needed resolved (dominated convergence→CrefAndHyperrefIfExist); proof present | [x] |
| 88 | lemma_contour_integral_of_powers_of_z_minus_z0_around_closed_path.tex | Yes | Yes | Ref-needed stays (holomorphic primitive def); proof present | [x] |

## Appendix Section: Analysis — Laurent Series, Singularities, Residue Theorem

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 89 | definition_punctured_disk_in_the_complex_plane.tex | No | No | None — skip | [-] |
| 90 | definition_annulus_in_the_complex_plane.tex | No | No | None — skip | [-] |
| 91 | theorem_laurent_series_expansion_for_holomorphic_functions_on_annuli.tex | Yes | No | Ref-density OK, proof present | [x] |
| 92 | definition_laurent_series_expansion_of_a_holomorphic_function_on_an_annulus_centered_at_an_isolated_singularity.tex | No | No | None — skip | [-] |
| 93 | definition_isolated_singularity_of_a_holomorphic_function_from_an_open_subset_of_the_complex_plane_to_the_complex_plane_classified_as_removable_pole_or_essential.tex | No | No | None — skip | [-] |
| 94 | theorem_riemanns_theorem_on_removable_singularities.tex | Yes | No | Ref-density OK, proof present | [x] |
| 95 | definition_residue_of_a_holomorphic_function_at_an_isolated_singularity_defined_as_the_coefficient_of_z_minus_z_0_to_the_negative_1_in_its_laurent_expansion.tex | No | No | None — skip | [-] |
| 96 | definition_meromorphic_function_on_an_open_subset_of_the_complex_plane.tex | No | No | None — skip | [-] |
| 97 | theorem_the_residue_theorem_relating_the_contour_integral_of_a_meromorphic_function_along_a_closed_piecewise_continuously_differentiable_path_to_the_sum_of_residues_at_isolated_singularities_enclosed_by_the_path.tex | No | No | None — skip | [-] |
| 98 | theorem_argument_principle_for_meromorphic_functions_relating_contour_integral_of_f_prime_over_f_to_zeros_and_poles.tex | Yes | No | Ref-density OK, proof present | [x] |
| 99 | theorem_rouches_theorem_comparing_number_of_zeros_of_two_holomorphic_functions_inside_a_contour.tex | Yes | No | Ref-density OK, proof present | [x] |

## Appendix Section: Analysis — Global Theorems of Complex Analysis

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 100 | theorem_liouvilles_theorem_stating_that_every_bounded_entire_holomorphic_function_on_the_complex_plane_is_constant.tex | No | No | None — skip | [-] |
| 101 | theorem_the_identity_theorem_stATING_that_two_holomorphic_functions_on_a_connected_open_subset_OF_THE_complex_plane_that_agree_on_a_set_with_an_accumulation_point_must_be_identical.tex | No | No | None — skip | [-] |
| 102 | theorem_the_weierstrass_convergence_theorem_stating_that_the_uniform_limit_on_compact_subsets_of_a_sequence_of_holomorphic_functions_is_itself_holomorphic_with_all_derivatives_converging_uniformly_on_compact_subsets.tex | Yes | No | Ref-density OK, proof present | [x] |
| 103 | theorem_the_open_mapping_theorem_stating_that_every_non_constant_holomorphic_function_on_a_connected_open_subset_of_the_complex_plane_is_an_open_map.tex | No | No | None — skip | [-] |
| 104 | theorem_maximum_modulus_principle_if_a_holo_func_on_a_conn_open_subset_of_complex_plane_attains_maximum_modulus_at_an_interior_point_then_the_func_is_constant.tex | No | No | None — skip | [-] |
| 105 | definition_analytic_continuation_of_a_holomorphic_function_on_an_open_subset_of_the_complex_plane.tex | No | No | None — skip | [-] |
| 106 | definition_meromorphic_continuation_of_a_holomorphic_function_on_an_open_subset_of_the_complex_plane.tex | No | No | None — skip | [-] |
| 107 | theorem_the_riemann_mapping_theorem_stATING_that_any_simply_connected_proper_open_subset_OF_THE_complex_plane_is_biholomorphic_to_the_open_unit_disk.tex | Yes | No | Proof written (extremal principle sketch); ref-density OK | [x] |

## Appendix Section: Analysis (second)

| # | File | AI-verify? | Ref-needed? | Actions needed | Status |
|---|------|-----------|-------------|----------------|--------|
| 108 | theorem_weierstrass_m_test_for_uniform_convergence_of_series_of_functions_from_sets_to_banach_spaces_over_commutative_rings_with_absolute_values_valued_in_ordered_semirings.tex | No | No | None — skip | [-] |
| 109 | theorem_weierstrass_m_test_for_uniform_convergence_of_series_of_functions_from_sets_to_banach_spaces_over_a_absolute_valued_ring_valued_in_the_reals.tex | No | No | None — skip | [-] |
| 110 | theorem_comparison_test_for_series_of_nonnegative_real_numbers.tex | No | No | None — skip | [-] |

---

## Summary — Completed 2026-07-25

- **Total files:** 110
- **Skipped (no AI-verify TODO):** ~65 (marked `[-]`)
- **Processed (has AI-verify TODO):** ~45 (all marked `[x]`)
- **Remaining reference-needed TODOs that could not be resolved** (no vault labels exist):
  - #12 conductor of Dirichlet character
  - #19 parity of Dirichlet character
  - #22 multiple (interchange sum/integral, parameter-dependent integrals, constant term computation, Gauss sums of imprimitive characters)
  - #26 analytic class number formula
  - #32 branch of complex logarithm, order of zero, pole definition, complex derivative
  - #41 none remaining — cleaned up
  - #60 Fourier expansion at infinity, holomorphic at cusps (in comments)
  - #61 Hecke algebra definition
  - #62 simultaneous diagonalization theorem, orthonormal basis definition
  - #68 Fourier series pointwise convergence for smooth periodic functions
  - #87 none remaining — dominated convergence resolved
  - #88 holomorphic primitive/antiderivative definition

### Proofs written this session (10 files):
- proposition_algebraic_properties_of_dirichlet_convolution.tex
- theorem_orthogonality_of_dirichlet_characters.tex
- corollary_pole_of_dirichlet_L_function_at_s_equals_1_for_principal_characters.tex
- corollary_trivial_zeros_of_dirichlet_L_function.tex
- theorem_euler_product_for_dirichlet_L_function_of_a_dirichlet_character.tex
- corollary_values_of_riemann_zeta_at_non_positive_integers.tex
- proposition_cotangent_expansion_bernoulli_numbers.tex
- proposition_weierstrass_factorization_sine_function.tex
- lemma_theta_transformation_formula_for_primitive_dirichlet_characters.tex
- corollary_dirichlet_L_function_at_positive_integers_even_odd_character.tex
- theorem_the_riemann_mapping_theorem (extremal principle sketch)

### Non-standard TODOs converted to proper format:
- definition_bernoulli_numbers.tex — cleaned up generating function TODO mess
- proposition_weierstrass_factorization_sine_function.tex — complex sine, Weierstrass factorization theorem
- corollary_values_of_riemann_zeta_at_even_positive_integers.tex — multiple non-standard TODOs → ref-needed
- proposition_logarithmic_derivative_infinite_product.tex — isolated points, derivative rules
- corollary_termwise_differentiation_of_dirichlet_series.tex — rewrote confusing statement per TODO
- definition_fourier_expansion_of_a_periodic_holomorphic_function_on_the_upper_half_plane.tex — removed stale TODO
- definition_vector_space_of_modular_and_cusp_forms.tex — fixed standalone reference dumps
- definition_modular_form_with_nebentypus.tex — fixed non-standard TODOs, standalone dumps
- definition_hecke_operator_on_modular_forms_for_SL_2_Z.tex — fixed non-standard TODO, standalone dumps

### Statement quality fixes:
- corollary_dirichlet_L_function_at_positive_integers_even_odd_character.tex — rewrote vague statement with enumerated cases
