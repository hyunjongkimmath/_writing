with open('content.tex', 'r') as f:
    content = f.read()

# Fix the messed up section
old = (
    r'\subsubsection{Basis of a topological space}' + '\n\n' +
    r'\input{../_definitions/definition_compact_open_topology_on_the_set_of_continuous_maps_between_topological_spaces_and_function_space.tex}' + '\n' +
    r'\input{../_definitions/definition_weak_topology_on_a_vector_space.tex}' + '\n' +
    r'\input{../_definitions/definition_weak_star_topology_on_a_dual_space.tex}' + '\n' +
    r'\input{../_concepts/proposition_weak_topology_is_initial_topology.tex}' + '\n' +
    r'\input{../_concepts/proposition_weak_star_topology_is_coarsest_making_evaluations_continuous.tex}' + '\n\n\n' +
    r'\subsection{Separation axioms}subsubsection{Separation axioms}' + '\n' +
    r'\input{../_definitions/definition_G_delta_set_and_F_sigma_set_of_a_topological_space.tex}' + '\n' +
    r'\input{../_definitions/definition_separation_axioms_of_topology.tex}'
)

new = (
    r'\subsubsection{Basis of a topological space}' + '\n\n' +
    r'\input{../_definitions/definition_neighborhood_and_neighborhood_basis_of_a_point_in_a_topological_space.tex}' + '\n' +
    r'\input{../_definitions/definition_basis_for_a_topology.tex}' + '\n' +
    r'\input{../_definitions/definition_first_and_second_countable_topological_space.tex}' + '\n\n\n' +
    r'\subsubsection{Function space topologies}' + '\n\n' +
    r'\input{../_definitions/definition_compact_open_topology_on_the_set_of_continuous_maps_between_topological_spaces_and_function_space.tex}' + '\n' +
    r'\input{../_definitions/definition_weak_topology_on_a_vector_space.tex}' + '\n' +
    r'\input{../_definitions/definition_weak_star_topology_on_a_dual_space.tex}' + '\n' +
    r'\input{../_concepts/proposition_weak_topology_is_initial_topology.tex}' + '\n' +
    r'\input{../_concepts/proposition_weak_star_topology_is_coarsest_making_evaluations_continuous.tex}' + '\n\n' +
    r'\subsubsection{Separation axioms}' + '\n' +
    r'\input{../_definitions/definition_G_delta_set_and_F_sigma_set_of_a_topological_space.tex}' + '\n' +
    r'\input{../_definitions/definition_separation_axioms_of_topology.tex}'
)

if old in content:
    content = content.replace(old, new)
    with open('content.tex', 'w') as f:
        f.write(content)
    print('Replaced successfully')
else:
    print('Not found')
    idx = content.find('Basis of a topological space')
    print('Context:', repr(content[idx:idx+500]))