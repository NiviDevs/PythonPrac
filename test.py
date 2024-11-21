
import email.utils
import re


if __name__ == '__main__':
    n = int(input())
    email_list = []
    for _ in range(n):
        _, email_id = email.utils.parseaddr(input())
        email_list.append(email_id)
        email_list.append(email.utils.parseaddr(input())[1])
    print(*email_list, sep='\n')
a = re.p

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(sum(student_marks[query_name])/3)   
s = "idk"
tuple()
email.utils.formataddr()
a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s)

# A valid email address meets the following criteria:
#
# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
# The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
# The domain and extension contain only English alphabetical characters.
# The extension is 1, 2, or 3 characters in length.

pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'



def binary_search(arr, target):
    """
    Return the index of the target if it is in the array, otherwise return -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1




# Test binary search
print(binary_search([1, 2, 3, 4, 5], 3))  # Output: 2
print(binary_search([1, 2, 3, 4, 5], 6))  # Output: -1


#binary search (array to be sorted)
# )