def verify_card_number(card):
    card = card.replace(" ", "")
    card = card.replace("-","")
    if not card.isdigit():
        return False
    total = 0
    reverse_digits = card[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)

        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9

        total += n

    if total % 10 == 0:
        return ('VALID!')
    else:
        return ('INVALID!')

print(verify_card_number("4111-1111-1111-1111"))

 
