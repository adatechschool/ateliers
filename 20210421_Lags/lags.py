#/usr/bin/env python3

# This code is a possible implementation of the lag problem.
#
# It is quite straightforward but lacks numerous algorithm and container
# optimizations, especially in the `generate_all_client_lists` function.
# Due to its complexity, this code would badly behave with really small datasets
# (~tens of lines). Just duplicate some lines in the DATA variable to see how bad
# it is.

from copy import copy


DATA = '''Roger 0 5 10
Pongo 3 7 14
Perdita 8 10 8
Anita 16 3 7
'''

def parse_line(line):
    return line.split()

def parse(text):
    clients = []
    for line in DATA.split('\n'):
        words = parse_line(line)
        if not words:
            # manage empty lines
            continue
        clients.append(
            {
                'client': words[0],
                'start': int(words[1]),
                'duration': int(words[2]),
                'price': int(words[3])
            }
        )
    return clients

clients = parse(DATA)

# check that we got 4 clients from DATA
assert len(clients) == 4

def total_price(clients):
    total = 0
    for client in clients:
        total += client['price']
    return total

# check that the price is neatly calculated
assert total_price(clients) == 39

def check_compat(client1, client2):
    start1 = client1['start']
    end1 = start1 + client1['duration']
    start2 = client2['start']
    end2 = start2 + client2['duration']

    if (start1 <= start2 <= end1 or start2 <= start1 <= end2):
        return False
    return True

# check clients compatibility
assert not check_compat(clients[0], clients[1])
assert not check_compat(clients[1], clients[2])
assert not check_compat(clients[2], clients[3])
assert check_compat(clients[0], clients[2])
assert check_compat(clients[0], clients[3])
assert check_compat(clients[1], clients[3])
# nb: with this function check_compat, a client IS NOT compatible with itself
#     this behavior will have an impact below
assert not check_compat(clients[0], clients[0])

def generate_all_client_lists(clients):
    # brutforce algorithm: trying every combination
    # brutforces always work, but are dumb (here it checks several time the same
    # combinations and produces duplicates) and heavy resource-consuming, they
    # generaly should be avoided

    # this variable will hosts EVERY compatible client lists
    possibilities = []
    for client in clients:
        # check_compat does not think a client is compatible with itself, but
        # we know that's legit:
        possibilities.append([client])

        # checking compatibility between existing possibilities with other
        # clients ('candidate')
        for candidate in clients:

            # we use existing possibilities to generate bigger compatible
            # client lists
            for possibility in possibilities:

                compatible_with_all_existing_clients = True
                # in each possibility a new client (candidate) must be
                # compatible with every existing client
                for existing_client in possibility:
                    if not check_compat(existing_client, candidate):
                        print('Clients \'{}\' and \'{}\' are not compatible' \
                              .format(existing_client['client'], candidate['client']))
                        # the client candidate is not compatible with at least
                        # one existing client, so this possibility is no more
                        # acceptable, we break the loop
                        compatible_with_all_existing_clients = False
                        break
                if compatible_with_all_existing_clients:
                    # every 'existing_clients' of this 'possibility' list are
                    # compatible with the candidate, its a win!
                    # we can generate a new possibility (previous 'possibility'
                    # + 'candidate')

                    # we want to keep the previous 'possibility' (it's still
                    # valid!), but in Python, 'a = [5]; b = a; b.append(3)' will
                    # result in 'a == [5, 3]', so we need to use 'copy' to break
                    # the link between 'a' and 'b' (between 'possibility' and
                    # 'new_possibility')
                    new_possibility = copy(possibility)
                    new_possibility.append(candidate)
                    # finally the new possibility is added in the top-level
                    # possibilities list
                    possibilities.append(new_possibility)

    return possibilities

# for compatible_client_list in generate_all_client_lists(parse(DATA)):
#     print(compatible_client_list)

def get_most_lucrative_client_list(text):
    top_price = 0
    top_list = None
    for candidate_list in generate_all_client_lists(parse(text)):
        price = total_price(candidate_list)
        if price > top_price:
            top_price = price
            top_list = candidate_list
    return top_list


best = get_most_lucrative_client_list(DATA)
print(best)
print(total_price(best))
