@time_trigger("cron(*/5 * * * *)")
def learn_heat_rate():
    # --- Szenzorok ---
    indoor_raw = state.get("sensor.kisnappali_homerseklet_atlag") # ÁTLAGOLT ÉRTÉK 
    if indoor_raw in [None, "unknown", "unavailable"]:
        log.info("⏸ Tanulás kihagyva: nincs érvényes belső hőmérséklet.")
        return

    try:
        indoor = float(indoor_raw)
    except ValueError:
        log.info(f"⚠️ Nem numerikus belső hőmérséklet: {indoor_raw}")
        return

    # --- Utolsó hőmérséklet ---
    last_temp_raw = state.get("input_number.last_temp")
    if last_temp_raw is None:
        last_temp = indoor
    else:
        try:
            last_temp = float(last_temp_raw)
        except ValueError:
            last_temp = indoor

    delta = indoor - last_temp
    if abs(delta) < 0.01:
        log.info("ℹ️ Nincs jelentős változás, tanulás kihagyva.")
        return

    # --- Fűtési / hűlési ráta (Exponential Moving Average) ---
    # !!! MÓDOSÍTVA: A delta szorzót 6-ról 12-re növeljük, mert 5 percenként fut (1/12 óra) !!!
    # Az EMA alfa értéke itt 0.1
    if delta > 0:
        prev_raw = state.get("input_number.heating_rate")
        prev = float(prev_raw) if prev_raw else 0
        new = (prev * 0.9) + (delta * 12 * 0.1) # <-- Szorzó 12!
        state.set("input_number.heating_rate", round(new, 3))
        log.info(f"🔥 Felfűtési ráta: {new:.3f} °C/óra")
    elif delta < 0:
        prev_raw = state.get("input_number.cooling_rate")
        prev = float(prev_raw) if prev_raw else 0
        new = (prev * 0.9) + (delta * 12 * 0.1) # <-- Szorzó 12!
        state.set("input_number.cooling_rate", round(new, 3))
        log.info(f"❄️ Hűlési ráta: {new:.3f} °C/óra")

    # --- Mentés ---
    state.set("input_number.last_temp", indoor)
    log.info(f"✅ Mentve last_temp = {indoor:.2f} °C")
