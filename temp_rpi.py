#!/usr/bin/env python3
# test
import subprocess
import platform
import time  # pour faire des pauses entre les mesures
import logging

#Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Service temp_rpi démarré")


# Définir le seuil de température (en °C)
TEMP_SEUIL = 70

# Fonction pour récupérer la température
def get_temp():
    try:
        result = subprocess.run(
            ['vcgencmd', 'measure_temp'],
            capture_output=True, text=True
        )
        temp_str = result.stdout.strip()  # "temp=55.2'C"
        temp_val = float(temp_str.replace("temp=", "").replace("'C", ""))
        return temp_val
    except Exception as e:
        # print(f"Erreur lors de la récupération de la température : {e}")
        logging.error(f"Erreur lors de la récupération de la température : {e}")
        return None

# Fonction pour envoyer un avertissement (ici sur la console)
def send_alert(temp):
    # print(f"⚠️ Avertissement ! Température élevée : {temp}°C")
    logging.warning(f"Température élevée détectée : {temp}°C")


# Fonction principale
def main():
    system_type = platform.system() + " " + platform.machine()
    # print(f"Système détecté : {system_type}")
    # logging.info(f"Système détecté : {system_type}")

    temp = get_temp()
    if temp is not None:
        # print(f"Température actuelle : {temp}°C")
        logging.info(f"Température actuelle : {temp}°C")

        if temp >= TEMP_SEUIL:
            send_alert(temp)

if __name__ == "__main__":
    while True:           # Boucle infinie
        main()            # Vérifie la température
        time.sleep(5)     # Pause de 5 secondes entre chaque vérification


