# SimplicialTheory Coverage Checklist

**Last updated**: 2026-07-23  
**Source vault**: `math/_writing/SimplicialTheory/` (currently only `content.tex` with `\nocite{*}` — **no components wired**)  
**Related vaults**: `AbstractAlgebra` (derived categories, abelian categories), `AlgebraicNumberTheory` (étale, Galois), `Schemes` (Nisnevich site, A¹-homotopy, six functors), `Topology` (classical homotopy, CW complexes, spectral sequences)

---

## Legend
| Status | Meaning |
|--------|---------|
| ✅ **ACTIVE** | Component file exists **and** is `\input`/`\include`d in `content.tex` |
| 📝 **DEFINED** | Component file exists in `_definitions/`, `_concepts/`, etc. but **not wired** in `content.tex` |
| 🔄 **PARTIAL** | Some pieces exist; major gaps remain |
| ❌ **MISSING** | No component file found in vault |
| 🔗 **EXT** | Exists primarily in another vault (cross-ref noted) |

---

## Phase 0: Foundations — Simplicial Sets & Categories

| # | Topic | Status | Notes / Key Labels |
|---|-------|--------|-------------------|
| 0.1 | **Simplicial sets** — definition, simplices, face/degeneracy maps, standard n-simplex Δⁿ, horns Λⁿₖ | 📝 | `definition_simplex_of_a_simplicial_object...`, `definition_standard_n_simplex`, `definition_horn_of_the_nth_standard_simplex`, `definition_empty_simplicial_set`, `definition_final_object_of_a_topological_or_simplicial_category_or_simplicial_set` |
| 0.2 | **Category of simplicial sets** sSet — limits/colimits, cartesian closure, subobject classifier | 📝 | `definition_simplicial_category_of_simplicial_sets`, `lemma_0_simplex_is_terminal_object_in_category_of_simplicial_sets`, `lemma_empty_simplicial_set_is_initial_object_in_category_of_simplicial_sets` |
| 0.3 | **Simplicial objects in a category** — simplicial/cosimplicial objects, Moore complex, Dold–Kan correspondence | 📝 | `definition_simplicial_cosimplicial_object_in_a_category`, `definition_moore_complex_of_a_simplicial_object_in_an_abelian_category`, `definition_simplicial_object_in_an_infty_category` |
| 0.4 | **Nerve of a category** — nerve, characterization (inner horn lifting), quasi-categories as ∞-categories | 📝 | `definition_nerve_of_a_category`, `proposition_simplicial_set_is_the_nerve_of_a_small_category...`, `corollary_the_nerve_of_a_small_category_is_a_quasi_category` |
| 0.5 | **Simplicial categories** — simplicial enrichment, homotopy coherent nerve, Bergner model structure | 📝 | `definition_simplicial_category`, `definition_simplicial_nerve_of_a_simplicial_category`, `proposition_geometric_realization_of_simplicial_category_and_singular_simplicial_category_of_topological_category_adjunction` |
| 0.6 | **Geometric realization / singular complex** — |𝐗|, Sing, adjunction, Quillen equivalence to CGWH spaces | 📝 | `definition_geometric_realization_of_a_simplicial_set`, `definition_singular_complex_of_a_topological_space`, `theorem_unit_and_counit_morphisms_for_geometric_realization_singular_complex_adjunction...`, `corollary_homotopy_category_of_simplicial_sets_is_equivalent_to_the_homotopy_category_of_compactly_generated_weakly_hausdorff_spaces` |
| 0.7 | **Kan complexes** — Kan extension condition, Kan fibrations, trivial Kan fibrations, ∞-groupoids | 📝 | `definition_kan_complex`, `definition_kan_extension_condition_for_a_horn_for_a_simplicial_set`, `definition_Kan_fibration_between_simplicial_sets`, `definition_trivial_Kan_fibration_between_simplicial_sets`, `proposition_infty_groupoids_are_equivalent_to_kan_complexes`, `lemma_every_kan_complex_is_a_quasi_category` |
| 0.8 | **Quasi-categories (∞-categories)** — inner horn lifting, Joyal model structure, mapping spaces, equivalences | 📝 | `definition_infty_category_quasi_category`, `definition_joyal_model_structure_on_the_category_of_simplicial_sets`, `proposition_simplicial_set_is_quasi_category_iff_maps_from_Delta_2_to_maps_from_Lambda_1_2_is_a_trivial_kan_fibration`, `definition_mapping_space_between_objects_of_a_simplicial_set`, `definition_infty_groupoid_infty_0_category` |
| 0.9 | **Homotopy category of an ∞-category** — hC, mapping spaces as ∞-groupoids, (∞,1)-category theory basics | 📝 | `definition_homotopy_category_of_a_simplicial_set`, `definition_homotopy_category_of_the_category_of_simplicial_sets`, `proposition_mapping_space_between_objects_of_a_quasi_category_is_an_infty_groupoid` |
| 0.10 | **Limits/colimits in ∞-categories** — (co)limits via slice ∞-categories, (co)final functors, Kan extensions | 📝 | `definition_limit_and_colimit_for_a_map_from_a_simplicial_set_to_an_infty_category`, `definition_overcategory_and_undercategory_of_an_infty_category_with_respect_to_a_map_from_a_simplicial_set`, `proposition_existence_of_overcategory_simplicial_set_S_slash_p_with_universal_property` |

