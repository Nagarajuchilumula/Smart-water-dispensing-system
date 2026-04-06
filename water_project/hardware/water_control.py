# import requests
# import time

# # Unique ID of tap
# TAP_ID = "tap_1"

# # Your Django server IP
# SERVER = "http://192.168.1.100:8000"

# # Flow sensor calibration
# PULSES_PER_LITER = 450

# pulse_count = 0


# # -----------------------------
# # Valve Control Functions
# # -----------------------------
# def open_valve():
#     print("Valve Opened")
#     # GPIO HIGH (real hardware)


# def close_valve():
#     print("Valve Closed")
#     # GPIO LOW (real hardware)


# # -----------------------------
# # Flow Sensor Simulation
# # -----------------------------
# def read_flow_sensor():
#     global pulse_count
#     pulse_count += 50  # simulate pulses
#     return pulse_count


# # -----------------------------
# # MAIN LOOP
# # -----------------------------
# while True:
#     try:
#         print("Checking server...")

#         # 1. Ask Django for order
#         res = requests.get(f"{SERVER}/api/check/{TAP_ID}/")
#         data = res.json()

#         # 2. If order available
#         if "liters" in data:
#             target_liters = data["liters"]
#             order_id = data["order_id"]

#             print(f"Dispensing {target_liters} Liters")

#             # 3. Open valve
#             open_valve()

#             pulse_count = 0

#             # 4. Dispense water
#             while (pulse_count / PULSES_PER_LITER) < target_liters:
#                 read_flow_sensor()
#                 time.sleep(0.5)

#             # 5. Close valve
#             close_valve()

#             # 6. Inform Django
#             requests.post(f"{SERVER}/api/complete/{order_id}/")

#             print("Dispensing Completed")

#     except Exception as e:
#         print("Error:", e)

#     time.sleep(5)