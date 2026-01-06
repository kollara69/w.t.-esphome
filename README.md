# w.t.-esphome
esphome heating with weather tracking

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
