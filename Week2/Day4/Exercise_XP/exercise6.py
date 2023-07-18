magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

def make_great(magician_names):
    great = lambda s: f"The Great {s}"
    return list(map(great, magician_names))

magician_names = make_great(magician_names)
show_magicians(magician_names)             