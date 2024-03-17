from typing import Any

import redis
from redis_lru import RedisLRU

from models import Author, Quote

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def find_by_tag(tag: str) -> list[str | None]:
    print(f"Find by {tag}")
    c_quotes: object = Quote.objects(tags__iregex=tag)
    result = [q.quote for q in c_quotes]
    return result


@cache
def find_by_author(author: str) -> dict[Any, list[Any]]:
    print(f"Find by {author}")
    authors = Author.objects(fullname__iregex=author)
    result = {}
    for a in authors:
        c_quotes = Quote.objects(author=a)
        result[a.fullname] = [q.quote for q in c_quotes]
    return result


if __name__ == '__main__':
    print(find_by_tag('mi'))
    print(find_by_tag('mi'))

    print(find_by_author('in'))
    print(find_by_author('in'))
    quotes = Quote.objects().all()
    print([e.to_json() for e in quotes])
