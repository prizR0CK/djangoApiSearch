import asyncio
from django.shortcuts import redirect
from scraping import parse_search, writing_to_db, views

main_loop = asyncio.new_event_loop()
asyncio.set_event_loop(main_loop)


class SaveClientsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_post = request.POST.copy()

        if 'search_query' in request_post:
            name = request_post['name']
            search_query = request_post['search_query']
            try:
                goods_list = main_loop.run_until_complete(parse_search.main(search_query))
                views.client_id = writing_to_db.write_goods_list(name, search_query, goods_list)
                return redirect('../goods')
            except Exception as e:
                print(e)

        response = self.get_response(request)
        return response
