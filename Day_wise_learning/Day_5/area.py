def cuboid_surface_area(length: float, breadth: float, height: float) -> float:
    """Return the surface area of a cuboid."""
    return 2 * (length * breadth + breadth * height + length * height)


print(cuboid_surface_area(4, 5, 6))


# The same calculation using a lambda function.

surface_area = lambda length, breadth, height: (
    2 * (length * breadth + breadth * height + length * height)
)

print(surface_area(4, 5, 6))