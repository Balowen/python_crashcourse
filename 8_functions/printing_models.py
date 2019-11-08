import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'robototron']
completed_models = []

# list_name[:] passes a copy of a list
pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)

print(unprinted_designs)