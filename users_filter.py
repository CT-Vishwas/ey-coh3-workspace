user_attempts = {
	"vishwas":2,
	"shruti":5,
	"John":9,
	"Riya":16,
	"Ganesh":1,
    "Arjun":16
}

# k = user_attempts.items()
# print(k)
# ---------------
# Logic 1
# v = user_attempts.values()
# print(v)
# max_val = max(user_attempts.values())
# print(max_val)

# max_failed = {}
# for k,v in user_attempts.items():
#     if v == max_val:
#         max_failed[k] = v

# print(max_failed)
# -----------------------------

# Sorting Logic Examples
# user_items = user_attempts.items()
# print(user_items)
# l1 = list(user_items)
# # l1.sort()
# l1.sort(key=lambda x: x[1])
# print(l1)

# sorted_dict = {k:v for k,v in sorted(user_attempts.items(), key=lambda item: item[1])}

# ---------------------------
# Logic 2
max_val = max(user_attempts.values())
max_users = list(filter(lambda user: user_attempts[user] == max_val, user_attempts))
print(max_users)
