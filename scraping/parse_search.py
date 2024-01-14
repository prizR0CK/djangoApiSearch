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
        link_el = good_el.find("a", {"class": "GoodsDescriptionstyled__StyledLinkWrapper-sc-1c1eyhs-0 gbyxYE"})
        name_el = good_el.find("span", {"class": "ui-library-body2Medium-fa40 "
                                                 "GoodsDescriptionstyled__StyledTypography-sc-1c1eyhs-1 bDXGew"})
        price_el = good_el.find("span", {"class": "ui-library-subtitle1Bold-399e"})

        eldorado_list = ["Eldorado", eldorado_main + link_el["href"], name_el["title"], price_el.text + "₴"]
        return eldorado_list
    except Exception as error:
        print(error)
        eldorado_list = ["Eldorado", "-", "I'm afraid we don't have it", "-"]
        return eldorado_list


async def parse_stilus(search):
    rq_stilus = await req_body(URL_stilus + search)
    bs_stilus = BeautifulSoup(rq_stilus, 'html5lib')
    try:
        good_stilus = bs_stilus.find("a", {"class": "name-block"})
        price_stilus = bs_stilus.find("div", {"class": "regular-price"}).text
        stilus_list = ["Stilus", stilus_main + good_stilus["href"], good_stilus["title"], price_stilus]
        return stilus_list
    except Exception as error:
        print(error)
        stilus_list = ["Stilus", "-", "I'm afraid we don't have it", "-"]
        return stilus_list
        
        
async def parse_moyo(search):
    rq_moyo = await req_body(URL_moyo + search)
    bs_moyo = BeautifulSoup(rq_moyo, 'html5lib')
    try:
        good_moyo = bs_moyo.find("a", {"class": "product-item_name gtm-link-product"})
        price_moyo = bs_moyo.find("div", {"class": "product-item_price_current"}).text.strip()
        moyo_list = ["Moyo",
                     moyo_main + good_moyo["href"],
                     good_moyo.text.strip(),
                     price_moyo.replace(" ", "")]
        return moyo_list
    except Exception as error:
        print(error)
        moyo_list = ["Moyo", "-", "I'm afraid we don't have it", "-"]
        return moyo_list
        
        
async def main(client_search):
    dict_goods = {
        "eldorado": await parse_eldorado(client_search),
        "Stilus": await parse_stilus(client_search),
        "Moyo": await parse_moyo(client_search)
    }
    return dict_goods
