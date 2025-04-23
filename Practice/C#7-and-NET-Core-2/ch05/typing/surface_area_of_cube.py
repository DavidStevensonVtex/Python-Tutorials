def surface_area_of_cube(edge_length: float) -> str:
    print("type(edge_length): ", type(edge_length), edge_length)
    return f"The surface area of the cube is {6 * edge_length ** 2}."


print(surface_area_of_cube(1))

# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# print(surface_area_of_cube("one"))

print(surface_area_of_cube(True))
