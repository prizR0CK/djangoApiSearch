import aiohttp
from bs4 import BeautifulSoup
from .sites import headers, URL_allo, URL_eldorado, eldorado_main, URL_foxtrot, foxtrot_main


async def req_body(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            body = await resp.text()
            return body


async def parse_allo(search):
    rq_allo = await req_body(URL_allo + search)
    bs_allo = BeautifulSoup(rq_allo, 'html5lib')
    try:
        good_allo = bs_allo.find("div", {"class": "products-layout__item"})

        name_a = good_allo.find("a", {"class": "product-card__title"})
        price_a = good_allo.find("div", {"class": "v-pb__cur discount"}).find("span", {"class": "sum"}).text

        allo_list = ["Allo", name_a["href"], name_a["title"], price_a + " ₴"]

        return allo_list
    except Exception as error:
        print(error)
        allo_list = ["Allo", "-", "I'm afraid we don't have it", "-"]
        return allo_list


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


async def parse_foxtrot(search):
    rq_fox = await req_body(URL_foxtrot + search)
    bs_fox = BeautifulSoup(rq_fox, 'html5lib')
    try:
        good_fox = bs_fox.find("div", {"class": "card__body"})

        name_fox = good_fox.find("a", {"class": "card__title"})
        price_fox = good_fox.find("div", {"class": "card-price"}).text.strip()

        foxtrot_list = ["Foxtrot", foxtrot_main + name_fox["href"], name_fox["title"], price_fox]
        return foxtrot_list
    except Exception as error:
        print(error)
        foxtrot_list = ["Foxtrot", "-", "I'm afraid we don't have it", "-"]
        return foxtrot_list


async def main(client_search):
    dict_goods = {"allo": await parse_allo(client_search),
                  "eldorado": await parse_eldorado(client_search),
                  "foxtrot": await parse_foxtrot(client_search)}
    return dict_goods