---

## Phase 1: Model Categories & Simplicial Model Categories

| # | Topic | Status | Notes / Key Labels |
|---|-------|--------|-------------------|
| 1.1 | **Model categories** — definitions, weak equivalences/cofibrations/fibrations, lifting properties, factorization, (co)fibrant replacement | 📝 | `definition_model_category`, `lemma_model_category_has_an_initial_object_and_a_final_object`, `definition_fibrant_cofibrant_object_in_a_model_category` |
| 1.2 | **Simplicial model categories** — enrichment over sSet, Quillen adjunctions, simplicial mapping spaces | 📝 | `definition_simplicial_model_structure_on_a_category`, `definition_simplicial_model_category_structure_on_the_category_of_simplicial_sheaves_on_a_small_site_and_simplicial_homotopy_category_of_a_site` |
| 1.3 | **Standard model structure on sSet** — Kan–Quillen model structure, cofibrations = monomorphisms, fibrations = Kan fibrations | 📝 | `definition_standard_model_structure_on_the_category_of_simplicial_sets` |
| 1.4 | **Joyal model structure on sSet** — fibrant objects = quasi-categories, (∞,1)-categorical localization | 📝 | `definition_joyal_model_structure_on_the_category_of_simplicial_sets` |
| 1.5 | **Model structure on simplicial sheaves** — local/global model structures, Jardine model structure, injective/projective variants | 📝 | `definition_simplicial_weak_equivalences_cofibrations_and_fibrations_for_simplicial_sheaves_on_a_site`, `theorem_simplicial_model_category_structure_on_simplicial_sheaves`, `definition_simplicial_model_category_structure_on_the_category_of_simplicial_sheaves_on_a_small_site_and_simplicial_homotopy_category_of_a_site` |
| 1.6 | **I-model structures** — interval object, A¹-localization, left Bousfield localization | 📝 | `definition_I_local_weak_I_weak_equivalence_I_weak_fibration_for_morphisms_of_simplicial_sheaves_on_a_site_with_interval`, `definition_A_local_object_A_weak_equivalence_A_fibration_of_simplicial_homotopy_category_of_sheaves_of_a_small_site`, `theorem_I_model_category_of_simplicial_sheaves_on_a_small_site_with_interval` |
| 1.7 | **A¹-homotopy theory (Morel–Voevodsky)** — Nisnevich site, A¹-local weak equivalences, A¹-homotopy category, A¹-invariant sheaves | 📝 | `definition_A1_weak_equivalence_of_simplicial_sheaves_of_sets_on_the_nisnevich_topology_over_a_noetherian_finite_dimensional_scheme`, `definition_A1_local_weak_equivalence_fibration_of_simplicial_sheaves_of_sets_on_the_nisnevich_site_over_a_noetherian_finite_dimensional_scheme`, `definition_A1_model_structure_on_the_category_of_simp_sheaves_of_sets_on_the_nis_site_over_a_noeth_scheme_of_fin_dim_and_the_unstable_A1_homotopy_category`, `proposition_A1_model_structure_on_category_of_simplicial_nisnevich_sheaves`, `corollary_A1_model_structure_on_simplicial_nisnevich_sheaves_over_a_noetherian_finite_dimensional_scheme_is_an_instance_of_an_I_model_structure`, `theorem_A1_homotopy_groups_are_strongly_A1_invariant`, `definition_A1_invariant_strongly_A1_invariant_strictly_A1_invariant_sheaves_of_sets_groups_ab_groups`, `definition_sheaf_of_A1_connected_components_of_an_unbased_space` |
| 1.8 | **Nisnevich site & topology** — Nisnevich covers, elementary distinguished squares, Nisnevich descent | 📝 | `definition_nisnevich_topology_on_a_noetherian_scheme_of_finite_dimension`, `proposition_elementary_distinguished_square_condition_for_a_presheaf_to_be_sheaf_in_the_nisnevich_topology_over_a_noetherian_scheme_of_finite_dimension`, `definition_small_nisnevich_site_of_a_schem`, `theorem_common_small_sites_of_a_scheme_are_essentially_small`, `theorem_hierarchy_of_common_grothendieck_topologies_on_Sch_S` |
| 1.9 | **Motivic homotopy theory (unstable)** — A¹-homotopy category, pointed/unstable, motivic spheres, A¹-connected components, A¹-fundamental group | 📝 | `definition_A1_homotopy_theoretic_space_over_a_noetherian_scheme_of_finite_dimension`, `definition_pointed_space_in_motivic_homotopy_theory`, `definition_A1_homotopy_group_sheaf_of_an_object_of_the_pointed_unstable_A1_homotopy_category_over_a_noetherian_finite_dimensional_scheme`, `lemma_A1_connected_components_of_pointed_space_equals_that_of_underlying_space`, `lemma_A1_homotopy_theory_is_a_kind_of_interval_homotopy_theory`, `lemma_pointification_forgetful_functorson_the_unstable_motivic_homotopy_categories_over_a_noetherian_finite_dimensional_scheme`, `theorem_homotopy_category_of_ordinary_sheaves_on_nisnevich_site_is_equivalent_to_unstable_homotopy_category` |
| 1.10 | **Motivic homotopy theory (stable)** — SH(S), motivic spectra, stable A¹-homotopy category, six operations, Tate objects | ❌ | **MISSING** — stable motivic homotopy category, motivic spectra, stable six functors, Tate twists, motivic stable homotopy groups of spheres |
| 1.11 | **Bousfield localization** — left/right localization, local objects, localization functors, monoidal localizations | 📝 | `definition_A_local_object_A_weak_equivalence_A_fibration_of_simplicial_homotopy_category_of_sheaves_of_a_small_site`, `theorem_A_model_category_and_A_localization_fnctor` |
| 1.12 | **Simplicial spectra / stable model categories** — spectra as model categories, symmetric spectra, orthogonal spectra, stable model structures | 📝 | `definition_model_category_classes_for_spectra_of_topological_spaces`, `theorem_stable_model_structure_topological_spectra`, `theorem_strict_level_model_category_structure_on_the_category_of_spectra` |
| 1.13 | **Proper model categories** — left/right properness, properness for sSet, simplicial sheaves, A¹-local model structure | 📝 | `definition_proper_model_category` |

