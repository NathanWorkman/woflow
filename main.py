import requests

all_ids = []
unique_ids = set()


def main():
    # Set start ID
    search_id = f"089ef556-dfff-4ff2-9733-654645be56fe"
    get_ids(search_id)
    print(len(unique_ids))
    print(most_frequent(all_ids))


def get_ids(search_id):
    # Set list of id's found in each node and child node
    ids = []
    # Set list of all ids
    all_ids.append(search_id)
    # Create set of unique id's
    unique_ids.add(search_id)
    r = requests.get(
        f"https://nodes-on-nodes-challenge.herokuapp.com/nodes/{search_id}"
    )
    response = r.json()

    # Traverse each response
    for obj in response:
        if isinstance(obj, dict):
            ids.append(obj.get("id"))
            children = obj.get("child_node_ids", None)
            # If child nodes are present traverse array
            if children:
                for item in children:
                    ids.append(item)
                    get_ids(item)
    return ids


def most_frequent(id_list):
    dict = {}
    count, itm = 0, ""
    for item in reversed(id_list):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return itm


if __name__ == "__main__":
    main()
