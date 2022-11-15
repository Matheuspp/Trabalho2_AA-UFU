import time
def editDistance(s1, s2):
   if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    elif s1[-1] == s2[-1]:
        return editDistance(s1[:-1], s2[:-1])
    else:
        return 1 + min(
            editDistance(s1, s2[:-1]),              ## Insertion
            editDistance(s1[:-1], s2[:-1]),         ## Replacing letter
            editDistance(s1[:-1], s2)               ## Deletion
        )

if __name__ == "__main__":
    s1 = "matheus"
    s2 = "matheus"

    tic = time.time()
    totalDistance = editDistance(s1.lower(), s2.lower())

    ## Printing the result
    print("\nEdit Distance to convert " + s1 + " to " + s2 + " is: " + str(totalDistance))
    toc = time.time()
    print(f'\nRuntime: {abs(toc-tic)}')