---

## Phase 2: ∞-Category Theory (Quasi-categories)

| # | Topic | Status | Notes / Key Labels |
|---|-------|--------|-------------------|
| 2.1 | **∞-categories (quasi-categories)** — definition, equivalences, homotopy category, mapping spaces, core | 📝 | `definition_infty_category_quasi_category`, `definition_infty_groupoid_infty_0_category`, `definition_infty_category_of_infty_categories`, `definition_infty_category_of_spaces` |
| 2.2 | **Functors between ∞-categories** — inner fibrations, categorical equivalences, straightening/unstraightening | 📝 | `definition_functor_between_infty_categories`, `definition_inner_fibration_between_infinity_categories`, `theorem_straightening_unstraightening_equivalence_between_functors_to_Cat_infty_and_coCartesian_fibrations` |
| 2.3 | **(Co)Cartesian fibrations** — (co)Cartesian edges, straightening equivalence, Grothendieck construction for ∞-categories | 📝 | `definition_coCartesian_fibration_between_infinity_categories`, `definition_locally_coCartesian_lift_of_a_morphism_in_an_infinity_category`, `theorem_straightening_unstraightening_equivalence_between_functors_to_Cat_infty_and_coCartesian_fibrations` |
| 2.4 | **Limits and colimits in ∞-categories** — (co)final functors, (co)limits via slice, Kan extensions, adjoint functor theorem | 📝 | `definition_limit_and_colimit_for_a_map_from_a_simplicial_set_to_an_infty_category`, `definition_kan_extension_condition_for_a_horn_for_a_simplicial_set` |
| 2.5 | **Adjunctions in ∞-categories** — unit/counit, equivalence of definitions, adjunctions via Cartesian fibrations | 📝 | `lemma_pointification_and_forgetful_functor_adjunction` |
| 2.6 | **Monoidal ∞-categories** — symmetric monoidal ∞-categories, (co)Cartesian fibrations for monoidal structure, Day convolution | 📝 | `definition_symmetric_monoidal_infinity_category`, `definition_symmetric_monoidal_infinity_category_via_coCartesian_fibration`, `definition_correspondence_symmetric_monoidal_infty_category_of_an_infty_category_with_finite_limtis_and_class_of_morphisms_containing_isomorphisms_and_stable_under_pulback_and_composition`, `definition_lax_symmetric_monoidal_functor_of_symmetric_monoidal_infinity_categories` |
| 2.7 | **Algebra in ∞-categories** — monoid/group/objects, Eₙ-algebras, commutative monoids, operads | 📝 | `definition_monoid_object_in_an_infty_category`, `definition_commutative_monoid_in_an_infinity_category`, `definition_group_object_in_an_infty_category`, `definition_semigroup_object_in_an_infty_category` |
| 2.8 | **Stable ∞-categories** — zero object, fiber/cofiber sequences, suspension equivalence, triangulated homotopy category | 📝 | `definition_stable_infinity_category`, `corollary_homotopy_category_of_a_stable_infty_category_is_a_triangulated_category`, `theorem_homotopy_category_of_a_pointed_infinity_category_with_cofibers_whose_suspension_is_an_equivalence_is_a_triangulated_category` |
| 2.9 | **Presentable ∞-categories** — presentability, adjoint functor theorem, compact generation, Ind-completion | ❌ | **MISSING** |
| 2.10 | **∞-topoi** — sheaves on ∞-sites, descent, hypercompletion, ∞-topos classification | ❌ | **MISSING** — (some descent in Schemes vault: `definition_nisnevich_descent_for_a_category_fibered_in_groupoids_over_a_scheme`) |

