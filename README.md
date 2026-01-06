Home Assistant Fűtésvezérlés v3 – Komplett Prediktív Kazánvezérlő Rendszer.

Áttekintés:

Ez egy  teljesen automatizált, önkalibráló fűtésvezérlő rendszer Home Assistant alapokon, amely egy hagyományos kondenzációs gázkazán energiahatékony és komfortos üzemeltetését biztosítja,
opentherm protokol nélkül.
A rendszer prediktívan kapcsolja be és ki a kazánt, modulálja a kazán görbéjét (szimulált külső hőmérséklettel), valamint folyamatosan tanulja a ház hőtehetetlenségét és fűtési/hűtési jellemzőit.

Főbb jellemzők:

Prediktív be- és kikapcsolás:
Figyelembe veszi a ház hűtési/fűtési rátáját és tehetetlenségi idejét → minimális túllövés, pontos célhőmérséklet-tartás.

Soft Start & Soft Stop:

Bekapcsoláskor alacsony görbével indul, kikapcsoláskor korábban áll le a tehetetlenség kompenzálásával.
ΔT-alapú moduláció.
Cél: 5 °C különbség az előremenő és visszatérő víz között.
A rendszer finoman korrigálja a kazánnak „hazudott” külső hőmérsékletet egy P-szabályozóval.

Öntanuló ráta:

5 percenként méri a beltéri hőmérséklet-változást és EMA-val frissíti a fűtési (heating_rate) és hűtési
(cooling_rate) rátákat.

Guardrail védelmek:
Figyeli, ha a kazán fut, de a felfűtési ráta túl alacsony (< 0.1 °C/h) → hiba jelzése és értesítés.


Hardver komponensek:

ESP8266 (D1 Mini) – kazánvezérlő modul.
2 × DS18B20 – előremenő és visszatérő víz hőmérséklet mérése.
PWM kimenet optocsatolóval – NTC ellenállás szimuláció (kazán külsőhő-érzékelője).
H11F1 optocsatoló - FET kimenettel, a teljes kazánoldali leválasztás miatt.
2 × relé – kazán ki/bekapcsolás + tiltás (túlmelegedés védelem).
Státusz LED intelligens jelzéssel.

Szoftver komponensek

Home Assistant automatizmusok (YAML):
Kazán BEKAPCSOLÁS (holtsáv + predikció)
Kazán KIKAPCSOLÁS (soft stop + dinamikus korrekció)
Modulációs vezérlés (ΔT alapú külső T szimuláció)
Guardrail hibaészlelés (alacsony ráta)

AppDaemon Python script:

learn_heat_rate() – 5 percenként futó öntanuló ráta számítás.
(Rakd ki egy kartyara az entitásokat, hogy lásd, hogyan dolgozik.)


ESPHome YAML – teljes firmware az eszközhöz

Fontos entitasok:

climate.futes – fő thermostat (célhőmérséklet)
sensor.kisnappali_homerseklet_atlag – beltéri átlaghőmérséklet (
sensor.ble_temperature_kuls_hmer – valós külső hőmérséklet
sensor.boiler_digipot_eloremeno_viz_hofok és visszatero_viz_hofok – vízhőmérsékletek
number.boiler_digipot_boiler_temperature – szimulált külső hőmérséklet (-20…+20 °C)
switch.boiler_digipot_boyler_on_off – kazán relé
input_boolean.futes_uzemmod_auto – auto mód ki/be
input_number.heating_rate, cooling_rate, last_temp – tanult értékek


Telepítés / Beüzemelés:

ESPHome: feltölteni a megadott YAML-t egy mini D1 eszközre (DS18B20 címeket cserélni!)
Home Assistant: létrehozni a szükséges input_number és input_boolean helper-eket


Automatizmusok bemásolása a configuration.yaml vagy automation.yamlba.


AppDaemon: 

Telepítsd a HACS-ból a Pyscript addont.
Hozz létre egy pyscript mappát es ebben egy learn_heat_rate.py fàjlt.
Másold be a python fàjlt, restartold a HA-t.
A hàttérben folyamatosan dolgozik a script.

Bekapcsolni az input_boolean.futes_uzemmod_auto-t.



Nálam egy WESTEN STAR CONDENS 24  kondenzációs kazánt vezérlel a HA. 
KT görbe alapján a kazán 20 értékre állítva.


Tapasztalatom 3 hónap használat után.

~ 15% - 20% gázmennyiséget tudtam spórolni, a hagyományos on-off vezérléssel szemben.
Túlmeretezett radiatorok vannak a rendszerben, így az előremenő víz max. 50 C⁰ lehet,
így bőven benne marad a kazán a megfelelő kondenzációs tartományban.



Hozzavalók: 

ESP8266 Wemos mini d1
H11F1 FET opto coupler
4.7 kOhm 0.5W ADC felső osztó
1 kOhm 0.5W  ADC  alsó  osztó
1 kOhm 1-2 db, a kapcsoló tranzisztorok bázisáramának beállítására

220 Ohm 0.5W --
Figyelem!
  Értéke változhat (a kazán időjáráskövető bemeneteletől függően), 
  az H11F1 opto LED-jének a megfelelő munkapontját(áramát) állítja be.
                 
 Ki kell kisérletezni a kazánodhoz, hogy a +-20 C⁰ hőmérsékleti határok között a linearitása megfelelő   
 legyen.
 (az esp-ben number.boiler_digipot_boiler_temperature értékének változtatásával         
 ellenőrizheted, hogy a kazán kijelzőjén megjelenő, külső hőmérséklet, megegyezik-e a   
  beállított értékkel)

1-2 db npn tranzisztor, ami az on-off relét illetve a teljes tiltást kapcsolja.
                 
  Saját példám, mivel megtartottam (esp hiba esetére) az eredeti COMPUTER RF kezelőt és                       vezérlőjét, igy a vezérlőbe beépített relé-t használtam fel erre a célra, azaz
  közvetlenül a relét kapcsoló tranzisztor bázisát vezérlem. 
  Megfutás, hiba esetén, a tilt bontja az on - off relét, 
  még a vész termosztát (Computherm RF) esetén is!
   
Kapcslolási rajz szerintem egyértelmű, akinek nincs, attól egy kis türelmet kérek.

Használjatok egészséggel.

használt entitasok, sensorok listája:

sensor.kisnappali_homerseklet_atlag  beltéri átlaghőmérséklet  
sensor.futes_tehetetlensegi_ido_teljes_perc  Tanult tehetetlenségi idő (perc)  
sensor.boiler_digipot_eloremeno_viz_hofok  Előremenő vízzhőmérséklet  
sensor.boiler_digipot_visszatero_viz_hofok  Visszatérő víz hőmérséklet  
sensor.ble_temperature_kuls_hmer  Valós külső hőmérséklet  
input_number.cooling_rate  Tanult hűtési ráta (°C/óra)  
input_number.heating_rate  Tanult fűtési ráta (°C/óra)  
input_number.futes_tehetetlensegi_ido_min  Bekapcsoláskori tehetetlenségi idő (perc)  
input_number.last_temp  Utolsó beltéri hőmérséklet a tanuláshoz  
input_boolean.futes_uzemmod_auto Auto üzemmód engedélyezése  
input_boolean.futes_ratavesztes_hiba  Hiba jelző (alacsony ráta esetén)  
climate.futes Fő thermostat (célhőmérséklet)  
switch.boiler_digipot_boyler_on_off  Kazán ki/bekapcsolás  
input_number.boiler_digipot_boiler_temperature  Szimulált külső hőmérséklet / görbe offset  
