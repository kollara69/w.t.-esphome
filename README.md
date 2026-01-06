# w.t.-esphome
esphome heating with weather tracking

WESTEN STAR CONDENS 24  kondenzációs kazán vezerlese HA  alól.

Opentherm nélküli, on-off vezérlésű kazán, modulciós vezérlése, külső hőmérséklet szimulációval HA alá.

Hozzavalók: 

Hacs-bol a Pyscript telepíteni, majd letrehozni egy pyscript mappát, abban egy learn_heat_rate.py fájlt.
Bemásolod a py tartalmat, restart és hagyd, hogy dolgozzon egy jó pár napig.
Rakd ki egy kartyara, hogy lásd, hogyan dolgozik a háttarben.



ESP8266 Wemos mini d1
H11F1 FET opto coupler
4.7 kOhm 0.5W ADC felső osztó
1 kOhm 0.5W  ADC  alsó  osztó
220 Ohm 0.5W -- 
                Értéke változhat (a kazántól fűggően), 
                az H11F1 opto LED-jének a megfelelő munkapontját(áramát) állítja be.
                 
                Ki kell kisérletezni, hogy a +-20 C⁰ hőmérsékleti határok között a linearitása megfelelő                     legyen.
                (az esp-ben number.boiler_digipot_boiler_temperature értékének változtatásával                               ellenőrizheted, hogy a kazán kijelzőjén megjelenő, külső hőmérséklet, megegyezik-e a   
                beállított értékkel)

1 db npn tranzisztor, amivel az on-off relét kapcsolod.
                 
                 Saját példám, mivel megtartottam (esp hiba esetére) az eredeti COMPUTER RF kezelőt és                        vezérlőjét, igy a vezérlőbe beépített relé-t használtam fel erre a célra, azaz
                 közvetlenül a relét kapcsoló tranzisztor bázisát vezérlem.

   



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
