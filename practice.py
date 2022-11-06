def find_num_shortest(m,n):
    if m == 1 or n == 1:
        return  m + n
    else:
        return find_num_shortest(m,n-1) + find_num_shortest(m-1,n)



def index(keys, values, match):
    return {k:[v for v in values if match(k,v)] for k in keys}


def count_paths(t, total):
    if total == label(t):
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total-label(t)) for b in branches(t)])



def make_city(name, long, lat):
    def city_info(value):
        if value == 'name':
            return name

        elif value == 'long':
            return long

        elif value == 'lat':
            return lat
    return city_info

def get_name(city):
    return city('name')

def get_lat(city):
    return city('long')

def get_lon(city):
    return city('lat')

amc = 125

def change_amc():
    amc = 1
    return amc


class Worker:
    greeting = "Sir"
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ", I work"
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = "Peon"
    def work(self):
        print(Worker.work(self))
        return "I gather welath"

jack = Worker()
john = Bourgeoisie()
jack.greeting = "Maam"


def small_index_map(s):
    '''Indices of all elements in sequence lst with the smallest absolute value'''
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]

def small_index_filter(s):
    '''Indices of all elements in sequence lst with the smallest absolute value'''
    min_abs = min(map(abs, s))
    f = lambda i: s[i] == min_abs
    return list(filter(f, range(len(s))))
    
def largest_sum_one(s):
    '''Largest sum of the two adjecent elements in a sequence'''
    return max([s[i] + s[i+1] for i in range(len(s)-1)])

def largest_sum_two(s):
    return max([x + y for x, y in zip(s[:-1],s[1:])])

def digit_dict(s):
    dict_map = {}
    for element in s:
        digit = element % 10
        if digit not in list(dict_map.keys()):
            dict_map[digit] = [element]
        else:
            dict_map[digit].append(element)
    return {k:dict_map[k] for k in sorted(dict_map)}

def digit_dict(s):
    '''Map each digit d to the lists of elements in s that end with d'''

    return {d:[x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}

def digit_dict_two(s):
    last_digits = [x % 10 for x in s]
    return {d:[x for x in s if x % 10 == d] for d in range(10) if d in last_digits}

s = [5, 8, 13, 21, 34, 55, 89]
    
def every_equal(s):
    s = sorted(s)
    if len(s) % 2 == 1:
        return False
    while len(s) > 0:
        if s[0] == s[1]:
            s = s[2:]
        else:
            return False
    return True
        
def every_equal(s):
    for i in range(len(s)):
        if s[i] not in s[:i] + s[i+1:]:
            return False
    return True

def every_equal(s):
    return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])

def every_equal(s):
    return all([sum([1 for y in s if y == x]) > 1 for x in s])

def every_equal(s):
    return min([sum([1 for y in s if y == x]) for x in s]) > 1

def every_equal(s):
    return min([s.count(x) for x in s]) > 1


class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


s = Link(1, Link(-3, Link(-4)))
t = Link(3,Link(2,Link(4)))

def is_ordered(s, key = lambda x: x):
    if isinstance(s.rest, tuple):
        return True
    else:
        if key(s.first) > key(s.rest.first):
            return False
        return is_ordered(s.rest)

def sorted_list_create(s, t):
    if isinstance(s, tuple) and not isinstance(t, tuple):
        return t
    elif isinstance(t, tuple):
        return s
    else:
        if s.first >= t.first:
            return Link(t.first, sorted_list(s, t.rest))
        else:
            return Link(s.first, sorted_list(s.rest, t))

s = Link(1, Link(5))
t = Link(3, Link(4))

def sorted_list_mutate(s,t):
    if not isinstance(t, tuple):
        if s.first <= t.first:
            if s.rest >= t.first:
                tmp = s.rest
                s.rest = t
                sorted_list = sorted_list_mutate(s.rest, tmp)
            else:
                sorted_list = sorted_list_mutate(s.rest, t)

        else:
            if t.rest >= s.first:
                tmp = t.rest
                t.rest = s
                sorted_list = sorted_list_mutate(t.rest, tmp)
            else:
                sorted_list = sorted_list_mutate(t.rest, s)
    

