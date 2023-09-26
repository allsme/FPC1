class HashTable:
    def __init__(self):
        self.table = {}
    
    def insert(self, key, value):
        if key in self.table:
            self.table[key] += value
        else:
            self.table[key] = value
    
    def get_max_region(self):
        max_region = max(self.table.values())
        return max_region

def main():
    M, N = map(int, input().split())
    plans = [list(map(int, input().split())) for _ in range(M)]
    planets = [list(map(int, input().split())) for _ in range(N)]

    region_counter = HashTable()

    for planet in planets:
        region_key = ""
        for plan in plans:
            A, B, C, D = plan
            X, Y, Z = planet
            if A * X + B * Y + C * Z - D > 0:
                region_key += '1'
            else:
                region_key += '0'
        region_counter.insert(region_key, 1)

    max_region = region_counter.get_max_region()
    print(max_region)

if __name__ == "__main__":
    main()

