import os
import subprocess
from typing import List, Dict

import config

DEBUG: bool = 'DEBUG' in os.environ


def get_printer_info() -> List[Dict[str, str]]:
  try:
    raw_text: str = get_info_from_device()
  except Exception:
    raise FileNotFoundError("printer connection error")
  return parse_info(raw_text)


def get_info_from_device() -> str:
  if DEBUG:
    return config.LPOPTION_SAMPLE
  else:
    rv = subprocess.Popen(["lpoptions", "-p", config.PRINTER_NAME, "-l"], stdout=subprocess.PIPE)
    plaintext, error = rv.communicate()
    if error:
      raise AttributeError(error)
    return plaintext.decode()


def parse_info(raw_text: str) -> List[Dict[str, str]]:
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
  return properties
