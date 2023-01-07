def print_color(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="purple":
    print("\033[35m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print()
print("With my ", end="")
print_color("purple", "new program ")
print_color("reset", "I can just call red('and') ")
print_color("red", "and ")
print_color("reset", "that word will appear in the color I set it to.")
print()
print("With no ", end="")
print_color("green", "weird gaps.")
print()
print_color("reset", "Epic.")