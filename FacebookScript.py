import facebook


def post_message(message):
	page_access_token = "EAAEPLWqEOzwBAFzNnAmYKg4MpYxuWdgfDeQHJO7v0pysShurMNtL1fYmDfZAq3DBlpoSXLe0i6MIFN31STJHgAFd5KK3GY1rX0AmdkQVLsnvfZABEa2i9I1HmQ1wcsHU3C48Mq2nh9mY4A6DJs0YZAmLP7XkQyd8wineS76DvoSgD16dgbXVZCshZBjNIDHgZD"
	graph = facebook.GraphAPI(page_access_token)
	facebook_page_id = "105105118382222"
	graph.put_object(facebook_page_id, "feed", message=message)


