from collections import deque

graph = {
    'you': ['Mike', 'Bob', 'Dean'],
    'Mike': ['Laura'],
    'Bob': ['John', 'Greg'],
    'Dean': ['Artur', 'Kate', 'Frank', 'Blume']
}
def search(name):
    search_queue = deque()
    print(search_queue)
    search_queue += graph[name]
    print(search_queue)
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, ' is a mango seller!')
                return True
                pass
            else:
                try:
                    search_queue += graph[person]
                    searched.append(person)
                except:
                    searched.append(person)
                    continue
    return False

def person_is_seller(name):
    return name[-2] == 'm'

print(search('you'))