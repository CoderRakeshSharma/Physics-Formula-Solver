import math
def mechanics_menu():
    print("\nMechanics Subtopics:")
    print("1. Newton's Second Law (F = m * a)")
    print("2. Kinetic Energy (KE = 0.5 * m * v^2)")
    print("3. Gravitational Potential Energy (PE = m * g * h)")
    choice = input("Choose an option (1-3): ")

    if choice == '1':
        m = float(input("Enter mass (kg): "))
        a = float(input("Enter acceleration (m/s^2): "))
        F = m * a
        print(f"Force = {F} N")
    elif choice == '2':
        m = float(input("Enter mass (kg): "))
        v = float(input("Enter velocity (m/s): "))
        KE = 0.5 * m * v ** 2
        print(f"Kinetic Energy = {KE} J")
    elif choice == '3':
        m = float(input("Enter mass (kg): "))
        h = float(input("Enter height (m): "))
        g = 9.8  # gravitational acceleration
        PE = m * g * h
        print(f"Potential Energy = {PE} J")
    else:
        print("Invalid option")

def electricity_menu():
    print("\nElectricity Subtopics:")
    print("1. Ohm's Law (V = I * R)")
    print("2. Electric Power (P = V * I)")
    choice = input("Choose an option (1-2): ")

    if choice == '1':
        I = float(input("Enter current (A): "))
        R = float(input("Enter resistance (ohm): "))
        V = I * R
        print(f"Voltage = {V} V")
    elif choice == '2':
        V = float(input("Enter voltage (V): "))
        I = float(input("Enter current (A): "))
        P = V * I
        print(f"Power = {P} W")
    else:
        print("Invalid option")

def thermodynamics_menu():
    print("\nThermodynamics Subtopics:")
    print("1. Heat Transfer (Q = m * c * ΔT)")
    choice = input("Choose an option (1): ")

    if choice == '1':
        m = float(input("Enter mass (kg): "))
        c = float(input("Enter specific heat capacity (J/kg°C): "))
        delta_T = float(input("Enter temperature change (°C): "))
        Q = m * c * delta_T
        print(f"Heat Transfer = {Q} J")
    else:
        print("Invalid option")

def optics_menu():
    print("\nOptics Subtopics:")
    print("1. Lens Formula (1/f = 1/v - 1/u)")
    choice = input("Choose an option (1): ")

    if choice == '1':
        v = float(input("Enter image distance v (cm): "))
        u = float(input("Enter object distance u (cm): "))
        if v == u:
            print("Invalid input: image and object distance cannot be the same.")
        else:
            f = 1 / ((1/v) - (1/u))
            print(f"Focal Length = {f} cm")
    else:
        print("Invalid option")

def motion_menu():
    print("\nMotion Subtopics:")
    print("1. Final velocity (v = u + at)")
    print("2. Distance (s = ut + 0.5at^2)")
    choice = input("Choose an option (1-2): ")

    if choice == '1':
        u = float(input("Enter initial velocity (m/s): "))
        a = float(input("Enter acceleration (m/s^2): "))
        t = float(input("Enter time (s): "))
        v = u + a * t
        print(f"Final Velocity = {v} m/s")
    elif choice == '2':
        u = float(input("Enter initial velocity (m/s): "))
        a = float(input("Enter acceleration (m/s^2): "))
        t = float(input("Enter time (s): "))
        s = u * t + 0.5 * a * t ** 2
        print(f"Distance = {s} m")
    else:
        print("Invalid option")

def waves_menu():
    print("\nWaves Subtopics:")
    print("1. Wave Speed (v = f * λ)")
    choice = input("Choose an option (1): ")

    if choice == '1':
        f = float(input("Enter frequency (Hz): "))
        wavelength = float(input("Enter wavelength (m): "))
        v = f * wavelength
        print(f"Wave Speed = {v} m/s")
    else:
        print("Invalid option")

def modern_physics_menu():
    print("\nModern Physics Subtopics:")
    print("1. Energy of Photon (E = h * f)")
    choice = input("Choose an option (1): ")

    if choice == '1':
        h = 6.626e-34  # Planck's constant
        f = float(input("Enter frequency (Hz): "))
        E = h * f
        print(f"Energy = {E} J")
    else:
        print("Invalid option")

def fluids_menu():
    print("\nFluid Mechanics Subtopics:")
    print("1. Pressure (P = F / A)")
    choice = input("Choose an option (1): ")

    if choice == '1':
        F = float(input("Enter force (N): "))
        A = float(input("Enter area (m^2): "))
        P = F / A
        print(f"Pressure = {P} Pa")
    else:
        print("Invalid option")

def magnetism_menu():
    print("\nMagnetism Subtopics:")
    print("1. Magnetic Force (F = q * v * B * sinθ)")
    choice = input("Choose an option (1): ")

    if choice == '1':
        q = float(input("Enter charge (C): "))
        v = float(input("Enter velocity (m/s): "))
        B = float(input("Enter magnetic field strength (T): "))
        theta = float(input("Enter angle between v and B (degrees): "))
        
        F = q * v * B * math.sin(math.radians(theta))
        print(f"Magnetic Force = {F} N")
    else:
        print("Invalid option")

def relativity_menu():
    print("\nRelativity Subtopics:")
    print("1. Time Dilation (t' = t / √(1 - v^2/c^2))")
    choice = input("Choose an option (1): ")

    if choice == '1':
        t = float(input("Enter proper time (s): "))
        v = float(input("Enter velocity (m/s): "))
        c = 3e8
        
        if v >= c:
            print("Velocity must be less than the speed of light.")
        else:
            t_prime = t / math.sqrt(1 - (v ** 2) / (c ** 2))
            print(f"Dilated Time = {t_prime} s")
    else:
        print("Invalid option")

def main():
    while True:
        print("\nPhysics Formula Solver")
        print("1. Mechanics")
        print("2. Electricity")
        print("3. Thermodynamics")
        print("4. Optics")
        print("5. Motion")
        print("6. Waves")
        print("7. Modern Physics")
        print("8. Fluid Mechanics")
        print("9. Magnetism")
        print("10. Relativity")
        print("11. Exit")
        topic = input("Select a topic (1-11): ")

        if topic == '1':
            mechanics_menu()
        elif topic == '2':
            electricity_menu()
        elif topic == '3':
            thermodynamics_menu()
        elif topic == '4':
            optics_menu()
        elif topic == '5':
            motion_menu()
        elif topic == '6':
            waves_menu()
        elif topic == '7':
            modern_physics_menu()
        elif topic == '8':
            fluids_menu()
        elif topic == '9':
            magnetism_menu()
        elif topic == '10':
            relativity_menu()
        elif topic == '11':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
