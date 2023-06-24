Famlies={
    'charley':
    {'sam':{'Boxy','Rosy'},
     'Nila':{'pepsi'}},
    'Devi':
    { 'Tommy':{'Tony'},
      'Timmy':{'Hamster'},
      'Tammy':{'Hamster'}},
    'Carlos':
    {'Diego':'Cat','ferret':'Fox'}
    }
for parent,children in Famlies.items():
    print(f"(parent) has )len(children) kid(s):")
    print(f"{',and'.join([str(child) for child in [*children]])}")
        