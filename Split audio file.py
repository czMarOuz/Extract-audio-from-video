# První krok
# Tento program má na starosti rozdělení audio souboru podle nastavené délky do několika souborů.
from pydub import AudioSegment
import os
from tkinter import filedialog

def stříhat_a_exportovat(audio, délky, výstupní_složka):
    for i, délka in enumerate(délky):
        # Stříhání audio podle délky
        cut_audio = audio[i * délka:(i + 1) * délka]
        
        # Nastavení názvu pro exportovaný soubor
        název_souboru = f"výstup_{i + 1}.mp3"
        
        # Exportování zkráceného audio do výstupní složky
        cesta_k_výstupu = os.path.join(výstupní_složka, název_souboru)
        cut_audio.export(cesta_k_výstupu, format="mp3")
        
        print(f"Soubor {název_souboru} byl úspěšně exportován.")

    # Zbývající délka původní stopy
    zbytek_audio = audio[len(délky) * délky[0]:]

    if len(zbytek_audio) > 0:
        # Nastavení názvu pro exportovaný soubor
        poslední_název = "transcript_last.mp3"
        
        # Exportování zbytku audio do výstupní složky
        cesta_k_poslednímu_souboru = os.path.join(výstupní_složka, poslední_název)
        zbytek_audio.export(cesta_k_poslednímu_souboru, format="mp3")
        
        print(f"Poslední soubor {poslední_název} byl úspěšně exportován.")

def vyber_soubor():
    cesta = filedialog.askopenfilename()
    print(f"Byl vybrán soubor: {cesta}")
    return cesta

cesta_k_souboru = vyber_soubor()

if cesta_k_souboru:
    segment = AudioSegment.from_file(cesta_k_souboru, format="mp3") # Načtení audio souboru
    délky_střihů = [1500000] * (len(segment) // 1500000)  # Délky, podle kterých chcete stříhat (v milisekundách. 25 minut pro každý segment
    výstupní_složka = os.path.join(os.path.dirname(cesta_k_souboru), "výstupní složka")
    os.makedirs(výstupní_složka, exist_ok=True) # Vytvoření výstupní složky, pokud neexistuje
    stříhat_a_exportovat(segment, délky_střihů, výstupní_složka) # Volání funkce pro stříhání a exportování