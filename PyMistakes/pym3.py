try:
    l = ["a", "b"]
    int(l[2])
except (ValueError, IndexError) as e:
    pass
