# Initial stock of medicine
stock = 100
# Minimum threshold for reordering
threshold = 10
# Quantity to reorder
order_quantity = 100

# Function to simulate checking and reordering medicine
def check_and_order_medicine(stock):
    while True:
        # Simulating the consumption of medicine
        medicine_used = int(input("Enter the amount of medicine used (0 to exit): "))
        
        if medicine_used == 0:
            print("Exiting the system.")
            break
        
        # Update the stock after usage
        stock -= medicine_used
        
        # Check if stock is below the threshold
        if stock < threshold:
            print(f"Stock is below {threshold}. Ordering {order_quantity} more medicine.")
            stock += order_quantity  # Reorder medicine
        else:
            print(f"Stock is sufficient. Current stock: {stock}")

# Run the function
check_and_order_medicine(stock)