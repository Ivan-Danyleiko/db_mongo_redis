from models import Quote


def search_quotes_by_author(name):
    quotes = Quote.objects(author__fullname=name)
    return quotes


def search_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return quotes


def search_quotes_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return quotes


def print_quotes(quotes):
    for quote in quotes:
        print(quote.to_json())


def search():
    while True:
        command = input("Enter command (name:<author_name>, tag:<tag_name>, tags:<tags_list>, exit): ")
        if command.startswith('name:'):
            author_name = command.split(':')[1].strip()
            quotes = search_quotes_by_author(author_name)
            print_quotes(quotes)
        elif command.startswith('tag:'):
            tag_name = command.split(':')[1].strip()
            quotes = search_quotes_by_tag(tag_name)
            print_quotes(quotes)
        elif command.startswith('tags:'):
            tags_list = command.split(':')[1].strip()
            quotes = search_quotes_by_tags(tags_list)
            print_quotes(quotes)
        elif command == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid command format. Please try again.")


if __name__ == "__main__":
    search()
