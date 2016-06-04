__author__ = 'prashantsaxena'

import httplib
from xml.dom.minidom import parse, parseString, Node
import ssl

devKey = "8d96b9a9-1d55-4ec0-94ae-107d67d9d14f"
appKey = "Prashant-PricePre-PRD-42f839365-6140ea4e"

certKey = "PRD-2f839365d365-be1a-4b21-8724-9eb8"
#userToken = "AgAAAA**AQAAAA**aAAAAA**005MVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDpKFpQudj6x9nY+seQ**bNQDAA**AAMAAA**HGnOvhqIT335X445Ob+myu/LtEU9E9+B/LMgA8UA98l/tcJVsymb55BQ7uljm0OXU5Ga0BVLbSs7i82UmS5VPSegxWglettH3ypfJO0+qEq/TZxqcGmBe9i+9HTq6is7FKSABt1nEqQBxHlypYKtJAtpPk048SmBX+QgkuJqS2mBh82LKvKossjGsVvWfDReaLQOHUNdmSZNyt6MBaA3VA65rSQMGaibi7592wBFzxXiLoRROxKQeVuGef9D8vqADw0b1d73A+51LnN5aYRbYd6z7tKxex9i+3lmYVF7JwJcNc7xSi9DHQQoC/HRynqZXDUcSxu9fnat2KAlFRj00h9opofJvTQHRiWuhEcPtFNQUcJ4vmB7kWHkDtbDZOP45YMLKZmbE3NTwqdjowjEF5BefXR01zpkzDyRl6l+TIST/6a4EeDeNr6jLm4NAdRbX90C04IQ5pNV8G7an4QOq3T2zM8Y/Ljs+BTOehO22Ui+8sb5BzZkj0Q7I0aaugs4ZNZws+cVO9YIhuDXy4VSG5arc/VpAeX97orDL6aG5jmvyxRFS0a8ODzyYFMjJdQAmgKreidlO7KPEfgJkMt3Bc3XpuLSwNb9yYrIM6HINlm0o68DLLXacdCRbKIRd+wSpINTg8DTMykczhVtEdns54K0a/W4J0Qm9RPjyzsCi5+fYbLnNu7GMkMRSLr+yMEjv6UHt1N6Y4imeoFTu35FM9MxpeEABkyIc3P/eDnekQPvt3gKRjFM+4bQBwmPcjnX"
userToken = "AgAAAA**AQAAAA**aAAAAA**iLxOVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6AAmYOjCpiEpAqdj6x9nY+seQ**Wk4DAA**AAMAAA**Gfjjtefj2Mgj1/sfadE8nbyHFzcn2J3ThI8VUn587aLXA7a9+qN7zs3JatnsVQG4JBUahG5PNLrIzSb4TD5Ttpx8GCzz9Fs0+ghEhd5xHKWudFQieQlNsl2MrS3elIbFHH9mXGF14cvly5wX7BBBhtfycaQudyUL0Tf2Ye3hL/CmjetDq0+rOJ2W/yh2kCxalBcwkpzg5aduhKhUT/8n5SMxo5EFOX/+bhJUEGluqX3rfN3uDPOKLoAmKaUhugwBdaQNdxL61EgonpdNMVMU5iT/QQhnbHk7VxwpIGOuN480DuL6raUvl7O+uHR28UtW9v0kj84fKzE3pworqxanfZzgq5SXGodQm3yy347DlBwivQoH7LANKT7WHVv272151FunR6lGcvKURMK1zXkWQUB/ac3V/SHWrIAsGoC+kzBpW1e2Qxd91SleErJ9TnDghxz3rwtU/hHRu7eeHxAZWmBJpLK/mxCnZ1a/H9RowLDqFiGYIN0ul6aU4wc8kLP4CAFtWP6cXwI6hYzgI7Ml+XT7g1eKIC2qvFMe2KhKmzm7eJNm2NQMgvZDryYeo/WAwybXgpAIPgXGY0iYNwpK4k7YHlnqppDe1zDq3xF1eQr+fCtsIdDYIjPIOlmrfzu3vcahvavO+DDiO5x7M0N5AIQf3TEpfA5pEOsVJuB1m1DzCP4mwJW+UjO5JSmTigOX5mdawnaX9CUfQGLg+quhwkAojxp9fFGhcNnHWapxIm4HFT8MMsv8A+3fcaNrCvFz"
serverUrl = "api.ebay.com"
#serverUrl = "open.api.ebay.com/shopping?"
#userToken =

def getHeaders(apicall, siteID="0", compatibilityLevel="433"):
    headers = {
                "X-EBAY-API-COMPATIBILITY-LEVEL":compatibilityLevel,
                "X-EBAY-API-DEV-NAME":devKey,
                "X-EBAY-API-APP-NAME" : appKey,
                "X-EBAY-API-CERT-NAME" : certKey,
                "X-EBAY-API-CALL-NAME" : apicall,
                "X-EBAY-API-SITEID" : siteID,
                "X-EBAY-API-REQUEST-ENCODING": "NV",
                "Content-Type" : "text/xml"
              }
    return headers