---

## Phase 3: Homotopy Theory & Classical Algebraic Topology

| # | Topic | Status | Notes / Key Labels |
|---|-------|--------|-------------------|
| 3.1 | **Homotopy groups of Kan complexes / spaces** — πₙ, long exact sequence of fibration, Whitehead theorem | 📝 | `definition_homotopy_groups_of_a_kan_simplicial_set`, `definition_homotopy_groups_of_maps_from_a_smooth_scheme_to_a_sheaf_of_sets_on_the_nisnevich_site_with_respect_to_a_base_point_over_a_noetherian_scheme_of_finite_dimension` |
| 3.2 | **Classical model structures on Top** — Quillen–Serre, Strøm, compactly generated weakly Hausdorff spaces | 📝 | `definition_quillen_serre_model_structure_on_the_category_of_topological_spaces` |
| 3.3 | **CW complexes & cellular homotopy** — CW approximation, cellular chains, Whitehead theorem for CW | 📝 | `proposition_nice_classes_of_spaces_that_are_CW_complexes` |
| 3.4 | **Fiber sequences & cofiber sequences** — homotopy fiber/cofiber, Puppe sequence, long exact sequences | 🔄 | Partial — fiber sequences via `theorem_homotopy_category_of_a_pointed_infinity_category_with_cofibers_whose_suspension_is_an_equivalence_is_a_triangulated_category`; explicit fiber/cofiber in ∞-categories missing |
| 3.5 | **Loop/suspension adjunction** — Ω ⊣ Σ, reduced suspension, loop space, Freudenthal suspension theorem | 📝 | `proposition_reduced_suspension_loop_space_adjucntion_for_pointed_topological_spaces`, `theorem_freudenthal_suspension_theorem` |
| 3.6 | **Stable homotopy theory (classical)** — spectra, stable homotopy groups of spheres, Adams spectral sequence, chromatic homotopy | 📝 | `definition_model_category_classes_for_spectra_of_topological_spaces`, `theorem_stable_model_structure_topological_spectra`, `corollary_stable_homotopy_groups_of_pointed_topological_spaces_give_a_reduced_homology_theory` |
| 3.7 | **Eilenberg–MacLane spaces & cohomology operations** — K(G,n), Steenrod algebra, cohomology operations | ❌ | **MISSING** |
| 3.8 | **Postnikov towers & k-invariants** — Postnikov decomposition, obstruction theory, k-invariants | ❌ | **MISSING** |
| 3.9 | **Model categories of chain complexes** — projective/injective model structures, Dold–Kan, monoidal model categories | 📝 | `lemma_acyclic_assembly_lemma_for_bounded_double_complexes_with_exact_rows_or_columns`, `lemma_bounded_above_complex_of_flat_objects_are_K_flat_with_respect_to_bi_daditive_functor_on_abelian_categories_where_target_is_AB5`, `corollary_right_exact_additive_bifunctor_with_enough_flats_have_flat_resolutions` |

---

## Phase 4: Derived Categories & Triangulated Categories

