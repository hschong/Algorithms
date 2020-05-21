class DLL_Element:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev


class Order:
    def __init__(self):
        # Using dictionary(hash) for a better searching.
        self.start = None
        self.end = None
        self.order_dict = {}

    def order(self, id, data):
        if id in self.order_dict:
            print('The order for the id you entered already exists.')
            return False

        new_order = DLL_Element(data, None, None)
        self.order_dict[id] = new_order

        if self.start == None:
            self.start = new_order
            self.end = new_order
        else:
            self.end.next = new_order
            new_order.prev = self.end
            self.end = new_order

    def remove_order(self, id):
        if id not in self.order_dict:  # Zero order in dict
            print('Not found with id')
            return None
        else:
            order = self.order_dict[id]
            if order == self.start and order == self.end:
                # only 1 order in dict
                self.start = None
                self.end = None

            # orders in dict >= 2
            if order == self.start:
                self.start = order.next
                order.next.prev = None
            elif order == self.end:
                self.end = order.prev
            else:
                order.prev.next = order.next
                order.next.prev = order.prev

            del self.order_dict[id]

    def get_order(self, id):
        if id not in self.order_dict:
            print('id {} is invalid'.format(id))
            return None
        else:
            return self.order_dict[id]

    def print_details(self, order):
        if order != None:
            print(order.data)


def main():
    manager = Order()

    manager.order(1, 'abc')
    manager.order(2, '가나다')
    manager.order(3, '123')
    manager.order(2, '!@#')

    manager.print_details(manager.get_order(1))
    manager.print_details(manager.get_order(2))
    manager.print_details(manager.get_order(3))
    manager.remove_order(1)
    manager.print_details(manager.get_order(1))
    manager.print_details(manager.get_order(2))
    manager.print_details(manager.get_order(3))


if __name__ == "__main__":
    main()
