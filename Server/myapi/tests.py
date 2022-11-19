def get_weight(number_of_share, closing_price): 
    weight = []
    for i in range(len(number_of_share)):
        weight.append(number_of_share[i] * closing_price[i])
    weight = [round(i/sum(weight), 3) for i in weight]

    return weight