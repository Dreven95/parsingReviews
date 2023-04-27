import requestsfrom bs4 import BeautifulSoup
url = "https://otziv-otziv.ru/katalog/headphones/sennheiser-naushniki/sennheiser-cx-300-ii-otzyvy.html"request = requests.get(url)
bs = BeautifulSoup(request.text, 'lxml')productName = bs.find('h1')
print(productName.get_text())review = bs.findAll('div', 'container-reviews collapsible collapsed')
# reviewAuthor = review.findAll('span', 'user')# reviewDate = review.findAll('span', 'date')
# reviewStars = review.find('div', 'stars-container')['title']#
# reviewText = review.findAll('p')
# print("Author: ", reviewAuthor)
# print("Date: ", reviewDate)# print("Stars: ", reviewStars)
# for elem in reviewAuthor:
#     print(elem.get_text())#
# for elem in reviewText:#     print(elem)
for biba in review:
    reviewAuthor = biba.find('span', 'user')
    reviewDate = biba.find('span', 'date')
    reviewStars = biba.find('div', 'stars-container')['title']
    print("Author: ", reviewAuthor.get_text())
    print("Date: ", reviewDate.get_text())
    # print("Stars: ", reviewStars.get_text())
    reviewText = biba.findAll('p')
        for elem in biba:
            print(elem.get_text())