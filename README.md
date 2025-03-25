# Calculate Discount

## Overview
This Python script defines a function `calculate_discount(price, discount_percent)` that calculates the final price after applying a discount. If the discount percentage is 20% or higher, the discount is applied; otherwise, the original price is returned.

## Features
- Accepts user input for the original price and discount percentage.
- Applies the discount only if it is 20% or higher.
- Returns the original price if the discount is less than 20%.
- Ensures proper error handling for invalid input.

## Usage
1. Run the script.
2. Enter the original price of the item when prompted.
3. Enter the discount percentage.
4. The final price after applying the discount (if applicable) will be displayed.

## Example
```
Enter the original price of the item: 100
Enter the discount percentage: 25
The final price after applying the discount is: $75.00
```

If the discount is below 20%:
```
Enter the original price of the item: 100
Enter the discount percentage: 15
The final price after applying the discount is: $100.00
```

## Error Handling
- If non-numeric values are entered, the script will prompt the user to enter valid numeric values.

## Requirements
- Python 3.x

## License
This script is open-source and can be modified as needed.
