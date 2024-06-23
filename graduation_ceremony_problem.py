
# In a university, your attendance determines whether you will be
# allowed to attend your graduation ceremony.
# You are not allowed to miss classes for four or more consecutive days.
# Your graduation ceremony is on the last day of the academic year,
# which is the Nth day.
#   Your task is to determine the following:
# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.

def attendance_probability(N):
    def count_attendance_patterns(N):
        if N == 0:
            return 1, 0

        total_ways = [0] * (N + 1)
        end_with_present = [0] * (N + 1)
        end_with_1_absent = [0] * (N + 1)
        end_with_2_absent = [0] * (N + 1)
        end_with_3_absent = [0] * (N + 1)

        total_ways[0] = 1
        end_with_present[1] = 1
        end_with_1_absent[1] = 1
        end_with_2_absent[1] = 0
        end_with_3_absent[1] = 0
        total_ways[1] = end_with_present[1] + end_with_1_absent[1]

        for day in range(2, N + 1):
            end_with_present[day] = total_ways[day - 1]
            end_with_1_absent[day] = end_with_present[day - 1]
            end_with_2_absent[day] = end_with_1_absent[day - 1]
            end_with_3_absent[day] = end_with_2_absent[day - 1]
            total_ways[day] = (end_with_present[day] + end_with_1_absent[day] + 
                               end_with_2_absent[day] + end_with_3_absent[day])
        
        miss_graduation_ways = (end_with_1_absent[N] + end_with_2_absent[N] + 
                                end_with_3_absent[N])
        
        return total_ways[N], miss_graduation_ways
    total_ways, miss_graduation_ways = count_attendance_patterns(N)
    return f"{miss_graduation_ways} / {total_ways}"


