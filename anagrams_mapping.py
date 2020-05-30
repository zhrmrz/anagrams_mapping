class Sol:
    def anagrams_mapping(self,A,B):
        lookup = {val: i for i, val in enumerate(B)}
        return [lookup[val] for val in A]
if __name__ == '__main__':
    p=Sol()
    print(p.anagrams_mapping(A = [12, 28, 46, 32, 50] ,B = [50, 12, 32, 46, 28]))