def findCompleteItems(query, categoryID=None, page=1):
    xml = "<?xml version='1.0' encoding='utf-8'?>"+\
             "<findCompletedItemsRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
             "<RequesterCredentials><eBayAuthToken>" +\
             userToken +\
             "</eBayAuthToken></RequesterCredentials>" + \
             "<Pagination>"+\
               "<EntriesPerPage>100</EntriesPerPage>"+\
               "<PageNumber>"+str(page)+"</PageNumber>"+\
             "</Pagination>"+\
             "<Query>" + query + "</Query>"
    if categoryID!=None:
         xml+="<CategoryID>"+str(categoryID)+"</CategoryID>"
    xml+="</findCompletedItemsRequest>"
    #return xml;
    data = sendRequest("findCompletedItems", xml)
    response = parseString(data)
    itemNodes = response.getElementsByTagName('Item');
    results = []
    for item in itemNodes:
        itemId=getSingleValue(item,'ItemID')
        print(itemId)

def findItemsByKeyWordMethod(query, categoryID=None, page=1):
    xml = "<?xml version='1.0' encoding='UTF-8'?>"+\
            "<findItemsByKeywordsRequest xmlns='http://www.ebay.com/marketplace/search/v1/services'>"+\
            "<keywords>"+query+"</keywords>"+\
            "<paginationInput>"+\
            "<entriesPerPage>"+str(2)+"</entriesPerPage>"+\
            "</paginationInput>"+\
            "</findItemsByKeywordsRequest>"
    data = sendRequest("findItemsByKeywords",xml)
    response = parseString(data)
    itemNodes = response.getElementsByTagName('Item');
    for item in itemNodes:
        itemId=getSingleValue(item,'ItemID')
        print(itemId)

def sendRequest(apicall, xmlparameters):
    #context = ssl._create_unverified_context()
    connection = httplib.HTTPSConnection(serverUrl);
    connection.request("POST", '/ws/api.dll', xmlparameters, getHeaders(apicall));
    response = connection.getresponse()
    if response.status != 200:
        print "Error Sending Request: " + response.reason
    else:
        data = response.read()
        connection.close()
    return data
def getSingleValue(node, tag):
    nl = node.getElementsByTagName(tag);
    if len(nl)>0:
        tagNode = nl[0]
    if tagNode.hasChildNodes():
        return tagNode.firstChild.nodeValue
    return '-1'

def doSearch(query,categoryID=None,page=1):
       xml = "<?xml version='1.0' encoding='utf-8'?>"+\
             "<GetSearchResultsRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
             "<RequesterCredentials><eBayAuthToken>" +\
             userToken +\
             "</eBayAuthToken></RequesterCredentials>" + \
             "<Pagination>"+\
               "<EntriesPerPage>100</EntriesPerPage>"+\
               "<PageNumber>"+str(page)+"</PageNumber>"+\
             "</Pagination>"+\
             "<Query>" + query + "</Query>"
       if categoryID!=None:
         xml+="<CategoryID>"+str(categoryID)+"</CategoryID>"
       xml+="</GetSearchResultsRequest>"

       data=sendRequest('GetSearchResults',xml)
       response = parseString(data)
       itemNodes = response.getElementsByTagName('Item');
       results = []
       for item in itemNodes:
         itemId=getSingleValue(item,'ItemID')
         itemTitle=getSingleValue(item,'Title')
         itemPrice=getSingleValue(item,'CurrentPrice')
         itemEnds=getSingleValue(item,'EndTime')
         results.append((itemId,itemTitle,itemPrice,itemEnds))
       return results

def getCategory(query='',parentID=None,siteID='0'):
    lquery=query.lower( )
    xml = "<?xml version='1.0' encoding='utf-8'?>"+\
             "<GetCategoriesRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
             "<RequesterCredentials><eBayAuthToken>" +\
             userToken +\
             "</eBayAuthToken></RequesterCredentials>"+\
             "<DetailLevel>ReturnAll</DetailLevel>"+\
             "<ViewAllNodes>true</ViewAllNodes>"+\
             "<CategorySiteID>"+siteID+"</CategorySiteID>"
    if parentID==None:
         xml+="<LevelLimit>1</LevelLimit>"
    else:
         xml+="<CategoryParent>"+str(parentID)+"</CategoryParent>"
    xml += "</GetCategoriesRequest>"
    data=sendRequest('GetCategories',xml)
    categoryList=parseString(data)
    catNodes=categoryList.getElementsByTagName('Category')

    for node in catNodes:
        catid=getSingleValue(node,'CategoryID')
        name=getSingleValue(node,'CategoryName')
        if name.lower().find(lquery)!=-1:
            print catid,name


laptops= findItemsByKeyWordMethod('Laptop')

#def sendRequest():
