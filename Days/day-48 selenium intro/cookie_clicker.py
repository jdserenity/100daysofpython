from selenium import webdriver; from selenium.webdriver.common.by import By; from selenium.webdriver.support.wait import WebDriverWait; from selenium.webdriver.support import expected_conditions as EC;
from database import products;

def main():
    options = webdriver.ChromeOptions(); options.add_experimental_option('detach', True); 

    d = webdriver.Chrome(options=options); d.get('https://orteil.dashnet.org/cookieclicker/'); 

    game_setup(d)

    game_loop(d)

    print('game ended')
    d.quit()


def game_setup(d):
    try: WebDriverWait(d, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'langSelectButton'))).click() # select language 
    except: print('lang select elem not found')

    count = 0
    while(count != 500):
        try:
            WebDriverWait(d, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cc_btn_accept_all'))).click() # accept cookies
            break
        except: count += 1

    d.switch_to.frame('aswift_1')
    count = 0
    while(count != 500):
        try:
            WebDriverWait(d, 10).until(EC.presence_of_element_located((By.ID, 'cbb'))).click() # close ad
            break
        except: count+=1
    d.switch_to.default_content()
        
    for i in range(10):
        try: d.find_element(By.CSS_SELECTOR, '#notes .close').click()
        except: pass


def game_loop(d):
    input()
    count = 0
    while(count <= 10000000):
        update_product_list(d); close_notification(d)

        d.find_element(By.ID, 'bigCookie').click()

        stats = get_cookie_stats(d); count = stats['cookie_count']; # print('cookies clicked: ', count)

        if stats['cookie_count'] % 20 == 0:
            upgrades = d.find_elements(By.CLASS_NAME, 'upgrade')
            for upgrade in upgrades:
                if 'enabled' in upgrade.get_attribute('class'):
                    upgrade.click()

                    # d.find_element(By.ID, 'statsButton').click()
                    # count = 0
                    # while(count != 500):
                    #     try:
                    #         upgrade_text = WebDriverWait(d, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#statsUpgrades.listing'))).text
                    #         input()
                    #         break
                    #     except: count += 1; print('stats upgrade page not found, attempt:', count)
                    
            choose_product(d, stats)
            

            if stats['cookie_count'] > price:
                d.find_element(By.ID, 'product' + str(best_cps['index'])).click()
                print(f'the best product to buy at that time was {products[best_cps['index']]} at {best_cps['dollar_per_cps']} cookies per cps')


def close_notification(d):
    try: d.find_element(By.CSS_SELECTOR, '#notes .close').click()
    except: pass


def get_cookie_stats(d):
    try:
        cookie_count = d.find_element(By.ID, 'cookies').text.split(' ')[0]
        if ',' in cookie_count: cookie_count = cookie_count.replace(',', '')
        if '\\' in cookie_count: cookie_count = cookie_count.split('\\')[0]
        cookie_count = int(cookie_count)
    except: pass
    
    try:
        per_second = d.find_element(By.ID, 'cookies').text.split(':')[-1].strip()
        if ',' in per_second: per_second = per_second.replace(',', '')
        per_second = float(per_second)
    except: pass

    return {'cookie_count': cookie_count, 'per_second': per_second}


def update_product_list(d):
    global products

    for i in range(5):
        if 'unlocked' in d.find_element(By.ID, 'product' + str(i)).get_attribute('class'):
            cost = d.find_element(By.ID, f'productPrice{i}').text
            if ',' in cost: cost = cost.replace(',', '')

            products[i]['current_cost'] = int(cost)
            try: products[i]['owned'] = int(d.find_element(By.ID, f'productOwned{i}').text) # raises error if no product is owned
            except ValueError: pass
            products[i]['unlocked'] = True


def choose_product(d, stats):
    best_cps = find_best_dollar_per_cps(d)
    best_cps_product_price = products[best_cps['index']]['current_cost']

    for i in range(5):
        price = products[i]['current_cost']
        price_difference = price - stats['cookie_count']
    stats['per_second']


def find_best_dollar_per_cps(d):
    cps_list = []
    cps_0 = products[0]['current_cost']/products[0]['cps']; cps_list.append(cps_0)
    cps_1 = products[1]['current_cost']/products[1]['cps']; cps_list.append(cps_1)
    cps_2 = products[2]['current_cost']/products[2]['cps']; cps_list.append(cps_2)
    cps_3 = products[3]['current_cost']/products[3]['cps']; cps_list.append(cps_3)
    cps_4 = products[4]['current_cost']/products[4]['cps']; cps_list.append(cps_4)

    min_cps = min(cps_list)

    i = cps_list.index(min_cps)
    
    return {'dollar_per_cps': min_cps, 'index': i}


if __name__ == '__main__':
    main()