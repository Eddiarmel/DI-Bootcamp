## Daily Challenge : Pagination
# step1 Create the Pagination Class
import math

class Pagination:

    # Step 2 : __init__
    def __init__(self, items=None, page_size=10):
        self.items       = items if items is not None else []
        self.page_size   = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # Step 3 : get_visible_items
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end   = start + self.page_size
        return self.items[start:end]

    # Step 4 : Navigation
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} hors limites (1 à {self.total_pages})")
        self.current_idx = page_num - 1  # user = 1-based, interne = 0-based

    def first_page(self):
        self.current_idx = 0
        return self                       # permet le chaînage

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Step 5 Bonus : __str__
    def __str__(self):
        return "\n".join(self.get_visible_items())


# ── Step 6 : Tests ───────────────────────────────────────────────
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError as e:
    print(f"ValueError : {e}")
# ValueError : Page 10 hors limites (1 à 7)

try:
    p.go_to_page(0)
except ValueError as e:
    print(f"ValueError : {e}")
# ValueError : Page 0 hors limites (1 à 7)

print(str(p))
# y
# z

# ── Bonus chaînage ───────────────────────────────────────────────
p.first_page()
print(p.next_page().next_page().next_page().get_visible_items())
# ['m', 'n', 'o', 'p']