import json
from utils import load_data, save_data

class Budget:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = load_data(file_name)

    def add_income(self, description, amount):
        self.data["incomes"].append({"description": description, "amount": amount})
        save_data(self.file_name, self.data)

    def add_expense(self, description, amount, category):
        self.data["expenses"].append({"description": description, "amount": amount, "category": category})
        save_data(self.file_name, self.data)

    def show_transactions(self):
        print("\n--- Ingresos ---")
        for i, inc in enumerate(self.data["incomes"], 1):
            print(f"{i}. {inc['description']}: ${inc['amount']:.2f}")

        print("\n--- Gastos ---")
        for i, exp in enumerate(self.data["expenses"], 1):
            print(f"{i}. {exp['description']} ({exp['category']}): ${exp['amount']:.2f}")

    def show_summary(self):
        total_income = sum(inc["amount"] for inc in self.data["incomes"])
        total_expense = sum(exp["amount"] for exp in self.data["expenses"])
        saldo = total_income - total_expense

        print("\n📊 Resumen Mensual")
        print(f"Total ingresos: ${total_income:.2f}")
        print(f"Total gastos: ${total_expense:.2f}")
        print(f"Saldo: ${saldo:.2f}")

        # Distribución de gastos por categoría
        categorias = {}
        for exp in self.data["expenses"]:
            categorias[exp["category"]] = categorias.get(exp["category"], 0) + exp["amount"]

        print("\nGastos por categoría:")
        for cat, monto in categorias.items():
            porcentaje = (monto / total_expense * 100) if total_expense > 0 else 0
            print(f"{cat}: ${monto:.2f} ({porcentaje:.1f}%)")
