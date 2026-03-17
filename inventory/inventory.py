import os
import json

# Utilities
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Files
def save_data(products, file="products.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def load_data(file="products.json"):
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Save sales for report
def save_sales(sales, file="sales.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(sales, f, ensure_ascii=False, indent=4)

def load_sales(file="sales.json"):
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Load product list
def list_products(p):
    sorted_products = sorted(p, key=lambda product: (product['name']).lower())
    for product in sorted_products:
        print(product)
    input('\nPress enter to continue...')

# Ask user if they want to continue
def want_to_continue():
    while True:
        clear_screen()
        resp = input('Do you want to continue [Y/N]? ').upper()
        if resp not in ('Y', 'N'):
            print('Type Y for yes and N for no.')
            input('\nPress enter to continue...')
            continue
        return resp == 'Y'

# Add new products
def add_new_products(p):  # p = products
    while True:
        while True:
            clear_screen()
            product_name = input('Enter product name [0 to cancel]: ')
            if product_name == "":
                print('Name cannot be empty')
                input('Press enter to continue...')
                continue
            if product_name == '0':
                return
            for product in p:
                if product['name'] == product_name:
                    print('Product already exists...')
                    input('Press enter to continue...')
                    return
            if product_name.replace(' ', '').isalpha():
                break
            elif product_name.isdigit():
                print('⚠️  Invalid product name.')
                input('Press enter to continue...')
                continue

        while True:
            clear_screen()
            try:
                price = float(input('Enter product price: '))
                break
            except ValueError:
                print('⚠️  Invalid price.')
                input('Press enter to continue...')
                continue

        while True:
            clear_screen()
            try:
                qty = int(input('Enter product quantity: '))
                if qty < 0:
                    print('⚠️  Cannot be negative.')
                    input('Press enter to continue')
                else:
                    break
            except ValueError:
                print('⚠️  Invalid value.')
                input('Press enter to continue...')
                continue
        
        data = {'name': product_name, 'price': price, 'quantity': qty}

        p.append(data)
        p.sort(key=lambda product: product['name'])
        save_data(p, file="products.json")
        print(f'💾  "{product_name}" saved successfully!')
        input('\nPress enter to continue...')
        if not want_to_continue():
            return

# Update products
def update_products(p):
    while True:
        clear_screen()
        product_name = input('Enter product name: ').strip()
        exists = False
        for product in p:
            if product['name'] == product_name:
                exists = True
                print(f'[1] Add stock')
                print(f'[2] Remove stock')
                print(f'[3] Exit')
                try:
                    option = int(input('\nChoose an option: '))
                    if option < 1 or option > 3:
                        print('Invalid option')
                    elif option == 1:
                        qty = int(input('Enter quantity [0 to cancel]: '))
                        if qty < 0:
                            print('⚠️  Cannot be negative.')
                            input('\nPress enter to continue...')
                        elif qty == 0:
                            continue
                        else:
                            product['quantity'] += qty
                            print(f'Stock updated "{product["name"]}": {product["quantity"]}')
                            save_data(p)
                            input('\nPress enter to continue...')
                    elif option == 2:
                        qty = int(input('Enter quantity [0 to cancel]: '))
                        if qty < 0:
                            print('⚠️  Cannot be negative.')
                            input('\nPress enter to continue...')
                        elif qty == 0:
                            continue
                        else:
                            current_qty = product['quantity']
                            product['quantity'] -= qty
                            if product['quantity'] >= 0:
                                print(f'Available stock "{product["name"]}": {product["quantity"]}')
                                save_data(p)
                                input('\nPress enter to continue...')
                            if product['quantity'] < 0:
                                product['quantity'] = current_qty
                                print('⚠️  Cannot be negative.')
                                print(f'Stock updated "{product["name"]}": {product["quantity"]}')
                                input('\nPress enter to continue...')
                except ValueError:
                    print('⚠️  Invalid option.')
                    input('\nPress enter to continue...')
        if not exists:
            print('⚠️  Product does not exist.')
            input('\nPress enter to continue...')
            clear_screen()
        if not want_to_continue():
            return

# Register a sale
def register_sale(p):
    product_name = input('Enter product name: ')
    exists = False
    for product in p:
        if product['name'] == product_name:
            exists = True
            qty_sale = int(input(f'Enter quantity to sell for "{product_name}": '))
            if product['quantity'] > 0:
                stock = product['quantity']
                if qty_sale > product['quantity']:
                    print(f'⚠️  Not enough stock.')
                    print(f'Stock available: {stock} units.')
                    input('\nPress enter to continue...')
                else:
                    product['quantity'] -= qty_sale
                    total_sale = product['price'] * qty_sale
                    sale_record = {
                        'name': product['name'],
                        'qty_sold': qty_sale,
                        'total': total_sale
                    }
                    sales.append(sale_record)
                    save_sales(sales)
                    save_data(p)
                    print('=-=-' * 15)
                    print(f'{"SALE REPORT":^60}')
                    print('=-=-' * 15)
                    print(f'Total sale: {total_sale:.2f}€')
                    print(f'Updated stock: {product["quantity"]} units.')
                    print('=-=-' * 15)
                    input('\nPress enter to continue...')
    if not exists:
        print(f'⚠️  "{product_name}" is not in stock.')
        input('\nPress enter to continue...')
        return

# Show report
def show_report(sales, p):
    clear_screen()
    if not sales:
        print('No sales at the moment.')
        input('\nPress enter to continue...')
    print('[1] Sales report')
    print('[2] Stock below 5 units')
    print('[3] Exit')
    while True:
        try:
            option = int(input('\nChoose an option: '))
            if option < 1 or option > 3:
                print('Invalid option')
                continue
            else:
                break
        except ValueError:
            print('⚠️  Invalid option.')
            continue
    
    if option == 1:
        print('=-=-' * 15)
        print(f'{"GENERAL SALES REPORT":^60}')
        print('=-=-' * 15)
        for i, sale in enumerate(sales, start=1):
            print(f'{"":^28}{i}th sale')
            print(f' Name: {sale["name"]}')
            print(f' Quantity: {sale["qty_sold"]}')
            print(f' Total: {sale["total"]:.2f}€')
            print('=-=-' * 15)
        input('\nPress enter to continue...')
    elif option == 2:
        print('=-=-' * 15)
        print(f'{"LOW STOCK":^60}')
        print('=-=-' * 15)
        low_stock = False
        for product in p:
            if product['quantity'] < 5:
                print(f'Name: {product["name"]}')
                print(f'Quantity: {product["quantity"]}')
                low_stock = True
                print('=-=-' * 15)
        input('\nPress enter to continue...')
        if not low_stock:
            print('✅  All stock is above 5 units.')
            input('\nPress enter to continue...')
    else:
        return

# Product & sales lists
products = load_data()
sales = load_sales()

def menu():
    print('[1] Add new products')
    print('[2] List products')
    print('[3] Update stock')
    print('[4] Register sales')
    print('[5] Show report')
    print('[6] Exit')

# Main program loop
while True:
    while True:
        clear_screen()
        menu()
        try:
            option = int(input('\nChoose an option: '))
            if option < 1 or option > 6:
                print('⚠️  Invalid option.')
                input('\nPress enter to continue...')
                continue
            else:
                break
        except ValueError:
            print('⚠️  Invalid option.')

    match option:
        case 1:
            add_new_products(products)
        case 2:
            list_products(products)
        case 3:
            update_products(products)
        case 4:
            register_sale(products)
        case 5:
            show_report(sales, products)
        case 6:
            break

print(products)