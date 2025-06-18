def array_of_names(name_dict):
    full_names = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_name.append(full_name)
    return full_name

if __name__ == "__name__":
    example_dict = {
        "john": "doe",
        "jane": "smith",
        "aloce" : "johnson"
    }
     
    
names = array_of_names(example_dict)
print(names)