3 Million Instacart Orders, Open Sourced (Instacart_2017_05_01)
The dataset is provided as-is for non-commercial use and is subject to our Terms and Conditions here:

https://gist.github.com/jeremystan/582eba13d6ee27ed465c43dc78934700. 

Download dataset (~200MB)

Data description: 
InstaCart Data is provided in 6 csv files. The order.csv links the orders and users with additional time details. 

orders.csv (3.4 million rows, 206k users, 7 columns):

order_id: unique order identifier
user_id:  unique customer identifier
eval_set: which evaluation set this order belongs in (see SET described below)
order_number: the order sequence number for this user (1 = first, n = nth)
order_dow: the day of the week the order was placed on starting at 0 going to 6
order_hour_of_day: the hour of the day the order was placed on starting a 0 to 23
days_since_prior: days since the last order. Maximum at 30 days (with NaNs for customer's first order)

Products.csv (50k rows):

product_id: product identifier
product_name: name of the product
aisle_id: foreign key ; link to aisles.csv
department_id: foreign key ; link to departments.csv



aisles.csv (134 rows):

aisle_id: aisle identifier
aisle: the name of the aisle

departments.csv (21 rows):

department_id: department identifier
department: the name of the department
order_products__SET (30m+ rows):

order_products_prior.csv and orders_products_train.csv:

order_id: foreign key ; link to orders.csv
product_id: foreign key ; link to products.csv
add_to_cart_order: order in which each product was added to cart
reordered: 1 if this product has been ordered by this user in the past, 0 otherwise
where SET is one of the four following evaluation sets (eval_set in orders):


"prior": orders prior to that users most recent order (~3.2m orders)
"train": training data supplied to participants (~131k orders)
"test": test data reserved for machine learning competitions (~75k orders)


Citation:

“The Instacart Online Grocery Shopping Dataset 2017”, Accessed from https://www.instacart.com/datasets/grocery-shopping-2017 on 17 Jan 2018"

If you have questions about this dataset, you can reach out to Instacart at open.data@instacart.com

Full blog post can be found on Tech @ Instacart
