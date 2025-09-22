from budget import Budget

def menu():
    print("=== 💰 Simulador de Economía Personal ===")
    budget = Budget("data.json")

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar ingreso")
        print("2. Agregar gasto")
        print("3. Ver transacciones")
        print("4. Ver resumen mensual")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            desc = input("Descripción del ingreso: ")
            monto = float(input("Monto: "))
            budget.add_income(desc, monto)
            print("✔️ Ingreso agregado.")

        elif opcion == "2":
            desc = input("Descripción del gasto: ")
            monto = float(input("Monto: "))
            categoria = input("Categoría (comida, transporte, entretenimiento, etc.): ")
            budget.add_expense(desc, monto, categoria)
            print("✔️ Gasto agregado.")

        elif opcion == "3":
            budget.show_transactions()

        elif opcion == "4":
            budget.show_summary()

        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    menu()