| # | Topic | Status | Notes / Key Labels |
|---|-------|--------|-------------------|
| 4.1 | **Derived categories of abelian categories** — D(A), K-injective/projective/flat resolutions, total derived functors | 📝 | `corollary_add_func_bewteen_ab_cats_has_a_right_or_left_total_derived_func_if_the_source_ab_cat_has_enough_injs_or_projs`, `corollary_cohomology_of_a_total_derived_functor_of_an_additive_functor_between_abelian_categories_can_be_calculated_by_hyper_derived_functors`, `lemma_an_object_of_abelian_category_with_enough_objects_of_a_class_on_the_right_left_has_right_left_resolution_by_the_class`, `lemma_any_projective_injective_object_of_an_abelian_category_is_acyclic_for_a_right_left_exact_functor` |
| 4.2 | **Triangulated categories** — exact triangles, octahedral axiom, t-structures, hearts, truncation functors | 📝 | `corollary_bdd_constructible_derived_category_with_algebraic_coefficients_is_triangulated`, `corollary_bdd_constructible_derived_category_with_rational_coefficients_is_triangulated`, `corollary_cone_of_a_morphism_in_a_triangulated_category_is_unique_if_no_nontrivial_backwards_morphism_exists`, `lemma_adjunctions_of_truncation_functors`, `proposition_subcategory_of_homotopy_category_of_an_abelian_category_whose_cohomology_objects_belong_to_a_serre_subcategory_is_a_triangulated_subcategory` |
| 4.3 | **Derived categories of sheaves** — constructible/adic sheaves, six operations (𝔸¹-local), perverse t-structure | 📝 | `definition_derived_category_of_bounded_constructible_complexes_of_adic_sheaves_with_integral_coefficients_on_a_noetherian_scheme`, `definition_derived_category_of_cohomologically_bounded_constructible_sheaves_with_rational_adic_coefficients_on_a_noetherian_scheme`, `proposition_base_change_theorem_for_a_three_functor_formalism_for_an_infty_category_with_finite_limits_and_a_class_of_morphisms_containing_isomorphisms_and_stable_under_pullback_and_composition`, `projection_formula_for_a_three_functor_formalism_for_an_infty_category_finite_limits_and_a_class_of_morphisms_containing_isomorphisms_and_stable_under_pullback_and_composition`, `proposition_kunneth_isomorphisms_for_a_three_functor_formalism_for_an_infty_category_finite_limits_and_a_class_of_morphisms_containing_isomorphisms_and_stable_under_pullback_and_composition`, `proposition_hom_to_pushforward_is_isom_to_pushforward_of_hom_from_pullback_for_a_six_functor_formalism_for_an_infty_category_with_finite_limits_and_a_class_of_morphisms_containing_isomorphisms_and_stable_under_pullback_and_composition` |
| 4.4 | **Six functor formalism (∞-categorical)** — f*, f*, f!, f!, ⊗, Hom, base change, projection formula, Künneth | 📝 | `definition_six_functor_formalism_for_an_infty_category_with_finite_limtis_and_class_of_morphisms_containing_isomorphisms_and_stable_under_pulback_and_composition`, `definition_three_functor_formalism_for_an_infty_category_with_finite_limtis_and_class_of_morphisms_containing_isomorphisms_and_stable_under_pulback_and_composition`, `definition_external_tensor_product_of_objects_for_a_three_functor_formalism_for_an_infty_category_finite_limits_and_a_class_of_morphisms_containing_isomorphisms_and_stable_under_pullback_and_composition` |
| 4.5 | **Stable ∞-categories as enhancements of triangulated** — stable ∞-cat → triangulated, uniqueness of enhancement, dg-enhancements | 🔄 | `corollary_homotopy_category_of_a_stable_infty_category_is_a_triangulated_category`; enhancement theory missing |
| 4.6 | **Spectral sequences** — Grothendieck spectral sequence, hypercohomology, Adams, Atiyah–Hirzebruch, motivic Adams | 🔄 | `lemma_bounded_below_spectral_sequence_in_abelian_category_converges_to_any_graded_object_that_it_abuts_to`, `corollary_cohomology_of_a_total_derived_functor_of_an_additive_functor_between_abelian_categories_can_be_calculated_by_hyper_derived_functors`; motivic spectral sequences missing |
| 4.7 | **K-theory & motivic cohomology** — algebraic K-theory, motivic cohomology, Bloch's higher Chow groups, motivic spectral sequence | 🔄 | Some in Schemes vault (`_concepts/corollary_chow_motives...`, `definition_chow_motive`); motivic cohomology proper missing |

---

## Phase 5: A¹-Homotopy Theory (Motivic) — Deep Dive

