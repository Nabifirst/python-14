
is_log = False
products = []
product_id = 1
current_user = None

def login():
    global is_log, current_user
    user = input('enter username --> ')
    passs = input('enter password --> ')
    with open('main.txt', 'r') as file:
        content = file.readlines()
        for i in content:
            n = i.split('-')
            if n[2] == user and n[3] == passs + '\n':
                is_log = True
                current_user = user
                return ''
    print('username or password incorrect !!')

def sign_up():
    fullname = input('enter fullname --> ')

    while True:
        t = True
        email = input('enter email --> ')
        with open('main.txt', 'r') as file:
            content = file.readlines()
            for i in content:
                n = i.split('-')
                if n[1] == email:
                    t = False
                    break
        if t == False:
            print("Email already exists. Try again.")
            continue
        break

    while True:
        b = True
        username = input('enter username --> ')
        with open('main.txt', 'r') as file:
            content = file.readlines()
            for i in content:
                n = i.split('-')
                if n[2] == username:
                    b = False
                    break
        if b == False:
            print("Username already exists. Try again.")
            continue
        break

    while True:
        passw = input('enter password --> ')
        pass2 = input('enter password once more --> ')
        if passw != pass2:
            print("Passwords do not match. Try again.")
            continue
        break

    return fullname, email, username, passw

def logout():
    global is_log, current_user
    is_log = False
    current_user = None
    print("You logged out successfully.")

def reset_pass():
    cheker=False
    ENTER=input("enter your email --> ")
    with open("main.txt","+r") as file:
        data=file.readlines()
        for i in data:
            spliti=i.split("-")
            if spliti[1]==ENTER:
                
                cheker=True
                pasword_new=input("enter new password --> ")
                spliti[-1]=pasword_new+"\n"
                arr=""
                for j in spliti:
                    arr+=j+"-"
                arr = arr[:-1] if arr.endswith("-") else arr
                with open("main.txt","w") as file2:
                    file2.write(arr)
                data.remove(i)
                for g in data:
                    with open("main.txt","a") as a:
                        a.write(g)
                
                with open("main.txt","r") as r:
                    print(r.readlines())
        if cheker==False:
            print("no")

def add_product():
    global product_id
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    quantity = input("Enter product quantity: ")
    product = {
        'id': product_id,
        'name': name,
        'price': price,
        'quantity': quantity,
        'user': current_user
    }
    products.append(product)
    product_id += 1
    print("Product added successfully.")

def get_all_products():
    found = False
    for p in products:
        if p['user'] == current_user:
            found = True
            print(f'''
ID       --> {p['id']}
Name     --> {p['name']}
Price    --> {p['price']}
Quantity --> {p['quantity']}
{'-'*20}
''')
    if not found:
        print("No products found.")

def get_product_by_id():
    idd = int(input("Enter product ID: "))
    for p in products:
        if p['id'] == idd and p['user'] == current_user:
            print(f'''
ID       --> {p['id']}
Name     --> {p['name']}
Price    --> {p['price']}
Quantity --> {p['quantity']}
''')
            return
    print("Product not found or not yours.")



def delete_product():
    idd = int(input("Enter product ID to delete: "))
    for p in products:
        if p['id'] == idd and p['user'] == current_user:
            products.remove(p)
            print("Product deleted.")
            return
    print("Product not found or not yours.")

def update_product():
    idd = int(input("Enter product ID to update: "))
    for p in products:
        if p['id'] == idd and p['user'] == current_user:
            p['name'] = input("Enter new product name: ")
            p['price'] = input("Enter new product price: ")
            p['quantity'] = input("Enter new product quantity: ")
            print("Product updated.")
            return
    print("Product not found or not yours.")


while True:
    if is_log == False:
        n = int(input('''\n
1 --> login
2 --> Sign up
3 --> reset password
choose your option --> '''))

        if n == 1:
            login()


        if n == 2:
            fullname, email, username, passw = sign_up()
            with open('main.txt', 'a') as file:
                file.write(f'{fullname}-{email}-{username}-{passw}\n')
            print('u signed in successfully')

        if n == 3:
            reset_pass()
        
        if n == 4:
            break

    else:
        n = int(input('''\nYou are logged in
1 --> Add product
2 --> Get all my products
3 --> Get my product by ID
4 --> Update my product
5 --> Delete my product
0 --> Logout
choose your option --> '''))

        if n == 0:
            logout()
        if n == 1:
            add_product()
        if n == 2:
            get_all_products()
        if n == 3:
            get_product_by_id()
        if n == 4:
            update_product()
        if n == 5:
            delete_product()
