import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_line(line, delay=0.08):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_lyrics(lyrics, line_delays, default_delay=2):
    clear_console()
    print("🎵 Multo - Cup of Joe (Chorus) 🎵\n")
    time.sleep(2)
    for i, line in enumerate(lyrics):
        type_line(line)
        # Use custom delay if specified, otherwise use default
        time.sleep(line_delays.get(i, default_delay))

# Chorus lyrics only
chorus = [
    "Hindi na makalaya",
    "Dinadalaw mo 'ko bawat gabi",
    "Wala mang nakikita",
    "Haplos mo'y ramdam pa rin sa dilim",
    "Hindi na na-nanaginip",
    "Hindi na ma-makagising",
    "Pasindi na ng ilaw",
    "Minumulto na 'ko ng damdamin ko",
    "Ng damdamin ko",
    "",
    "'Di mo ba ako lilisanin?",
    "Hindi pa ba sapat pagpapahirap sa 'kin? (Damdamin ko)",
    "Hindi na ba ma-mamamayapa?",
    "Hindi na ba ma-mamamayapa?"
]

# Custom delay for specific dramatic lines (index: delay in seconds)
line_delays = {
    4: 3,  # "Hindi na na-nanaginip"
    5: 3,  # "Hindi na ma-makagising"
    6: 2,  # "Pasindi na ng ilaw"
    7: 3,  # "Minumulto na 'ko ng damdamin ko"
    8: 2   # "Ng damdamin ko"
}

display_lyrics(chorus, line_delays)
