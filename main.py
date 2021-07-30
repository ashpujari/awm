import pymongo

promotions_list = [{"promotion_id" : "42234",
               "discount" : "10%",
               "description" : "10% less in financing"},
              {"promotion_id" : "42235",
               "discount" : "15%",
               "description" : "15% less in financing"},
              {"promotion_id" : "42236",
               "discount" : "20%",
               "description" : "20% less in financing"},
              {"promotion_id" : "42237",
               "discount" : "25%",
               "description" : "25% less in financing"},
              {"promotion_id" : "42238",
               "discount" : "30%",
               "description" : "30% less in financing"},
              {"promotion_id" : "42239",
               "discount" : "2%",
               "description" : "2% less in financing"},
              {"promotion_id" : "42240",
               "discount" : "21%",
               "description" : "21% less in financing"},
              {"promotion_id" : "42241",
               "discount" : "12%",
               "description" : "12% less in financing"},
              {"promotion_id" : "42242",
               "discount" : "16%",
               "description" : "16% less in financing"},
              {"promotion_id" : "42243",
               "discount" : "17%",
               "description" : "17% less in financing"}]


locations_list = [{"store_id" : "1002",
                    "name" : "Markham Store",
                    "address" : "325 Weston Rd, Markham, ON M6N 4Z9, Canada",
                    "phone_num" : "+14162430630",
                    "email" : "markham@awm.com"},
                   {"store_id" : "1003",
                    "name" : "Scarborough Store",
                    "address" : "60 Town Centre Court Unit 104, Scarborough, ON M1P 0B1, Canada",
                    "phone_num" : "+14167921008",
                    "email" : "scarborough@awm.com"},
                   {"store_id" : "1004",
                    "name" : "Vaughan Store",
                    "address" : "38740 Jane St, Vaughan, ON L4L 4V3, Canada",
                    "phone_num" : "+19055978225",
                    "email" : "vaughan@awm.com"},
                   {"store_id" : "1005",
                    "name" : "Brampton Store",
                    "address" : "47 Kennedy Rd N Unit 11, Brampton, ON L6V 1X6, Canada",
                    "phone_num" : "+19054572999",
                    "email" : "brampton@awm.com"},
                   {"store_id" : "1006",
                    "name" : "Ajax Store",
                    "address" : "310 Harwood Ave S, Ajax, ON L1S 2J1, Canada",
                    "phone_num" : "+19052311985",
                    "email" : "ajax@awm.com"}
                   ]

try:
    myclient = pymongo.MongoClient('mongodb://localhost:27017')

    mydb = myclient['AWM']
    promotions = mydb["promotions"]
    store_locations = mydb["store_locations"]

    promotions.insert_many(promotions_list)
    store_locations.insert_many(locations_list)



except Exception as ex:
    print(ex)


