# somehow can't use this slope calculation

# def get_slope(x,y):
#     xy = [a*b for a,b in zip(x, y)]
#     n = len(x)
#     x_2 = [a * a for a in x]
#     num = n * sum(xy) - sum(x) * sum(y)
#     denom = n * sum(x_2) * sum(x)**2
#     return num/denom

def get_pred(x,y):
    m_x   = sum(x)/len(x)
    m_y = sum(y)/len(y)
    slope = get_slope(x,y)
    intercept = m_y - (slope * m_x)
    predict = slope * 10 + intercept
    return predict


# this one works
def get_slope(x,y):
    m_x = sum(x)/len(x)
    m_y = sum(y)/len(y)
    num = sum([(xi - m_x) * (yi - m_y) for xi, yi in zip(x,y)])
    denom = sum([(xi-m_x)**2 for xi in x])
    return num/denom    



if __name__ == '__main__':
    physics_score = [15 , 12 , 8 , 8 , 7 , 7 , 7 , 6 , 5 , 3]
    history_score = [10 , 25 , 17 , 11 , 13 , 17 , 20 , 13 , 9 , 15]
    prediction = get_pred(physics_score, history_score)
    print(f'{prediction:.2f}')
