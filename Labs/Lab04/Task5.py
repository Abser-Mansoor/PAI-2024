class Restaurant :
    menu_items = []
    customer_orders = []
    book_tables = []
    def __init__(self, menu, orders, tables) :
        self.menu_items = menu
        self.customer_orders = orders
        self.book_tables = tables

    def Add_Item_To_Menu(self, item) :
        if (item in self.menu_items) :
            print("Item exists in menu already\n")
            return
        self.menu_items.append(item)
    
    def Book_Table(self, table) :
        if (table in self.book_tables) :
            print("Table is already booked\n")
            return
        self.book_tables.append(table)
    
    def Customer_Order(self, order) :
        if (order in self.customer_orders) :
            print("Order is already being processed\n")
            return
        self.customer_orders.append(order)

    def Print_Menu(self) :
        print([item for item in self.menu_items])

    def Print_Booked_Tables(self) :
        print([item for item in self.book_tables])
        

    def Print_Customer_Orders(self) :
        print([item for item in self.customer_orders])

Restaurant1 = Restaurant(["Lamb Chops"], ["2 Servings of Lamb Chops"], ["Table 1"])
Restaurant1.Add_Item_To_Menu("Ice Cream")
Restaurant1.Book_Table("Table 2")
Restaurant1.Customer_Order("3 Cones of Vanilla Ice Cream")
Restaurant1.Print_Menu()
Restaurant1.Print_Booked_Tables()
Restaurant1.Print_Customer_Orders()