| # | Topic | Status | Notes / Key Labels |
|---|-------|--------|-------------------|
| 5.1 | **A¹-homotopy category (unstable)** — H(S)ₐ¹, A¹-localization, A¹-weak equivalences, A¹-invariant sheaves | 📝 | `definition_A1_model_structure_on_the_category_of_simp_sheaves_of_sets_on_the_nis_site_over_a_noeth_scheme_of_fin_dim_and_the_unstable_A1_homotopy_category`, `theorem_A1_homotopy_groups_are_strongly_A1_invariant`, `definition_A1_invariant_strongly_A1_invariant_strictly_A1_invariant_sheaves_of_sets_groups_ab_groups`, `theorem_sheaf_on_abelian_groups_is_strongly_A1_invariant_iff_strictly_A1_invariant` |
| 5.2 | **A¹-homotopy sheaves / A¹-fundamental group** — π₀ᴬ¹, π₁ᴬ¹, A¹-connected components, Nisnevich sheafification | 📝 | `definition_A1_homotopy_group_sheaf_of_an_object_of_the_pointed_unstable_A1_homotopy_category_over_a_noetherian_finite_dimensional_scheme`, `definition_sheaf_of_A1_connected_components_of_an_unbased_space` |
| 5.3 | **Motivic spheres & Tate objects** — Sⁿ, Gₘ^∧ⁿ, Tate spheres, suspension/tate suspension, motivic stable stems | ❌ | **MISSING** |
| 5.4 | **Stable A¹-homotopy category SH(S)** — motivic spectra, stable six functors, Tate twists, motives, ⊗, Hom | ❌ | **MISSING** — `definition_motivic_local_system_on_a_smooth_algebraic_variety` exists but stable theory absent |
| 5.5 | **Algebraic cobordism / MGL** — MGL, Landweber exactness, orientation, formal group laws, algebraic cobordism | ❌ | **MISSING** |
| 5.6 | **Motivic cohomology & Bloch's cycle complexes** — ℤ(n), higher Chow groups, motivic cohomology, Beilinson–Lichtenbaum | 🔄 | `definition_chow_motive` in Schemes; Bloch complexes, motivic cohomology proper missing |
| 5.7 | **A¹-representability & Nisnevich descent** — representability of A¹-homotopy sheaves, A¹-invariance + Nisnevich excision | 🔄 | `proposition_elementary_distinguished_square_condition_for_a_presheaf_to_be_sheaf_in_the_nisnevich_topology_over_a_noetherian_scheme_of_finite_dimension`, `definition_nisnevich_descent_for_a_category_fibered_in_groupoids_over_a_scheme`; A¹-representability theorems missing |
| 5.8 | **Motivic Steenrod operations / Adams spectral sequence** — motivic Steenrod algebra, motivic Adams, slice filtration, slice spectral sequence | ❌ | **MISSING** |
| 5.9 | **Étale realization & comparison** — étale realization functor, comparison to classical stable homotopy, Galois actions | 🔄 | Six functors for adic/constructible sheaves in Schemes; étale realization of motivic spectra missing |
| 5.10 | **Rigidity / conservativity theorems** — rigidity for motivic spectra, conservativity of realization, ℚ-completeness | ❌ | **MISSING** |

---

## Phase 6: Higher Category Theory & (∞,n)-Categories

| # | Topic | Status | Notes / Key Labels |
|---|-------|--------|-------------------|
| 6.1 | **(∞,n)-categories** — complete Segal spaces, n-fold quasi-categories, Θₙ-spaces, iterated (∞,1)-categories | 📝 | `definition_weak_n_category_tamsamani_simpson`, `definition_weak_infty_category`, `definition_parentheses_infty_category` |
| 6.2 | **(∞,2)-categories & double categories** — 2-categories as (∞,2), adjunctions, mates, fibrations of (∞,2)-cats | ❌ | **MISSING** |
| 6.3 | **(∞,n)-operads & Eₙ-algebras** — operads in ∞-categories, little disks, Eₙ-algebras, factorization homology | ❌ | **MISSING** |
| 6.4 | **Higher topos theory** — ∞-topoi, object classifiers, descent, hypercompletion, shape theory | ❌ | **MISSING** |
| 6.5 | **Goodwillie calculus / calculus of functors** — Taylor tower, derivatives, excision, chain rule, Goodwillie derivatives of identity | ❌ | **MISSING** |
| 6.6 | **Parametrized spectra / exodromy** — ∞-categories over a base, straightening for parametrized spectra | 🔄 | `theorem_straightening_unstraightening_equivalence_between_functors_to_Cat_infty_and_coCartesian_fibrations` covers straightening; parametrized stable homotopy missing |

---

## Phase 7: Derived Algebraic Geometry (DAG) Interface

| # | Topic | Status | Notes / Key Labels |
|---|-------|--------|-------------------|
| 7.1 | **Simplicial commutative rings / cdgas** — sCRing, cdga, model structures, cotangent complex, André–Quillen homology | ❌ | **MISSING** |
| 7.2 | **Derived schemes / stacks** — Spec of cdga, derived structure sheaf, derived mapping stacks, dg-stacks | ❌ | **MISSING** |
| 7.3 | **Derived ∞-categories QCoh** — quasi-coherent sheaves on derived stacks, t-structure, perfect complexes | ❌ | **MISSING** |
| 7.4 | **Deformation theory & cotangent complex** — obstruction theory, derived deformation functor, Lurie's DAG, formal moduli problems | ❌ | **MISSING** |
| 7.5 | **Derived loop spaces / HKR** — derived loop space, Hochschild homology, HKR filtration, cyclic homology | ❌ | **MISSING** |

---

## Phase 8: Applications & Advanced Topics

