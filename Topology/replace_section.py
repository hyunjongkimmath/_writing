with open('content.tex', 'r') as f:
    content = f.read()
content = content.replace('\r\n', '\n')

# Find the exact location
idx = content.find('Basis of a topological space}')
print(f"Found at index: {idx}")

# We need to replace from idx+29 (after the two \n) to idx+287 (before \subsection)
# Let's verify the target
print(f"Content at idx+29 to idx+287:")
print(repr(content[idx+29:idx+288]))

# Build replacement
old_text = content[idx+29:idx+288]
new_text = (
    "\n\n"
    "\\input{../_definitions/definition_compact_open_topology_on_the_set_of_continuous_maps_between_topological_spaces_and_function_space.tex}\n"
    "\\input{../_definitions/definition_weak_topology_on_a_vector_space.tex}\n"
    "\\input{../_definitions/definition_weak_star_topology_on_a_dual_space.tex}\n"
    "\\input{../_concepts/proposition_weak_topology_is_initial_topology.tex}\n"
    "\\input{../_concepts/proposition_weak_star_topology_is_coarsest_making_evaluations_continuous.tex}\n\n\n\n"
    "\\subsection{Separation axioms}"
)

print(f"\nOld text:")
print(repr(old_text))
print(f"\nNew text:")
print(repr(new_text))

if old_text in content:
    content = content.replace(old_text, new_text)
    with open('content.tex', 'w') as f:
        f.write(content)
    print("SUCCESS: Replaced!")
else:
    print("FAILED: Old text not found in content")
    # Try without the last \subsection part
    old_text2 = content[idx+29:idx+287]
    print(f"\nTrying without last char:")
    print(repr(old_text2))
    if old_text2 in content:
        content = content.replace(old_text2, new_text[:-len("\\subsection{Separation axioms}")])
        with open('content.tex', 'w') as f:
            f.write(content)
        print("SUCCESS with alt!")