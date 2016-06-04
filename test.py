__author__ = 'ps13150'
import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection as finding
from ebaysdk.soa.finditem import Connection as FindItem
from ebaysdk.shopping import Connection as Shopping
from ebaysdk.utils import getNodeText
#from ebaysdk.exception import ConnectionError


try:
    api = finding(appid='Prashant-PricePre-PRD-42f839365-6140ea4e', config_file=None)
    api_find = FindItem(debug=True,
                    appid='Prashant-PricePre-PRD-42f839365-6140ea4e',
                    config_file=None)
    for i in range(1,5,1):
        response = api.execute('findCompletedItems', {'keywords': 'Laptops Netbooks',
                                                     'paginationInput':{
                                                                    'pageNumber':str(i),
                                                                    'entriesPerPage':"100"
                                                                        }
                                                    })

        #xml = '<keywords>"Laptops Netbooks"</keywords><paginationInput><entriesPerPage>100</entriesPerPage><pageNumber>'+'2'+'</pageNumber></paginationInput>'
        #response = api.execute('findItemsAdvanced',xml)

        assert(response.reply.ack == 'Success')
        assert(type(response.reply.timestamp) == datetime.datetime)
        assert(type(response.reply.searchResult.item) == list)

        item = response.reply.searchResult.item[0]
        assert(type(item.listingInfo.endTime) == datetime.datetime)
        assert(type(response.dict()) == dict)
        size = len(response.reply.searchResult.item)
        print response.reply.paginationOutput.totalPages
        print 'Number of Items ', size
        #print 'Number of Pages'
        f = open('SearchedResult.txt','w')

        for item in response.reply.searchResult.item:
            #print(item)
            print(item.itemId)
            #records = api_find.find_items_by_ids(['391444653233'])

            #f.write(str(item))
            #f.write('\n')

except ConnectionError as e:
    print(e)
    print(e.response.dict())