| # | Topic | Status | Notes / Key Labels |
|---|-------|--------|-------------------|
| 8.1 | **Algebraic K-theory of schemes / ∞-categories** — K-theory as additive invariant, Dundas–Goodwillie–McCarthy, trace methods | ❌ | **MISSING** |
| 8.2 | **THH / TC / cyclotomic spectra** — topological Hochschild homology, topological cyclic homology, Bhatt–Morrow–Scholze | ❌ | **MISSING** |
| 8.3 | **Prismatic cohomology via δ-rings** — prismatic site, Nygaard filtration, Hodge–Tate comparison, A_inf-cohomology | ❌ | **MISSING** |
| 8.4 | **Geometric Langlands (categorical)** — D-modules, Hecke eigensheaves, spectral side, ind-coherent sheaves | ❌ | **MISSING** |
| 8.5 | **Factorization homology / topological chiral homology** — Eₙ-algebras, framed/disk algebras, factorization homology of manifolds | ❌ | **MISSING** |
| 8.6 | **Condensed mathematics / analytic ∞-categories** — condensed sets, analytic ∞-categories, condensed spectra, solid abelian groups | ❌ | **MISSING** |

---

## Cross-Vault Dependencies

| This Phase | Depends On | Vault |
|------------|------------|-------|
| 0–1 (simplicial sets, model cats) | Abelian categories, derived functors | `AbstractAlgebra` (✅ extensive) |
| 1.7–1.9, 5 (A¹/motivic) | Nisnevich site, schemes, étale cohomology | `Schemes` (📝 extensive), `AlgebraicNumberTheory` (📝 étale) |
| 2–3 (∞-cats, classical htpy) | Topological spaces, CW complexes, spectral sequences | `Topology` (📝 good coverage) |
| 4 (derived cats, six functors) | Constructible/adic sheaves, six functors | `Schemes` (📝 extensive for adic/constructible) |
| 7 (DAG) | Simplicial rings, cotangent complex | **Missing** | — |
| 8 (advanced) | All of the above | — |

---

## Priority Next Steps (for SimplicialTheory content.tex wiring)

### Immediate (wire existing components)
1. **Wire Phase 0 foundations** — simplicial sets, nerves, Kan complexes, quasi-categories, geometric realization, homotopy categories
2. **Wire Phase 1 model categories** — standard/Joyal/A¹ model structures, simplicial sheaves, Bousfield localization
3. **Wire Phase 2 ∞-category basics** — functors, (co)limits, adjunctions, monoidal ∞-cats, stable ∞-cats
4. **Wire Phase 3 classical homotopy** — homotopy groups, loop/suspension, stable homotopy theory

### Medium-term (create missing components)
5. **A¹-homotopy theory deepening** — A¹-fundamental group, A¹-representability, A¹-invariance theorems
6. **Stable motivic homotopy (SH(S))** — motivic spectra, Tate objects, stable six functors (major gap)
7. **Derived ∞-categories enhancement** — stable ∞-cat ↔ triangulated, uniqueness of enhancement
8. **Motivic cohomology / algebraic K-theory** — Bloch's higher Chow groups, motivic spectral sequence

### Long-term (create new major areas)
9. **Goodwillie calculus, (∞,n)-categories** — calculus of functors, higher operads
10. **Derived algebraic geometry** — sCRing, derived schemes, cotangent complex, HKR
11. **Prismatic / THH / geometric Langlands** — p-adic cohomology, factorization homology, condensed math

---

## Quick-Start: What to `\input` First in `content.tex`

