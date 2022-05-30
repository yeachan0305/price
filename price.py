def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체
    
    with open(f'data/{shop_file}') as f:
        cnt = 0
        for line in f:
            if cnt == 0 or cnt == 1:
                cnt += 1
            else:
                A, B = line.split()
                shop_dict[A] = B[:-1]

    return shop_dict
  
def item_price(shop_file, item):
    
    shoplist = shopping(shop_file)
    return shoplist[item]
