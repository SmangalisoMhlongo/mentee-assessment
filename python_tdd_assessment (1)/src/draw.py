def draw_square(size):
    """Return a filled square of '*' characters."""
    if size <= 0:
        raise ValueError
    square = "*"
    re_square = ((square * size)+"\n") * size
    return re_square
# print(draw_square(4))

def draw_triangle(height):
    """Return a right triangle of '*' characters."""
    if height <= 0:
        raise ValueError
    char = "*"
    tri = 1
    ls = []
    for i in range(1,height+1):
        tri = char * i
        ls.append(tri)
    return "\n".join(ls)
# print(draw_triangle(4))   

def draw_hollow_rectangle(width, height):
    """Return a hollow rectangle of '*' characters."""
    if height <= 0 or width <= 0:
        raise ValueError
    char = "*"

    ls = []
    rect = ((width * char)+"\n")*height
    ls.append(rect)
    for i in range(len(ls)):
        if ls[i] != ls[0] or ls[i] != ls[-1]:
          
            ls.remove(i[1:-2])

    return "".join(ls)

print(draw_hollow_rectangle(5, 4))
  

