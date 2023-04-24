



from rest_framework.pagination import PageNumberPagination
#https://www.youtube.com/watch?((v=ZLmtyuGbtVw)))--> esto significa page_query_param
class SmallSetPagination(PageNumberPagination):
    page_query_param='p'
    page_size=6
    page_size_query_param ='page_size'
    max_page_size = 6



class MediumSetPagination(PageNumberPagination):
    page_query_param='p'
    page_size=9
    page_size_query_param ='page_size'
    max_page_size = 9


class LastSetPagination(PageNumberPagination):
    page_query_param='p'
    page_size=18
    page_size_query_param ='page_size'
    max_page_size = 18










    
