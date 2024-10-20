"""
Hexadecimal Colour Lookup
Estimate: 20 minutes
Actual: 15 minutes
"""

COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc",
    "antiquewhite3": "#cdc0b0",
    "antiquewhite4": "#8b8378",
    "aquamarine1": "#7fffd4",
    "aquamarine2": "#76eec6",
    "aquamarine4": "#458b74",
    "azure1": "#f0ffff",
    "azure2": "#e0eeee"
}

def main():
    colour_name = input("Enter a colour name: ").lower()
    while colour_name != "":
        hex_code = COLOUR_CODES.get(colour_name)
        if hex_code:
            print(f"The code for \"{colour_name}\" is {hex_code}")
        else:
            print(f"Invalid colour name: \"{colour_name}\". Please try again.")
        colour_name = input("Enter a colour name: ").lower()

if __name__ == "__main__":
    main()
