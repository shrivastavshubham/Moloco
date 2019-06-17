from data_parse.json_load import JsonParse
import sys, os
from collections import defaultdict
sys.path.append(os.path.abspath(os.path.join('..', 'data_parse')))
json = JsonParse()


class Products:
    def popular_product_by_purchases(self):
        ##############################################################
        #Returns product(s) bought by maximum num of user: type list[]
        ##############################################################
        product_user_id = defaultdict(set)
        max_purchase = 0 ; res = []
        for line in json.get():
            product = line['product_id']
            user_id = line['user_id']
            product_user_id[product].add(user_id)
        for elem in product_user_id:
            val = len(product_user_id[elem])
            if val > max_purchase:
                res = [elem]
                max_purchase = val
            elif val == max_purchase:res.append(elem)
        return res




    def popular_product_by_quantity(self):
        ###########################################################
        #returns product(s) bought in largest quantity: type list[]
        ###########################################################
        product_quantity = {}
        max_quantity = 0
        res = []
        for line in json.get():
            product = line['product_id']
            quantity = line['quantity']
            product_quantity[product] = product_quantity.get(product,0)+quantity
        for elem in product_quantity:
            val = product_quantity[elem]
            if val > max_quantity:
                res = [elem]
                max_quantity = val
            elif val == max_quantity:
                res.append(elem)
        return res


product_obj = Products()
print(product_obj.popular_product_by_purchases())
print(product_obj.popular_product_by_quantity())
