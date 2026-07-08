def join_customers_orders(customer_df, order_df):

    """ Joins customers with order. """

    return customer_df.join(
        order_df,
        on="customer_id",
        how="inner"
    )



def join_order_items(order_df, order_item_df):

    """Joins orders with order_items"""

    return order_df.join(
        order_item_df,
        on="order_id",
        how="inner"

    )



def join_products(order_item_df, product_df):

    """Joins ordered items with products"""

    return order_item_df.join(
        product_df,
        on="product_id",
        how="inner"
    )



def join_payments(order_df, payment_df):

    """Joins orders with payments."""

    return order_df.join(
        payment_df,
        on="order_id",
        how="inner"
    )


def create_sales_dataframe(
        customer_df,
        order_df,
        order_item_df,
        product_df,
        payment_df

):
    
    """Create an analytical data frame"""

    customer_orders_df = join_customers_orders(customer_df, order_df)

    order_items_df = join_order_items(customer_orders_df, order_item_df)

    sales_df = join_products(order_items_df, product_df)

    sales_df = join_payments(sales_df, payment_df)


    return sales_df



