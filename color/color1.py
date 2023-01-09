import crayons

# print 'red string' in red
print(crayons.red('red string'))

# Red White and Blue text
print(f"{crayons.red('red')} white {crayons.blue('blue')}")

crayons.disable()

print(f"{crayons.red('red')} white {crayons.blue('blue')}")

crayons.DISABLE_COLOR = False  # Enable the crayons package

# This line will print in color because color is enabled 
print(f"{crayons.red('red')} white {crayons.blue('blue')}")


# print 'red string' in red
print(crayons.red('red string', bold=True))

# print 'yellow string' in yellow
print(crayons.yellow('yellow string', bold=True))

# print 'magenta string' in magenta
print(crayons.magenta('magenta string', bold=True))

# print 'white string' in white
print(crayons.white('white string', bold=True))
