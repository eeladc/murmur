def multi_search(keyword, page_no, page_size, *fields):
    return {
        'query': {
            'multi_match': {
                'query': keyword,
                'fields': fields
            }
        },
        'from': (page_no - 1) * page_size,
        'size': page_size
    }