```latex
% Phase 0: Simplicial foundations
\input{../_definitions/definition_simplex_of_a_simplicial_object_in_a_category_and_face_and_degeneracy_maps}
\input{../_definitions/definition_standard_n_simplex}
\input{../_definitions/definition_horn_of_the_nth_standard_simplex}
\input{../_definitions/definition_empty_simplicial_set}
\input{../_definitions/definition_final_object_of_a_topological_or_simplicial_category_or_simplicial_set}
\input{../_definitions/definition_nerve_of_a_category}
\input{../_definitions/definition_kan_complex}
\input{../_definitions/definition_infty_category_quasi_category}
\input{../_definitions/definition_joyal_model_structure_on_the_category_of_simplicial_sets}
\input{../_definitions/definition_geometric_realization_of_a_simplicial_set}
\input{../_definitions/definition_singular_complex_of_a_topological_space}
\input{../_concepts/theorem_unit_and_counit_morphisms_for_geometric_realization_singular_complex_adjunction_are_weak_homotopy_equivalences_for_compactly_generated_spaces_and_simplicial_sets}
\input{../_concepts/corollary_homotopy_category_of_simplicial_sets_is_equivalent_to_the_homotopy_category_of_compactly_generated_weakly_hausdorff_spaces}
\input{../_definitions/definition_homotopy_category_of_a_simplicial_set}
\input{../_definitions/definition_homotopy_category_of_the_category_of_simplicial_sets}

% Phase 1: Model categories
\input{../_definitions/definition_model_category}
\input{../_definitions/definition_simplicial_model_structure_on_a_category}
\input{../_definitions/definition_standard_model_structure_on_the_category_of_simplicial_sets}
\input{../_definitions/definition_simplicial_weak_equivalences_cofibrations_and_fibrations_for_simplicial_sheaves_on_a_site}
\input{../_concepts/theorem_simplicial_model_category_structure_on_simplicial_sheaves}
\input{../_definitions/definition_A1_weak_equivalence_of_simplicial_sheaves_of_sets_on_the_nisnevich_topology_over_a_noetherian_finite_dimensional_scheme}
\input{../_definitions/definition_A1_local_weak_equivalence_fibration_of_simplicial_sheaves_of_sets_on_the_nisnevich_site_over_a_noetherian_finite_dimensional_scheme}
\input{../_definitions/definition_A1_model_structure_on_the_category_of_simp_sheaves_of_sets_on_the_nis_site_over_a_noeth_scheme_of_fin_dim_and_the_unstable_A1_homotopy_category}
\input{../_concepts/proposition_A1_model_structure_on_category_of_simplicial_nisnevich_sheaves}
\input{../_concepts/theorem_A1_homotopy_groups_are_strongly_A1_invariant}

% Phase 2: ∞-categories
\input{../_definitions/definition_functor_between_infty_categories}
\input{../_definitions/definition_inner_fibration_between_infinity_categories}
\input{../_definitions/definition_coCartesian_fibration_between_infinity_categories}
\input{../_concepts/theorem_straightening_unstraightening_equivalence_between_functors_to_Cat_infty_and_coCartesian_fibrations}
\input{../_definitions/definition_limit_and_colimit_for_a_map_from_a_simplicial_set_to_an_infty_category}
\input{../_definitions/definition_symmetric_monoidal_infinity_category}
\input{../_definitions/definition_stable_infinity_category}
\input{../_concepts/corollary_homotopy_category_of_a_stable_infty_category_is_a_triangulated_category}

% Phase 3: Classical homotopy
\input{../_definitions/definition_homotopy_groups_of_a_kan_simplicial_set}
\input{../_concepts/proposition_reduced_suspension_loop_space_adjucntion_for_pointed_topological_spaces}
\input{../_concepts/theorem_freudenthal_suspension_theorem}
\input{../_definitions/definition_model_category_classes_for_spectra_of_topological_spaces}
\input{../_concepts/theorem_stable_model_structure_topological_spectra}
\input{../_concepts/corollary_stable_homotopy_groups_of_pointed_topological_spaces_give_a_reduced_homology_theory}
```

---

## Summary Statistics

| Phase | Total Items | ✅ ACTIVE | 📝 DEFINED | ❌ MISSING |
|-------|-------------|-----------|------------|------------|
| 0: Foundations | 10 | 0 | 10 | 0 |
| 1: Model Categories | 13 | 0 | 12 | 1 |
| 2: ∞-Categories | 10 | 0 | 8 | 2 |
| 3: Classical Homotopy | 9 | 0 | 6 | 3 |
| 4: Derived/Triangulated | 7 | 0 | 6 | 1 |
| 5: A¹/Motivic Deep | 10 | 0 | 4 | 6 |
| 6: Higher Cats | 6 | 0 | 1 | 5 |
| 7: DAG Interface | 5 | 0 | 0 | 5 |
| 8: Advanced | 6 | 0 | 0 | 6 |
| **TOTAL** | **76** | **0** | **47** | **29** |

**Key observation**: `SimplicialTheory/content.tex` currently contains **only `\nocite{*}`** — zero components are wired. However, the vault has **substantial pre-existing components** (47 DEFINED across Phases 0–5), mostly in `_definitions/` and `_concepts/`, covering:
- Simplicial sets, Kan complexes, quasi-categories, nerves
- Model structures (standard, Joyal, simplicial sheaves, A¹)
- Geometric realization / singular complex adjunction
- ∞-categories: functors, fibrations, straightening, monoidal, stable
- Classical homotopy: homotopy groups, loop/suspension, stable spectra
- Derived/triangulated: six functor formalism (∞-categorical), constructible/adic derived categories
- A¹-homotopy: Nisnevich site, A¹-local model structure, A¹-homotopy groups

**The main gaps** are:
- **No content wired at all** — `content.tex` is empty
- **Stable motivic homotopy (SH(S)) entirely missing** (Phase 1.10, 5.3–5.4)
- **Higher category theory** ((∞,n)-cats, operads, Goodwillie) missing
- **Derived algebraic geometry** missing
- **Advanced applications** (THH, prismatic, geometric Langlands, condensed) missing

---

*Generated from vault inspection on 2026-07-23. Update after each wiring/authoring session.*