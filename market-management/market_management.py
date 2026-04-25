import os
import json

from datetime import datetime

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

class Customer(Person): #cliente
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self.customer_id = customer_id
        self.sale = []

    def add_sale(self, sale):
        self.sale.append(sale)

    def to_dict(self):
        return {
            "name": self._name,
            "age": self.age,
            "customer_id": self.customer_id
        }

    def __str__(self):
        return f"{self._name} {self.age} ({self.customer_id})"
    
class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role # cargo do funcionário (ex.: Caixa, Gerente, Repositor)
        self.sale = []

    def add_sale(self, sale):
        self.sale.append(sale)

    def to_dict(self):
        return {
            'name': self._name,
            'age': self.age,
            'role': self.role
        }
    
class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name #nome do produto
        self.price = price #Preço do produto
        self.stock_quantity = stock_quantity #Quantidade de estoque
    
    def reduce_stock(self, quantity): #reduzir estoque
        self.stock_quantity -= quantity

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'stock_quantity': self.stock_quantity
        }

class Cart: #carrinho de compras
    def __init__(self, customer):
        self.customer = customer
        self.product_with_quantity = []

    def add_product(self, product, quantity):
        self.product_with_quantity.append((product, quantity))

    def get_cart_total(self):
        return sum(product.price * quantity for product, quantity in self.product_with_quantity)

class Sale: #venda
    #Represents a completed purchase (Representa uma compra finalizada).
    def __init__(self, customer, employee, total, date):
        self.customer = customer
        self.employee = employee
        self.products = []
        self.total = total
        self.date = date

    def add_product(self,product, quantity):
        self.products.append((product, quantity))

class Market: # Manages the entire system” → Gerencia todo o sistema
    def __init__(self, name ):
        self.name = name
        self.list_products = []
        self.list_customers = []
        self.list_employees = []
        self.list_sales = []

    def add_product(self, product):
        self.list_products.append(product)
        
    def add_customer(self, customer):
        self.list_customers.append(customer)

    def add_employee(self, employee):
        self.list_employees.append(employee)

    def register_sales(self, sale):
        self.list_sales.append(sale)
                
        #adiciona a venda ao mercado
        #adiciona ao cliente
        #adiciona ao funcionário
        #reduz stock dos produtos
        
    def list_customer_purchase(self, customer):
        if not customer.sale:
            print("\n⚠️  This customer has no recorded purchases.")
            input("\nPress Enter to return to the menu...")
            return

        for i, sale in enumerate(customer.sale, start=1):
            print(f"\nSale: {i}. "
                f"\nDate: {sale.date} "
                f"\nEmployee: {sale.employee._name} | Role: {sale.employee.role}"
                f"\nTotal: {sale.total:,.2f}€"
                "\nProducts: "
                )
            
            for product, qty in sale.products:
                subtotal = product.price * qty
                print(f" - {product.name} x{qty} -> {subtotal:,.2f}€")

        input("\nPress Enter to return to the menu...")

    def list_employee_sales(self, employee):
        if not employee.sale:
            print("⚠️  This Employee has no recorded purchases.") # Este funcionário não possui compras registradas.
            input("\nPress Enter to return to the menu...")
            return
        
        for i, sale in enumerate(employee.sale, start=1):
            print(f"\nSale: {i}")
            print(f"Date: {sale.date}")
            print(f"Customer: {sale.customer._name}")
            print(f"Total: {sale.total:,.2f}£")
            print("\nProducts: ")

            for product, qty in sale.products:
                subtotal = product.price * qty
                print(f"{product.name} x{qty} -> {subtotal:,.2f}")
        input("\nPress Enter to return to the menu...")

    def list_low_stock(self, threshold):
        limpar_tela()
        print("")
        if not market.list_products:
            print("There are no products available in stock.")
        else:
            print("=== Products with Low Stock Levels ===\n")
            for product in market.list_products:
                if product.stock_quantity < threshold:
                    print(f"{product.name} -> qty: {product.stock_quantity}")
        input("\nPress Enter to return to the menu...")
        return



