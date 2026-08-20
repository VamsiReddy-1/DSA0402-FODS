prices = [50, 120, 80]

quantities = [2, 1, 3]

discount_rate = 10      # 10%
tax_rate = 5            # 5%

subtotal = 0

for i in range(len(prices)):
    subtotal += prices[i] * quantities[i]

discount = subtotal * (discount_rate / 100)

amount_after_discount = subtotal - discount

tax = amount_after_discount * (tax_rate / 100)

final_amount = amount_after_discount + tax

print("Subtotal =", subtotal)
print("Discount =", discount)
print("Tax =", tax)
print("Final Amount =", final_amount)
