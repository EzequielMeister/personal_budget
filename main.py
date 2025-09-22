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

        match opcion:
            case "1":
                desc = input("Descripción del ingreso: ")
                monto = float(input("Monto: "))
                budget.add_income(desc, monto)
                print("✔️ Ingreso agregado.")

            case "2":
                desc = input("Descripción del gasto: ")
                monto = float(input("Monto: "))
                categoria = input("Categoría (comida, transporte, entretenimiento, etc.): ")
                budget.add_expense(desc, monto, categoria)
                print("✔️ Gasto agregado.")

            case "3":
                budget.show_transactions()

            case "4":
                budget.show_summary()

            case "5":
                print("👋 ¡Hasta luego!")
                break

            case _:
                print("⚠️ Opción inválida.")

if __name__ == "__main__":
    menu()
