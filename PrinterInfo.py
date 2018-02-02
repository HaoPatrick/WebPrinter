import os

DEBUG = 'DEBUG' in os.environ


def get_info_from_IO():
  pass


def get_printer_info():
  property_lines = list(filter(None, raw_text.split("\n")))
  properties = []
  for prt in property_lines:
    tokens = prt.split(": ")
    options = tokens[1].split(" ")
    current = ''
    # Ugly
    for index, op in enumerate(options):
      if op[0] == '*':
        current = op[1:]
        options[index] = op[1:]
        break
    names = tokens[0].split("/")
    properties.append({
      "display_name": names[1],
      "option_name": names[0],
      "options": options,
      "default": current
    })
  print(properties)
