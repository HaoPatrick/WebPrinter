raw_text = '''PageSize/Paper Size: Custom.WIDTHxHEIGHT *Letter Legal Executive.2 Statement 8.5x13 A4 A5 B5 216x330mm DoublePostcardRotated 7.75x10.75 Env10 EnvMonarch EnvC5 EnvDL EnvISOB5
MediaType/Paper Type: *automatic plain-paper preprinted letterhead transparency prepunched labels bond recycled color light intermediate heavy extra-heavy card-stock rough glossy heavy-glossy extra-heavy-glossy tough-paper envelope
OutputMode/Quality: *normal
HPColorMode/Color: colorsmart colorsync *grayscale
ColorModel/Color Model: *Gray RGB RGBW
HPPaperSource/Source: *Autoselect ManualFeed Tray1 Tray2 Tray3
OutputBin/Output Bin: *Main Rear
Resolution/Resolution: *600x600dpi
Duplex/Two-Sided: *None DuplexNoTumble DuplexTumble
HPDigitalFlash/Adaptive Lighting: *default off low medium high automatic
HPContrastEnhance/Photo Brightening: *default off low medium high automatic
HPSmartFocus/SmartFocus: *default off automatic
HPSmoothing/Smoothing: *default off low medium high automatic
HPSharpness/Sharpness: *default off low medium high automatic
HPRedEye/Auto Red-eye Removal: *default off automatic
'''
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
