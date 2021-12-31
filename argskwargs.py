def func(*args, **kwargs):
    colors = list()
    for color in args:
        colors.append(color)
    for key, value in kwargs.items():
        colors.append(value)
    return(", ".join(colors))