##########################################################################
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_FILE = os.path.join(BASE_DIR, 'data', 'products.json')
CUSTOMERS_FILE = os.path.join(BASE_DIR, 'data', 'customers.json')
EMPLOYEES_FILE = os.path.join(BASE_DIR, 'data', 'employees.json')
##########################################################################
def save_product(list_products):
    list_of_dicts = [p.to_dict() for p in list_products]

    os.makedirs(os.path.join(BASE_DIR, 'data'), exist_ok=True)

    with open(PRODUCTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(list_of_dicts, f, ensure_ascii=False, indent=4)

def load_products():
    if not os.path.exists(PRODUCTS_FILE):
        return []

    with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    list_products = []
    for item in data:
        product = Product(item['name'], item['price'], item['stock_quantity'])
        list_products.append(product)

    list_products = sorted(list_products, key=lambda p: p.name)
    return list_products

#################################################################################

def save_customers(list_customers):
    list_of_dicts = [c.to_dict() for c in list_customers]

    os.makedirs(os.path.join(BASE_DIR, 'data'), exist_ok=True)
    # for c in list_customers:
    #     list_of_dicts.append(c.to_dict())

    with open(CUSTOMERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(list_of_dicts, f, ensure_ascii=False, indent=4)

def load_customers():
    if not os.path.exists(CUSTOMERS_FILE):
        return []

    with open(CUSTOMERS_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    list_customers = []
    for item in data:
        customer = Customer(item["name"], item["age"], item["customer_id"])
        list_customers.append(customer)

    return list_customers

def save_employees(list_employees):
    list_of_dicts = [e.to_dict()  for e in list_employees]
    os.makedirs(os.path.join(BASE_DIR, 'data'), exist_ok=True)
    
    with open(EMPLOYEES_FILE, 'w', encoding='utf-8') as f:
        json.dump(list_of_dicts, f, ensure_ascii=False, indent=4)

def load_employees():
    if not os.path.exists(EMPLOYEES_FILE):
        return []

    with open(EMPLOYEES_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    list_employees = []
    for item in data:
        employee = Employee(item["name"], item["age"], item["role"])
        list_employees.append(employee)
    
    return list_employees
#--------------------------------------------------------#
#Creating instanse of the Market Class
market = Market('Super Market')
#--------------------------------------------------------#

#Load the products,employees and customers lists
market.list_products = load_products()
market.list_customers = load_customers()
market.list_employees = load_employees()
#--------------------------------------------------------#

# ============================
# 📋 MAIN PROGRAM
# ============================

while True:
    limpar_tela()

    print("\n====== MARKET SYSTEM ======")
    print("1 - Register product")
    print("2 - Register customer")
    print("3 - Register employee")
    print("4 - Register sale") #cart class
    print("5 - Listar compras de um cliente")
    print("6 - Listar vendas de um funcionário")
    print("7 - Listar produtos com baixo estoque")
    print("8 - Listar produtos do estoque")
    print("9 - Customer list")
    print("10 - Employees list")
    print("0 - Sair")

    try:
        option = int(input("\nChoose an option: "))
        if option < 0 or option > 10:
            print("⚠️  Invalid option")
            input("\nPress Enter to go back to the menu...")
            continue
        
    except ValueError:
        print("⚠️  Invalid option")
        continue

    match option:
        case 1:
            print("→ Register a product")
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            stock_quantity = int(input("Enter the product quantity: "))

            product = Product(name, price, stock_quantity)
            market.add_product(product)
            save_product(market.list_products)
            
        
        case 2:
            print("→ Cadastrar cliente")
            name_customer = input("Enter customer's name: ")
            age_customer = int(input("Enter customer's age: "))
            customer_id = input("Enter customer's ID: ")

            customer = Customer(name_customer, age_customer, customer_id)
            market.add_customer(customer)
            save_customers(market.list_customers)

        case 3:
            print("→ Cadastrar funcionário")
            name_employee = input("Enter employee's name: ")
            age_employee = int(input("Enter employee's age: "))
            role_employee = input("Enter employee's role: ")
            
            employee = Employee(name_employee, age_employee, role_employee)
            market.add_employee(employee)
            save_employees(market.list_employees)

        case 4:
            print("→ Registrar venda")
            limpar_tela()
            print("=-"*22)
            print(f"{'':<16}SELECT CUSTOMER")
            print("=-"*22)
            sort_customers = sorted(market.list_customers, key=lambda c: c._name)
            for i, c in enumerate(sort_customers, start=1):
                print(f"{i:>2}. {c._name:<18} | age: {c.age:>1} | ID: {c.customer_id:>1} ")

            opt_customer = int(input("\nselect the customer: "))
            
            if 1<= opt_customer <= len(sort_customers):
                chosen_customer = sort_customers[opt_customer -1]
                print(chosen_customer._name)

            limpar_tela()
            print("=-"*29)
            print(f"{'':<18} SELECT CASHIER")
            print("=-"*29)

            list_cachier = []
            for i, e in enumerate(market.list_employees, start=1):
                if e.role == "Cashier":
                    list_cachier.append(e)
                    # print(f"{i:>2}  {e._name:<18} | age: {e.age:>1} | role: {e.role} ")
            
            for i, e in enumerate(list_cachier, start=1):
                print(f"{i:>2}  {e._name:<18} | age: {e.age:>1} | role: {e.role} ")

            while True:
                try:
                    opt_employee = int(input("Select the employee: "))
                    if 1 <= opt_employee <= len(list_cachier):
                        chosen_employee = list_cachier[opt_employee -1]
                        break
                except ValueError:
                    print("⚠️  Invalid option")
                    continue

            print(f"Customer: {chosen_customer._name}")
            print(f"Employee: {chosen_employee._name}")
            input("\nPress Enter to continue...")

            #-------------------------------------------------------------------
            #creating instances of the class Cart
            cart = Cart(chosen_customer)
            #-------------------------------------------------------------------
            
            shopping_list = [] #lista de compras
            while True:
                limpar_tela()
            
                print("=-"*24)
                print(f"{'':<16}Record Sale") #Registrar venda
                print("=-"*24)

                sort_products = sorted(market.list_products, key=lambda p: p.name)
                for i, product in enumerate(sort_products, start=1):
                    print(f"{i:>2}. {product.name:<18} | Price: {product.price:>1.2f}€ | Qty: {product.stock_quantity:>1}")

                try:
                    print('\n⚠️ press 0 to cancel the operation.')
                    opt_product = int(input("Select the product: "))
                    
                    if 1 <= opt_product <= len(sort_products):
                        chosen_product = sort_products[opt_product - 1]
                        
                    elif opt_product == 0:
                        break
                    else:
                        continue

                except ValueError:
                    print("⚠️ invalid option.")
                    input("\nPress Enter to continue...")
                    continue

                while True:
                    limpar_tela()
                    print("=-"*19)
                    print(f"🛒  chosen product: {chosen_product.name} | qty: {chosen_product.stock_quantity}")
                    print("=-"*19)
                    try:
                        qty_product = int(input("\nEnter the product quantity: "))
                        if qty_product > chosen_product.stock_quantity:
                            print('\n⚠️ Quantity not available in stock')
                            input("\nPress Enter to continue...")
                            continue
                        else:
                            shopping_list.append((chosen_product, qty_product))
                            break
                    except ValueError:
                        print("⚠️ invalid option.")
                        input("\nPress Enter to continue...")
                        continue
            
            while True:
                confirm = input("Are you sure you want to register [Y/N]?: ").strip().upper()
                if confirm not in ("Y", "N"):
                    print("Type 'Y' for yes and 'N' for no.")
                    continue
                if confirm == 'N':
                    input("\nPress Enter to go to the menu...")
                    break
                else:
                    for product, quantity in shopping_list:
                        print(
                            f"{product.name:<15} | "
                            f"unit: {product.price:>1,.2f}€ | "
                            f"qty: {quantity:>1} | "
                            f"total: {(product.price * quantity):>4,.2f}€"
                        )
                        cart.add_product(product, quantity)

                    total = cart.get_cart_total()
                    print(" " * 39 + f"  total: {total:>3,.2f}€")
                    print('🎉 Successfully registered!')
                    input("\nPress Enter to continue...")
                    
                    sale = Sale(chosen_customer,
                                chosen_employee,
                                total,
                                date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            )
                    
                    for product, quantity in cart.product_with_quantity:
                        sale.add_product(product, quantity)

                    chosen_customer.add_sale(sale)
                    chosen_employee.add_sale(sale)
                    market.register_sales(sale)

                    for product, quantity in cart.product_with_quantity:
                        product.reduce_stock(quantity)
                    
                    save_product(market.list_products)
                    save_customers(market.list_customers)
                    save_employees(market.list_employees)
                    break

        case 5:
            print("→ Listar compras de um cliente")

            sort_customers = sorted(market.list_customers, key=lambda c: c._name)
            for i, customer in enumerate(sort_customers, start=1):
                print(f" {i}. {customer._name}")
                
            
            while True:
                try:
                    customer_choice = int(input("Select the customer: "))
                    if 1 <= customer_choice <= len(sort_customers):
                        chosen_customer = sort_customers[customer_choice - 1]
                        break

                except ValueError:
                    print("Invalid option.")

            market.list_customer_purchase(chosen_customer)
            # for c in market.list_sales:
            #     print(c.date)
            # input('bbciuabcibciu')
        case 6:
            print("→ Listar vendas de um funcionário")

            list_cachier = []
            for i, e in enumerate(market.list_employees, start=1):
                if e.role == "Cashier":
                    list_cachier.append(e)
                    # print(f"{i:>2}  {e._name:<18} | age: {e.age:>1} | role: {e.role} ")
            
            for i, e in enumerate(list_cachier, start=1):
                print(f"{i:>2} {e._name:<18} | age: {e.age:>1} | role: {e.role} ")

            while True:
                try:
                    employee_choice = int(input("Select the employee: "))
                    if 1 <= employee_choice <= len(list_cachier):
                        chosen_employee = list_cachier[employee_choice - 1]
                        break
                except ValueError:
                    print("⚠️  Invalid option")
                    continue
                
            market.list_employee_sales(chosen_employee)
    
        case 7:
            print("→ Listar produtos com baixo estoque")
            
            limpar_tela()
            print("=== Low Stock Products Report ===\n")
            while True:
                try:
                    threshold = int(input("Enter the stock limit: "))
                    market.list_low_stock(threshold)
                    break
                except ValueError:
                    print("⚠️  Invalid number.")
                    input("\nPress Enter to return to the menu...")
                    continue

        case 8:
            limpar_tela()
            print("=-"*24)
            print(f"{'':<16}INVENTORY LIST")
            print("=-"*24)
            sort_products = sorted(market.list_products, key=lambda p: p.name)
            for i, product in enumerate(sort_products, start=1):
                print(f"{i:>2}. {product.name:<18} | Price: {product.price:>1.2f}€ | Qty: {product.stock_quantity:>1}")
    
            input("\nPress Enter to go back to the menu...")

        case 9:
            limpar_tela()
            print("=-"*22)
            print(f"{'':<16}CUSTOMER LIST")
            print("=-"*22)
            list_customers = market.list_customers
            sort_customers = sorted(list_customers, key=lambda c: c._name)
            for i, c in enumerate(sort_customers, start=1):
                print(f"{i:>2}. {c._name:<18} | age: {c.age:>1} | ID: {c.customer_id:>1} ")

            input("\nPress Enter to go back to the menu...")

        case 10:
            limpar_tela()
            print("=-"*29)
            print(f"{'':<18} EMPLOYEES LIST")
            print("=-"*29)
            list_emploeyees = market.list_employees
            sort_employees = sorted(list_emploeyees, key=lambda e: e._name)
            for i, e in enumerate(sort_employees, start=1):
                print(f"{i:>2}  {e._name:<18} | age: {e.age:>1} | role: {e.role} ")

            input("\nPress Enter to go back to the menu...")
        case 0:
            print("Saindo...")
            break
        
        case _:
            print("Opção inválida.")
            input("\nPress Enter to go back to the menu...")

