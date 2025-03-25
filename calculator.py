def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.
    
    Returns:
    float: The final price after applying the discount, or the original price if discount is less than 20%.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount)
    print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")