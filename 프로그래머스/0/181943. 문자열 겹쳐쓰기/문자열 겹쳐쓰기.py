def solution(my_string, overwrite_string, s):
    
    answer = my_string[:s]+overwrite_string+my_string[s+len(overwrite_string):]
    return answer

print(solution("He11oWor1d", "lloWorl", 2))
print(solution("Peogarm29b8UYP", "merS123", 7))
