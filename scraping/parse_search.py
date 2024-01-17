import aiohttp
from bs4 import BeautifulSoup
from .sites import headers, URL_eldorado, eldorado_main, URL_stilus, stilus_main, URL_moyo, moyo_main


async def req_body(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            body = await resp.text()
            return body


async def parse_eldorado(search):
    rq_el = await req_body(URL_eldorado + search)
    bs_el = BeautifulSoup(rq_el, 'html5lib')
    try:
        good_el = bs_el.find("div", {"class": "TileBlockstyled__StyledTileBlock-sc-ogrpyx-3 "
                                              "bwJliX OfferTilestyled__StyledTileBlock-sc-1lnuwp1-0 jUUHxV"})
    except Exception as e:
        print(e)
        good_el = None
    try:
        link_el = good_el.find("a", {"class": "GoodsDescriptionstyled__StyledLinkWrapper-sc-1c1eyhs-0 gbyxYE"})["href"]
    except Exception as e:
        print(e)
        link_el = ""
    try:
        name_el = good_el.find("span", {"class": "ui-library-body2Medium-fa40 "
                                        "GoodsDescriptionstyled__StyledTypography-sc-1c1eyhs-1 bDXGew"})["title"]
    except Exception as e:
        print(e)
        name_el = search
    try:
        price_el = good_el.find("span", {"class": "ui-library-subtitle1Bold-399e"}).text + "₴"
    except Exception as e:
        print(e)
        price_el = "I'm afraid we don't have it"
    eldorado_list = ["Eldorado", eldorado_main + link_el, name_el, price_el]
    return eldorado_list


async def parse_stilus(search):
    rq_stilus = await req_body(URL_stilus + search)
    bs_stilus = BeautifulSoup(rq_stilus, 'html5lib')
    try:
        good_stilus = bs_stilus.find("a", {"class": "name-block"})
    except Exception as e:
        print(e)
        good_stilus = None
    try:
        name_stilus = good_stilus["title"]
    except Exception as e:
        print(e)
        name_stilus = search
    try:
        link_stilus = good_stilus["href"]
    except Exception as e:
        print(e)
        link_stilus = ""
    try:
        price_stilus = bs_stilus.find("div", {"class": "regular-price"}).text
    except Exception as e:
        print(e)
        price_stilus = "I'm afraid we don't have it"
    stilus_list = ["Stilus", stilus_main + link_stilus, name_stilus, price_stilus]
    return stilus_list
        
        
async def parse_moyo(search):
    rq_moyo = await req_body(URL_moyo + search)
    bs_moyo = BeautifulSoup(rq_moyo, 'html5lib')
    try:
        good_moyo = bs_moyo.find("a", {"class": "product-item_name gtm-link-product"})
    except Exception as e:
        print(e)
        good_moyo = None
    try:
        name_moyo = good_moyo.text.strip()
    except Exception as e:
        print(e)
        name_moyo = search
    try:
        link_moyo = good_moyo["href"]
    except Exception as e:
        print(e)
        link_moyo = ""
    try:
        price_moyo = bs_moyo.find("div", {"class": "product-item_price_current"}).text.strip().replace(" ", "")
    except Exception as e:
        print(e)
        price_moyo = "I'm afraid we don't have it"
    moyo_list = ["Moyo", moyo_main + link_moyo, name_moyo, price_moyo]
    return moyo_list
        
        
async def main(client_search):
    dict_goods = {
        "eldorado": await parse_eldorado(client_search),
        "Stilus": await parse_stilus(client_search),
        "Moyo": await parse_moyo(client_search)
    }
    return dict_goods
