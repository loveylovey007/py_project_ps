
ma_gifts = ["Personalized jewelry (necklace, ring, bracelet)","Customized photo frame or photo album","Love letter or handwritten note","Flower bouquet with cake","Perfume or luxury fragrance",    "Personalized shadow box","Romantic dinner date or candlelight dinner","Weekend getaway or staycation","Couple spa or massage voucher","Customized couple illustration or portrait",    "Name a star gift",    "Personalized watch","Gift hamper (chocolates, skincare, candles)","Customized mug or cushion","Memory scrapbook","Designer handbag or wallet",    "Customized home décor item",    "Engraved keepsake or showpiece","Surprise party with close family/friends","Experience gift (concert, adventure, photoshoot)"]
birth_gifts = ["Personalized jewelry","Designer handbag","Luxury perfume","Customized birthday cake","Flower bouquet","Romantic dinner date",    "Weekend getaway","Couple spa voucher","Customized photo album","Memory scrapbook","Smartwatch or fitness band","Personalized watch",    "Customized name necklace","Skincare or beauty gift hamper","Makeup kit from her favorite brand","Customized cushion or mug",    "Love letter or birthday card","Surprise birthday party","Experience gift (concert, travel, photoshoot)","Customized birthday video message"]
fbth_gifts = ["Customized name necklace","Luxury shawl or scarf","Silk saree or ethnic wear","Designer footwear","Personalized perfume",    "Skincare or wellness subscription","Fitness class or yoga membership","Cooking or hobby workshop","E-reader or favorite books set",    "Customized phone cover","Jewelry organizer box","Vanity storage box","Handwritten poem or framed quote","Customized calendar with photos",    "Indoor plants with personalized pot","Dry fruits or sweets hamper","Traditional brass or silver décor item","Home temple décor",    "Premium tea or coffee set","Personalized family photo frame","Kitchen appliance (mixer, kettle, air fryer)","Bedsheets or cushion covers set",    "Dinnerware or serving bowls","Indoor plants","Spiritual books or idols","Wall clock or home décor showpiece","Customized calendar with family photos",    "Health and wellness gift box","Religious gift hamper","Gift cards for grocery or lifestyle stores","Gift vouchers","Customized greeting card",    "Chocolates or premium sweets","Personalized mugs","Photo frame","Decorative candles","Aromatherapy set","Books","Plants"]

def print_gifts_with_serial(gifts):
    for index, gift in enumerate(gifts, start=1):
        print(f"{index}. {gift}")

def gift_for_wify(occation):
    if occation == 'marriage anniversary':
        print('Marriage Anniversary gift should be from the list :')
        print_gifts_with_serial(ma_gifts)
    elif occation == 'wifyy birthday':
        print('Birthday gift should be from the list :')
        print_gifts_with_serial(birth_gifts)
    elif occation == 'other gifts':
        print('Other gift should be from the list :')
        print_gifts_with_serial(fbth_gifts)
    else:
        print("\nInvalid occasion. Please try again.")

occation = input("Welcome to gift idea. Occation like Marriage Anniversary, Wifyy Birthday, Other Gifts. \n Enter your occation:  ").strip().lower()
gift_for_wify(occation)





